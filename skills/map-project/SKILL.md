---
name: map-project
description: Maps a project's shape with its owner, by interviewing them and writing the map under docs/ (INTENT.md, then capabilities, primitives and interfaces, each a short file of statements that must always hold) — use when someone says "let's start a new project", "I want to build X", "map this out", "map this project", or "write the invariants", for a project that doesn't exist yet or one that already has code but no map, or when someone wants to add or change a primitive, capability or interface in an existing map. Stops at the map and does not plan or implement.
tags:
  - design
  - primitives
  - invariants
---

# Map Project

Find a project's shape with its owner and write it down as a map: `INTENT.md`, `primitives/`, `capabilities/` and `interfaces/` under `docs/`, saying what the project is for, what it's made of, what it does and where the outside touches it, as statements that must always hold.

Capable models write excellent code, but rarely beautiful structure. Structure comes from the abstractions: the few things a project is made of, chosen so that its behaviour follows from them and someone new can hold the whole of it in mind. Good code and an intuitive model go together, so finding that model is the design. The map's main job is to find those abstractions with the owner and fix them, so every build shares the same core.

The map must be **enough, on its own, for a capable agent to build a working project of the right shape**, and readable by anyone who wants to understand the project without reading its code. It fixes the core and leaves the rest open. Two builders given only the map should produce the same core, with the same names and the same boundaries, on whatever stack each one chose.

It's the north star for every agent that touches the project, for the project's whole life, not for one feature. This skill stops at the map. Choosing a stack, writing a plan and writing code belong to `develop-project`, and none of them happen here.

**Read [the shared rules](#shared-rules) first.** They're at the end of this file: the words, the map's layout and layers, what counts as an invariant, the writing style, and the templates. They come from one source shared by both skills.

## Quick Reference

| Step | Job | Output |
|------|-----|--------|
| 1 | Listen, and check the ground: new, existing code, or an existing map | A shared picture of the project |
| 2 | Intent | `docs/INTENT.md`, `docs/README.md` copied from the template, and a pointer to the map in `AGENTS.md` |
| 3 | Capabilities, from the owner's list | `docs/capabilities/<VERB>.md`, as drafts |
| 4 | Primitives, proposed from them | `docs/primitives/<NOUN>.md`, and the capability drafts revised |
| 5 | Interfaces | `docs/interfaces/<SURFACE>.md` |
| 6 | Walk the map | Gaps closed, behaviour with its primitive, links resolve, nothing built in |
| 7 | Hand off | A short summary, then stop |

Work one layer at a time, in this order. It starts at what the owner already has in mind, the pitch and what the project must do, and goes towards what only careful design shows. The deeper the layer, the more of it you propose and the less the owner has to compose. Each layer uses the words the one before it settled. Get the owner's agreement on a layer before starting the next, and on a proposed layer before writing its files. The owner's own list of capabilities needs no agreement before its drafts are written.

## Interviewing

The owner has the idea. You do the drafting. Interview where guidance is needed, and nowhere else.

- **Propose, don't quiz.** Put a concrete candidate in front of the owner and let them correct it. They should be able to confirm rather than compose.
- **Ask what only the owner knows:** who it's for, what it must work with, what's deliberately out or deferred, and which of two reasonable shapes they want.
- **Ask when two capable builders would choose differently and the owner would mind.** If they wouldn't mind, it's implementation. Leave it open and don't ask.
- **Every question carries your best answer as the default.** Use a structured-question tool when one is available, and a short numbered list when not.
- **Batch questions per layer.** One round is the aim.
- **Disagree out loud.** When the owner's framing has a gap or two of their ideas collide, say so with the specific case, and offer a way through.
- **A default is not a guess.** A default is something the owner sees and confirms. A guess is something written into the map that they never saw. If the owner doesn't answer, the statement stays out.
- **Unresolved is a legitimate outcome.** Leave the statement out and carry the question to the hand-off.

## Process

### 1. Listen

Let the owner describe what they want. Restate it in two or three sentences so they can correct the picture early.

Check the ground:

- **Nothing here yet?** Map the project from the conversation.
- **Code here, but no map?** Map it retroactively. See [Mapping an Existing Project](#mapping-an-existing-project) before Step 2.
- **A map already here** (`docs/INTENT.md` with `docs/primitives/` beside it)? Go to [Changing the Map](#changing-the-map).
- **A prototype or earlier attempt?** Read it for what turned out to matter, not for how it worked. Keep the consequence and drop the cause: "empty audio clips deadlock the player" becomes "silence is never ambiguous". A later build is expected to rediscover the details, and that is intended.

Don't research stacks, libraries or architectures. Research into the problem itself is fine when the owner asks for it.

### 2. Intent

Draft `docs/INTENT.md` from what the owner said, and ask only for what's missing. **Your first reply shows the whole draft pitch, with the questions after it**: fill every gap with a default in the draft rather than asking before drafting. It's an elevator pitch: about ten lines of prose with no sections, no lists and no mechanism. It says, in whatever order and words read best:

- **What the project is**, in a few words, and the one thing that sets it apart.
- **Why the obvious version is only half the job**, with concrete cases in everyday words.
- **How it answers those cases**, and the one idea it's built on. Behaviour in broad strokes, never mechanism.

One shape that often works, not a form to fill in:

```markdown
# <Name>

<What it is>: <what sets it apart>.

<Why the obvious version is only half the job.>

<How it answers that, and the idea it's built on.>
```

- If the project has no name, propose one.
- `INTENT.md` links to nothing. It's written before the other layers exist and should read on its own.
- It's a first draft. What sets the project apart often only becomes clear once the primitives exist, and Step 6 comes back to it.

Show the draft and get agreement before going on.

When you write `INTENT.md`, also copy [the README template](#docsreadmemd) to `docs/README.md`, word for word. The README tells an agent that has never seen this skill what the map is and how to read it. It is the same in every project, so it is never drafted, discussed or edited per project.

In the same step, point the project's agent instructions at the map, so the pointer is in place however the session ends. Add these lines to `AGENTS.md`, or to `CLAUDE.md` if that's the file the project already uses, creating `AGENTS.md` if neither exists:

```markdown
## The Map

This project has a map in `docs/`: what it's for, what it's made of and what must always hold. Read `docs/README.md` before changing code, and work with the `develop-project` skill.
```

### 3. Capabilities

A capability is something the project does that the owner can name with a verb. This is the layer the owner most likely already has in mind, so it's their list. Ask for the core capabilities in their words, and draft a file for each. Don't propose capabilities of your own, except to point out a gap you can name with a specific case.

These are drafts. The primitives don't exist yet, so each file says what happens in everyday words and links nothing. Step 4 revises them once it knows what the project is made of.

```markdown
# <Verb>

<What it does, in everyday terms.>

<Where judgment sits and what is fixed: "Deciding X takes judgment, so <who> makes
that call. That Y happens is fixed.">

## Invariants

- ...
```

- **Say where judgment lives.** When a person or a model decides something, name who decides, and then state what is guaranteed whatever they decide. This is what lets a build leave room for judgment without leaving room for silence.
- Look for: what it never does, what stays true if it runs twice, what happens when it fails, what it leaves untouched, when it runs and when it mustn't.
- **A capability can be deferred.** Write `**Deferred.**` under its description and record only the guardrails that are already settled.
- Don't worry yet whether a capability is really one primitive's own job. Step 4 settles that.

### 4. Primitives

A primitive is a thing the project is made of, and that would exist in any implementation of it. You'd need the word to explain the project to someone. It's also where behaviour lives: how one comes to exist, how it changes, how it ends and what it never does all belong in its file, not in a capability.

This is the layer that decides whether the structure will be beautiful. Spend the most effort here, and propose it yourself: the owner has described what the project does, and the things it's made of are what those descriptions keep naming.

Propose the list before writing files: each name, one line on what it is, and why it's its own thing. Also list what you considered and folded in, and which capability drafts it changes (see "Fold behaviour in" below). Expect three to six.

- **Read the capabilities for the things.** The nouns that keep turning up across them are the candidates. When the same record, condition or relationship appears in several capabilities, a primitive is often missing. Name it and give it a file.
- **Collapse hard.** For every pair, ask if they're different kinds of thing, or the same kind in different circumstances. If what separates them is how they came to be or how they're connected, they're one primitive, and its description says so. An observation, a belief and a concept are all memories. A prepared slide and one sketched ten seconds ago are both slides.
- **Don't collapse one word with two meanings.** Before merging, check the opposite case: the same word meaning different things in different parts of the project. If a "policy" as billing sees it and a "policy" as underwriting sees it hold different things and follow different rules, they are two primitives, even when they share an identity. Give each its own name, and say in each description how it relates to the other. If many words split this way, the idea may be more than one project. Say so to the owner.
- **Find the idea the rest follows from.** Look for the one statement about a primitive that many of its rules follow from. "How much a memory is believed is never stored: it's read off its evidence" explains why belief fades, why it can always be explained, why recalling a memory never changes it, and why recalibrating never rewrites the record. A primitive with an idea like that needs few invariants. One that needs a long list of unrelated rules is probably the wrong abstraction, so look again before adding more.
- **A thing, not a view of one.** What a thing looks like in one moment or to one reader, such as a memory as it comes to mind or a deck as it appears on screen, is a view of a primitive, not a primitive. Its rules belong to the capability or interface that produces the view.
- **Not primitives:** a field of something else, a storage structure, a screen, or anyone who uses the project. A person is never a primitive. What the project keeps about them can be: the user isn't a primitive, but their mind is.
- **Fold behaviour in.** Check each capability draft against the primitives. Invariants that are all about one primitive, how it begins, changes or ends, belong in that primitive's file. When nothing is left, the capability isn't one: recording a memory, revising belief in it and forgetting it all turned out to be Memory, while consolidating many memories in the background didn't. The owner listed the capabilities, so show them each one that moves or goes, in the same round as the list.

Once the owner agrees, write the primitive files. Then revise the capability drafts: move the folded invariants, delete the empty capabilities, and link each remaining capability to the primitives it spans.

Each file:

```markdown
# <Noun>

<What it is, in everyday terms. What it gathers or separates. Which things that look
different are really this same kind of thing.>

<The idea the rest follows from, when there is one.>

<Where judgment sits, when anything about it takes judgment: "Deciding X takes
judgment, so <who> makes that call. How Y follows is fixed.">

## Invariants

- **<One of the few statements the project would be different without.>** <What it means in practice.>
- <Most statements are plain, one per bullet.>
```

A lifecycle or a relationship diagram can sit above the invariants when it saves reading. See [Diagrams](#diagrams).

Look for: what it belongs to, how one comes to exist, how it changes and how it ends, what about it never changes, what is only ever added, what is kept and what deleting means, what it never claims, and what it does when it can't do its job.

### 5. Interfaces

An interface is a surface where the outside touches the project: the tools an agent calls, the hooks a host fires, the jobs that run when nobody is there, the API another system calls, the screens a person sees. Name each one with the word a builder would already use for that surface, and say in the file who or what is on the other side.

Propose the list, then check it against the capabilities: **something must start each capability, and something must see its result.** A capability nothing reaches means a surface is missing.

- **Name the surface, not the actor.** "Tools", not "Agent". "Hooks", not "Host". One actor can use several surfaces, and one surface can serve several actors.
- **An actor with no surface of their own gets no file.** When someone only reaches the project through another actor, such as a user who only ever talks to an agent, their rules land where they belong: in primitives, in capabilities, and on the surface that serves them, as what it must always let them do.
- **What the project calls out to isn't an interface.** A model it asks for judgment, or a service it relies on, is something it depends on, not a surface the outside touches. Its rules go where its answers are used: what it may decide, in the primitive or capability that asks, and what's recorded about its answers, wherever records are kept.
- **One surface across many hosts is still one surface.** Tools served over MCP in one host and natively in another are still `TOOLS.md`. How each host provides it goes in a column of the table, and the file says that a behaviour differing by host is a bug.

```markdown
# <Surface>

<What crosses here, who or what is on the other side, and what it is to the project.>

## <What passes>

| <Tool, hook, job, endpoint or screen> | <What it returns or does> |
|---|---|

## Invariants

- ...
```

- The table is the heart of the file: it names what crosses and what each thing does. Exact inputs and outputs belong to a later contract, and the file can say so.
- Use as many tables as the surface has parts. Group rows by what they're allowed to do, such as reading against changing.
- A row doesn't need a capability behind it. Small acts like listing or opening something live only in the table. When a row needs rules of its own, it has become a capability and gets a file.
- Interfaces are where naming an outside system is right, because the project has to meet it.
- Look for: what this side can and can't reach, what it's always able to ask for, what it's never asked to do or learn, how failure looks from this side, and what stays the same across every host or instance of it.

### 6. Walk the Map

Read the whole map once, as a builder who has nothing else.

- **Links.** When a file means another file's subject specifically, its first mention is a relative link, and every link resolves. An everyday use of the same word needs no link. Capabilities were drafted before the primitives existed, so check that each now links the primitives it spans. Files written early can point forward now that the later ones exist.
- **Behaviour sits with its primitive.** No capability's invariants are all about one primitive. If one's are, fold them in and delete the capability.
- **Few rules per idea.** A file past ten invariants, or one whose invariants don't share an idea, is where an abstraction is missing or wrong. Look there before adding anything else.
- **Primitives are used.** Each one is read or changed by at least one capability or surface. If not, it isn't a primitive or something is missing.
- **Capabilities are reachable.** Each one is started and observed through at least one surface.
- **The pitch matches the core.** Each promise in `INTENT.md` is held up by at least one invariant. What the primitives turned out to make distinctive is what `INTENT.md` leads with. If the most interesting things in the map aren't in the pitch, redraft the pitch with the owner.
- **Timing is said.** Each invariant that ties primitives together says whether it holds at every moment or catches up, and by when.
- **Nothing collides.** No two invariants contradict. The same rule appearing in two files says the same thing.
- **Nothing is built in.** Search for storage, libraries, algorithms, protocols and file layouts. Apply the swap test to each.
- **The guess test.** Ask: "If this map were all I had, what would I have to guess that the owner would mind me guessing wrong?" Each answer is a missing invariant or a question for the owner.

Fix what you can settle and ask about the rest in one round. Adding or removing a file changes a layer's list, so it goes to the owner with the questions.

### 7. Hand Off

Report the project in one sentence, the names in each layer, anything deferred, any question left open, and any default you took that the owner didn't explicitly confirm. Don't paste the files back.

Before stopping, check that the pointer from Step 2 is still in the project's agent instructions.

Then stop. Don't write a plan, pick a stack, scaffold a repository or start building. Building is `develop-project`'s job. For a project that already has code, say that `develop-project`'s audit is the natural next step: it shows where the code and the new map disagree.

## Mapping an Existing Project

A project with code but no map gets the same map a new project would, through the same steps and the same interview. The code is evidence, not the answer.

1. **Read before drafting.** Read the code, the README and any agent instructions, plans and commit history, for what the project is, what it's made of, and what turned out to matter. Don't copy how it works into the map.
2. **Draft every layer from what exists, as a proposal.** The owner still confirms each layer. Code shows what was built, not always what was meant, and owners often reshape it once they see it written down: a different focus, primitives cut along different lines.
3. **Use the code's names where they're right, and the right names where they aren't.** When the code has drifted, with two names for one thing or a rule held far from its thing, the map says what the project should be. Note each gap for the hand-off.
4. **A project's own conventions aren't primitives.** A file format, a folder layout or a style guide belongs on the surface that meets it, or nowhere.

## Changing the Map

When the map exists, it is the project's, so a new feature changes the map in place. There is no per-feature file. Work in `develop-project` that changes what the project is comes here, and goes back once the map says the new thing.

Once a project is mapped, changes don't wait for the owner. Make them and list them in the report so the owner can reverse any of them. Only the intent, and what's deliberately out or deferred, still need the owner.

1. Read the whole map first. If `docs/README.md` is missing, copy it. If it differs from its template, show the owner the difference and ask before replacing it.
2. Say which layer the change lands in. Most features add or change a primitive. A change to `INTENT.md` means it's becoming a different project, so confirm that with the owner explicitly, and do the same for anything deliberately out or deferred.
3. List the change as files added, edited and removed, with the reason for the change.
4. Edit in place. Files say what is true now, with no history, dates or "previously". When a primitive is replaced, delete its file and fix every link to it.
5. Walk the map again (Step 6), settling what you can yourself. A change to a primitive usually touches the capabilities and interfaces that mention it.
6. Report every file changed, and why, so the owner can reverse any of it.

## Common Mistakes

- **Writing a specification.** User stories, acceptance criteria, task lists and phases describe work to do. The map describes what stays true once the work is done.
- **Letting implementation in.** A database, a framework or a wire format in an invariant closes a decision the map exists to leave open.
- **Leaving the core open.** A map that lets each build decide what the core abstractions are gets code that works and has no shape. The primitives are the one part of the design the map fixes.
- **Splitting behaviour from its thing.** A capability for each thing a primitive does to itself, such as record, revise and forget, leaves the primitives as bare data and invites a layer of services over them. Fold the behaviour into the primitive.
- **Listing features.** "Supports search" says what's there. An invariant says what must hold about it.
- **Too many primitives.** Separate primitives for things that differ only in origin or circumstance produce a build with needless types. Collapse them.
- **One primitive for two meanings.** The reverse of too many primitives. A word that means different things in different parts of the project, merged into one file, gives a build one bloated type that serves every part badly.
- **A view as a primitive.** How a thing appears in one moment is produced by a capability or a surface. Making it a primitive doubles the thing.
- **Interfaces named after people.** "User" and "Agent" name who's there, not what they touch, and the rules inside end up belonging elsewhere. Name the surface.
- **A dependency as an interface.** A model or service the project calls is not a surface. Its rules belong with the work that uses it.
- **Capabilities with nobody to call them.** Writing interfaces last makes it easy to skip the check that each capability is reachable.
- **Leaving judgment unbounded.** "The agent decides when to ask" with no fixed guarantee beside it gives a build that may never ask, or always ask.
- **Stating the obvious.** Invariants any capable builder would honour anyway bury the ones that matter.
- **Quizzing the owner.** A long list of open questions hands the drafting back to them. Draft, then ask about what's left.
- **Guessing instead of asking.** The opposite error: settling something only the owner knows because asking felt like friction.
- **Copying the code into the map.** In a retroactive map, the code shows what was built. The map says what the project is, and where the two differ is a finding, not a reason to bend the map.
- **Carrying a prototype's lessons across as mechanism.** Keep what turned out to matter. Leave how it was solved.
- **Rationale in the map.** The map says what holds, never why. A "because" in a map file is the wrong content, so leave it out.
- **Going past the map.** Suggesting a stack, a schema or a first milestone is out of scope even when it seems helpful.

## Key Principles

- **The core is the design.** The primitives are the abstractions every build shares. Get them right and the rest follows. Leave them open and each build invents its own.
- **The map is enough, and no more.** Enough for a capable builder to get the core right, and open about everything around it.
- **Invariants over instructions.** Say what must stay true and let the builder find the way there. Statements about what holds survive a rewrite. Statements about how to build it don't.
- **Each layer earns the next.** Intent says what it's for, capabilities say what it must do, primitives are what those keep naming and where their behaviour lives, and interfaces make it all reachable.
- **Start where the owner is.** The owner knows what the project is for and what it must do, so those come first, from them. The agent helps more the deeper it goes, so primitives and interfaces are proposals.
- **Same kind of thing.** The most valuable move at the primitive layer is noticing that several things are one.
- **One idea, many rules.** The best primitive has an idea its rules follow from.
- **Judgment next to a guarantee.** Wherever someone decides, state what is fixed regardless.
- **Failure is visible.** For every primitive, capability and interface, the map says what the project does when it can't do its job. It never goes quiet.
- **The map says what holds.** It changes in place, and carries no history and no rationale.
- **The project owns the map.** It changes when the project changes, in place, and it carries no trace of the features that shaped it.
- **Rediscovery is fine.** A build from this map will relearn details an earlier attempt already knew. That cost is accepted, in exchange for a map that fixes only what matters.

<!-- shared:start (generated from skills/shared/ by checks/sync_shared.py; edit there) -->

## Shared Rules

These rules come from `skills/shared/RULES.md`, the one source both skills share.

Both skills, `map-project` and `develop-project`, follow these rules. This file is their one source: a skill links here instead of restating a rule, so the two can't drift apart.

### Words

| Word | Means |
|---|---|
| **Project** | What gets mapped and built, new or already existing |
| **Owner** | The person whose project it is, and who decides what only they can know |
| **Shape** | The model a person holds of a project: the few things it's made of, each with one idea behind it |
| **Map** | The shape written down in a project's `docs/`: its intent, primitives, capabilities and interfaces |
| **Primitive** | A thing the project is made of. The core of the code takes its shape |
| **Capability** | A process across primitives that no one primitive owns |
| **Interface** | A surface where the outside touches the project |
| **Invariant** | A statement that holds at every moment, in every build |
| **Check** | Something that would notice an invariant breaking |
| **Audit** | Showing whether the code keeps the map, for one change or a whole project |

"User" means someone who uses the project, as in "the user is not nagged". It never means the owner.

### The Map

```
docs/
  README.md                    how to read the map, copied from templates/README.md
  INTENT.md                    what it's for
  primitives/<NOUN>.md         what it's made of, and how each thing behaves
  capabilities/<VERB>.md       what it does that no one thing does
  interfaces/<SURFACE>.md      where the outside touches it, and what crosses
```

`AGENTS.md`, or `CLAUDE.md` if the project uses that, points at the map. Every file except `INTENT.md` is a short description followed by invariants. Filenames are uppercase: a singular noun for a primitive, a verb for a capability, and the surface's common name for an interface.

| Layer | Answers | Named with | Examples |
|-------|---------|-----------|----------|
| Intent | What is this for? | The project's name | `INTENT.md` |
| Primitives | What is it made of, and how does each thing behave? | A singular noun | `MEMORY.md`, `DECK.md`, `QUESTION.md` |
| Capabilities | What does it do that no one thing does? | A verb | `CONSOLIDATE.md`, `RECALL.md`, `ANSWER.md` |
| Interfaces | Where does the outside touch it, and what crosses? | The surface's common name | `TOOLS.md`, `HOOKS.md`, `JOBS.md`, `API.md` |

**The primitives are the core of the code.** A build names its core after them, keeps their boundaries, and holds each primitive's invariants in that primitive. The abstractions are the design, and a build that dissolves them into services and helpers has lost it. Good code and an intuitive model go together: someone who has read the map can predict where each thing lives in the code and what it does, and code that's hard to explain from the map is usually a sign the map or the code has the wrong things in it. Everything around the core is the builder's call: storage, frameworks, protocols, layout, and where the rules of a capability or interface are enforced.

A primitive file still never reads as a list of fields, and a capability file never reads as a function signature. The map says what each thing is and what holds about it, not how it's stored or called.

### What Counts as an Invariant

An invariant is a statement about the project that is true at every moment, in every build of it. It passes four tests:

1. **Always.** It holds all the time, not at one step. If it describes a sequence, it's a procedure.
2. **Breakable.** A build could visibly violate it, and someone could point at the violation.
3. **Open.** Two quite different implementations could both satisfy it.
4. **Earned.** A capable builder working from the rest of the map could plausibly get it wrong without being told. What any sensible builder would do anyway is left out.

| Not an invariant | Why | Invariant |
|------------------|-----|-----------|
| "Memories are rows in a SQLite table" | Implementation | "A memory's content is never edited. When it turns out to be wrong, a new memory supersedes it." |
| "Listeners can ask questions" | Feature | "No question is dropped. Every question is answered, put off out loud, or declined out loud." |
| "Recall should be accurate" | Can't be broken visibly | "A memory that is only loosely related is labelled that way. It's never passed off as an answer." |
| "At most three questions a week" | A tuning number | "The user is not nagged. Questions to the user are strictly limited per conversation and per week." |
| "Load the slide, then start the audio" | Procedure | "What's seen and what's heard stay together." |
| "Errors are handled gracefully" | Any builder would say this | "Recall that fails says it failed. An agent is never shown 'nothing relevant' when the mind wasn't searched." |

**Naming a technology.** Name one only when the project must *meet* it: a runtime it has to live inside, a system it has to talk to, a format the owner insists on. Never name one the project is merely *built with*. The test: swap it out. If what's left is the same project built differently, it doesn't belong in the map.

**Across primitives.** An invariant that ties two or more primitives together says when it holds: at every moment, or restored after each change and by when. "A deck's slide count always matches its slides" and "a deck's slide count catches up before anyone next opens it" are different projects to someone watching. When the owner wouldn't mind which, write the one that catches up: it's the weaker promise, and a build that holds the stronger one keeps it too.

**Numbers.** State the limit, not its value. "Strictly limited per conversation" survives every build. A number is a tuning decision that a build makes and measures.

### Diagrams

Diagrams help a person who skims. Use them where they save reading, and nowhere else.

- **Mermaid only.** It renders on GitHub and in most editors, and it's text, so it diffs and reviews like the rest of the file.
- **A diagram follows the rules of the file it's in.** In the map it names no implementation: no tables, services or protocols. A relationship diagram of primitives never shows fields, for the same reason a primitive file never reads as a list of fields. In a plan or a README, implementation is fine.
- **It adds to the invariants and never replaces them.** An invariant can be broken and quoted; a box in a diagram can't. When the diagram and the text disagree, the text wins and the diagram is fixed.
- **Each layer has a natural shape:**

  | Layer | Diagram |
  |---|---|
  | Primitives | A lifecycle (state diagram), or how primitives relate (relationship diagram) |
  | Capabilities | A flow, or a decision |
  | Interfaces | A sequence: who calls what, in order |

- **One or two per file at most, and only where prose or a table is slower.** A short list doesn't need a picture.
- **A gradual change isn't a state.** Something that fades or drifts goes in a note, not a self-loop.
- **Relationship labels are a word or two:** "owns", "from", "to".
- **Render it before committing.** A diagram that doesn't parse is worse than none.

### Writing Style

For the map:

- Plain, everyday words. Describe the project the way you'd explain it to someone who will never see the code.
- Short declarative sentences in the present tense. "Never", "always", "only", "exactly one".
- One idea per bullet. Bold the few statements in each file the project would be a different project without, and no others.
- Concrete examples in quotes beat abstractions: "is your favorite color still pink?", "wait, why?".
- Use colons and commas for asides, not dashes.
- Files are short: a description and four to ten invariants. A file that keeps growing is usually two things, or a thing still missing its idea.
- No status, no dates, no rationale, no references to the conversation that wrote it.

## Templates

Copy these into a project word for word, at the path each one names.

### `docs/README.md`

````markdown
# The Map

These files are the map of the project. Apart from the intent, each is a short description followed by statements that hold in every build of it.

- [INTENT.md](INTENT.md): what it's for. Read it first.
- `primitives/`: what it's made of, and how each thing behaves.
- `capabilities/`: what it does that no one thing does.
- `interfaces/`: where the outside touches it, and what crosses.

## Reading the Map

- **The primitives are the core of the code.** Name the core after them, keep their boundaries, and hold each primitive's rules in that primitive. Everything around the core is the builder's choice.
- Where the map says nothing, the choice is the builder's.
- Bold statements are the ones the project would be a different project without.
- An invariant that says it catches up may be held sooner, never later.
- A build that can't keep an invariant changes the map, or finds another way. It never becomes a quiet exception.
- When the project changes, these files change in place.
````

<!-- shared:end -->
