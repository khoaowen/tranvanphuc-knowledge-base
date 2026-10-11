import contextlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import summarize  # noqa: E402

DISCLAIMER_FILE = (
    REPO_ROOT
    / "_bmad-output/initiative-tran-van-phuc-knowledge-base"
    / "spec-tran-van-phuc-kb/disclaimer.md"
)

SECRET = "AIzaSy-test-secret-value-123"

TRANSCRIPT = "\n".join(
    [
        "[00:00:01] [âm nhạc]",
        "[00:00:15] Chào mừng quý vị.",
        "[00:10:00] Omega 3 có thể giúp giảm triglyceride.",
        "[00:20:00] Liều dùng tùy từng trường hợp.",
        "",
    ]
)

REDUCE_OUTPUT = """TAGS: omega-3, thực phẩm bổ sung
## [00:10:00] Omega 3 và triglyceride
**Q: Omega 3 có giảm triglyceride không?**
Có thể giúp giảm triglyceride.
## [00:20:00] Liều dùng
**Q: Liều omega 3 bao nhiêu?**
Tùy từng trường hợp.

## Glossary
| Vietnamese | English | French |
|---|---|---|
| mỡ máu | blood lipids | lipides sanguins |
"""


class StubClient:
    """Records prompts; answers map prompts with sections, reduce with REDUCE_OUTPUT."""

    def __init__(self, failures=()):
        self.prompts = []
        self.failures = list(failures)

    def __call__(self, prompt):
        self.prompts.append(prompt)
        if self.failures:
            raise self.failures.pop(0)
        if prompt.startswith(summarize.REDUCE_INSTRUCTIONS.split("{TAG_RULE}")[0]):
            return REDUCE_OUTPUT
        return "## [00:10:00] Omega 3\n**Q: Omega 3?**\nCó thể giúp."


def make_video_dir(root, transcript=TRANSCRIPT):
    video_dir = Path(root) / "2025-01-01-test"
    video_dir.mkdir()
    (video_dir / "transcript.md").write_text(transcript, encoding="utf-8")
    (video_dir / "metadata.json").write_text(
        json.dumps(
            {
                "video_id": "abc123",
                "title": "Tiêu đề thử",
                "url": "https://www.youtube.com/watch?v=abc123",
                "published_at": "2025-01-01",
                "duration": 1300,
                "topics": [],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return video_dir


def run_summarize(video_dir, client, **kwargs):
    kwargs.setdefault("pace_seconds", 0)
    kwargs.setdefault("sleep", lambda seconds: None)
    kwargs.setdefault("jitter", lambda low, high: 0)
    return summarize.summarize_video(video_dir, client, **kwargs)


class ChunkingTest(unittest.TestCase):
    def test_parse_transcript_reads_seconds_and_joins_continuations(self):
        entries = summarize.parse_transcript("[00:01:05] một\ntiếp theo\n\n[01:00:00] hai\n")
        self.assertEqual(
            entries, [(65, "[00:01:05] một tiếp theo"), (3600, "[01:00:00] hai")]
        )

    def test_chunks_split_on_line_boundaries_within_budget(self):
        entries = summarize.parse_transcript(TRANSCRIPT)
        chunks = summarize.chunk_transcript(entries, 60)
        self.assertGreater(len(chunks), 1)
        self.assertEqual([e for chunk in chunks for e in chunk], entries)
        for chunk in chunks:
            self.assertLessEqual(sum(len(line) + 1 for _, line in chunk), 60)

    def test_oversized_line_gets_its_own_chunk(self):
        entries = [(0, "[00:00:00] " + "x" * 100), (1, "[00:00:01] y")]
        chunks = summarize.chunk_transcript(entries, 20)
        self.assertEqual([len(c) for c in chunks], [1, 1])

    def test_one_map_call_per_chunk_plus_reduce(self):
        with tempfile.TemporaryDirectory() as root:
            client = StubClient()
            run_summarize(make_video_dir(root), client, chunk_chars=60)
            chunks = summarize.chunk_transcript(summarize.parse_transcript(TRANSCRIPT), 60)
            self.assertEqual(len(client.prompts), len(chunks) + 1)


class HappyPathTest(unittest.TestCase):
    def test_summary_has_every_contract_element(self):
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            path = run_summarize(video_dir, StubClient())
            text = path.read_text(encoding="utf-8")

        self.assertTrue(text.startswith("# Tiêu đề thử\n"))
        for field in ("abc123", "2025-01-01", "https://www.youtube.com/watch?v=abc123"):
            self.assertIn(field, text)
        self.assertIn("**Topics:** omega-3, thực phẩm bổ sung", text)
        header, _, rest = text.partition("\n\n> ")
        self.assertTrue(rest.startswith("**Health disclaimer.**"))
        self.assertIn("https://www.youtube.com/watch?v=abc123&t=600s", text)
        self.assertIn("## [00:20:00] Liều dùng — https://www.youtube.com/watch?v=abc123&t=1200s", text)
        self.assertIn("**Q: ", text)
        self.assertIn("## Glossary", text)
        self.assertIn("Vietnamese | English | French", text)

    def test_banner_matches_disclaimer_file(self):
        if not DISCLAIMER_FILE.is_file():
            self.skipTest("disclaimer.md not present")
        quoted = [
            line
            for line in DISCLAIMER_FILE.read_text(encoding="utf-8").splitlines()
            if line.startswith("> ")
        ]
        self.assertEqual(summarize.DISCLAIMER_BANNER, "\n".join(quoted))

    def test_model_supplied_links_and_fences_are_normalized(self):
        output = (
            "```markdown\nTAGS: a, b\n"
            "## [00:00:10] Tiêu đề (https://evil.example/x)\n**Q: q?**\na\n## Glossary\n| VI | EN | FR |\n```"
        )
        tags, body = summarize.parse_reduce_output(output)
        linked = summarize.add_deep_links(body, "vid")
        self.assertEqual(tags, ["a", "b"])
        self.assertEqual(
            linked.splitlines()[0],
            "## [00:00:10] Tiêu đề — https://www.youtube.com/watch?v=vid&t=10s",
        )

    def test_malformed_reduce_output_is_rejected(self):
        with self.assertRaises(summarize.SummarizeError):
            summarize.parse_reduce_output("no tags here\n## [00:00:10] x")
        with self.assertRaises(summarize.SummarizeError):
            summarize.parse_reduce_output("TAGS: a\nno sections")
        with self.assertRaises(summarize.SummarizeError):
            summarize.parse_reduce_output("TAGS: a\n## [00:00:10] x\n**Q: q?**")
        with self.assertRaises(summarize.SummarizeError):
            summarize.parse_reduce_output("TAGS: a\n## [00:00:10] x\n## Glossary")

    def test_trailing_parenthetical_in_title_survives(self):
        out = summarize.add_deep_links("## [00:10:00] Dầu cá (fish oil)", "v")
        self.assertTrue(out.startswith("## [00:10:00] Dầu cá (fish oil) — "))


class RateLimitTest(unittest.TestCase):
    def test_429_retries_with_backoff_then_succeeds(self):
        waits = []
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            client = StubClient(failures=[summarize.RateLimitError(), summarize.RateLimitError()])
            run_summarize(video_dir, client, sleep=waits.append)
            self.assertTrue((video_dir / "summary.md").is_file())
        self.assertEqual(waits, [10.0, 20.0])

    def test_retry_after_is_honored_when_longer_than_backoff(self):
        waits = []
        client = StubClient(failures=[summarize.RateLimitError(retry_after=45)])
        summarize.call_with_retry(client, "p", sleep=waits.append, jitter=lambda a, b: 2)
        self.assertEqual(waits, [47])

    def test_jitter_is_added(self):
        waits = []
        client = StubClient(failures=[summarize.RateLimitError()])
        summarize.call_with_retry(client, "p", sleep=waits.append, jitter=lambda a, b: b)
        self.assertEqual(waits, [10.0 + summarize.BACKOFF_MAX_JITTER_SECONDS])

    def test_exhausted_retries_fail_without_writing_summary(self):
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            client = StubClient(failures=[summarize.RateLimitError()] * 10)
            with self.assertRaises(summarize.SummarizeError):
                run_summarize(video_dir, client, max_retries=2)
            self.assertEqual(len(client.prompts), 3)
            self.assertEqual(os.listdir(video_dir), ["metadata.json", "transcript.md"])

    def test_cli_exits_non_zero_on_exhausted_retries(self):
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            client = StubClient(failures=[summarize.RateLimitError()] * 10)
            with mock.patch.object(summarize.time, "sleep"):
                with contextlib.redirect_stderr(io.StringIO()):
                    code = summarize.main(
                        [str(video_dir), "--max-retries", "1", "--pace-seconds", "0"],
                        client=client,
                    )
            self.assertEqual(code, 1)
            self.assertFalse((video_dir / "summary.md").exists())


class DailyQuotaTest(unittest.TestCase):
    def test_daily_quota_stops_with_hint_and_no_file(self):
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            client = StubClient(failures=[summarize.DailyQuotaExhausted()])
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = summarize.main([str(video_dir), "--pace-seconds", "0"], client=client)
            self.assertEqual(code, 1)
            self.assertIn("resets", stderr.getvalue())
            self.assertFalse((video_dir / "summary.md").exists())
            self.assertEqual(len(client.prompts), 1)

    def test_daily_quota_detected_in_429_body(self):
        body = '{"error": {"details": [{"violations": [{"quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier"}]}]}}'
        self.assertTrue(summarize.is_daily_quota(body))
        self.assertFalse(summarize.is_daily_quota('{"quotaId": "GenerateRequestsPerMinute"}'))

    def test_retry_after_parsing(self):
        self.assertEqual(summarize.parse_retry_after("12", ""), 12.0)
        self.assertEqual(summarize.parse_retry_after(None, '"retryDelay": "34s"'), 34.0)
        self.assertIsNone(summarize.parse_retry_after(None, "{}"))


class AtomicWriteTest(unittest.TestCase):
    def test_failure_after_temp_write_keeps_existing_summary_and_removes_temp(self):
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            existing = video_dir / "summary.md"
            existing.write_text("old summary", encoding="utf-8")
            with mock.patch.object(summarize.os, "replace", side_effect=OSError("boom")):
                with self.assertRaises(OSError):
                    run_summarize(video_dir, StubClient())
            self.assertEqual(existing.read_text(encoding="utf-8"), "old summary")
            self.assertEqual(
                sorted(os.listdir(video_dir)), ["metadata.json", "summary.md", "transcript.md"]
            )

    def test_write_replaces_existing_file(self):
        with tempfile.TemporaryDirectory() as root:
            target = Path(root) / "summary.md"
            target.write_text("old", encoding="utf-8")
            summarize.write_atomic(target, "new")
            self.assertEqual(target.read_text(encoding="utf-8"), "new")
            self.assertEqual(os.listdir(root), ["summary.md"])


class VocabularyTest(unittest.TestCase):
    def test_absent_vocabulary_means_free_form_tags(self):
        with tempfile.TemporaryDirectory() as root:
            client = StubClient()
            run_summarize(
                make_video_dir(root), client, vocabulary_path=Path(root) / "missing.md"
            )
            reduce_prompt = client.prompts[-1]
        self.assertIn(summarize.TAG_RULE_FREE_FORM, reduce_prompt)
        self.assertNotIn("<vocabulary>", reduce_prompt)

    def test_present_vocabulary_is_in_reduce_prompt(self):
        with tempfile.TemporaryDirectory() as root:
            vocabulary = Path(root) / "vocabulary.md"
            vocabulary.write_text("- tim-mach\n- omega-3\n", encoding="utf-8")
            client = StubClient()
            run_summarize(make_video_dir(root), client, vocabulary_path=vocabulary)
            reduce_prompt = client.prompts[-1]
        self.assertIn("<vocabulary>", reduce_prompt)
        self.assertIn("- tim-mach", reduce_prompt)
        self.assertIn(summarize.TAG_RULE_VOCABULARY, reduce_prompt)


class SecretTest(unittest.TestCase):
    def test_missing_env_fails_before_any_call(self):
        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            stderr = io.StringIO()
            with mock.patch.dict(os.environ, {}, clear=True):
                with contextlib.redirect_stderr(stderr):
                    code = summarize.main([str(video_dir)])
            self.assertEqual(code, 2)
            self.assertIn("GEMINI_API_KEY", stderr.getvalue())
            self.assertFalse((video_dir / "summary.md").exists())

    def test_scrub_removes_secret(self):
        self.assertNotIn(SECRET, summarize.scrub(f"bad key {SECRET} here", SECRET))

    def test_http_error_text_never_contains_key(self):
        import urllib.error

        error = urllib.error.HTTPError(
            "https://x", 400, "Bad", {}, io.BytesIO(f"API key {SECRET} invalid".encode())
        )
        client = summarize.GeminiClient(SECRET, "model-x")
        with mock.patch.object(summarize.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(summarize.SummarizeError) as ctx:
                client("prompt")
        self.assertNotIn(SECRET, str(ctx.exception))

    def test_request_sends_key_in_header_not_url_and_run_output_has_no_key(self):
        captured = {}

        class FakeResponse(io.BytesIO):
            def __enter__(self):
                return self

            def __exit__(self, *exc):
                return False

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["headers"] = {k.lower(): v for k, v in request.header_items()}
            prompt = json.loads(request.data)["contents"][0]["parts"][0]["text"]
            text = REDUCE_OUTPUT if "TAGS:" in prompt else "## [00:10:00] X\n**Q: q?**\na"
            body = {
                "candidates": [{"content": {"parts": [{"text": text}]}}],
                "usageMetadata": {"totalTokenCount": 5},
            }
            return FakeResponse(json.dumps(body).encode())

        with tempfile.TemporaryDirectory() as root:
            video_dir = make_video_dir(root)
            client = summarize.GeminiClient(SECRET, "model-x")
            stderr, stdout = io.StringIO(), io.StringIO()
            with mock.patch.object(summarize.urllib.request, "urlopen", fake_urlopen):
                with contextlib.redirect_stderr(stderr), contextlib.redirect_stdout(stdout):
                    code = summarize.main([str(video_dir), "--pace-seconds", "0"], client=client)
            summary = (video_dir / "summary.md").read_text(encoding="utf-8")

        self.assertEqual(code, 0)
        self.assertNotIn(SECRET, captured["url"])
        self.assertEqual(captured["headers"]["x-goog-api-key"], SECRET)
        for output in (stderr.getvalue(), stdout.getvalue(), summary):
            self.assertNotIn(SECRET, output)
        self.assertIn("usage=", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
