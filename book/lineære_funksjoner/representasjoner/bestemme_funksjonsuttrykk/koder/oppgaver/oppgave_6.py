import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):

    # Define functions
    def f(x):
        return -2 * x + 1

    def g(x):
        return -2 * x - 3

    # List of functions and their labels.
    functions = [f, g]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,  # Set `None` hvis du ikke vil ha labels.
        xmin=-4,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
    )

    x1 = -1
    y1 = f(x1)
    x2 = 2
    y2 = f(x2)
    x3 = 1
    y3 = g(x3)
    ax.plot(x1, y1, "ko", markersize=8, alpha=0.7)
    ax.plot(x2, y2, "ko", markersize=8, alpha=0.7)
    ax.plot(x3, y3, "ko", markersize=8, alpha=0.7)

    ax.text(
        s=f"$({x1},{y1})$",
        x=x1,
        y=y1,
        fontsize=16,
        ha="right",
        va="top",
    )

    ax.text(
        s=f"$({x2},{y2})$",
        x=x2,
        y=y2,
        fontsize=16,
        ha="left",
        va="bottom",
    )

    ax.text(
        s=f"$({x3},{y3})$",
        x=x3,
        y=y3,
        fontsize=16,
        ha="left",
        va="bottom",
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

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

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    dirname = current_dir.replace("koder", "figurer")
    main(dirname=dirname, save=True)
