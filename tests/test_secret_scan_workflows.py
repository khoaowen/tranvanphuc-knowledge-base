"""Static checks of the workflow files (no YAML dependency, no network)."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SHA_USE = re.compile(r"^\s*(?:-\s*)?uses:\s*(\S+?)@(\S+)", re.M)


def text(name):
    """Workflow source without comment lines (comments may mention what is forbidden)."""
    lines = (WORKFLOWS / name).read_text(encoding="utf-8").splitlines()
    return "\n".join(l for l in lines if not l.lstrip().startswith("#")) + "\n"


def step(content, name):
    return content.split(f"- name: {name}", 1)[1].split("\n      - name:", 1)[0]


class HostedScanWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.text = text("secret-scan.yml")

    def test_triggers_are_pr_push_and_manual_only(self):
        on = self.text.split("\non:", 1)[1].split("\npermissions:", 1)[0]
        for trigger in ("pull_request:", "push:", "workflow_dispatch"):
            self.assertIn(trigger, on)
        for forbidden in ("pull_request_target", "workflow_run", "schedule"):
            self.assertNotIn(forbidden, self.text)

    def test_read_only_permissions_hosted_runner_and_no_secrets(self):
        self.assertRegex(self.text, r"permissions:\s*\n\s+contents:\s*read\n")
        self.assertNotRegex(self.text, r"contents:\s*write")
        self.assertNotIn("${{ secrets.", self.text)
        self.assertNotIn("self-hosted", self.text)
        self.assertIn("runs-on: ubuntu-latest", self.text)
        self.assertNotRegex(self.text, r"\$\{\{\s*github\.event\.(pull_request|head)")  # no injection

    def test_full_history_checkout_without_persisted_credentials(self):
        self.assertIn("fetch-depth: 0", self.text)
        self.assertIn("persist-credentials: false", self.text)

    def test_uses_the_shared_gate_for_bootstrap_and_repository(self):
        self.assertIn("python scripts/scan_secrets.py bootstrap", self.text)
        self.assertIn("python scripts/scan_secrets.py repository", self.text)
        self.assertNotIn("continue-on-error", self.text)
        self.assertNotIn("|| true", self.text)


class PinnedActionsTest(unittest.TestCase):
    def test_every_action_in_touched_workflows_is_pinned_to_a_full_sha(self):
        for name in ("secret-scan.yml", "weekly-sync.yml", "summarize-seed.yml"):
            uses = SHA_USE.findall(text(name))
            self.assertTrue(uses, name)
            for action, ref in uses:
                self.assertRegex(ref, r"^[0-9a-f]{40}$", f"{name}: {action}@{ref}")


class UploadGateTest(unittest.TestCase):
    def setUp(self):
        self.text = text("summarize-seed.yml")

    def test_upload_requires_a_successful_scan_of_the_exact_files(self):
        scan = step(self.text, "Scan outputs for secrets")
        self.assertIn("id: scan", scan)
        self.assertIn("if: always()", scan)  # runs even when summarize failed
        self.assertIn("scan_secrets.py artifacts", scan)
        self.assertNotIn("--allow-missing", scan)
        self.assertIn("$SEED_DIR/summary.md", scan)
        self.assertIn("measurement.log", scan)
        self.assertNotIn("continue-on-error", self.text)
        self.assertNotIn("${{ secrets.", scan)
        upload = step(self.text, "Upload summary and measurement log")
        self.assertIn("steps.scan.outcome == 'success'", upload)
        self.assertIn("summary.md", upload)
        self.assertIn("measurement.log", upload)

    def test_scan_precedes_upload_and_follows_summarize(self):
        order = [self.text.index(n) for n in ("Summarize seed video", "Scan outputs for secrets",
                                               "Upload summary and measurement log")]
        self.assertEqual(order, sorted(order))

    def test_permissions_are_explicit_and_read_only(self):
        self.assertRegex(self.text, r"\npermissions:\n  contents: read\n\n(?=\S)")
        self.assertEqual(self.text.count("permissions:"), 1)  # top-level only, no job override
        self.assertNotRegex(self.text, r"(?m)^\s*[\w-]+:\s*write\s*$")

    def test_only_the_summarize_step_receives_the_gemini_key(self):
        self.assertEqual(self.text.count("${{ secrets."), 1)
        self.assertEqual(self.text.count("secrets.GEMINI_API_KEY"), 1)
        self.assertIn("secrets.GEMINI_API_KEY", step(self.text, "Summarize seed video"))


class WeeklySyncWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.text = text("weekly-sync.yml")

    def test_scanner_verified_before_prepare_and_finalize_still_gates_publication(self):
        self.assertLess(self.text.index("Verify pinned secret scanner"), self.text.index("Detect, select, queue"))
        self.assertIn("python scripts/scan_secrets.py bootstrap", step(self.text, "Verify pinned secret scanner"))
        finalize = step(self.text, "Validate, test, commit and push")
        self.assertIn("weekly_sync.py finalize", finalize)  # the scan gate lives inside finalize
        self.assertNotIn("continue-on-error", self.text)

    def test_key_scope_and_triggers_are_unchanged(self):
        self.assertEqual(self.text.count("${{ secrets."), 1)
        self.assertEqual(self.text.count("secrets.GEMINI_API_KEY"), 1)
        self.assertNotIn("pull_request", self.text)
        self.assertIn("workflow_dispatch", self.text)


if __name__ == "__main__":
    unittest.main()
