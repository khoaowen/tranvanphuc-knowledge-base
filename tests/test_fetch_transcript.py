import contextlib
import gzip
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import fetch_transcript  # noqa: E402

VID = "abc123"
YT_DLP_VERSION = "2026.03.17"
METADATA = {
    "id": VID,
    "title": "Số 7: Omega 3 và mỡ máu",
    "upload_date": "20251206",
    "duration": 3800,
    "webpage_url": f"https://www.youtube.com/watch?v={VID}",
}
VIDEO_DIRNAME = "2025-12-06-so-7-omega-3-va-mo-mau"
# Shaped like YouTube json3: a window-setup event (no segs), a newline-only
# append event (no dDurationMs), a speaker-change ">>" line with word offsets,
# and an event past one hour.
FIXTURE_JSON3 = json.dumps({
    "wireMagic": "pb3",
    "events": [
        {"tStartMs": 0, "dDurationMs": 3800000, "id": 1, "wpWinPosId": 1},
        {"tStartMs": 1964, "dDurationMs": 2020, "wWinId": 1, "segs": [{"utf8": "[âm nhạc]"}]},
        {"tStartMs": 7195, "wWinId": 1, "aAppend": 1, "segs": [{"utf8": "\n"}]},
        {"tStartMs": 65000, "dDurationMs": 3000, "wWinId": 1,
         "segs": [{"utf8": ">> Chào", "acAsrConf": 0}, {"utf8": " quý vị", "tOffsetMs": 400}]},
        {"tStartMs": 3723500, "dDurationMs": 1000, "wWinId": 1, "segs": [{"utf8": "Omega 3 "}]},
    ],
}, ensure_ascii=False, indent=2).encode("utf-8")
EXPECTED_TRANSCRIPT = (
    "[00:00:01] [âm nhạc]\n"
    "[00:01:05] >> Chào quý vị\n"
    "[01:02:03] Omega 3\n"
)


def fake_yt_dlp(tracks=("vi-orig", "vi"), version_exit=0):
    """Return a subprocess.run stand-in for the three yt-dlp calls fetch makes."""
    def run(cmd, **kwargs):
        if "--version" in cmd:
            out = YT_DLP_VERSION + "\n" if version_exit == 0 else ""
            return subprocess.CompletedProcess(cmd, version_exit, out, "boom")
        if "-j" in cmd:
            return subprocess.CompletedProcess(cmd, 0, json.dumps(METADATA), "")
        if "--write-auto-sub" in cmd:
            template = cmd[cmd.index("-o") + 1]
            for track in tracks:
                Path(template.replace("%(id)s", VID) + f".{track}.json3").write_bytes(FIXTURE_JSON3)
            return subprocess.CompletedProcess(cmd, 0, "", "")
        raise AssertionError(f"unexpected command {cmd}")
    return run


def run_main(*argv):
    out, err = io.StringIO(), io.StringIO()
    with mock.patch.object(sys, "argv", ["fetch_transcript.py", *argv]), \
            contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fetch_transcript.main()
    return code, out.getvalue(), err.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.videos = Path(self._tmp.name) / "videos"
        self.video_dir = self.videos / VIDEO_DIRNAME

    def tearDown(self):
        self._tmp.cleanup()

    def fetch(self, **fake_kwargs):
        with mock.patch.object(fetch_transcript.subprocess, "run", fake_yt_dlp(**fake_kwargs)):
            return run_main("--videos-dir", str(self.videos), VID)

    def provenance(self):
        return json.loads((self.video_dir / "raw" / "provenance.json").read_text(encoding="utf-8"))


class FetchWritesRawLayer(Base):
    def test_raw_file_and_provenance_written(self):
        code, _, err = self.fetch()
        self.assertEqual(code, 0, err)
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        stored = raw_path.read_bytes()
        self.assertEqual(gzip.decompress(stored), FIXTURE_JSON3)
        transcript = (self.video_dir / "transcript.md").read_bytes()
        self.assertEqual(transcript, EXPECTED_TRANSCRIPT.encode("utf-8"))

        prov = self.provenance()
        self.assertEqual(prov["video_id"], VID)
        self.assertEqual(prov["source_url"], f"https://www.youtube.com/watch?v={VID}")
        self.assertEqual(prov["track"], "vi-orig")
        self.assertEqual(prov["caption_kind"], "asr")
        self.assertRegex(prov["retrieved_at"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
        self.assertEqual(prov["raw_file"], "captions.vi-orig.json3.gz")
        self.assertEqual(prov["sha256"], hashlib.sha256(stored).hexdigest())
        self.assertEqual(prov["yt_dlp_version"], YT_DLP_VERSION)
        self.assertEqual(prov["tool"], "scripts/fetch_transcript.py")
        self.assertEqual(prov["transcript_sha256"], hashlib.sha256(transcript).hexdigest())

    def test_metadata_schema_unchanged(self):
        self.fetch()
        meta = json.loads((self.video_dir / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(set(meta), {"video_id", "title", "url", "published_at", "duration", "topics"})

    def test_gzip_is_deterministic(self):
        self.fetch()
        stored = (self.video_dir / "raw" / "captions.vi-orig.json3.gz").read_bytes()
        self.assertEqual(stored, gzip.compress(FIXTURE_JSON3, compresslevel=9, mtime=0))

    def test_vi_fallback_records_vi_track(self):
        code, _, err = self.fetch(tracks=("vi",))
        self.assertEqual(code, 0, err)
        self.assertEqual(self.provenance()["track"], "vi")
        self.assertEqual(self.provenance()["raw_file"], "captions.vi.json3.gz")
        self.assertTrue((self.video_dir / "raw" / "captions.vi.json3.gz").is_file())
        self.assertFalse((self.video_dir / "raw" / "captions.vi-orig.json3.gz").exists())

    def test_existing_video_is_not_overwritten(self):
        self.video_dir.mkdir(parents=True)
        metadata_path = self.video_dir / "metadata.json"
        transcript_path = self.video_dir / "transcript.md"
        metadata_path.write_text("original metadata\n", encoding="utf-8")
        transcript_path.write_text("original transcript\n", encoding="utf-8")
        code, _, err = self.fetch()
        self.assertEqual(code, 1)
        self.assertIn("already exists", err)
        self.assertIn("--rerender", err)
        self.assertEqual(metadata_path.read_text(encoding="utf-8"), "original metadata\n")
        self.assertEqual(transcript_path.read_text(encoding="utf-8"), "original transcript\n")
        self.assertFalse((self.video_dir / "raw").exists())

    def test_pending_completion_fails_closed_on_install_collision(self):
        self.video_dir.mkdir(parents=True)
        metadata_path = self.video_dir / "metadata.json"
        metadata_path.write_text(json.dumps({"video_id": VID}), encoding="utf-8")
        transcript_path = self.video_dir / "transcript.md"
        original_link = fetch_transcript.os.link

        def collide(source, target):
            if Path(target) == transcript_path:
                transcript_path.write_text("concurrent artifact\\n", encoding="utf-8")
            return original_link(source, target)

        with mock.patch.object(fetch_transcript.subprocess, "run", fake_yt_dlp()), \
                mock.patch.object(fetch_transcript.os, "link", side_effect=collide):
            code, _, err = run_main("--videos-dir", str(self.videos),
                                    "--complete-pending", str(self.video_dir), VID)
        self.assertEqual(code, 1)
        self.assertIn("File exists", err)
        self.assertEqual(metadata_path.read_text(encoding="utf-8"), json.dumps({"video_id": VID}))
        self.assertEqual(transcript_path.read_text(encoding="utf-8"), "concurrent artifact\\n")
        self.assertFalse((self.video_dir / "raw").exists())

    def test_raw_write_failure_leaves_no_video_directory(self):
        with mock.patch.object(fetch_transcript.subprocess, "run", fake_yt_dlp()), \
                mock.patch.object(fetch_transcript, "write_raw_captions", side_effect=OSError("disk full")):
            code, _, err = run_main("--videos-dir", str(self.videos), VID)
        self.assertEqual(code, 1)
        self.assertIn("disk full", err)
        self.assertFalse(self.video_dir.exists())

    def test_yt_dlp_version_failure_writes_nothing(self):
        code, _, err = self.fetch(version_exit=1)
        self.assertEqual(code, 1)
        self.assertIn("--version", err)
        self.assertFalse(self.video_dir.exists())


class RerenderAndCheck(Base):
    def setUp(self):
        super().setUp()
        code, _, err = self.fetch()
        self.assertEqual(code, 0, err)
        self.transcript = self.video_dir / "transcript.md"

    def test_check_passes_on_fresh_fetch(self):
        code, out, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 0, err)
        self.assertIn("ok", out)

    def test_rerender_equals_transcript(self):
        original = self.transcript.read_bytes()
        self.transcript.unlink()
        code, _, err = run_main("--rerender", str(self.video_dir))
        self.assertEqual(code, 0, err)
        self.assertEqual(self.transcript.read_bytes(), original)

    def test_check_detects_tampered_transcript(self):
        self.transcript.write_text(EXPECTED_TRANSCRIPT.replace("Omega 3", "Omega 6"), encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("differs from a re-render", err)

    def test_rerender_restores_tampered_transcript(self):
        self.transcript.write_text("edited\n", encoding="utf-8")
        self.assertEqual(run_main("--rerender", str(self.video_dir))[0], 0)
        self.assertEqual(run_main("--check", str(self.video_dir))[0], 0)
        self.assertEqual(self.transcript.read_text(encoding="utf-8"), EXPECTED_TRANSCRIPT)

    def test_check_detects_tampered_raw(self):
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        raw_path.write_bytes(gzip.compress(FIXTURE_JSON3.replace(b"Omega", b"Omegx"), mtime=0))
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("sha256 does not match", err)
        self.assertEqual(run_main("--rerender", str(self.video_dir))[0], 1)
        self.assertEqual(self.transcript.read_text(encoding="utf-8"), EXPECTED_TRANSCRIPT)

    def test_check_detects_stale_transcript_sha256(self):
        prov_path = self.video_dir / "raw" / "provenance.json"
        prov = self.provenance()
        prov["transcript_sha256"] = "0" * 64
        prov_path.write_text(json.dumps(prov), encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("transcript_sha256", err)

    def test_check_reports_truncated_gzip_without_aborting_later_dirs(self):
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        raw_path.write_bytes(gzip.compress(FIXTURE_JSON3, mtime=0)[:-8])
        prov_path = self.video_dir / "raw" / "provenance.json"
        prov = self.provenance()
        prov["sha256"] = hashlib.sha256(raw_path.read_bytes()).hexdigest()
        prov_path.write_text(json.dumps(prov), encoding="utf-8")
        other = self.videos / "other"
        other.mkdir()
        code, out, err = run_main("--check", str(self.video_dir), str(other))
        self.assertEqual(code, 1)
        self.assertIn("cannot read raw captions", err)
        self.assertIn("no raw captions", err)
        self.assertEqual(out, "")

    def test_check_reports_invalid_json(self):
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        raw_path.write_bytes(gzip.compress(b"not json", mtime=0))
        prov_path = self.video_dir / "raw" / "provenance.json"
        prov = self.provenance()
        prov["sha256"] = hashlib.sha256(raw_path.read_bytes()).hexdigest()
        prov_path.write_text(json.dumps(prov), encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("cannot read raw captions", err)

    def test_check_rejects_json_without_events_list(self):
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        raw_path.write_bytes(gzip.compress(b"{}", mtime=0))
        prov_path = self.video_dir / "raw" / "provenance.json"
        prov = self.provenance()
        prov["sha256"] = hashlib.sha256(raw_path.read_bytes()).hexdigest()
        prov_path.write_text(json.dumps(prov), encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("events list", err)

    def test_check_contains_recursion_error_during_render(self):
        with mock.patch.object(fetch_transcript, "build_transcript_lines",
                               side_effect=RecursionError("maximum recursion depth exceeded")):
            code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("maximum recursion depth exceeded", err)

    def test_check_reports_schema_malformed_json3(self):
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        malformed = json.loads(FIXTURE_JSON3)
        malformed["events"][1]["tStartMs"] = 1.5
        raw_path.write_bytes(gzip.compress(json.dumps(malformed).encode("utf-8"), mtime=0))
        prov_path = self.video_dir / "raw" / "provenance.json"
        prov = self.provenance()
        prov["sha256"] = hashlib.sha256(raw_path.read_bytes()).hexdigest()
        prov_path.write_text(json.dumps(prov), encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("cannot read raw captions", err)

    def test_check_reports_unreadable_transcript(self):
        original_read_bytes = Path.read_bytes

        def read_bytes(path):
            if path == self.transcript:
                raise OSError("permission denied")
            return original_read_bytes(path)

        with mock.patch.object(fetch_transcript.Path, "read_bytes", new=read_bytes):
            code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("cannot read transcript", err)
        self.assertNotIn("cannot read raw captions", err)

    def test_check_rejects_negative_timestamp(self):
        raw_path = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        malformed = json.loads(FIXTURE_JSON3)
        malformed["events"][1]["tStartMs"] = -1
        raw_path.write_bytes(gzip.compress(json.dumps(malformed).encode("utf-8"), mtime=0))
        prov_path = self.video_dir / "raw" / "provenance.json"
        prov = self.provenance()
        prov["sha256"] = hashlib.sha256(raw_path.read_bytes()).hexdigest()
        prov_path.write_text(json.dumps(prov), encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir))
        self.assertEqual(code, 1)
        self.assertIn("invalid tStartMs", err)

    def test_check_fails_without_raw_layer(self):
        bare = self.videos / "2024-01-01-no-raw"
        bare.mkdir()
        (bare / "transcript.md").write_text(EXPECTED_TRANSCRIPT, encoding="utf-8")
        code, _, err = run_main("--check", str(self.video_dir), str(bare))
        self.assertEqual(code, 1)
        self.assertIn("no raw captions", err)
        self.assertNotIn(str(self.video_dir) + ":", err)
        code, _, err = run_main("--rerender", str(bare))
        self.assertEqual(code, 1)
        self.assertIn("no raw captions", err)
        self.assertEqual((bare / "transcript.md").read_text(encoding="utf-8"), EXPECTED_TRANSCRIPT)

    def test_video_ids_cannot_combine_with_check(self):
        with self.assertRaises(SystemExit):
            run_main("--check", str(self.video_dir), "--videos-dir", "x", VID)

    def test_renderer_reads_plain_and_gzip_identically(self):
        plain = Path(self._tmp.name) / f"{VID}.vi-orig.json3"
        plain.write_bytes(FIXTURE_JSON3)
        gz = self.video_dir / "raw" / "captions.vi-orig.json3.gz"
        self.assertEqual(fetch_transcript.build_transcript_lines(plain),
                         fetch_transcript.build_transcript_lines(gz))


if __name__ == "__main__":
    unittest.main()
