# Gemini Agent Guidance

This document provides guidance for the Gemini agent to effectively work within the `dspy_llmstxt_generator` repository.

---

## 1. Project Overview

- **Name:** `dspy_llmstxt_generator`
- **Purpose:** A tool leveraging DSPy (Stanford’s declarative self-improving Python framework) to generate standardized `llms.txt` documentation for GitHub repositories. It converts a repository's structure and documentation into a concise, LLM-friendly Markdown format.
- **Core Task:** The primary feature is a DSPy pipeline that generates coherent, structured `llms.txt` files. This involves prompt programming with declarative supervision, few-shot learning, and metric-based compilation.

---

## 2. Project Structure

- **`analysis/`**: Contains DSPy signatures for repository analysis.
- **`docs/`**: Holds documentation and tutorials.
- **`scripts/`**: Includes utility and build scripts.
- **`tests/`**: Contains unit and integration tests.
- **`pyproject.toml`**: Defines project dependencies and build configurations.
- **`README.md`**: Provides a comprehensive project overview.
- **`step-*.py` files**: These files represent the sequential pipeline for generating the `llms.txt` file.

---

## 3. Build & Test Workflow

Use the following commands to build and validate changes:

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run linting and formatting checks
flake8 .
black --check .
```

---

## 4. Development Guidelines & Key DSPy Concepts

- **Supervision:** Use `dspy.Example` to provide supervised input-output pairs for compiling and improving the pipeline.
- **Signatures:** Define precise signatures with specific `InputField` and `OutputField` annotations. Avoid overly broad fields.
- **Metrics:** Implement human-readable accuracy or coherence metrics for evaluation and compilation.
- **Compilation:** Use `dspy.BootstrapFewShot` to compile the pipeline and improve text quality based on defined metrics.
- **Extensibility:** Consider integrating `dspy.ChainOfThought` for more complex generation tasks in the future.
- **LLM Variability:** Be aware that LLM behavior can differ significantly across providers (e.g., OpenAI, Anthropic). Test changes accordingly.
