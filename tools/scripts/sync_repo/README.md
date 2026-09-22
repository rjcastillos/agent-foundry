# Repository Overlay Synchronizer

## Overview

This utility synchronizes content from:

```text
/home/a233c1f/agent-foundry
```

into:

```text
/home/a233c1f/agent-foundry
```

The synchronization is performed as an **overlay operation**.

This means:

- New files from SOURCE are copied to TARGET.
- Modified files from SOURCE update matching files in TARGET.
- Files and directories existing only in TARGET are preserved.
- No files are removed from TARGET.
- Repository references are automatically renamed.

---

## Repository Name Transformation

During synchronization, all text files are scanned for repository references.

The following replacement is performed:

```text
agent-foundry -> agent-foundry
```

The original letter case is preserved.

Examples:

```text
agent-foundry  -> agent-foundry
AGENT-FOUNDRY  -> AGENT-FOUNDRY
Agent-Foundry  -> Agent-Foundry
```

---

## Directory Configuration

Current configuration:

```python
SOURCE = "/home/a233c1f/agent-foundry"
TARGET = "/home/a233c1f/agent-foundry"
```

---

## Main Processing Blocks

### 1. Configuration

Defines:

- Source repository
- Target repository
- Repository name mapping
- Excluded directories

---

### 2. Repository Name Replacement

The script searches text files for:

```text
agent-foundry
```

and replaces them with:

```text
agent-foundry
```

while maintaining the original casing.

---

### 3. File Detection

The script performs a simple text-file detection.

Text files:

- Read contents
- Replace repository references
- Write updated contents

Binary files:

- Copied unchanged

---

### 4. Overlay Synchronization

The SOURCE repository is traversed recursively.

For every file:

- If the file does not exist in TARGET:
  - Copy file

- If the file exists and differs:
  - Update file

- If the transformed source content matches TARGET:
  - Leave TARGET untouched

- If the file matches `SOURCE/.gitignore`:
  - Skip it and do not copy or update TARGET

- If SOURCE is a Git worktree and the file is not tracked by Git:
  - Skip it and do not copy or update TARGET

- If the file exists only in TARGET:
  - Leave untouched

No deletions are performed.

### Console Output

Each source file reports its impact on TARGET:

```text
[SKIPPED  ] SOURCE /home/a233c1f/agent-foundry/output/report.docx (SOURCE/.gitignore)
[CREATED  ] SOURCE /home/a233c1f/agent-foundry/new-file.md -> TARGET /home/a233c1f/agent-foundry/new-file.md
[REPLACED ] SOURCE /home/a233c1f/agent-foundry/README.md -> TARGET /home/a233c1f/agent-foundry/README.md
[UNCHANGED] SOURCE /home/a233c1f/agent-foundry/LICENSE -> TARGET /home/a233c1f/agent-foundry/LICENSE
[SKIPPED  ] SOURCE /home/a233c1f/agent-foundry/local-note.md (untracked by Git)
```

`REPLACED` and `CREATED` are emitted only when TARGET is actually written.
Text files are transformed before comparison so repository-name replacements
do not cause unnecessary writes.

At completion, the script prints:

```text
Synchronization summary:
  Files scanned in SOURCE : 120
  Files created in TARGET : 5
  Files changed in TARGET : 12
```

`Files scanned in SOURCE` counts every regular file discovered before skip
rules are applied. Created and changed totals count only files actually
written to TARGET; unchanged and skipped files are excluded from those totals.

---

### 5. Safety Controls

The following directories are ignored:

```text
.git
__pycache__
.pytest_cache
.mypy_cache
.tox
.venv
venv
```

This prevents accidental synchronization of:

- Git metadata
- Python build artifacts
- Temporary caches

The root `SOURCE/.gitignore` is also loaded. Files matching its patterns are
skipped and are never copied or updated in TARGET. Negated patterns beginning
with `!` are supported with last-match-wins behavior.

If SOURCE contains a `.git` directory or worktree marker, the script also
uses `git ls-files --others --exclude-standard` to identify non-ignored files
that Git does not track. Those files are skipped as untracked. If Git is not
available or SOURCE is not a Git worktree, this additional check is disabled.

---

## Usage

Run:

```bash
python3 sync_repo.py
```

or

```bash
chmod +x sync_repo.py
./sync_repo.py
```

---

## Example

Initial state:

```text
SOURCE
├── README.md
├── docs/
└── skills/

TARGET
├── README.md
├── docs/
├── skills/
└── experiments/
```

After synchronization:

```text
TARGET
├── README.md      (updated)
├── docs/          (updated)
├── skills/        (updated)
└── experiments/  (preserved)
```

---

## Design Principles

- Simple Python implementation
- Standard library only
- No external dependencies
- Safe overlay behavior
- Readable and maintainable code
- Suitable for automation and CI/CD pipelines