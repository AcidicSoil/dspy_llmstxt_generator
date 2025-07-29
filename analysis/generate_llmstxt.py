def generate_llms_txt_for_dspy():
    # Configure DSPy (use your preferred LM)
    lm = dspy.LM(model="gpt-4o-mini")
    dspy.configure(lm=lm)
    os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI KEY>"

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

    return result

# Run the generation
if __name__ == "__main__":
    result = generate_llms_txt_for_dspy()

    # Save the generated llms.txt
    with open("llms.txt", "w") as f:
        f.write(result.llms_txt_content)

    print("Generated llms.txt file!")
    print("\nPreview:")
    print(result.llms_txt_content[:500] + "...")