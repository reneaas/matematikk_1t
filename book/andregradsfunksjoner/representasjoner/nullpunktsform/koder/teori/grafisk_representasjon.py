import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 1) * (x + 2)

    # List of functions and their labels.
    functions = [f]
    fn_labels = [f"${fn.__name__}$" for fn in functions]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-4,
        xmax=4,
        ymin=-5,
        ymax=8,
        ticks=False,
        alpha=0.8,
    )

    x1 = -2
    x2 = 1
    ax.plot(x1, 0, "ko", markersize=10, alpha=0.7)
    ax.plot(x2, 0, "ko", markersize=10, alpha=0.7)

    xytext = (x1, 4)
    fontsize = 22
    plt.annotate(
        text="Nullpunkter",
        xy=(x1, 0),
        xytext=xytext,
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8),
    )

    plt.annotate(
        text="Nullpunkter",
        xy=(x2, 0),
        xytext=xytext,
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8),
    )

    plt.annotate(
        text="$$x_1$$",
        xy=(x1, 0),
        xytext=(-2, -4),
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8),
    )

    plt.annotate(
        text="$$x_2$$",
        xy=(x2, 0),
        xytext=(2, -4),
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8),
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory
        fname = __file__.split("/")[-1].replace(".py", ".png")
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

    # Add the GitHub repository root to sys.path
    sys.path.append(repo_root)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
