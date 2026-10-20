---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if a chore that nobody shares has no turn, and the code is safe with it: it doesn't crash and doesn't hand the turn to anybody. Fail if it crashes, divides by zero, or invents a person.
