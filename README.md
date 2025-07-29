
# dspy_llmstxt_generator

This project uses the DSPy library to automatically generate `llms.txt` files for GitHub repositories. These files provide a standardized, high-level overview of a project's purpose, architecture, and key components, making it easier for developers and LLMs to quickly understand new codebases.

## How it Works

The process is broken down into four main steps:

### 1. Defining Signatures

We define three DSPy signatures to structure the analysis:

-   `AnalyzeRepository`: Analyzes the repository's structure, README, and file tree to determine its main purpose, key concepts, and architecture.
-   `AnalyzeCodeStructure`: Identifies important directories, entry points, and development workflow information from the file tree and package files.
-   `GenerateLLMsTxt`: Takes the analyzed information and generates a comprehensive `llms.txt` file.

### 2. Creating the Repository Analyzer Module

A `RepositoryAnalyzer` module chains the signatures together. It takes a repository URL, file tree, README content, and package files as input, and then:

1.  Analyzes the repository's purpose and concepts.
2.  Analyzes the code structure.
3.  Generates usage examples.
4.  Generates the final `llms.txt` file.

### 3. Gathering Repository Information

The script uses the GitHub API to gather the necessary information from the target repository, including:

-   The file tree
-   The content of the `README.md` file
-   The content of key package files (e.g., `pyproject.toml`, `requirements.txt`, `package.json`)

### 4. Generating `llms.txt`

Finally, the script configures DSPy with a language model, initializes the `RepositoryAnalyzer`, and runs it on the target repository to generate the `llms.txt` file.

## Usage

To use the `dspy_llmstxt_generator`:

1.  **Set your GitHub Access Token:**
    ```python
    import os
    os.environ["GITHUB_ACCESS_TOKEN"] = "<your_access_token>"
    ```

2.  **Set your OpenAI API Key:**
    ```python
    os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI KEY>"
    ```

3.  **Run the generation script:**
    ```python
    from step_4_Configure_DSPy_Generate_llmstxt import generate_llms_txt_for_dspy

    if __name__ == "__main__":
        result = generate_llms_txt_for_dspy()

        # Save the generated llms.txt
        with open("llms.txt", "w") as f:
            f.write(result.llms_txt_content)

        print("Generated llms.txt file!")
    ```

## Example Output

The expected output is a `llms.txt` file with the following structure:

```
# llms.txt

## Project Purpose
[Project purpose and goals]

## Key Concepts
- [Concept 1]
- [Concept 2]

## Architecture Overview
[High-level architecture description]

## Important Directories
- [Directory 1]: [Purpose]
- [Directory 2]: [Purpose]

## Entry Points
- [File 1]: [Description]
- [File 2]: [Description]

## Development
[Development setup and workflow information]

## Usage Examples
[Common usage patterns and examples]
```

Here is a snippet of the expected output when run on the `stanfordnlp/dspy` repository:

```
# DSPy: Programming Language Models

## Project Overview
DSPy is a framework for programming—rather than prompting—language models...

## Key Concepts
- **Modules**: Building blocks for LM programs
- **Signatures**: Input/output specifications
- **Teleprompters**: Optimization algorithms
- **Predictors**: Core reasoning components

## Architecture
- `/dspy/`: Main package directory
  - `/adapters/`: Input/output format handlers
  - `/clients/`: LM client interfaces
  - `/predict/`: Core prediction modules
  - `/teleprompt/`: Optimization algorithms
```

## File Structure

- `analysis/` – DSPy modules for analyzing repositories (`signatures.py`,
  `repository_analyzer.py`, `repository_info.py`, `generate_llmstxt.py`).
- `docs/` – Additional documentation and example outputs (see
  `docs/llms_examples/`).
- `scripts/` – Entry-point utilities such as `main.py`.
- `tests/` – Unit tests and integration tests.

## Dependencies

-   `dspy-ai`
-   `requests`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
