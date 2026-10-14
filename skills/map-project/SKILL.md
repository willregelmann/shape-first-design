---
name: map-project
description: Maps a project's shape with its owner, by interviewing them and writing the map under docs/ (INTENT.md, then primitives, capabilities and interfaces, each a short file of statements that must always hold, with MADR decision records for why it has that shape) — use when someone says "let's start a new project", "I want to build X", "map this out", "map this project", or "write the invariants", for a project that doesn't exist yet or one that already has code but no map, or when someone wants to add or change a primitive, capability or interface in an existing map. Stops at the map and does not plan or implement.
tags:
  - design
  - primitives
  - invariants
  - decision-records
---

# Map Project

Find a project's shape with its owner and write it down as a map: `INTENT.md`, `primitives/`, `capabilities/` and `interfaces/` under `docs/`, saying what the project is for, what it's made of, what it does and where the outside touches it, as statements that must always hold. Beside it, `docs/decisions/` records why the map has the shape it has.

Capable models write excellent code, but rarely beautiful structure. Structure comes from the abstractions: the few things a project is made of, chosen so that its behaviour follows from them and someone new can hold the whole of it in mind. The map's main job is to find those abstractions with the owner and fix them, so every build shares the same core.

The map must be **enough, on its own, for a capable agent to build a working project of the right shape**, and readable by anyone who wants to understand the project without reading its code. It fixes the core and leaves the rest open. Two builders given only the map should produce the same core, with the same names and the same boundaries, on whatever stack each one chose.

It's the north star for every agent that touches the project, for the project's whole life, not for one feature. This skill stops at the map. Choosing a stack, writing a plan and writing code belong to `develop-project`, and none of them happen here.

**Read [the shared rules](../shared/RULES.md) first.** They define the words, the map's layout and layers, what counts as an invariant, how decisions are kept, and the writing style. This skill doesn't restate them.

## Quick Reference

| Step | Job | Output |
|------|-----|--------|
| 1 | Listen, and check the ground: new, existing code, or an existing map | A shared picture of the project |
| 2 | Intent | `docs/INTENT.md`, plus `docs/README.md` and `docs/decisions/` copied from the templates |
| 3 | Primitives | `docs/primitives/<NOUN>.md` |
| 4 | Capabilities | `docs/capabilities/<VERB>.md` |
| 5 | Interfaces | `docs/interfaces/<SURFACE>.md` |
| 6 | Walk the map | Gaps closed, behaviour with its primitive, links resolve, nothing built in |
| 7 | Hand off | A short summary and a pointer to the map, then stop |

Decision records are written during Steps 2 to 6, as soon as the owner settles each choice. See [Decisions](#decisions).

Work one layer at a time, in this order. Each layer uses the words the one before it defined. Get the owner's agreement on a layer before writing its files, and before starting the next.

## Interviewing

The owner has the idea. You do the drafting. Interview where guidance is needed, and nowhere else.

- **Propose, don't quiz.** Put a concrete candidate in front of the owner and let them correct it. They should be able to confirm rather than compose.
- **Ask what only the owner knows:** who it's for, what would make it pointless, what it must work with, what's deliberately out or deferred, and which of two reasonable shapes they want.
- **Ask when two capable builders would choose differently and the owner would mind.** If they wouldn't mind, it's implementation. Leave it open and don't ask.
- **Every question carries your best answer as the default.** Use a structured-question tool when one is available, and a short numbered list when not.
- **Batch questions per layer.** One round is the aim.
- **Disagree out loud.** When the owner's framing has a gap or two of their ideas collide, say so with the specific case, and offer a way through.
- **A default is not a guess.** A default is something the owner sees and confirms. A guess is something written into the map that they never saw. If the owner doesn't answer, the statement stays out.
- **Unresolved is a legitimate outcome.** Leave the statement out and carry the question to the hand-off.

## Decisions

Follow [the shared rules for decisions](../shared/RULES.md#decisions). This skill records choices about what the project is. In practice that means a record for:

- each question the owner answers that settles a fork, including the question in `INTENT.md` when there were candidates, as `0001`;
- each collapse or split at the primitive layer that had a real alternative, with what you considered and folded in as the options turned down;
- each capability folded into a primitive, and each surface named, when there was a real alternative.

Small choices that answer one question share a record, with the options grouped under each part of the question. The title states the decision: "One kind of memory: observations, beliefs and concepts differ by evidence, not by type". When the owner chooses without giving a reason, the record says the owner chose, and marks the reason `TODO`.

## Process

### 1. Listen

Let the owner describe what they want. Restate it in two or three sentences so they can correct the picture early.

Check the ground:

- **Nothing here yet?** Map the project from the conversation.
- **Code here, but no map?** Map it retroactively. See [Mapping an Existing Project](#mapping-an-existing-project) before Step 2.
- **A map already here** (`docs/INTENT.md` with `docs/primitives/` beside it)? Go to [Changing the Map](#changing-the-map).
- **A prototype or earlier attempt?** Read it for what turned out to matter, not for how it worked. Keep the consequence and drop the cause: "empty audio clips deadlock the player" becomes "silence is never ambiguous". A later build is expected to rediscover the details, and that is intended. When the prototype settled a choice the map now relies on, that choice can become a record, written after the fact.

Don't research stacks, libraries or architectures. Research into the problem itself is fine when the owner asks for it.

### 2. Intent

Draft `docs/INTENT.md` from what the owner said, and ask only for what's missing. It's an elevator pitch: about ten lines of prose with no sections, no lists and no mechanism.

```markdown
# <Name>

<What it is, in a few words>: <the one thing that sets it apart>.

<When it matters>, <Name> <answers | keeps open> one question: **<the question>**

<Why the obvious version of this project is only half the job. Concrete cases in
everyday words.>

<How it answers those cases, in the same order, and the one idea it's built on.
Behaviour in broad strokes, never mechanism.>

If <the specific thing that would make it pointless>, <Name> has failed at the one
thing it exists to do.
```

- The **question** is the one the project exists to keep answering: "what should I have in mind right now?", "did that land?". If you can't find one, the idea isn't sharp yet. Keep talking.
- The **failure sentence** names an outcome someone could observe: "If a lecture would have gone exactly the same with nobody listening". It's the most useful line in the map, so ask for it directly if the owner hasn't given it.
- If the project has no name, propose one.
- `INTENT.md` links to nothing. It's written before the other layers exist and should read on its own.
- It's a first draft. What sets the project apart often only becomes clear once the primitives exist, and Step 6 comes back to it.

Show the draft and get agreement before going on.

When you write `INTENT.md`, also copy [templates/README.md](../shared/templates/README.md) to `docs/README.md`, and the files in [templates/decisions/](../shared/templates/decisions/) to `docs/decisions/`, word for word. The README tells an agent that has never seen this skill what the map is and how to read it. The decision templates set how records are kept. They are the same in every project, so they are never drafted, discussed or edited per project.

### 3. Primitives

A primitive is a thing the project is made of, and that would exist in any implementation of it. You'd need the word to explain the project to someone. It's also where behaviour lives: how one comes to exist, how it changes, how it ends and what it never does all belong in its file, not in a capability.

This is the layer that decides whether the structure will be beautiful. Spend the most effort here.

Propose the list before writing files: each name, one line on what it is, and why it's its own thing. Also list what you considered and folded in. Expect three to six. Once the owner agrees, write a record for each collapse or split that had a real alternative.

- **Collapse hard.** For every pair, ask if they're different kinds of thing, or the same kind in different circumstances. If what separates them is how they came to be or how they're connected, they're one primitive, and its description says so. An observation, a belief and a concept are all memories. A prepared slide and one sketched ten seconds ago are both slides.
- **Don't collapse one word with two meanings.** Before merging, check the opposite case: the same word meaning different things in different parts of the project. If a "policy" as billing sees it and a "policy" as underwriting sees it hold different things and follow different rules, they are two primitives, even when they share an identity. Give each its own name, and say in each description how it relates to the other. If many words split this way, the idea may be more than one project. Say so to the owner.
- **Find the idea the rest follows from.** Look for the one statement about a primitive that many of its rules follow from. "How much a memory is believed is never stored: it's read off its evidence" explains why belief fades, why it can always be explained, why recalling a memory never changes it, and why recalibrating never rewrites the record. A primitive with an idea like that needs few invariants. One that needs a long list of unrelated rules is probably the wrong abstraction, so look again before adding more.
- **Name the concept that keeps turning up.** When the same record, condition or relationship appears in several files, a primitive is often missing. Name it and give it a file.
- **A thing, not a view of one.** What a thing looks like in one moment or to one reader, such as a memory as it comes to mind or a deck as it appears on screen, is a view of a primitive, not a primitive. Its rules belong to the capability or interface that produces the view.
- **Not primitives:** a field of something else, a storage structure, a screen, or anyone who uses the project. A person is never a primitive. What the project keeps about them can be: the user isn't a primitive, but their mind is.

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

Look for: what it belongs to, how one comes to exist, how it changes and how it ends, what about it never changes, what is only ever added, what is kept and what deleting means, what it never claims, and what it does when it can't do its job.

### 4. Capabilities

A capability is a process the project carries out across several primitives, which isn't the natural job of any one of them. It's named with a verb. Most behaviour already lives in the primitives, so expect few capabilities. Propose the list the same way: name, one line, why it isn't a primitive's own job.

```markdown
# <Verb>

<What it does, across which [primitives](../primitives/NOUN.md).>

<Where judgment sits and what is fixed: "Deciding X takes judgment, so <who> makes
that call. That Y happens is fixed.">

## Invariants

- ...
```

- **Fold before you add.** Check each candidate's invariants. If they're all about one primitive, how it begins, changes or ends, they belong in that primitive's file and the candidate isn't a capability. Recording a memory, revising belief in it and forgetting it all turned out to be Memory. Consolidating many memories in the background didn't.
- **Say where judgment lives.** When a person or a model decides something, name who decides, and then state what is guaranteed whatever they decide. This is what lets a build leave room for judgment without leaving room for silence.
- Look for: what it never does, what stays true if it runs twice, what happens when it fails, what it leaves untouched, when it runs and when it mustn't.
- **A capability can be deferred.** Write `**Deferred.**` under its description and record only the guardrails that are already settled.

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

- **Links.** When a file means another file's subject specifically, its first mention is a relative link, and every link resolves. An everyday use of the same word needs no link. Files written early can point forward now that the later ones exist.
- **Behaviour sits with its primitive.** No capability's invariants are all about one primitive. If one's are, fold them in and delete the capability.
- **Few rules per idea.** A file past ten invariants, or one whose invariants don't share an idea, is where an abstraction is missing or wrong. Look there before adding anything else.
- **Primitives are used.** Each one is read or changed by at least one capability or surface. If not, it isn't a primitive or something is missing.
- **Capabilities are reachable.** Each one is started and observed through at least one surface.
- **The pitch matches the core.** Each promise in `INTENT.md` is held up by at least one invariant, and you can name the invariants that stop the failure sentence from coming true. What the primitives turned out to make distinctive is what `INTENT.md` leads with. If the most interesting things in the map aren't in the pitch, redraft the pitch with the owner.
- **Timing is said.** Each invariant that ties primitives together says whether it holds at every moment or catches up, and by when.
- **Nothing collides.** No two invariants contradict. The same rule appearing in two files says the same thing.
- **Nothing is built in.** Search for storage, libraries, algorithms, protocols and file layouts. Apply the swap test to each.
- **Decisions are recorded.** Every fork the owner settled has a record. Each record's Confirmation names invariants that exist. No map file links into `docs/decisions/`, and no map file explains itself with a "because" that belongs in a record.
- **The guess test.** Ask: "If this map were all I had, what would I have to guess that the owner would mind me guessing wrong?" Each answer is a missing invariant or a question for the owner.

Fix what you can settle and ask about the rest in one round. Adding or removing a file changes a layer's list, so it goes to the owner with the questions.

### 7. Hand Off

Report the project in one sentence, the names in each layer, the decisions recorded, anything deferred, any question left open, and any default you took that the owner didn't explicitly confirm. Don't paste the files back.

Before stopping, make sure the project's agent instructions point at the map, so that any agent working in the repository finds it. Add these lines to `AGENTS.md`, or to `CLAUDE.md` if that's the file the project uses, creating it if neither exists:

```markdown
## The Map

This project has a map in `docs/`: what it's for, what it's made of and what must always hold, with decision records for why. Read `docs/README.md` before changing code, and work with the `develop-project` skill.
```

Then stop. Don't write a plan, pick a stack, scaffold a repository or start building. Building is `develop-project`'s job. For a project that already has code, say that `develop-project`'s audit is the natural next step: it shows where the code and the new map disagree.

## Mapping an Existing Project

A project with code but no map gets the same map a new project would, through the same steps and the same interview. The code is evidence, not the answer.

1. **Read before drafting.** Read the code, the README and any agent instructions, plans and commit history, for what the project is, what it's made of, and what turned out to matter. Don't copy how it works into the map.
2. **Draft every layer from what exists, as a proposal.** The owner still confirms each layer. Code shows what was built, not always what was meant, and owners often reshape it once they see it written down: a different question, primitives cut along different lines.
3. **Use the code's names where they're right, and the right names where they aren't.** When the code has drifted, with two names for one thing or a rule held far from its thing, the map says what the project should be. Note each gap for the hand-off.
4. **Record what the history shows.** Choices settled in the conversation are recorded as usual. Choices visible only in the history can be backfilled after the fact, following `develop-project`'s Backfilling Decisions, with the owner's agreement.
5. **A project's own conventions aren't primitives.** A file format, a folder layout or a style guide belongs on the surface that meets it, or nowhere.

## Changing the Map

When the map exists, it is the project's, so a new feature changes the map in place. There is no per-feature file. Work in `develop-project` that changes the model comes here, and goes back once the map says the new thing.

1. Read the whole map and its decisions first. If `docs/README.md` or the files from [templates/decisions/](../shared/templates/decisions/) are missing, copy them. If one differs from its template, show the owner the difference and ask before replacing it. If the map has no records but its history is written down somewhere, such as a plan, commit messages or research notes, offer to backfill records after the fact, following `develop-project`'s Backfilling Decisions.
2. Say which layer the change lands in. Most features add or change a primitive. A change to `INTENT.md` means it's becoming a different project, so confirm that explicitly.
3. Propose the change as a list of files added, edited and removed, and get agreement.
4. Edit in place. Files say what is true now, with no history, dates or "previously". When a primitive is replaced, delete its file and fix every link to it. A change that reverses a recorded decision gets a new record that supersedes the old one.
5. Walk the map again (Step 6). A change to a primitive usually touches the capabilities and interfaces that mention it.

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
- **Rationale in the map.** A "because" in a map file is a record waiting to be written. Move it.
- **Going past the map.** Suggesting a stack, a schema or a first milestone is out of scope even when it seems helpful.

## Key Principles

- **The core is the design.** The primitives are the abstractions every build shares. Get them right and the rest follows. Leave them open and each build invents its own.
- **The map is enough, and no more.** Enough for a capable builder to get the core right, and open about everything around it.
- **Invariants over instructions.** Say what must stay true and let the builder find the way there. Statements about what holds survive a rewrite. Statements about how to build it don't.
- **Each layer earns the next.** Intent gives the question, primitives give the words and the behaviour, capabilities do what no one thing does, and interfaces make it all reachable.
- **Same kind of thing.** The most valuable move at the primitive layer is noticing that several things are one.
- **One idea, many rules.** The best primitive has an idea its rules follow from.
- **Judgment next to a guarantee.** Wherever someone decides, state what is fixed regardless.
- **Failure is visible.** For every primitive, capability and interface, the map says what the project does when it can't do its job. It never goes quiet.
- **What and why live apart.** The map changes in place and carries no history. The decisions only grow, and explain the map without repeating it.
- **The project owns the map.** It changes when the project changes, in place, and it carries no trace of the features that shaped it.
- **Rediscovery is fine.** A build from this map will relearn details an earlier attempt already knew. That cost is accepted, in exchange for a map that fixes only what matters.
