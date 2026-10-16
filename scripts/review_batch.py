#!/usr/bin/env python3
"""Summarize the backlog locally through `claude -p` (subscription login).

Usage: review_batch.py [--videos-dir videos] [--model sonnet|haiku]
                       [--claude-cmd claude] [--limit N] [--max-retries N]

Loops over videos with no summary.md, newest first. A pending video gets its
transcript fetched first. Each video is summarized by summarize.summarize_video
with a claude client and committed on its own (no push). Re-running resumes,
because finished videos have a summary.md. Local only: never use in CI.

Env REVIEW_BATCH_CLAUDE overrides the claude command (for stubbing).
"""

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import queue_state  # noqa: E402
import summarize  # noqa: E402
from summarize import (  # noqa: E402
    RateLimitError,
    SummarizeError,
    TransientError,
    log_stderr,
)

CALL_TIMEOUT_SECONDS = 1800
USAGE_LIMIT = re.compile(r"usage limit|session limit|hit your limit|limit reached|out of (extra )?usage", re.I)
SHORT_429 = re.compile(r"\b429\b|rate.?limit|overloaded|too many requests", re.I)
RESET_HINT = re.compile(r"(resets?[^\n.]*)", re.I)


class UsageLimitReached(Exception):
    """The subscription usage limit is hit; stop the whole run."""

    def __init__(self, reset_text):
        super().__init__(reset_text)
        self.reset_text = reset_text


def extract_text(stdout):
    """Return (is_error, text) from `claude -p --output-format json` stdout.

    Falls back to raw stdout when it is not JSON.
    """
    try:
        data = json.loads(stdout)
    except ValueError:
        return False, stdout
    if isinstance(data, dict):
        return bool(data.get("is_error")), str(data.get("result", ""))
    return False, stdout


def classify_failure(returncode, stdout, stderr):
    """Map a failed claude call to an exception. One place to tune patterns.

    A real usage limit mentions a limit AND a reset (or "usage limit");
    a short 429 mentions 429/rate limit/overloaded without a reset.
    Anything else is a per-video SummarizeError, never a silent success.
    """
    _, text = extract_text(stdout)
    blob = f"{text}\n{stderr}"
    reset = RESET_HINT.search(blob)
    if USAGE_LIMIT.search(blob):
        raise UsageLimitReached(reset.group(1).strip() if reset else "not provided by Claude")
    if SHORT_429.search(blob):
        raise RateLimitError(None)
    raise SummarizeError(f"claude failed (exit {returncode}): {blob.strip()[:300]}")


class ClaudeClient:
    """Callable client(prompt) -> text; prompt goes on stdin."""

    def __init__(self, command="claude", model="sonnet", timeout=CALL_TIMEOUT_SECONDS):
        self._argv = shlex.split(command) + ["-p", "--output-format", "json", "--model", model]
        self._timeout = timeout
        self.last_usage = None

    def __call__(self, prompt):
        try:
            proc = subprocess.run(
                self._argv, input=prompt, capture_output=True, text=True, timeout=self._timeout
            )
        except subprocess.TimeoutExpired:
            raise TransientError("claude call timed out") from None
        except FileNotFoundError:
            raise SummarizeError(f"claude command not found: {self._argv[0]}") from None
        is_error, text = extract_text(proc.stdout)
        if proc.returncode != 0 or is_error:
            classify_failure(proc.returncode, proc.stdout, proc.stderr)
        if not text.strip():
            raise SummarizeError("claude returned empty output")
        return text


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def commit_video(video_dir, video_id, repo_root):
    rel = os.path.relpath(video_dir, repo_root)
    added = git("add", "--", rel, cwd=repo_root)
    if added.returncode != 0:
        raise SummarizeError(f"git add failed: {added.stderr.strip()}")
    done = git("commit", "-m", f"content: summary for {video_id} (review-batch)", "--", rel,
               cwd=repo_root)
    if done.returncode != 0:
        raise SummarizeError(f"git commit failed: {(done.stderr or done.stdout).strip()}")


def fetch_missing_transcript(entry, videos_dir):
    script = Path(__file__).resolve().parent / "fetch_transcript.py"
    proc = subprocess.run(
        [sys.executable, str(script), "--videos-dir", str(videos_dir), entry["video_id"]],
        capture_output=True, text=True,
    )
    if proc.returncode != 0 or not (entry["dir"] / "transcript.md").is_file():
        # fetch may have written a new dir (slug) if metadata dir had other name
        raise SummarizeError(f"fetch failed for {entry['video_id']}: {proc.stderr.strip()[:200]}")


def run_batch(videos_dir, client, repo_root, limit=None, max_retries=5, pace_seconds=0.0,
              sleep=None, log=log_stderr, commit=True):
    """Process the queue. Returns dict: done, failed, stopped_reset (or None)."""
    result = {"done": [], "failed": [], "stopped_reset": None}
    queue = queue_state.todo(videos_dir)
    if not queue:
        log("nothing pending: every video has a summary")
        return result
    for entry in queue:
        if limit is not None and len(result["done"]) >= limit:
            break
        vid = entry["video_id"]
        try:
            if entry["state"] == queue_state.PENDING:
                log(f"{vid}: fetching transcript")
                fetch_missing_transcript(entry, videos_dir)
            log(f"{vid}: summarizing {entry['dir'].name}")
            summarize.summarize_video(
                entry["dir"], client,
                vocabulary_path=summarize.default_vocabulary_path(),
                pace_seconds=pace_seconds, max_retries=max_retries, sleep=sleep, log=log,
            )
            if commit:
                commit_video(entry["dir"], vid, repo_root)
            result["done"].append(vid)
        except UsageLimitReached as exc:
            result["stopped_reset"] = exc.reset_text
            log(f"usage limit reached; stopping. Reset: {exc.reset_text}")
            break
        except (SummarizeError, summarize.DailyQuotaExhausted) as exc:
            log(f"warning: skipping {vid}: {exc}")
            result["failed"].append(vid)
    return result


def main(argv=None, client=None):
    parser = argparse.ArgumentParser(description="Summarize backlog videos via claude -p.")
    parser.add_argument("--videos-dir", default="videos")
    parser.add_argument("--model", default="sonnet", choices=["sonnet", "haiku"])
    parser.add_argument("--claude-cmd", default=os.environ.get("REVIEW_BATCH_CLAUDE", "claude"))
    parser.add_argument("--limit", type=int, default=None, help="Max videos to summarize")
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--no-commit", action="store_true")
    args = parser.parse_args(argv)

    client = client or ClaudeClient(args.claude_cmd, args.model)
    repo_root = Path(__file__).resolve().parent.parent
    result = run_batch(args.videos_dir, client, repo_root, limit=args.limit,
                       max_retries=args.max_retries, commit=not args.no_commit)
    print(f"summarized {len(result['done'])}, failed {len(result['failed'])}")
    if result["stopped_reset"]:
        print(f"stopped at usage limit; resets: {result['stopped_reset']}")
        return 0
    if result["failed"] and not result["done"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
