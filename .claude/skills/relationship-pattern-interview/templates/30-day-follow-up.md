# 30-Day Follow-Up Reminder Template

Use only after the participant explicitly agrees to a reminder.

## Suggested reminder name

`Relationship Pattern Interview — 30-day review`

## Schedule

One-shot, 30 days from final synthesis. Use whatever the environment provides, in order of preference:

1. A native scheduled task or automation (for example, ChatGPT scheduled tasks or Claude automations), delivered to the originating conversation unless the participant requests otherwise.
2. A calendar or cron tool the participant already uses.
3. No tooling: give the participant the reminder name above as a copyable calendar title plus the seven questions below.

## Self-contained reminder prompt

```text
Deliver a concise 30-day follow-up for a participant who completed an evidence-informed Relationship Pattern Interview. Do not diagnose, reinterpret their history, or schedule another reminder. Invite them to reply with answers to these behavioral review questions:

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

After scheduling, record the reminder's identifier or delivery method in `templates/final-synthesis.md` (Follow-up commitment) and the Resume Capsule. If scheduling fails, provide the copyable calendar title and the seven questions instead of claiming success.
