import matplotlib.pyplot as plt
import plotmath

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x, a, b):
        return a * x + b

    # List of functions and their labels.
    a = 2
    b = -1
    c = -1
    d = 4

    x_skjæring = (d - b) / (a - c)
    y_skjæring = a * x_skjæring + b

    functions = [
        lambda x: f(x, a=a, b=b),
        lambda x: f(x, a=c, b=d),
    ]
    fn_labels = ["$f$", "$g$"]

    # Create the math figure
    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-2,
        xmax=6,
        ymin=-4,
        ymax=10,
        ticks=False,
    )

    ax.plot(x_skjæring, y_skjæring, "ko", markersize=8, alpha=0.7)

    plt.annotate(
        text="$x$-koordinaten til skjæringspunktet\n løser likningen $f(x) = g(x)$",
        xy=(x_skjæring, y_skjæring),
        xytext=(0.2, 7.5),
        fontsize=16,
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

    ax.vlines(x_skjæring, 0, y_skjæring, color="red", linestyle="--", alpha=0.7)

    plt.xticks([x_skjæring], labels=[r"$x_0$"], fontsize=16)
    plt.grid(False)

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
