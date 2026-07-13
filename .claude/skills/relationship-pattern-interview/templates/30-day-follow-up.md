# 30-Day Follow-Up Job Template

Use only after the participant explicitly agrees to a reminder.

## Suggested job name

`Relationship Pattern Interview — 30-day review`

## Schedule

One-shot, 30 days from final synthesis. In Hermes: `schedule="30d"`, `repeat=1`, `attach_to_session=true`, delivery to the originating conversation unless the participant requests otherwise.

## Self-contained cron prompt

```text
Deliver a concise 30-day follow-up for a participant who completed an evidence-informed Relationship Pattern Interview. Do not diagnose, reinterpret their history, or schedule another job. Invite them to reply with answers to these behavioral review questions:

1. What agreed experiment or behavior change did you actually try?
2. What observable result occurred?
3. Did you make any clear bids, clarify or release ambiguity, use reciprocity to guide investment, or communicate a boundary?
4. Did rumination decrease, stay the same, or increase?
5. Which provisional hypothesis is now stronger, weaker, contradicted, or still unknown?
6. Did any interview advice feel imposed or cause an unintended problem?
7. What should be kept, changed, or tested next?

State that lack of action is useful data rather than failure. Ask the participant to paste or reference their Resume Capsule/final synthesis if they want a detailed update. Keep the message under 180 words.
```

## Verification

After creating the job, record its job ID or delivery handle in `templates/final-synthesis.md` and the Resume Capsule. If scheduling fails, provide a copyable calendar title and the seven questions instead of claiming success.
