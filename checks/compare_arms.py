"""Measures the A/B/C comparison (evals/compare-*) from the code each run built.

The judged graders give pass or fail per run. The thesis is about how much
structure there is, so this counts it: classes beyond the map's, synonyms for
the map's words, lines of code, and how alike the runs of one arm are.

Run the arms with --keep-temp. Each kept run is a folder of its own (the run
prints where, under /private/tmp/e-*) with the built project in sealed/home/cwd,
which is made unreadable after the run. Point this at those folders, or at a
folder holding them; it opens them with chmod, as the run's warning says to.
A run's arm is read from what it was given: a map (docs/primitives) is C, a
spec (docs/SPEC.md) is B, and neither is A. Standard library only.

    python3 checks/compare_arms.py /private/tmp/e-*
"""

from __future__ import annotations

import ast
import os
import re
import sys
from itertools import combinations
from pathlib import Path

MAP_CLASSES = {"Chore", "Household"}
SYNONYMS = re.compile(r"\b(task|todo|job|family|member|resident|flatmate|roommate|user)s?\b", re.I)
ARMS = {"a": "A brief only", "b": "B prose spec", "c": "C map and skill"}


def measure(src: Path) -> dict:
    code = [p for p in sorted(src.glob("*.py")) if p.name != "__init__.py"]
    classes, core_classes, exceptions, members, loc, syn = set(), set(), set(), set(), 0, 0
    for p in code:
        text = p.read_text()
        loc += sum(1 for l in text.splitlines() if l.strip() and not l.strip().startswith("#"))
        if p.name == "chores.py":
            syn += len(SYNONYMS.findall(re.sub(r'""".*?"""', "", text, flags=re.S)))
        for node in ast.walk(ast.parse(text)):
            if isinstance(node, ast.ClassDef):
                classes.add(node.name)
                if node.name.endswith(("Error", "Failed")) or any(
                        ast.unparse(b).endswith(("Exception", "Error")) for b in node.bases):
                    exceptions.add(node.name)
                if p.name == "chores.py":
                    core_classes.add(node.name)
                if node.name in MAP_CLASSES:
                    members |= {f"{node.name}.{n.name}" for n in node.body
                                if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")}
    extra = {c for c in classes if c not in MAP_CLASSES and c not in exceptions}
    extra_core = {c for c in core_classes if c not in MAP_CLASSES and c not in exceptions}
    return {"classes": classes, "extra": extra, "extra_core": extra_core, "members": members, "loc": loc, "synonyms": syn}


def jaccard(a: set, b: set) -> float:
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def open_kept(kept: Path) -> Path | None:
    """The built project inside a kept run, opened up, or None if the run built no core."""
    for d in (kept, kept / "sealed"):
        if d.exists():
            os.chmod(d, 0o700)
    cwd = kept / "sealed" / "home" / "cwd"
    return cwd if (cwd / "src" / "chores.py").exists() else None


def arm_of(cwd: Path) -> str:
    if (cwd / "docs" / "primitives").exists():
        return "c"
    return "b" if (cwd / "docs" / "SPEC.md").exists() else "a"


def main(roots: list[Path]) -> int:
    runs: dict[str, list[dict]] = {k: [] for k in ARMS}
    skipped = []
    for kept in sorted(r for root in roots for r in ([root] if (root / "out").exists() else sorted(root.glob("e-*")))):
        cwd = open_kept(kept)
        if cwd is None:
            skipped.append(kept.name)
            continue
        runs[arm_of(cwd)].append(measure(cwd / "src"))
    if skipped:
        print(f"no core built in: {', '.join(skipped)}\n")
    if not any(runs.values()):
        print("no built projects found (did you run with --keep-temp?)")
        return 1
    print(f"{'arm':18} {'runs':>4} {'extra (core)':>13} {'extra (all)':>12} {'synonyms':>9} {'lines':>6} "
          f"{'same classes':>13} {'same members':>13}")
    for k, name in ARMS.items():
        rs = runs[k]
        if not rs:
            print(f"{name:18} {0:>4}")
            continue
        pairs = list(combinations(rs, 2))
        sim = lambda key: sum(jaccard(a[key], b[key]) for a, b in pairs) / len(pairs) if pairs else float("nan")
        mean = lambda key: sum(r[key] if isinstance(r[key], int) else len(r[key]) for r in rs) / len(rs)
        print(f"{name:18} {len(rs):>4} {mean('extra_core'):>13.1f} {mean('extra'):>12.1f} {mean('synonyms'):>9.1f} {mean('loc'):>6.0f} "
              f"{sim('classes'):>13.2f} {sim('members'):>13.2f}")
    print("\nextra = classes beyond Chore and Household (not counting exceptions), in src/chores.py (core) or all of src/. "
          "same classes/members = mean pairwise Jaccard similarity between runs of one arm.")
    for k, name in ARMS.items():
        for i, r in enumerate(runs[k], 1):
            print(f"  {name} run {i}: {sorted(r['classes'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main([Path(a) for a in sys.argv[1:]] or [Path("/private/tmp")]))
