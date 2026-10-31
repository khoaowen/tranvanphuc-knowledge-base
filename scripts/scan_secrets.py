#!/usr/bin/env python3
"""Fail-closed secret-leak gate built on a pinned, checksum-verified Gitleaks.

Deterministic means fixed rules: the scanner's built-in default ruleset, no LLM
and no credential-validity calls. A clean scan does NOT prove the absence of
every secret, medical safety or prompt-injection safety.

Modes (all exit 0 only when every examined byte was scanned clean):

  bootstrap                   install/verify the pinned scanner in the cache
  index                       scan the exact prospective index (write-tree)
  commit [REV]                scan reachable history of REV plus its final tree
  repository                  same as `commit HEAD`
  artifacts PATH...           scan files about to be uploaded
                              (--allow-missing tolerates absent paths)

Exit codes: 0 clean, 3 findings, 4 scanner unavailable/errored (blocked).
Matched values, snippets and raw reports are never printed or stored; only a
sanitized outcome (rule ids, repo-relative path, line) is emitted.

Content is written to opaque file names so the scanner's built-in path allowlist cannot
exempt anything; history mode scans every reachable blob, not diffs.

Inline `gitleaks:allow`, repository ignore/baseline files and GITLEAKS_* env
overrides are disabled. Repo-level `.gitleaks.toml` / `.gitleaksignore` files are
extracted as inert text (scanned, never honored).
"""

import argparse
import hashlib
import io
import json
import os
import platform
import re
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zlib
from pathlib import Path

GITLEAKS_VERSION = "8.30.1"
RELEASE_URL = "https://github.com/gitleaks/gitleaks/releases/download/v{v}/gitleaks_{v}_{plat}.tar.gz"
# Tarball SHA-256 from upstream gitleaks_8.30.1_checksums.txt (cross-checked against the
# GitHub release asset digests); binary SHA-256 of the `gitleaks` member of each tarball.
PLATFORMS = {
    "darwin_arm64": ("b40ab0ae55c505963e365f271a8d3846efbc170aa17f2607f13df610a9aeb6a5",
                     "ba52fb1bfabbcde42f032afad3d6e0b19dff8ed105229a16e7caa338bbc0e84f"),
    "darwin_x64": ("dfe101a4db2255fc85120ac7f3d25e4342c3c20cf749f2c20a18081af1952709",
                   "cee01fea7173f1b779dff188e1c26ecbcb4027d394acc573b23aaf0be260e291"),
    "linux_arm64": ("e4a487ee7ccd7d3a7f7ec08657610aa3606637dab924210b3aee62570fb4b080",
                    "00e91bbe655bd7c47753e8cfe61cb76ea1a5d7e7702fe161ee40102b46b3823b"),
    "linux_x64": ("551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb",
                  "88f91962aa2f93ac6ab281d553b9e125f5197bbbce38f9f2437f7299c32e5509"),
}
MAX_DOWNLOAD = 100 * 1024 * 1024
MAX_FILE_BYTES = 20 * 1024 * 1024      # larger files are an error, never silently skipped
MAX_TREE_BYTES = 500 * 1024 * 1024
SCAN_TIMEOUT = 900
TIMEOUT_SLACK = 60
LEAK_EXIT = 42                         # distinct from gitleaks' generic error exit (1)
INERT_NAMES = {".gitleaks.toml", ".gitleaksignore"}
# Reviewed, content-bound exception: three historical blobs of tests/test_weekly_sync.py hold a
# synthetic, non-working placeholder key (AIza-prefixed, malformed) on one line. Only these exact
# blob ids qualify, only in history mode, and only that line is dropped; every other byte of the
# blob is still scanned. Not a rule change, path exclusion or baseline. See docs/security.md.
SYNTHETIC_PLACEHOLDER_MARKER = b"weekly-sentinel-key-987"
SYNTHETIC_PLACEHOLDER_BLOBS = frozenset({
    "b8d935717c4cadf0fcf651f792a3681a58be03e3",
    "ced8d4f44cdbd3cecb4f1b192767252b8a09bf9a",
    "840dd934aa1d4512eb3c519dee8557762b2e46d8",
})
EXIT_OK, EXIT_FINDINGS, EXIT_BLOCKED = 0, 3, 4


class ScanError(Exception):
    """Scanner unavailable or unable to certify; message is always safe to print."""


class Result:
    def __init__(self, mode, status, target=None, findings=None, detail="", notes=None):
        self.mode, self.status, self.target = mode, status, target
        self.findings = findings or []   # [{"rule", "path", "line"}] — never matched values
        self.detail = detail
        self.notes = notes or []

    @property
    def ok(self):
        return self.status == "clean"

    def to_dict(self):
        return {"mode": self.mode, "status": self.status, "target": self.target,
                "scanner": f"gitleaks {GITLEAKS_VERSION}", "findings": self.findings,
                "detail": self.detail, "notes": self.notes}

    def summary(self):
        if self.status == "clean":
            return f"secret scan clean ({self.mode} {self.target or ''})".strip()
        if self.status == "findings":
            rules = sorted({f["rule"] for f in self.findings})
            return (f"secret scan found {len(self.findings)} potential secret(s) in {self.mode} "
                    f"{self.target or ''}: rules {rules}; values withheld").replace("  ", " ")
        return f"secret scan could not certify {self.mode}: {self.detail}"


# --- scanner bootstrap -----------------------------------------------------


def platform_key(system=None, machine=None):
    system = (system or platform.system()).lower()
    machine = (machine or platform.machine()).lower()
    arch = {"x86_64": "x64", "amd64": "x64", "arm64": "arm64", "aarch64": "arm64"}.get(machine)
    if system not in ("darwin", "linux") or arch is None or f"{system}_{arch}" not in PLATFORMS:
        raise ScanError(f"unsupported platform {system}/{machine}; publication blocked")
    return f"{system}_{arch}"


def cache_dir():
    base = os.environ.get("TRANVANPHUC_SCANNER_CACHE")
    return Path(base) if base else Path.home() / ".cache" / "tranvanphuc-weekly" / "scanner"


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def scanner_env(home):
    env = {k: v for k, v in os.environ.items()
           if not k.upper().startswith("GITLEAKS") and not k.upper().startswith("GIT_")
           and k.upper() not in ("PAGER",)}
    env["HOME"] = str(home)
    env["GIT_CONFIG_NOSYSTEM"] = "1"
    env["GIT_CONFIG_GLOBAL"] = os.devnull
    env["GIT_TERMINAL_PROMPT"] = "0"
    return env


def download(url):
    """Default fetcher (replaceable in tests). https only, size capped."""
    if not url.startswith("https://"):
        raise ScanError("scanner download must use https")
    with urllib.request.urlopen(url, timeout=120) as response:  # noqa: S310 - https enforced
        data = response.read(MAX_DOWNLOAD + 1)
    if len(data) > MAX_DOWNLOAD:
        raise ScanError("scanner download exceeds size cap")
    return data


def verify_binary(path, key):
    """True only for the exact pinned binary that reports the pinned version."""
    try:
        if not os.access(path, os.X_OK) or sha256_file(path) != PLATFORMS[key][1]:
            return False
        with tempfile.TemporaryDirectory(prefix="gl-ver-") as home:
            out = subprocess.run([str(path), "version"], capture_output=True, text=True,
                                 timeout=60, env=scanner_env(home), cwd=home)
        return out.returncode == 0 and out.stdout.strip() == GITLEAKS_VERSION
    except (OSError, subprocess.SubprocessError):
        return False


def ensure_scanner(fetch=None, system=None, machine=None):
    """Return the path of the verified pinned scanner, installing it if needed."""
    key = platform_key(system, machine)
    target_dir = cache_dir() / GITLEAKS_VERSION / key
    binary = target_dir / "gitleaks"
    if verify_binary(binary, key):
        return binary
    archive_sha, binary_sha = PLATFORMS[key]
    try:
        data = (fetch or download)(RELEASE_URL.format(v=GITLEAKS_VERSION, plat=key))
    except ScanError:
        raise
    except Exception:
        raise ScanError("scanner download failed; publication blocked") from None
    if hashlib.sha256(data).hexdigest() != archive_sha:
        raise ScanError("scanner archive checksum mismatch; refusing to install")
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            member = archive.getmember("gitleaks")
            if not member.isreg() or member.size > MAX_DOWNLOAD:
                raise ScanError("scanner archive member is not a regular file")
            payload = archive.extractfile(member).read()
    except ScanError:
        raise
    except Exception:
        raise ScanError("scanner archive unreadable; refusing to install") from None
    if hashlib.sha256(payload).hexdigest() != binary_sha:
        raise ScanError("scanner binary checksum mismatch; refusing to install")
    target_dir.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=target_dir, prefix=".gitleaks.")
    with os.fdopen(fd, "wb") as handle:
        handle.write(payload)
    os.chmod(tmp, stat.S_IRWXU)
    os.replace(tmp, binary)
    if not verify_binary(binary, key):
        raise ScanError("installed scanner failed verification (version/checksum)")
    return binary


# --- running the scanner ---------------------------------------------------

_SAFE_PATH = re.compile(r"[A-Za-z0-9._/@+=,~ -]{1,240}")


def safe_path(path):
    """Repo-relative path for diagnostics; withheld if it could itself carry a secret."""
    if not isinstance(path, str) or not _SAFE_PATH.fullmatch(path):
        return "<redacted-path>"
    if any(len(run) >= 20 for run in re.findall(r"[A-Za-z0-9_]+", path)):
        return "<redacted-path>"
    return path


def _sanitize_findings(raw, labels):
    findings = []
    for item in raw if isinstance(raw, list) else []:
        if not isinstance(item, dict):
            continue
        rule = str(item.get("RuleID", ""))
        line = item.get("StartLine")
        findings.append({
            "rule": rule if re.fullmatch(r"[A-Za-z0-9._-]{1,80}", rule) else "unknown",
            "path": safe_path(labels.get(os.path.basename(str(item.get("File", ""))), "")),
            "line": line if isinstance(line, int) else None,
        })
    return findings


def run_gitleaks(binary, root, work, mode, target, labels):
    """Run one scan; returns Result. Output is captured and never surfaced."""
    report = work / "report.json"
    empty_ignore = work / "ignore"
    empty_ignore.mkdir(exist_ok=True)
    home = work / "home"
    home.mkdir(exist_ok=True)
    command = [str(binary), "dir", str(root), "--no-banner", "--no-color", "--redact", "--ignore-gitleaks-allow",
               "--max-target-megabytes", str(MAX_FILE_BYTES // (1024 * 1024)),
               "--gitleaks-ignore-path", str(empty_ignore), "--exit-code", str(LEAK_EXIT),
               "--report-format", "json", "--report-path", str(report),
               "--log-level", "error", "--timeout", str(int(SCAN_TIMEOUT))]
    try:
        proc = subprocess.run(command, cwd=str(root), capture_output=True, timeout=SCAN_TIMEOUT + TIMEOUT_SLACK,
                              env=scanner_env(home), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return Result(mode, "error", target, detail="scanner timed out")
    except OSError:
        return Result(mode, "error", target, detail="scanner could not be executed")
    if proc.returncode == 0:
        if report.exists():
            try:
                if json.loads(report.read_text(encoding="utf-8") or "[]"):
                    return Result(mode, "error", target, detail="scanner reported findings with clean exit")
            except ValueError:
                return Result(mode, "error", target, detail="scanner report unreadable")
        return Result(mode, "clean", target)
    if proc.returncode == LEAK_EXIT:
        try:
            findings = _sanitize_findings(json.loads(report.read_text(encoding="utf-8")), labels)
        except (OSError, ValueError):
            findings = []
        if not findings:
            findings = [{"rule": "unknown", "path": "<redacted-path>", "line": None}]
        return Result(mode, "findings", target, findings=findings)
    return Result(mode, "error", target, detail=f"scanner exit {proc.returncode}")


# --- exact-content extraction ---------------------------------------------
# Every examined byte string is written to an opaque, collision-free file name, so
# neither the scanner's built-in path allowlist (lockfiles, .svg, gitleaks.toml, ...)
# nor path tricks can exempt content. Real paths are kept only in a side map.

IMAGE_MAGIC = {".png": (b"\x89PNG\r\n\x1a\n",), ".jpg": (b"\xff\xd8\xff",), ".jpeg": (b"\xff\xd8\xff",),
               ".gif": (b"GIF87a", b"GIF89a"), ".webp": (b"RIFF",), ".ico": (b"\x00\x00\x01\x00",)}
STRINGS = re.compile(rb"[\x20-\x7e\t]{16,}")


def _classify(label, data):
    """'text' | 'image' (verified magic; printable strings still scanned) | 'gzip'.

    Raises ScanError for content that cannot be examined. Bytes without NULs are
    scanned as-is even when not valid UTF-8; NUL-bearing unknown content (e.g.
    UTF-16, which would hide ASCII secrets from the rules) blocks.
    """
    ext = os.path.splitext(label)[1].lower()
    if len(data) > MAX_FILE_BYTES:
        raise ScanError("a file exceeds the scan size limit; refusing to certify")
    if ext == ".gz" and data[:2] == b"\x1f\x8b":
        return "gzip"
    if b"\0" not in data:
        return "text"
    if ext in IMAGE_MAGIC and data.startswith(IMAGE_MAGIC[ext]):
        return "image"
    raise ScanError("a file looks binary or non-UTF-8 text; refusing to certify")


def _gunzip(data):
    """Bounded gzip decompression; anything malformed or oversized blocks."""
    try:
        inflater = zlib.decompressobj(31)
        out = inflater.decompress(data, MAX_FILE_BYTES + 1)
        if len(out) > MAX_FILE_BYTES or inflater.unconsumed_tail or not inflater.eof:
            raise ScanError("compressed file exceeds the scan size limit; refusing to certify")
    except zlib.error:
        raise ScanError("compressed file is corrupt; refusing to certify") from None
    if b"\0" in out:
        raise ScanError("compressed content looks binary; refusing to certify")
    return out


class Corpus:
    """Writes content to opaque files under `root`; remembers label per file."""

    def __init__(self, root):
        self.root, self.labels, self.notes = root, {}, set()
        self.total = self.images = self.count = 0

    def _put(self, label, data):
        name = f"f{len(self.labels):07d}.txt"
        (self.root / name).write_bytes(data)
        self.labels[name] = label

    def add(self, label, data, symlink=False):
        self.total += len(data)
        if self.total > MAX_TREE_BYTES:
            raise ScanError("scan target too large; refusing to certify")
        if os.path.basename(label).lower() in INERT_NAMES:
            self.notes.add("scanner override file present; treated as inert text")
        kind = "text" if symlink else _classify(label, data)
        if kind == "gzip":
            data, label = _gunzip(data), label + " (decompressed)"
        elif kind == "image":
            self.images += 1
            data = b"\n".join(STRINGS.findall(data))
            label += " (image strings)"
        self._put(label, data)
        self.count += 1

    def add_paths(self, paths):
        """The path names themselves are content too."""
        self._put("<path names>", "\n".join(paths).encode("utf-8", "surrogateescape"))

    def finish(self):
        if self.images:
            self.notes.add(f"{self.images} image file(s): only printable strings were text-scanned")
        return sorted(self.notes)


def git_out(repo, *args):
    out = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True,
                         env=scanner_env(tempfile.gettempdir()))
    if out.returncode != 0:
        raise ScanError("git inspection failed")
    return out.stdout.strip()


def read_blobs(repo, shas):
    """Yield (sha, bytes) for blob ids via git cat-file; size-checked before reading."""
    shas = list(dict.fromkeys(shas))
    env = scanner_env(tempfile.gettempdir())
    base = ["git", "-C", str(repo), "cat-file"]
    check = subprocess.run([*base, "--batch-check"], input="".join(f"{x}\n" for x in shas).encode(),
                           capture_output=True, env=env)
    lines = check.stdout.decode().splitlines()
    if check.returncode != 0 or len(lines) != len(shas):
        raise ScanError("git inspection failed")
    sizes = {}
    for sha, line in zip(shas, lines):
        parts = line.split()
        if len(parts) != 3 or parts[1] != "blob":
            raise ScanError("scan target has a missing or non-blob object; refusing to certify")
        sizes[sha] = int(parts[2])
        if sizes[sha] > MAX_FILE_BYTES:
            raise ScanError("a file exceeds the scan size limit; refusing to certify")
    chunk, weight = [], 0
    for sha in [*shas, None]:
        if sha is None or weight + sizes.get(sha, 0) > 64 * 1024 * 1024:
            if chunk:
                out = subprocess.run([*base, "--batch"], input="".join(f"{x}\n" for x in chunk).encode(),
                                     capture_output=True, env=env)
                if out.returncode != 0:
                    raise ScanError("git inspection failed")
                data, pos = out.stdout, 0
                for want in chunk:
                    end = data.index(b"\n", pos)
                    header = data[pos:end].split()
                    if len(header) != 3 or header[0].decode() != want or int(header[2]) != sizes[want]:
                        raise ScanError("git inspection failed")
                    pos = end + 1 + sizes[want] + 1
                    yield want, data[end + 1:end + 1 + sizes[want]]
            chunk, weight = [], 0
        if sha is not None:
            chunk.append(sha)
            weight += sizes[sha]


def list_tree(repo, tree):
    """[(mode, sha, path)] for every entry of an immutable tree id."""
    out = subprocess.run(["git", "-C", str(repo), "ls-tree", "-r", "-z", "--full-tree", tree],
                         capture_output=True, env=scanner_env(tempfile.gettempdir()))
    if out.returncode != 0:
        raise ScanError("git inspection failed")
    entries = []
    for raw in out.stdout.split(b"\0"):
        if not raw:
            continue
        meta, _, path = raw.partition(b"\t")
        mode, kind, sha = meta.decode().split()
        entries.append((mode, kind, sha, path.decode("utf-8", "surrogateescape")))
    return entries


# --- public scans ----------------------------------------------------------


def _scan_corpus(binary, fill, mode, target):
    """Common driver: build an opaque corpus in a temp dir, scan it, clean up."""
    try:
        binary = binary or ensure_scanner()
        with tempfile.TemporaryDirectory(prefix="secret-scan-") as work_dir:
            work = Path(work_dir)
            root = work / "corpus"
            root.mkdir()
            corpus = Corpus(root.resolve())
            fill(corpus)
            if not corpus.count:
                raise ScanError("nothing to scan; refusing to certify")
            result = run_gitleaks(binary, corpus.root, work, mode, target, corpus.labels)
            result.notes = corpus.finish()
            return result
    except ScanError as exc:
        return Result(mode, "error", target, detail=str(exc))
    except Exception:
        return Result(mode, "error", target, detail="unexpected scanner failure")


def scan_tree(repo, tree, mode="tree", binary=None):
    """Scan the files of an immutable tree id (no export attributes or replace refs involved)."""
    def fill(corpus):
        entries = list_tree(repo, tree)
        corpus.add_paths([e[3] for e in entries])
        gitlinks = [e for e in entries if e[0] == "160000"]
        if gitlinks:
            raise ScanError("submodule entries cannot be scanned; refusing to certify")
        names = {}
        for mode_, _kind, sha, path in entries:
            names.setdefault(sha, []).append((mode_, path))
        for sha, data in read_blobs(repo, [e[2] for e in entries]):
            for mode_, path in names[sha]:
                corpus.add(path, data, symlink=(mode_ == "120000"))
    return _scan_corpus(binary, fill, mode, tree)


def scan_history(repo, commit, binary=None):
    """Scan every blob reachable from `commit` (all versions in all reachable commits)."""
    def fill(corpus):
        shallow = git_out(repo, "rev-parse", "--is-shallow-repository")
        if shallow != "false":
            raise ScanError("shallow checkout cannot prove reachable history; fetch full history")
        listing = git_out(repo, "rev-list", "--objects", "--full-history", commit)
        first_path, order = {}, []
        for line in listing.splitlines():
            sha, _, path = line.partition(" ")
            if sha not in first_path:
                first_path[sha] = path
                order.append(sha)
        check = subprocess.run(["git", "-C", str(repo), "cat-file", "--batch-check"],
                               input="".join(f"{x}\n" for x in order).encode(), capture_output=True,
                               env=scanner_env(tempfile.gettempdir()))
        kinds = check.stdout.decode().splitlines()
        if check.returncode != 0 or len(kinds) != len(order):
            raise ScanError("git inspection failed")
        blobs = [sha for sha, line in zip(order, kinds) if line.split()[1] == "blob"]
        corpus.add_paths([first_path[x] for x in blobs if first_path[x]])
        for sha, data in read_blobs(repo, blobs):
            if sha in SYNTHETIC_PLACEHOLDER_BLOBS:
                data = b"\n".join(l for l in data.split(b"\n") if SYNTHETIC_PLACEHOLDER_MARKER not in l)
                corpus.notes.add("known synthetic placeholder line in 3 pinned historical blobs excluded")
            corpus.add(first_path[sha] or "<blob>", data)
    return _scan_corpus(binary, fill, "history", commit)


def scan_index(repo, binary=None):
    """Scan the exact prospective index; verifies the index did not change while scanning."""
    try:
        tree = git_out(repo, "write-tree")
    except ScanError as exc:
        return Result("index", "error", detail=str(exc))
    result = scan_tree(repo, tree, mode="index", binary=binary)
    try:
        if git_out(repo, "write-tree") != tree:
            return Result("index", "error", tree, detail="index changed during the scan")
    except ScanError as exc:
        return Result("index", "error", tree, detail=str(exc))
    return result


def scan_commit(repo, commit, binary=None):
    """History reachable from the immutable commit id plus its final tracked snapshot."""
    try:
        commit = git_out(repo, "rev-parse", "--verify", commit + "^{commit}")
        tree = git_out(repo, "rev-parse", commit + "^{tree}")
    except ScanError as exc:
        return Result("commit", "error", detail=str(exc))
    history = scan_history(repo, commit, binary)
    snapshot = scan_tree(repo, tree, mode="snapshot", binary=binary)
    snapshot.notes = sorted(set(snapshot.notes) | set(history.notes))
    for part in (history, snapshot):
        if part.status == "error":
            return Result("commit", "error", commit, detail=f"{part.mode}: {part.detail}")
    findings = history.findings + snapshot.findings
    if findings:
        return Result("commit", "findings", commit, findings=findings, notes=snapshot.notes)
    return Result("commit", "clean", commit, notes=snapshot.notes)


def scan_artifacts(paths, allow_missing=False, binary=None):
    """Scan files about to be uploaded. At least one must exist; unreadable ones block."""
    def fill(corpus):
        for raw in paths:
            path = Path(raw)
            if not path.exists():
                if allow_missing:
                    corpus.notes.add("an optional artifact was absent")
                    continue
                raise ScanError("an artifact is missing; refusing to certify")
            if path.is_symlink() or not path.is_file():
                raise ScanError("artifact is not a regular file; refusing to certify")
            data = path.read_bytes()
            if b"\0" in data and not data[:2] == b"\x1f\x8b":
                raise ScanError("binary artifact cannot be text-scanned; refusing to certify")
            corpus.add(path.name, data)
    return _scan_corpus(binary, fill, "artifacts", "upload files")


# --- CLI -------------------------------------------------------------------


def exit_code(result):
    return {"clean": EXIT_OK, "findings": EXIT_FINDINGS}.get(result.status, EXIT_BLOCKED)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    common.add_argument("--json", action="store_true", help="print the sanitized outcome as JSON")
    sub = parser.add_subparsers(dest="mode", required=True)
    for name in ("bootstrap", "index", "repository"):
        sub.add_parser(name, parents=[common])
    commit = sub.add_parser("commit", parents=[common])
    commit.add_argument("rev", nargs="?", default="HEAD")
    artifacts = sub.add_parser("artifacts", parents=[common])
    artifacts.add_argument("paths", nargs="+")
    artifacts.add_argument("--allow-missing", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo)
    if args.mode == "bootstrap":
        try:
            ensure_scanner()
            result = Result("bootstrap", "clean", detail="scanner verified")
        except ScanError as exc:
            result = Result("bootstrap", "error", detail=str(exc))
    elif args.mode == "index":
        result = scan_index(repo)
    elif args.mode in ("repository", "commit"):
        result = scan_commit(repo, "HEAD" if args.mode == "repository" else args.rev)
    else:
        result = scan_artifacts(args.paths, args.allow_missing)
    print(json.dumps(result.to_dict(), indent=2) if args.json else result.summary())
    for finding in result.findings[:50]:
        print(f"  finding: rule={finding['rule']} path={finding['path']} line={finding['line']}")
    return exit_code(result)


if __name__ == "__main__":
    sys.exit(main())
