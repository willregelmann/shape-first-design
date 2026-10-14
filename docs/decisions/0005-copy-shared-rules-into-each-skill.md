# Shared rules have one source, carried inline by each skill and checked

## Context and Problem Statement

Both skills rely on the same rules: the words, what counts as an invariant, how decisions are kept, the writing style, and the templates copied into every project. [Skills](../interfaces/SKILLS.md) requires those to have one source that neither skill restates. How do both skills reach one source of rules?

## Decision Drivers

* A rule both skills rely on has one source.
* An agent gets the rules whenever it loads a skill, whatever it's allowed to read.
* Nothing keeps two copies in step by hand.

## Considered Options

* Link from each skill to `skills/shared/`
* Copy `skills/shared/` into a folder inside each skill
* Keep `skills/shared/` as the source, write it into each `SKILL.md` between marker comments, and fail the checks when a skill's copy differs

## Decision Outcome

Chosen option: "Keep `skills/shared/` as the source, write it into each `SKILL.md`", because both other options failed in judged runs: the agent was refused permission to read `skills/shared/RULES.md` beside the skill, and then refused the same file inside the skill's own folder. Text in `SKILL.md` arrives with the skill itself.

* Shared rules and templates are edited only in `skills/shared/`.
* `checks/sync_shared.py` writes them into each `SKILL.md`, between marker comments.
* `checks/check_map.py` fails while any skill's copy differs from the source.

### Consequences

* Good, because each skill is complete on its own, whichever way it's installed and whatever an agent may read.
* Bad, because each `SKILL.md` is longer, and every shared change shows up three times in a diff.

### Confirmation

`each_skill_carries_the_shared_rules_unchanged` and `shared_rules_have_one_source` in `checks/check_map.py`.

## More Information

Written on 2026-10-14.
