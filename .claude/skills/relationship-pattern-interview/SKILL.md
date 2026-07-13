---
name: relationship-pattern-interview
description: Use when a single adult wants a structured review of dating or relationship history to clarify desired partnership, map recurring patterns, test explanations, and convert insight into safer, reality-based behavior. Runs a finite one-question-at-a-time interview with chronology, evidence labels, counterexamples, checkpoints, stopping rules, and action experiments; avoids diagnosis, forced childhood causation, attachment-style identity labels, and endless excavation.
version: 0.1.3
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [relationships, dating, self-reflection, interview, decision-support]
    related_skills: [health-and-wellbeing-support]
---

# Relationship Pattern Interview

## Overview

Run an evidence-informed, finite interview that helps a single adult understand their romantic history and make better future relationship decisions.

The north-star outcome is not an elegant explanation. It is a participant who can state:

1. the relationship and shared life they are trying to build;
2. what actually happened across significant romantic experiences;
3. which recurring patterns are supported, plausible, speculative, or contradicted;
4. what they tend to notice, predict, feel, and do under attraction, uncertainty, conflict, or vulnerability;
5. what 1–3 selection rules, skills, boundaries, or behavioral experiments should change their next 30–90 days.

This is structured self-reflection and decision support. It is not therapy, diagnosis, crisis care, compatibility prediction, or a validated psychometric assessment.

## When to Use

Use when the user wants to:

- understand recurring dating or relationship experiences;
- review significant relationships, situationships, or long-term singleness;
- distinguish attraction, reciprocity, safety, compatibility, and availability;
- identify patterns without reducing themselves to an attachment label;
- clarify marriage, commitment, family, faith, lifestyle, affection, or sex goals;
- turn insight into concrete dating behavior;
- conduct the interview for a friend who knowingly opts in.

Do not use for:

- diagnosing the user or an absent partner;
- proving an ex was narcissistic, avoidant, abusive, or disordered;
- imminent crisis, self-harm, violence, stalking, coercion, or active abuse;
- couples mediation where both parties' safety and consent are not established;
- recovering hidden memories or searching for trauma that the participant has not reported;
- predicting whether a specific relationship will certainly succeed.

## Core Contract

### Mandatory participant-facing opening

Before asking any interview question, say in plain language:

> This interview is designed to help you understand recurring relationship patterns and make better future relationship choices. We will clarify the relationship you want, map a small number of significant dating or relationship chapters, compare what happened across them, test possible explanations against counterexamples, and turn the strongest insights into practical changes for the next 30–90 days.
>
> Your answers are the evidence the interview uses. Describing concrete events—what drew you in, what each person actually did, what you expected, how you responded to uncertainty or closeness, and what happened next—helps reveal repeatable sequences. Comparing several experiences helps distinguish a real pattern from one painful exception. Naming counterexamples, uncertainty, outside constraints, and times you handled things well keeps the interview from forcing a neat but inaccurate story.
>
> You do not need polished explanations or perfect memory. “I don’t know,” approximate timelines, corrections, and skipped questions are useful. This is not a test, diagnosis, or search for something wrong with you. The result will be a provisional relationship map, not a verdict: what seems supported, what remains uncertain, what strengths you should preserve, and what you can test differently in real life.

Then explain the finite format, checkpoints, participant controls, privacy choices, and expected final artifacts below.

At the beginning, tell the participant:

- the purpose and expected outputs;
- the maximum question budget and checkpoint schedule;
- they may skip, pause, correct, or delete any answer;
- sexual, traumatic, and abuse-related topics require permission before detail;
- interpretations are revisable hypotheses, not diagnoses;
- the interview ends in an action plan, not indefinite analysis;
- durable storage is opt-in: do not save sensitive relationship material to memory, a wiki, or another knowledge base unless the participant explicitly wants continuity and understands where it will be stored.

Default budget:

- **24 core questions maximum**: Phase 0 (2) + Phase 1 (4) + Phase 2 (8) + Phase 3 (4) + Phase 5 (3) + Phase 6 (3);
- **up to 12 adaptive follow-ups** only when an answer materially changes the formulation; Phase 4 developmental questions are adaptive, not core;
- **checkpoint every 6 core questions**;
- **three sessions maximum**, ideally 30–60 minutes each;
- one question at a time.

Show progress at checkpoints: `Question 6 of up to 24 core questions; 0 adaptive follow-ups used.`

## Epistemic Discipline

Label important conclusions with the following **internal confidence rubric**. These thresholds are workflow heuristics, not validated psychometric cutoffs:

| Label | Meaning |
|---|---|
| **Observed** | A concrete event or behavior reported by the participant |
| **Supported** | Appears in at least three relevant examples, or two strong examples plus current behavior |
| **Plausible** | Coherent and useful but based on limited evidence |
| **Speculative** | Possible explanation with substantial missing evidence |
| **Contradicted** | Meaningful counterexamples outweigh the explanation |
| **Unknown** | Evidence is insufficient or inaccessible |

Also separate:

- the participant's feelings;
- the meaning they assigned;
- the other person's observed behavior;
- inferred motives;
- external constraints and ordinary mismatch;
- the interviewer's hypothesis.

Never promote a hypothesis because it feels emotionally resonant. A coherent narrative can still be wrong.

## Interview Method

Use `templates/core-question-bank.md` for the exact 24-question backbone. Adapt wording to the participant's own language, but preserve each question's function and the 6-question checkpoints.

### Phase 0 — Contract and baseline (2 questions)

**Goal:** Define what decision or behavior this interview should improve.

Capture:

- desired outcome from the process;
- current dating/relationship context;
- topics to avoid or approach carefully;
- baseline 0–10 ratings: clarity, agency, distress/rumination, confidence in next steps.

If the participant asks for diagnosis, certainty about another person's motives, or crisis help, reset scope before continuing.

#### Outcome routing

The Q1 answer must change the interview's emphasis; it is not merely rapport-building metadata. Record one **primary outcome** and, only if clearly stated, one secondary outcome. Preserve the 24-question backbone and the same epistemic safeguards, but use the primary outcome to route behavior:

| Primary outcome | Agent emphasis | Adaptive follow-ups | Case selection | Final-output priority | Earlier stopping condition |
|---|---|---|---|---|---|
| **Understand why patterns repeat** | Current trigger → prediction → feeling → protection → consequence loops; developmental context only after adult evidence | Competing mechanisms, origins when action-relevant, counterexamples | Repeated pattern plus healthiest contrasting case | Pattern cards, confidence, alternative explanations, maintenance mechanisms | A supported/plausible mechanism can be stated and tested without more origin excavation |
| **Decide what to change** | Present behaviors under the participant's control: selection, pacing, reciprocity, communication, boundaries, repair | Moments where a different action could have changed information or outcome | Recent/actionable cases and successful exceptions | Prioritized behavior changes, continuation gates, 30–90 day experiments | Additional history would not change the action plan |
| **Clarify the relationship wanted** | Ordinary-life fit, values, desire, affection, faith/culture, roles, tradeoffs, and standards | Ambiguities among non-negotiables, preferences, and fantasies | Best-fit, poor-fit, and “good on paper but not desired” examples | Relationship direction card, signal-weighting profile, selection criteria | The target and tradeoffs are specific enough to guide real choices |
| **Test a specific concern** | Convert the concern into a falsifiable hypothesis before gathering evidence | Evidence that distinguishes the concern from alternatives; active disconfirmation | Cases most relevant to the concern plus at least one counterexample | Hypothesis verdict: supported/plausible/speculative/contradicted, risk if wrong, next observation | Available evidence has reached saturation or real-world data are required |
| **Other concrete goal** | Translate the goal into a decision, behavior, or artifact before continuing | Only information that changes that decision/artifact | Cases selected for relevance, not drama | Output explicitly matched to the stated goal | The agreed output can be produced responsibly |

At every checkpoint, report whether the interview is producing evidence for the primary outcome. If not, redirect the remaining questions or offer early synthesis.

The outcome changes **attention and allocation**, not standards of truth. Never selectively gather confirming examples, suppress counterevidence, force childhood causation because the participant asked “why,” or skip safety and scope rules to satisfy the requested outcome.

#### Route transparency and branch contracts

Adaptiveness should create useful depth without making the participant wonder where the conversation is going.

After Q1 and Q2, give a brief working route in participant-facing language:

> Your primary goal is [goal]. We’ll first define the relationship you want, then map the most informative relationship chapters and compare them. If an adult pattern raises a meaningful developmental question, I may propose a short adolescence or childhood branch and explain exactly what it would test. We will then challenge the strongest explanation and finish with concrete changes or experiments. I’ll show you our progress every six core questions, and you can redirect or stop at any checkpoint.

Before any adaptive branch—especially adolescence, childhood, trauma, sexuality, or family-of-origin—state a **branch contract**:

1. **Current hypothesis:** what adult pattern or unanswered question prompted the branch.
2. **Why this branch may help:** what distinction the answers could clarify.
3. **What it cannot establish:** usually causal certainty, hidden trauma, or another person's motives.
4. **Budget:** how many adaptive questions are proposed.
5. **Return point:** which core phase the interview will resume afterward.
6. **Choice:** ask whether the participant wants to take the branch, defer it, or continue on the main route.

Example:

> A recurring pattern may involve feeling exposed when romantic interest becomes visible. A two-question adolescence branch could help us distinguish whether that response also appeared around peer evaluation before your adult relationships. It would not prove childhood causation. Afterward we would return to comparing your adult cases. Would that branch be useful, or should we stay with the adult timeline?

After a branch, explicitly reconnect it:

> Here is what the branch added, what remains uncertain, and whether it changes our current explanation or action plan. We are now returning to [phase].

At every six-question checkpoint, show:

- **Destination:** the participant's primary outcome;
- **Current location:** phase and question count;
- **Evidence gained:** what the answers have contributed;
- **Active hypotheses:** with confidence and counterevidence;
- **Why the next section matters:** the decision or distinction it should improve;
- **Remaining route:** including any proposed optional branches;
- **Choice:** continue, redirect, pause, or synthesize.

Do not eliminate useful developmental exploration merely to stay linear. Make it visible, justified, bounded, and connected to the final outcome.

### Phase 1 — Desired life and relationship (4 questions)

Start with an ordinary-day picture several years in the future, not a trait checklist.

Cover:

- marriage/commitment, children, faith/culture, home, work, money, and family roles;
- affection, sex, companionship, conflict, repair, and independence;
- non-negotiables, strong preferences, flexible preferences, and unknowns;
- tradeoffs the participant is genuinely willing to make.

Output a **relationship direction card**. Do not turn this into a fantasy-partner inventory.

### Phase 2 — Relationship timeline and matrix (8 core questions)

Map up to five significant relationships or dating situations. Add one meaningful non-relationship period if it shaped the pattern. Use adaptive follow-ups only when a case cannot be represented accurately from the core answers.

For each case, capture only what is needed:

- age/life stage, duration, start, transition, and ending;
- initial and changing attraction;
- pacing of emotional, sexual, logistical, and commitment intimacy;
- initiation, follow-through, reciprocity, and choice;
- commitment, investment, perceived alternatives, and what made staying or leaving difficult;
- emotional safety and responsiveness;
- vulnerability and emotional intimacy;
- affection and sexuality, only with permission and when relevant;
- conflict, rupture, and repair;
- power, agency, boundaries, influence, and coercion;
- values, faith/culture, work, geography, family, and timing;
- the participant's behavior and what carried forward.

Rules:

1. Ask for concrete episodes before explanations.
2. Ask “What happened next?” before “Why do you think?”
3. Record positive and negative evidence.
4. Do not create a full dossier for every minor date.
5. Do not infer an absent partner's internal state from one person's account.

Use `templates/relationship-matrix.md` when an artifact is useful.

### Phase 3 — Cross-case pattern detection (4 questions)

Generate no more than five candidate pattern cards:

```text
Context/trigger
→ prediction or meaning
→ emotion/body signal
→ protective behavior
→ short-term payoff
→ long-term cost
→ counterevidence
→ current hypothesis and confidence
```

Useful distinctions include:

- attraction vs compatibility;
- chemistry vs consistency;
- availability vs reciprocity;
- responsiveness vs generic niceness;
- desire vs safety;
- explanation vs excuse;
- present evidence vs imagined potential;
- healthy independence vs protection from intimacy.

Do not assume unavailable-partner attraction, loss of interest when chosen, fear of intimacy, or childhood reenactment. Test each against actual cases.

### Phase 4 — Developmental context, only if useful (0–3 adaptive questions)

These do not count against the 24 core questions but do count against the 12-follow-up cap. Explore origins only after adult chronology and current mechanisms are visible. Use the mandatory branch contract before entering this phase, and explicitly reconnect any developmental evidence to the adult pattern and primary outcome before returning to the core route.

Possible domains:

- how caregivers showed love, comfort, conflict, affection, agency, and repair;
- peer belonging, teasing, exclusion, body image, status, and early romantic learning;
- cultural, religious, gender, and family scripts;
- performance or evaluation experiences resembling current triggers.

Safeguards:

- test neglect hypotheses against evidence of care;
- test “never chosen” narratives against evidence of interest;
- do not infer hidden events or recover memories;
- do not make childhood the sole cause;
- use “may have contributed,” not causal certainty.

Stop developmental questioning when another answer would not change present action.

### Phase 5 — Falsification and alternatives (3 questions)

For every high-impact formulation, ask:

1. What evidence does not fit?
2. What ordinary alternative could explain the same pattern—mismatch, partner behavior, limited dating pool, culture, timing, burnout, geography, or chance?
3. What future observation would increase or decrease confidence?

A final synthesis without counterevidence is incomplete.

### Phase 6 — Translation into action (3 questions)

Convert no more than three patterns into behavior.

Action classes:

- **Selection:** who receives another date or increased investment.
- **Reciprocity:** evidence required before escalating effort.
- **Communication:** one plain-language request, disclosure, or boundary.
- **Pacing:** slow fantasy, accelerate clarity, or limit ambiguous investment.
- **Exposure:** a small, safe act that tests a feared prediction.
- **Repair:** change a recurring conflict response.
- **Life design:** make room for partnership without erasing healthy identity.
- **Professional support:** bring a persistent or destabilizing issue to a qualified clinician.

Each experiment must state:

```text
Hypothesis:
Situation:
Old prediction:
New behavior:
What I will observe:
Safety boundary:
Review date:
```

## Required Checkpoints

After every six core questions:

1. Summarize the strongest facts and tentative hypotheses.
2. Name what remains unknown.
3. Invite correction: “What did I misunderstand or overstate?”
4. State the remaining question budget and phases.
5. Ask whether to continue, pause, or synthesize now.

If the participant pauses, produce a synthesis from current evidence. Do not pressure them to complete the protocol.

## Stopping Rules

Stop or move to synthesis when:

- the participant asks to pause;
- answers become repetitive;
- one person or episode is consuming more than roughly 30% of the interview without being the explicitly agreed focus;
- the participant is flooded, spiraling about one person, seeking certainty about another person's hidden feelings, or becoming more ashamed or hopeless;
- new questions only generate increasingly speculative origin stories;
- insight is no longer changing present-day action;
- distress is rising without corresponding value;
- the question budget is reached;
- a safety gate requires scope change;
- the participant has enough evidence for 1–3 useful experiments;
- the remaining uncertainty requires real-world observation rather than more interviewing.

Never keep asking questions merely because the interview has a numbered sequence.

## Required Final Artifacts

Use `templates/final-synthesis.md`.

The final output contains:

1. **Relationship direction card** — desired ordinary life, values, standards, and accepted tradeoffs.
2. **Relationship history matrix** — concise chronological evidence.
3. **Pattern cards** — maximum five, each with evidence, counterevidence, alternatives, risk if wrong, and confidence.
4. **Signal-weighting profile** — signals historically overweighted or underweighted, stated as hypotheses rather than verdicts.
5. **Strengths and protective capacities** — avoid deficit-only analysis.
6. **External constraints** — dating pool, faith/culture, timing, health, geography, workload, and other people's choices.
7. **Continuation gates** — behaviorally observable questions for early dating, 30 days, and 60–90 days; not rigid deadlines.
8. **Unresolved questions** — maximum five, preferably answerable by future observation.
9. **30–90 day operating plan** — 1–3 experiments, reciprocity/pacing rules, a skill, a boundary or clarity action, and a review date.
10. **Scope caveat** — what cannot be concluded from the interview.

## Safety Gates

Pause the normal interview if the participant reports:

- current coercion, stalking, threats, violence, or sexual assault;
- imminent self-harm or harm to another person;
- severe destabilization, dissociation, panic, or inability to function;
- ongoing abuse where confrontation could increase danger.

Respond with support, immediate safety orientation, and appropriate local or professional resources. Do not continue as though the primary issue were attachment or communication. For disclosed partner or sexual violence, use the WHO **LIVES** first-line sequence at a high level: Listen without judgment; Inquire about needs and concerns; Validate; Enhance safety; Support connection to chosen resources. Do not pressure for detail, tell the participant to confront or leave, or override their autonomy.

General safeguards:

- no participant or partner diagnoses;
- no direct-confrontation advice in unsafe relationships;
- no false-memory or hidden-trauma prompts;
- no moral ranking of attachment categories;
- no motive certainty from silence, texting patterns, or ambiguity;
- no copyrighted/proprietary questionnaire reproduction without permission;
- protect privacy: encourage pseudonyms and omission of identifying details;
- for friends, prefer that the friend participate directly; do not analyze a third party from hearsay or without informed consent;
- include faith, culture, sexuality, disability, class, and dating-pool constraints where relevant;
- use plain language rather than performative therapy jargon.

For personal health or crisis content, load `health-and-wellbeing-support` and follow its escalation rules.

## Outcome Evaluation

Before and immediately after the interview, rate 0–10:

- clarity about desired relationship;
- clarity about recurring patterns;
- confidence in next action;
- sense of agency;
- distress or rumination.

Ask:

- Which conclusion feels useful but uncertain?
- Which conclusion felt imposed or inaccurate?
- What action will occur because of this interview?

At 30 days, measure behavior rather than insight alone:

- dates initiated or accepted;
- clear bids made;
- ambiguous situations clarified or released;
- reciprocity-based investment decisions;
- boundaries communicated;
- small vulnerability/response experiments completed;
- rumination reduced;
- hypotheses strengthened, weakened, or discarded by new evidence.

## Common Pitfalls

1. **Endless numbered questions.** State the endpoint and budget at the start and every checkpoint.
2. **Attachment horoscope.** Use dimensions or mechanisms only when evidence supports them; never assign a fixed identity.
3. **Childhood monocausality.** Map adult behavior first and treat developmental explanations as optional contributors.
4. **Narrative fallacy.** Require counterevidence, alternatives, and confidence labels.
5. **Partner prosecution.** Describe observed behavior and compatibility; do not diagnose motives or disorders.
6. **Deficit-only analysis.** Preserve strengths, positive experiences, and adaptive functions of protective behavior.
7. **Insight without action.** No final synthesis is complete without a reversible experiment or decision rule.
8. **Generic questions.** Use the participant's own language and ask about concrete episodes.
9. **Premature sexual or trauma detail.** Ask permission and explain relevance.
10. **Treating an individual narrative as dyadic truth.** State the limits of one-person retrospective evidence.

## Verification Checklist

Before completing an interview, verify:

- [ ] Purpose, scope, question budget, and checkpoints were stated.
- [ ] Questions were asked one at a time.
- [ ] Desired relationship/life was defined before pattern analysis.
- [ ] Chronology and concrete episodes preceded theory.
- [ ] Attraction, reciprocity, safety, compatibility, and availability were distinguished.
- [ ] External constraints and other people's observed choices were included.
- [ ] Every high-impact hypothesis includes counterevidence and alternatives.
- [ ] No diagnosis, hidden-trauma inference, or fixed attachment label was given.
- [ ] Strengths and adaptive functions were preserved.
- [ ] Stopping rules were honored.
- [ ] Final output includes 1–3 testable actions and a review date.

## Research Foundation

See `references/research-foundation.md` for the relationship-science constructs, source links, limitations, and validation roadmap behind this protocol.

## Safety Reference

See `references/safety-guardrails.md` for opening language, trauma/distress handling, abuse/coercion/stalking behaviors, suicidality routing, privacy and digital-safety rules, false-memory safeguards, cultural/faith considerations, referral language, and authoritative sources. Load it whenever sensitive or high-risk content appears.
