---
name: compare-c-map-and-skill
tags: [compare]
plugins: ["../.."]
max_turns: 40
runs: 5
timeout_seconds: 1200
---
Build the chores tool described in this repository, in Python with only the standard library. Put the core in `src/chores.py`, the command line in `src/cli.py` and the tests in `tests/`. It should support chores that repeat on a schedule and chores that happen once, turns that rotate in order, people leaving the household, and reminders when a chore is due. Read the repository's documentation before you start.
