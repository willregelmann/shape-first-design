# AGENTS.md

This repository is Shape-First Design: a Claude Code plugin with two skills, `map-project` and `develop-project`, under `skills/`. The skills are markdown with YAML front matter. There is no build system and there are no dependencies.

- Edit shared rules and templates only in `skills/shared/`, then run `python3 checks/sync_shared.py` to write them into each skill. Never edit the generated block at the end of a `SKILL.md`.
- Run `python3 checks/check_map.py` before committing. The judged scenarios in `evals/` cost model calls; run them when a skill's behaviour changes (see README.md).

## The Map

This project has a map in `docs/`: what it's for, what it's made of and what must always hold, with decision records for why. Read `docs/README.md` before changing code, and work with the `develop-project` skill.
