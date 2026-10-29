import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "tests"))

import generate_index as gi  # noqa: E402
from summarize import DISCLAIMER_BANNER  # noqa: E402
from test_validate_summaries import DURATION, TRANSCRIPT, VID, summary_text, write_review  # noqa: E402


class Fixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "README.md").write_text(
            "# Title\n\nhand-written intro\n\n<!-- index:start -->\nold\n<!-- index:end -->\n\nhand-written outro\n",
            encoding="utf-8")

    def add_video(self, vid, date, title, tags="omega-3, mỡ máu", state="published"):
        d = self.root / "videos" / f"{date}-{vid}"
        d.mkdir(parents=True)
        (d / "metadata.json").write_text(json.dumps(
            {"video_id": vid, "title": title, "url": f"https://www.youtube.com/watch?v={vid}",
             "published_at": date, "duration": DURATION}), encoding="utf-8")
        (d / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
        if state == "pending":
            (d / "transcript.md").unlink()
            return d
        if state == "transcribed":
            return d
        (d / "summary.md").write_text(
            summary_text(tags=tags).replace(VID, vid).replace("2025-01-01", date), encoding="utf-8")
        if state in {"published", "stale"}:
            write_review(d)
        elif state in {"flag", "fail"}:
            write_review(d, verdict=state)
        if state == "stale":
            (d / "summary.stale").write_text(
                __import__("hashlib").sha256((d / "summary.md").read_bytes()).hexdigest() + "\n", encoding="utf-8")
        return d

    def run_gen(self, expect=0):
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            rc = gi.main(["--root", str(self.root)])
        self.assertEqual(rc, expect, err.getvalue())
        return err.getvalue()

    def readme(self):
        return (self.root / "README.md").read_text(encoding="utf-8")

    def snapshot(self):
        return {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}


class GenerateIndexTest(Fixture):
    def test_published_video_is_listed_with_links_and_topic_pages(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.run_gen()
        text = self.readme()
        self.assertIn("[Omega 3](videos/2025-12-06-PUB1/summary.md)", text)
        self.assertIn("[transcript](videos/2025-12-06-PUB1/transcript.md)", text)
        self.assertIn("[omega-3](topics/omega-3.md)", text)
        self.assertIn(DISCLAIMER_BANNER, text)
        self.assertIn("hand-written intro", text)
        self.assertIn("hand-written outro", text)
        page = (self.root / "topics" / "omega-3.md").read_text(encoding="utf-8")
        self.assertIn("(../videos/2025-12-06-PUB1/summary.md)", page)
        self.assertTrue((self.root / "topics" / "mo-mau.md").is_file())

    def test_unpublished_videos_appear_nowhere(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        for n, state in enumerate(["transcribed", "pending", "flag", "fail", "stale", "summarized"]):
            self.add_video(f"BAD{n}", f"2025-11-0{n + 1}", f"Chưa {n}", state=state)
        self.run_gen()
        generated = self.readme() + "".join(p.read_text(encoding="utf-8") for p in (self.root / "topics").glob("*.md"))
        self.assertIn("PUB1", generated)
        self.assertNotIn("BAD", generated)

    def test_no_vocabulary_builds_topics_from_tags(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3", tags="đường huyết")
        self.run_gen()
        self.assertTrue((self.root / "topics" / "duong-huyet.md").is_file())

    def test_zero_published_says_none_and_writes_no_topics(self):
        self.add_video("BAD", "2025-11-01", "Chưa", state="summarized")
        self.run_gen()
        self.assertIn("No videos have been published yet.", self.readme())
        self.assertFalse(list((self.root / "topics").glob("*.md")) if (self.root / "topics").exists() else [])

    def test_rerun_is_idempotent(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.add_video("PUB2", "2025-12-13", "Magie", tags="omega-3")
        self.run_gen()
        before = self.snapshot()
        self.run_gen()
        self.assertEqual(before, self.snapshot())

    def test_newest_first_and_dates_ordered(self):
        self.add_video("OLD", "2025-01-06", "Cũ")
        self.add_video("NEW", "2025-12-06", "Mới")
        self.run_gen()
        self.assertLess(self.readme().index("NEW"), self.readme().index("OLD"))

    def test_only_generated_topic_files_are_removed_and_hand_written_kept(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        topics = self.root / "topics"
        topics.mkdir()
        (topics / "vocabulary.md").write_text("omega-3\nmỡ máu\n", encoding="utf-8")
        (topics / "notes.md").write_text("hand-written\n", encoding="utf-8")
        (topics / "gone.md").write_text(gi.GENERATED + "\nold\n", encoding="utf-8")
        self.run_gen()
        self.assertFalse((topics / "gone.md").exists())
        self.assertEqual((topics / "notes.md").read_text(encoding="utf-8"), "hand-written\n")
        self.assertEqual((topics / "vocabulary.md").read_text(encoding="utf-8"), "omega-3\nmỡ máu\n")

    def test_tag_outside_vocabulary_is_unpublished(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3", tags="omega-3, lạ")
        (self.root / "topics").mkdir()
        (self.root / "topics" / "vocabulary.md").write_text("omega-3\n", encoding="utf-8")
        self.run_gen()
        self.assertNotIn("PUB1", self.readme())

    def test_vocabulary_tag_slug_never_overwrites_vocabulary_file(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3", tags="vocabulary")
        (self.root / "topics").mkdir()
        (self.root / "topics" / "vocabulary.md").write_text("vocabulary\n", encoding="utf-8")
        self.run_gen()
        self.assertEqual((self.root / "topics" / "vocabulary.md").read_text(encoding="utf-8"), "vocabulary\n")
        self.assertTrue((self.root / "topics" / "vocabulary-topic.md").is_file())

    def test_videos_directory_is_never_written(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        before = {k: v for k, v in self.snapshot().items() if "/videos/" in k}
        self.run_gen()
        self.assertEqual(before, {k: v for k, v in self.snapshot().items() if "/videos/" in k})

    def test_readme_without_markers_gets_block_appended(self):
        (self.root / "README.md").write_text("# T\n\nintro\n", encoding="utf-8")
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.run_gen()
        self.assertTrue(self.readme().startswith("# T\n\nintro\n"))
        self.assertIn(gi.INDEX_START, self.readme())
        before = self.readme()
        self.run_gen()
        self.assertEqual(before, self.readme())

    def test_missing_readme_fails_and_writes_nothing(self):
        (self.root / "README.md").unlink()
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.run_gen(expect=1)
        self.assertFalse((self.root / "topics").exists())

    def test_slugify(self):
        self.assertEqual(gi.slugify("Đường Huyết"), "duong-huyet")
        self.assertEqual(gi.slugify("vitamin D3"), "vitamin-d3")


if __name__ == "__main__":
    unittest.main()
