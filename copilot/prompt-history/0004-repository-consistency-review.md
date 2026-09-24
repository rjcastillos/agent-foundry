# Prompt History: Repository Consistency Review

- Date: 2026-09-24
- Asset: `prompts/repository-consistency-review.prompt.md`
- Change: Added a reusable repository-local audit prompt for detecting contradictions between policy, documentation, assets, scripts, templates, and validation mechanisms.
- Justification: Keep future consistency reviews out of transient chat context while preserving a repeatable method, evidence requirements, and review history.
- Scope of initial review: Full repository, with focus on documented layout, reusable asset conventions, synchronizer documentation and implementation, and Copilot memory records.
- Initial findings: Synchronizer documentation disagrees with its Python defaults; synchronizer history contains stale paths and identities; repository conventions contain duplicate metadata and an unfinished section; several guidance and example files are empty or placeholder-only; asset naming and validation claims are inconsistent.
- Affected files or areas:
  - `prompts/repository-consistency-review.prompt.md`
  - `tools/scripts/sync_repo/README.md`
  - `tools/scripts/sync_repo/sync_repo.py`
  - `docs/repository-conventions.md`
  - `copilot/decisions/`
  - `copilot/prompt-history/`
  - Empty or placeholder guidance and asset files identified by the review
- Related decision record: None. The initial review reports issues but does not yet accept a repository policy change.
- Compatibility or migration notes: Future reviews should use the next available history number and create a decision record only when a policy change is accepted.
