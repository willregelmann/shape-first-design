---
type: regex
pattern: "^class\\s+(?!Chore\\b)(?!\\w+Error\\b)\\w*Chore\\w*|^class\\s+\\w+\\(\\s*Chore\\s*\\)"
flags: m
match: not_contains
target:
  source: file
  path: src/chores.py
---
