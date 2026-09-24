# Prompt History: Repository Consistency Review Skill

- Date: 2026-09-24
- Asset: `skills/repository-consistency-review/SKILL.md`
- Change: Added a reusable skill version of `prompts/repository-consistency-review.prompt.md` with activation triggers, audit workflow, finding contract, guardrails, validation rules, and traceability requirements.
- Justification: Make repository consistency reviews discoverable and reusable as an agent skill while preserving the original prompt as a direct prompt option.
- Related prompt: `prompts/repository-consistency-review.prompt.md`
- Affected files or areas:
  - `skills/repository-consistency-review/SKILL.md`
  - `prompts/repository-consistency-review.prompt.md`
  - `copilot/prompt-history/`
- Related decision record: None. This adds a reusable capability without changing repository policy.
- Compatibility or migration notes: The skill is read-only by default. Use the existing prompt-history and decision-record rules when a review must be persisted or results in an accepted policy change.
