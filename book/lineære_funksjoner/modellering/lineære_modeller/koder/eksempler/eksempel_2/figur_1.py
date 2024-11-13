import matplotlib.pyplot as plt
import numpy as np

plt.rc("text", usetex=True)


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return x - 2

    # List of functions and their labels.
    functions = []
    fn_labels = None

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=fn_labels,  # NOTE: Set `None` hvis du ikke vil ha labels.
        xmin=-3,
        xmax=10,
        ymin=-3,
        ymax=8,
        ticks=True,
    )

    xmin = 3
    xmax = 8
    x = np.linspace(xmin, xmax, 1024)
    ax.plot(x, f(x), lw=2, color="teal", alpha=0.7, label="$f$")
    ax.hlines(
        y=f(xmin),
        xmin=0,
        xmax=xmin,
        linestyle="--",
        lw=0.8,
        color="black",
        alpha=0.5,
    )

    ax.hlines(
        y=f(xmax),
        xmin=0,
        xmax=xmax,
        linestyle="--",
        lw=0.8,
        color="black",
        alpha=0.5,
    )

    ax.vlines(
        x=xmin,
        ymin=0,
        ymax=f(xmin),
        linestyle="--",
        color="black",
        alpha=0.5,
        lw=0.8,
    )

    ax.vlines(
        x=xmax,
        ymin=0,
        ymax=f(xmax),
        linestyle="--",
        color="black",
        alpha=0.5,
        lw=0.8,
    )

    # Annoterer definisjonsmengden
    fontsize = 18
    ax.annotate(
        text="$D_f$",
        xy=(0.5 * (xmin + xmax), 0),
        xytext=(0.5 * (xmin + xmax), -2),
        fontsize=fontsize,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="$D_f$",
        xy=(xmin + 0.5, 0),
        xytext=(0.5 * (xmin + xmax), -2),
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.3",
        ),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="$D_f$",
        xy=(xmax - 0.5, 0),
        xytext=(0.5 * (xmin + xmax), -2),
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.hlines(y=0, xmin=xmin, xmax=xmax, color="red", lw=5, alpha=0.5)

    plt.text(
        xmin,
        0,
        r"$\langle$",
        va="center",
        ha="center",
        fontsize=40,
        color="red",
    )

    plt.text(
        xmax,
        0,
        "$]$",
        va="center",
        ha="center",
        fontsize=40,
        color="red",
    )

    # Annoterer verdimengden

    ax.annotate(
        text="$V_f$",
        xy=(0, 0.5 * (f(xmin) + f(xmax))),
        xytext=(-2, 0.5 * (f(xmin) + f(xmax))),
        fontsize=fontsize,
        arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="$V_f$",
        xy=(0, f(xmax) - 0.5),
        xytext=(-2, 0.5 * (f(xmin) + f(xmax))),
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.3",
        ),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.annotate(
        text="$V_f$",
        xy=(0, f(xmin) + 0.5),
        xytext=(-2, 0.5 * (f(xmin) + f(xmax))),
        fontsize=fontsize,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        horizontalalignment="center",
        verticalalignment="center",
    )

    ax.vlines(x=0, ymin=f(xmin), ymax=f(xmax), color="blue", lw=5, alpha=0.5)

    plt.text(
        0,
        f(xmin),
        r"$\langle$",
        va="center",
        ha="center",
        fontsize=40,
        color="blue",
        rotation=90,
    )

    plt.text(
        0,
        f(xmax),
        "$]$",
        va="center",
        ha="center",
        fontsize=40,
        color="blue",
        rotation=90,
    )

    plt.legend(fontsize=16)

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
