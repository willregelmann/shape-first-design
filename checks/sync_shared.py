"""Copies the shared rules and templates into each skill.

skills/shared/ is the one source. Each skill carries an exact copy in its own
shared/ folder, because an agent may only be allowed to read inside the skill
it loaded. Run after editing skills/shared/; check_map.py fails until you do.
"""

from __future__ import annotations

import shutil
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "skills"
SOURCE = SKILLS / "shared"

for skill in sorted(p.parent for p in SKILLS.glob("*/SKILL.md")):
    copy = skill / "shared"
    if copy.exists():
        shutil.rmtree(copy)
    shutil.copytree(SOURCE, copy)
    print(f"copied {SOURCE.relative_to(SKILLS.parent)} -> {copy.relative_to(SKILLS.parent)}")
