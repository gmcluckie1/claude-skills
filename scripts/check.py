"""Smoke test: every skill has valid frontmatter; eval cases are in sync with gen.py."""
import pathlib
import subprocess
import sys
import tempfile

root = pathlib.Path(__file__).resolve().parent.parent
errors = []
for skill in sorted((root / "skills").glob("*/SKILL.md")):
    lines = skill.read_text().splitlines()
    if lines[0] != "---" or "---" not in lines[1:]:
        errors.append(f"{skill}: missing frontmatter")
        continue
    head = lines[1:lines.index("---", 1)]
    keys = {l.split(":", 1)[0] for l in head if ":" in l}
    if not {"name", "description"} <= keys:
        errors.append(f"{skill}: frontmatter needs name and description")
    if f"name: {skill.parent.name}" not in head:
        errors.append(f"{skill}: name must match directory")
gen = root / "evals/marketing/gen.py"
before = sorted(p.read_text() for p in (gen.parent / "evals").rglob("*.md"))
subprocess.run([sys.executable, str(gen)], check=True)
after = sorted(p.read_text() for p in (gen.parent / "evals").rglob("*.md"))
if before != after:
    errors.append("eval cases out of date; run evals/marketing/gen.py")
for e in errors:
    print(e)
sys.exit(1 if errors else 0)
