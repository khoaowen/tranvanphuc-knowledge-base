"""Tests for the fail-closed secret gate. Tokens are synthetic and built at runtime.

Real-scanner tests use the pinned, verified binary from the local cache and make
no network calls; they are skipped only when it was never bootstrapped (run
`python3 scripts/scan_secrets.py bootstrap` once; CI and ./weekly-sync do).
"""
import contextlib
import gzip
import hashlib
import io
import json
import os
import random
import stat
import string
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import scan_secrets  # noqa: E402

ALNUM = string.ascii_letters + string.digits


def fake_token(kind="github", seed=1):
    """A synthetic, recognizable credential; never present as a literal in source."""
    rng = random.Random(seed)
    if kind == "github":
        return "ghp_" + "".join(rng.choice(ALNUM) for _ in range(36))
    if kind == "aws":
        return "AKIA" + "".join(rng.choice(string.ascii_uppercase + "234567") for _ in range(16))
    if kind == "gemini":
        return "AIza" + "".join(rng.choice(ALNUM + "-_") for _ in range(35))
    raise ValueError(kind)


def real_binary():
    try:
        key = scan_secrets.platform_key()
    except scan_secrets.ScanError:
        return None
    path = scan_secrets.cache_dir() / scan_secrets.GITLEAKS_VERSION / key / "gitleaks"
    return path if scan_secrets.verify_binary(path, key) else None


REAL = real_binary()
if not REAL and os.environ.get("CI"):  # never let CI pass with the real-scanner tests skipped
    raise RuntimeError("pinned scanner missing in CI: run scripts/scan_secrets.py bootstrap first")
needs_scanner = unittest.skipUnless(REAL, "pinned scanner not bootstrapped in the local cache")


def git(cwd, *args, env=None):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, check=True,
                          env={**os.environ, **(env or {})}).stdout.strip()


def make_repo(tmp):
    repo = Path(tmp) / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.name", "Fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    return repo


def write_commit(repo, files, message="c"):
    for name, content in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if content is None:
            path.unlink()
        else:
            path.write_bytes(content if isinstance(content, bytes) else content.encode())
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def blob(result):
    return json.dumps(result.to_dict()) + result.summary()


@needs_scanner
class RealScannerTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.repo = make_repo(self._tmp.name)
        self.token = fake_token()

    def stage(self, files):
        for name, content in files.items():
            path = self.repo / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content if isinstance(content, bytes) else content.encode())
        git(self.repo, "add", "-A")

    def test_clean_index_and_commit_pass(self):
        head = write_commit(self.repo, {"a.md": "nothing sensitive here\n"})
        self.assertTrue(scan_secrets.scan_index(self.repo).ok)
        result = scan_secrets.scan_commit(self.repo, head)
        self.assertTrue(result.ok, result.summary())
        self.assertEqual(result.target, head)

    def test_token_in_staged_index_blocks_without_leaking_it(self):
        write_commit(self.repo, {"a.md": "ok\n"})
        self.stage({"videos/x/summary.md": f"key = {self.token}\n"})
        result = scan_secrets.scan_index(self.repo)
        self.assertEqual(result.status, "findings")
        self.assertNotIn(self.token, blob(result))
        self.assertNotIn(self.token[:10], blob(result))
        self.assertEqual(result.findings[0]["path"], "videos/x/summary.md")

    def test_every_candidate_surface_is_covered(self):
        write_commit(self.repo, {"a.md": "ok\n"})
        for index, name in enumerate(["metadata.json", "raw/provenance.json", "summary.md",
                                      "README.md", "topics/t.md", "knowledge-gpt/k.md"]):
            git(self.repo, "reset", "-q", "--hard")
            self.stage({f"videos/v/{name}": f'{{"note": "{fake_token("aws", index)}"}}\n'})
            self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings", name)

    def test_secret_removed_before_head_still_blocks_history(self):
        write_commit(self.repo, {"a.md": f"{self.token}\n"}, "add")
        head = write_commit(self.repo, {"a.md": "clean now\n"}, "remove")
        self.assertTrue(scan_secrets.scan_tree(self.repo, git(self.repo, "rev-parse", "HEAD^{tree}")).ok)
        result = scan_secrets.scan_commit(self.repo, head)
        self.assertEqual(result.status, "findings")
        self.assertNotIn(self.token, blob(result))

    def test_secret_in_merged_side_branch_blocks(self):
        write_commit(self.repo, {"a.md": "base\n"})
        git(self.repo, "checkout", "-q", "-b", "side")
        write_commit(self.repo, {"s.md": f"{self.token}\n"}, "side add")
        write_commit(self.repo, {"s.md": "gone\n"}, "side remove")
        git(self.repo, "checkout", "-q", "main")
        write_commit(self.repo, {"m.md": "main\n"}, "main")
        git(self.repo, "merge", "-q", "--no-ff", "side", "-m", "merge")
        self.assertEqual(scan_secrets.scan_commit(self.repo, "HEAD").status, "findings")

    def test_inline_allow_comment_is_ignored(self):
        write_commit(self.repo, {"a.py": f'x = "{self.token}"  # gitleaks:allow\n'})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")

    def test_repository_ignore_baseline_and_config_files_are_inert(self):
        first = write_commit(self.repo, {"a.md": f"{self.token}\n"})
        raw = scan_secrets.scan_commit(self.repo, first)
        self.assertEqual(raw.status, "findings")
        write_commit(self.repo, {
            ".gitleaks.toml": '[allowlist]\npaths = [".*"]\nregexes = [".*"]\n',
            ".gitleaksignore": "a.md:github-pat:1\n" + f"{first}:a.md:github-pat:1\n",
        }, "overrides")
        index = scan_secrets.scan_index(self.repo)
        self.assertEqual(index.status, "findings")
        self.assertIn("scanner override file present; treated as inert text", index.notes)
        self.assertEqual(scan_secrets.scan_commit(self.repo, "HEAD").status, "findings")

    def test_environment_overrides_are_ignored(self):
        write_commit(self.repo, {"a.md": f"{self.token}\n"})
        cfg = Path(self._tmp.name) / "allow.toml"
        cfg.write_text('[allowlist]\nregexes = [".*"]\n')
        with mock.patch.dict(os.environ, {"GITLEAKS_CONFIG": str(cfg),
                                          "GITLEAKS_CONFIG_TOML": '[allowlist]\nregexes=[".*"]',
                                          "GIT_DIR": str(self.repo / "nowhere")}):
            self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")

    def test_tests_and_generated_content_are_not_excluded(self):
        self.stage({"tests/test_x.py": f't = "{fake_token("gemini", 3)}"\n',
                    "knowledge-gpt/g.md": f"{fake_token('aws', 4)}\n"})
        paths = {f["path"] for f in scan_secrets.scan_index(self.repo).findings}
        self.assertEqual(paths, {"tests/test_x.py", "knowledge-gpt/g.md"})

    def test_gzip_content_is_decompressed_and_scanned(self):
        self.stage({"raw/c.json3.gz": gzip.compress(f"{self.token}\n".encode())})
        result = scan_secrets.scan_index(self.repo)
        self.assertEqual(result.status, "findings")
        self.assertNotIn(self.token, blob(result))

    def test_unexaminable_content_cannot_certify_clean(self):
        write_commit(self.repo, {"a.md": "ok\n"})
        for name, data in {"u16.md": f"{self.token}\n".encode("utf-16"),
                           "blob.bin": b"\x00\x01\x02binary"}.items():
            git(self.repo, "reset", "-q", "--hard")
            self.stage({name: data})
            result = scan_secrets.scan_index(self.repo)
            self.assertEqual(result.status, "error", name)
            self.assertNotIn(self.token, blob(result))

    def test_oversized_file_cannot_certify_clean(self):
        self.stage({"big.txt": b"a" * (scan_secrets.MAX_FILE_BYTES + 1)})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "error")

    def test_real_image_is_noted_and_its_embedded_text_is_still_scanned(self):
        header = b"\x89PNG\r\n\x1a\n\x00\x00"
        self.stage({"p.png": header})
        result = scan_secrets.scan_index(self.repo)
        self.assertTrue(result.ok)
        self.assertTrue(any("image file" in n for n in result.notes))
        self.stage({"p.png": header + f"\x00 tEXt key={self.token} \x00".encode()})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")

    def test_nul_bearing_file_with_image_extension_but_wrong_magic_blocks(self):
        self.stage({"x.png": b"\x00\x00" + f"{self.token}".encode()})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "error")

    def test_scanner_builtin_path_allowlist_cannot_exempt_content(self):
        names = ["package-lock.json", "yarn.lock", "x.svg", "doc.pdf", "go.sum", "node_modules/a/b.js",
                 "vendor/x.txt", ".gitleaks.toml", "a.bin", "z.exe"]
        for index, name in enumerate(names):
            repo = make_repo(tempfile.mkdtemp(dir=self._tmp.name))
            write_commit(repo, {"base.md": "ok\n"})
            content = f"token={fake_token('aws', 20 + index)}\n"
            for rel in (name,):
                path = repo / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            git(repo, "add", "-A")
            self.assertEqual(scan_secrets.scan_index(repo).status, "findings", name)
            git(repo, "commit", "-q", "-m", "x")
            self.assertEqual(scan_secrets.scan_commit(repo, "HEAD").status, "findings", name)

    def test_export_ignore_attributes_cannot_hide_files(self):
        self.stage({".gitattributes": "* export-ignore\n", "a.md": f"{self.token}\n"})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")

    def test_colliding_names_each_get_scanned(self):
        self.stage({"a.gz": gzip.compress(b"harmless\n"), "a.decompressed.txt": f"{self.token}\n"})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")
        git(self.repo, "reset", "-q", "--hard")
        self.stage({".gitleaks.toml": "x\n", ".gitleaks.toml.inert.txt": f"{self.token}\n"})
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")

    def test_token_hidden_in_a_path_name_is_found_and_the_path_withheld(self):
        self.stage({f"notes/{self.token}.md": "x\n"})
        result = scan_secrets.scan_index(self.repo)
        self.assertEqual(result.status, "findings")
        self.assertNotIn(self.token, blob(result))

    def test_submodule_entries_cannot_certify_clean(self):
        write_commit(self.repo, {"a.md": "ok\n"})
        sha = git(self.repo, "rev-parse", "HEAD")
        git(self.repo, "update-index", "--add", "--cacheinfo", f"160000,{sha},sub")
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "error")

    def test_symlink_target_is_scanned(self):
        write_commit(self.repo, {"a.md": "ok\n"})
        os.symlink(f"/tmp/{self.token}", self.repo / "link")
        git(self.repo, "add", "link")
        self.assertEqual(scan_secrets.scan_index(self.repo).status, "findings")

    def test_shallow_clone_cannot_prove_history(self):
        head = write_commit(self.repo, {"a.md": "1\n"})
        write_commit(self.repo, {"a.md": "2\n"})
        shallow = Path(self._tmp.name) / "shallow"
        git(self._tmp.name, "clone", "-q", "--depth", "1", f"file://{self.repo}", str(shallow))
        result = scan_secrets.scan_commit(shallow, "HEAD")
        self.assertEqual(result.status, "error")
        self.assertNotIn(head, result.detail)

    def test_index_changing_during_scan_is_an_error(self):
        write_commit(self.repo, {"a.md": "ok\n"})
        real = scan_secrets.scan_tree

        def racing(repo, tree, mode="tree", binary=None):
            out = real(repo, tree, mode, binary)
            self.stage({"late.md": "changed\n"})
            return out

        with mock.patch.object(scan_secrets, "scan_tree", racing):
            self.assertEqual(scan_secrets.scan_index(self.repo).status, "error")

    def test_artifacts_clean_finding_missing_and_unsafe(self):
        ok = Path(self._tmp.name) / "measurement.log"
        ok.write_text("tokens: 12\n")
        bad = Path(self._tmp.name) / "summary.md"
        bad.write_text(f"leak {self.token}\n")
        self.assertTrue(scan_secrets.scan_artifacts([ok]).ok)
        found = scan_secrets.scan_artifacts([ok, bad])
        self.assertEqual(found.status, "findings")
        self.assertNotIn(self.token, blob(found))
        absent = Path(self._tmp.name) / "none.md"
        self.assertEqual(scan_secrets.scan_artifacts([ok, absent]).status, "error")
        self.assertTrue(scan_secrets.scan_artifacts([ok, absent], allow_missing=True).ok)
        self.assertEqual(scan_secrets.scan_artifacts([absent], allow_missing=True).status, "error")
        self.assertEqual(scan_secrets.scan_artifacts([self._tmp.name]).status, "error")

    def test_cli_exit_codes_and_redacted_output(self):
        head = write_commit(self.repo, {"a.md": "ok\n"})
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(scan_secrets.main(["commit", head, "--repo", str(self.repo)]), 0)
            self.stage({"b.md": f"{self.token}\n"})
            self.assertEqual(scan_secrets.main(["index", "--repo", str(self.repo)]), 3)
            self.assertEqual(scan_secrets.main(["index", "--json", "--repo", str(self.repo)]), 3)
            self.assertEqual(scan_secrets.main(["commit", "nonexistent", "--repo", str(self.repo)]), 4)
        self.assertNotIn(self.token, out.getvalue() + err.getvalue())
        self.assertIn("github-pat", out.getvalue())

    def test_scanner_subprocess_output_is_never_surfaced(self):
        write_commit(self.repo, {"a.md": f"{self.token}\n"})
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            scan_secrets.scan_commit(self.repo, "HEAD")
        self.assertEqual(out.getvalue() + err.getvalue(), "")


class FakeScannerTest(unittest.TestCase):
    """Scanner failure modes through a stand-in executable (no real scanner needed)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        self.token = fake_token("aws", 9)

    def script(self, body):
        path = self.tmp / "fake-gitleaks"
        path.write_text("#!/usr/bin/env python3\n" + body)
        path.chmod(0o755)
        return path

    def artifact(self):
        file = self.tmp / "out.log"
        file.write_text("harmless\n")
        return file

    def test_scanner_error_exit_fails_closed_and_hides_diagnostics(self):
        fake = self.script(f"import sys\nprint('boom {self.token}', file=sys.stderr)\nsys.exit(1)\n")
        result = scan_secrets.scan_artifacts([self.artifact()], binary=fake)
        self.assertEqual(result.status, "error")
        self.assertNotIn(self.token, blob(result))
        self.assertEqual(scan_secrets.exit_code(result), scan_secrets.EXIT_BLOCKED)

    def test_findings_report_values_are_dropped(self):
        fake = self.script(
            "import sys,json\n"
            "a=sys.argv\nreport=a[a.index('--report-path')+1]\n"
            f"json.dump([{{'RuleID':'aws-access-token','File':'x/out.log','StartLine':3,"
            f"'Secret':'{self.token}','Match':'{self.token}','Line':'{self.token}'}}],open(report,'w'))\n"
            f"sys.exit({scan_secrets.LEAK_EXIT})\n")
        result = scan_secrets.scan_artifacts([self.artifact()], binary=fake)
        self.assertEqual(result.status, "findings")
        self.assertEqual(result.findings[0]["rule"], "aws-access-token")
        self.assertNotIn(self.token, blob(result))
        self.assertEqual(scan_secrets.exit_code(result), scan_secrets.EXIT_FINDINGS)

    def test_clean_exit_with_nonempty_report_is_an_error(self):
        fake = self.script(
            "import sys,json\na=sys.argv\njson.dump([{'RuleID':'x'}],open(a[a.index('--report-path')+1],'w'))\n")
        self.assertEqual(scan_secrets.scan_artifacts([self.artifact()], binary=fake).status, "error")

    def test_scanner_timeout_is_an_error(self):
        fake = self.script("import time\ntime.sleep(30)\n")
        with mock.patch.object(scan_secrets, "SCAN_TIMEOUT", 0.2), \
                mock.patch.object(scan_secrets, "TIMEOUT_SLACK", 0):
            self.assertEqual(scan_secrets.scan_artifacts([self.artifact()], binary=fake).status, "error")

    def test_missing_scanner_executable_is_an_error(self):
        result = scan_secrets.scan_artifacts([self.artifact()], binary=self.tmp / "absent")
        self.assertEqual(result.status, "error")

    def test_command_disables_overrides_and_never_passes_config_or_baseline(self):
        seen = {}

        def fake_run(command, **kwargs):
            seen["command"], seen["env"] = command, kwargs["env"]
            return subprocess.CompletedProcess(command, 0, b"", b"")

        with mock.patch.dict(os.environ, {"GITLEAKS_CONFIG": "/x", "GITLEAKS_ANYTHING": "1"}), \
                mock.patch.object(scan_secrets.subprocess, "run", fake_run):
            scan_secrets.scan_artifacts([self.artifact()], binary=Path("/bin/true"))
        words = seen["command"]
        for required in ("--ignore-gitleaks-allow", "--redact", "--gitleaks-ignore-path"):
            self.assertIn(required, words)
        for forbidden in ("--config", "-c", "--baseline-path", "-b", "--enable-rule"):
            self.assertNotIn(forbidden, words)
        self.assertFalse([k for k in seen["env"] if k.upper().startswith("GITLEAKS")])

    def test_sensitive_looking_paths_are_withheld(self):
        self.assertEqual(scan_secrets.safe_path("videos/a-b/summary.md"), "videos/a-b/summary.md")
        self.assertEqual(scan_secrets.safe_path(f"x/{self.token}.md"), "<redacted-path>")
        self.assertEqual(scan_secrets.safe_path("a\nb"), "<redacted-path>")

    def test_result_summary_never_includes_findings_values(self):
        result = scan_secrets.Result("index", "findings", "t", [{"rule": "r", "path": "p", "line": 1}])
        self.assertIn("values withheld", result.summary())


class BootstrapTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        patcher = mock.patch.dict(os.environ, {"TRANVANPHUC_SCANNER_CACHE": self._tmp.name})
        patcher.start()
        self.addCleanup(patcher.stop)

    def archive(self, payload=b"#!/bin/sh\necho 8.30.1\n", name="gitleaks"):
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
            info = tarfile.TarInfo(name)
            info.size, info.mode = len(payload), 0o755
            tar.addfile(info, io.BytesIO(payload))
        return buffer.getvalue()

    def test_pins_cover_supported_platforms_with_valid_digests(self):
        self.assertEqual(set(scan_secrets.PLATFORMS),
                         {"darwin_arm64", "darwin_x64", "linux_arm64", "linux_x64"})
        for archive_sha, binary_sha in scan_secrets.PLATFORMS.values():
            self.assertRegex(archive_sha, r"^[0-9a-f]{64}$")
            self.assertRegex(binary_sha, r"^[0-9a-f]{64}$")
        self.assertEqual(scan_secrets.GITLEAKS_VERSION, "8.30.1")
        self.assertTrue(scan_secrets.RELEASE_URL.startswith("https://github.com/gitleaks/gitleaks/"))

    def test_platform_mapping_and_unsupported_platforms_block(self):
        self.assertEqual(scan_secrets.platform_key("Darwin", "arm64"), "darwin_arm64")
        self.assertEqual(scan_secrets.platform_key("Linux", "aarch64"), "linux_arm64")
        self.assertEqual(scan_secrets.platform_key("Linux", "x86_64"), "linux_x64")
        self.assertEqual(scan_secrets.platform_key("Darwin", "x86_64"), "darwin_x64")
        for system, machine in (("Windows", "AMD64"), ("Linux", "riscv64"), ("FreeBSD", "x86_64")):
            with self.assertRaises(scan_secrets.ScanError):
                scan_secrets.platform_key(system, machine)

    def test_archive_with_wrong_checksum_is_refused_and_not_installed(self):
        with self.assertRaisesRegex(scan_secrets.ScanError, "checksum"):
            scan_secrets.ensure_scanner(fetch=lambda url: self.archive(), system="Linux", machine="x86_64")
        self.assertFalse(list(Path(self._tmp.name).rglob("gitleaks")))

    def test_correct_archive_with_substituted_binary_is_refused(self):
        data = self.archive()
        pins = dict(scan_secrets.PLATFORMS)
        pins["linux_x64"] = (hashlib.sha256(data).hexdigest(), "0" * 64)
        with mock.patch.object(scan_secrets, "PLATFORMS", pins):
            with self.assertRaisesRegex(scan_secrets.ScanError, "binary checksum"):
                scan_secrets.ensure_scanner(fetch=lambda url: data, system="Linux", machine="x86_64")

    def test_wrong_version_binary_is_refused(self):
        payload = b"#!/bin/sh\necho 8.0.0\n"
        data = self.archive(payload)
        pins = dict(scan_secrets.PLATFORMS)
        pins["linux_x64"] = (hashlib.sha256(data).hexdigest(), hashlib.sha256(payload).hexdigest())
        with mock.patch.object(scan_secrets, "PLATFORMS", pins):
            with self.assertRaisesRegex(scan_secrets.ScanError, "verification"):
                scan_secrets.ensure_scanner(fetch=lambda url: data, system="Linux", machine="x86_64")

    def test_matching_archive_and_version_installs_then_corruption_is_detected(self):
        payload = b"#!/bin/sh\necho 8.30.1\n"
        data = self.archive(payload)
        pins = dict(scan_secrets.PLATFORMS)
        pins["linux_x64"] = (hashlib.sha256(data).hexdigest(), hashlib.sha256(payload).hexdigest())
        calls = []
        with mock.patch.object(scan_secrets, "PLATFORMS", pins), \
                mock.patch.object(scan_secrets, "platform_key", lambda *a: "linux_x64"):
            binary = scan_secrets.ensure_scanner(fetch=lambda url: calls.append(url) or data)
            self.assertTrue(stat.S_IMODE(binary.stat().st_mode) & stat.S_IXUSR)
            scan_secrets.ensure_scanner(fetch=lambda url: calls.append(url) or data)
            self.assertEqual(len(calls), 1)  # verified cache reused, no refetch
            binary.write_bytes(b"#!/bin/sh\necho tampered\n")
            scan_secrets.ensure_scanner(fetch=lambda url: calls.append(url) or data)
            self.assertEqual(len(calls), 2)  # corrupt cache replaced from verified archive
            self.assertEqual(binary.read_bytes(), payload)

    def test_download_failure_and_non_https_block_without_details(self):
        def boom(url):
            raise OSError("secret-ish detail")
        with self.assertRaises(scan_secrets.ScanError) as caught:
            scan_secrets.ensure_scanner(fetch=boom, system="Linux", machine="x86_64")
        self.assertNotIn("secret-ish", str(caught.exception))
        with self.assertRaises(scan_secrets.ScanError):
            scan_secrets.download("http://example.invalid/x")

    def test_scan_failures_from_bootstrap_become_blocking_results(self):
        with mock.patch.object(scan_secrets, "ensure_scanner",
                               side_effect=scan_secrets.ScanError("scanner archive checksum mismatch")):
            result = scan_secrets.scan_artifacts([__file__])
        self.assertEqual(result.status, "error")
        self.assertFalse(result.ok)


if __name__ == "__main__":
    unittest.main()
