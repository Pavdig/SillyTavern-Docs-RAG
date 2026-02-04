![Update Status](https://github.com/Pavdig/SillyTavern-Docs-RAG/actions/workflows/update_docs.yml/badge.svg)
# SillyTavern Documentation (RAG-Ready)

This repository hosts an automated pipeline that mirrors, processes, and sanitizes the official [SillyTavern Documentation](https://github.com/SillyTavern/SillyTavern-Docs). 

The goal is to create a "flat" and clean set of Markdown files optimized for ingestion into AI apps like **Open WebUI** or other RAG (Retrieval-Augmented Generation) knowledge bases.

It now also generates **single-file bundles** (`llms.txt` and `llms.json`) for easy drag-and-drop context in LLMs like ChatGPT or Claude.

## 📥 Downloads

Go to the **[Releases Page](https://github.com/Pavdig/SillyTavern-Docs-RAG/releases)** to download the latest RAG-ready ZIP package.

## 🛠️ Usage for RAG

### Option 1: Knowledge Bases (e.g., Open WebUI)
1.  Download the latest `.zip` from **Releases**.
2.  Extract the `docs/` folder.
3.  Upload the files to your RAG Knowledge Base.

### Option 2: Single-File Context (ChatGPT, Claude, etc.)
1.  Download the `.zip` or view the files in the repo root.
2.  Use **`llms.txt`**: Drag and drop this single file into a "Project" or long-context chat window. It contains the *entire* documentation in one readable text file.
3.  Use **`llms.json`**: For programmatic ingestion or tools that support JSON knowledge dumps.

## ⚙️ How it Works

The automation pipeline runs on a schedule to ensure this repo stays in sync with SillyTavern documentation development.

### 1. The Build Process
*   **Clone Upstream:** Pulls the latest docs from the official repository.
*   **Flatten Structure:** Converts nested folders into flat filenames to preserve context for the AI.
    *   *Example:* `SillyTavern-Docs/Installation/Windows.md` → `SillyTavern_Installation_Windows.md`
*   **Sanitize Content:** Removes noise that confuses LLMs:
    *   **Redirect stubs:** Files that just say "Page moved" are removed.
    *   **Front Matter:** Metadata headers (`---`) are stripped.
    *   **Admonitions:** Tags like `!!!warning` are stripped, but **titles and text are preserved** (formatted as bold text).
    *   **Images:** Removed entirely to reduce token usage.
    *   **Ghost Tables:** Empty table artifacts left by images are cleaned up.
    *   **Links:** Context-aware rewriting of relative links to match flattened filenames.
*   **Generate Bundles:** Aggregates all processed files into:
    *   `llms.txt`: A single concatenated file with headers and original URLs (optimized for logical reading order).
    *   `llms.json`: A structured JSON array containing source filenames, real URLs, and content.

### 2. The Update Cycle (CI/CD)
1.  **Check:** The bot checks the official docs for changes every hour.
2.  **Sync:** If updates are found, they are processed and pushed to a temporary `docs-sync` branch.
3.  **Notify:** A **Pull Request** is automatically opened (or updated) with the changelog.
4.  **Release:** When the PR is merged into `main`, a GitHub Release is automatically published with a date-stamped ZIP file containing the docs and bundles.

## 🎖️ Credits

*   [Original Documentation](https://github.com/SillyTavern/SillyTavern-Docs): [SillyTavern Team](https://github.com/SillyTavern)