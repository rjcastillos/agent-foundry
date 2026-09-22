# AISeed Foundry

> A centralized collection of reusable AI engineering assets, including agents, skills, prompts, workflows, templates, MCP integrations, examples, and knowledge bases.

AISeed Foundry serves as a personal and collaborative foundation for building, sharing, and reusing AI-powered development assets across projects. The repository is designed to promote consistency, accelerate development, and capture proven patterns for Agentic AI solutions.

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

---

## Prompts

Reusable prompt libraries for common engineering and operational tasks.

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

Clone the repository:

```bash
git clone <repository-url>
cd agent-foundry
```

Explore available assets:

```bash
tree -L 2
```

Review repository standards:

```text
docs/repository-conventions.md
```

Create new assets from the provided templates:

```text
templates/
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

AISeed Foundry is intended for:

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