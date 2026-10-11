#!/usr/bin/env python3
"""Summarize a video transcript into videos/<slug>/summary.md using Gemini.

Usage: summarize.py <video-dir>

Reads <video-dir>/transcript.md ([HH:MM:SS] text lines) and metadata.json,
splits the transcript into timestamp-aligned chunks, map-reduces them through
a Gemini model, and atomically writes <video-dir>/summary.md following
summary-contract.md (header, disclaimer banner, timestamped topic sections
with ?t= deep links, question-shaped lines, VI/EN/FR glossary).

Configuration comes from the environment only:
  GEMINI_API_KEY  API key (free tier). Never printed, logged or written.
  GEMINI_MODEL    Gemini model name.

The model call is an injectable `client(prompt) -> text` callable so tests
and later entries can reuse the pipeline and the SCHEMA/prompt constants.
Stdlib only. Progress and measurement lines go to stderr.
"""

import argparse
import json
import os
import random
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_CHUNK_CHARS = 60000
DEFAULT_PACE_SECONDS = 6.0
DEFAULT_MAX_RETRIES = 5
BACKOFF_BASE_SECONDS = 10.0
BACKOFF_MAX_JITTER_SECONDS = 5.0
REQUEST_TIMEOUT_SECONDS = 300

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

# Verbatim from spec-tran-van-phuc-kb/disclaimer.md (English canonical text).
DISCLAIMER_BANNER = (
    "> **Health disclaimer.** This content is a transcription and summary of "
    "Dr. Trần Văn Phúc's public videos (channel \"Bác sĩ Trần Văn Phúc "
    "Official\"). It is provided for informational and educational purposes "
    "only, does not constitute personalized medical advice, and is not a "
    "substitute for consultation, diagnosis, or treatment by a healthcare "
    "professional. If you have a health concern, consult a doctor."
)

# Schema and fidelity rules mirror summary-contract.md. Reused by entries 9/10.
SECTION_SCHEMA = """\
Each topic section must follow this exact shape:

## [HH:MM:SS] Section title

**Q: <a question a viewer would ask, phrased as users would query>**
<answer, stated with the specifics from the transcript>

(Repeat Q/A pairs as needed; every section needs at least one.)

Rules for sections:
- One section per topic discussed. HH:MM:SS is the start timestamp of that
  topic, taken from the transcript's own [HH:MM:SS] markers.
- Do not write URLs or links; links are added afterwards.
- Each section must make sense on its own, without the other sections.
- Write in Vietnamese, the language of the transcript.
- Be specific: name the conditions, substances, doses, numbers and durations
  exactly as stated. No generic gloss such as "discusses nutrition"."""

FIDELITY_RULES = """\
Fidelity rules:
- Every claim must trace to the transcript at the cited timestamp.
- Keep the doctor's hedges (may, in some cases, depends on...). Never harden
  them into absolutes.
- Add no medical content, correction or advice that is absent from the
  transcript. If unsure, leave it out."""

MAP_INSTRUCTIONS = f"""\
You are summarizing one part of a Vietnamese health-education video transcript
for a retrieval index. Lines look like "[HH:MM:SS] text".

Produce only topic sections for this part of the transcript, nothing else (no
preamble, no code fences, no glossary).

{SECTION_SCHEMA}

{FIDELITY_RULES}"""

REDUCE_INSTRUCTIONS = f"""\
Below are topic sections drafted from consecutive parts of one video's
transcript. Merge them into the final summary body.

- Merge sections that cover the same topic across a part boundary; keep the
  earliest start timestamp. Drop filler (greetings, music, sign-offs).
- Keep all specific claims (conditions, substances, doses, numbers,
  durations) and hedges. Do not add anything not present in the drafts.

Output exactly, in this order, with no code fences:
1. One line: TAGS: tag1, tag2, tag3   ({{TAG_RULE}})
2. The merged topic sections.
3. A final section titled exactly "## Glossary" with a Markdown table with
   columns Vietnamese | English | French, listing the key terms of the video,
   so that queries in any of the three languages match.

{SECTION_SCHEMA}

{FIDELITY_RULES}"""

TAG_RULE_FREE_FORM = "3 to 8 short lowercase topic tags, free-form"
TAG_RULE_VOCABULARY = (
    "3 to 8 tags, each chosen only from the vocabulary listed below"
)

TIMESTAMP_LINE = re.compile(r"^\[(\d+):(\d{2}):(\d{2})\]\s?(.*)$")
SECTION_HEADING = re.compile(r"^## \[(\d+):(\d{2}):(\d{2})\]\s*(.*?)\s*$")
URL = re.compile(r"https?://\S+")
CODE_FENCE = re.compile(r"^```[a-zA-Z]*\s*$")


class SummarizeError(Exception):
    """Unrecoverable summarization failure; no summary.md is written."""


class RateLimitError(Exception):
    """Per-minute rate limit (HTTP 429). retry_after is seconds or None."""

    def __init__(self, retry_after=None):
        super().__init__("rate limited (429)")
        self.retry_after = retry_after


class TransientError(Exception):
    """Retryable server/network failure (HTTP 5xx, timeout, connection error)."""


class DailyQuotaExhausted(Exception):
    """Daily free-tier quota is used up; retrying today is pointless."""


# --- transcript parsing and chunking ---------------------------------------


def format_timestamp(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def parse_transcript(text):
    """Parse transcript text into a list of (start_seconds, line) tuples.

    Each line keeps its original "[HH:MM:SS] text" form. Lines without a
    leading timestamp are appended to the previous entry; blank lines are
    skipped.
    """
    entries = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        match = TIMESTAMP_LINE.match(line)
        if match:
            hours, minutes, seconds = (int(g) for g in match.group(1, 2, 3))
            entries.append((hours * 3600 + minutes * 60 + seconds, line))
        elif entries:
            start, previous = entries[-1]
            entries[-1] = (start, f"{previous} {line}")
    return entries


def chunk_transcript(entries, max_chars):
    """Group entries into chunks of at most max_chars, split on line boundaries.

    A single line longer than max_chars becomes its own chunk. Returns a list
    of chunks; each chunk is a list of (start_seconds, line) tuples.
    """
    chunks = []
    current = []
    size = 0
    for entry in entries:
        line_size = len(entry[1]) + 1
        if current and size + line_size > max_chars:
            chunks.append(current)
            current = []
            size = 0
        current.append(entry)
        size += line_size
    if current:
        chunks.append(current)
    return chunks


def render_chunk(chunk):
    return "\n".join(line for _, line in chunk)


# --- prompts ---------------------------------------------------------------


def build_map_prompt(chunk):
    return f"{MAP_INSTRUCTIONS}\n\n<transcript_part>\n{render_chunk(chunk)}\n</transcript_part>"


def build_reduce_prompt(partials, vocabulary_text):
    if vocabulary_text:
        instructions = REDUCE_INSTRUCTIONS.replace("{TAG_RULE}", TAG_RULE_VOCABULARY)
        vocabulary = f"\n\n<vocabulary>\n{vocabulary_text}\n</vocabulary>"
    else:
        instructions = REDUCE_INSTRUCTIONS.replace("{TAG_RULE}", TAG_RULE_FREE_FORM)
        vocabulary = ""
    drafts = "\n\n".join(
        f"<draft part=\"{i}\">\n{partial}\n</draft>"
        for i, partial in enumerate(partials, start=1)
    )
    return f"{instructions}{vocabulary}\n\n{drafts}"


def load_vocabulary(path):
    """Return the vocabulary file's text, or None if the file does not exist."""
    path = Path(path)
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8").strip()
    return text or None


# --- output assembly -------------------------------------------------------


def strip_code_fences(text):
    lines = [line for line in text.strip().splitlines() if not CODE_FENCE.match(line)]
    return "\n".join(lines).strip()


def add_deep_links(body, video_id):
    """Append the ?t= deep link to every `## [HH:MM:SS] title` heading."""
    out = []
    for line in body.splitlines():
        match = SECTION_HEADING.match(line)
        if match:
            hours, minutes, seconds = (int(g) for g in match.group(1, 2, 3))
            start = hours * 3600 + minutes * 60 + seconds
            title = re.sub(r"[(\[]?\s*" + URL.pattern, "", match.group(4)).strip(" -—")
            title = re.sub(r"\(\s*\)|\[\s*\]", "", title).strip(" -—")
            link = f"https://www.youtube.com/watch?v={video_id}&t={start}s"
            line = f"## [{format_timestamp(start)}] {title} — {link}"
        out.append(line)
    return "\n".join(out)


def parse_reduce_output(text):
    """Split reduce output into (tags, body). Raises SummarizeError if malformed."""
    cleaned = strip_code_fences(text)
    lines = cleaned.splitlines()
    tags = None
    body_start = 0
    for index, line in enumerate(lines):
        if line.strip().upper().startswith("TAGS:"):
            tags = [t.strip() for t in line.split(":", 1)[1].split(",") if t.strip()]
            body_start = index + 1
            break
    if not tags:
        raise SummarizeError("reduce output has no TAGS line")
    body = "\n".join(lines[body_start:]).strip()
    if not any(SECTION_HEADING.match(line) for line in body.splitlines()):
        raise SummarizeError("reduce output has no timestamped topic section")
    if not re.search(r"^## Glossary\s*$", body, re.M):
        raise SummarizeError("reduce output has no Glossary section")
    if "**Q:" not in body:
        raise SummarizeError("reduce output has no Q: question lines")
    return tags, body


def build_summary(metadata, tags, body):
    header = "\n".join(
        [
            f"# {metadata['title']}",
            "",
            f"- **Video ID:** {metadata['video_id']}",
            f"- **Published:** {metadata['published_at']}",
            f"- **URL:** {metadata['url']}",
            f"- **Topics:** {', '.join(tags)}",
        ]
    )
    body = add_deep_links(body, metadata["video_id"])
    return f"{header}\n\n{DISCLAIMER_BANNER}\n\n{body}\n"


def write_atomic(path, content):
    """Write content to path via a temp file in the same dir and os.replace.

    On any failure the temp file is removed and an existing file at path is
    left untouched.
    """
    path = Path(path)
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


# --- calling the model -----------------------------------------------------


def call_with_retry(
    client,
    prompt,
    max_retries=DEFAULT_MAX_RETRIES,
    sleep=None,
    jitter=random.uniform,
    log=lambda message: None,
):
    """Call client(prompt), backing off with jitter on RateLimitError.

    Waits max(Retry-After, exponential backoff) plus jitter. Raises
    SummarizeError after max_retries retries; DailyQuotaExhausted propagates
    immediately. Returns (text, rate_limit_hits).
    """
    sleep = sleep or time.sleep
    hits = 0
    transient = 0
    while True:
        try:
            return client(prompt), hits
        except TransientError as exc:
            transient += 1
            if transient > max_retries:
                raise SummarizeError(
                    f"transient failure persisted after {max_retries} retries: "
                    f"{str(exc)[:200]}"
                ) from exc
            wait = BACKOFF_BASE_SECONDS * (2 ** (transient - 1)) + jitter(
                0, BACKOFF_MAX_JITTER_SECONDS
            )
            log(f"transient error #{transient}: waiting {wait:.1f}s before retry")
            sleep(wait)
        except RateLimitError as exc:
            hits += 1
            if hits > max_retries:
                raise SummarizeError(
                    f"still rate limited after {max_retries} retries"
                ) from exc
            backoff = BACKOFF_BASE_SECONDS * (2 ** (hits - 1))
            wait = max(exc.retry_after or 0, backoff) + jitter(0, BACKOFF_MAX_JITTER_SECONDS)
            log(
                f"429 #{hits}: retry_after={exc.retry_after} "
                f"waiting {wait:.1f}s before retry"
            )
            sleep(wait)


def summarize_video(
    video_dir,
    client,
    vocabulary_path=None,
    chunk_chars=DEFAULT_CHUNK_CHARS,
    pace_seconds=DEFAULT_PACE_SECONDS,
    max_retries=DEFAULT_MAX_RETRIES,
    sleep=None,
    jitter=random.uniform,
    log=lambda message: None,
):
    """Summarize video_dir/transcript.md into video_dir/summary.md.

    Returns the Path of summary.md. summary.md is written only after every
    model call has succeeded.
    """
    sleep = sleep or time.sleep
    video_dir = Path(video_dir)
    try:
        metadata = json.loads((video_dir / "metadata.json").read_text(encoding="utf-8"))
        transcript = (video_dir / "transcript.md").read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        raise SummarizeError(f"cannot read inputs in {video_dir}: {exc}") from exc

    entries = parse_transcript(transcript)
    if not entries:
        raise SummarizeError(f"no timestamped transcript lines in {video_dir}")
    chunks = chunk_transcript(entries, chunk_chars)
    vocabulary_text = load_vocabulary(vocabulary_path) if vocabulary_path else None
    total_calls = len(chunks) + 1
    log(
        f"transcript: {len(entries)} lines, {len(transcript)} chars -> "
        f"{len(chunks)} chunk(s) of <= {chunk_chars} chars; "
        f"vocabulary={'yes' if vocabulary_text else 'no'}; pace={pace_seconds}s"
    )

    call_number = 0

    def run(label, prompt):
        nonlocal call_number
        call_number += 1
        if call_number > 1 and pace_seconds > 0:
            sleep(pace_seconds)
        started = time.monotonic()
        text, hits = call_with_retry(
            client, prompt, max_retries=max_retries, sleep=sleep, jitter=jitter, log=log
        )
        usage = getattr(client, "last_usage", None)
        log(
            f"call {call_number}/{total_calls} {label}: prompt_chars={len(prompt)} "
            f"response_chars={len(text)} rate_limit_hits={hits} "
            f"elapsed={time.monotonic() - started:.1f}s usage={usage}"
        )
        return text

    partials = []
    for index, chunk in enumerate(chunks, start=1):
        partials.append(
            strip_code_fences(run(f"map {index}/{len(chunks)}", build_map_prompt(chunk)))
        )
    reduced = run("reduce", build_reduce_prompt(partials, vocabulary_text))
    tags, body = parse_reduce_output(reduced)

    summary = build_summary(metadata, tags, body)
    summary_path = video_dir / "summary.md"
    write_atomic(summary_path, summary)
    log(f"summary: {len(summary)} chars ({len(summary) / len(transcript):.1%} of transcript)")
    return summary_path


# --- Gemini client ---------------------------------------------------------


def scrub(text, secret):
    """Remove the secret value from text before it is printed."""
    return text.replace(secret, "[redacted]") if secret else text


def parse_retry_after(header_value, body):
    """Seconds to wait from a Retry-After header or RetryInfo.retryDelay, else None."""
    if header_value:
        try:
            return float(header_value)
        except ValueError:
            pass
    match = re.search(r'"retryDelay"\s*:\s*"([\d.]+)s"', body)
    return float(match.group(1)) if match else None


def is_daily_quota(body):
    """True if a 429 body reports a per-day quota violation."""
    return bool(re.search(r'"quotaId"\s*:\s*"[^"]*PerDay', body))


class GeminiClient:
    """Callable client(prompt) -> text for the Gemini generateContent REST API."""

    def __init__(self, api_key, model, timeout=REQUEST_TIMEOUT_SECONDS):
        self._api_key = api_key
        self._url = GEMINI_URL.format(model=model)
        self._timeout = timeout
        self.last_usage = None

    def __call__(self, prompt):
        payload = json.dumps(
            {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.2},
            }
        ).encode("utf-8")
        request = urllib.request.Request(
            self._url,
            data=payload,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": self._api_key,
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                data = json.load(response)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429:
                if is_daily_quota(body):
                    raise DailyQuotaExhausted() from None
                raise RateLimitError(
                    parse_retry_after(exc.headers.get("Retry-After"), body)
                ) from None
            message = scrub(f"Gemini HTTP {exc.code}: {body[:500]}", self._api_key)
            if exc.code >= 500:
                raise TransientError(message) from None
            raise SummarizeError(message) from None
        except (urllib.error.URLError, TimeoutError) as exc:
            raise TransientError(
                scrub(f"Gemini request failed: {exc}", self._api_key)
            ) from None
        except json.JSONDecodeError as exc:
            raise SummarizeError(
                scrub(f"Gemini request failed: {exc}", self._api_key)
            ) from None

        self.last_usage = data.get("usageMetadata")
        try:
            parts = data["candidates"][0]["content"]["parts"]
            return "".join(part.get("text", "") for part in parts)
        except (KeyError, IndexError, TypeError):
            reason = (data.get("promptFeedback") or {}).get("blockReason")
            raise SummarizeError(
                f"Gemini returned no candidate text (blockReason={reason})"
            ) from None


# --- CLI -------------------------------------------------------------------


def default_vocabulary_path():
    return Path(__file__).resolve().parent.parent / "topics" / "vocabulary.md"


def log_stderr(message):
    print(message, file=sys.stderr, flush=True)


def main(argv=None, client=None):
    parser = argparse.ArgumentParser(
        description="Summarize a video transcript into summary.md using Gemini."
    )
    parser.add_argument("video_dir", help="Path to videos/<date>-<slug>/")
    parser.add_argument(
        "--chunk-chars",
        type=int,
        default=DEFAULT_CHUNK_CHARS,
        help=f"Max characters per transcript chunk (default: {DEFAULT_CHUNK_CHARS})",
    )
    parser.add_argument(
        "--pace-seconds",
        type=float,
        default=DEFAULT_PACE_SECONDS,
        help=f"Delay between model calls (default: {DEFAULT_PACE_SECONDS})",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        help=f"Retries per call on HTTP 429 (default: {DEFAULT_MAX_RETRIES})",
    )
    parser.add_argument(
        "--vocabulary",
        default=str(default_vocabulary_path()),
        help="Path to topics/vocabulary.md (used only if the file exists)",
    )
    args = parser.parse_args(argv)

    if client is None:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        model = os.environ.get("GEMINI_MODEL", "")
        if not api_key or not model:
            print(
                "error: GEMINI_API_KEY and GEMINI_MODEL must be set in the environment",
                file=sys.stderr,
            )
            return 2
        client = GeminiClient(api_key, model)

    try:
        summary_path = summarize_video(
            args.video_dir,
            client,
            vocabulary_path=args.vocabulary,
            chunk_chars=args.chunk_chars,
            pace_seconds=args.pace_seconds,
            max_retries=args.max_retries,
            log=log_stderr,
        )
    except DailyQuotaExhausted:
        print(
            "error: Gemini free-tier daily quota exhausted; no summary written. "
            "The daily quota resets at midnight Pacific time; re-run after that.",
            file=sys.stderr,
        )
        return 1
    except SummarizeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
