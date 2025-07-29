You:

DETAIL using ChatGPT { "prompt": "You are 'DocBot', an experienced open-source technical writer and software architect. Your task is to generate two markdown documentation files—\*\*GEMINI.md\*\* and \*\*AGENTS.md\*\*—tailored to a user-defined project, which will be provided during the initial query or start of the conversation. These instruction files must be adaptable to any project context (i.e., repo-agnostic) and should not assume a specific repository such as gemini-cli. Instead, use the user’s described project goals and structure to inform the content. For both files, follow the formatting, tone, and structural guidance outlined below, while aligning your content with the expectations detailed in the following resources: https://platform.openai.com/docs/codex/overview and https://gemini-cli.xyz/docs/en/cli/configuration#example-context-file-content-e-g-gemini-md. For \*\*AGENTS.md\*\*, include the following sections: (1) Purpose & Scope, (2) Project Philosophy, (3) Ask vs Code Modes (with examples), (4) Coding Standards (language-agnostic), (5) Project-Specific Conventions (replace Gemini-CLI specifics with those relevant to the user’s project), (6) AI-Assisted Workflow, (7) Testing & CI, (8) Documentation Requirements, (9) Security & Privacy, (10) Change Management, and (11) Appendix. Use inclusive second-person tone for human readers and imperative tone for Codex agents. All section headers should be H2 unless a deeper level is necessary. Start the file with a bold one-sentence TL;DR. Keep line lengths ≤ 100 characters. Use fenced code blocks for examples and block quotes for tips or warnings. Do not reuse wording verbatim from any existing style guide, but aim to capture the spirit of clear, actionable, concise rules. Return only the full markdown content of each file (\*\*GEMINI.md\*\* and \*\*AGENTS.md\*\*), with no extra commentary or enclosing code fences." }

ChatGPT:

Hello! I'm Lyra, your AI prompt optimizer. I transform vague requests into precise, effective prompts that deliver better results.
**What I need to know:**

-   **Target AI:** ChatGPT, Claude, Gemini, or Other

-   **Prompt Style:** DETAIL (I'll ask clarifying questions first) or BASIC (quick optimization)
    **Examples:**

-   "DETAIL using ChatGPT — Write me a marketing email"

-   "BASIC using Claude — Help with my resume"
    Just share your rough prompt and I'll handle the optimization!


---

Thanks for choosing **DETAIL with ChatGPT** — this is a **complex multi-file generation task** with advanced structure, formatting requirements, and dynamic project context. I’ll apply full optimization.

Before finalizing, I need to ask **3 quick clarifying questions** to tailor this prompt for maximum accuracy and flexibility:

---

### 🔍 Clarification Questions

1.  **User Project Input Format**
    How should the AI expect the user to define their project?
    *(E.g., as natural language description, structured JSON, a repo tree, etc.)*

2.  **Expected Tone Consistency Across Files**
    Do you want the same tone (inclusive second-person + imperative for agents) in both files, or should GEMINI.md have a more config/instructional flavor?

3.  **OpenAI vs Gemini CLI Alignment**
    Should the AI **mirror the Gemini-CLI style** and adapt its structure across contexts, or should it use only its high-level philosophy and not emulate any of its wording or formatting patterns?


---

Once you confirm or clarify, I’ll generate a refined version of your prompt with role-based framing, modular logic, and output specs fully embedded.

You:

Clarification Questions User Project Input Format How should the AI expect the user to define their project? (E.g., as natural language description, structured JSON, a repo tree, etc.) (any of the above, be flexible) Expected Tone Consistency Across Files Do you want the same tone (inclusive second-person + imperative for agents) in both files, or should GEMINI.md have a more config/instructional flavor? (give me examples of the output before finalizing so I can decide which is best for my situation) OpenAI vs Gemini CLI Alignment Should the AI mirror the Gemini-CLI style and adapt its structure across contexts, or should it use only its high-level philosophy and not emulate any of its wording or formatting patterns? (explain in detail to me what you mean by this before finalizing the instructions)

ChatGPT:

Great — thanks for the answers! Let’s go step-by-step to ensure the final optimized prompt is **tailored and flexible** for your needs.

---

## 🧠 Clarification Breakdown & Guidance

### 1\. **User Project Input Format — "Be flexible"**

✅ Understood. The AI should **accept natural language, JSON configs, repo trees**, or mixed input.
This will be reflected as a flexible input parser—checking for structure but not enforcing it.

---

### 2\. **Tone Consistency — Example Comparison**

Here are **two short sample intros** (for `GEMINI.md`) using different tones. You can choose one or mix elements:

#### 🟦 *Inclusive + Imperative Tone (matches `AGENTS.md`):*

> **TL;DR**: This file defines how to configure and guide Codex agents to assist your team effectively.
>
> Use this file to describe your goals, provide system context, and guide agent behavior. Be specific.
> Agents will read this file to determine intent, boundaries, and preferred workflows.

#### 🟨 *Config-Instructional Tone (more declarative/config-ish):*

> **TL;DR**: This file contains project-specific configuration and usage context for Codex agents.
>
> It outlines metadata, intent signals, system affordances, and behavioral instructions in markdown.
> This file is agent-readable but should also assist maintainers in evolving system expectations.

**➡️ Let me know which one you prefer**, or if you'd like a hybrid (e.g., agent-focused but neutral in tone).

---

### 3\. **Gemini CLI vs High-Level Philosophy — What I Meant**

You asked whether to **adapt the Gemini CLI doc style**, so here’s a breakdown of the two options:

#### Option A — *Mirror Gemini-CLI Style & Format*

-   Closely follow the [Gemini CLI's documentation structure](https://gemini-cli.xyz/docs/en/cli/configuration#example-context-file-content-e-g-gemini-md).

-   Emphasize sections like `intent`, `context`, and `behavioral examples` with specific markdown formatting.

-   Structure would lean toward: `## Intent`, `## System Goals`, `## User Affordances`, etc.

-   Might include formatted bullets like:

    ```md
    - intent: automate legacy system refactoring
    - constraints: must preserve database schema integrity
    ```


> ✅ Useful if your users are **familiar with Gemini CLI** or you're porting its philosophy to your own platform.

#### Option B — *Use Only High-Level Philosophy*

-   Emulate the *goals* of Gemini CLI: clarity, human-AI co-specification, system thinking — without mimicking their structure or headings.

-   Free to rename and reorganize sections as long as you maintain the **intent-driven**, AI-readable, user-aidable principles.


> ✅ Better if your tool or project **is not Gemini-based**, and you want a universal, adaptable style.

---

## ✅ Next Steps

Please confirm:

-   ✔️ Your **preferred tone** for `GEMINI.md` (Inclusive/Imperative vs Instructional)

-   ✔️ Whether to go with **Option A (structure mirroring)** or **Option B (philosophy only)**


Once I have that, I’ll finalize and deliver the **fully optimized prompt**.

You:

Option B — Use Only High-Level Philosophy (explain in detail what you mean by this by providing an example)

ChatGPT:

Excellent — you’ve chosen **Option B: Use Only High-Level Philosophy**, which gives you **maximum flexibility** across different projects while keeping the spirit of Gemini-CLI.

Let me break this down clearly and show a direct **before vs. after** to illustrate what this means in practice.

---

## 🧭 What “High-Level Philosophy Only” Means

We **don’t copy or mimic** Gemini CLI’s:

-   Section titles like `## Intent`, `## System Goals`, `## Task Templates`

-   Config-like formatting (e.g., YAML-flavored bulleted markdown)

-   Hard assumptions like CLI usage, shell-first workflows, or VSCode integration


Instead, we extract and reframe **the underlying purpose** of Gemini CLI, which is:

> "Help Codex-style agents collaborate with humans effectively by defining goals, boundaries, constraints, and tone—while ensuring documentation is readable by both parties."

---

## 📘 Example: GEMINI.md – Gemini-CLI vs High-Level Philosophy Style

### 🟥 Gemini-CLI Styled

```markdown
## Intent
Automate the process of migrating Python 2 code to Python 3 across multiple microservices.

## Context
These services interact with legacy APIs, so compatibility is critical.

## Affordances
- Agents can refactor code for syntax compatibility.
- Agents may update unit tests if required.

## Constraints
- Do not remove any logging statements.
- All changes must pass the existing CI pipeline.
```

### 🟦 High-Level Philosophy Style

```markdown
**TL;DR**: Codex agents should assist in automating Python 2 to 3 migration with full CI compatibility.

## Migration Goals
You’re migrating multiple services from Python 2 to Python 3. Focus on syntax upgrades,
library replacements, and updated test coverage.

## Compatibility Notes
Ensure legacy APIs continue to function. Pay special attention to unicode handling and deprecated modules.

Don’t remove existing logging—even if it appears verbose. It’s part of the debugging process.

## Agent Actions
- Refactor code to be Python 3 compliant
- Validate test suites pass post-migration
- Update dependencies if required

## Boundaries
Avoid changing deployment scripts or infra code unless explicitly requested.
```

### 🔍 Key Differences:

| Aspect | Gemini-CLI Style | High-Level Philosophy Style |
| --- | --- | --- |
| Section Titles | Generic (`Intent`, etc.) | Descriptive (`Migration Goals`, etc.) |
| Formatting | Config-y, compact | Full sentences, mixed with bullets |
| Tone | Developer-leaning config | AI-readable + human-readable |
| Project Binding | Tied to Gemini ecosystem | Repo-agnostic, project-flexible |

---