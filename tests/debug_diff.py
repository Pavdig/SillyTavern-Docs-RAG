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