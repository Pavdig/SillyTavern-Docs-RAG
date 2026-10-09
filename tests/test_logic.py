#!/usr/bin/env python3
"""Local comparison helper: sanitize comparison/raw_source into comparison/sanitized_test.

Uses the real logic from scripts/sanitize_docs.py (no pasted copy), so results
always match what the CI pipeline produces. Use debug_diff.py afterwards to
inspect before/after changes.
"""
import argparse
import logging
import shutil
import sys
from pathlib import Path

# Find the repo root (the folder that contains scripts/sanitize_docs.py),
# so this file works from the repo root or from a subfolder like tests/.
ROOT = Path(__file__).resolve().parent
while not (ROOT / "scripts" / "sanitize_docs.py").exists():
    if ROOT == ROOT.parent:
        raise SystemExit("Could not find scripts/sanitize_docs.py above this file.")
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "scripts"))

from sanitize_docs import make_flat_output_name, sanitize_text  # noqa: E402

# === CONFIGURATION ===
# Paths are relative to the folder you run the script from (same as the old version).
DEFAULT_SOURCE = "comparison/raw_source"
DEFAULT_OUTPUT = "comparison/sanitized_test"


def process_files(source_dir: Path, output_dir: Path) -> int:
    global SOURCE_DIR, OUTPUT_DIR
    SOURCE_DIR, OUTPUT_DIR = source_dir.resolve(), output_dir.resolve()

    if not SOURCE_DIR.is_dir():
        print(f"Source folder not found: {SOURCE_DIR}")
        print("Run this from the folder that contains comparison/raw_source, or pass --source.")
        return 1

    if OUTPUT_DIR.exists():
        for item in OUTPUT_DIR.iterdir():
            if item.name == ".gitkeep":
                continue
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    skipped_count = 0

    for file_path in sorted(SOURCE_DIR.rglob("*.md")):
        content = file_path.read_text(encoding="utf-8")

        if "This page has been moved to" in content:
            skipped_count += 1
            continue

        sanitized = sanitize_text(content, file_path, SOURCE_DIR)
        rel_path = file_path.relative_to(SOURCE_DIR)
        output_path = OUTPUT_DIR / f"SillyTavern_{make_flat_output_name(rel_path)}"
        output_path.write_text(sanitized, encoding="utf-8")
        processed_count += 1

    if processed_count == 0 and skipped_count == 0:
        print(f"No .md files found under {SOURCE_DIR}")
        return 1

    print(f"Done. Processed {processed_count} files. Skipped {skipped_count} redirects.")
    print(f"Output: {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sanitize a raw docs copy for before/after comparison.")
    parser.add_argument("--source", default=DEFAULT_SOURCE, help="Folder with the raw upstream docs")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Folder for the sanitized result")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    raise SystemExit(process_files(Path(args.source), Path(args.output)))
