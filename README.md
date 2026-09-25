# Agent Foundry

> A centralized collection of reusable AI engineering assets, including agents, skills, prompts, workflows, templates, MCP integrations, examples, and knowledge bases.

Agent Foundry serves as a personal and collaborative foundation for building, sharing, and reusing AI-powered development assets across projects. The repository is designed to promote consistency, accelerate development, and capture proven patterns for Agentic AI solutions.

## Vision

Create a single source of truth for AI development assets that can be reused across multiple projects, teams, and technologies.

The repository focuses on:

- Reusability
- Standardization
- Discoverability
- Automation
- Knowledge Sharing
- Continuous Improvement

---

# Repository Structure

```text
agent-foundry/
│
├── agents/
├── skills/
├── prompts/
├── templates/
├── workflows/
├── mcp/
├── examples/
├── knowledge/
├── .github/
├── copilot/
├── docs/
├── tools/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

---

# Source Assets from this repo and real Generated Projects using this repo assets

The root-level directories are the canonical source catalog for Agent Foundry.
For example, reusable skills are authored under:

```text
skills/<skill-name>/SKILL.md
```

When these assets are copied into another project, GitHub- and
Copilot-specific assets belong under that project's `.github/` directory:

```text
.github/
├── copilot-instructions.md
├── instructions/
├── agents/
├── prompts/
├── skills/
├── copilot/
│   ├── decisions/
│   └── prompt-history/
└── workflows/
```

If both locations exist in the same project:

- `.github/skills/` is the active project-local configuration.
- Root-level `skills/` is the reusable source and reference catalog.
- Changes made to `.github/skills/` do not automatically update the source asset.
- New or improved reusable content should be copied back to the root-level
    source directory deliberately.
- Generated projects may customize their `.github/skills/` copy without
    changing the Agent Foundry source asset.

For this repository, `.github/` contains repository-local instructions.
Root-level assets remain the canonical reusable source unless a specific
instruction explicitly states otherwise.

# However, not everything belongs there
docs/       # General project documentation
adr/        # Optional architecture decision records
src/        # Application source
tests/      # Tests
.vscode/    # Editor and MCP configuration, where applicable

---

# Asset Types

## Agents

Reusable AI agents designed to perform specific roles or solve specific problems.

Examples:

- GitHub Release Agent
- Incident Response Agent
- Kubernetes Operations Agent
- Azure Cost Optimization Agent

Location:

```text
agents/
```

---

## Skills

Reusable capabilities that can be consumed by AI agents.

Examples:

- Generate Go Service
- Review Pull Request
- Validate Terraform Module
- Create Kubernetes Manifest

Location:

```text
skills/
```

The repository consistency audit is available as the reusable skill
[`skills/repository-consistency-review/SKILL.md`](skills/repository-consistency-review/SKILL.md).

---

## Prompts

Reusable prompt libraries for common engineering and operational tasks.

For repeatable repository audits, use [`prompts/repository-consistency-review.prompt.md`](prompts/repository-consistency-review.prompt.md)
and record the resulting review in `copilot/prompt-history/`.

Examples:

- Code Review
- Architecture Review
- Root Cause Analysis
- Documentation Generation

Location:

```text
prompts/
```

---

## Workflows

Agentic workflows that define repeatable processes.

Examples:

- CI/CD Workflow
- Release Workflow
- Incident Management Workflow
- Skill Validation Workflow

Location:

```text
workflows/
```

---

## MCP Integrations

Model Context Protocol (MCP) integrations and configurations.

Examples:

- GitHub MCP
- Azure DevOps MCP
- Jira MCP
- ServiceNow MCP

Location:

```text
mcp/
```

---

## Templates

Reusable templates to accelerate creation of new assets.

Examples:

- Agent Template
- Skill Template
- Workflow Template
- MCP Template

Location:

```text
templates/
```

---

## Knowledge Base

Reference documentation, architecture notes, patterns, lessons learned, and AI engineering practices.

Location:

```text
knowledge/
```

---

## Copilot Memory

Repository-level decisions and prompt history for reusable AI assets are maintained in:

```text
copilot/
├── decisions/
└── prompt-history/
```

Use `copilot/decisions/` to record durable decisions with their rationale and affected areas. Use `copilot/prompt-history/` to record significant changes to prompts, agents, and skills.

Generated projects should keep their local Copilot instructions and memory under `.github/copilot/`.

---

## Examples

Working examples demonstrating how assets can be implemented and used.

Location:

```text
examples/
```

---

# Standards

## Repository Tools

The repository includes an overlay synchronizer for copying reusable assets
from this repository into a related target repository without deleting
target-only content:

```text
tools/scripts/sync_repo/
```

The synchronizer honors the source `.gitignore` and reports whether each
target path was skipped, created, replaced, or left unchanged. See
`tools/scripts/sync_repo/README.md` for usage and output details.
When SOURCE is a Git worktree, untracked files are skipped and a summary of
scanned, created, and changed files is printed at completion.


See:

```text
docs/repository-conventions.md
```

Key principles:

- Use kebab-case names
- Favor descriptive names over abbreviations
- Version reusable assets
- Keep assets self-contained
- Design for reuse across projects
- Keep generated test outputs under `output/`
- Do not commit dependency directories such as `node_modules/`
- Commit lockfiles when they provide reproducible installs

---

# Getting Started

Agent Foundry is a catalog of reusable agents, skills, prompts, workflows,
templates, examples, knowledge, and automation tools.

## Explore the Repository

Start with:

- `agents/` for reusable agent definitions
- `skills/` for reusable capability playbooks
- `prompts/` for reusable prompt definitions
- `workflows/` for repeatable processes
- `templates/` for new asset starting points
- `docs/repository-conventions.md` for naming and structure rules

## Create a Reusable Asset

1. Identify the asset type.
2. Copy the corresponding directory from `templates/`.
3. Give the asset a descriptive kebab-case name.
4. Add required metadata and usage instructions.
5. Include examples where they clarify expected behavior.
6. Validate paths, entry-point names, and Markdown structure.

## Use an Asset in Another Project

Copy the selected asset into the appropriate project-local location.
GitHub- and Copilot-specific assets normally belong under `.github/`.

For skills, use:

```text
.github/skills/<skill-name>/SKILL.md
```

---

# Recommended Workflow

1. Identify a reusable capability.
2. Create a corresponding Agent, Skill, Prompt, or Workflow.
3. Document usage and examples.
4. Version the asset.
5. Reuse it across projects.
6. Improve and iterate continuously.

---

# Target Audience

Agent Foundry is intended for:

- AI Engineers
- DevOps Engineers
- Platform Engineers
- Software Developers
- SRE Teams
- Automation Engineers
- Technical Architects

---

# Guiding Principle

> Build once, document well, reuse everywhere.

Every contribution should increase the repository's value as a reusable foundation for future AI-powered projects.

---

# License

See the repository LICENSE file for details.