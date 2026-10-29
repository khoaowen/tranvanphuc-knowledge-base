import contextlib
import io
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "tests"))

import consolidate as co  # noqa: E402
from summarize import DISCLAIMER_BANNER  # noqa: E402
from test_generate_index import Fixture  # noqa: E402


class ConsolidateTest(Fixture):
    def run_con(self, expect=0):
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            rc = co.main(["--root", str(self.root)])
        self.assertEqual(rc, expect, err.getvalue())
        return err.getvalue()

    def out(self):
        return self.root / "knowledge-gpt"

    def test_published_summary_is_copied_whole_with_disclaimer(self):
        d = self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.run_con()
        volume = (self.out() / "01-summaries.md").read_text(encoding="utf-8")
        self.assertIn((d / "summary.md").read_text(encoding="utf-8").rstrip("\n"), volume)
        for path in self.out().glob("*.md"):
            self.assertIn(DISCLAIMER_BANNER, path.read_text(encoding="utf-8"))
        self.assertIn("PUB1", (self.out() / "00-overview.md").read_text(encoding="utf-8"))

    def test_unpublished_videos_are_absent(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        for n, state in enumerate(["transcribed", "pending", "flag", "fail", "stale", "summarized"]):
            self.add_video(f"BAD{n}", f"2025-11-0{n + 1}", f"Chưa {n}", state=state)
        self.run_con()
        text = "".join(p.read_text(encoding="utf-8") for p in self.out().glob("*.md"))
        self.assertIn("PUB1", text)
        self.assertNotIn("BAD", text)
        self.assertNotIn("Đoạn nói thêm", text)  # transcript text never included

    def test_zero_published_holds_only_overview(self):
        self.add_video("BAD", "2025-11-01", "Chưa", state="summarized")
        self.run_con()
        self.assertEqual([p.name for p in self.out().glob("*")], ["00-overview.md"])
        self.assertIn("No videos have been published yet.", (self.out() / "00-overview.md").read_text(encoding="utf-8"))

    def test_rerun_is_idempotent(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.run_con()
        before = self.snapshot()
        self.run_con()
        self.assertEqual(before, self.snapshot())

    def test_packing_is_oldest_first_and_only_appends(self):
        for n in range(5):
            self.add_video(f"V{n}", f"2025-0{n + 1}-01", f"Video {n}")
        size = len((self.root / "videos" / "2025-01-01-V0" / "summary.md").read_bytes())
        cap = co.size(co.volume_header(1)) + 2 * (size + co.size(co.SEPARATOR)) + 400
        videos = co.generate_index.published_videos(self.root / "videos", self.root / "topics" / "vocabulary.md")
        volumes = co.pack(videos, cap)
        self.assertEqual([[v["video_id"] for v in vol] for vol in volumes], [["V0", "V1"], ["V2", "V3"], ["V4"]])
        more = co.pack(videos[:4], cap)
        self.assertEqual([[v["video_id"] for v in vol] for vol in more], [["V0", "V1"], ["V2", "V3"]])

    def test_overflow_by_file_count_exits_1_and_writes_nothing(self):
        for n in range(3):
            self.add_video(f"V{n}", f"2025-0{n + 1}-01", f"Video {n}")
        one = len((self.root / "videos" / "2025-01-01-V0" / "summary.md").read_bytes())
        stale = self.out()
        stale.mkdir()
        (stale / "07-old.md").write_text(co.GENERATED + "\nold\n", encoding="utf-8")
        saved = co.MAX_FILES, co.MAX_FILE_BYTES
        co.MAX_FILES, co.MAX_FILE_BYTES = 3, co.size(co.volume_header(1)) + one + co.size(co.SEPARATOR) + 50
        try:
            err = self.run_con(expect=1)
        finally:
            co.MAX_FILES, co.MAX_FILE_BYTES = saved
        self.assertIn("needs 4 files, cap is 3", err)
        self.assertTrue((stale / "07-old.md").exists())
        self.assertFalse((stale / "00-overview.md").exists())

    def test_overflow_by_single_oversize_summary_exits_1_and_writes_nothing(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        saved = co.MAX_FILE_BYTES
        co.MAX_FILE_BYTES = 1000
        try:
            err = self.run_con(expect=1)
        finally:
            co.MAX_FILE_BYTES = saved
        self.assertIn("alone needs", err)
        self.assertFalse(self.out().exists())

    def test_only_marked_generated_files_are_removed(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        self.out().mkdir()
        (self.out() / "99-old.md").write_text(co.GENERATED + "\nold\n", encoding="utf-8")
        (self.out() / "keep.md").write_text("hand-written\n", encoding="utf-8")
        self.run_con()
        self.assertFalse((self.out() / "99-old.md").exists())
        self.assertEqual((self.out() / "keep.md").read_text(encoding="utf-8"), "hand-written\n")

    def test_hand_written_readme_and_videos_untouched(self):
        self.add_video("PUB1", "2025-12-06", "Omega 3")
        before = {k: v for k, v in self.snapshot().items() if "/videos/" in k or k.endswith("README.md")}
        self.run_con()
        after = {k: v for k, v in self.snapshot().items() if "/videos/" in k or k.endswith("README.md")}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
