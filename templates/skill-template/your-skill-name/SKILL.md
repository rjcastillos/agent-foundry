---
name: your-skill-name
description: Explicit summary of what this skill executes. MUST contain a "Use when..." clause detailing exact triggers to tell the engine when to activate it.
version: "1.0.0"
compatibility: "requires Node.js v22+ or Python 3.11+"
metadata:
  author: "Your Team / Organization"
  category: "Refactoring | Security | DevOps | Testing"
---

# Skill Playbook: [Human Readable Skill Name]

> [!NOTE]
> This skill provides specialized automation for [Core Purpose]. When active, prioritize the instructions, decision rules, and negative guardrails outlined below.

---

## 1. Trigger Scenarios (When to Run)
The agent must load and evaluate this skill when the user explicitly or implicitly requests:
* [Trigger keyword or phrase 1] (e.g., "Run a security audit on this module")
* [Trigger keyword or phrase 2] (e.g., "Generate a database schema migration")
* [Trigger keyword or phrase 3] (e.g., "Verify compliance with API standards")

---

## 2. Structural Overview & Mental Map
Before modifying code or performing tasks, orient your execution path against the following structural layout:
* **Core Artifacts:** [e.g., `/src/models/`, `package.json`]
* **Key Configurations:** [e.g., `tsconfig.json`, `.env.example`]
* **Primary Entrypoint:** [e.g., `/src/index.ts`]

---

## 3. Step-by-Step Workflow
Execute your task strictly in the following sequential order:

1. **Discovery:** Scan the active target file(s) and list all dependencies.
2. **Analysis:** Evaluate code patterns against standard rules found in `references/STANDARDS.md`.
3. **Drafting:** Implement the localized adjustments. If multiple files are affected, generate changes file-by-file.
4. **Validation:** Check the code by running the local companion script: `scripts/validate.sh`.
5. **Report:** Output the result following the established structural layout contract.

---

## 4. Decision Rules (If / Then Logic)
* **IF** the target code handles authentication or cryptography, **THEN** do not modify it; flag it for manual developer review instead.
* **IF** the payload is missing required schema properties, **THEN** halt execution and prompt the user for the missing fields.
* **IF** performance thresholds are violated, **THEN** apply code memoization hooks.

---

## 5. Negative Guardrails (What NEVER to do)
* **Do Not Bypass Types:** Never introduce structural fallbacks like `any` or cast types via `as unknown`.
* **Do Not Mask Errors:** Never implement blank catch blocks (`catch (e) {}`). All failures must trigger explicit logging.
* **Do Not Add Dependencies:** Do not introduce external libraries or packages to solve local execution bugs.

---

## 6. Target Output Structure & Examples
Always map outputs to this pattern-matched structure:

### Expected Code block Layout
```[language]
// [Short architectural header explaining the change]
export const processPayload = (input: ContextType): OutputType => {
  // Your implementation here
};
```

### Example Input / Output Mapping
* **User Request:** *"Refactor user service endpoints"*
* **Expected Output Behavior:** *"Apply functional array maps, wrap async queries in try/catch, and append standard unit testing stubs."*
