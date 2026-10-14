---
type: regex
pattern: "^class\\s+(?!Chore\\b|Household\\b)\\w+"
flags: m
match: not_contains
target:
  source: file
  path: src/chores.py
---
