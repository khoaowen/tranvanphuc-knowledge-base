import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import fidelity  # noqa: E402
import queue_state  # noqa: E402
import review_summaries  # noqa: E402
import review_summaries as r  # noqa: E402

TRANSCRIPT = "[00:00:01] Mở đầu.\n[00:00:02] Có thể hỗ trợ sức khỏe.\n[00:00:03] Không phải lúc nào cũng đúng.\n"
SUMMARY = ("# T\n\n> Health disclaimer.\n\n## [00:00:01] Phần một — https://x/y\n\n**Q: Hỏi?**\n"
           "- Có thể hỗ trợ sức khỏe.\n- Không phải lúc nào cũng đúng.\n")
OK = dict(status="in_slice", supported=True, attributed=True, qualifications_preserved=True,
          contradicts=False, finding="")


def entry(cid, quote, **over):
    return {"id": cid, "quote": quote, **{**OK, **over}}


def resp(claims=(), concerns=(), omitted=()):
    return json.dumps({"claims": list(claims), "concerns": list(concerns),
                       "omitted_topics": list(omitted)}, ensure_ascii=False)


FULL = resp([entry("c001", "Có thể hỗ trợ sức khỏe."), entry("c002", "Không phải lúc nào cũng đúng.")])


def make(d, summary=SUMMARY, transcript=TRANSCRIPT, vid="v"):
    d = Path(d)
    (d / "summary.md").write_text(summary, encoding="utf-8")
    (d / "transcript.md").write_text(transcript, encoding="utf-8")
    (d / "metadata.json").write_text(json.dumps({"video_id": vid}), encoding="utf-8")
    return d


def fill(client):
    """Wrap a test client: every claim listed in the prompt but not answered is not_in_slice."""
    import re as _re
    def wrapped(prompt):
        data = json.loads(client(prompt))
        if "claims" not in data:
            return json.dumps(data, ensure_ascii=False)  # coverage-audit reply
        listed = _re.findall(r"^\[(c\d+)\]", prompt.split("<timestamped_transcript>")[0], _re.M)
        answered = {c["id"] for c in data["claims"]}
        data["claims"] += [{"id": i, "status": "not_in_slice"} for i in listed if i not in answered]
        return json.dumps(data, ensure_ascii=False)
    return wrapped


def run(client, summary=SUMMARY, transcript=TRANSCRIPT, **kw):
    with tempfile.TemporaryDirectory() as tmp:
        d = make(tmp, summary, transcript)
        result = review_summaries.review_video(d, fill(client), sleep=lambda s: None, **kw)
        return result, queue_state.publishable(d)


def by_id(result):
    return {c["id"]: c for c in result["claims"]}


LONG = "".join(f"[00:00:{i:02d}] dòng số {i} nội dung\n" for i in range(1, 9))
LONG_SUMMARY = "## [00:00:01] P\n- dòng số 1 nội dung.\n- dòng số 4 nội dung.\n- dòng số 8 nội dung.\n"


def has(prompt, n):
    """True if transcript line n is inside this chunk's slice."""
    return f"dòng số {n} nội dung" in prompt.split("<timestamped_transcript>")[1]


class AggregationTests(unittest.TestCase):
    def test_claims_extracted_deterministically(self):
        claims = fidelity.extract_claims(SUMMARY)
        self.assertEqual([c["id"] for c in claims], ["c001", "c002"])
        self.assertEqual(claims[0]["claim"], "Có thể hỗ trợ sức khỏe.")
        self.assertIn("Phần một", claims[0]["section"])

    def test_claim_evidenced_in_only_one_of_several_chunks_passes(self):
        summary = "## [00:00:01] P\n- dòng số 4 nội dung.\n- dòng số 8 nội dung.\n"
        def client(prompt):
            out = []
            if has(prompt, 4):
                out.append(entry("c001", "dòng số 4 nội dung"))
            if has(prompt, 8):
                out.append(entry("c002", "dòng số 8 nội dung"))
            return resp(out)  # every other chunk reports nothing: out of slice
        result, publishable = run(client, summary, LONG, chunk_chars=70, overlap_chars=0)
        self.assertGreaterEqual(result["chunks"], 3)
        self.assertEqual(result["verdict"], "pass")
        self.assertTrue(publishable)
        self.assertEqual(by_id(result)["c001"]["evidence"][0]["timestamp"], "00:00:04")

    def test_out_of_slice_claim_is_not_penalized_but_missing_evidence_fails(self):
        out = resp([{"id": "c001", "status": "not_in_slice"}, entry("c002", "Không phải lúc nào cũng đúng.")])
        result, publishable = run(lambda p: out)
        # c001 has no evidence in any chunk -> fail, but only because nothing anywhere supports it
        self.assertEqual(by_id(result)["c002"]["status"], "pass")
        self.assertEqual(by_id(result)["c001"]["status"], "fail")
        self.assertEqual(by_id(result)["c001"]["issues"][0]["finding"], "no transcript evidence found in any chunk")
        self.assertEqual(result["verdict"], "fail")
        self.assertFalse(publishable)

    def test_not_in_slice_in_one_chunk_with_evidence_in_another_passes(self):
        summary = "## [00:00:01] P\n- dòng số 1 nội dung.\n- dòng số 8 nội dung.\n"
        def client(prompt):
            out = [{"id": "c001", "status": "not_in_slice"}, {"id": "c002", "status": "not_in_slice"}]
            if has(prompt, 1):
                out[0] = entry("c001", "dòng số 1 nội dung")
            if has(prompt, 8):
                out[1] = entry("c002", "dòng số 8 nội dung")
            return resp(out)
        result, publishable = run(client, summary, LONG, chunk_chars=70, overlap_chars=0)
        self.assertEqual(result["verdict"], "pass")
        self.assertTrue(publishable)

    def test_claim_without_evidence_anywhere_fails(self):
        result, publishable = run(lambda p: resp([entry("c001", "Có thể hỗ trợ sức khỏe.")]))
        self.assertEqual(by_id(result)["c002"]["status"], "fail")
        self.assertEqual(result["verdict"], "fail")
        self.assertFalse(publishable)

    def test_empty_review_never_passes(self):
        result, publishable = run(lambda p: resp())
        self.assertEqual(result["verdict"], "fail")
        self.assertFalse(publishable)

    def test_contradicting_chunk_fails_even_if_another_supports(self):
        summary = "## [00:00:01] P\n- dòng số 1 nội dung.\n"
        def client(prompt):
            if has(prompt, 1):
                return resp([entry("c001", "dòng số 1 nội dung")])
            if has(prompt, 8):
                return resp([entry("c001", "dòng số 8 nội dung", supported=False, contradicts=True, finding="khác số")])
            return resp()
        result, publishable = run(client, summary, LONG, chunk_chars=70, overlap_chars=0)
        c = by_id(result)["c001"]
        self.assertEqual(c["status"], "fail")
        self.assertEqual(c["issues"][0]["finding"], "khác số")
        self.assertEqual(result["verdict"], "fail")
        self.assertFalse(publishable)

    def test_each_hardened_check_fails(self):
        for field in ("attributed", "qualifications_preserved"):
            with self.subTest(field=field):
                bad = entry("c001", "Có thể hỗ trợ sức khỏe.", finding="x", **{field: False})
                result, publishable = run(lambda p: resp([bad, entry("c002", "Không phải lúc nào cũng đúng.")]))
                self.assertEqual(by_id(result)["c001"]["status"], "fail")
                self.assertFalse(publishable)

    def test_unresolved_unsupported_with_clean_support_elsewhere_flags(self):
        summary = "## [00:00:01] P\n- dòng số 4 nội dung.\n"
        def client(prompt):
            if has(prompt, 1):
                return resp([entry("c001", "dòng số 1 nội dung", supported=False, finding="chỉ nhắc một phần")])
            if has(prompt, 4):
                return resp([entry("c001", "dòng số 4 nội dung")])
            return resp()
        result, publishable = run(client, summary, LONG, chunk_chars=70, overlap_chars=0)
        self.assertEqual(by_id(result)["c001"]["status"], "flag")
        self.assertEqual(result["verdict"], "flag")
        self.assertFalse(publishable)

    def test_overlap_boundary_claim_seen_by_both_chunks_passes(self):
        summary = "## [00:00:01] P\n- dòng số 4 nội dung.\n"
        entries = [(i, f"[00:00:{i:02d}] dòng số {i} nội dung") for i in range(1, 9)]
        chunks = review_summaries.chunk_overlapping(entries, max_chars=100, overlap_chars=60)
        shared = set(chunks[0]) & set(chunks[1])
        self.assertTrue(any("số 4 " in e[1] or "số 5 " in e[1] or "số 3 " in e[1] for e in shared))
        seen = []
        def client(prompt):
            seen.append(prompt)
            return resp([entry("c001", "dòng số 4 nội dung")]) if has(prompt, 4) else resp()
        result, publishable = run(client, summary, LONG, chunk_chars=100, overlap_chars=60)
        c = by_id(result)["c001"]
        self.assertGreaterEqual(len(c["evidence"]), 2)  # both overlapping chunks report it
        self.assertEqual(result["verdict"], "pass")
        self.assertTrue(publishable)

    def test_coverage_audit_failure_fails(self):
        omitted = {"topic": "cảnh báo", "quote": "Mở đầu"}
        audit = json.dumps({"coverage_complete": False, "omissions": [omitted]}, ensure_ascii=False)
        def client(prompt):
            return audit if "final whole-summary coverage auditor" in prompt else resp(
                [entry("c001", "Có thể hỗ trợ sức khỏe."), entry("c002", "Không phải lúc nào cũng đúng.")], omitted=[omitted])
        result, publishable = run(client)
        self.assertFalse(result["coverage_complete"])
        self.assertEqual(result["omissions"][0]["topic"], "cảnh báo")
        self.assertEqual(result["verdict"], "fail")
        self.assertFalse(publishable)

    def test_coverage_audit_can_dismiss_candidate_omissions(self):
        omitted = {"topic": "chào hỏi", "quote": "Mở đầu"}
        audit = json.dumps({"coverage_complete": True, "omissions": []})
        def client(prompt):
            return audit if "final whole-summary coverage auditor" in prompt else resp(
                [entry("c001", "Có thể hỗ trợ sức khỏe."), entry("c002", "Không phải lúc nào cũng đúng.")], omitted=[omitted])
        result, publishable = run(client)
        self.assertEqual(result["verdict"], "pass")
        self.assertTrue(publishable)

    def test_audit_with_fabricated_omission_quote_is_rejected(self):
        with self.assertRaises(review_summaries.ReviewError):
            review_summaries.parse_coverage_audit(
                json.dumps({"coverage_complete": False, "omissions": [{"topic": "t", "quote": "bịa đặt"}]}), TRANSCRIPT)

    def test_unknown_claim_id_and_non_verbatim_quote_rejected(self):
        ids = {"c001", "c002"}
        with self.assertRaises(review_summaries.ReviewError):
            review_summaries.parse_model_review(resp([entry("c999", "Mở đầu")]), TRANSCRIPT, ids)
        with self.assertRaises(review_summaries.ReviewError):
            review_summaries.parse_model_review(resp([entry("c001", "paraphrase")]), TRANSCRIPT, ids)
        with self.assertRaises(review_summaries.ReviewError):  # failed check needs a finding
            review_summaries.parse_model_review(resp([entry("c001", "Mở đầu", attributed=False)]), TRANSCRIPT, ids)

    def test_timestamp_is_computed_from_quote_not_trusted(self):
        e = entry("c001", "Có thể hỗ trợ sức khỏe.")
        e["timestamp"] = "00:09:09"
        data = review_summaries.parse_model_review(resp([e]), TRANSCRIPT, {"c001"})
        self.assertEqual(data["claims"][0]["timestamp"], "00:00:02")

    def test_material_concern_fails_minor_flags(self):
        for sev, verdict in (("material", "fail"), ("minor", "flag")):
            concern = {"severity": sev, "finding": "f", "quote": "Mở đầu"}
            result, publishable = run(lambda p: resp(
                [entry("c001", "Có thể hỗ trợ sức khỏe."), entry("c002", "Không phải lúc nào cũng đúng.")], [concern]))
            self.assertEqual(result["verdict"], verdict)
            self.assertFalse(publishable)

    def test_stale_hash_blocks_publication(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = make(tmp)
            review_summaries.review_video(d, fill(lambda p: FULL), sleep=lambda s: None)
            self.assertTrue(queue_state.publishable(d))
            (d / "summary.md").write_text(SUMMARY + "- Thêm một câu mới.\n", encoding="utf-8")
            self.assertFalse(queue_state.publishable(d))

    def test_pass_record_must_cover_every_summary_claim_and_verify_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = make(tmp)
            review_summaries.review_video(d, fill(lambda p: FULL), sleep=lambda s: None)
            good = json.loads((d / "review.md").read_text(encoding="utf-8"))
            for mutate in (lambda x: x["claims"].pop(),
                           lambda x: x["claims"][0]["evidence"][0].update(quote="bịa đặt"),
                           lambda x: x["claims"][0].update(evidence=[]),
                           lambda x: x.update(coverage_complete=False),
                           lambda x: x.update(omissions=[{"topic": "t"}]),
                           lambda x: x["claims"][0].update(claim="đã sửa")):
                bad = json.loads(json.dumps(good))
                mutate(bad)
                (d / "review.md").write_text(json.dumps(bad, ensure_ascii=False), encoding="utf-8")
                self.assertFalse(queue_state.publishable(d))
                if bad["claims"][0].get("evidence") and bad["claims"][0]["evidence"][0].get("quote") == "bịa đặt":
                    self.assertIsNone(queue_state.completed_review(d))
            (d / "review.md").write_text(json.dumps(good, ensure_ascii=False), encoding="utf-8")
            self.assertTrue(queue_state.publishable(d))

    def test_review_never_changes_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = make(tmp)
            before = (d / "summary.md").read_bytes()
            review_summaries.review_video(d, fill(lambda p: FULL), sleep=lambda s: None)
            self.assertEqual((d / "summary.md").read_bytes(), before)
            self.assertEqual(json.loads((d / "review.md").read_text(encoding="utf-8"))["summary_sha256"],
                             review_summaries.summary_hash(before))

    def test_chunk_prompt_does_not_demand_global_coverage(self):
        prompts = []
        run(lambda p: prompts.append(p) or FULL)
        self.assertIn("PART 1/1", prompts[0])
        self.assertIn("never", prompts[0].lower())
        self.assertNotIn("coverage_complete", prompts[0])

    def test_evidence_outside_section_window_is_a_wrong_timestamp(self):
        # section [00:00:01] has a later section at 00:10:00, so its window ends ~00:12:00
        summary = "## [00:00:01] A\n- dòng số 1 nội dung.\n## [00:10:00] B\n- dòng số 2 nội dung.\n"
        transcript = "[00:00:01] dòng số 1 nội dung\n[00:30:00] dòng số 2 nội dung\n"
        def client(prompt):
            return resp([entry("c001", "dòng số 2 nội dung"), entry("c002", "dòng số 2 nội dung")])
        result, publishable = run(client, summary, transcript)
        self.assertEqual(by_id(result)["c002"]["status"], "pass")
        c1 = by_id(result)["c001"]
        self.assertEqual(c1["status"], "fail")
        self.assertIn("outside the section's timestamp window", c1["issues"][0]["finding"])
        self.assertFalse(publishable)

    def test_glossary_table_rows_are_not_claims(self):
        claims = fidelity.extract_claims(SUMMARY + "\n## [00:00:09] Glossary\n| A | B |\n| --- | --- |\n")
        self.assertEqual([c["claim"] for c in claims], ["Có thể hỗ trợ sức khỏe.", "Không phải lúc nào cũng đúng."])

    def test_candidate_chunks_prefer_overlapping_chunk_and_never_loses_claim(self):
        claims = [{"id": "c001", "claim": "vitamin d giúp hấp thu canxi"}]
        chunks = ["[00:00:01] hôm nay nói về sắt", "[00:01:00] vitamin d giúp hấp thu canxi tốt", "[00:02:00] kết thúc"]
        chosen = fidelity.candidate_chunks(claims, chunks, top=1)
        self.assertEqual(chosen["c001"], {1})

    def test_unanswered_listed_claims_are_rejected_then_treated_as_no_evidence(self):
        with self.assertRaises(review_summaries.ReviewError):
            review_summaries.parse_model_review(resp([entry("c001", "Mở đầu")]), TRANSCRIPT, {"c001", "c002"})
        data = review_summaries.parse_model_review(resp([entry("c001", "Mở đầu")]), TRANSCRIPT, {"c001", "c002"}, salvage=True)
        self.assertEqual([c["id"] for c in data["claims"]], ["c001"])

    def test_resolve_quote_spans_lines(self):
        t = "[00:02:16] video ngắn\n[00:02:18] hoàn toàn không thể\n[00:02:20] đáp ứng được.\n"
        self.assertEqual(review_summaries.resolve_quote("Ngắn, hoàn toàn không thể đáp ứng", t), "00:02:16-00:02:20")
        self.assertIsNone(review_summaries.resolve_quote("bịa đặt", t))


class ReviewTests(unittest.TestCase):
    def test_chunks_overlap_on_timestamped_entry_boundaries(self):
        entries = [(i, f"[{i:02}:00:00] " + "x" * 20) for i in range(5)]
        chunks = review_summaries.chunk_overlapping(entries, max_chars=60, overlap_chars=40)
        self.assertEqual(chunks, [entries[:1], entries[:2], entries[1:3], entries[2:4], entries[3:]])
        for left, right in zip(chunks, chunks[1:]):
            self.assertEqual(left[-1], right[0])

    def test_long_transcript_chunks_cover_early_middle_late_and_boundaries(self):
        entries = [(i, f"[{i // 3600:02}:{(i // 60) % 60:02}:{i % 60:02}] " + "nội dung " * 8)
                   for i in range(60)]
        chunks = review_summaries.chunk_overlapping(entries, max_chars=350, overlap_chars=100)
        seen = [entry for chunk in chunks for entry in chunk]
        for expected in (entries[0], entries[29], entries[30], entries[-1]):
            self.assertIn(expected, seen)
        for left, right in zip(chunks, chunks[1:]):
            self.assertTrue(set(left) & set(right))
        self.assertEqual(set(seen), set(entries))

    def test_usage_limit_stops_and_reports_reset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            videos = root / "videos"
            d = videos / "2025-01-01-test"
            d.mkdir(parents=True)
            (d / "metadata.json").write_text('{"video_id":"v"}', encoding="utf-8")
            make(d)
            def limited(_prompt):
                import review_batch
                response = json.dumps({"is_error": True,
                                       "result": "You've hit your session limit · resets 5pm"})
                review_batch.classify_failure(1, response, "")
            result = review_summaries.run_batch(videos, limited, root, commit=False, log=lambda _: None)
            self.assertEqual(result["stopped_reset"], "resets 5pm")
            self.assertFalse((d / "review.md").exists())
            import review_batch
            with self.assertRaises(review_batch.UsageLimitReached) as exc:
                review_batch.classify_failure(
                    1, json.dumps({"is_error": True, "result": "session limit reached"}), "")
            self.assertEqual(exc.exception.reset_text, "not provided by Claude")

    def test_current_review_is_skipped_without_calling_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "videos" / "2025-01-01-test"
            d.mkdir(parents=True)
            make(d)
            review_summaries.review_video(d, fill(lambda p: FULL), sleep=lambda s: None)
            def unexpected(_):
                raise AssertionError("current review should not call model")
            result = review_summaries.run_batch(root / "videos", unexpected, root, commit=False, log=lambda _: None)
            self.assertEqual(result["skipped"], ["v"])

    def test_stale_review_is_rerun_and_rebound_to_current_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "videos" / "2025-01-01-test"
            d.mkdir(parents=True)
            make(d)
            review_summaries.review_video(d, fill(lambda p: FULL), sleep=lambda s: None)
            (d / "summary.md").write_text(SUMMARY + "- Câu thêm.\n", encoding="utf-8")
            calls = []
            result = review_summaries.run_batch(
                root / "videos", fill(lambda p: calls.append(p) or FULL), root, commit=False, log=lambda _: None)
            self.assertEqual(result["done"], ["v"])
            self.assertEqual(len(calls), 1)
            self.assertFalse(queue_state.publishable(d))  # new claim has no evidence -> fail
            self.assertEqual(json.loads((d / "review.md").read_text(encoding="utf-8"))["summary_sha256"],
                             review_summaries.summary_hash((d / "summary.md").read_bytes()))


if __name__ == "__main__":
    unittest.main()


class MultiLineEvidenceTest(unittest.TestCase):
    T = "[00:02:16] video ngắn\n[00:02:18] hoàn toàn không thể\n[00:02:20] đáp ứng được.\n"

    def test_quote_spanning_lines_with_covering_range(self):
        import review_summaries as r
        self.assertTrue(r.evidence_timestamp_matches("ngắn hoàn toàn không thể đáp ứng", "00:02:16-00:02:20", self.T))

    def test_range_must_overlap_a_quoted_caption(self):
        import review_summaries as r
        self.assertTrue(r.evidence_timestamp_matches("ngắn hoàn toàn", "00:02:18", self.T))
        self.assertTrue(r.evidence_timestamp_matches("ngắn hoàn toàn", "00:02:16", self.T))
        self.assertFalse(r.evidence_timestamp_matches("hoàn toàn", "00:02:20", self.T))
        self.assertFalse(r.evidence_timestamp_matches("hoàn toàn", "00:02:16", self.T))

    def test_non_verbatim_rejected(self):
        import review_summaries as r
        self.assertFalse(r.evidence_timestamp_matches("ngắn rất không thể", "00:02:16-00:02:20", self.T))


class TurnMarkerEvidenceTest(unittest.TestCase):
    def test_turn_marker_ignored_but_words_must_match(self):
        import review_summaries as r
        t = "[00:01:00] >> Thì đây cũng là một cái gốc tự do rất\n[00:01:03] nguy hiểm.\n"
        self.assertTrue(r.evidence_timestamp_matches("Thì đây cũng là một cái gốc tự do rất nguy hiểm.", "00:01:00-00:01:03", t))
        self.assertFalse(r.evidence_timestamp_matches("Thì đây là gốc tự do rất nguy hiểm.", "00:01:00-00:01:03", t))


class InvalidResponseRetryTest(unittest.TestCase):
    def test_invalid_then_valid_response_is_retried_never_accepted_blindly(self):
        with tempfile.TemporaryDirectory() as d:
            v = make(d, "## [00:00:01] P\n- xin chào.\n", "[00:00:01] xin chào các bạn\n")
            replies = iter([resp([entry("c001", "bịa đặt")]), resp([entry("c001", "xin chào")])])
            res = r.review_video(v, lambda prompt: next(replies), sleep=lambda s: None)
            self.assertEqual(res["verdict"], "pass")
            (v / "review.md").unlink()
            # never-valid quote: positive report is dropped on the last attempt -> no evidence -> fail
            calls = []
            res = r.review_video(v, lambda prompt: calls.append(1) or resp([entry("c001", "bịa đặt")]), sleep=lambda s: None)
            self.assertEqual(len(calls), r.INVALID_RESPONSE_ATTEMPTS)
            self.assertEqual(res["verdict"], "fail")
            self.assertEqual(res["claims"][0]["evidence"], [])
            self.assertFalse(queue_state.publishable(v))
            (v / "review.md").unlink()
            # a fabricated-quote NEGATIVE report is kept (flagged unverified), never discarded
            neg = resp([entry("c001", "bịa đặt", supported=False, contradicts=True, finding="sai")])
            res = r.review_video(v, lambda prompt: neg, sleep=lambda s: None)
            self.assertEqual(res["claims"][0]["status"], "fail")
            self.assertTrue(res["claims"][0]["issues"][0]["unverified_quote"])

    def test_all_errors_reported_together_in_retry_feedback(self):
        with self.assertRaises(r.ReviewError) as ctx:
            r.parse_model_review(resp([entry("c001", "bịa 1"), entry("c002", "bịa 2")]), TRANSCRIPT, {"c001", "c002"})
        self.assertIn("c001", str(ctx.exception))
        self.assertIn("c002", str(ctx.exception))


class ChunkProgressCacheTest(unittest.TestCase):
    def test_rerun_redoes_only_failed_chunk(self):
        with tempfile.TemporaryDirectory() as d:
            v = make(d, "## [00:00:01] P\n- một hai ba.\n- bốn năm sáu.\n- bảy tám chín.\n",
                     "[00:00:01] một hai ba\n[00:00:02] bốn năm sáu\n[00:00:03] bảy tám chín\n")
            quotes = {"1/3": ("c001", "một hai ba"), "2/3": ("c002", "bốn năm sáu"), "3/3": ("c003", "bảy tám chín")}
            def answer(prompt, bad_second):
                key = [k for k in quotes if f"PART {k}" in prompt][0]
                cid, q = quotes[key]
                return resp([entry(cid, "bịa đặt" if bad_second and key == "2/3" else q)])
            calls = []
            def flaky(prompt):
                calls.append(prompt)
                if "PART 2/3" in prompt:
                    raise RuntimeError("model crashed")
                return answer(prompt, False)
            with self.assertRaises(RuntimeError):
                r.review_video(v, fill(flaky), chunk_chars=11, overlap_chars=0, sleep=lambda s: None)
            self.assertTrue((v / r.PROGRESS_NAME).exists())
            calls.clear()
            def fixed(prompt):
                calls.append(prompt)
                return answer(prompt, False)
            res = r.review_video(v, fill(fixed), chunk_chars=11, overlap_chars=0, sleep=lambda s: None)
            self.assertEqual(res["verdict"], "pass")
            self.assertFalse((v / r.PROGRESS_NAME).exists())
            self.assertEqual(len(calls), 2)  # chunk 1 restored; 2 and 3 redone


class ReviewedDefectRegressionTests(unittest.TestCase):
    def test_chronological_section_end_ignores_reversed_text_order(self):
        summary = "## [00:04:04] Later\n- Later fact.\n## [00:04:03] Earlier\n- Earlier fact.\n"
        claims = fidelity.extract_claims(summary)
        self.assertEqual(claims[0]["section_end"], None)
        self.assertEqual(claims[1]["section_end"], 4 * 60 + 4)

    def test_repeated_quote_resolves_at_occurrence_overlapping_timestamp(self):
        transcript = "[00:00:01] lặp lại câu này\n[00:10:01] lặp lại câu này\n"
        self.assertTrue(fidelity.evidence_timestamp_matches("lặp lại câu này", "00:10:01", transcript))
        self.assertFalse(fidelity.evidence_timestamp_matches("lặp lại câu này", "00:05:00", transcript))

    def test_navigation_note_excluded_but_medical_assertion_kept(self):
        claims = fidelity.extract_claims("## [00:00:01] P\n- Đã gộp vào mục dinh dưỡng.\n- Vitamin có thể hỗ trợ sức khỏe.\n")
        self.assertEqual([c["claim"] for c in claims], ["Vitamin có thể hỗ trợ sức khỏe."])

    def test_strict_pass_rejects_authentic_evidence_outside_derived_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary = "## [00:00:01] A\n- Có thể hỗ trợ sức khỏe.\n- Không phải lúc nào cũng đúng.\n## [00:40:00] B\n"
            transcript = TRANSCRIPT + "[00:50:00] Có thể hỗ trợ sức khỏe.\n"
            d = make(tmp, summary, transcript)
            good = review_summaries.review_video(d, fill(lambda p: FULL), sleep=lambda s: None)
            self.assertEqual(good["verdict"], "pass")
            changed = json.loads((d / "review.md").read_text(encoding="utf-8"))
            changed["claims"][0]["evidence"] = [{"timestamp": "00:50:00", "quote": "Có thể hỗ trợ sức khỏe."}]
            (d / "review.md").write_text(json.dumps(changed, ensure_ascii=False), encoding="utf-8")
            self.assertFalse(queue_state.publishable(d))

    def test_completed_fail_or_incomplete_coverage_is_skipped_but_malformed_is_queued(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = make(tmp)
            base = json.loads(json.dumps({"claims": [entry("c001", "Có thể hỗ trợ sức khỏe."),
                                                       entry("c002", "Không phải lúc nào cũng đúng.")],
                                          "concerns": [], "omitted_topics": []}))
            result = review_summaries.review_video(d, fill(lambda p: resp(base["claims"])), sleep=lambda s: None)
            stored = json.loads((d / "review.md").read_text(encoding="utf-8"))
            stored["coverage_complete"] = False
            stored["omissions"] = [{"topic": "missing"}]
            stored["verdict"] = "fail"
            (d / "review.md").write_text(json.dumps(stored, ensure_ascii=False), encoding="utf-8")
            self.assertIsNotNone(queue_state.completed_review(d))
            self.assertIsNone(queue_state.current_review(d))
            calls = []
            review_summaries.review_video(d, lambda p: calls.append(p), sleep=lambda s: None)
            self.assertFalse(calls)  # completed failed/incomplete-coverage review resumes without model
            stored["claims"].pop()
            (d / "review.md").write_text(json.dumps(stored, ensure_ascii=False), encoding="utf-8")
            self.assertIsNone(queue_state.completed_review(d))
            review_summaries.review_video(d, lambda p: calls.append(p) or resp([]), sleep=lambda s: None)
            self.assertTrue(calls)

    def test_limit_one_skips_newer_current_review_then_reviews_older_video(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); videos = root / "videos"
            newer = videos / "2025-02-02-new"; newer.mkdir(parents=True)
            older = videos / "2025-02-01-old"; older.mkdir(parents=True)
            make(newer, vid="new"); make(older, vid="old")
            review_summaries.review_video(newer, fill(lambda p: FULL), sleep=lambda s: None)
            calls = []
            response = fill(lambda p: calls.append(p) or FULL)
            result = review_summaries.run_batch(videos, response, root, limit=1, commit=False, log=lambda _: None)
            self.assertEqual(result["skipped"], ["new"])
            self.assertEqual(result["done"], ["old"])
            self.assertTrue(calls)
