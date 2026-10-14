# Shape-First Design

Agent skills for building software shape first: find what a project is made of, then keep the code to it.

Whenever an agent is about to build or change a project, Shape-First Design answers one question: **what shape should this have, and does it still have it?**

Working code is only half the job. Capable models write excellent functions and still produce structure nobody chose: a new type for a case an existing abstraction already covers, three names for one idea, a rule checked in one caller and forgotten in the next. Each change is reasonable on its own, and the shape drifts anyway. The reasons behind a shape vanish too, so the next agent undoes a decision it never knew was made. And nobody can see what's being built without reading all of the code.

So Shape-First Design starts by finding the few things a project is made of, chosen so its behaviour follows from them, and writing what must always hold about them as a map. It works with the person who has the idea, for a project that doesn't exist yet or one that already does. The map is a north star for every agent that touches the project, and a description any person can read to understand what's being built without reading the code. Every later change is placed against the map before it's written, every promise it touches gets a check that can fail, and every choice someone could later want to undo is recorded with what was turned down. When the project changes what it is, the map changes first.

If agents working from the map write code that doesn't mean what the map says, or invent a new kind of thing where one the map already names was the right fit, Shape-First Design has failed at the one thing it exists to do.
