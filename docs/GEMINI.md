## GEMINI.md

## Overview

This file defines **context file standards and best practices** for any “Gemini”-style LLM or agent orchestrator in the *context-engineering-intro* project. It is **repo-agnostic** and documents how to structure, validate, and adapt context for any orchestration or LLM provider, not just Google Gemini.
**Philosophy:** All conventions in this file are derived from the project’s core principles:
- *Context is King*: Always make all context explicit, dense, referenceable, and traceable.
- *Validation Loops*: Every context/config must be testable, preferably automated.
- *Structure Mirrors Intent*: The file structure and organization should reflect the *purpose* and *validation* needed.
- *Explainability & Traceability*: Every pattern, config, or field must be understandable by a mid-level contributor.
- *Progressive Success*: Start simple, validate, and evolve context as new needs arise.
- *Avoid Anti-Patterns*: Never over-engineer, never skip validation, never assume context, always call out edge cases.

For all conventions, reference the project’s AGENTS.md, INITIAL.md, and PRPs/templates for philosophy and validation loop patterns.

---

## Context File Structure

A Gemini (or general LLM orchestrator) context file must be:

- **Modular**: Context for models, prompts, agents, validation, and gotchas should be in clear, separate sections.
- **Explicit**: All sources (URLs, example files, external docs) must be listed and referenced—never assume any context.
- **Traceable**: Every config, default, or override must specify *why* it exists (add a `reason:` or comment).
- **Validation-Ready**: Include test artifacts or validation steps that prove context coverage—validation gates, test prompts, edge cases.
- **Extensible**: Custom sections or overrides must document both the *default* and *customized* behavior, and *why*.
- **Reference-rich**: List all key files, PRPs, and examples (by path or URL) in a “References” or “Sources” section.

**Recommended Section Layout:**

- `# Overview`
- `# Inputs` (docs, example files, PRPs, relevant configs)
- `# Context Sections` (model config, system prompts, agent patterns, validation steps, gotchas)
- `# References`
- `# Customization & Overrides` (describe any non-default logic)
- `# Validation Loop` (step-by-step validation/test process)

---

## Example Configuration

```yaml
# context-gemini.yaml

overview: |
  Context for Gemini LLM orchestration in a context engineering project.
  Explicitly documents all inputs, sources, and validation steps for reproducibility.

inputs:
  - file: PRPs/templates/prp_base.md         # Core PRP template rules
  - file: CLAUDE.md                          # Global context engineering rules
  - file: examples/                          # Agent/example reference folder
  - url: https://ai.pydantic.dev/models/     # (Example) Model provider docs

model_config:
  provider: "gemini"
  model: "gemini-1.5-pro"
  api_key_env: "GEMINI_API_KEY"
  reason: "Default to Gemini Pro for broad capability; override via env for testing."
  fallback_models:
    - openai:gpt-4o
    - anthropic:claude-3-sonnet
  validation: "Model providers and keys must be set via .env, validated on load."

system_prompt:
  file: prompts/gemini_system.md
  reason: "Centralizes prompt for reproducible agent behavior."

agent_patterns:
  - file: examples/agent/agent.py
  - file: PRPs/EXAMPLE_multi_agent_prp.md

validation_loop:
  - step: "Run model selection self-test using provided validation gate."
  - step: "Check prompt rendering with test context; confirm match to expected system prompt."
  - step: "Run agent with test input and compare to golden outputs/examples."
  - step: "Verify that all references resolve and inputs exist."
  - step: "Iteratively update as edge cases and new requirements are found."

gotchas:
  - "Never hardcode API keys—must be read from env and validated at startup."
  - "If context file omits a reference, prompt for clarification before proceeding."
  - "Document all fallback models and failover logic explicitly."
  - "Explicitly validate system prompt integrity and encoding."

references:
  - CLAUDE.md
  - PRPs/templates/prp_base.md
  - PRPs/EXAMPLE_multi_agent_prp.md
  - examples/agent/agent.py

customization:
  - "To extend for non-Gemini providers, add provider blocks as new sections, documenting validation logic for each."
  - "For project-specific overrides, document them in a separate section with explicit rationale."
```

---

## Best Practices for Customization

-   **Always Document Rationale:** For every override, default, or extension, *state why*—avoid context drift.

-   **Provider-Agnostic Sections:** Abstract provider config (`provider:`, `model:`) so new LLMs can be added without restructuring the file.

-   **Validation Steps as First-Class Citizens:** Never just describe configuration—always include a way to *prove* it works (e.g., self-test scripts, lint gates, golden prompt validation).

-   **Explicit Gotchas:** List any provider or context-engineering quirks. Example: Gemini’s streaming API edge cases, API rate limits, max context window.

-   **References Must be Up-to-Date:** If you add a new agent, prompt, or PRP, update the references section—never assume the context file is self-maintaining.


---

## Troubleshooting

**Common Issues and How to Address Them:**

-   **Context Omitted:** If a required source or doc is missing, *fail validation* and prompt the contributor to add it. Do not guess or proceed.

-   **Ambiguity in Provider Config:** If model/provider config is unclear, check `.env.example` and prompt for explicit environment variable setup.

-   **Missing Validation:** If there are no validation steps/gates, add at least:

    -   Syntax/lint check on the config file.

    -   Reference resolution for every input/source.

    -   Self-test agent run with example input.

-   **Edge Cases Unhandled:** Add a “gotchas” section to document and validate known edge cases—reference both code and docs.

-   **Unexplained Customization:** If any section overrides defaults, but rationale is missing, *require* a comment or field explaining *why*.

-   **No Traceability:** Always update the “References” section when adding new context sources; validation should fail if out of sync.


---

*For further patterns, see CLAUDE.md and PRPs/templates/prp\_base.md in this project.*