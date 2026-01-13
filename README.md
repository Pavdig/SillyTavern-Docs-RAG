![Update Status](https://github.com/Pavdig/SillyTavern-Docs-RAG/actions/workflows/update_docs.yml/badge.svg)
# SillyTavern Documentation (RAG-Ready)

This repository hosts an automated pipeline that mirrors, processes, and sanitizes the official [SillyTavern Documentation](https://github.com/SillyTavern/SillyTavern-Docs). 

The goal is to create a "flat" and clean set of Markdown files optimized for ingestion into AI apps like **Open WebUI** or other RAG (Retrieval-Augmented Generation) knowledge bases.

## 📥 Downloads

Go to the **[Releases Page](https://github.com/Pavdig/SillyTavern-Docs-RAG/releases)** to download the latest RAG-ready ZIP package.

## 🚀 How it Works

The automation pipeline runs on a schedule to ensure this repo stays in sync with SillyTavern documentation development.

### 1. The Build Process
*   **Clone Upstream:** Pulls the latest docs from the official repository.
*   **Flatten Structure:** Converts nested folders into flat filenames to preserve context for the AI.
    *   *Example:* `SillyTavern-Docs/Installation/Windows.md` → `SillyTavern_Installation_Windows.md`
*   **Sanitize Content:** Removes noise that confuses LLMs:
    *   Redirect stubs
    *   YAML front matter (metadata headers)
    *   Docusaurus-specific tags (admonitions like `!!!warning`)
    *   Images and relative links (keeping anchor text)

### 2. The Update Cycle (CI/CD)
1.  **Check:** The bot checks the official docs for changes ever hour.
2.  **Stage:** If updates are found, they are processed and pushed to the `staging` branch.
3.  **Notify:** A **Pull Request** is automatically opened (or updated) with the changelog.
4.  **Release:** When the PR is merged into `main`, a GitHub Release is automatically published with a date-stamped ZIP file.

## 📂 Usage for RAG

1.  Download the latest `.zip` from **Releases**.
2.  Extract the files.
3.  Upload them to your RAG Knowledge Base (e.g., Open WebUI "Knowledge").

## 📝 Credits

*   Original Documentation: [SillyTavern Team](https://github.com/SillyTavern/SillyTavern-Docs)
