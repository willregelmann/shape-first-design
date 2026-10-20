"""Checks that this repository keeps the invariants in its map (docs/).

Each check is named after the invariant it holds and names the map file the
invariant comes from. Run from anywhere: python3 checks/check_map.py
Exits 1 if any check fails. Standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SKILLS = ROOT / "skills"
SHARED = SKILLS / "shared"
LINK = re.compile(r"\]\(([^)\s]+)\)")
CHECKS = []


def check(fn):
    CHECKS.append(fn)
    return fn


def layer_files() -> list[Path]:
    return sorted(p for d in ("primitives", "capabilities", "interfaces")
                  for p in (DOCS / d).glob("*.md"))


def invariants(path: Path) -> list[str]:
    text = path.read_text()
    if "## Invariants" not in text:
        return []
    section = text.split("## Invariants", 1)[1].split("\n## ", 1)[0]
    return [l for l in section.splitlines() if l.startswith("- ")]


@check
def copies_match_their_templates():
    """docs/interfaces/DOCS.md: the README is copied word for word."""
    template = SHARED / "templates" / "README.md"
    projects = [DOCS] + sorted((ROOT / "evals" / "fixtures").glob("*/docs"))
    return [f"{(docs / 'README.md').relative_to(ROOT)} differs from {template.relative_to(ROOT)}"
            for docs in projects
            if not (docs / "README.md").exists() or (docs / "README.md").read_bytes() != template.read_bytes()]


@check
def every_link_resolves():
    """docs/interfaces/DOCS.md: every link between map files resolves (and the skills' links too)."""
    bad = []
    files = list(DOCS.rglob("*.md")) + [p for p in (ROOT / "README.md", ROOT / "AGENTS.md") if p.exists()] + [
        p for p in SKILLS.rglob("*.md") if "templates" not in p.parts]  # templates link once copied
    for p in files:
        text = re.sub(r"```.*?```", "", p.read_text(), flags=re.S)  # examples in code blocks
        for target in LINK.findall(text):
            target = target.split("#", 1)[0]
            if not target or re.match(r"[a-z]+:", target):
                continue
            if not (p.parent / target).resolve().exists():
                bad.append(f"{p.relative_to(ROOT)} -> {target}")
    return bad


@check
def every_map_file_except_the_intent_has_invariants():
    """docs/interfaces/DOCS.md: every map file except the intent is a description followed by invariants."""
    return [f"{p.relative_to(ROOT)} has no invariants" for p in layer_files() if not invariants(p)]


@check
def a_files_rules_stay_few():
    """docs/primitives/PRIMITIVE.md: a primitive's rules stay few (the shared rules: four to ten per file)."""
    return [f"{p.relative_to(ROOT)} has {len(invariants(p))} invariants"
            for p in layer_files() if len(invariants(p)) > 10]


@check
def each_skill_says_when_it_loads():
    """docs/interfaces/SKILLS.md: each skill's description says when it loads."""
    bad = []
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        head = skill.read_text().split("---", 2)[1]
        name = re.search(r"^name:\s*(\S+)", head, re.M)
        desc = re.search(r"^description:\s*(.+)", head, re.M)
        if not name or name.group(1) != skill.parent.name:
            bad.append(f"{skill.relative_to(ROOT)}: name doesn't match its folder")
        if not desc or not re.search(r"\buse (when|for)\b", desc.group(1)):
            bad.append(f"{skill.relative_to(ROOT)}: description doesn't say when it loads")
    return bad


@check
def each_capability_is_started_by_exactly_one_skill():
    """docs/interfaces/SKILLS.md: each capability is started by exactly one skill."""
    table = (DOCS / "interfaces" / "SKILLS.md").read_text().split("## Skills", 1)[1].split("\n## ", 1)[0]
    starts: dict[str, list[str]] = {}
    bad = []
    for row in table.splitlines():
        cells = [c.strip() for c in row.strip("|").split("|")]
        m = re.fullmatch(r"`([\w-]+)`", cells[0]) if len(cells) >= 2 else None
        if not m:
            continue
        if not (SKILLS / m.group(1) / "SKILL.md").exists():
            bad.append(f"the table names {m.group(1)}, which isn't a skill")
        for cap in re.findall(r"\(\.\./capabilities/(\w+)\.md\)", cells[1]):
            starts.setdefault(cap, []).append(m.group(1))
    for cap in (p.stem for p in (DOCS / "capabilities").glob("*.md")):
        if len(starts.get(cap, [])) != 1:
            bad.append(f"{cap} is started by {starts.get(cap, [])}")
    return bad


@check
def shared_rules_have_one_source():
    """docs/interfaces/SKILLS.md: a rule both skills rely on has one source, and neither restates it."""
    markers = ["What Counts as an Invariant", "Writing Style", "1. **Always.**",
               "**Naming a technology.**", "**Across primitives.**", "| **Owner** |"]
    bad = []
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        text = re.sub(r"<!-- shared:start.*?<!-- shared:end -->", "", skill.read_text(), flags=re.S)
        bad += [f"{skill.relative_to(ROOT)} restates {m!r}" for m in markers if m in text]
        if "](#shared-rules)" not in text:
            bad.append(f"{skill.relative_to(ROOT)} doesn't point at the shared rules")
    return bad


@check
def each_skill_carries_the_shared_rules_unchanged():
    """docs/interfaces/SKILLS.md: shared rules have one source (skills/shared/), carried inline by each skill."""
    sys.path.insert(0, str(ROOT / "checks"))
    from sync_shared import with_block
    return [f"{p.relative_to(ROOT)} doesn't carry skills/shared/ as it is; run checks/sync_shared.py"
            for p in sorted(SKILLS.glob("*/SKILL.md")) if with_block(p.read_text()) != p.read_text()]


@check
def each_eval_case_carries_an_exact_copy_of_its_fixture():
    """docs/capabilities/AUDIT.md: judged runs start from the same project every time."""
    source = ROOT / "evals" / "fixtures" / "chores"
    want = {p.relative_to(source): p.read_bytes() for p in source.rglob("*") if p.is_file()}
    bad = []
    for setup in sorted((ROOT / "evals").glob("*/setup.sh")):
        if "/fixture" not in setup.read_text():
            continue
        copy = setup.parent / "fixture"
        have = {p.relative_to(copy): p.read_bytes() for p in copy.rglob("*") if p.is_file()} \
            if copy.exists() else {}
        if have != want:
            bad.append(f"{copy.relative_to(ROOT)} differs from evals/fixtures/chores; run checks/sync_shared.py")
    return bad


@check
def the_comparison_arms_differ_only_in_what_they_are_given():
    """evals: the A/B/C comparison gives every arm the same task, the same brief and the same graders."""
    arms = sorted((ROOT / "evals").glob("compare-*/"))
    if len(arms) != 3:
        return [f"expected three comparison arms, found {len(arms)}"]

    def body(p: Path) -> str:
        return p.read_text().split("---", 2)[2]

    bad = []
    for name, get in (("prompt", lambda a: body(a / "prompt.md")),
                      ("brief", lambda a: (a / "workspace" / "README.md").read_text()),
                      ("graders", lambda a: {g.name: g.read_bytes() for g in (a / "graders").glob("*.md")})):
        if len({repr(get(a)) for a in arms}) != 1:
            bad.append(f"the arms have different {name}s")
    return bad


@check
def agent_instructions_point_at_the_map():
    """docs/interfaces/DOCS.md: a project's agent instructions point at its map."""
    found = [p for p in (ROOT / "AGENTS.md", ROOT / "CLAUDE.md")
             if p.exists() and "docs/README.md" in p.read_text()]
    return [] if found else ["neither AGENTS.md nor CLAUDE.md points at docs/README.md"]


def main() -> int:
    failed = 0
    for fn in CHECKS:
        problems = fn()
        print(f"{'PASS' if not problems else 'FAIL'}  {fn.__name__}")
        for p in problems:
            print(f"      {p}")
        failed += bool(problems)
    print(f"\n{len(CHECKS) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
