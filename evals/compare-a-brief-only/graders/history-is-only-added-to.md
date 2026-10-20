---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if each chore keeps a history of who did it and when, that is only ever appended to, and nothing in the code removes or rewrites entries, including when someone leaves the household. Fail if there is no history, or if any code deletes or edits entries.
