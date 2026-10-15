---
type: regex
pattern: "^class\\s+\\w+Chore\\b"
flags: m
match: not_contains
target:
  source: file
  path: src/chores.py
---
