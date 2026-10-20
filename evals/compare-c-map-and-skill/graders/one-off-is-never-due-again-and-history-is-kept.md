---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if the code supports a chore that happens once, and once such a chore is done it is never due again and never reminded again, while the record of who did it and when is kept. Fail if one-off chores aren't supported, if a done one-off chore can come due again, or if its history is lost.
