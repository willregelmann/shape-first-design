# Interface

A surface where the outside touches a project: the tools an agent calls, the hooks a host fires, the jobs that run when nobody is there, an API, the screens a person sees. Its file says who or what is on the other side, and a table names what crosses.

## Invariants

- **An interface is named for its surface, never its actor**, with the word a builder already uses for it: "Tools", not "Agent". "Hooks", not "Host".
- An actor with no surface of their own gets no interface. Their rules live where they belong, and on the surface that serves them as what it must always let them do.
- Something the project only calls out to, such as a model or a service it relies on, is not an interface. Its rules sit with the work that uses its answers.
- **One surface served differently by different hosts is one interface.** How each host serves it is a column in its table, and a behaviour that differs by host is a bug.
- Its table names what crosses and what each thing does. Exact inputs and outputs belong to a later contract.
- An interface is where naming an outside system belongs, because the project has to meet it.
- It changes in place, and carries no history and no rationale.
