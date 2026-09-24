# Repository Consistency Review

Use this prompt to audit a repository for contradictions, stale references, incomplete assets, and gaps between documented policy and implementation.

## Inputs

- Repository root: `<repository-root>`
- Review date: `<YYYY-MM-DD>`
- Scope: `<full repository or selected paths>`
- Requested focus: `<optional focus>`

## Instructions

Act as a senior repository maintainer. Inspect the repository-local instructions first, then compare the authoritative documentation with the current files and implementation.

Check at least:

1. Root layout and documented directory trees against the actual repository.
2. Naming, entry-point, metadata, and front-matter conventions against representative assets and templates.
3. README, contribution, getting-started, and tool documentation against current commands and paths.
4. Scripts and examples against their documented defaults, inputs, outputs, and behavior.
5. Decision records and prompt history against their stated schemas, numbering, links, and affected paths.
6. Placeholder, empty, unfinished, duplicated, machine-specific, or contradictory content.
7. Validation claims against available tests, validators, CI workflows, and executable checks.

Use targeted reads and searches. Do not modify files during the audit unless explicitly requested. Treat repository-local instructions as policy, but report contradictions between policies rather than silently choosing one.

For every finding, capture:

| Field | Required content |
| --- | --- |
| Severity | `High`, `Medium`, or `Low` |
| Evidence | Exact repository-relative file paths and the conflicting facts |
| Impact | Why the inconsistency can mislead contributors or break workflows |
| Recommendation | Smallest practical remediation |
| Validation | A check that would confirm the remediation |

Order findings by severity, then by affected workflow. Distinguish confirmed inconsistencies from suggestions or questions. Do not report style preferences as defects unless a repository policy supports them.

## Traceability Outputs

After the audit, create or update these repository-relative records when the user requests a durable review:

- `copilot/prompt-history/NNNN-repository-consistency-review.md`: date, scope, prompt used, findings summary, and affected files.
- `copilot/decisions/NNNN-short-title.md`: only for accepted policy changes or decisions that affect future repository behavior.
- The relevant README or convention document: only when the review results in a changed path, naming rule, workflow, or supported behavior.

Use the next available sequence number. Preserve earlier records. Link the history entry to any decision record it creates or follows. Record `None` when no decision record is needed.

## Report Format

# Repository Consistency Review: `<review date>`

## Findings

List findings from highest to lowest severity. Include evidence, impact, recommendation, and validation for each finding.

## Suggestions

List improvements that are not confirmed policy violations.

## Open Questions

List decisions that require repository-owner input.

## Validation Performed

List the searches, scripts, tests, or checks actually run. State clearly when no executable validator exists.
