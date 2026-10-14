"""Writes the shared rules and templates into each skill, and the eval fixture into each case.

skills/shared/ is the one source. Each SKILL.md carries it inline, between
marker comments, because an agent may not be allowed to read any file beside
the skill it loaded: a judged run refused even the skill's own folder. Eval
cases can't share a fixture through a link either, so each case with a
setup.sh carries its own copy of evals/fixtures/chores/. Run after editing
either source; check_map.py fails until you do.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
SHARED = SKILLS / "shared"
START, END = "<!-- shared:start (generated from skills/shared/ by checks/sync_shared.py; edit there) -->", "<!-- shared:end -->"


def shared_block() -> str:
    parts = [START, "", "## Shared Rules", "",
             "These rules come from `skills/shared/RULES.md`, the one source both skills share.", ""]
    rules = (SHARED / "RULES.md").read_text().split("\n", 1)[1].strip()  # drop its title
    parts += [re.sub(r"^## ", "### ", rules, flags=re.M), "", "## Templates", "",
              "Copy these into a project word for word, at the path each one names."]
    for t in sorted((SHARED / "templates").rglob("*.md")):
        rel = t.relative_to(SHARED / "templates")
        dest = "docs/" + str(rel)
        parts += ["", f"### `{dest}`", "", "````markdown", t.read_text().rstrip("\n"), "````"]
    parts += ["", END]
    return "\n".join(parts) + "\n"


def with_block(text: str) -> str:
    block = shared_block()
    if START in text:
        return text[:text.index(START)] + block + text[text.index(END) + len(END) + 1:]
    return text.rstrip("\n") + "\n\n" + block


if __name__ == "__main__":
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        skill.write_text(with_block(skill.read_text()))
        print(f"wrote the shared rules into {skill.relative_to(ROOT)}")
    for setup in sorted((ROOT / "evals").glob("*/setup.sh")):
        copy = setup.parent / "fixture"
        if copy.exists():
            shutil.rmtree(copy)
        shutil.copytree(ROOT / "evals" / "fixtures" / "chores", copy)
        print(f"copied evals/fixtures/chores -> {copy.relative_to(ROOT)}")
