import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**2 - 4 * x + 5

    def g(x):
        return x + 1

    # List of functions and their labels.
    functions = [f, g]
    fn_labels = [f"${fn.__name__}$" for fn in functions]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-2,
        xmax=7,
        ymin=-1,
        ymax=10,
        ticks=False,
    )

    annotation_text = (
        "$x$-koordinatene til skjæringene \n løser likningen $f(x) = g(x)$"
    )
    plt.annotate(
        text=annotation_text,
        xy=(1, 2),
        xytext=(0, 8),
        fontsize=16,
        bbox=dict(
            boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text=annotation_text,
        xy=(4, 5),
        xytext=(0, 8),
        fontsize=16,
        bbox=dict(
            boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
    )

    ax.plot(4, 5, "ko", markersize=8, alpha=0.7)
    ax.plot(1, 2, "ko", markersize=8, alpha=0.7)

    x1, y1 = 4, 5
    x2, y1 = 1, 2

    plt.xticks([x1, x2], ["$x_1$", "$x_2$"], fontsize=16)

    ax.vlines(x=4, ymin=0, ymax=5, color="black", linestyle="--", alpha=0.5)
    ax.vlines(x=1, ymin=0, ymax=2, color="black", linestyle="--", alpha=0.5)

    plt.legend(fontsize=16, loc="center right")
    plt.grid(False)

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
