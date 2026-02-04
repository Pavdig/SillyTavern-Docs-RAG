import os
import json

# Configuration
SOURCE_DIR = "docs"
OUTPUT_TXT = "llms.txt"
OUTPUT_JSON = "llms.json"
BASE_URL = "https://docs.sillytavern.app"

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
# Helper: Generate clean URL from flattened filename
# ---------------------------------------------------------
def generate_url(filename):
    # 1. Strip the artificial prefix added by the flattener
    clean_name = filename.replace("SillyTavern_", "")
    
    # 2. Remove extension
    clean_name = clean_name.replace(".md", "")
    
    # 3. Restore directory structure (underscore -> slash)
    path = clean_name.replace("_", "/")
    
    # 4. Lowercase (URLs are usually lowercase)
    path = path.lower()
    
    # 5. Handle special cases (index, readme)
    if path == "readme":
        path = ""  # Root URL
    elif path == "index":
        path = ""  # Root URL (if exists)
    elif path.endswith("/index"):
        path = path[:-6] # remove '/index' to point to the folder
        
    # Remove trailing slash if it exists (optional, but cleaner)
    path = path.rstrip("/")
    
    if path:
        return f"{BASE_URL}/{path}"
    else:
        return BASE_URL

# ---------------------------------------------------------
# Main Execution
# ---------------------------------------------------------
def generate_bundles():

    # --- Create a Header ---
    combined_text = f"""# SILlYTAVERN DOCUMENTATION
# Website: {BASE_URL}
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
            
            # Generate the Web URL
            web_url = generate_url(filename)

            # --- Text Bundle Construction ---
            combined_text += f"#{'='*30}\n"
            combined_text += f"# Filename: {filename}\n"
            combined_text += f"# URL: {web_url}\n"
            combined_text += f"#{'='*30}\n\n"
            combined_text += content + "\n\n"
            
            # --- JSON Bundle Construction ---
            json_data.append({
                "source": filename,
                "url": web_url,
                "content": content
            })
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # Write llms.txt
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write(combined_text)
    print(f"✅ Generated {OUTPUT_TXT} (Ordered by section)")

    # Write llms.json
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    print(f"✅ Generated {OUTPUT_JSON} (Corrected URLs)")

if __name__ == "__main__":
    generate_bundles()