"""End-to-end run of the pipeline against q7uDJG8YQ5c, fully offline.

Real code paths: weekly_sync (detect -> fetch files -> summarize -> validate -> generate ->
commit -> push to a local bare remote), summarize, validate_summaries, review_summaries,
review_batch, generate_index and consolidate. Stubbed seams only: the channel listing, the
yt-dlp fetch, the Gemini client, and the `claude -p` command. No network, no secrets.

Done-when items (epic-video-knowledge-pipeline) checked in order:
  1 detection identifies known vs new videos;   2 transcript + metadata + valid, shorter summary;
  3 README/topics reach the video in <= 2 clicks, disclaimer present;   4 knowledge-gpt/ within caps;
  and: an invalid summary stays queued; pipeline state is derived from files.
The GPT Builder check (docs/custom-gpt-setup.md) is manual and is deliberately not run here.
"""

import contextlib
import io
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import consolidate  # noqa: E402
import fetch_transcript  # noqa: E402
import queue_state  # noqa: E402
import review_batch  # noqa: E402
import review_summaries  # noqa: E402
import scan_secrets  # noqa: E402
import summarize  # noqa: E402
import validate_summaries  # noqa: E402
import weekly_sync  # noqa: E402
from summarize import DISCLAIMER_BANNER  # noqa: E402

VID = "q7uDJG8YQ5c"
KNOWN = "KNOWN000001"
BAD = "BADSUMM0001"
BACKLOG = "BACKLOG0001"
DURATION = 1500
TITLES = {VID: "Những mẹo chọn thực phẩm bổ sung Omega 3", KNOWN: "Video đã có", BAD: "Video tóm tắt lỗi",
          BACKLOG: "Video tồn đọng"}
DATES = {VID: "20251206", KNOWN: "20250101", BAD: "20251213", BACKLOG: "20251101"}

FILLER = "\n".join(f"[00:{m:02d}:30] Đoạn nói thêm số {m} về chủ đề khác nhau của buổi nói chuyện dài."
                   for m in range(1, 9)) * 4
TRANSCRIPT_LINES = (["[00:00:15] Chào mừng quý vị."]
                    + ["[00:10:00] Omega 3 có thể giúp giảm triglyceride."]
                    + ["[00:20:00] Liều dùng tùy từng trường hợp."]
                    + FILLER.splitlines())

MAP_OUTPUT = "## [00:10:00] Omega 3\n**Q: Omega 3?**\nCó thể giúp giảm triglyceride."
REDUCE_OK = """TAGS: omega-3, mỡ máu
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
REDUCE_BAD = REDUCE_OK.replace("## Glossary", "## Notes")  # missing Glossary: fails validation


def sh(cwd, *args):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, check=True).stdout


def metadata(video_id):
    return {"id": video_id, "title": TITLES[video_id], "upload_date": DATES[video_id], "duration": DURATION,
            "webpage_url": f"https://www.youtube.com/watch?v={video_id}"}


def stub_model(reduce_output):
    """Stub of Gemini / `claude -p`: map prompts get a section, the reduce prompt gets reduce_output."""
    def client(prompt):
        return reduce_output if "TAGS:" in prompt else MAP_OUTPUT
    client.last_usage = None
    return client


def stub_reviewer(prompt):
    """Stub reviewer: quotes, per claim, the transcript line sharing the most words with it."""
    if "final whole-summary coverage auditor" in prompt:
        return json.dumps({"coverage_complete": True, "omissions": []})
    claims_part, transcript_part = prompt.split("<timestamped_transcript>")
    lines = [re.sub(r"^\[[\d:]+\]\s*", "", line) for line in transcript_part.splitlines()
             if re.match(r"^\[\d\d:\d\d:\d\d\]", line)]
    out = []
    for cid, claim in re.findall(r"^\[(c\d+)\]\s*(.+)$", claims_part, re.M):
        words = set(claim.lower().strip(".").split())
        best = max(lines, key=lambda line: len(words & set(line.lower().split())))
        out.append({"id": cid, "status": "in_slice", "supported": True, "attributed": True,
                    "qualifications_preserved": True, "contradicts": False, "finding": "",
                    "quote": best, "support_scope": "full"})
    return json.dumps({"claims": out, "concerns": [], "omitted_topics": []}, ensure_ascii=False)


class EndToEnd(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        self.remote = self.tmp / "remote.git"
        sh(self.tmp, "init", "--bare", "-b", "main", str(self.remote))
        self.repo = self.tmp / "work"
        sh(self.tmp, "clone", "-q", str(self.remote), str(self.repo))
        sh(self.repo, "config", "user.name", "Fixture")
        sh(self.repo, "config", "user.email", "fixture@example.invalid")
        (self.repo / "README.md").write_text(
            "# Fixture\n\n<!-- index:start -->\n<!-- index:end -->\n", encoding="utf-8")
        self.videos = self.repo / "videos"
        known = fetch_transcript.write_video_files(self.videos, metadata(KNOWN), TRANSCRIPT_LINES)
        summarize.summarize_video(known, stub_model(REDUCE_OK), pace_seconds=0)
        review_summaries.review_video(known, stub_reviewer)  # an already published video
        self.known_rel = f"videos/{known.name}"
        sh(self.repo, "add", "-A")
        sh(self.repo, "commit", "-q", "-m", "initial")
        sh(self.repo, "push", "-q", "-u", "origin", "HEAD:main")
        sh(self.repo, "branch", "-M", "main")

        self.channel = [VID, KNOWN]
        self.calls = {"fetch": [], "gemini": 0}
        self.report = self.tmp / "report.json"

    def deps(self, reduce_output=REDUCE_OK):
        gemini = stub_model(reduce_output)

        def counting(prompt):
            self.calls["gemini"] += 1
            return gemini(prompt)
        counting.last_usage = None

        def fetch_one(video_id, videos_dir):
            self.calls["fetch"].append(video_id)
            video_dir = fetch_transcript.write_video_files(videos_dir, metadata(video_id), TRANSCRIPT_LINES)
            fetch_transcript.write_raw_captions(video_dir, video_id, "vi", b'{"events": []}',
                                                "2026-01-01T00:00:00Z", "e2e")
            return video_dir

        deps = weekly_sync.Deps(repo=self.repo)
        deps.channel_ids = lambda channel_id: list(self.channel)
        deps.fetch_metadata = lambda video_id: metadata(video_id)
        deps.fetch_one = fetch_one
        deps.make_client = lambda key, model: counting
        deps.run_tests = lambda: True  # the suite is already what is running
        deps.scan_index = lambda: scan_secrets.Result("index", "clean", sh(self.repo, "write-tree").strip())
        deps.scan_commit = lambda commit: scan_secrets.Result("commit", "clean", commit)
        deps.log = lambda message: None
        return deps

    def sync(self, deps):
        env = {"GEMINI_API_KEY": "stub-key", "GEMINI_MODEL": "stub-model"}
        with mock.patch.dict(os.environ, env), contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            os.environ.pop("GITHUB_STEP_SUMMARY", None)
            rc = weekly_sync.main(["all", "--report", str(self.report)], deps=deps)
        return rc, json.loads(self.report.read_text(encoding="utf-8"))

    def vdir(self, video_id):
        return next(d["dir"] for d in queue_state.list_videos(self.videos) if d["video_id"] == video_id)

    def review(self):
        """Local fidelity review of every summarized video that has no current review."""
        return review_summaries.run_batch(self.videos, stub_reviewer, self.repo, commit=False,
                                          log=lambda m: None)

    # --- the single-pass run -------------------------------------------------

    def test_pipeline_end_to_end_for_q7uDJG8YQ5c(self):
        # Done-when 1: a known video is recognised, the genuinely new one is selected and fetched alone.
        rc, state = self.sync(self.deps())
        self.assertEqual(rc, 0, state)
        self.assertEqual(state["unseen"], [VID])
        self.assertEqual(state["selected"], VID)
        self.assertEqual(self.calls["fetch"], [VID])
        self.assertEqual(self.calls["gemini"], 2)  # one map chunk + reduce, no real network

        # Done-when 2: transcript, metadata and a valid, materially shorter, tagged, timestamped summary.
        d = self.vdir(VID)
        self.assertEqual(sorted(p.name for p in d.iterdir()), ["metadata.json", "raw", "summary.md", "transcript.md"])
        meta = json.loads((d / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual((meta["video_id"], meta["duration"]), (VID, DURATION))
        transcript = (d / "transcript.md").read_text(encoding="utf-8")
        summary = (d / "summary.md").read_text(encoding="utf-8")
        self.assertLess(len(summary), len(transcript))
        self.assertIn("omega-3", summary)
        self.assertRegex(summary, rf"watch\?v={VID}&t=600s")
        self.assertIn(DISCLAIMER_BANNER, summary)
        result = validate_summaries.validate_video(d, None)
        self.assertFalse(result["invalid"], result)

        # The CI video is committed but unpublished until the local fidelity review passes.
        self.assertFalse(result["published"])
        self.assertEqual(state["report"]["published"], [self.known_rel])
        self.assertEqual(sh(self.repo, "rev-parse", "HEAD"), sh(self.remote, "rev-parse", "main"))
        gpt_text = "".join(p.read_text(encoding="utf-8") for p in (self.repo / "knowledge-gpt").glob("*.md"))
        self.assertNotIn(VID, gpt_text)
        self.assertNotIn(d.name, (self.repo / "README.md").read_text(encoding="utf-8"))
        self.assertEqual(queue_state.video_state(d), queue_state.SUMMARIZED)

        # Local review gate (stubbed reviewer), then the next run publishes.
        self.assertEqual(self.review()["done"], [VID])
        self.assertTrue(queue_state.publishable(d))
        sh(self.repo, "add", "-A")
        sh(self.repo, "commit", "-q", "-m", "review")
        self.channel = [VID, KNOWN]
        rc, state = self.sync(self.deps())
        self.assertEqual(rc, 0, state)
        self.assertEqual(state["report"]["published"], sorted([self.known_rel, f"videos/{d.name}"]))
        self.assertEqual(sh(self.repo, "rev-parse", "HEAD"), sh(self.remote, "rev-parse", "main"))

        # Done-when 3: README -> topic page -> video files, two clicks; disclaimer on health content.
        readme = (self.repo / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"videos/{d.name}", readme)  # click 1: README links the video
        topic = (self.repo / "topics" / "omega-3.md").read_text(encoding="utf-8")
        self.assertIn(f"videos/{d.name}", topic)
        self.assertIn("topics/omega-3.md", readme)  # click 1 -> topic page, click 2 -> video
        self.assertIn(DISCLAIMER_BANNER, readme)
        self.assertIn(DISCLAIMER_BANNER, topic)

        # Done-when 4: knowledge-gpt/ within the file-count and per-file size caps.
        files = sorted((self.repo / "knowledge-gpt").glob("*.md"))
        self.assertTrue(files)
        self.assertLessEqual(len(files), consolidate.MAX_FILES)
        for path in files:
            self.assertLessEqual(path.stat().st_size, consolidate.MAX_FILE_BYTES)
        self.assertIn(VID, "".join(p.read_text(encoding="utf-8") for p in files))

        # Idempotent: a further run with no new video changes nothing.
        head = sh(self.repo, "rev-parse", "HEAD")
        self.channel = [VID, KNOWN]
        rc, _ = self.sync(self.deps())
        self.assertEqual(rc, 0)
        self.assertEqual(sh(self.repo, "rev-parse", "HEAD"), head)
        self.assertEqual(self.calls["fetch"], [VID])

    def test_invalid_summary_stays_queued_and_unpublished(self):
        self.channel = [BAD, KNOWN]
        rc, state = self.sync(self.deps(REDUCE_BAD))
        self.assertEqual(rc, 1, state)
        d = self.vdir(BAD)
        self.assertFalse((d / "summary.md").exists())  # rejected output is not kept
        self.assertEqual(queue_state.video_state(d), queue_state.TRANSCRIBED)  # still queued
        self.assertEqual(state["report"]["published"], [self.known_rel])  # only the pre-existing one
        self.assertEqual([e["video_id"] for e in queue_state.todo(self.videos)], [BAD])
        self.assertTrue(any(BAD in f for f in state["failures"]), state["failures"])

    def test_backlog_is_queued_then_summarized_locally_via_stubbed_claude(self):
        self.channel = [VID, BACKLOG, KNOWN]
        rc, state = self.sync(self.deps())
        self.assertEqual(rc, 0, state)
        self.assertEqual(state["pending"], [BACKLOG])
        backlog = self.vdir(BACKLOG)
        self.assertEqual(queue_state.video_state(backlog), queue_state.PENDING)  # metadata only, never fetched
        self.assertEqual(self.calls["fetch"], [VID])

        # Give the backlog video its transcript (the network fetch is the one seam not run here),
        # then summarize it through the real ClaudeClient against a stub `claude` executable.
        (backlog / "transcript.md").write_bytes(fetch_transcript.render_transcript(TRANSCRIPT_LINES).encode())
        self.assertEqual(queue_state.video_state(backlog), queue_state.TRANSCRIBED)
        stub = self.tmp / "claude-stub"
        stub.write_text("#!/usr/bin/env python3\nimport json, sys\nprompt = sys.stdin.read()\n"
                        f"print(json.dumps({{'result': {REDUCE_OK!r} if 'TAGS:' in prompt else {MAP_OUTPUT!r}}}))\n",
                        encoding="utf-8")
        stub.chmod(stub.stat().st_mode | stat.S_IEXEC)
        client = review_batch.ClaudeClient(f"{sys.executable} {stub}", "sonnet")
        with mock.patch.object(summarize, "default_vocabulary_path", lambda: None):
            result = review_batch.run_batch(self.videos, client, self.repo, commit=False, log=lambda m: None)
        self.assertEqual(result["done"], [BACKLOG])
        self.assertEqual(queue_state.video_state(backlog), queue_state.SUMMARIZED)
        self.assertFalse(validate_summaries.validate_video(backlog, None)["invalid"])


if __name__ == "__main__":
    unittest.main()
