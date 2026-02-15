import os
import json
import re

# Configuration
SOURCE_DIR = "docs"
OUTPUT_TXT = "llms.txt"
OUTPUT_JSON = "llms.json"
OUTPUT_MD = "llms.md"

# ---------------------------------------------------------
# Helper: Define logical sort order
# ---------------------------------------------------------
def get_sort_weight(filename):
    """
    Returns a tuple (priority_score, filename) to force a logical reading order.
    Lower numbers = appears earlier in the file.
    """
    name = filename.lower()
    
    # 1. Readme / Intro
    if "readme" in name: return (1, name)
    
    # 2. Installation & Updates
    if "installation" in name: return (2, name)
    
    # 3. Usage (The main meat of the docs)
    if "usage" in name: return (3, name)
    
    # 4. Administration (Config, etc)
    if "administration" in name: return (4, name)
    
    # 5. Extensions
    if "extensions" in name: return (5, name)
    
    # 6. Contributor info
    if "contributors" in name: return (6, name)
    
    # 7. Everything else (License, etc)
    return (99, name)

# ---------------------------------------------------------
# Main Execution
# ---------------------------------------------------------
def generate_bundles():

    # --- Create a Header ---
    combined_text = f"""# SILLYTAVERN DOCUMENTATION
# Context: This file contains the full, flattened documentation for SillyTavern.
# Structure: Each section below corresponds to a file from the official docs.

"""
    
    json_data = []

    # Get files
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".md")]
    
    # Sort files using our custom weight function
    files.sort(key=get_sort_weight)

    print(f"Found {len(files)} files. Processing...")

    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
            
            # --- STRIP LINKS FOR BUNDLE ---
            # Replaces [Link Name](SillyTavern_File.md) with just "Link Name"
            # Note: External links have already been converted to "Name (URL)" in the sanitize step.
            content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
            
            # --- PREPARE SECTION NAME ---
            # Remove .md extension for cleaner headers
            section_name = filename.replace(".md", "")
            
            # --- Text Bundle Construction ---
            # Separator using H1 style for section distinction
            combined_text += f"# SECTION: {section_name}\n\n"
            combined_text += content + "\n\n"
            
            # --- JSON Bundle Construction ---
            json_data.append({
                "SECTION": section_name,
                "content": content
            })
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # Write llms.txt
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write(combined_text)
    print(f"✅ Generated {OUTPUT_TXT} (Ordered by section)")

    # Write llms.md
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(combined_text)
    print(f"✅ Generated {OUTPUT_MD} (Markdown copy)")

    # Write llms.json
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    print(f"✅ Generated {OUTPUT_JSON} (Clean content)")

if __name__ == "__main__":
    generate_bundles()