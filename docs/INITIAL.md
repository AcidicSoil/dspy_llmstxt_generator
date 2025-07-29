## FEATURE:

Build and supervise a DSPy pipeline that generates coherent, structured paragraphs of natural language text based on minimal user inputs (topic, style, and audience). The goal is to demonstrate prompt programming with declarative supervision, few-shot learning, and metric-based compilation within the DSPy framework.

## EXAMPLES:

This project includes multiple end-to-end examples:
- `examples/basic_pipeline.py`: A simple DSPy `Predict` module that turns topic prompts into paragraphs.
- `examples/compile_with_metric.py`: Shows how to compile a pipeline using `dspy.BootstrapFewShot` and a custom accuracy metric to improve text quality.
- `examples/style_and_audience.py`: Demonstrates the use of multiple input fields (topic, style, audience) to control the tone and format of the generated text.

Each example is structured to be executable, visualizable, and easily extensible.

## DOCUMENTATION:

Primary sources referenced:
- 🧠 DSPy official tutorial: https://dspy.ai/tutorials/llms_txt_generation/
- 📦 GitHub repository: https://github.com/AcidicSoil/dspy_llmstxt_generator
- 📘 DSPy API Reference:
  - [`dspy.Signature`](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/primitives/Signature.md)
  - [`dspy.Predict`](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/modules/Predict.md)
  - [`dspy.BootstrapFewShot`](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/BootstrapFewShot.md)
  - [`dspy.Example`](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/primitives/Example.md)
  - [`dspy.Evaluate`](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/evaluation/Evaluate.md)

## OTHER CONSIDERATIONS:

- ✅ Use `dspy.Example` to provide supervised input-output pairs for compilation
- ✅ Avoid overly broad signature fields — be precise in defining inputs and expected outputs
- ✅ Include human-readable accuracy or coherence metric functions for evaluation
- ⚠️ LLM behavior varies significantly across providers (OpenAI, Anthropic, etc.) — test across configurations
- ⚠️ Ensure all modules define `Signature` with appropriate `InputField` and `OutputField` annotations
- 💡 Consider integrating `dspy.ChainOfThought` for more complex generation pipelines in future iterations
