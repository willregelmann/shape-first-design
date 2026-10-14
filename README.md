# Invariant-Driven Development

[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An agent skill for starting a new product with a map: what it's for, what it's made of, what it does and where the outside touches it, written as statements that must always hold.

Capable models write excellent code but rarely beautiful structure. Structure comes from the abstractions, so the map's main job is to find the few things the product is made of, chosen so its behaviour follows from them, and fix them as the core every build shares. It's meant to be enough, on its own, for a capable agent to build a working product of the right shape, with the stack and everything around the core left open. It lives with the product, not with a feature.

## Skills

| Skill | What it does |
|-------|-------------|
| [map-project](skills/map-project/SKILL.md) | Interviews you about a new product and writes its map under `docs/`, one layer at a time, then stops |

## Install

This repository is a Claude Code plugin and its own single-plugin marketplace:

```
/plugin marketplace add willregelmann/invariant-driven-development
/plugin install invariant-driven-development@invariant-driven-development
```

The skill activates when you say something like "let's start a new project, I want to build X", or you can invoke it by name.

## The Map

```
docs/
  README.md                 how to read the map, copied from a standard template
  INTENT.md                 what it's for, and what would make it pointless
  primitives/<NOUN>.md      what it's made of, and how each thing behaves: the core of the code
  capabilities/<VERB>.md    what it does that no one thing does
  interfaces/<SURFACE>.md   where the outside touches it: TOOLS, HOOKS, JOBS, API
  decisions/NNNN-*.md       why it has this shape, as MADR records
```

Each file is a short description followed by a list of invariants. An invariant is true at every moment, in every build of the product:

| Not an invariant | Invariant |
|------------------|-----------|
| "Memories are rows in a SQLite table" | "A memory's content is never edited. When it turns out to be wrong, a new memory supersedes it." |
| "Listeners can ask questions" | "No question is dropped. Every question is answered, put off out loud, or declined out loud." |

The map says what holds. The decision records say why: each fork you settle during the interview is written down with the options that were turned down, so a later agent can find the reason before undoing it.

The skill drafts and you correct. It asks only what you alone know: who it's for, what would make it pointless, what it must work with, and which of two reasonable shapes you want.

## What It Doesn't Do

It stops at the map. Choosing a stack, writing a plan and writing code are separate work. It's for products that don't exist yet, before any architectural decision has been made.

## Structure

```
.claude-plugin/
  plugin.json        # plugin manifest
  marketplace.json   # single-plugin marketplace, so the repo installs itself
skills/
  map-project/
    SKILL.md
    templates/
      README.md          # copied unchanged into every map
      decisions/         # 0000 conventions record and MADR template, copied unchanged
```

No build system, no dependencies. The artifacts are markdown files.

## License

MIT
