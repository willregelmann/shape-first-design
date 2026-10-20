---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. Pass if, in this code, exactly one person has the turn for a chore at any moment, and marking a chore done passes the turn to the next person in order, wrapping round after the last. Fail if the turn can belong to nobody or to two people for a chore that has people, or if it doesn't pass in order.
