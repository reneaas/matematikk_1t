def main():
    synthetic_div(
        fname=__file__.split("/")[-1].replace(".py", ""),
        p="x^4 + 3x^3 - 15x^2 - 19x + 30",
        x=1,
        stage=None,
    )

    synthetic_div(
        fname=__file__.split("/")[-1].replace(".py", "") + "_tutor",
        p="x^4 + 3x^3 - 15x^2 - 19x + 30",
        x=1,
        stage=12,
    )


# NOTE: Ikke endre på noe under denne linjen
if __name__ == "__main__":

    import sys
    import pathlib

    def find_repo_root(current_path):
        current_path = pathlib.Path(
            current_path
        ).resolve()  # Convert to an absolute Path object
        while (
            current_path != current_path.parent
        ):  # Stop when you reach the filesystem root
            if (current_path / ".git").is_dir():  # Check if the .git directory exists
                return str(current_path)
            current_path = current_path.parent  # Move one level up
        raise FileNotFoundError("No .git directory found in any parent directories.")

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    # Find the root of the GitHub repository (where .git is located)
    repo_root = find_repo_root(current_dir)

    # Add the GitHub repository root to sys.path
    sys.path.append(repo_root)

    from python_util.synthetic_div import synthetic_div

    main()
