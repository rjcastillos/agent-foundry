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
aiseed-foundry/
│
├── agents/
├── skills/
├── prompts/
├── templates/
├── workflows/
├── mcp/
├── examples/
├── knowledge/
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

## Examples

Working examples demonstrating how assets can be implemented and used.

Location:

```text
examples/
```

---

# Standards

This repository follows a consistent set of naming and organizational conventions.

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

---

# Getting Started

Clone the repository:

```bash
git clone <repository-url>
cd aiseed-foundry
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