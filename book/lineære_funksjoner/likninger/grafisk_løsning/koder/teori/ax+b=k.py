import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x, a, b):
        return a * x + b

    def g(x, y):
        if isinstance(x, (int, float)):
            return y
        else:
            return [y for _ in x]

    # List of functions and their labels.
    a = 1
    b = -1
    k = 3
    functions = [
        lambda x: f(x, a=a, b=b),
        lambda x: g(x, y=k),
    ]

    fn_labels = ["$f$", "$g$"]

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-2,
        xmax=6,
        ymin=-4,
        ymax=8,
        ticks=False,
    )

    ax.plot(((k - b) / a), k, "ko", markersize=8, alpha=0.7)
    ax.vlines(((k - b) / a), 0, k, color="red", linestyle="--", alpha=0.7)

    ax.annotate(
        text="$x$-koordinaten til skjæringspunktet \n løser likningen $f(x) = g(x)$",
        xy=((k - b) / a, k),
        xytext=(1, 6),
        fontsize=16,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="left",  # Changed to left alignment
        verticalalignment="center",
    )

    plt.xticks([(k - b) / a], labels=[r"$x_0$"], fontsize=16)
    plt.yticks([])

    plt.grid(False)

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
