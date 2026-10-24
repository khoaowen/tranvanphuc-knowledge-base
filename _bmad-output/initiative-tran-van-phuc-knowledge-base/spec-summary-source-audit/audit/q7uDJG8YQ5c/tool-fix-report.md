# Step 1 — tool fix for q7uDJG8YQ5c

Date: 2026-10-18. Status: implemented, uncommitted, pending human review. Steps 2–4 have not started.

## Result

Claims can use authentic evidence from anywhere in the transcript. Review aggregation no longer rejects a quote solely because its timestamp falls outside the summary section. The publication gate follows the same rule.

The existing verbatim check is unchanged: it matches consecutive transcript words after normalizing case, punctuation, whitespace and caption boundaries. Evidence timestamps must still overlap the actual quote occurrence. Model checks for support, attribution, preserved qualifications and contradictions are unchanged, as are coverage, concerns, claim inventory and exact-summary hash binding.

Changed production files: `scripts/review_summaries.py` and `scripts/queue_state.py`. No edit to `scripts/fidelity.py` was necessary.

## Pre-change impact check

Before changing production code, inspected both existing video reviews and ran a read-only simulation in memory. No model was called and no review was rewritten. The repository contains two video directories; **V-Qfwjo28Zg is the glutathione video**.

The simulation promoted only failures whose issues were exclusively the section-window rejection, whose attribution and qualification checks passed, and whose issue quotes and timestamps were independently verified against their transcript. It retained content findings, concerns and coverage results.

| Video | Stored verdict | Projected overall verdict | Window-only claims eligible to pass | Coverage | Publishable before / projected |
| --- | --- | --- | --- | --- | --- |
| q7uDJG8YQ5c, Omega-3 | fail | fail | 7 | false, 17 omissions | false / false |
| V-Qfwjo28Zg, glutathione | fail | fail | 106 | false, 2 omissions | false / false |

**No overall verdict changes.** Omega-3's seven eligible claims are c002, c014–c017, c116 and c121. Holding the stored model findings fixed, they would bring its claim results to 160 pass, while incomplete coverage would still force an overall fail.

For glutathione, c443 has a mixed window/content finding and was left unresolved in this conservative simulation. Its content failures, five concerns and omissions remain blockers. Its stored review is already rejected by `completed_review`: it contains 561 claims while the current extractor derives 554, with mismatches starting at c301. Its summary hash matches. This pre-existing inventory mismatch is unchanged and was not repaired. The simulation is an impact estimate from stored findings, not a new fidelity review.

After the code change, actual stored verdicts remain fail for both videos; actual `queue_state.publishable` is false for both. Stored claim statuses remain 153 pass / 7 fail for Omega-3 and 403 pass / 155 fail / 3 flag for glutathione. Existing failed reviews are not silently upgraded or rerun.

## Validation

- Updated regression tests first: the new acceptance expectations failed in the old aggregator and old gate, demonstrating both obsolete restrictions.
- Full suite: `python3 -m unittest discover -s tests -v` — **86 tests passed**.
- Tests cover authentic quotes before and after a section, all four adverse semantic checks on cross-section evidence, and gate rejection of fabricated quotes, wrong timestamps and malformed timestamps. Existing tests retain coverage, stale-hash, missing-evidence and inventory protection.
- `git diff --check -- scripts/review_summaries.py scripts/queue_state.py tests/test_review_summaries.py` — passed.
- Bmad-build quick code review by an independent reviewer: **no findings**. Thorough review lenses were not run for this oneshot change.

## Protected files and checkpoint

Omega-3 transcript SHA-256 before and after:

`bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`

The manifest of all video files plus V-Qfwjo28Zg audit files and `proposed-corrections.r1.md` is identical before and after: 94 files, digest `61e215231ac543a6560a63d8ed8bcbecf32a1efcaa0aebcb334706d3d0285384`. The manifest hashes each sorted repository-relative path, NUL, and that file's SHA-256 bytes.

All video summaries, transcripts and reviews are byte-identical to the start of this step. Approved correction text, V-Qfwjo28Zg's audit and ticket 1.12 were not edited. Nothing was staged, committed, pushed or published. Existing accepted working-tree changes were preserved.

Workflow plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/tickets/story-apply-approved-corrections-q7uDJG8YQ5c-plan.md`.

**Stopped for the human's step-1 review.** The next authorized stage, after that review, is drafting the 17 omission proposals as pending-human-approval; no summary addition has been drafted or applied during this step.

## Complete code and test diff

```diff
diff --git a/scripts/queue_state.py b/scripts/queue_state.py
index dcfadfa..0926534 100644
--- a/scripts/queue_state.py
+++ b/scripts/queue_state.py
@@ -75,13 +75,12 @@ def current_review(video_dir):
             return None
         if data.get("concerns") or any(c["status"] != "pass" or c.get("issues") for c in claims):
             return None
-        for claim, derived in zip(claims, expected):
+        for claim in claims:
             if (any(claim.get(k) is not True for k in ("supported", "attributed", "qualifications_preserved"))
                     or not claim["evidence"]):
                 return None
             for ev in claim["evidence"]:
-                if (not fidelity.evidence_timestamp_matches(ev.get("quote"), ev.get("timestamp"), transcript)
-                        or not fidelity.in_section_window(derived, ev.get("timestamp"))):
+                if not fidelity.evidence_timestamp_matches(ev.get("quote"), ev.get("timestamp"), transcript):
                     return None
         return data
     except (OSError, ValueError, TypeError, AttributeError, KeyError):
diff --git a/scripts/review_summaries.py b/scripts/review_summaries.py
index 6c3e715..2950962 100644
--- a/scripts/review_summaries.py
+++ b/scripts/review_summaries.py
@@ -17,7 +17,7 @@ import queue_state  # noqa: E402
 import review_batch  # noqa: E402
 import summarize  # noqa: E402
 from fidelity import (candidate_chunks, evidence_timestamp_matches, extract_claims,  # noqa: E402,F401
-                      in_section_window, resolve_quote)
+                      resolve_quote)
 
 DEFAULT_CHUNK_CHARS = 40000
 OVERLAP_CHARS = 4000
@@ -233,35 +233,30 @@ def parse_coverage_audit(text, transcript):
 def aggregate_claim(claim, evidences):
     """Combine every chunk's in-slice report of one claim into a single result.
 
-    pass: >=1 clean verbatim evidence located inside the claim's section window, nothing
-          contradicting or defective.
-    fail: contradicted, wrong attribution/qualification, clean evidence only outside the section's
-          timestamp window (wrong timestamp), evidence that never supports the claim, or no
-          evidence at all.
+    pass: >=1 clean verbatim evidence anywhere in the transcript, nothing contradicting or defective.
+    fail: contradicted, wrong attribution/qualification, evidence that never supports the claim,
+          or no evidence at all.
     flag: one slice calls the claim merely unsupported while another gives clean support.
     """
     clean = [e for e in evidences if e["supported"] and e["attributed"] and e["qualifications_preserved"]
              and not e["contradicts"]]
-    located = [e for e in clean if in_section_window(claim, e["timestamp"])]
     hard = [e for e in evidences if e["contradicts"] or not e["attributed"] or not e["qualifications_preserved"]]
     soft = [e for e in evidences if e not in clean and e not in hard]  # merely supported == False
-    misplaced = [dict(e, finding="evidence found at " + str(e["timestamp"]) + ", outside the section's timestamp window")
-                 for e in clean if e not in located]
     if hard:
         status, issues = "fail", hard
-    elif not located:
-        status, issues = "fail", soft + misplaced
+    elif not clean:
+        status, issues = "fail", soft
     elif soft:
         status, issues = "flag", soft
     else:
         status, issues = "pass", []
-    best = (located or evidences or [None])[0]
+    best = (clean or evidences or [None])[0]
     result = {"id": claim["id"], "claim": claim["claim"], "section": claim["section"], "status": status,
-              "supported": bool(located) and not hard,
+              "supported": bool(clean) and not hard,
               "attributed": bool(evidences) and all(e["attributed"] for e in evidences),
               "qualifications_preserved": bool(evidences) and all(e["qualifications_preserved"] for e in evidences),
               "timestamp": best["timestamp"] if best else None, "quote": best["quote"] if best else None,
-              "evidence": [{k: e[k] for k in ("chunk", "timestamp", "quote")} for e in located],
+              "evidence": [{k: e[k] for k in ("chunk", "timestamp", "quote")} for e in clean],
               "issues": [{k: e.get(k) for k in ("chunk", "timestamp", "quote", "finding")} for e in issues]}
     for issue, e in zip(result["issues"], issues):
         if e.get("unverified_quote"):
diff --git a/tests/test_review_summaries.py b/tests/test_review_summaries.py
index d8a2303..38aa8d4 100644
--- a/tests/test_review_summaries.py
+++ b/tests/test_review_summaries.py
@@ -274,18 +274,32 @@ class AggregationTests(unittest.TestCase):
         self.assertIn("never", prompts[0].lower())
         self.assertNotIn("coverage_complete", prompts[0])
 
-    def test_evidence_outside_section_window_is_a_wrong_timestamp(self):
-        # section [00:00:01] has a later section at 00:10:00, so its window ends ~00:12:00
-        summary = "## [00:00:01] A\n- dòng số 1 nội dung.\n## [00:10:00] B\n- dòng số 2 nội dung.\n"
+    def test_verbatim_evidence_before_or_after_section_passes(self):
+        summary = "## [00:00:01] A\n- dòng số 2 nội dung.\n## [00:10:00] B\n- dòng số 1 nội dung.\n## [00:20:00] C\n"
         transcript = "[00:00:01] dòng số 1 nội dung\n[00:30:00] dòng số 2 nội dung\n"
         def client(prompt):
-            return resp([entry("c001", "dòng số 2 nội dung"), entry("c002", "dòng số 2 nội dung")])
+            return resp([entry("c001", "dòng số 2 nội dung"), entry("c002", "dòng số 1 nội dung")])
         result, publishable = run(client, summary, transcript)
-        self.assertEqual(by_id(result)["c002"]["status"], "pass")
-        c1 = by_id(result)["c001"]
-        self.assertEqual(c1["status"], "fail")
-        self.assertIn("outside the section's timestamp window", c1["issues"][0]["finding"])
-        self.assertFalse(publishable)
+        self.assertEqual(result["verdict"], "pass")
+        self.assertTrue(publishable)
+        for cid, timestamp in (("c001", "00:30:00"), ("c002", "00:00:01")):
+            claim = by_id(result)[cid]
+            self.assertEqual(claim["status"], "pass")
+            self.assertEqual(claim["evidence"][0]["timestamp"], timestamp)
+            self.assertEqual(claim["issues"], [])
+
+    def test_cross_section_evidence_does_not_excuse_content_failures(self):
+        summary = "## [00:00:01] A\n- Có thể hỗ trợ sức khỏe.\n## [00:10:00] B\n"
+        transcript = "[00:30:00] Có thể hỗ trợ sức khỏe.\n"
+        for failed_check, value in (("supported", False), ("attributed", False),
+                                    ("qualifications_preserved", False), ("contradicts", True)):
+            with self.subTest(check=failed_check):
+                result, publishable = run(lambda prompt: resp([
+                    entry("c001", "Có thể hỗ trợ sức khỏe.", finding="content defect",
+                          **{failed_check: value})]), summary, transcript)
+                self.assertEqual(result["verdict"], "fail")
+                self.assertEqual(by_id(result)["c001"]["status"], "fail")
+                self.assertFalse(publishable)
 
     def test_glossary_table_rows_are_not_claims(self):
         claims = fidelity.extract_claims(SUMMARY + "\n## [00:00:09] Glossary\n| A | B |\n| --- | --- |\n")
@@ -485,7 +499,7 @@ class ReviewedDefectRegressionTests(unittest.TestCase):
         claims = fidelity.extract_claims("## [00:00:01] P\n- Đã gộp vào mục dinh dưỡng.\n- Vitamin có thể hỗ trợ sức khỏe.\n")
         self.assertEqual([c["claim"] for c in claims], ["Vitamin có thể hỗ trợ sức khỏe."])
 
-    def test_strict_pass_rejects_authentic_evidence_outside_derived_window(self):
+    def test_strict_pass_accepts_cross_section_quote_but_rejects_invalid_evidence(self):
         with tempfile.TemporaryDirectory() as tmp:
             summary = "## [00:00:01] A\n- Có thể hỗ trợ sức khỏe.\n- Không phải lúc nào cũng đúng.\n## [00:40:00] B\n"
             transcript = TRANSCRIPT + "[00:50:00] Có thể hỗ trợ sức khỏe.\n"
@@ -495,7 +509,14 @@ class ReviewedDefectRegressionTests(unittest.TestCase):
             changed = json.loads((d / "review.md").read_text(encoding="utf-8"))
             changed["claims"][0]["evidence"] = [{"timestamp": "00:50:00", "quote": "Có thể hỗ trợ sức khỏe."}]
             (d / "review.md").write_text(json.dumps(changed, ensure_ascii=False), encoding="utf-8")
-            self.assertFalse(queue_state.publishable(d))
+            self.assertTrue(queue_state.publishable(d))
+            for evidence in ({"timestamp": "00:45:00", "quote": "Có thể hỗ trợ sức khỏe."},
+                             {"timestamp": "00:50:00", "quote": "bịa đặt"},
+                             {"timestamp": "invalid", "quote": "Có thể hỗ trợ sức khỏe."}):
+                with self.subTest(evidence=evidence):
+                    changed["claims"][0]["evidence"] = [evidence]
+                    (d / "review.md").write_text(json.dumps(changed, ensure_ascii=False), encoding="utf-8")
+                    self.assertFalse(queue_state.publishable(d))
 
     def test_completed_fail_or_incomplete_coverage_is_skipped_but_malformed_is_queued(self):
         with tempfile.TemporaryDirectory() as tmp:
```
