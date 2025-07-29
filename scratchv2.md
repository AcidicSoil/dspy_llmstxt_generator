You:

project tutorial - https://dspy.ai/tutorials/llms\_txt\_generation repo - https://github.com/AcidicSoil/dspy\_llmstxt\_generator

ChatGPT:

```markdown
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

For all conventions, reference the project’s CLAUDE.md, INITIAL.md, and PRPs/templates for philosophy and validation loop patterns.

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

---

## AGENTS.md

## Purpose & Scope

This document defines **project-wide agent development standards** for all agent-based workflows in *context-engineering-intro*.
**Goal:** Make all agents modular, context-aware, validation-first, and fully explainable—enabling any contributor to understand, extend, and validate agent logic without hidden context or ambiguous patterns.

---

## Project Philosophy

Agent development in this project must always reflect these core rules:

-   **Context is King:** No agent, tool, or prompt may assume implicit context; all dependencies, docs, and edge cases must be made explicit.

-   **Validation Loops:** Every agent or tool must have test artifacts and explicit validation steps—never mark an agent complete without passing all validation gates.

-   **Structure Mirrors Intent:** Modular code and documentation; agent artifacts should reflect their responsibilities and validation requirements.

-   **Explainability & Traceability:** All agent logic, config, and outputs must be understandable by a mid-level dev. Every file and pattern must explain *why*, not just *what*.

-   **Progressive Success:** Always start simple—build, validate, and extend. Avoid “big bang” rewrites or unvalidated abstractions.

-   **Avoid Anti-Patterns:** No over-engineering, no skipped validation, no hidden gotchas. All edge cases and failure points must be called out, not swept under the rug.


Reference and inherit all conventions from CLAUDE.md, INITIAL.md, PRPs/templates, and related context files. Any agent- or project-specific overrides must be explicitly documented.

---

## Coding Standards

**Global Conventions (Language-Agnostic):**

-   **Modularity:**

    -   Each agent is defined in its own file/module (`agent.py`, `agent.ts`, etc.), separated from tools, models, and prompts.

    -   Feature-specific logic belongs in modules/folders reflecting intent.

-   **Information Density:**

    -   Avoid boilerplate. Prefer meaningful docstrings/comments and explicit parameter naming.

    -   Never include unused imports, placeholder functions, or empty abstractions.

-   **Strict Input Validation:**

    -   All agent/tool parameters must be validated (e.g., Pydantic models, Zod schemas).

    -   Never accept raw user input without validation.

-   **Docstrings & Comments:**

    -   Every function/method/class requires a docstring explaining *what* and *why* (reference project-wide conventions, e.g., Google or reStructuredText style).

    -   Inline comments must clarify *why* complex or non-obvious code is present, not just *what*.

-   **Validation Gates:**

    -   Every agent must have parallel test/validation artifacts (unit, edge, failure case).

    -   CI/lint/test patterns must be easy to run and documented alongside implementation.

-   **No Boilerplate:**

    -   All code and documentation must be adapted from real, working patterns in the examples or PRPs/templates—never copied verbatim or left generic.

-   **Never Assume Context:**

    -   If context is missing or ambiguous, *require* clarification (raise an error or file a TODO for the contributor).


---

## Project-Specific Conventions

-   **Referencing Context:**

    -   Every agent, tool, or pattern must list the key context files, PRPs, or examples it is based on (see: CLAUDE.md, PRPs/templates/prp\_base.md).

-   **Validation Artifacts:**

    -   Every agent or tool requires validation/test artifacts, living in parallel to the implementation (e.g., `/tests` for Python, `/__tests__` for TypeScript).

    -   Each new pattern must call out gotchas and document critical failure cases at the same level as the implementation code.

-   **Extension and Override Rules:**

    -   If you extend a base pattern, document both the *original* and the *customized* logic, with rationale and validation steps.

-   **Documentation Synchronization:**

    -   If the implementation is updated, *update the documentation and references* at the same time. Never allow agent logic to diverge from documented patterns.


---

## AI-Assisted Workflow

**How to iterate with LLMs and agent-based tooling:**

-   **Context Window Discipline:**

    -   Every LLM/agent call must specify which docs/examples/PRPs are in context—never guess. If any input is missing, *ask* for it or halt with a TODO.

-   **Validation Gates:**

    -   All AI-generated artifacts (code, docs, configs) must pass validation steps (lint, tests, reference checks) before merging or shipping.

-   **Explicit PRP/Doc References:**

    -   LLM-driven agents must always reference which PRP(s), templates, or examples informed their logic or output.

-   **Progressive Enhancement:**

    -   Start with minimal, validated implementations—iterate with additional context, requirements, and test cases, not with speculative complexity.

-   **No Implicit Context:**

    -   Never allow agents or LLMs to assume “standard” context; require explicit listing of all dependencies and sources.


---

## Testing & CI

-   **Validation Loop Philosophy:**

    -   Each agent/tool must have:

        -   At least one unit test (expected/happy path)

        -   At least one edge case

        -   At least one known failure/error case

    -   Tests must be runnable via CI or documented scripts; always include lint/type checks where supported.

-   **CI Enforces Completeness:**

    -   CI pipeline (or its documented equivalent) must check for:

        -   Syntax/lint errors

        -   Type checking (if supported by language)

        -   Test coverage (minimum: all new features/agents)

        -   Reference/documentation up-to-date

-   **Failure Handling:**

    -   If a test, lint, or validation fails, fix it before merging or release—do not allow “skip and fix later.”

-   **Validation Gates in Docs:**

    -   All validation/test commands must be listed in the relevant doc (README, agent docstring, or PRP).


---

## Documentation Requirements

-   **Full Documentation:**

    -   Every agent/context file must have:

        -   Rationale for its existence, referencing the PRP/template or example it derives from

        -   Edge cases and gotchas, documented in the same file (not in a separate “gotchas.md”)

        -   All source docs/PRPs/examples referenced (with relative paths or URLs)

        -   Enough context for a future maintainer to understand *why* this agent exists, *how* it works, and *what* to watch out for

-   **Change Traceability:**

    -   Every time logic or context changes, update references and rationale in documentation. Never leave code and context out of sync.

-   **Progressive Documentation:**

    -   Start with minimal docs, validate with real examples/tests, then enhance. Do not write speculative docs for unimplemented features.


---

*For examples of these patterns, see CLAUDE.md, PRPs/templates/prp\_base.md, and PRPs/EXAMPLE\_multi\_agent\_prp.md. All agent code and docs must pass the validation loops described above, and clearly list sources, edge cases, and rationale for future maintainers.*

