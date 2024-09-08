def main(dirname, save):

    # Define functions

    def f(x, a, b):
        return a * x + b

    # List of functions and their labels.

    for a in range(-10, 11):
        for b in range(-10, 11):
            functions = [lambda x: f(x, a=a, b=b)]
            fn_labels = [f"$f(x) = {a}x + {b}$"]

            # Create the math figure
            fig, ax = make_figure(
                functions=functions,
                fn_labels=fn_labels,  # Set `None` hvis du ikke vil ha labels.
                xmin=-6,
                xmax=6,
                ymin=-6,
                ymax=6,
                ticks=True,
            )

            if save:
                fname = f"{a=}_{b=}.svg"
                savefig(
                    dirname=dirname, fname=fname
                )  # Lagrer figuren i `dirname`-directory
                import matplotlib.pyplot as plt

                plt.close()

    if not save:
        import matplotlib.pyplot as plt

        plt.show()


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

    # Now you can import modules from the GitHub repo root
    from python_templates.plot_utils import make_figure, savefig

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    dirname = current_dir.replace("koder", "figurer")
    main(dirname=dirname, save=True)
