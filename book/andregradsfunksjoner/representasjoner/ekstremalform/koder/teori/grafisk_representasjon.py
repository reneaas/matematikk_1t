import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x**2 - 5 * x + 4

    # List of functions and their labels.
    functions = [f]
    fn_labels = [f"${fn.__name__}$" for fn in functions]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-4,
        xmax=8,
        ymin=-8,
        ymax=8,
        ticks=False,
    )

    xmin = 5 / 2
    ymin = f(xmin)

    ax.plot(xmin, ymin, "ko", markersize=10, alpha=0.7)

    # ax.plot(0, ymin, "ko", markersize=8, alpha=0.7)
    # ax.plot(xmin, 0, "ko", markersize=8, alpha=0.7)

    # ax.hlines(y=ymin, xmin=0, xmax=xmin, linestyle="--", alpha=0.5, color="black")

    fontsize = 20
    plt.annotate(
        text="Ekstremalpunkt $(x_0, y_0)$",
        xy=(xmin, ymin),
        xytext=(xmin + 0.25, ymin - 4),
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

    # plt.annotate(
    #     text="Ekstremalverdi",
    #     xy=(0, ymin),
    #     xytext=(xmin - 6, ymin - 4),
    #     fontsize=fontsize,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=-0.2",
    #     ),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    # )

    # plt.annotate(
    #     text="(x_0, y_0)",
    #     xy=(xmin, ymin),
    #     xytext=(xmin + 0.5, ymin - 4),
    #     fontsize=fontsize,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=-0.2",
    #     ),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    # )

    plt.annotate(
        text="Symmetrilinje $x = x_0$",
        xy=(xmin, ymin + 4),
        xytext=(xmin - 6, ymin - 2),
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

    red = plotmath.COLORS.get("red")
    ax.vlines(x=xmin, ymin=-10, ymax=10, linestyle="--", color=red, lw=1.5)

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

    # Now you can import modules from the GitHub repo root

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
