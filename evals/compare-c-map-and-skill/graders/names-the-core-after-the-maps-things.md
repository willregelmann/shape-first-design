---
type: regex
pattern: "(?=[\\s\\S]*^class\\s+Chore\\b)(?=[\\s\\S]*^class\\s+Household\\b)"
flags: m
match: contains
target:
  source: file
  path: src/chores.py
---
