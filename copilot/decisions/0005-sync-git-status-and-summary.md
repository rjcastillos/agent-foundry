# Decision: Skip Git-Untracked Source Files and Report Synchronization Totals

- Date: 2026-09-22
- Status: Accepted
- Scope: `tools/scripts/sync_repo/`
- Decision: When SOURCE is a Git worktree, skip files not tracked by Git. At completion, report source files scanned, target files created, and target files changed.
- Rationale: Prevent local, untracked source artifacts from propagating to TARGET and provide a concise measure of the synchronization impact.
- Affected files or areas:
  - `tools/scripts/sync_repo/sync_repo.py`
  - `tools/scripts/sync_repo/README.md`
  - Root `README.md`

  Seed:
  September 22 2026 13:55

  Synchronization summary:
  Files scanned in SOURCE : 435
  Files created in TARGET : 14
  Files changed in TARGET : 11