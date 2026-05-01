#!/usr/bin/env python3
"""
Package Instagram Carousel Generator skill for distribution.
"""

import argparse
import json
import shutil
import sys
import tarfile
from pathlib import Path


def package_skill(skill_dir: Path, output_path: Path):
    """Package skill directory as .skill archive."""
    skill_dir = skill_dir.resolve()
    output_path = output_path.resolve()

    if not skill_dir.exists():
        print(f"Error: Skill directory not found: {skill_dir}")
        return 1

    # Validate structure
    if not (skill_dir / "SKILL.md").exists():
        print("Error: SKILL.md not found")
        return 1

    if not (skill_dir / "_meta.json").exists():
        print("Error: _meta.json not found")
        return 1

    # Load meta for filename
    meta = json.loads((skill_dir / "_meta.json").read_text())
    skill_name = skill_dir.name

    if not output_path.name.endswith(".skill"):
        output_path = output_path / f"{skill_name}.skill"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Create tar archive
    with tarfile.open(output_path, "w:gz") as tar:
        tar.add(skill_dir, arcname=skill_name)

    print(f"Packaged skill: {output_path}")
    print(f"  - Version: {meta.get('version', 'unknown')}")
    print(f"  - ID: {meta.get('id', 'unknown')}")

    return 0


def main():
    parser = argparse.ArgumentParser(description="Package skill for distribution")
    parser.add_argument("skill_dir", type=Path, help="Skill directory to package")
    parser.add_argument("--output", type=Path, help="Output .skill file path")
    args = parser.parse_args()

    output = args.output or Path(".")

    return package_skill(args.skill_dir, output)


if __name__ == "__main__":
    sys.exit(main())
