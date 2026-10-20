---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if, when a repeating chore is done, its next due date is worked out from when it was due plus its interval, not from the day it was done: a weekly chore due on 5 January and done on 6 January is next due on 12 January. Fail if it is worked out from the day it was done.
