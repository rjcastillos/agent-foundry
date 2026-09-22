# (Repo name) Instructions

## Repository Purpose

text

## Core Rules

- Treat the visible root-level directories as the canonical source layout for this repository.
- Keep reusable assets technology-agnostic unless the asset explicitly targets a technology.
- Inspect the target directory and neighboring examples before adding or changing an asset.
- Follow the naming, file-layout, metadata, and Markdown conventions in `docs/repository-conventions.md`.
- Keep changes focused; do not reorganize the repository or introduce new top-level directories without documenting the convention.
- Prefer existing templates and patterns over introducing a new format.
- Do not add generated outputs, dependency directories, caches, secrets, or local environment files to version control.
- Preserve user changes and avoid unrelated formatting or content changes.

# General Coding Instructions

- Very important: Use internal program documentation to make the code more human readable and understandable.


## Source and Generated Projects

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

## Documentation and Memory

- Record durable repository decisions in `copilot/decisions/`.
- Record substantial prompt, agent, or skill changes in `copilot/prompt-history/`.
- For generated projects, use the corresponding `.github/copilot/` directories.
- Update the relevant README or convention document when changing repository structure, reusable asset formats, supported technologies, or user-facing workflows.
- Use repository-relative paths in documentation; do not document machine-specific paths.

## Validation

Before completing a change:

1. Check the changed Markdown for valid structure and consistent paths.
2. Run the narrowest relevant test or script validation available.
3. Review the final diff for unrelated changes and accidental generated files.









Engineering







Enterprise software








News & insights








Open Source






Security






Home / AI & ML / GitHub Copilot
5 tips for writing better custom instructions for Copilot
This guide offers five essential tips for writing effective GitHub Copilot custom instructions, covering project overview, tech stack, coding guidelines, structure, and resources, to help developers get better code suggestions.


Christopher Harrison·@geektrainer
September 3, 2025
|
Updated June 14, 2026
|
7 minutes
Share:
If you’ve read any of my stuff or listened to one of my presentations before, you’ve likely heard my snarky joke: “Don’t be passive aggressive with Copilot.” 

My point with this joke is serious, though. Copilot works best when you give it the right context. Just like a new teammate, it can’t read your mind (even if it sometimes feels like it can).

Copilot can likely figure out what you’re doing and how you’re doing it. But spelling out the essentials – what you’re building, the stack you’re using, the rules to follow, etc., will help avoid confusion and mistakes.

This is why instructions files are so important. They’re your chance to give Copilot that background, that institutional knowledge the rest of your team has from their experience with the project.

The centerpiece for Copilot is copilot-instructions.md, the file which is read on every Copilot chat or agent request.

So how should one be crafted?

To help you avoid the blank-page problem, here are five things every instruction file should include (plus a bonus tip on how Copilot can even help you write the file itself).

Before we get started
One important tip I want to share before we get into more details is to not overthink things. There isn’t a specific prescribed way to write instructions files. The nature of generative AI is probabilistic, meaning the same requests can actually render different results. Your goal is to tilt the scales, to help point Copilot to finding the answer you’re hoping for as often as possible.

The five sections (and bonus tip) below aren’t meant as requirements, but recommendations. In my experience, having these sections, or at the very least the key information indicated by these sections, in your instructions file will vastly increase the quality of suggestions from Copilot.

You should use these as a starting point, and experiment and explore based on your projects, models, and experience with Copilot.

Give GitHub Copilot a project overview
It’s tough to write code for an app if you don’t know what the app is! The same thing is true for GitHub Copilot, and that’s where a project overview instructions file can be exceptionally helpful. 

The header for your instructions file should be the elevator pitch for your app. What’s the app? Who’s the audience? What are the key features? It doesn’t need to be long, just a few sentences to set the stage.

Here’s an example of a project overview for an instructions file:


## Tech stack in use

### Backend

- Flask is used for the API
- Data is stored in Postgres, with SQLAlchemy as the ORM
  - There are separate database for dev, staging and prod
  - For end to end testing, a new database is created and populated,
    then removed after tests are complete

### Frontend

- Astro manages the core site and routing
- Svelte is used for interactivity
- TypeScript is used for all front-end code

### Testing

- Unittest for Python
- Vitest for TypeScript
- Playwright for e2e tests

## Resources

- scripts folder
  - start-app.sh : Installs all libraries and starts the app
  - setup-env.sh : Installs all libraries
  - test-project.sh : Installs all libraries, runs unit and e2e tests
- MCP servers
  - Playwright: Used for generating Playwright tests or interacting with site
  - GitHub: Used to interact with repository and backlog
