#!/usr/bin/env python3

"""
Repository Overlay Synchronizer

Purpose
-------
Update TARGET with the latest content from SOURCE while preserving
TARGET-specific files and directories.

Behavior
--------
- Copy new files from SOURCE to TARGET.
- Update modified files in TARGET.
- Preserve files/directories that exist only in TARGET.
- Replace repository references:
      agent-foundry -> agent-foundry
- Preserve the original letter case of repository names.
- Skip common cache and Git metadata directories.
- Skip files ignored by SOURCE/.gitignore.
- Report whether each TARGET path was skipped, unchanged, created, or replaced.
- Skip files not tracked by Git when SOURCE is a Git worktree.
- Report synchronization totals at completion.
"""

from pathlib import Path
import filecmp
import fnmatch
import re
import shutil
import subprocess


# ============================================================================
# Configuration
# ============================================================================

SOURCE = "/home/a233c1f/agent-foundry"
TARGET = "/home/a233c1f/agent-foundry"

SOURCE_REPO = "agent-foundry"
TARGET_REPO = "agent-foundry"

#SOURCE = "/home/a233c1f/agent-foundry"
#TARGET = "/home/a233c1f/agent-foundry"

#SOURCE_REPO = "agent-foundry"
#TARGET_REPO = "agent-foundry"

SOURCE_GITIGNORE = Path(SOURCE) / ".gitignore"

EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".venv",
    "venv",
}


# ============================================================================
# Repository Name Replacement
# ============================================================================

def match_case(source_text: str, replacement: str) -> str:
    """
    Apply the casing style of source_text to replacement.

    Examples:
        agent-foundry -> agent-foundry
        AGENT-FOUNDRY -> AGENT-FOUNDRY
        Agent-Foundry -> Agent-Foundry
    """

    if source_text.isupper():
        return replacement.upper()

    if source_text.islower():
        return replacement.lower()

    if source_text.istitle():
        return replacement.title()

    result = []

    for index, char in enumerate(replacement):
        if index < len(source_text) and source_text[index].isupper():
            result.append(char.upper())
        else:
            result.append(char.lower())

    return "".join(result)


def replace_repository_references(content: str) -> str:
    """
    Replace repository references while preserving letter case.
    """

    pattern = re.compile(re.escape(SOURCE_REPO), re.IGNORECASE)

    return pattern.sub(
        lambda match: match_case(
            match.group(0),
            TARGET_REPO
        ),
        content,
    )


# ============================================================================
# File Helpers
# ============================================================================

def is_excluded(path: Path) -> bool:
    """
    Determine whether a path should be skipped.
    """

    return any(part in EXCLUDED_DIRS for part in path.parts)


def load_gitignore_patterns(gitignore_file: Path) -> list[str]:
    """Load non-empty, non-comment patterns from SOURCE/.gitignore."""

    if not gitignore_file.exists():
        return []

    return [
        line.strip()
        for line in gitignore_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def is_gitignored(
    source_file: Path,
    source_root: Path,
    patterns: list[str],
) -> bool:
    """Apply common root .gitignore patterns using last-match-wins semantics."""

    relative_path = source_file.relative_to(source_root).as_posix()
    path_parts = relative_path.split("/")
    ignored = False

    for raw_pattern in patterns:
        pattern = raw_pattern
        negated = pattern.startswith("!")
        if negated:
            pattern = pattern[1:]

        directory_pattern = pattern.endswith("/")
        pattern = pattern.rstrip("/").lstrip("/")
        if not pattern:
            continue

        if "/" in pattern:
            matches = fnmatch.fnmatch(relative_path, pattern)
        else:
            matches = any(fnmatch.fnmatch(part, pattern) for part in path_parts)

        if directory_pattern:
            matches = matches or any(
                fnmatch.fnmatch("/".join(path_parts[:index]), pattern)
                for index in range(1, len(path_parts))
            )

        if matches:
            ignored = not negated

    return ignored


def load_untracked_files(source_root: Path) -> set[str]:
    """Return non-ignored files not tracked by Git, if SOURCE is a worktree."""

    if not (source_root / ".git").exists():
        return set()

    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(source_root),
                "ls-files",
                "--others",
                "--exclude-standard",
                "-z",
            ],
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return set()

    return {
        path.decode("utf-8")
        for path in result.stdout.split(b"\0")
        if path
    }


def is_text_file(file_path: Path) -> bool:
    """
    Simple text-file detection.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.read(1024)
        return True
    except Exception:
        return False


def process_file(source_file: Path, target_file: Path) -> str:
    """
    Copy a file from SOURCE to TARGET.

    Text files:
        Replace repository references.

    Binary files:
        Copy as-is.

    Returns:
        The actual TARGET action: unchanged, created, or replaced.
    """

    if is_text_file(source_file):
        try:
            content = source_file.read_text(encoding="utf-8")

            transformed_content = replace_repository_references(
                content
            )

            if target_file.exists() and target_file.read_text(
                encoding="utf-8"
            ) == transformed_content:
                return "unchanged"

            existed = target_file.exists()
            target_file.parent.mkdir(parents=True, exist_ok=True)
            target_file.write_text(
                transformed_content,
                encoding="utf-8"
            )

            return "replaced" if existed else "created"

        except Exception:
            pass

    if target_file.exists() and filecmp.cmp(
        source_file,
        target_file,
        shallow=False,
    ):
        return "unchanged"

    existed = target_file.exists()
    target_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_file, target_file)
    return "replaced" if existed else "created"


# ============================================================================
# Synchronization Logic
# ============================================================================

def sync_source_to_target() -> None:
    """
    Overlay SOURCE onto TARGET.

    Rules:
    - SOURCE is authoritative for matching paths.
    - TARGET-specific files remain untouched.
    - No deletions are performed.
    """

    source_root = Path(SOURCE)
    target_root = Path(TARGET)

    print(f"Source : {source_root}")
    print(f"Target : {target_root}")
    print()

    gitignore_patterns = load_gitignore_patterns(SOURCE_GITIGNORE)
    untracked_files = load_untracked_files(source_root)
    totals = {
        "scanned": 0,
        "created": 0,
        "changed": 0,
    }

    for source_file in source_root.rglob("*"):

        if is_excluded(source_file):
            continue

        if source_file.is_dir():
            continue

        totals["scanned"] += 1
        relative_path = source_file.relative_to(source_root)
        relative_path_text = relative_path.as_posix()
        if is_gitignored(source_file, source_root, gitignore_patterns):
            print(f"[SKIPPED  ] SOURCE {source_file} (SOURCE/.gitignore)")
            continue

        if relative_path_text in untracked_files:
            print(f"[SKIPPED  ] SOURCE {source_file} (untracked by Git)")
            continue

        target_file = target_root / relative_path
        action = process_file(source_file, target_file)
        if action == "created":
            totals["created"] += 1
        elif action == "replaced":
            totals["changed"] += 1

        print(
            f"[{action.upper():9}] SOURCE {source_file} -> TARGET {target_file}"
        )

    print()
    print("Synchronization summary:")
    print(f"  Files scanned in SOURCE : {totals['scanned']}")
    print(f"  Files created in TARGET : {totals['created']}")
    print(f"  Files changed in TARGET : {totals['changed']}")


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    """
    Program entry point.
    """

    print("Starting repository synchronization...")
    sync_source_to_target()
    print()
    print("Synchronization completed successfully.")


if __name__ == "__main__":
    main()