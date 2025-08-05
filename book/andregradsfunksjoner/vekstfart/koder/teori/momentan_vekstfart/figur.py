import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * (x - 1) ** 2 + 1

    def dfdx(x):
        return 4 * (x - 1)

    a = 2

    slope = dfdx(a)

    def line(x):
        return slope * (x - a) + f(a)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=5,
        ymin=-2,
        ymax=11,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x = np.linspace(-10, 10, 1024)
    color = plotmath.COLORS.get("red")
    ax.plot(x, line(x), color=color, lw=2.5)

    ax.plot(a, f(a), "ko", markersize=10, alpha=0.7)
    ax.text(
        a - 0.2,
        f(a),
        f"$(a, f(a))$",
        fontsize=18,
        va="center",
        ha="right",
    )

    ax.vlines(x=a + 1, ymin=line(a), ymax=line(a + 1), lw=2, ls="--", color="gray")
    ax.hlines(y=line(a), xmin=a, xmax=a + 1, lw=2, ls="--", color="gray")

    ax.text(
        x=0.5 * (2 * a + 1),
        y=line(a) - 0.5,
        s="$1$",
        fontsize=18,
        va="top",
        ha="center",
    )

    plt.annotate(
        text="$f'(a)$",
        xy=(a + 1, 0.5 * (line(a) + line(a + 1))),
        xytext=(a + 2, 2),
        fontsize=18,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5, alpha=0.9),
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
