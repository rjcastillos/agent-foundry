In agentic AI development and GitHub Copilot workflows, establishing a standard configuration layout is critical so that LLMs, autonomous coding agents, and extension engines automatically discover your codebase rules. [1] 
------------------------------
## Standard Location of repository-conventions.md
By modern convention, a standalone file named repository-conventions.md does not have an officially hardcoded, native auto-discovery pathway in GitHub Copilot. Instead, it serves as a modular "source of truth" document. [2, 3] 
To make GitHub Copilot natively parse these conventions, the standard location is inside the repository root at:

* 
* 📂 .github/copilot-instructions.md (or alternatively, standardizing globally as an ecosystem-wide AGENTS.md file at the absolute root of the repository). [4, 5, 6, 7] 
* 

## The Best-Practice Strategy
Instead of leaving repository-conventions.md floating around, teams typically handle it in one of two ways:

   1. The Direct Method: Merge your conventions directly into .github/copilot-instructions.md.
   2. The Symlink/Reference Method: Keep repository-conventions.md in the root (or under a documentation folder) and create a symlink from .github/copilot-instructions.md to it, or use Copilot's path-specific rules to include it. [2, 5] 

------------------------------
## Most Common "Wiring" Places
To wire up, reference, or inject your repository-conventions.md file into agentic and Copilot frameworks, developers use these standard structural configuration entry points:

| Wiring Mechanism / Location | Purpose & Target Tool | Behavior |
|---|---|---|
| .github/copilot-instructions.md | GitHub Copilot (Chat, Agents, Inline) | Global Project Rules: Copilot auto-discovers this file and appends it to its system context window for every request in the workspace. You can copy-paste your conventions here. |
| AGENTS.md (at repository root) | Ecosystem Agents (Copilot CLI, Cursor, Claude Code, Aider) | Cross-Tool Standard: An open-format "README for agents" managed by the Agentic AI Foundation. Perfect for wiring tool execution paths, architecture breakdowns, and tech stacks. |
| .github/instructions/*.instructions.md | Path & Language-Specific Wiring | Scoped Context: You can isolate parts of your conventions (e.g., frontend-only rules) by wiring them to specific file types using Frontmatter matching (e.g., applyTo: "**/*.ts" ). |
| .github/agents/*.agent.md | Custom Specialized Sub-Agents | Role-Based Wiring: If you build dedicated sub-agents (e.g., a review-agent), you wire your conventions into the prompt body of these files so they audit code against your strict rules. |
| .github/prompts/*.prompt.md | Reusable Chat Macros | Slash Commands: Lets you wire a custom forward-slash macro (like /audit-conventions) inside the chat panel to instantly run a validation prompt against your markdown files. |

## Monorepo Considerations 💡
If you are developing inside a large Monorepo, relying entirely on a single global file breaks granularity. In these environments, agents use a "nearest file wins" hierarchy: [8, 9, 10] 

* 
* Place a high-level AGENTS.md at the root for global settings.
* Wire folder-specific conventions by dropping nested AGENTS.md or scoped .instructions.md files directly inside sub-packages (e.g., /packages/backend/AGENTS.md). [8, 10] 
* 

Would you like me to help you write the Frontmatter configurations for path-scoped instructions, or do you want a scaffold template for a project-wide .github/copilot-instructions.md file?

[1] [https://github.com](https://github.com/github/gh-stack/issues/132)
[2] [https://github.com](https://github.com/fork-the-planet/github___awesome-copilot/blob/main/agents/repo-architect.agent.md)
[3] [https://www.deployhq.com](https://www.deployhq.com/blog/ai-coding-config-files-guide)
[4] [https://docs.github.com](https://docs.github.com/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
[5] [https://fast.io](https://fast.io/resources/configure-github-codespaces-copilot-agent-mode/)
[6] [https://awesome-copilot.github.com](https://awesome-copilot.github.com/skill/create-agentsmd/)
[7] [https://devblogs.microsoft.com](https://devblogs.microsoft.com/ise/ai-assisted-development-agents-skills-copilot-cli/)
[8] https://agents.md
[9] [https://www.iamraghuveer.com](https://www.iamraghuveer.com/posts/copilot-monorepo-workspace-context/)
[10] [https://qaskills.sh](https://qaskills.sh/blog/copilot-coding-agent-setup-testing-repos)
