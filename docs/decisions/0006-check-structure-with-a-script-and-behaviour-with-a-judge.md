# Check the map's structure with a script, and the skills' behaviour with judged scenarios

## Context and Problem Statement

[Audit](../capabilities/AUDIT.md) requires every invariant to have a check that has been seen to fail. In this repository the "code" is skill text. Some invariants are about structure (the copies match their templates, links resolve, records are never edited) and some are about what an agent does with the skills (it drafts before asking, it stops at the map, it routes a model change back through the map). How are both checked, without breaking the promise of no build system and no dependencies?

## Considered Options

Structure:

* A test suite with a test framework
* A standard-library Python script, one check per invariant

Behaviour:

* Reading the skill text and judging it by hand
* Judged scenarios run with `claude plugin eval`, several runs each, failing below a pass-rate threshold

## Decision Outcome

Chosen options: "A standard-library Python script, one check per invariant" and "Judged scenarios run with `claude plugin eval`".

* `checks/check_map.py` names each check after its invariant and the map file it comes from, and exits non-zero when any fails. Each check was broken once on purpose to watch it fail.
* `evals/` holds scenarios: a prompt, sometimes a fixture project, and graders that are either exact (a tool was or wasn't used, a file exists) or a judge reading the reply, the files or the trace.

### Consequences

* Good, because the structural checks are free and fast, and need nothing installed.
* Good, because behaviour is checked the way the method says it should be: real runs, a judge, a pass rate.
* Bad, because scenarios cost model calls and a judge can be noisy, so they run when a skill's behaviour changes, not on every commit.

### Confirmation

`checks/check_map.py` exits 0. The scenarios pass at the threshold in README.md.

## More Information

Written on 2026-10-14. The test framework option was weighed and left out to keep the repository free of dependencies.
