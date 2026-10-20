---
type: regex
pattern: "\\b(task|todo|job|family|member|resident|flatmate|roommate|user)s?\\b"
flags: i
match: not_contains
target:
  source: file
  path: src/chores.py
---
