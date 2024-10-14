import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x, a=1, b=-1):
        return a * x + b

    # List of functions and their labels.
    a = 1
    b = -2
    functions = [lambda x: f(x, a=a, b=b)]
    fn_labels = [f"$f$" for fn in functions]

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-8,
        xmax=8,
        ymin=-8,
        ymax=8,
        ticks=False,
    )

    ax.plot(-b / a, 0, "ko", markersize=10, alpha=0.7)

    ax.hlines(y=0, xmin=-100, xmax=-b / a, color="red", alpha=0.5, lw=5)

    # ax.text(
    #     s=r"$ax + b > 0$ eller $ax + b \geq 0$",
    #     x=0,
    #     y=4,
    #     fontsize=16,
    #     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    #     horizontalalignment="center",
    #     verticalalignment="center",
    # )

    x_coord = -3
    y_coord = 4
    ax.annotate(
        text="Løsningsmengde",
        xy=(x_coord + 4, 0),
        xytext=(x_coord, y_coord),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Løsningsmengde",
        xy=(x_coord + 1, 0),
        xytext=(x_coord, y_coord),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Løsningsmengde",
        xy=(x_coord - 1, 0),
        xytext=(x_coord, y_coord),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Løsningsmengde",
        xy=(x_coord - 4, 0),
        xytext=(x_coord, y_coord),
        fontsize=16,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="Nullpunkt er inkludert \n for $f(x) \\leq 0$",
        xy=(-b / a, 0),
        xytext=(3, -4),
        fontsize=16,
        ha="left",
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.3",
        ),
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
