# Shape-First Design

Agent skills for building software shape first: find what a project is made of, then keep the code to it.

Whenever an agent is about to build or change a project, Shape-First Design answers one question: **what shape should this have, and does it still have it?**

A project's shape is the model a person holds of it: the few things it's made of, each with one idea behind it. Good code and an intuitive model go together. Code someone can explain with a few things is easy to change, and code that's hard to explain is usually built on the wrong things. Capable models write excellent functions and still lose the model: a new type for a case an existing thing already covers, three names for one idea, a rule checked in one caller and forgotten in the next. Each change is reasonable on its own, and the code drifts away from anything a person could hold in mind. The reasons behind a shape vanish too, so the next agent undoes a decision it never knew was made.

So Shape-First Design finds the few things a project is made of with the person who has the idea, for a project that doesn't exist yet or one that already does, and writes what must always hold about them as a map anyone can read without the code. The core of the code takes those things' names and boundaries, so the map and the code are one model. Every change is placed against the map before it's written, every promise it touches gets a check that can fail, and every choice someone could later want to undo is recorded with what was turned down. When the code fights the map, the map is suspected first, and when the project changes what it is, the map changes first.

If someone who has read only the map can't predict what the code does or where it does it, or agents invent a new kind of thing where one the map already names was the right fit, Shape-First Design has failed at the one thing it exists to do.
