import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "tests"))

import queue_state  # noqa: E402
import review_batch  # noqa: E402
import summarize  # noqa: E402
from test_summarize import REDUCE_OUTPUT, TRANSCRIPT  # noqa: E402


def make_video(videos, name, vid, transcript=True, summary=False):
    d = videos / name
    d.mkdir(parents=True)
    (d / "metadata.json").write_text(json.dumps({
        "video_id": vid, "title": f"T {vid}", "url": f"https://youtu.be/{vid}",
        "published_at": name[:10], "duration": 1, "topics": []}), encoding="utf-8")
    if transcript:
        (d / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
    if summary:
        (d / "summary.md").write_text("done", encoding="utf-8")
    return d


class Stub:
    def __init__(self, script=()):
        self.script = list(script)
        self.calls = 0

    def __call__(self, prompt):
        self.calls += 1
        if self.script:
            step = self.script.pop(0)
            if isinstance(step, Exception):
                raise step
        if prompt.startswith(summarize.REDUCE_INSTRUCTIONS.split("{TAG_RULE}")[0]):
            return REDUCE_OUTPUT
        return "## [00:10:00] Omega 3\n**Q: Omega 3?**\nCó thể giúp."


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.videos = self.root / "videos"
        self.videos.mkdir()
        for cmd in (["init", "-q"], ["config", "user.email", "t@t"], ["config", "user.name", "t"]):
            subprocess.run(["git", *cmd], cwd=self.root, check=True)
        (self.root / "x").write_text("x")
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "init"], cwd=self.root, check=True)
        self.logs = []

    def tearDown(self):
        self._tmp.cleanup()

    def run_batch(self, client, **kw):
        kw.setdefault("sleep", lambda s: None)
        return review_batch.run_batch(self.videos, client, self.root, log=self.logs.append, **kw)

    def commits(self):
        out = subprocess.run(["git", "log", "--format=%s"], cwd=self.root,
                             capture_output=True, text=True).stdout.split("\n")
        return [l for l in out if "review-batch" in l]


class QueueState(unittest.TestCase):
    def test_states_and_order(self):
        with tempfile.TemporaryDirectory() as t:
            v = Path(t)
            make_video(v, "2025-01-01-a", "a", summary=True)
            make_video(v, "2025-03-01-c", "c", transcript=False)
            make_video(v, "2025-02-01-b", "b")
            got = [(e["video_id"], e["state"]) for e in queue_state.list_videos(v)]
            self.assertEqual(got, [("c", "pending"), ("b", "transcribed"), ("a", "summarized")])
            self.assertEqual([e["video_id"] for e in queue_state.todo(v)], ["c", "b"])

    def test_missing_dir(self):
        self.assertEqual(queue_state.list_videos("/nonexistent/x"), [])


class Batch(Base):
    def test_happy_newest_first_commits(self):
        make_video(self.videos, "2025-01-01-a", "a")
        make_video(self.videos, "2025-02-01-b", "b")
        r = self.run_batch(Stub())
        self.assertEqual(r["done"], ["b", "a"])
        self.assertEqual(len(self.commits()), 2)
        self.assertTrue((self.videos / "2025-01-01-a/summary.md").is_file())

    def test_resume(self):
        make_video(self.videos, "2025-01-01-a", "a", summary=True)
        make_video(self.videos, "2025-02-01-b", "b")
        self.assertEqual(self.run_batch(Stub())["done"], ["b"])

    def test_pending_fetches(self):
        d = make_video(self.videos, "2025-01-01-a", "a", transcript=False)
        orig = review_batch.fetch_missing_transcript
        review_batch.fetch_missing_transcript = lambda e, vd: (d / "transcript.md").write_text(TRANSCRIPT)
        try:
            self.assertEqual(self.run_batch(Stub())["done"], ["a"])
        finally:
            review_batch.fetch_missing_transcript = orig

    def test_pending_fetch_uses_real_fetcher_and_preserves_metadata(self):
        import gzip

        d = make_video(self.videos, "2025-01-01-a", "a", transcript=False)
        metadata_path = d / "metadata.json"
        metadata_before = metadata_path.read_bytes()
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        stub = bin_dir / "yt-dlp"
        stub.write_text('''#!/usr/bin/env python3
import json, pathlib, sys
args = sys.argv[1:]
if "--version" in args:
    print("test-version")
elif "-j" in args:
    print(json.dumps({"id":"a", "title":"A title", "upload_date":"20250101",
                      "duration":120, "webpage_url":"https://youtu.be/a"}))
elif "--write-auto-sub" in args:
    template = args[args.index("-o") + 1]
    pathlib.Path(template.replace("%(id)s", "a") + ".vi-orig.json3").write_text(
        json.dumps({"events":[{"tStartMs":1000,"dDurationMs":1000,
                                 "segs":[{"utf8":"pending transcript"}]}]}))
else:
    raise SystemExit("unexpected yt-dlp args: " + repr(args))
''', encoding="utf-8")
        stub.chmod(0o755)
        with mock.patch.dict(os.environ, {"PATH": f"{bin_dir}:{os.environ['PATH']}"}):
            result = self.run_batch(Stub(), commit=False)
        self.assertEqual(result["done"], ["a"])
        self.assertEqual(metadata_path.read_bytes(), metadata_before)
        self.assertEqual((d / "transcript.md").read_text(encoding="utf-8"),
                         "[00:00:01] pending transcript\n")
        raw = d / "raw" / "captions.vi-orig.json3.gz"
        self.assertTrue(raw.is_file())
        self.assertIn(b"pending transcript", gzip.decompress(raw.read_bytes()))
        self.assertTrue((d / "raw" / "provenance.json").is_file())

    def test_pending_fetch_failure_skipped(self):
        make_video(self.videos, "2025-01-01-a", "a", transcript=False)
        make_video(self.videos, "2025-02-01-b", "b")
        orig = review_batch.fetch_missing_transcript

        def fail(entry, vd):
            raise summarize.SummarizeError("fetch failed")

        review_batch.fetch_missing_transcript = fail
        try:
            r = self.run_batch(Stub())
        finally:
            review_batch.fetch_missing_transcript = orig
        self.assertEqual(r["failed"], ["a"])
        self.assertEqual(r["done"], ["b"])

    def test_short_429_retries(self):
        make_video(self.videos, "2025-01-01-a", "a")
        stub = Stub([summarize.RateLimitError(None)])
        r = self.run_batch(stub)
        self.assertEqual(r["done"], ["a"])
        self.assertGreater(stub.calls, 2)

    def test_429_exhausted_skips(self):
        make_video(self.videos, "2025-01-01-a", "a")
        r = self.run_batch(Stub([summarize.RateLimitError(None)] * 9), max_retries=1)
        self.assertEqual(r["failed"], ["a"])
        self.assertFalse((self.videos / "2025-01-01-a/summary.md").exists())

    def test_usage_limit_stops_cleanly(self):
        make_video(self.videos, "2025-01-01-a", "a")
        make_video(self.videos, "2025-02-01-b", "b")
        # first video: map + reduce succeed; second video hits limit
        r = self.run_batch(Stub([None, None, review_batch.UsageLimitReached("resets 5pm")]))
        self.assertEqual(r["done"], ["b"])
        self.assertEqual(r["stopped_reset"], "resets 5pm")
        self.assertFalse((self.videos / "2025-01-01-a/summary.md").exists())
        self.assertEqual(len(self.commits()), 1)

    def test_bad_output_no_file(self):
        make_video(self.videos, "2025-01-01-a", "a")
        r = self.run_batch(lambda p: "garbage")
        self.assertEqual(r["failed"], ["a"])
        self.assertFalse((self.videos / "2025-01-01-a/summary.md").exists())

    def test_nothing_pending(self):
        make_video(self.videos, "2025-01-01-a", "a", summary=True)
        r = self.run_batch(Stub())
        self.assertEqual(r["done"], [])
        self.assertIn("nothing pending", self.logs[0])


class Classify(unittest.TestCase):
    def j(self, text):
        return json.dumps({"is_error": True, "result": text})

    def test_usage_limit(self):
        with self.assertRaises(review_batch.UsageLimitReached) as c:
            review_batch.classify_failure(1, self.j("You've hit your limit · resets 5pm"), "")
        self.assertIn("resets 5pm", c.exception.reset_text)

    def test_429(self):
        with self.assertRaises(summarize.RateLimitError):
            review_batch.classify_failure(1, self.j("API Error: 429 rate limit"), "")

    def test_unknown(self):
        with self.assertRaises(summarize.SummarizeError):
            review_batch.classify_failure(1, self.j("Failed to authenticate"), "")


class CliStub(Base):
    def test_claude_cmd_stub(self):
        stub = self.root / "stub.sh"
        stub.write_text("#!/bin/sh\ncat >/dev/null\necho '{\"is_error\":true,\"result\":\"limit reached, resets 9am\"}'\nexit 1\n")
        stub.chmod(0o755)
        client = review_batch.ClaudeClient(str(stub))
        with self.assertRaises(review_batch.UsageLimitReached):
            client("hi")


if __name__ == "__main__":
    unittest.main()
