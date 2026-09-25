# Prompt Name

## Purpose

Describe the task this prompt performs and the expected outcome.

## Inputs

- Repository or file scope: `<scope>`
- User request: `<request>`
- Optional constraints: `<constraints>`

## Instructions

Act as `<role>`. Follow these steps:

1. Inspect the relevant context.
2. Apply the required analysis or transformation.
3. Validate the result.
4. Report the outcome and remaining risks.

## Output Format

Return:

- Summary
- Findings or result
- Files affected
- Validation performed
- Open questions

## Guardrails

- Do not invent missing facts.
- Do not modify files unless explicitly requested.
- State uncertainty clearly.
