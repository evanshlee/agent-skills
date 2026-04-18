#!/usr/bin/env python3
"""Copy canonical skills into Claude Code plugin packages.

Run this from the repository root after editing anything under skills/.
Each directory under skills/ must have a matching plugin package under plugins/.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PLUGINS_DIR = ROOT / "plugins"


def iter_skill_names() -> list[str]:
    if not SKILLS_DIR.exists():
        raise SystemExit(f"Missing skills directory: {SKILLS_DIR}")
    return sorted(path.name for path in SKILLS_DIR.iterdir() if path.is_dir())


def sync_skill(skill_name: str) -> None:
    source = SKILLS_DIR / skill_name
    plugin_root = PLUGINS_DIR / skill_name
    destination = plugin_root / "skills" / skill_name

    if not plugin_root.exists():
        raise SystemExit(f"Missing Claude plugin package for skill: {skill_name}")

    if destination.exists():
        shutil.rmtree(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print(f"synced {source.relative_to(ROOT)} -> {destination.relative_to(ROOT)}")


def main() -> None:
    for skill_name in iter_skill_names():
        sync_skill(skill_name)


if __name__ == "__main__":
    main()
