#!/usr/bin/env python3
"""Stage the authored tutorial Markdown and publishable assets for MkDocs."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "_docs"

EXCLUDED_DIRECTORIES = {
    ".git",
    ".github",
    ".githooks",
    "_docs",
    "_site",
    "scripts",
    "__pycache__",
}
EXCLUDED_FILES = {
    ".gitignore",
    "AGENTS.md",
    "ABLETON-TUTORIAL-IDEAS.MD",
    "ABLETON_TUT_REFS.md",
    "LICENSE",
    "mkdocs.yml",
    "requirements.txt",
    "SHREDSCOPES-TUTORIAL-IDEAS.MD",
}
PUBLISHABLE_SUFFIXES = {
    ".css",
    ".gif",
    ".jpeg",
    ".jpg",
    ".md",
    ".mp3",
    ".mp4",
    ".ogg",
    ".png",
    ".svg",
    ".webm",
    ".webp",
}


def is_publishable(source: Path) -> bool:
    relative = source.relative_to(ROOT)
    return (
        source.is_file()
        and not any(part in EXCLUDED_DIRECTORIES for part in relative.parts)
        and source.name not in EXCLUDED_FILES
        and source.suffix.lower() in PUBLISHABLE_SUFFIXES
    )


def main() -> None:
    if DESTINATION.exists():
        shutil.rmtree(DESTINATION)

    for source in ROOT.rglob("*"):
        if not is_publishable(source):
            continue

        relative = source.relative_to(ROOT)
        if relative == Path("README.md"):
            relative = Path("tutorial-catalog.md")

        destination = DESTINATION / relative
        destination.parent.mkdir(parents=True, exist_ok=True)

        if source.name == "index.md":
            contents = source.read_text(encoding="utf-8")
            destination.write_text(
                contents.replace("(README.md)", "(tutorial-catalog.md)"),
                encoding="utf-8",
            )
        else:
            shutil.copy2(source, destination)


if __name__ == "__main__":
    main()
