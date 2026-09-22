---
name: md-to-docx
description: Convert Markdown files to professionally formatted Word (.docx) documents with embedded PNG images — pure JavaScript, no external tools required
---

# Markdown to Word (.docx) Skill

Convert Markdown (`.md`) files into professionally formatted Word (`.docx`) documents with embedded PNG images. Uses **pure JavaScript** via the `docx` and `marked` npm packages — no Pandoc, LibreOffice, or any native binary required.

## How to Convert

```bash
# Install dependencies from the scripts folder.
# Use npm install only when package-lock.json does not exist.
cd skills/md-to-docx/scripts && npm ci

# Convert from the workspace root and place generated files under output/.
cd ../../..
node skills/md-to-docx/scripts/md-to-docx.mjs <input.md> output/<output-name>.docx
```

If `package-lock.json` is absent for a new checkout, run `npm install` once from `skills/md-to-docx/scripts`, then commit the resulting lockfile. The `node_modules/` directory must not be committed.

Generated documents under `output/` are ignored by the repository. Keep a generated `.docx` elsewhere only when it is an intentional versioned deliverable.

For cleanup after local testing:

```bash
rm -rf skills/md-to-docx/scripts/node_modules
```

## Skill Folder Contents

| File | Purpose |
|------|---------|
| `SKILL.md` | This instruction file |
| `scripts/md-to-docx.mjs` | Node.js Markdown-to-Word converter |
| `scripts/package.json` | Dependencies (`docx`, `marked`) |
| `scripts/package-lock.json` | Reproducible dependency versions |

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Node.js** | 18+ | Required runtime |
| **`docx`** | 9+ | Pure JS Word document generator |
| **`marked`** | 15+ | Markdown parser |

No native binaries. No system-level installs. Works on Windows, macOS, and Linux.

## Features

The converter:

- **Extracts YAML front-matter** — uses `title`, `date`, `version`, `audience` for the title page
- **Generates a title page** — with project name, subtitle, date, version, and audience
- **Generates a table of contents** — built from H1-H3 headings
- **Embeds PNG images** — resolves `![alt](path)` references relative to the input `.md` file, reads the PNG, and embeds it inline in the Word document
- **Styled output** — Calibri font, colored headings (`#1F3864`), styled tables with alternating row colors, code blocks in Consolas
- **Handles all Markdown elements** — headings, paragraphs, tables, code blocks, lists, images, links, horizontal rules

## Image Embedding

The converter automatically embeds PNG images referenced in the Markdown:

```markdown
![High-Level Architecture](diagrams/high-level-architecture.drawio.png)
```

The image path is resolved **relative to the input Markdown file**. The PNG is read, dimensions are extracted from the PNG header, and the image is scaled to fit within 6 inches width while preserving aspect ratio.

If an image file is not found, a placeholder `[Image not found: <path>]` is inserted.

## Front-Matter Format

```yaml
---
title: Project Name — Project Summary
date: 2025-01-15
version: 1.0
audience: Engineering Team, Architects, Stakeholders
---
```

The title is split on `—` or `–` into main title and subtitle for the title page.

##Ramon memory:

#Before cleaning improvements 


```bash

cd /home/a233c1f/agent-foundry/skills/md-to-docx/scripts
npm install

cd /home/a233c1f/agent-foundry
node skills/md-to-docx/scripts/md-to-docx.mjs \
  README.md \
  copilot/AGEnt-fOundry-README.docx

```

#Recommended cleanup:

```bash
rm -rf skills/md-to-docx/scripts/node_modules
mkdir -p output
mv copilot/AGEnt-fOundry-README.docx output/
git status --short --ignored
```
#After cleaning improvements

```bash
cd skills/md-to-docx/scripts
npm ci
```

#Then generate outputs into output/:

```bash
cd /home/a233c1f/agent-foundry
node skills/md-to-docx/scripts/md-to-docx.mjs \
  README.md \
  output/AGEnt-fOundry-README.docx
```

