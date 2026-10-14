---
type: regex
pattern: "one.?off|\\bonce\\b|every_days\\s*:\\s*(int\\s*\\|\\s*None|Optional)"
flags: i
match: contains
target:
  source: file
  path: src/chores.py
---
