# Tran Van Phuc Knowledge Base

A knowledge base distilled from the videos of **Bác sĩ Trần Văn Phúc Official** ([@BacsiTranVanPhucOfficial](https://www.youtube.com/@BacsiTranVanPhucOfficial), the official channel of Dr. Trần Văn Phúc, Saint Paul Hospital, Hanoi).

Modeled after [mlabonne/llm-course](https://github.com/mlabonne/llm-course): a versioned GitHub repo as the source of truth, feeding a ChatGPT Custom GPT people can chat with to learn from the doctor's health content.

> **Health disclaimer.** This content is a transcription and summary of Dr. Trần Văn Phúc's public videos. It is provided for informational and educational purposes only, does not constitute personalized medical advice, and is not a substitute for consultation, diagnosis, or treatment by a healthcare professional. If you have a health concern, consult a doctor.

## Status

Project in specification phase (BMad). See `_bmad-output/initiative-tran-van-phuc-knowledge-base/` for the full contract (capabilities, constraints, pipeline architecture).

Next step: breaking the work into tickets (`bmad-ticket`), then implementation (`bmad-build`).

Newly fetched videos keep the raw YouTube caption file their `transcript.md` is rendered from, with provenance, under `raw/`. See [docs/raw-captions.md](docs/raw-captions.md).

## Language note

Source transcripts stay in Vietnamese (the doctor's original language). Repo documentation, code, and commit messages are in English. The Custom GPT translates on demand when answering in another language.
