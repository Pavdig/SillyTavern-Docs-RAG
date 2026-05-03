<!-- Badges -->
![Status](https://img.shields.io/badge/status-experimental-yellow)
![Update Status](https://github.com/Pavdig/SillyTavern-Docs-RAG/actions/workflows/update_docs.yml/badge.svg)
[![Last Commit](https://img.shields.io/github/last-commit/Pavdig/SillyTavern-Docs-RAG)](https://github.com/Pavdig/SillyTavern-Docs-RAG/commits/main)
[![GitHub Downloads](https://img.shields.io/github/downloads/Pavdig/SillyTavern-Docs-RAG/total.svg)](https://github.com/Pavdig/SillyTavern-Docs-RAG/releases)
[![GitHub Stars](https://img.shields.io/github/stars/Pavdig/SillyTavern-Docs-RAG)](https://github.com/Pavdig/SillyTavern-Docs-RAG/stargazers)

# SillyTavern Documentation (RAG-Ready)

> **Note:** This is a **Proof of Concept (PoC)** project initiated from [SillyTavern-Docs Issue #183](https://github.com/SillyTavern/SillyTavern-Docs/issues/183). It aims to solve the problem of "token noise" and nested directory parsing issues when ingesting SillyTavern documentation into RAG knowledge bases (like Open WebUI).

This repository hosts a fully automated pipeline that mirrors, processes, and sanitizes the official [SillyTavern Documentation](https://github.com/SillyTavern/SillyTavern-Docs).

The goal is to create a "flat" and clean set of Markdown files optimized for AI ingestion. It also generates **single-file bundles** (`llms.txt`, `llms.md`, and `llms.json`) for easy drag-and-drop context in LLMs like ChatGPT or Claude.

## 📥 Downloads

Go to the **[Releases Page](https://github.com/Pavdig/SillyTavern-Docs-RAG/releases)** to download the latest RAG-ready ZIP package.

## 🛠️ Usage for RAG

### Option 1: Knowledge Bases (e.g., Open WebUI)
1. Download the latest `.zip` from **Releases**.
2. Extract the `docs/` folder.
3. Upload the files to your RAG Knowledge Base.

### Option 2: Single-File Context (ChatGPT, Claude, etc.)
1. Download the `.zip` or view the files in the repo root.
2. Use **`llms.txt`** or **`llms.md`**: Drag and drop this single file into a "Project" or long-context chat window. It contains the *entire* documentation in one readable file. Both files are identical in content — `llms.md` is provided for tools that prefer a `.md` extension.
3. Use **`llms.json`**: For programmatic ingestion or tools that support JSON knowledge dumps.

## ⚙️ How it Works

The automation pipeline runs on a schedule to keep this repo in sync with SillyTavern documentation development — no manual intervention required.

### 1. The Build Process

#### Sanitization (`sanitize_docs.py`)
- **Clone Upstream:** Pulls the latest docs from the official repository.
- **Flatten Structure:** Converts nested folders into flat filenames to preserve context for the AI.
  - *Example:* `SillyTavern-Docs/Installation/Windows.md` → `SillyTavern_Installation_Windows.md`
- **Sanitize Content:** Removes noise that confuses LLMs:
  - **Redirect stubs:** Files that just say "Page moved" are skipped entirely.
  - **Front Matter:** Metadata headers (`---`) are stripped.
  - **Screenshots:** The entire "Screenshots" section is removed from files.
  - **Admonitions:** Tags like `!!!warning` and `:::tip` are stripped, but titles and body text are preserved.
  - **Images:** All image tags are removed entirely to reduce token usage.
  - **Internal links:** Resolved and rewritten to match the flat output filenames (e.g. `[text](../foo/bar.md)` → `[text](SillyTavern_foo_bar.md)`). Unresolvable links fall back to plain text.
  - **External links:** Converted to `Name (URL)` format.
  - **Empty table rows and `<br>` tags:** Cleaned up to reduce formatting noise.

#### Bundle Generation (`generate_rag_bundle.py`)
- **Sort:** Files are ordered logically for reading coherence — Readme → Installation → Usage → Administration → Extensions → Contributors → everything else.
- **Strip remaining links:** Any internal links still present after sanitization are reduced to plain text at the bundle stage.
- **Generate Bundles:** Aggregates all processed files into:
  - `llms.txt` / `llms.md` — identical single-file text bundles, one per extension.
  - `llms.json` — structured JSON with one entry per doc section.

### 2. The Update Cycle (CI/CD)

The pipeline is fully automated end-to-end:

1. **Check:** Every hour, the bot checks the official SillyTavern-Docs for changes.
2. **Process:** If updates are found, docs are sanitized and bundles are regenerated.
3. **Commit:** Changes are committed directly to `main` with a descriptive message linking back to the upstream source commit. If multiple updates happen in one day, commits are named `Sync: Docs Update YYYY-MM-DD`, `Sync: Docs Update YYYY-MM-DD - Update 2`, and so on.
4. **Release:** The commit to `main` automatically triggers a GitHub Release with a date-stamped ZIP file. Multiple releases in one day are tagged `release-Mon-DD-YYYY`, `release-Mon-DD-YYYY-update-2`, etc.
5. **No-op guard:** If the processed output is identical to what's already on `main`, nothing is pushed and no release is created.

## 🎖️ Credits

- [Original Documentation](https://github.com/SillyTavern/SillyTavern-Docs): [SillyTavern Team](https://github.com/SillyTavern)
