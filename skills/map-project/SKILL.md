---
name: map-project
description: Maps a new product before anything is planned or built, by interviewing the user and writing its map under docs/ (INTENT.md, then primitives, capabilities and interfaces, each a short file of statements that must always hold, with MADR decision records for why it has that shape) — use when the user says "let's start a new project", "I want to build X", "new project", "map this out", or "write the invariants", or wants to add a primitive, capability or interface to an existing map. For greenfield work only. Stops at the map and does not plan or implement.
tags:
  - invariants
  - intent
  - greenfield
  - design
---

# Map Project

Turn an idea into a map: `INTENT.md`, `primitives/`, `capabilities/` and `interfaces/` under `docs/`, saying what the product is for, what it's made of, what it does and where the outside touches it, as statements that must always hold. Beside it, `docs/decisions/` records why the map has the shape it has.

Capable models write excellent code, but rarely beautiful structure. Structure comes from the abstractions: the few things a product is made of, chosen so that its behaviour follows from them and someone new can hold the whole of it in mind. The map's main job is to find those abstractions with the user and fix them, so every build shares the same core.

The map must be **enough, on its own, for a capable agent to build a working product of the right shape**. It fixes the core and leaves the rest open. Two builders given only the map should produce the same core, with the same names and the same boundaries, on whatever stack each one chose.

It is the north star for every agent that touches the product, for the product's whole life, not for one feature. This skill stops at the map. Choosing a stack, writing a plan and writing code are separate work, and none of them happen here.

## Quick Reference

| Step | Job | Output |
|------|-----|--------|
| 1 | Listen, and check this is greenfield | A shared picture of the idea |
| 2 | Intent | `docs/INTENT.md`, plus `docs/README.md` and `docs/decisions/` copied from the templates |
| 3 | Primitives | `docs/primitives/<NOUN>.md` |
| 4 | Capabilities | `docs/capabilities/<VERB>.md` |
| 5 | Interfaces | `docs/interfaces/<SURFACE>.md` |
| 6 | Walk the map | Gaps closed, behaviour with its primitive, links resolve, nothing built in |
| 7 | Hand off | A short summary, then stop |

Decision records in `docs/decisions/` are written during Steps 2 to 6, as soon as the user settles each choice. See [Decisions](#decisions).

Filenames are uppercase with a `.md` extension: a singular noun for a primitive, a verb for a capability, the surface's common name for an interface.

Work one layer at a time, in this order. Each layer uses the words the one before it defined. Get the user's agreement on a layer before writing its files, and before starting the next.

## The Layers

| Layer | Answers | Named with | Examples |
|-------|---------|-----------|----------|
| Intent | What is this for, and what would make it pointless? | The product's name | `INTENT.md` |
| Primitives | What is it made of, and how does each thing behave? | A singular noun | `MEMORY.md`, `DECK.md`, `QUESTION.md` |
| Capabilities | What does it do that no one thing does? | A verb | `CONSOLIDATE.md`, `RECALL.md`, `ANSWER.md` |
| Interfaces | Where does the outside touch it, and what crosses? | The surface's common name | `TOOLS.md`, `HOOKS.md`, `JOBS.md`, `API.md` |

**The primitives are the core of the code.** A build names its core after them, keeps their boundaries, and holds each primitive's invariants in that primitive. That is the point of the map: the abstractions are the design, and a build that dissolves them into services and helpers has lost it. Everything around the core is the builder's call: storage, frameworks, protocols, layout, and where the rules of a capability or interface are enforced.

A primitive file still never reads as a list of fields, and a capability file never reads as a function signature. The map says what each thing is and what holds about it, not how it's stored or called.

## What Counts as an Invariant

An invariant is a statement about the product that is true at every moment, in every build of it. It passes four tests:

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

**Naming a technology.** Name one only when the product must *meet* it: a runtime it has to live inside, a system it has to talk to, a format the user insists on. Never name one the product is merely *built with*. The test: swap it out. If what's left is the same product built differently, it doesn't belong here.

**Across primitives.** An invariant that ties two or more primitives together says when it holds: at every moment, or restored after each change and by when. "A deck's slide count always matches its slides" and "a deck's slide count catches up before anyone next opens it" are different products to someone watching. Both pass the Always test, because each says what is true at every moment. Ask when the user would mind which. When they wouldn't, write the one that catches up: it's the weaker promise, and a build that holds the stronger one keeps it too.

**Numbers.** State the limit, not its value. "Strictly limited per conversation" survives every build. A number is a tuning decision that a build makes and measures.

## Interviewing

The user has the idea. You do the drafting. Interview where guidance is needed, and nowhere else.

- **Propose, don't quiz.** Put a concrete candidate in front of the user and let them correct it. They should be able to confirm rather than compose.
- **Ask what only the user knows:** who it's for, what would make it pointless, what it must work with, what's deliberately out or deferred, and which of two reasonable shapes they want.
- **Ask when two capable builders would choose differently and the user would mind.** If they wouldn't mind, it's implementation. Leave it open and don't ask.
- **Every question carries your best answer as the default.** Use a structured-question tool when one is available, and a short numbered list when not.
- **Batch questions per layer.** One round is the aim.
- **Disagree out loud.** When the user's framing has a gap or two of their ideas collide, say so with the specific case, and offer a way through.
- **A default is not a guess.** A default is something the user sees and confirms. A guess is something written into the map that they never saw. If the user doesn't answer, the statement stays out.
- **Unresolved is a legitimate outcome.** Leave the statement out and carry the question to the hand-off.

## Decisions

The map says what holds. `docs/decisions/` says why, as [MADR](https://adr.github.io/madr/) records. Every map starts with two files copied word for word from [templates/decisions/](templates/decisions/): `0000-record-decisions-as-madr.md`, which sets the conventions, and `adr-template.md`. Like the README, they are the same in every product and never drafted or edited per product.

**Write a record when a choice is made that someone could later want to undo.** The bar is the same as for asking: two capable builders would choose differently and the user would mind. In practice that means:

- each question the user answers that settles a fork, including the question in `INTENT.md` when there were candidates;
- each collapse or split at the primitive layer that had a real alternative, with what you considered and folded in as the options turned down;
- each capability folded into a primitive, and each surface named, when there was a real alternative.

Small choices that answer one question share a record, with the options grouped under each part of the question. The title states the decision: "One kind of memory: observations, beliefs and concepts differ by evidence, not by type".

- **A pattern or a boundary, not a setting.** The same swap test as for invariants: if changing a value or a name leaves the record true, it isn't a record.
- **Modelling decisions only.** This skill records what shaped the map. Decisions about the stack, storage and deployment come later, from whoever builds, in the same folder.
- **The map never links to a record.** A record can be superseded, and the map carries no history. A record links to the map files that hold its decision, and its Confirmation names the invariants that keep it true.
- **Only what was weighed.** List the options that were actually on the table, give the user's reason in their words where they gave one, and write `TODO` where the reason is unknown. Never invent a rejected option to make a record look complete.
- **Written at the time.** Write the record right after the user agrees, while the options and reasons are in front of you, not reconstructed at the end.
- **Never edited.** A reversed decision gets a new record that supersedes the old one.

## Process

### 1. Listen

Let the user describe what they want. Restate it in two or three sentences so they can correct the picture early.

Check the ground:

- **Source code already here?** This skill maps products that don't exist yet, before any architectural decision. Say so, and ask how to proceed.
- **A map already here** (`docs/INTENT.md` with `docs/primitives/` beside it)? Go to [Changing the Map](#changing-the-map).
- **A prototype or earlier attempt?** Read it for what turned out to matter, not for how it worked. Keep the consequence and drop the cause: "empty audio clips deadlock the player" becomes "silence is never ambiguous". A later build is expected to rediscover the details, and that is intended. When the prototype settled a choice the map now relies on, that choice can become a record, written after the fact.

Don't research stacks, libraries or architectures. Research into the problem itself is fine when the user asks for it.

### 2. Intent

Draft `docs/INTENT.md` from what the user said, and ask only for what's missing. It's an elevator pitch: about ten lines of prose with no sections, no lists and no mechanism.

```markdown
# <Name>

<What it is, in a few words>: <the one thing that sets it apart>.

<When it matters>, <Name> <answers | keeps open> one question: **<the question>**

<Why the obvious version of this product is only half the job. Concrete cases in
everyday words.>

<How it answers those cases, in the same order, and the one idea it's built on.
Behaviour in broad strokes, never mechanism.>

If <the specific thing that would make it pointless>, <Name> has failed at the one
thing it exists to do.
```

- The **question** is the one the product exists to keep answering: "what should I have in mind right now?", "did that land?". If you can't find one, the idea isn't sharp yet. Keep talking.
- The **failure sentence** names an outcome someone could observe: "If a lecture would have gone exactly the same with nobody listening". It's the most useful line in the map, so ask for it directly if the user hasn't given it.
- If the product has no name, propose one.
- `INTENT.md` links to nothing. It's written before the other layers exist and should read on its own.
- It's a first draft. What sets the product apart often only becomes clear once the primitives exist, and Step 6 comes back to it.

Show the draft and get agreement before going on.

When you write `INTENT.md`, also copy [templates/README.md](templates/README.md) to `docs/README.md`, and the files in [templates/decisions/](templates/decisions/) to `docs/decisions/`, word for word. The README tells an agent that has never seen this skill what the map is and how to read it. The decision templates set how records are kept. They are the same in every product, so they are never drafted, discussed or edited per product, and the rules for the map's other files don't apply to them.

If the user chose the product's question from more than one candidate, record it as `0001`.

### 3. Primitives

A primitive is a thing the product is made of, and that would exist in any implementation of it. You'd need the word to explain the product to someone. It's also where behaviour lives: how one comes to exist, how it changes, how it ends and what it never does all belong in its file, not in a capability.

This is the layer that decides whether the structure will be beautiful. Spend the most effort here.

Propose the list before writing files: each name, one line on what it is, and why it's its own thing. Also list what you considered and folded in. Expect three to six. Once the user agrees, write a record for each collapse or split that had a real alternative.

- **Collapse hard.** For every pair, ask if they're different kinds of thing, or the same kind in different circumstances. If what separates them is how they came to be or how they're connected, they're one primitive, and its description says so. An observation, a belief and a concept are all memories. A prepared slide and one sketched ten seconds ago are both slides.
- **Don't collapse one word with two meanings.** Before merging, check the opposite case: the same word meaning different things in different parts of the product. If a "policy" as billing sees it and a "policy" as underwriting sees it hold different things and follow different rules, they are two primitives, even when they share an identity. Give each its own name, and say in each description how it relates to the other. If many words split this way, the idea may be more than one product. Say so to the user.
- **Find the idea the rest follows from.** Look for the one statement about a primitive that many of its rules follow from. "How much a memory is believed is never stored: it's read off its evidence" explains why belief fades, why it can always be explained, why recalling a memory never changes it, and why recalibrating never rewrites the record. A primitive with an idea like that needs few invariants. One that needs a long list of unrelated rules is probably the wrong abstraction, so look again before adding more.
- **Name the concept that keeps turning up.** When the same record, condition or relationship appears in several files, a primitive is often missing. Name it and give it a file.
- **A thing, not a view of one.** What a thing looks like in one moment or to one reader, such as a memory as it comes to mind or a deck as it appears on screen, is a view of a primitive, not a primitive. Its rules belong to the capability or interface that produces the view.
- **Not primitives:** a field of something else, a storage structure, a screen, or anyone who uses the product. A person is never a primitive. What the product keeps about them can be: the user isn't a primitive, but their mind is.

Each file:

```markdown
# <Noun>

<What it is, in everyday terms. What it gathers or separates. Which things that look
different are really this same kind of thing.>

<The idea the rest follows from, when there is one.>

<Where judgment sits, when anything about it takes judgment: "Deciding X takes
judgment, so <who> makes that call. How Y follows is fixed.">

## Invariants

- **<One of the few statements the product would be different without.>** <What it means in practice.>
- <Most statements are plain, one per bullet.>
```

Look for: what it belongs to, how one comes to exist, how it changes and how it ends, what about it never changes, what is only ever added, what is kept and what deleting means, what it never claims, and what it does when it can't do its job.

### 4. Capabilities

A capability is a process the product carries out across several primitives, which isn't the natural job of any one of them. It's named with a verb. Most behaviour already lives in the primitives, so expect few capabilities. Propose the list the same way: name, one line, why it isn't a primitive's own job.

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

An interface is a surface where the outside touches the product: the tools an agent calls, the hooks a host fires, the jobs that run when nobody is there, the API another system calls, the screens a person sees. Name each one with the word a builder would already use for that surface, and say in the file who or what is on the other side.

Propose the list, then check it against the capabilities: **something must start each capability, and something must see its result.** A capability nothing reaches means a surface is missing.

- **Name the surface, not the actor.** "Tools", not "Agent". "Hooks", not "Host". One actor can use several surfaces, and one surface can serve several actors.
- **An actor with no surface of their own gets no file.** When someone only reaches the product through another actor, such as a user who only ever talks to an agent, their rules land where they belong: in primitives, in capabilities, and on the surface that serves them, as what it must always let them do.
- **What the product calls out to isn't an interface.** A model it asks for judgment, or a service it relies on, is something it depends on, not a surface the outside touches. Its rules go where its answers are used: what it may decide, in the primitive or capability that asks, and what's recorded about its answers, wherever records are kept.
- **One surface across many hosts is still one surface.** Tools served over MCP in one host and natively in another are still `TOOLS.md`. How each host provides it goes in a column of the table.

```markdown
# <Surface>

<What crosses here, who or what is on the other side, and what it is to the product.>

## <What passes>

| <Tool, hook, job, endpoint or screen> | <What it returns or does> |
|---|---|

## Invariants

- ...
```

- The table is the heart of the file: it names what crosses and what each thing does. Exact inputs and outputs belong to a later contract, and the file can say so.
- Use as many tables as the surface has parts. Group rows by what they're allowed to do, such as reading against changing.
- A row doesn't need a capability behind it. Small acts like listing or opening something live only in the table. When a row needs rules of its own, it has become a capability and gets a file.
- Interfaces are where naming an outside system is right, because the product has to meet it.
- Look for: what this side can and can't reach, what it's always able to ask for, what it's never asked to do or learn, how failure looks from this side, and what stays the same across every host or instance of it.

### 6. Walk the Map

Read the whole map once, as a builder who has nothing else.

- **Links.** When a file means another file's subject specifically, its first mention is a relative link, and every link resolves. An everyday use of the same word needs no link. Files written early can point forward now that the later ones exist.
- **Behaviour sits with its primitive.** No capability's invariants are all about one primitive. If one's are, fold them in and delete the capability.
- **Few rules per idea.** A file past ten invariants, or one whose invariants don't share an idea, is where an abstraction is missing or wrong. Look there before adding anything else.
- **Primitives are used.** Each one is read or changed by at least one capability or surface. If not, it isn't a primitive or something is missing.
- **Capabilities are reachable.** Each one is started and observed through at least one surface.
- **The pitch matches the core.** Each promise in `INTENT.md` is held up by at least one invariant, and you can name the invariants that stop the failure sentence from coming true. What the primitives turned out to make distinctive is what `INTENT.md` leads with. If the most interesting things in the map aren't in the pitch, redraft the pitch with the user.
- **Timing is said.** Each invariant that ties primitives together says whether it holds at every moment or catches up, and by when.
- **Nothing collides.** No two invariants contradict. The same rule appearing in two files says the same thing.
- **Nothing is built in.** Search for storage, libraries, algorithms, protocols and file layouts. Apply the swap test to each.
- **Decisions are recorded.** Every fork the user settled has a record. Each record's Confirmation names invariants that exist. No map file links into `docs/decisions/`, and no map file explains itself with a "because" that belongs in a record.
- **The guess test.** Ask: "If this map were all I had, what would I have to guess that the user would mind me guessing wrong?" Each answer is a missing invariant or a question for the user.

Fix what you can settle and ask about the rest in one round. Adding or removing a file changes a layer's list, so it goes to the user with the questions.

### 7. Hand Off

Report the product in one sentence, the names in each layer, the decisions recorded, anything deferred, any question left open, and any default you took that the user didn't explicitly confirm. Don't paste the files back.

Then stop. Don't write a plan, pick a stack, scaffold a repository or start building, and don't offer to as part of this skill.

## Changing the Map

When the map exists, it is the product's, so a new feature changes the map in place. There is no per-feature file.

1. Read the whole map and its decisions first. If `docs/README.md` or the files from `templates/decisions/` are missing, copy them. If one differs from its template, show the user the difference and ask before replacing it. If the map has no records but its history is written down somewhere, such as a plan, commit messages or research notes, offer to backfill records after the fact.
2. Say which layer the change lands in. Most features add or change a primitive. A change to `INTENT.md` means it's becoming a different product, so confirm that explicitly.
3. Propose the change as a list of files added, edited and removed, and get agreement.
4. Edit in place. Files say what is true now, with no history, dates or "previously". When a primitive is replaced, delete its file and fix every link to it. A change that reverses a recorded decision gets a new record that supersedes the old one.
5. Walk the map again (Step 6). A change to a primitive usually touches the capabilities and interfaces that mention it.

## Writing Style

- Plain, everyday words. Describe the product the way you'd explain it to someone who will never see the code.
- Short declarative sentences in the present tense. "Never", "always", "only", "exactly one".
- One idea per bullet. Bold the few statements in each file the product would be a different product without, and no others.
- Concrete examples in quotes beat abstractions: "is your favorite color still pink?", "wait, why?".
- Use colons and commas for asides, not dashes.
- Files are short: a description and four to ten invariants. A file that keeps growing is usually two things, or a thing still missing its idea.
- No status, no dates, no rationale, no references to this conversation. Rationale goes in a record.

## Common Mistakes

- **Writing a specification.** User stories, acceptance criteria, task lists and phases describe work to do. The map describes what stays true once the work is done.
- **Letting implementation in.** A database, a framework or a wire format in an invariant closes a decision the map exists to leave open.
- **Leaving the core open.** A map that lets each build decide what the core abstractions are gets code that works and has no shape. The primitives are the one part of the design the map fixes.
- **Splitting behaviour from its thing.** A capability for each thing a primitive does to itself, such as record, revise and forget, leaves the primitives as bare data and invites a layer of services over them. Fold the behaviour into the primitive.
- **Listing features.** "Supports search" says what's there. An invariant says what must hold about it.
- **Too many primitives.** Separate primitives for things that differ only in origin or circumstance produce a build with needless types. Collapse them.
- **One primitive for two meanings.** The reverse of too many primitives. A word that means different things in different parts of the product, merged into one file, gives a build one bloated type that serves every part badly.
- **A view as a primitive.** How a thing appears in one moment is produced by a capability or a surface. Making it a primitive doubles the thing.
- **Interfaces named after people.** "User" and "Agent" name who's there, not what they touch, and the rules inside end up belonging elsewhere. Name the surface.
- **A dependency as an interface.** A model or service the product calls is not a surface. Its rules belong with the work that uses it.
- **Capabilities with nobody to call them.** Writing interfaces last makes it easy to skip the check that each capability is reachable.
- **Leaving judgment unbounded.** "The agent decides when to ask" with no fixed guarantee beside it gives a build that may never ask, or always ask.
- **Stating the obvious.** Invariants any capable builder would honour anyway bury the ones that matter.
- **Quizzing the user.** A long list of open questions hands the drafting back to them. Draft, then ask about what's left.
- **Guessing instead of asking.** The opposite error: settling something only the user knows because asking felt like friction.
- **Carrying a prototype's lessons across as mechanism.** Keep what turned out to matter. Leave how it was solved.
- **Rationale in the map.** A "because" in a map file is a record waiting to be written. Move it.
- **Recording a setting.** A record about a value or a name goes stale the first time someone tunes it. Record the pattern it belongs to, or nothing.
- **Inventing the road not taken.** A rejected option nobody weighed makes a record look complete and makes it wrong. Write `TODO`.
- **Editing a record.** Reversing a decision in place erases why it was made. Supersede it.
- **Going past the map.** Suggesting a stack, a schema or a first milestone is out of scope even when it seems helpful.

## Key Principles

- **The core is the design.** The primitives are the abstractions every build shares. Get them right and the rest follows. Leave them open and each build invents its own.
- **The map is enough, and no more.** Enough for a capable builder to get the core right, and open about everything around it.
- **Invariants over instructions.** Say what must stay true and let the builder find the way there. Statements about what holds survive a rewrite. Statements about how to build it don't.
- **Each layer earns the next.** Intent gives the question, primitives give the words and the behaviour, capabilities do what no one thing does, and interfaces make it all reachable.
- **Same kind of thing.** The most valuable move at the primitive layer is noticing that several things are one.
- **One idea, many rules.** The best primitive has an idea its rules follow from.
- **Judgment next to a guarantee.** Wherever someone decides, state what is fixed regardless.
- **Failure is visible.** For every primitive, capability and interface, the map says what the product does when it can't do its job. It never goes quiet.
- **What and why live apart.** The map changes in place and carries no history. The decisions only grow, and explain the map without repeating it.
- **The product owns the map.** It changes when the product changes, in place, and it carries no trace of the features that shaped it.
- **Rediscovery is fine.** A build from this map will relearn details an earlier attempt already knew. That cost is accepted, in exchange for a map that fixes only what matters.
