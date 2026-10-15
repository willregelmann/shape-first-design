# An intent names one focus, a question or a promise, and isn't held to a fixed layout

## Context and Problem Statement

`map-project` drafted every [intent](../primitives/INTENT.md) from one template, line by line, and every intent had to name a question. Some projects don't fall into a question naturally: the owner struggled to phrase the intent of a test framework as one. What must every intent have, and how much of its wording should the skill fix?

## Considered Options

* Keep the template, and require a question in every intent
* Require what the intent must say: what the project is, one focus in one sentence (a question it keeps answering or a promise it keeps), the problem, the response and a failure sentence; offer the template as one shape that often works

## Decision Outcome

Chosen option: "Require what the intent must say", because the owner asked for the skill to be "a little less opinionated about line-level specifics" after struggling to phrase an intent as a question.

### Consequences

* Good, because a project that keeps a promise rather than answering a question no longer has its pitch forced into a question.
* Good, because the test for a sharp idea stays: the focus fits in one sentence, and the failure sentence names something someone could observe.
* Bad, because intents across projects no longer read alike line by line.

### Confirmation

[INTENT.md](../primitives/INTENT.md) requires one focus in one sentence and a failure sentence that names an observable outcome. The `map-drafts-before-asking` scenario accepts a draft pitch with either a question or a promise.

## More Information

Written on 2026-10-14.
