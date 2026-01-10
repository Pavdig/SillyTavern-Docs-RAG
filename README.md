# SillyTavern Documentation (RAG-Ready)

This repository contains an automated workflow to mirror, process, and sanitize the official [SillyTavern Documentation](https://github.com/SillyTavern/SillyTavern-Docs). 

The goal is to create a "flat" and clean set of Markdown files optimized for ingestion into AI apps like **Open WebUI** or other RAG (Retrieval-Augmented Generation) knowledge bases.

## 📂 Usage

### Option 1: Direct Download
1.  Go to the Code tab -> **Download ZIP**.
2.  Extract the `SillyTavern-Docs-RAG` folder.
3.  Upload the files directly to Knowledge Base of your AI app.

### Option 2: Git clone
You can clone this repo to keep a local copy with:

```bash
git clone https://github.com/Pavdig/SillyTavern-Docs-RAG.git
```

To update the files later, just run:
```bash
git pull
```

## 🚀 How it Works

A GitHub Actions workflow runs automatically on a schedule to perform the following steps:

1.  **Clone Upstream:** Pulls the latest documentation from the official [SillyTavern-Docs repository](https://github.com/SillyTavern/SillyTavern-Docs).
2.  **Flatten Structure:** converts the nested folder structure into flat filenames to preserve context.
    *   *Example:* `docs/installation.md` &rarr; `SillyTavern_docs_installation.md`
3.  **Sanitize Content:** Cleans the Markdown files to remove noise that confuses AI models:
    *   Removes "Redirect" file stubs.
    *   Strips YAML front matter (metadata headers).
    *   Removes Docusaurus-specific tags (admonitions like `!!!warning`).
    *   Removes images and relative links while keeping the anchor text.
4.  **Publish:** Pushes the processed files to the `docs/` directory in this repository.

## 📝 Credits

*   Original Documentation: [SillyTavern Team](https://github.com/SillyTavern/SillyTavern-Docs)
