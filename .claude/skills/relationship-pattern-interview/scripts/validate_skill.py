#!/usr/bin/env python3
"""Static consistency checks for the Relationship Pattern Interview skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


texts: dict[str, str] = {}


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        failures.append(f"missing linked file: {rel}")
        return ""
    texts[rel] = path.read_text(encoding="utf-8")
    return texts[rel]


failures: list[str] = []
skill = read("SKILL.md")
questions = read("templates/core-question-bank.md")
safety = read("references/safety-guardrails.md")
final = read("templates/final-synthesis.md")
read("templates/relationship-matrix.md")
read("templates/session-resume.md")
read("templates/30-day-follow-up.md")
read("references/research-foundation.md")
read("references/adherence-test-rubric.md")

# Portability: the skill must run on any assistant (Claude, ChatGPT, etc.).
# No references to a specific host runtime or its scheduler/loader syntax.
for rel, text in texts.items():
    for line_no, line in enumerate(text.splitlines(), 1):
        if re.search(r"(?i)hermes", line):
            failures.append(f"runtime-specific reference in {rel} at line {line_no}: {line.strip()}")

description_match = re.search(r"^description:\s*(.+)$", skill, re.MULTILINE)
if not description_match:
    failures.append("missing description in SKILL.md frontmatter")
else:
    description = description_match.group(1)
    if len(description) > 1024:
        failures.append(f"description exceeds 1024 chars: {len(description)}")
    if not description.startswith("Use when"):
        failures.append("description must start with 'Use when' (triggers only)")
    if re.search(r"(?i)\bruns a\b|one-question-at-a-time interview with", description):
        failures.append("description summarizes the workflow; keep it to triggering conditions only")

version_match = re.search(r"^version:\s*(\S+)", skill, re.MULTILINE)
version = version_match.group(1) if version_match else None
if not version:
    failures.append("missing version in SKILL.md frontmatter")

qnums = [int(x) for x in re.findall(r"^### Q(\d+)\b", questions, re.MULTILINE)]
if qnums != list(range(1, 25)):
    failures.append(f"question headings are not exactly Q1-Q24: {qnums}")

qblocks = re.split(r"(?=^### Q\d+\b)", questions, flags=re.MULTILINE)[1:]
for block in qblocks:
    heading = re.search(r"^### Q(\d+)\b", block, re.MULTILINE)
    if heading and not re.search(r"^> .+", block, re.MULTILINE):
        failures.append(f"Q{heading.group(1)} has no explicit quoted prompt")

opening_match = re.search(
    r"### Default participant-facing opening.*?\n\n> (.*?)\n\nProgressively",
    skill,
    re.DOTALL,
)
if not opening_match:
    failures.append("default participant-facing opening not found")
    opening_words = None
else:
    opening = re.sub(r"\n> ?", " ", opening_match.group(1))
    opening_words = len(opening.split())
    if opening_words > 130:
        failures.append(f"opening ceremony exceeds 130 words: {opening_words}")

for rel, text in (("question bank", questions), ("safety reference", safety)):
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.startswith("> ") and line.count("?") > 1:
            failures.append(f"compound quoted question in {rel} at line {line_no}: {line}")

for forbidden in (
    "8-12 substantive questions",
    "### Phase A",
    "## 14) Final output template",
    "## 15) Quality checklist",
):
    if forbidden in safety:
        failures.append(f"safety reference contains competing protocol marker: {forbidden}")

required_skill_markers = (
    "### Execution state and drift control",
    "### Multi-session continuity",
    "conditional safety override only",
    "one atomic question at a time",
    "### Required follow-up mechanism",
    "A final output without a review date is incomplete.",
)
for marker in required_skill_markers:
    if marker not in skill:
        failures.append(f"missing SKILL.md mechanism: {marker}")

required_final_sections = (
    "## 7. Signal-weighting profile",
    "## 8. Continuation gates",
    "## 12. 30-day behavioral review",
    "## 13. Optional pilot usability measures",
)
for marker in required_final_sections:
    if marker not in final:
        failures.append(f"missing final synthesis section: {marker}")

final_numbers = [int(x) for x in re.findall(r"^## (\d+)\.", final, re.MULTILINE)]
if final_numbers != list(range(1, 14)):
    failures.append(f"final synthesis sections are not exactly 1-13: {final_numbers}")

result = {
    "version": version,
    "opening_words": opening_words,
    "question_count": len(qnums),
    "failures": failures,
    "status": "PASS" if not failures else "FAIL",
}
print(json.dumps(result, indent=2))
sys.exit(0 if not failures else 1)
