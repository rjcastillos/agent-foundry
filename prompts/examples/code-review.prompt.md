# Code Review Prompt

## Inputs

- Repository or file scope: `<scope>`
- Review focus: `<optional focus>`
- Risk tolerance: `<low|medium|high>`

## Instructions

Review the requested code as a senior maintainer. Prioritize correctness,
security, regressions, missing tests, and compatibility risks.

For each finding, provide:

- Severity
- File and location
- Evidence
- Impact
- Recommendation

Order findings from highest to lowest severity. If no issues are found, state
that clearly and mention remaining test gaps or residual risk.

Do not modify files unless the user explicitly requests implementation.
