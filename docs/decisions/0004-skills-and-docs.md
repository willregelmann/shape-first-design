# Two interfaces: the skills agents load, and the docs where the map is read

## Context and Problem Statement

The method touches the outside in three ways: an agent loads its skills, the map it writes lands in a project's files, and it's installed, as a Claude Code plugin or by linking the skills into an agent's skills folder. Which of these are interfaces, and what are they called?

## Considered Options

* Skills, Docs and Plugin
* Skills and Docs, with how the skills are installed as a column of Skills

The name for where the map is read:

* Docs
* Map, which is now the name of a capability

## Decision Outcome

Chosen options: "Skills and Docs, with how the skills are installed as a column of Skills", named "Docs", agreed with the user.

* [Skills](../interfaces/SKILLS.md) is where an agent picks up the method, and starts every capability.
* [Docs](../interfaces/DOCS.md) is where every capability shows its result.
* Installing as a plugin and linking into a skills folder are two ways of serving one surface, which is the method's own rule for interfaces ([Interface](../primitives/INTERFACE.md)).

### Consequences

* Good, because every capability is started through Skills and observed through Docs.
* Bad, because "Docs" undersells that the folder is the project's north star, not just its documentation.

### Confirmation

[Interface](../primitives/INTERFACE.md)'s rule that one surface served differently by different hosts is one interface.

## More Information

Written on 2026-10-14.
