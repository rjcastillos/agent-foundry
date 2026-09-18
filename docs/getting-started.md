# Getting Started

## Browse the catalog

Clone the repository and inspect the category directories:

```bash
git clone <repository-url>
cd agent-foundry
```

Start with an asset's `AGENT.md`, `SKILL.md`, prompt file, or workflow README. Confirm its `status`, `version`, compatibility, dependencies, and examples before using it.

## Reuse an asset

Copy the complete asset directory into the destination expected by your AI tool or repository conventions. For example:

```text
agent-foundry/skills/gocoder/
	-> consuming-repository/.agents/skills/gocoder/
```

The source directories remain visible in this repository. Only the consuming repository needs a hidden destination when a tool requires one.

## Create an asset

1. Choose the category that owns the behavior.
2. Start from the matching directory under `templates/`.
3. Give the asset a descriptive kebab-case directory name.
4. Add metadata and usage instructions using the conventions in `repository-conventions.md`.
5. Include a minimal example and record dependencies or compatibility limits.

## Current maturity

This repository is intentionally skeletal while the asset contract is being established. The `gocoder` skill is the reference implementation; the other examples and templates are starting points rather than complete production assets.
