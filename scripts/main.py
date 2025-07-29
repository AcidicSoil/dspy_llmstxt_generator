import os
import dspy
from analysis.repository_analyzer import RepositoryAnalyzer
from analysis.repository_info import gather_repository_info

def main():
    # Configure DSPy (use your preferred LM)
    lm = dspy.LM(model="gpt-4o-mini")
    dspy.configure(lm=lm)
    # Make sure to set your OPENAI_API_KEY environment variable

    # Initialize our analyzer
    analyzer = RepositoryAnalyzer()

    # Gather DSPy repository information
    repo_url = "https://github.com/stanfordnlp/dspy"
    file_tree, readme_content, package_files = gather_repository_info(repo_url)

    # Generate llms.txt
    result = analyzer(
        repo_url=repo_url,
        file_tree=file_tree,
        readme_content=readme_content,
        package_files=package_files
    )

    # Save the generated llms.txt
    with open("llms.txt", "w") as f:
        f.write(result.llms_txt_content)

    print("Generated llms.txt file!")
    print("\nPreview:")
    print(result.llms_txt_content[:500] + "...")

if __name__ == "__main__":
    main()