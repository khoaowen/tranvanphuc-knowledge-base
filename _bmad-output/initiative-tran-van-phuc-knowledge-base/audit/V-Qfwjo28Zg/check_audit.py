#!/usr/bin/env python3
"""Read-only checker for the V-Qfwjo28Zg audit. Run from the repo root; exits non-zero on any failure."""
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True  # importing scripts/ must not write __pycache__ into the tree
ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "scripts"))
import fidelity  # noqa: E402
import queue_state  # noqa: E402

VIDEO_ID = "V-Qfwjo28Zg"
AUDIT = Path("_bmad-output/initiative-tran-van-phuc-knowledge-base/audit")
A = AUDIT / VIDEO_ID
VIDEO_DIR = Path(
    "videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu"
)
TRANSCRIPT = VIDEO_DIR / "transcript.md"
BOUND_REV = "4e31e57^"
BOUND_SHA = "fbae11bf16fa47c8055fe7b309f45dfeb696db23a0009c593504c1351a98203c"
CLASSES = {"supported", "attribution_qualification", "mismatch", "unresolved"}
PENDING = "pending-human-approval"

failures = []


def check(ok, message):
    print(("ok   " if ok else "FAIL ") + message)
    if not ok:
        failures.append(message)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, check=True).stdout


def load(name):
    return json.loads((A / name).read_text(encoding="utf-8"))


def verify_quotes(name):
    """Run verify_quotes.py and return (passed, quote count, failure count)."""
    run = subprocess.run(
        [sys.executable, str(AUDIT / "verify_quotes.py"), VIDEO_ID, str(TRANSCRIPT), str(A / name)],
        capture_output=True, text=True,
    )
    match = re.search(r"quotes (\d+) failures (\d+)", run.stdout)
    if run.returncode or not match:
        print(run.stdout + run.stderr)
    quotes, bad = (int(match.group(1)), int(match.group(2))) if match else (0, -1)
    return run.returncode == 0 and bad == 0, quotes, bad


records = load("final_records.json")
corrections = load("proposed-corrections.json")
anchors = load("omission-anchors.json")
by_id = {r["id"]: r for r in records}

# Bound summary extraction equals the records.
summary_bytes = git("show", f"{BOUND_REV}:{VIDEO_DIR.as_posix()}/summary.md")
check(hashlib.sha256(summary_bytes).hexdigest() == BOUND_SHA, "bound summary SHA-256 matches")
claims = fidelity.extract_claims(summary_bytes.decode("utf-8"))
diffs = [
    c["id"] for c, r in zip(claims, records)
    if (c["id"], c["section"], c["claim"]) != (r["id"], r["section"], r["claim"])
]
check(len(claims) == len(records) == 554 and not diffs,
      f"extraction equals final_records on id, section, claim ({len(claims)} claims, {len(diffs)} differences)")

# Classes, evidence, pass 2.
counts = Counter(r["class"] for r in records)
check(set(counts) <= CLASSES, f"classes allowed: {dict(counts)}")
no_evidence = [r["id"] for r in records if r["class"] != "unresolved" and not r["evidence"]]
check(not no_evidence, f"every non-unresolved record has evidence (missing: {no_evidence})")
non_supported = {r["id"] for r in records if r["class"] != "supported"}
pass2 = {r["id"] for r in records if r.get("pass2_class")}
check(non_supported <= pass2,
      f"pass 2 covers every non-supported id ({len(pass2)} total, missing {sorted(non_supported - pass2)})")

# Quotes.
total_bad = 0
for name in ("final_records.json", "omission-anchors.json", "proposed-corrections.json"):
    passed, quotes, bad = verify_quotes(name)
    total_bad += bad if bad >= 0 else 1
    check(passed, f"verify_quotes {name}: {quotes} quotes, {bad} failures")

# Corrections.
ids = [c["id"] for c in corrections]
check(len(ids) == len(set(ids)) and set(ids) == non_supported,
      f"corrections are exactly the non-supported ids ({len(ids)})")
pending = sum(c["status"] == PENDING for c in corrections)
check(pending == len(corrections) and pending == 63, f"corrections pending: {pending}")
check(all(c["id"] in by_id and c["current"] == by_id[c["id"]]["claim"] and c["class"] == by_id[c["id"]]["class"]
          for c in corrections), "each correction's current text and class equal its record")
check(all(c["proposed"].strip() and c["why"].strip() for c in corrections), "each correction has proposed and why")
check([c["id"] for c in corrections if not c["evidence"]] == ["c541"], "only c541 has no supporting quote")

# Generated markdown agrees with its data.
corrections_md = (A / "proposed-corrections.md").read_text(encoding="utf-8")
check(BOUND_SHA in corrections_md and all(
    f"## {c['id']}\n- **status:** {PENDING}\n" in corrections_md and c["proposed"] in corrections_md
    for c in corrections), "proposed-corrections.md matches its JSON and names the bound SHA")
omissions_md = (A / "omissions.md").read_text(encoding="utf-8")
check(all(f"### {a['id']} " in omissions_md and a["evidence"][0]["quote"] in omissions_md for a in anchors)
      and omissions_md.count("\n### o") == len(anchors), f"omissions.md matches omission-anchors.json ({len(anchors)})")

# Nothing published or changed under videos/.
check(not git("diff", "origin/main", "--", "videos/"), "videos/ diff against origin/main is empty")
check(queue_state.publishable(VIDEO_DIR) is False, "publishable(video_dir) is False")

print(f"records {len(records)}; quote failures {total_bad}; corrections {len(corrections)}, pending {pending}; "
      f"omissions {len(anchors)}; pass 2 {len(pass2)}; classes {dict(counts)}")
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed; publication status: blocked")
