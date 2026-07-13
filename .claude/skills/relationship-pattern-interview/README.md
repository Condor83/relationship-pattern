# Relationship Pattern Interview

A structured, finite interview that a general-purpose AI assistant (Claude, ChatGPT, or similar) can run to help a single adult understand their dating history, test explanations for recurring patterns, and turn the strongest insights into 1–3 concrete changes to try over the next 30–90 days.

It is evidence-informed self-reflection and decision support — not therapy, diagnosis, crisis care, or a validated assessment.

## Quick start

**Claude (claude.ai):** Create a Project and upload this folder's files, or paste `SKILL.md` and `templates/core-question-bank.md` into a chat. Then say something like "Run the relationship pattern interview with me."

**Claude Code / Agent SDK:** Place this folder in `.claude/skills/`. The skill triggers automatically when the conversation calls for it.

**ChatGPT:** Upload the files to a Project (or a custom GPT's knowledge), or paste `SKILL.md` and `templates/core-question-bank.md` into the chat and ask it to run the interview.

The minimum the assistant needs is `SKILL.md` plus `templates/core-question-bank.md`. Give it the whole folder when you can — the other files handle safety responses, multi-session resumes, and the final report format.

## What's in the folder

| File | Purpose |
|---|---|
| `SKILL.md` | The protocol: contract, phases, checkpoints, stopping rules, safety gates |
| `templates/core-question-bank.md` | The exact 24-question backbone |
| `templates/relationship-matrix.md` | Timeline/evidence table for mapped relationships |
| `templates/session-resume.md` | Resume Capsule for pausing and continuing in a new chat |
| `templates/final-synthesis.md` | Format of the final relationship map and action plan |
| `templates/30-day-follow-up.md` | Optional 30-day behavioral review reminder |
| `references/safety-guardrails.md` | Safety override: distress, abuse/coercion, crisis routing |
| `references/research-foundation.md` | Research sources, limits, validation roadmap |
| `references/adherence-test-rubric.md` | Rubric for grading test transcripts (maintainers) |
| `scripts/validate_skill.py` | Static consistency checks (maintainers) |

## Privacy

The interview covers sensitive history. Use pseudonyms, skip anything you want, and remember AI chats are stored under your provider's policies — this is not legally privileged therapy. Nothing is saved beyond the conversation unless you explicitly ask for it.

If you are in immediate danger or crisis, contact local emergency services or a crisis line instead of running this interview.

## License

MIT.
