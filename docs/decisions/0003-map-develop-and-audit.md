# Three capabilities: map, develop and audit

## Context and Problem Statement

Most of the method's behaviour lives in its primitives. What it does that no one primitive does is find a project's shape, build by it, and show whether the code still keeps it. Which processes are capabilities, and what are they called?

## Considered Options

The set:

* Discover, develop and audit, with backfilling records as a fourth
* Map, develop and check, with backfilling folded into Decision, walking folded into mapping, and a whole-project audit as checking run across everything

The name for showing the code keeps the map:

* Check
* Audit

## Decision Outcome

Chosen options: "Map, develop and check, with backfilling folded into Decision", named "Audit", chosen by the user.

* [Map](../capabilities/MAP.md) finds a project's shape with its owner, for a new project or an existing one.
* [Develop](../capabilities/DEVELOP.md) builds by the map and audits every change against the invariants it touches.
* [Audit](../capabilities/AUDIT.md) covers both one change and a whole project.

### Consequences

* Good, because each capability spans primitives, and none restates a primitive's own rules.
* Good, because one capability covers checking a change and auditing a project, so both use the same verdicts.
* Bad, because "audit" suggests a whole-project review, while most audits are of a single change.
* TODO: record the reason for preferring "Audit" to "Check".

### Confirmation

Each of the three spans primitives, as [Capability](../primitives/CAPABILITY.md) requires, and [Skills](../interfaces/SKILLS.md) starts all three.

## More Information

Written on 2026-10-14.
