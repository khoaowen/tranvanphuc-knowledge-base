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
    """Run git; a missing ref or shallow clone is reported as a FAIL line, not a traceback."""
    run = subprocess.run(["git", *args], capture_output=True)
    if run.returncode:
        check(False, f"git {' '.join(args)} failed: {run.stderr.decode('utf-8', 'replace').strip()}")
        print(f"{len(failures)} check(s) failed")
        sys.exit(1)
    return run.stdout


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
additional = load("additional-corrections.json")
overrides = load("effective-overrides.json")
decisions = load("decisions.json")["decisions"]
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

# Effective classes: overrides supersede final_records.json without rewriting it.
override_ids = [o["id"] for o in overrides]
check(len(override_ids) == len(set(override_ids)) and all(i in by_id for i in override_ids),
      f"overrides are unique and name known claims ({override_ids})")
check(all(o["original_class"] == by_id[o["id"]]["class"] and o["effective_class"] in CLASSES
          and o["effective_class"] != o["original_class"] and o["evidence"] and o["reason"].strip()
          for o in overrides), "each override states the record's class, a different allowed class, a reason and evidence")
effective = {r["id"]: r["class"] for r in records}
effective.update({o["id"]: o["effective_class"] for o in overrides})
eff_counts = Counter(effective.values())
eff_non_supported = {i for i, c in effective.items() if c != "supported"}
override_pass2 = {o["id"]: o for o in overrides}
check(all(o.get("pass2_class") in CLASSES and o["pass2_class"] == o["effective_class"] and o["pass2_note"].strip()
          for o in overrides if o["effective_class"] != "supported"),
      "every newly non-supported override has an agreeing second pass")
pass2_all = pass2 | {i for i, o in override_pass2.items() if o.get("pass2_class")}
check(eff_non_supported <= pass2_all,
      f"pass 2 covers every effectively non-supported id (missing {sorted(eff_non_supported - pass2_all)})")
sampled = {r["id"] for r in records if r.get("pass2_class") and r["class"] == "supported"}
pass2_total = len(pass2_all)

# Additional corrections: supplemental quotes, statuses, text equality, markdown agreement.
add_ids = [c["id"] for c in additional]
check(len(add_ids) == len(set(add_ids)) and all(i in by_id for i in add_ids), f"additional corrections unique and known ({len(add_ids)})")
if not all(i in by_id for i in add_ids):
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
check(all(c["status"] == PENDING for c in additional), "all additional corrections are pending-human-approval")
check(all(c["current"] == by_id[c["id"]]["claim"] and c["class"] == by_id[c["id"]]["class"]
          and c["proposed"].strip() and c["why"].strip() and c["evidence"] for c in additional),
      "each additional correction's current text and class equal its record, with proposed, why and evidence")
check(set(override_ids) <= set(add_ids), "every overridden claim has an additional correction")
additional_md = (A / "additional-corrections.md").read_text(encoding="utf-8")
add_sections = {x.split("\n", 1)[0]: x for x in additional_md.split("\n## ")[1:]}


def additional_matches(c):
    section = add_sections.get(c["id"], "")
    return (f"- **status:** {PENDING}\n" in section
            and all(f"- **{f}:** {c[f]}\n" in section for f in ("class", "current", "proposed", "why"))
            and all(f"[{e['timestamp']}]: \"{e['quote']}\"\n" in section for e in c["evidence"]))


bad_add = [c["id"] for c in additional if not additional_matches(c)]
check(BOUND_SHA in additional_md and set(add_sections) == set(add_ids) and not bad_add
      and f"{len(add_ids)} mục" in additional_md,
      f"additional-corrections.md matches its JSON per item (mismatched: {bad_add})")

# Quotes.
total_bad = 0
for name in ("final_records.json", "omission-anchors.json", "proposed-corrections.json",
             "additional-corrections.json", "effective-overrides.json"):
    passed, quotes, bad = verify_quotes(name)
    total_bad += bad if bad >= 0 else 1
    check(passed, f"verify_quotes {name}: {quotes} quotes, {bad} failures")

# Corrections.
ids = [c["id"] for c in corrections]
check(len(ids) == len(set(ids)) and set(ids) == non_supported,
      f"corrections are exactly the non-supported ids ({len(ids)})")
pending = sum(c["status"] == PENDING for c in corrections)
check(pending == len(corrections) == len(non_supported), f"corrections pending: {pending}")
overlap = sorted(set(add_ids) & set(ids))
check(all(c.get("supersedes") == "proposed-corrections.json" for c in additional if c["id"] in overlap)
      and all(f"- **supersedes:** proposed-corrections.json" in add_sections[i] for i in overlap),
      f"ids in both correction files declare that the additional entry supersedes ({overlap})")
check(all(i in by_id for i in decisions),
      f"decisions.json names known claims ({len(decisions)})")
check(all(v in {"keep-original", "drop", "keep-with-label", "apply-proposed-when-approved"} for v in decisions.values())
      and all(c["status"] == PENDING for c in corrections + additional),
      "decisions are recorded without applying any correction (all items still pending)")
check(not [i for i, v in decisions.items() if v == "keep-original" and i in add_ids],
      "no keep-original decision targets an additional correction")
check(non_supported | set(override_ids) == eff_non_supported,
      f"effective non-supported = historical non-supported plus overrides ({len(eff_non_supported)})")
check(all(c["id"] in by_id and c["current"] == by_id[c["id"]]["claim"] and c["class"] == by_id[c["id"]]["class"]
          for c in corrections), "each correction's current text and class equal its record")
check(all(c["proposed"].strip() and c["why"].strip() for c in corrections), "each correction has proposed and why")
no_quote = [c["id"] for c in corrections if not c["evidence"]]
check(all(by_id[i]["class"] == "unresolved" for i in no_quote), f"only unresolved corrections lack a supporting quote ({no_quote})")

# Generated markdown agrees with its data.
corrections_md = (A / "proposed-corrections.md").read_text(encoding="utf-8")
sections = {s.split("\n", 1)[0]: s for s in corrections_md.split("\n## ")[1:]}


def section_matches(c):
    """Every field of a correction, and each quote with its timestamp, appears in that item's own section."""
    section = sections.get(c["id"], "")
    return (f"- **status:** {PENDING}\n" in section
            and all(f"- **{field}:** {c[field]}\n" in section for field in ("current", "proposed", "why"))
            and all(f"[{e['timestamp']}]: \"{e['quote']}\"\n" in section for e in c["evidence"]))


mismatched = [c["id"] for c in corrections if not section_matches(c)]
check(BOUND_SHA in corrections_md and set(sections) == set(ids) and not mismatched,
      f"proposed-corrections.md matches its JSON per item and names the bound SHA (mismatched: {mismatched})")
omissions_md = (A / "omissions.md").read_text(encoding="utf-8")
check(all(f"### {a['id']} " in omissions_md and a["evidence"][0]["quote"] in omissions_md for a in anchors)
      and omissions_md.count("\n### o") == len(anchors), f"omissions.md matches omission-anchors.json ({len(anchors)})")

# Summary and omissions agree with the data.
summary_md = (A / "audit-summary.md").read_text(encoding="utf-8")
excluded_rows = len(re.findall(r"^\| (?:\d+#\d+|o\d+) \|", omissions_md.split("## Excluded candidates", 1)[1], re.M))
kept = len(anchors)
check(f"{kept} kept (" in omissions_md and f"{excluded_rows} excluded" in omissions_md
      and f"**Omissions:** {kept} kept, {excluded_rows} candidates excluded" in summary_md,
      f"omission counts agree across omissions.md and audit-summary.md ({kept} kept, {excluded_rows} excluded)")
check("o48-o50" in omissions_md.split("## Result", 1)[0] and "sequential read" in omissions_md.split("## Result", 1)[0],
      "omissions.md method covers the later sequential read (o48-o50)")
expected = ", ".join(f"{k} {eff_counts[k]}" for k in ("supported", "attribution_qualification", "mismatch", "unresolved"))
check(f"**Classes (effective):** {expected}." in summary_md,
      f"audit-summary.md reports the effective classes ({expected})")
check(f"**Pass-2 coverage:** {pass2_total} claims" in summary_md,
      f"audit-summary.md reports pass-2 coverage ({pass2_total})")

# Nothing published or changed under videos/.
check(not git("diff", "origin/main", "--", "videos/"), "videos/ diff against origin/main is empty (origin/main as last fetched)")
check(not git("status", "--porcelain", "--", "videos/"), "videos/ has no uncommitted or untracked changes")
check(not (VIDEO_DIR / "summary.md").exists(), "summary.md is absent from videos/, so publishable() below reflects an absent summary")
check(queue_state.publishable(VIDEO_DIR) is False, "publishable(video_dir) is False")

print(f"records {len(records)}; quote failures {total_bad}; corrections {len(corrections)}, pending {pending}; "
      f"omissions {len(anchors)}; pass 2 {pass2_total}; historical classes {dict(counts)}; effective classes {dict(eff_counts)}")
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed; publication status: blocked")
