import re
import os
import shutil

# === CONFIGURATION ===
SOURCE_DIR = "comparison/raw_source"
OUTPUT_DIR = "comparison/sanitized_test"
ROOT_DIR = "comparison/raw_source"

# Standard MkDocs admonition types to strip
ADMONITION_TYPES = [
    "note", "abstract", "info", "tip", "success", "question", 
    "warning", "failure", "danger", "bug", "example", "quote", "callout"
]

def replace_link(match, file_path):
    text = match.group(1)
    url = match.group(2)
    
    # 1. Ignore external links
    if url.startswith('http') or url.startswith('www'):
        return f'{text} ({url})'
    
    # 2. Remove anchors and query strings
    url = url.split('#')[0].split('?')[0]
    
    # 3. RESOLVE PATHS
    current_dir = os.path.dirname(file_path)
    
    try:
        if url.startswith('/') or url.startswith('\\'):
            # Root-relative path
            abs_path = os.path.normpath(os.path.join(ROOT_DIR, url.lstrip('/\\')))
        else:
            # Relative path
            abs_path = os.path.normpath(os.path.join(current_dir, url))
        
        rel_path = os.path.relpath(abs_path, ROOT_DIR)
    except ValueError:
        return text 

    if rel_path.startswith('..'):
        return text 
    
    # 4. Flatten the relative path
    flat_name = rel_path.replace(os.sep, '_')
    
    # Fix: Handle links without extensions
    filename, ext = os.path.splitext(flat_name)
    if not ext:
        flat_name += '.md'
    
    # 5. Handle specific extensions
    if flat_name.endswith('.yaml'):
        flat_name = flat_name.replace('.yaml', '-yaml.md')
    
    if flat_name and (flat_name.endswith('.md') or flat_name.endswith('.json')):
        # We keep the Markdown link structure here for the docs/ folder.
        # The internal link removal happens later in generate_rag_bundle.py
        return f'[{text}](SillyTavern_{flat_name})'
    
    return text

def replace_image(match):
    return '' 

def replace_admonition(match):
    # Capture everything after !!!
    content = match.group(1).strip()
    if not content:
        return ''
    
    # 1. Remove the admonition type if it exists (e.g. "warning")
    first_word = content.split(' ')[0]
    if first_word.lower() in ADMONITION_TYPES:
        content = content[len(first_word):].strip()
        
    if not content:
        return ''

    # 2. Check if content is a Table or Code Block
    # If it starts with | (Table) or ``` (Code), return it RAW (no bold)
    if content.startswith('|') or content.startswith('```'):
        return f"\n{content}\n"

    # Otherwise, bold the title/text
    return f"\n**{content}**\n"

def process_files():
    # --- Clear output dir but keep .gitkeep ---
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    else:
        for filename in os.listdir(OUTPUT_DIR):
            if filename == ".gitkeep":
                continue
            
            file_path = os.path.join(OUTPUT_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    print(f"Scanning nested files in '{SOURCE_DIR}'...")
    
    skipped_count = 0
    processed_count = 0

    for root, dirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            # 1. Explicitly ignore .gitkeep
            if filename == ".gitkeep":
                continue

            # 2. Skip non-Markdown files
            if not filename.endswith(".md"):
                continue

            file_path = os.path.join(root, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # === 1. SKIP REDIRECT STUBS ===
                if "This page has been moved to" in content:
                    skipped_count += 1
                    continue

                # === 2. REMOVE FRONT MATTER ===
                content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

                # === 3. REMOVE SCREENSHOTS SECTION ===
                # This removes everything from '## Screenshots' up to '## Installation Requirements'
                content = re.sub(r'## Screenshots.*?(?=## Installation Requirements)', '', content, flags=re.DOTALL)

                # === 4. APPLY REGEX LOGIC ===
                
                # Images
                content = re.sub(r'!\[((?:[^][]+|\[[^][]*\])*)\]\s*\(([^)]*)\)', replace_image, content)
                
                # Links
                content = re.sub(r'\[([^]]+)\]\(([^)]+)\)', lambda m: replace_link(m, file_path), content)
                
                # Admonitions
                content = re.sub(r'^\s*(?:!!!|:::)\s*(.*)$', replace_admonition, content, flags=re.MULTILINE)
                
                # Ghost Tables
                content = re.sub(r'^\s*\|[\s|]+\|\s*$', '', content, flags=re.MULTILINE)

                # === 5. CLEANUP WHITESPACE ===
                content = re.sub(r'<br\s*\/?>', '', content, flags=re.IGNORECASE)
                content = re.sub(r'\n{3,}', '\n\n', content)

                # Determine output path
                rel_path_from_root = os.path.relpath(file_path, SOURCE_DIR)
                flat_name = rel_path_from_root.replace(os.sep, '_')
                output_filename = f"SillyTavern_{flat_name}"
                output_path = os.path.join(OUTPUT_DIR, output_filename)

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                processed_count += 1
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"Done. Processed {processed_count} files. Skipped {skipped_count} redirects.")

if __name__ == "__main__":
    process_files()