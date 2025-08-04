def main(dirname):
    fname = __file__.split("/")[-1].replace(".py", "")
    synthetic_div(
        fname=fname,
        p="x^3 - 7x^2 - 10x + 16",
        x=1,
        stage=None,
    )

    if dirname:
        import os

        target_fname = "/".join([dirname, fname + ".svg"])
        os.system(f"mv {fname}.svg {target_fname}")


# NOTE: Ikke endre på noe under denne linjen
if __name__ == "__main__":

    import sys
    import pathlib
    import os

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

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # Find the root of the GitHub repository (where .git is located)
    repo_root = find_repo_root(current_dir)

    # Add the GitHub repository root to sys.path
    sys.path.append(repo_root)

    from python_util.synthetic_div import synthetic_div

    main(dirname=dirname)
