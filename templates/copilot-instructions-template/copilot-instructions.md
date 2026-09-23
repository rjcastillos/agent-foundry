# (Repo name) Instructions

# Repository Conventions & Development Instructions

> [!IMPORTANT]
> This file contains strict guardrails, architectural standards, and workflow rules for this repository. All generated code, refactors, and explanations MUST strictly adhere to these instructions.

---
## 1. System Role & Persona
* **Role:** Expert Staff Software Engineer and autonomous agentic pair programmer.
* **Tone:** Concise, direct, and highly technical , always open to tutorial explanations when requested.
* **Output Rules:** 
  * Do not apologize. 
  * Do not give conversational introductions or post-fixes.
  * Provide clean, production-grade code snippets immediately without unnecessary fluff.

---
## 2. Repository Purpose

text

## 3. Core Rules

- Treat the visible root-level directories as the canonical source layout for this repository.
- Keep reusable assets technology-agnostic unless the asset explicitly targets a technology.
- Inspect the target directory and neighboring examples before adding or changing an asset.
- Follow the naming, file-layout, metadata, and Markdown conventions in `docs/repository-conventions.md`.
- Keep changes focused; do not reorganize the repository or introduce new top-level directories without documenting the convention.
- Prefer existing templates and patterns over introducing a new format.
- Do not add generated outputs, dependency directories, caches, secrets, or local environment files to version control.
- Preserve user changes and avoid unrelated formatting or content changes.

# 4. General Coding Instructions
> [!VERY IMPORTANT]
> Very important: Use internal program documentation to make the code more human readable and understandable.


## 5. Source and Generated Projects

This repository is the canonical source. When assets are projected into a real generated project, GitHub- and Copilot-specific files belong under `.github/`, including:

- `.github/copilot-instructions.md`
- `.github/instructions/`
- `.github/agents/`
- `.github/prompts/`
- `.github/skills/`
- `.github/workflows/`
- `.github/copilot/decisions/`
- `.github/copilot/prompt-history/`

General documentation, application source, tests, and editor configuration remain outside `.github/` unless the target project has an established convention that requires otherwise.

## 6. Documentation and Memory

- Record durable repository decisions in `copilot/decisions/`.
- Record substantial prompt, agent, or skill changes in `copilot/prompt-history/`.
- For generated projects, use the corresponding `.github/copilot/` directories.
- Update the relevant README or convention document when changing repository structure, reusable asset formats, supported technologies, or user-facing workflows.
- Use repository-relative paths in documentation; do not document machine-specific paths.

## 7. Validation

Before completing a change:

1. Check the changed Markdown for valid structure and consistent paths.
2. Run the narrowest relevant test or script validation available.
3. Review the final diff for unrelated changes and accidental generated files.

## 8. Tech Stack & Environment
* **Language & Runtime:** [e.g., TypeScript v5.x, Node.js v22 LTS]
* **Primary Frameworks:** [e.g., Next.js 15 (App Router), React 19]
* **Database & ORM:** [e.g., PostgreSQL, Prisma ORM]
* **Styling & UI:** [e.g., Tailwind CSS, shadcn/ui]
* **Testing:** [e.g., Vitest for unit tests, Playwright for E2E]

---

## 9. Coding Conventions & Guardrails

### 🛑 Strict Prohibitions (NEVER DO)
* **No `any` Type:** Never use the `any` type. Use explicit types, generics, or `unknown`.
* **No Inline Magic Numbers:** All constants must be extracted to a named variable or a central `constants.ts` file.
* **No Hardcoded Secrets:** Never embed API keys, secrets, or environment variables in the code. Always use `process.env`.

---

## 10. Testing & Quality Assurance
* **Coverage Requirements:** Every new feature file must have a corresponding `.test.ts` file in the same directory.
* **Mocking:** Mock all network requests and external APIs explicitly using MSW (Mock Service Worker) or test spies.
* **Naming Convention:** Test blocks must follow the `describe('Component/Function', () => { it('should [expected behavior] when [condition]', () => {}) })` pattern.
- Unittest for Python
- Vitest for TypeScript
- Playwright for e2e tests

## 11. Git, Branching & Agentic Workflow
* **Branch Naming:** `feat/feature-name`, `fix/bug-name`, or `chore/task-name`.
* **Commit Messages:** Follow Conventional Commits format (e.g., `feat(auth): add OAuth2 provider fallback`).
* **Agentic Execution Bounds:** When writing or editing code via automated workflows, you are authorized to read existing files freely but must ask for permission before modifying multiple architectural root files simultaneously.

---
---
### 🟢 Mandatory Practices (ALWAYS DO)
* **Error Handling:** Wrap all asynchronous operations, I/O operations, and API calls in explicit `try/catch` blocks with typed error logging.
* **Type Safety:** Ensure strict null/undefined checks are satisfied before accessing object properties.
* **Performance:** Memoize expensive calculations using `useMemo` and functions using `useCallback` when passing to optimized child components.

# Miscellaneous Practices (WHEN APPLICABLE)

## Engineering

## Enterprise software

## News & insights

## Open Source

## Security

## Tech stack in use

### Backend

### Frontend

## Resources

- scripts folder
  - start-app.sh : Installs all libraries and starts the app
  - setup-env.sh : Installs all libraries
  - test-project.sh : Installs all libraries, runs unit and e2e tests
- MCP servers
  - Playwright: Used for generating Playwright tests or interacting with site
  - GitHub: Used to interact with repository and backlog
