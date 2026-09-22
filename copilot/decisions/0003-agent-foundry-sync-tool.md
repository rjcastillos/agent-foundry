## Prompt History: Agent Foundry Repository Synchronization Tool

- Date: 2026-09-22
- Asset: tools/repo-sync/sync_repo.py
- Change: Added a repository overlay synchronization utility that updates agent-foundry from agent-foundry while preserving target-only content. Implemented automatic replacement of repository references from "agent-foundry" to "agent-foundry" with case-preserving transformations.
- Justification: Enable controlled propagation of reusable assets from agent-foundry into agent-foundry without deleting target-specific files, experiments, or local customizations.
- Affected files or areas:
  - tools/repo-sync/
  - tools/repo-sync/sync_repo.py
  - tools/repo-sync/README.md
- Compatibility Notes:
  - Uses only Python standard library modules.
  - Performs overlay synchronization only.
  - Does not remove files or directories from TARGET.
  - Excludes Git metadata and common cache directories.
  - Applies repository-name transformation only to detected text files.

  ### Real prompt used
```
I need a python script to update a GitHub repository with the new content in another one:
1)Please create the script with a readme file.
2)Do simple code at a senior level but with simple python 
3)Document the main script blocks internally and in the readme.
4)The directories are :
4.1) SOURCE="/home/a233c1f/agent-foundry"
4.2) TARGET="/home/a233c1f/agent-foundry"
5)The process is to diff both directories and update TARGET to match SOURCE content.
5.1) The CAVEAT here is that any reference on the source of the repo name "agent-foundry" needs to be replaced in TARGET with "agent-foundry" respeting the letter case .
6)Covert this promt into a memory folowing :
6.1) /home/a233c1f/agent-foundry/copilot/prompt-history/0001-copilot-memory-structure.md (attached)
6.2) create the memory of this prompt 
6.3 attached an example of memory "0001-copilot-memory-structure.md"

After the initial result
========================

One clarification: files or Directories exist in TARGET these should be kept intact 

as of 2026-09-22
The script location is :
    /home/a233c1f/agent-foundry/tools/scripts/sync_repo/sync_repo.py

