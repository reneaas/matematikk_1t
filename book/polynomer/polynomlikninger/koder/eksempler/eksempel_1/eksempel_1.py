def main():
    polylongdiv(
        fname="eksempel_1",
        p="x^3 + 2x^2 - 4x - 8",
        q="x - 2",
        stage=None,
    )

    x_vals = [1, -1, 2, -2]
    for i in x_vals:
        synthetic_div(
            fname=f"eksempel_1_syntetisk_{i}",
            p="x^3 + 2x^2 - 4x - 8",
            x=f"{i}",
            stage=None,
        )

    return None


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
    print(repo_root)

    from python_util.polydiv import polylongdiv
    from python_util.synthetic_div import synthetic_div

    main()
