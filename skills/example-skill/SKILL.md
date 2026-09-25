---
name: example-skill
description: >-
	Example reusable skill showing the expected structure, metadata, workflow,
	validation, and guardrails for a project-specific capability.
version: "1.0.0"
compatibility: "Repository read and write access as required by the target task."
metadata:
	author: "Agent Foundry"
	category: "Example"
---

# Example Skill

Use this file as a starting point for a real skill. Replace the example
metadata, triggers, workflow, decision rules, and validation commands.

## Trigger Scenarios

Use this skill when the user requests:

- [Specific task or keyword]
- [Related task or keyword]

## Workflow

1. Inspect the target files and applicable instructions.
2. Identify the smallest change that satisfies the request.
3. Apply the change using the repository's established conventions.
4. Validate the result with the narrowest available check.
5. Report changed files, validation performed, and remaining risks.

## Decision Rules

- If required context is missing, ask for it before modifying files.
- If the requested change affects shared behavior, inspect call sites and tests.
- If validation is unavailable, state that explicitly.

## Negative Guardrails

- Do not modify unrelated files.
- Do not use machine-specific paths or credentials.
- Do not claim validation was performed when it was not.

## Output

Report:

- Summary of the result
- Files changed
- Validation performed
- Remaining questions or risks
