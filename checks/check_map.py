"""Checks that this repository keeps the invariants in its map (docs/).

Each check is named after the invariant it holds and names the map file the
invariant comes from. Run from anywhere: python3 checks/check_map.py
Exits 1 if any check fails. Standard library only.
"""

from __future__ import annotations

import re
import subprocess
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


def map_files() -> list[Path]:
    """The map's own files: everything in docs/ except the README and the records."""
    return sorted(p for p in DOCS.rglob("*.md")
                  if p.name != "README.md" and "decisions" not in p.relative_to(DOCS).parts)


def layer_files() -> list[Path]:
    return sorted(p for d in ("primitives", "capabilities", "interfaces")
                  for p in (DOCS / d).glob("*.md"))


def records() -> list[Path]:
    return sorted(p for p in (DOCS / "decisions").glob("*.md") if re.match(r"\d{4}-", p.name))


def invariants(path: Path) -> list[str]:
    text = path.read_text()
    if "## Invariants" not in text:
        return []
    section = text.split("## Invariants", 1)[1].split("\n## ", 1)[0]
    return [l for l in section.splitlines() if l.startswith("- ")]


@check
def copies_match_their_templates():
    """docs/interfaces/DOCS.md: the README, 0000 and the template are copied word for word."""
    projects = [DOCS] + sorted((ROOT / "evals" / "fixtures").glob("*/docs"))
    pairs = [pair for docs in projects for pair in
             [(docs / "README.md", SHARED / "templates" / "README.md")] + [
                 (docs / "decisions" / t.name, t)
                 for t in (SHARED / "templates" / "decisions").glob("*.md")]]
    return [f"{c.relative_to(ROOT)} differs from {t.relative_to(ROOT)}"
            for c, t in pairs if not c.exists() or c.read_bytes() != t.read_bytes()]


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
def the_map_never_links_to_a_record():
    """docs/primitives/DECISION.md: the map never links to a record."""
    return [f"{p.relative_to(ROOT)} links to {t}" for p in map_files()
            for t in LINK.findall(p.read_text()) if "decisions/" in t]


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
    markers = ["## What Counts as an Invariant", "## Writing Style", "1. **Always.**",
               "**Naming a technology.**", "**Across primitives.**", "## Words"]
    bad = []
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        text = skill.read_text()
        bad += [f"{skill.relative_to(ROOT)} restates {m!r}" for m in markers if m in text]
        if "](shared/RULES.md" not in text:
            bad.append(f"{skill.relative_to(ROOT)} doesn't point at the shared rules")
    return bad


@check
def each_skill_carries_an_exact_copy_of_the_shared_rules():
    """docs/interfaces/SKILLS.md: shared rules have one source (skills/shared/); each skill's copy matches it."""
    bad = []
    source = {p.relative_to(SHARED): p.read_bytes() for p in SHARED.rglob("*") if p.is_file()}
    for skill in sorted(p.parent for p in SKILLS.glob("*/SKILL.md")):
        copy = skill / "shared"
        have = {p.relative_to(copy): p.read_bytes() for p in copy.rglob("*") if p.is_file()} \
            if copy.exists() else {}
        if have != source:
            bad.append(f"{copy.relative_to(ROOT)} differs from skills/shared/; run checks/sync_shared.py")
    return bad


@check
def records_are_numbered_in_order():
    """docs/interfaces/DOCS.md: one record each, numbered in order from 0000."""
    nums = [int(p.name[:4]) for p in records()]
    return [] if nums == list(range(len(nums))) else [f"record numbers are {nums}"]


@check
def records_have_no_front_matter():
    """The 0000 record: records have no front matter; version control holds who and when."""
    return [f"{p.relative_to(ROOT)} doesn't start with its title"
            for p in records() if not p.read_text().startswith("# ")]


@check
def a_record_is_never_edited():
    """docs/primitives/DECISION.md: a record is never edited, except to add a Superseded-by line."""
    base = subprocess.run(["git", "-C", str(ROOT), "merge-base", "HEAD", "main"],
                          capture_output=True, text=True).stdout.strip()
    if not base:
        return []  # no main to compare with
    bad = []
    for p in records():
        rel = str(p.relative_to(ROOT))
        if subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", f"{base}:{rel}"],
                          capture_output=True).returncode:
            continue  # new since main
        diff = subprocess.run(["git", "-C", str(ROOT), "diff", "-U0", base, "--", rel],
                              capture_output=True, text=True).stdout
        changed = [l for l in diff.splitlines()
                   if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        if any(not re.fullmatch(r"\+Superseded by ADR-\d{4}\.|\+", l) for l in changed):
            bad.append(f"{rel} was edited")
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
