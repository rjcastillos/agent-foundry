# Decision: Synchronizer Ignores Source Exclusions and Reports Actual Actions

- Date: 2026-09-22
- Status: Accepted
- Scope: `tools/scripts/sync_repo/`
- Decision: The repository overlay synchronizer must honor the source root `.gitignore`, compare transformed text before writing, and distinguish skipped, unchanged, created, and replaced target actions in its console output.
- Rationale: Prevent ignored artifacts from leaking into TARGET and make synchronization logs accurately describe filesystem impact instead of reporting every processed file as updated.
- Affected files or areas:
  - `tools/scripts/sync_repo/sync_repo.py`
  - `tools/scripts/sync_repo/README.md`
  - Root `README.md`