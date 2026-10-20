---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if, when a person leaves the household, they are taken out of every chore's turns, and each chore they had the turn for passes to the next person, without skipping anyone or leaving a stale turn. Fail if leaving is unsupported, if the person stays in any chore, or if the turn goes wrong.
