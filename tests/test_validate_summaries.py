import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import fidelity  # noqa: E402
import queue_state  # noqa: E402
import validate_summaries as vs  # noqa: E402
from summarize import DISCLAIMER_BANNER  # noqa: E402

VID = "abc123"
DURATION = 1500
FILLER = "\n".join(f"[00:{m:02d}:30] Đoạn nói thêm số {m} về chủ đề khác nhau của buổi nói chuyện dài." for m in range(1, 9)) * 4
TRANSCRIPT = "\n".join([
    "[00:00:15] Chào mừng quý vị.",
    "[00:10:00] Omega 3 có thể giúp giảm triglyceride.",
    "[00:20:00] Liều dùng tùy từng trường hợp.",
]) + "\n" + FILLER + "\n"


def summary_text(tags="omega-3, mỡ máu", banner=True, header_id=True, section_time="00:10:00", seconds=600,
                 q=True, glossary="| Vietnamese | English | French |", extra=""):
    parts = ["# Video thử", ""]
    if header_id:
        parts.append(f"- **Video ID:** {VID}")
    parts += ["- **Published:** 2025-01-01", f"- **URL:** https://www.youtube.com/watch?v={VID}", f"- **Topics:** {tags}", ""]
    if banner:
        parts += [DISCLAIMER_BANNER, ""]
    parts.append(f"## [{section_time}] Omega 3 — https://www.youtube.com/watch?v={VID}&t={seconds}s")
    if q:
        parts.append("**Q: Omega 3 có giảm triglyceride không?**")
    parts += ["Omega 3 có thể giúp giảm triglyceride.", "",
              f"## [00:20:00] Liều dùng — https://www.youtube.com/watch?v={VID}&t=1200s",
              "**Q: Liều bao nhiêu?**", "Liều dùng tùy từng trường hợp.", "", extra]
    if glossary:
        parts += ["## Glossary", glossary, "|---|---|---|", "| mỡ máu | blood lipids | lipides sanguins |"]
    return "\n".join(parts) + "\n"


def write_review(d, verdict="pass", digest=None):
    summary = (d / "summary.md").read_text(encoding="utf-8")
    quotes = {"Omega 3 có thể giúp giảm triglyceride.": ("giúp giảm triglyceride", "00:10:00"),
              "Liều dùng tùy từng trường hợp.": ("tùy từng trường hợp", "00:20:00")}
    claims = [{"id": c["id"], "claim": c["claim"], "status": verdict, "supported": True, "attributed": True,
               "qualifications_preserved": True, "issues": [],
               "evidence": [{"quote": quotes[c["claim"]][0], "timestamp": quotes[c["claim"]][1]}]}
              for c in fidelity.extract_claims(summary)]
    (d / "review.md").write_text(json.dumps({
        "verdict": verdict, "summary_sha256": digest or hashlib.sha256(summary.encode()).hexdigest(),
        "claims": claims, "concerns": [], "coverage_complete": True, "omissions": []}), encoding="utf-8")


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.d = self.root / "videos" / "2025-01-01-x"
        self.d.mkdir(parents=True)
        (self.d / "metadata.json").write_text(json.dumps({"video_id": VID, "duration": DURATION}), encoding="utf-8")
        (self.d / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
        self.vocab = self.root / "vocabulary.md"

    def tearDown(self):
        self._tmp.cleanup()

    def put(self, **kw):
        (self.d / "summary.md").write_text(summary_text(**kw), encoding="utf-8")

    def validate(self):
        return vs.validate_video(self.d, self.vocab)

    def assertRejected(self, fragment):
        r = self.validate()
        self.assertFalse(r["published"])
        self.assertEqual(r["state"], "summarized")
        self.assertTrue(any(fragment in x for x in r["reasons"]), r["reasons"])


class Validate(Base):
    def test_published(self):
        self.put()
        write_review(self.d)
        r = self.validate()
        self.assertEqual((r["state"], r["reasons"]), ("published", []))

    def test_missing_header_field(self):
        self.put(header_id=False)
        self.assertRejected("missing Video ID")

    def test_no_disclaimer(self):
        self.put(banner=False)
        self.assertRejected("disclaimer")

    def test_disclaimer_must_follow_header(self):
        text = summary_text(banner=False)
        text = text.replace("Omega 3 có thể giúp giảm triglyceride.", "Omega 3 có thể giúp giảm triglyceride.\n\n" + DISCLAIMER_BANNER)
        (self.d / "summary.md").write_text(text, encoding="utf-8")
        self.assertRejected("misplaced disclaimer")

    def test_no_question_line(self):
        self.put(q=False)
        self.assertRejected("no **Q:")

    def test_no_timestamp_section(self):
        (self.d / "summary.md").write_text(summary_text().replace("## [", "## ["[:3]).replace("[00:10:00]", "x").replace("[00:20:00]", "y"), encoding="utf-8")
        self.assertRejected("no timestamped topic section")

    def test_missing_link(self):
        (self.d / "summary.md").write_text(summary_text().replace(f"&t=600s", ""), encoding="utf-8")
        self.assertRejected("missing ?t= link")

    def test_glossary_missing_language(self):
        self.put(glossary="| Vietnamese | English |")
        self.assertRejected("Glossary lacks")

    def test_no_glossary(self):
        self.put(glossary="")
        self.assertRejected("missing Glossary")

    def test_all_merged_sections_are_rejected(self):
        text = summary_text()
        text = text.replace("**Q: Omega 3 có giảm triglyceride không?**\nOmega 3 có thể giúp giảm triglyceride.", "Đã gộp vào mục [00:20:00] ở trên.")
        text = text.replace("**Q: Liều bao nhiêu?**\nLiều dùng tùy từng trường hợp.", "Đã gộp vào mục [00:10:00] ở trên.")
        (self.d / "summary.md").write_text(text, encoding="utf-8")
        self.assertRejected("no question-bearing topic section")

    def test_glossary_must_follow_topics(self):
        text = summary_text().replace("## Glossary\n", "## Glossary\n## [00:25:00] Another topic — https://www.youtube.com/watch?v=abc123&t=1500s\n**Q: What else?**\nAnother answer.\n\n")
        (self.d / "summary.md").write_text(text, encoding="utf-8")
        self.assertRejected("Glossary must follow all topic sections")

    def test_invalid_minute_or_second_timestamp(self):
        text = summary_text().replace("[00:10:00]", "[00:99:00]").replace("&t=600s", "&t=5940s")
        (self.d / "summary.md").write_text(text, encoding="utf-8")
        self.assertRejected("invalid timestamp format")

    def test_merged_section_needs_no_question(self):
        text = summary_text() + ""
        text = text.replace("## Glossary", f"## [00:25:00] Gộp — https://www.youtube.com/watch?v={VID}&t=1500s\n\nĐã gộp vào mục [00:10:00] ở trên.\n\n## Glossary")
        (self.d / "summary.md").write_text(text, encoding="utf-8")
        write_review(self.d)
        self.assertEqual(self.validate()["reasons"], [])

    def test_timestamp_past_duration(self):
        (self.d / "metadata.json").write_text(json.dumps({"video_id": VID, "duration": 700}), encoding="utf-8")
        self.put()
        self.assertRejected("beyond video duration")

    def test_too_short(self):
        self.put()
        (self.d / "transcript.md").write_text(TRANSCRIPT * 40, encoding="utf-8")
        self.assertRejected("too short")

    def test_too_long(self):
        self.put(extra="x" * 20000)
        self.assertRejected("too long")

    def test_unknown_tag_with_vocab(self):
        self.vocab.write_text("# tags\n- omega-3\n", encoding="utf-8")
        self.put()
        self.assertRejected("tags outside vocabulary: mỡ máu")

    def test_known_tags_and_comma_format(self):
        self.vocab.write_text("Omega-3, MỠ MÁU\n", encoding="utf-8")
        self.put()
        write_review(self.d)
        self.assertTrue(self.validate()["published"])

    def test_no_vocab_file_skips_tags(self):
        self.put(tags="anything")
        write_review(self.d)
        self.assertTrue(self.validate()["published"])


class Strict(Base):
    def test_tag_beyond_duration_only(self):
        """Heading within duration but ?t= beyond it is still rejected."""
        (self.d / "summary.md").write_text(summary_text().replace("&t=600s", "&t=9999s"), encoding="utf-8")
        self.assertRejected("?t= beyond video duration")

    def test_t_differs_from_heading(self):
        (self.d / "summary.md").write_text(summary_text().replace("&t=600s", "&t=601s"), encoding="utf-8")
        self.assertRejected("?t= differs from heading time")

    def test_link_other_video(self):
        text = summary_text().replace(f"watch?v={VID}&t=600s", "watch?v=zzzzzzz&t=600s")
        (self.d / "summary.md").write_text(text, encoding="utf-8")
        self.assertRejected("link points at another video")

    def test_header_video_id_mismatch(self):
        (self.d / "summary.md").write_text(summary_text().replace(f"**Video ID:** {VID}", "**Video ID:** other"), encoding="utf-8")
        self.assertRejected("Video ID differs")

    def test_duration_invalid_fails_closed(self):
        self.put()
        write_review(self.d)
        for bad in (None, 0, "1500", True):
            (self.d / "metadata.json").write_text(json.dumps({"video_id": VID, "duration": bad}), encoding="utf-8")
            self.assertRejected("duration missing or invalid")

    def test_tags_nfc_normalized(self):
        import unicodedata
        self.vocab.write_text(unicodedata.normalize("NFD", "omega-3, mỡ máu\n"), encoding="utf-8")
        self.put(tags=unicodedata.normalize("NFC", "omega-3, mỡ máu"))
        write_review(self.d)
        self.assertTrue(self.validate()["published"])

    def test_unreadable_vocabulary_is_a_reason_not_a_crash(self):
        self.vocab.write_bytes(b"\xff\xfe bad")
        self.put()
        self.assertRejected("vocabulary unreadable")

    def test_review_missing_flag(self):
        self.put()
        self.assertTrue(self.validate()["review_missing"])
        self.put(banner=False)
        self.assertFalse(self.validate()["review_missing"])


class RealVideos(unittest.TestCase):
    def test_real_summaries_have_no_structural_reasons(self):
        for entry in queue_state.list_videos(REPO_ROOT / "videos"):
            if entry["state"] != queue_state.SUMMARIZED:
                continue
            r = vs.validate_video(entry["dir"], REPO_ROOT / "topics" / "vocabulary.md")
            # Tag failures against the approved vocabulary are listed for re-queue, not structural.
            structural = [x for x in r["reasons"] if not x.startswith("tags outside vocabulary")]
            self.assertEqual(structural, [], entry["dir"].name)


class Review(Base):
    def test_no_review(self):
        self.put()
        r = self.validate()
        self.assertEqual((r["state"], r["invalid"]), ("summarized", False))

    def test_flag_and_fail(self):
        self.put()
        for verdict in ("flag", "fail"):
            write_review(self.d, verdict)
            self.assertFalse(self.validate()["published"], verdict)

    def test_hash_mismatch(self):
        self.put()
        write_review(self.d, digest="0" * 64)
        self.assertFalse(self.validate()["published"])

    def test_review_of_older_bytes(self):
        self.put()
        write_review(self.d)
        self.put(tags="omega-3")
        self.assertFalse(self.validate()["published"])


class Stale(Base):
    def test_stale_blocks_matching_pass_review(self):
        self.put()
        write_review(self.d)
        before = (self.d / "summary.md").read_bytes()
        vs.mark_stale(self.d)
        self.assertEqual((self.d / "summary.md").read_bytes(), before)
        self.assertRejected("stale")

    def test_regenerated_summary_clears_marker(self):
        self.put()
        vs.mark_stale(self.d)
        self.put(tags="omega-3")  # different bytes -> marker no longer applies
        self.assertEqual(self.validate()["reasons"], ["no passing review bound to this summary"])
        write_review(self.d)
        self.assertTrue(self.validate()["published"])


class Cli(Base):
    def run_cli(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = vs.main(["--videos-dir", str(self.root / "videos"), "--vocabulary", str(self.vocab), *args])
        return code, out.getvalue()

    def test_exit_codes_and_lines(self):
        self.put()
        write_review(self.d)
        self.assertEqual(self.run_cli(), (0, "2025-01-01-x: published\n"))
        self.put(banner=False)
        code, out = self.run_cli()
        self.assertEqual(code, 1)
        self.assertIn("disclaimer", out)

    def test_unreviewed_is_not_ci_failure(self):
        self.put()
        self.assertEqual(self.run_cli()[0], 0)

    def test_mark_stale_cli(self):
        self.put()
        write_review(self.d)
        before = (self.d / "summary.md").read_bytes()
        self.assertEqual(self.run_cli("--mark-stale", VID)[0], 0)
        self.assertEqual((self.d / "summary.md").read_bytes(), before)
        self.assertEqual(self.run_cli()[0], 1)

    def test_transcript_changed_aborts(self):
        self.put()
        original = vs.check_summary

        def tamper(video_dir, vocabulary):
            (self.d / "transcript.md").write_text("changed", encoding="utf-8")
            return original(video_dir, vocabulary)
        vs.check_summary = tamper
        try:
            self.assertEqual(self.run_cli()[0], 2)
        finally:
            vs.check_summary = original

    def test_mark_stale_duplicate_video_id_is_rejected(self):
        self.put()
        other = self.root / "videos" / "2025-01-02-y"
        other.mkdir(parents=True)
        (other / "metadata.json").write_text(json.dumps({"video_id": VID, "duration": DURATION}), encoding="utf-8")
        (other / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
        (other / "summary.md").write_text(summary_text(), encoding="utf-8")
        code, _ = self.run_cli("--mark-stale", VID)
        self.assertEqual(code, 1)
        self.assertFalse((self.d / "summary.stale").exists())
        self.assertFalse((other / "summary.stale").exists())

    def test_mark_stale_missing_video(self):
        self.put()
        self.assertEqual(self.run_cli("--mark-stale", "nope")[0], 1)
        self.assertFalse((self.d / "summary.stale").exists())

    def test_non_summarized_videos_listed(self):
        self.assertEqual(self.run_cli(), (0, "2025-01-01-x: transcribed\n"))


if __name__ == "__main__":
    unittest.main()
