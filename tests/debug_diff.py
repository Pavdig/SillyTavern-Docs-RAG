import os
import re
import difflib

# === CONFIGURATION ===
RAW_DIR = "comparison/raw_source"         # Nested source folders
SANITIZED_DIR = "comparison/sanitized_test" # Flattened output files
OUTPUT_FILE = "debug_report.md"

# We only care about changes involving these patterns
INTERESTING_PATTERNS = [
    r"!\[",           # Images
    r"\]\(",          # Links
    r"!!!",           # Admonitions
    r":::",           # Admonitions
    r"<br",           # HTML tags
    r"\|.*\|",        # Tables
    r"\*\*",          # Bold text (admonition titles)
    r"## Screenshots" # DETECT SCREENSHOT REMOVAL
]

def is_interesting(text_lines):
    """Check if any line in the text block matches our patterns."""
    text = "".join(text_lines)
    for pattern in INTERESTING_PATTERNS:
        # Use DOTALL so we can match across lines if needed
        if re.search(pattern, text, flags=re.DOTALL):
            return True
    return False

def generate_report():
    print(f"Scanning nested files in '{RAW_DIR}'...")
    
    if not os.path.exists(RAW_DIR) or not os.path.exists(SANITIZED_DIR):
        print("Error: Directories not found. Check your paths.")
        return

    count = 0
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# Debug Comparison Report\n\n")
        out.write("> Source: Nested Folders | Output: Flattened Files\n\n")

        # Walk through the nested source directory
        for root, dirs, files in os.walk(RAW_DIR):
            for filename in files:
                if not filename.endswith(".md"):
                    continue

                # 1. Get the Raw Content
                raw_path = os.path.join(root, filename)
                with open(raw_path, "r", encoding="utf-8") as f:
                    raw_lines = f.readlines()

                # 2. Calculate the expected Flattened Filename
                # e.g. Administration/config.md -> SillyTavern_Administration_config.md
                rel_path = os.path.relpath(raw_path, RAW_DIR)
                flat_name = "SillyTavern_" + rel_path.replace(os.sep, "_")
                sanitized_path = os.path.join(SANITIZED_DIR, flat_name)

                # 3. Check if the sanitized file exists (it might have been skipped/redirect)
                if not os.path.exists(sanitized_path):
                    continue

                with open(sanitized_path, "r", encoding="utf-8") as f:
                    clean_lines = f.readlines()

                # 4. Compare
                matcher = difflib.SequenceMatcher(None, raw_lines, clean_lines)
                file_header_written = False

                for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                    if tag in ('replace', 'delete'):
                        old_segment = raw_lines[i1:i2]
                        new_segment = clean_lines[j1:j2]

                        if is_interesting(old_segment):
                            if not file_header_written:
                                out.write(f"\n## File: `{rel_path}` -> `{flat_name}`\n\n")
                                file_header_written = True
                                count += 1
                            
                            out.write("**1. Before (Source)**\n")
                            out.write("```markdown\n")
                            out.write("".join(old_segment).rstrip())
                            out.write("\n```\n")
                            
                            out.write("**2. After (Sanitized)**\n")
                            out.write("```markdown\n")
                            out.write("".join(new_segment).rstrip())
                            out.write("\n```\n")
                            out.write("---\n")

    print(f"Done! Found interesting changes in {count} files.")
    print(f"Report saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_report()

import unittest
from pathlib import Path
from unittest.mock import patch
import tempfile
import shutil
import sys
import os

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from sanitize_docs import (
    is_external_link,
    normalize_url,
    make_flat_output_name,
    resolve_relative_link,
    replace_link,
    replace_image,
    normalize_admonition_block,
    sanitize_admonitions,
    sanitize_text,
    collect_markdown_files,
)

class TestSanitizeDocs(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.root_dir = self.temp_dir / 'root'
        self.root_dir.mkdir()
        self.file_path = self.root_dir / 'test.md'

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_is_external_link(self):
        self.assertTrue(is_external_link('http://example.com'))
        self.assertTrue(is_external_link('https://example.com'))
        self.assertTrue(is_external_link('www.example.com'))
        self.assertTrue(is_external_link('//example.com'))
        self.assertFalse(is_external_link('relative/path'))
        self.assertFalse(is_external_link('#anchor'))

    def test_normalize_url(self):
        self.assertEqual(normalize_url('  http://example.com?query#frag  '), 'http://example.com')
        self.assertEqual(normalize_url('path/to/file.md'), 'path/to/file.md')

    def test_make_flat_output_name(self):
        rel_path = Path('dir/subdir/file.md')
        self.assertEqual(make_flat_output_name(rel_path), 'dir_subdir_file.md')
        rel_path = Path('file.yaml')
        self.assertEqual(make_flat_output_name(rel_path), 'file-yaml.md')
        rel_path = Path('file.json')
        self.assertEqual(make_flat_output_name(rel_path), 'file.json')
        rel_path = Path('file')
        self.assertEqual(make_flat_output_name(rel_path), 'file.md')

    def test_resolve_relative_link(self):
        root = self.root_dir
        file_path = root / 'subdir' / 'test.md'
        file_path.parent.mkdir(parents=True)
        # Create a target file
        target = root / 'other.md'
        target.write_text('content')
        resolved = resolve_relative_link('../other.md', file_path, root)
        self.assertEqual(resolved, 'other.md')

    def test_replace_link(self):
        root = self.root_dir
        file_path = root / 'test.md'
        match = type('Match', (), {'group': lambda self, i: ['text', 'http://example.com'][i-1]})()
        result = replace_link(match, file_path, root)
        self.assertEqual(result, 'text (http://example.com)')

    def test_replace_image(self):
        match = type('Match', (), {'group': lambda self, i: 'alt'})()
        self.assertEqual(replace_image(match), '')

    def test_normalize_admonition_block(self):
        lines = ['    content line']
        result = normalize_admonition_block('note', 'Title', lines)
        self.assertIn('**Note Title:**', result)

    def test_sanitize_admonitions(self):
        text = '::: note\ncontent\n:::\n'
        result = sanitize_admonitions(text)
        self.assertIn('**Note:**', result)

    def test_sanitize_text(self):
        content = '---\nfront: matter\n---\n## Screenshots\n![img](img.png)\n[link](file.md)\n'
        result = sanitize_text(content, self.file_path, self.root_dir)
        self.assertNotIn('---', result)
        self.assertNotIn('## Screenshots', result)
        self.assertNotIn('![img]', result)

    def test_collect_markdown_files(self):
        (self.root_dir / 'file.md').write_text('content')
        (self.root_dir / 'subdir').mkdir()
        (self.root_dir / 'subdir' / 'file2.md').write_text('content')
        files = collect_markdown_files(self.root_dir)
        self.assertEqual(len(files), 2)

if __name__ == '__main__':
    unittest.main()