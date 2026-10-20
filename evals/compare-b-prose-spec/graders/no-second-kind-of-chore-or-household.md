---
type: llm
focus:
  source: file
  path: src/chores.py
---
The file is a build of a household chores tool. The tool's model has two things: Chore (including one-off chores, its turn rotation and its history of who did it and when) and Household (the people who share chores). Pass if the file adds no class that duplicates or stands in for either of them: no second kind of chore, no class that holds a household's people and chores under another name, and no class for a person. Small immutable value records for history entries, reminders, delivery outcomes or schedules are fine, and so are persistence, serialization and exceptions, which the model leaves to the builder. Fail only if such a duplicate is present.
