# End-to-end test suite

`tests/test_end_to_end.py` runs the whole pipeline once for video `q7uDJG8YQ5c` with every
network and model seam stubbed: the channel listing, the yt-dlp fetch, the Gemini client and
the `claude -p` command. It needs no network and no secrets, and runs with the rest of the
suite: `python3 -m unittest discover -s tests`.

It checks the epic's Done-when items in one pass:

1. Detection tells the known video from the new one and fetches only the new one.
2. `transcript.md`, `metadata.json` and a valid, shorter, tagged, timestamped `summary.md` exist.
3. The README and `topics/` reach the video in two clicks or fewer, with the disclaimer shown.
4. `knowledge-gpt/` stays within 20 files and the per-file size cap.

It also checks that the CI video stays unpublished until the local fidelity review passes,
that an invalid summary is rejected and the video stays queued, that backlog videos stay
`pending` in CI and are summarized locally through a stubbed `claude -p`, and that video
state is derived from files.

## Not automated: the GPT Builder check

The Custom GPT answering a question about `q7uDJG8YQ5c` in a non-Vietnamese language, grounded,
with the disclaimer shown, needs a human in the GPT Builder. Follow
[custom-gpt-setup.md](custom-gpt-setup.md) after each run; the test suite never calls it.
