---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if the rules about a chore (whose turn it is, passing the turn, when it is next due, its history) are kept inside the chore itself, and the rules about the household (who leaves, who may take turns) inside the household, so a caller can't skip them. Fail if those rules are held in separate helper functions, services or managers that callers must remember to use, leaving the chore or household as bare data.
