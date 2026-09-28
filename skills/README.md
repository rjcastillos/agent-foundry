# Skills

This directory contains reusable capabilities designed for AI agents, Copilot, and autonomous workflows.

A skill encapsulates a specialized task or domain expertise—such as code review, infrastructure automation, repository auditing, or language-specific development—along with its triggering conditions, workflow, decision rules, guardrails, and validation procedure.

## Skill Structure

Each skill resides in its own subdirectory and contains:

- `SKILL.md`: The primary skill definition, including metadata, trigger scenarios, workflow, decision rules, guardrails, and output contract.
- Supporting files: Scripts, examples, configuration templates, or reference materials specific to the skill's domain (optional).

## Skill Metadata

Every skill defines:

| Field | Purpose |
| --- | --- |
| `name` | Unique kebab-case identifier for the skill (e.g., `repository-consistency-review`) |
| `description` | Concise summary of the skill's purpose and "Use when..." trigger clause |
| `version` | Semantic version (e.g., `1.0.0`) |
| `compatibility` | Tool compatibility, runtime requirements, or access constraints |
| `metadata.author` | Skill creator or maintaining team |
| `metadata.category` | Domain or type (e.g., `Repository Maintenance`, `Code Review`, `DevOps`) |
| `tags` (optional) | Searchable keywords (e.g., `go`, `kubernetes`, `devops`) |

## What Each Skill Should Document

1. **Trigger Scenarios**: Explicit conditions or user requests that activate the skill.
2. **Workflow**: Step-by-step execution phases (discovery, analysis, implementation, validation).
3. **Decision Rules**: Branching logic for handling edge cases, missing context, or conflicts.
4. **Negative Guardrails**: Hard constraints on what the skill must never do.
5. **Output Contract**: Expected format, structure, and content of the skill's output.

## Skill Categories

Skills commonly fall into these domains:

- **Repository Maintenance**: Consistency review, documentation audit, validation.
- **Code Review & Quality**: Security analysis, performance audit, style enforcement.
- **Domain Specialization**: Language-specific development (Go, Python, etc.), specialized workflows.
- **Automation & DevOps**: Infrastructure changes, deployment, CI/CD configuration.
- **Testing & Validation**: Test generation, coverage analysis, integration testing.

## Creating a New Skill

1. Identify the skill's domain and purpose.
2. Choose a descriptive kebab-case name (e.g., `kubernetes-manifest-validator`, `python-type-annotator`).
3. Copy the directory structure from `templates/skill-template/`.
4. Fill in the SKILL.md metadata, triggers, and workflow.
5. Include examples of expected inputs and outputs.
6. Document decision rules and guardrails explicitly.
7. Test the skill against its intended use cases.
8. Add or update `copilot/prompt-history/` when the skill is added or significantly changed.

## Using a Skill in a Project

Skills are designed to be copied into project-local locations, typically:

```text
.github/skills/<skill-name>/SKILL.md
```

When a skill is copied:

- It becomes project-local and can be customized without affecting the AISeed Foundry source.
- The original skill in `skills/` remains the canonical reusable source.
- Document significant customizations in the project's own `copilot/prompt-history/`.

## Validation

Skills should include or reference:

- Trigger detection examples (user phrases or patterns that activate the skill).
- Expected output examples.
- Available validation commands or procedures.
- Known limitations or edge cases.

If no executable validator exists, the skill should document this explicitly.

## Reference Skills

- `repository-consistency-review`: Audits repositories for policy/documentation drift.
- `gocoder`: Senior Go developer expertise and DevOps workflow.
- `bashcoder`: Bash scripting and shell automation.
- `example-skill`: Template showing expected structure and metadata.
