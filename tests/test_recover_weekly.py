"""Offline tests for scripts/recover_weekly.py on real temporary Git repositories."""

import gzip
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "tests"))

import fetch_transcript  # noqa: E402
import recover_weekly  # noqa: E402
import weekly_sync  # noqa: E402
from test_fetch_transcript import FIXTURE_JSON3  # noqa: E402

SELECTED = "s2cOsPTA_Ek"
PENDING = ["Pend0000001", "Pend0000002", "Pend0000003"]
KNOWN = "Known000001"


def sh(cwd, *args):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True,
                          check=True).stdout


def meta(video_id, title=None, date="20261020"):
    return {"id": video_id, "title": title or f"Video {video_id}", "upload_date": date,
            "duration": 1234, "webpage_url": f"https://www.youtube.com/watch?v={video_id}"}


class RecoverWeeklyTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        self.repo = self.tmp / "repo"
        self.repo.mkdir()
        self.runs = self.tmp / "state" / "runs"
        sh(self.repo, "init", "-q", "-b", "feature")
        sh(self.repo, "config", "user.name", "Fixture")
        sh(self.repo, "config", "user.email", "fixture@example.invalid")
        self.videos = self.repo / "videos"
        fetch_transcript.write_pending_metadata(self.videos, meta(KNOWN, date="20250101"))
        (self.repo / "README.md").write_text("fixture\n", encoding="utf-8")
        (self.repo / ".gitignore").write_text(".DS_Store\n", encoding="utf-8")
        sh(self.repo, "add", "-A")
        sh(self.repo, "commit", "-q", "-m", "initial")
        self.head = sh(self.repo, "rev-parse", "HEAD").strip()
        self.selected_dir = self.fetch(SELECTED, title="Số 7: Omega 3", date="20261028")
        self.pending_dirs = [fetch_transcript.write_pending_metadata(
            self.videos, meta(video_id, date=f"2026102{i}"), expected_id=video_id)
            for i, video_id in enumerate(PENDING)]

    def fetch(self, video_id, title=None, date="20261020", raw=FIXTURE_JSON3):
        """Create a fetch result exactly as fetch_one_video writes it (no network)."""
        metadata = meta(video_id, title, date)
        source = self.tmp / f"{video_id}.json3"
        source.write_bytes(raw)
        try:
            lines = fetch_transcript.build_transcript_lines(source)
        except ValueError:
            lines = []
        video_dir = fetch_transcript.write_video_files(self.videos, metadata, lines)
        fetch_transcript.write_raw_captions(video_dir, video_id, "vi-orig", raw,
                                            "2026-10-28T10:00:00Z", "2026.03.17")
        return video_dir

    def snapshot(self):
        return {str(p.relative_to(self.repo)): (p.read_bytes() if p.is_file() else None)
                for p in sorted(self.repo.rglob("*")) if ".git" not in p.parts}

    def assert_rejected(self, pattern):
        before = self.snapshot()
        with self.assertRaisesRegex(recover_weekly.RecoveryError, pattern):
            recover_weekly.inspect_inventory(self.repo)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse(self.runs.exists())

    def write_json(self, path, data):
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # --- accepted inventory ---

    def test_valid_inventory_is_inspected_read_only(self):
        before = self.snapshot()
        inventory = recover_weekly.inspect_inventory(self.repo)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(inventory["selected"], {"video_id": SELECTED,
                                                 "dir": f"videos/{self.selected_dir.name}"})
        self.assertEqual(sorted(i["video_id"] for i in inventory["pending"]), sorted(PENDING))
        self.assertEqual([i["dir"] for i in inventory["pending"]],
                         sorted((i["dir"] for i in inventory["pending"]), reverse=True))
        self.assertEqual((inventory["head"], inventory["branch"]), (self.head, "feature"))
        self.assertEqual(len(inventory["files"]), 4 + len(PENDING))

    def test_confirmed_recovery_saves_labelled_durable_state_outside_repo(self):
        inventory = recover_weekly.inspect_inventory(self.repo)
        before = self.snapshot()
        evidence = recover_weekly.save_recovered_evidence(self.repo, self.runs, inventory)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(evidence.parent, self.runs.resolve())
        self.assertEqual((evidence / "before.sha").read_text(), self.head + "\n")
        state = weekly_sync.load_state(evidence / "report.json")
        self.assertIsNotNone(state)
        self.assertEqual(state["selected"], SELECTED)
        self.assertEqual(sorted(state["pending"]), sorted(PENDING))
        self.assertEqual(len(state["pending"]), len(PENDING))
        self.assertEqual((state["failures"], state["fatal"]), ([], []))
        self.assertEqual(state["unseen"], [])
        self.assertNotIn("report", state)
        recovery = state["recovery"]
        self.assertEqual(recovery["kind"], "local-artifact-recovery")
        self.assertEqual((recovery["head"], recovery["branch"]), (self.head, "feature"))
        self.assertIn("replacement", recovery["baseline"])
        self.assertEqual(recovery["inventory_sha256"], inventory["inventory_sha256"])
        self.assertTrue(any("lost" in caveat for caveat in recovery["caveats"]))
        self.assertRegex(recovery["recovered_at"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
        # Finalize would stage exactly the verified fetch result and pending metadata.
        deps = weekly_sync.Deps(repo=self.repo)
        allowlist = weekly_sync.build_allowlist(deps, state, {}, [])
        self.assertEqual(allowlist, sorted(inventory["files"]))

    def test_recovery_never_reaches_network_or_gemini_seams(self):
        def forbidden(*args, **kwargs):
            raise AssertionError("recovery must not fetch, detect or call Gemini")
        with mock.patch.object(fetch_transcript, "fetch_metadata", forbidden), \
                mock.patch.object(fetch_transcript, "fetch_caption_json3", forbidden), \
                mock.patch.object(fetch_transcript, "yt_dlp_version", forbidden), \
                mock.patch.object(recover_weekly.detect_new_videos, "get_channel_video_ids", forbidden), \
                mock.patch.object(weekly_sync.summarize, "GeminiClient", forbidden):
            inventory = recover_weekly.inspect_inventory(self.repo)
            recover_weekly.save_recovered_evidence(self.repo, self.runs, inventory)
        self.assertEqual(sh(self.repo, "rev-parse", "HEAD").strip(), self.head)
        self.assertEqual(sh(self.repo, "diff", "--cached", "--name-only"), "")

    def test_recovered_state_summarizes_only_the_selected_video(self):
        inventory = recover_weekly.inspect_inventory(self.repo)
        evidence = recover_weekly.save_recovered_evidence(self.repo, self.runs, inventory)
        deps = weekly_sync.Deps(repo=self.repo)
        summarized = []
        deps.make_client = lambda key, model: object()
        deps.summarize = lambda video_dir, client, **kwargs: summarized.append(Path(video_dir).name)
        deps.validate = lambda video_dir, vocab: {"invalid": False, "reasons": []}
        env = {"GEMINI_API_KEY": "k", "GEMINI_MODEL": "m"}
        with mock.patch.dict(os.environ, env):
            rc = weekly_sync.main(["summarize", "--report", str(evidence / "report.json")], deps=deps)
        self.assertEqual(rc, 0)
        self.assertEqual(summarized, [self.selected_dir.name])

    def test_inventory_changed_after_inspection_is_not_adopted(self):
        inventory = recover_weekly.inspect_inventory(self.repo)
        fetch_transcript.write_pending_metadata(self.videos, meta("Late0000001"))
        with self.assertRaisesRegex(recover_weekly.RecoveryError, "changed after inspection"):
            recover_weekly.save_recovered_evidence(self.repo, self.runs, inventory)
        self.assertFalse(self.runs.exists())

    def test_evidence_inside_repository_is_refused(self):
        inventory = recover_weekly.inspect_inventory(self.repo)
        with self.assertRaisesRegex(recover_weekly.RecoveryError, "outside the repository"):
            recover_weekly.save_recovered_evidence(self.repo, self.repo / ".git" / "runs", inventory)
        self.assertFalse((self.repo / ".git" / "runs").exists())

    # --- unsafe inventory ---

    def test_staged_work_is_refused(self):
        sh(self.repo, "add", "--", f"videos/{self.pending_dirs[0].name}/metadata.json")
        self.assert_rejected("Staged work")

    def test_modified_tracked_file_is_refused(self):
        (self.repo / "README.md").write_text("changed\n", encoding="utf-8")
        self.assert_rejected("Tracked files are modified")

    def test_unrelated_untracked_file_is_refused(self):
        for path in ("notes.txt", "videos/loose.txt", "videos/.fetch-x/metadata.json",
                     f"videos/{self.pending_dirs[0].name}/extra/file"):
            with self.subTest(path=path):
                target = self.repo / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("x", encoding="utf-8")
                self.assert_rejected("Unrelated untracked")
                target.unlink()

    def test_untracked_file_inside_tracked_folder_is_refused(self):
        known = next(p for p in self.videos.iterdir() if KNOWN.lower() in p.name)
        (known / "summary.md").write_text("x", encoding="utf-8")
        self.assert_rejected("inside tracked folder")

    def test_symlinks_are_refused(self):
        target = self.pending_dirs[0] / "metadata.json"
        moved = self.tmp / "outside.json"
        target.rename(moved)
        target.symlink_to(moved)
        self.assert_rejected("symlink")
        target.unlink()
        moved.rename(target)
        (self.videos / "linked").symlink_to(self.pending_dirs[1])
        self.assert_rejected("Unrelated untracked")

    def test_ignored_file_in_prepared_folder_is_refused(self):
        (self.pending_dirs[0] / ".DS_Store").write_bytes(b"x")
        self.assert_rejected("does not list as untracked")

    def test_malformed_metadata_is_refused(self):
        path = self.pending_dirs[0] / "metadata.json"
        good = path.read_bytes()
        content = json.loads(good)
        cases = [
            ("not json", "malformed"),
            (dict(content, extra=1), "unexpected fields"),
            (dict(content, video_id="short"), "invalid video_id"),
            (dict(content, duration=0), "invalid duration"),
            (dict(content, duration=True), "invalid duration"),
            (dict(content, duration=float("nan")), "invalid duration"),
            (dict(content, duration=float("inf")), "invalid duration"),
            (dict(content, published_at="2026-13-40"), "invalid published_at"),
            (dict(content, url="https://example.com/watch?v=" + PENDING[0]), "url"),
            (dict(content, title="Other title"), "canonical folder"),
        ]
        for data, pattern in cases:
            with self.subTest(pattern=pattern):
                if isinstance(data, str):
                    path.write_text(data, encoding="utf-8")
                else:
                    self.write_json(path, data)
                self.assert_rejected(pattern)
                path.write_bytes(good)
        path.write_text(json.dumps(content), encoding="utf-8")
        self.assert_rejected("canonical written form")

    def test_duplicate_ids_are_refused(self):
        fetch_transcript.write_pending_metadata(self.videos, meta(PENDING[0], title="Copy"))
        self.assert_rejected("appears in both")

    def test_id_already_in_tracked_corpus_is_refused(self):
        fetch_transcript.write_pending_metadata(self.videos, meta(KNOWN, title="Again"))
        self.assert_rejected("duplicates tracked")

    def test_partial_fetches_are_refused(self):
        (self.selected_dir / "raw" / "provenance.json").unlink()
        self.assert_rejected("partial fetch")

    def test_empty_leftover_raw_directory_is_refused(self):
        (self.pending_dirs[0] / "raw").mkdir()
        self.assert_rejected("partial fetch")

    def test_zero_or_multiple_fetched_videos_are_refused(self):
        self.fetch("Second00001")
        self.assert_rejected("exactly one fully fetched")

    def test_no_fetched_video_is_refused(self):
        for path in sorted(self.selected_dir.rglob("*"), reverse=True):
            if path.name != "metadata.json":
                path.rmdir() if path.is_dir() else path.unlink()
        self.assert_rejected("exactly one fully fetched")

    def test_existing_summary_review_or_stale_artifacts_are_refused(self):
        for name in ("summary.md", "review.md", "summary.stale"):
            with self.subTest(name=name):
                (self.selected_dir / name).write_text("x", encoding="utf-8")
                self.assert_rejected("not exactly one complete fetch")
                (self.selected_dir / name).unlink()
        (self.pending_dirs[0] / "summary.md").write_text("x", encoding="utf-8")
        self.assert_rejected("partial fetch")

    def test_caption_checksum_mismatch_is_refused(self):
        raw = self.selected_dir / "raw" / "captions.vi-orig.json3.gz"
        raw.write_bytes(gzip.compress(FIXTURE_JSON3 + b" ", mtime=0))
        self.assert_rejected("sha256 does not match")

    def test_transcript_mismatch_is_refused(self):
        transcript = self.selected_dir / "transcript.md"
        transcript.write_text(transcript.read_text(encoding="utf-8") + "[09:00:00] thêm\n",
                              encoding="utf-8")
        self.assert_rejected("transcript of .* fails verification")

    def test_malformed_or_empty_captions_are_refused(self):
        for raw, pattern in ((b"not json", "cannot be parsed"),
                             (json.dumps({"events": []}).encode(), "no transcript lines")):
            with self.subTest(pattern=pattern):
                for path in sorted(self.selected_dir.rglob("*"), reverse=True):
                    path.rmdir() if path.is_dir() else path.unlink()
                self.selected_dir.rmdir()
                self.selected_dir = self.fetch(SELECTED, title="Số 7: Omega 3", date="20261028", raw=raw)
                self.assert_rejected(pattern)

    def test_provenance_identity_mismatch_is_refused(self):
        path = self.selected_dir / "raw" / "provenance.json"
        good = json.loads(path.read_text(encoding="utf-8"))
        for field, value in (("video_id", PENDING[0]),
                             ("source_url", "https://example.com/"),
                             ("track", "en"),
                             ("caption_kind", "manual")):
            with self.subTest(field=field):
                self.write_json(path, dict(good, **{field: value}))
                self.assert_rejected("does not identify video")
        self.write_json(path, good)
        recover_weekly.inspect_inventory(self.repo)

    def test_main_or_detached_head_is_refused(self):
        sh(self.repo, "branch", "-m", "main")
        self.assert_rejected("feature branch")
        sh(self.repo, "checkout", "-q", "--detach")
        self.assert_rejected("feature branch")


if __name__ == "__main__":
    unittest.main()
