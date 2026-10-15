# A project's shape is the model a person holds of it

## Context and Problem Statement

[0001](0001-ask-what-shape-a-project-should-have.md) chose the question "what shape should this have, and does it still have it?" without a recorded reason, and noted that "shape" is soft until someone reads what the map means by it. The intent framed the method around drift and lost reasons, and never said why a map of a few things should make code better. What does "shape" mean, and what is the method's case for it?

## Considered Options

* Keep the question, and define shape in the intent as the model a person holds of a project
* Put the model in the question: "what is this made of, in words a person can hold, and does the code still say so?"
* A promise instead of a question: "anyone who has read the map can predict the code"

## Decision Outcome

Chosen option: "Keep the question, and define shape in the intent as the model a person holds of a project", chosen by the user, who holds that good code and intuitive mental models are strongly correlated, and wants the project centred on that idea.

* [INTENT.md](../INTENT.md) defines shape as the few things a project is made of, each with one idea behind it, and says the map and the code are one model.
* Its failure sentence becomes observable as a prediction: someone who has read only the map can predict what the code does and where.
* [Develop](../capabilities/DEVELOP.md) treats code that fights the map as evidence about the map, since the correlation runs both ways.

This supersedes 0001, and gives the reason 0001 left out.

### Consequences

* Good, because "shape" now means something a person can test: read the map, predict the code, and see.
* Good, because it keeps the word the method is named after.
* Bad, because "model" now has one meaning in the map, so the skills can no longer use it loosely for "the map".

### Confirmation

[INTENT.md](../INTENT.md) defines shape and states the prediction in its failure sentence. The `develop-builds-the-core-the-map-names` scenario checks that two builds from the same map give the core a reader of the map would predict.

## Pros and Cons of the Options

### Put the model in the question

* Good, because the question says what shape means without a definition beside it.
* Bad, because it reopens the option 0001 turned down, and drops the method's own word.

### A promise instead of a question

* Good, because it's the shortest and the easiest to test.
* Bad, because it says nothing about finding the model in the first place.

## More Information

Written on 2026-10-14.
