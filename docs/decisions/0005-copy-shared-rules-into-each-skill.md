# Shared rules have one source, copied into each skill and checked

## Context and Problem Statement

Both skills rely on the same rules: the words, what counts as an invariant, how decisions are kept, and the writing style. [Skills](../interfaces/SKILLS.md) requires those to have one source that neither skill restates. The first version kept them in `skills/shared/` and linked to it from each skill. In the first judged run, the agent was refused permission to read `skills/shared/RULES.md`: it could load the skill, but not a file beside it. How do both skills reach one source of rules?

## Decision Drivers

* A rule both skills rely on has one source.
* An agent can read the rules wherever it's allowed to read the skill it loaded.
* Nothing keeps two copies in step by hand.

## Considered Options

* Link from each skill to `skills/shared/`
* Keep `skills/shared/` as the source, copy it into each skill, and fail the checks when a copy differs

## Decision Outcome

Chosen option: "Keep `skills/shared/` as the source, copy it into each skill, and fail the checks when a copy differs", because the link was refused in a real run, and a checked copy keeps one source without relying on what an agent may read outside the skill.

* Shared rules and templates are edited only in `skills/shared/`.
* `checks/sync_shared.py` copies them into each skill's own `shared/` folder.
* `checks/check_map.py` fails while any copy differs from the source.

### Consequences

* Good, because each skill is self-contained, whichever way it's installed.
* Bad, because every shared change touches three places in a diff, and someone has to run the sync.

### Confirmation

`each_skill_carries_an_exact_copy_of_the_shared_rules` and `shared_rules_have_one_source` in `checks/check_map.py`.

## More Information

Written on 2026-10-14.
