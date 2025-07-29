## FEATURE:

Build a text generation pipeline using DSPy, where a language model generates creative completions for given story prompts. The system should be trainable using few-shot supervision and evaluable for correctness and creativity.

## EXAMPLES:

- **`examples/story_prompts.json`**:
  Contains input prompts like "Once upon a time, in a distant galaxy..." and target outputs such as short imaginative continuations.
  These examples are used for few-shot supervision during `compile()` with `BootstrapFewShot`.

- **`examples/story_eval_set.json`**:
  Holds a separate set of prompts and completions for evaluating generation quality post-compile.

## DOCUMENTATION:

- DSPy Text Generation Tutorial: https://dspy.ai/tutorials/llms_txt_generation/
- DSPy API References:
  - `dspy.Signature`: https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/primitives/Signature.md
  - `dspy.Predict`: https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/modules/Generate.md
  - `dspy.BootstrapFewShot`: https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/BootstrapFewShot.md
  - `dspy.Evaluate`: https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/evaluation/Evaluate.md

## OTHER CONSIDERATIONS:

- Keep completions concise (≤ 100 words).
- Avoid overly generic or repetitive responses — model should favor creativity.
- Watch for edge cases in prompt phrasing (e.g., rhetorical or misleading prompts).
- Make sure to separate training (`examples/`) and evaluation data to prevent overfitting.
- For reproducibility, set the same random seed across optimization runs.
- LLM configuration (OpenAI, Ollama, etc.) should be modular and overrideable via config or CLI.
