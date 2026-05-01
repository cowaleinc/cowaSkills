#!/usr/bin/env python3
"""
Validate Instagram Carousel Generator skill structure and content.
"""

import json
import sys
from pathlib import Path


def validate_skill(skill_dir: Path) -> list[str]:
    """Validate skill directory structure and content."""
    errors = []

    # Check SKILL.md exists and has proper frontmatter
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md not found")
        return errors

    content = skill_md.read_text(encoding="utf-8")

    # Check frontmatter
    if not content.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter (---)")

    if "name:" not in content[:500]:
        errors.append("Frontmatter must contain 'name' field")

    if "description:" not in content[:1000]:
        errors.append("Frontmatter must contain 'description' field")

    # Check _meta.json
    meta = skill_dir / "_meta.json"
    if not meta.exists():
        errors.append("_meta.json not found")
    else:
        try:
            meta_data = json.loads(meta.read_text())
            if "id" not in meta_data:
                errors.append("_meta.json must contain 'id' field")
            if "version" not in meta_data:
                errors.append("_meta.json must contain 'version' field")
        except json.JSONDecodeError:
            errors.append("_meta.json is not valid JSON")

    # Check required scripts exist
    scripts_dir = skill_dir / "scripts"
    if not scripts_dir.exists():
        errors.append("scripts/ directory not found")
    else:
        export_script = scripts_dir / "export_slides.py"
        if not export_script.exists():
            errors.append("scripts/export_slides.py not found")

    return errors


def main():
    skill_dir = Path(__file__).parent.parent

    print(f"Validating skill at: {skill_dir}")
    print("-" * 50)

    errors = validate_skill(skill_dir)

    if errors:
        print("VALIDATION FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("VALIDATION PASSED")
    print("  - SKILL.md with proper frontmatter")
    print("  - _meta.json with id and version")
    print("  - export_slides.py script present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
