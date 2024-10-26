import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**2 - x - 6

    def g(x):
        return -(x**2) - 4 * x - 4

    def h(x):
        return 4 * x**2 - 3 * x + 1

    # List of functions and their labels.
    functions = [f, g, h]

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=None,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-8,
        xmax=8,
        ymin=-8,
        ymax=8,
        ticks=False,
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        savefig(dirname=dirname, fname=fname)  # Lagrer figuren i `dirname`-directory

    if not save:

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
    from python_utils.plot_utils import make_figure, savefig

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
