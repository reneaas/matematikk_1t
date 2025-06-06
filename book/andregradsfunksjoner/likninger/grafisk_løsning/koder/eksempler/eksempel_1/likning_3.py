import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**2 + x - 2

    def g(x):
        return -(2 / 3) * x**2 - (7 / 3) * x + 3

    # List of functions and their labels.
    functions = [f, g]
    fn_labels = [f"${fn.__name__}$" for fn in functions]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-5,
        xmax=5,
        ymin=-3,
        ymax=9,
        ticks=True,
    )

    annotation_text = (
        "$x$-koordinatene til skjæringene \n løser likningen $f(x) = g(x)$"
    )
    plt.annotate(
        text=annotation_text,
        xy=(-3, 4),
        xytext=(-3, 7),
        fontsize=16,
        bbox=dict(
            boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.4",
        ),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text=annotation_text,
        xy=(1, 0),
        xytext=(-3, 7),
        fontsize=16,
        bbox=dict(
            boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.1",
        ),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.legend(fontsize=16, loc="center right")

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

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

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
