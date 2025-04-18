import matplotlib.pyplot as plt

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * x + 3

    def g(x):
        if isinstance(x, (int, float)):
            return 5
        else:
            return [5 for _ in x]

    # List of functions and their labels.
    functions = [f, g]
    fn_labels = [f"${fn.__name__}$" for fn in functions]

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-3,
        xmax=5,
        ymin=-3,
        ymax=8,
        ticks=True,
    )

    ax.plot(1, 5, "ko", markersize=8, alpha=0.7)

    ax.annotate(
        text="Skjæringspunkt",
        xy=(1, 5),
        xytext=(2, 3),
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

    ax.annotate(
        text="Løsning av likningen",
        xy=(1, 0),
        xytext=(1.2, -2),
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

    ax.vlines(1, 0, 5, color="red", linestyle="--", alpha=0.7)

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".png")
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
