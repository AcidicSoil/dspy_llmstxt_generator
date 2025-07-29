# AGENTS.md

This file provides guidance for OpenAI Codex (and similar coding agents) to safely and effectively work within the `dspy_llmstxt_generator` repository.

---

## 🧩 Project Overview

- **Name:** dspy_llmstxt_generator
- **Purpose:** A tool leveraging DSPy (Stanford’s declarative self-improving Python framework) to generate standardized `llms.txt` documentation for GitHub repositories, converting code/project structure into LLM‑friendly Markdown.
- **Key Features:**
  - Parses repository structure and README content
  - Runs DSPy modules to extract purpose, architecture, directories, etc.
  - Outputs a formatted `llms.txt` file per DSPy conventions :contentReference[oaicite:1]{index=1}

---

## 🗂️ Project Structure

- **`analysis/`**: DSPy signatures for repository analysis
- **`docs/`:** Documentation and tutorials
- **`scripts/`:** Utility and build scripts
- **`tests/`:** Unit and integration tests
- **`README.md`:** Full project overview
- **`pyproject.toml`:** Dependency and dev build config

---

## ⚙️ Build & Test Workflow

OpenAI Codex should follow these commands to build and validate changes:

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# (Optional) Linting/checks
flake8 .
black --check .
