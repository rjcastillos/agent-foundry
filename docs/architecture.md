# Architecture

## Design

Agent Foundry separates reusable source assets from the documentation and tooling used to maintain them.

```text
canonical assets -> documentation and validation -> copied or exported assets
```

Canonical assets live in visible top-level categories:

- `agents/` contains role-oriented agents and their supporting prompts or assets.
- `skills/` contains focused capabilities that agents or users can invoke.
- `prompts/` contains reusable prompt definitions.
- `workflows/` contains repeatable multi-step processes.
- `mcp/` contains Model Context Protocol integrations and configuration guidance.
- `templates/` contains starting structures for new assets.
- `examples/` contains complete demonstrations.
- `knowledge/` contains reference material and durable engineering guidance.

`docs/` defines the contracts shared by these categories. `tools/` contains validation, discovery, and future export or installation utilities.

## Source and destination paths

The catalog is the source of truth and keeps its directories visible for discoverability and review.

### Decision: keep canonical directories visible

Canonical asset directories such as `agents/`, `skills/`, `prompts/`, and `workflows/` remain visible rather than being renamed to hidden directories such as `.agents/`.

This decision is justified because visible directories:

- make the catalog easier to browse, search, document, and review in source control;
- preserve a clear distinction between reusable source assets and repository-specific configuration;
- avoid coupling the catalog's structure to one AI tool's discovery convention; and
- allow the same asset to be exported to different consuming repositories without duplicating the catalog.

The tradeoff is that consumers may need a copy or export step. That is intentional: a consuming repository may project an asset into a hidden or tool-specific path, such as `.agents/`, `.github/`, or `.vscode/`, when required by its tooling. Export logic should preserve the asset contents and record the source version rather than requiring the catalog to mirror every destination convention.

## Asset lifecycle

Assets should move from `draft` to `experimental` to `stable` as documentation, examples, compatibility information, and validation improve. Deprecated assets remain available long enough for consumers to migrate, then may be removed according to the repository's versioning policy.
