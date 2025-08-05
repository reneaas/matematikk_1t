import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * (x - 2) ** 2 + 1

    a = 1
    b = 4

    slope = (f(b) - f(a)) / (b - a)

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
        a + 0.2,
        f(a),
        f"$(a, f(a))$",
        fontsize=18,
        va="center",
        ha="left",
    )

    ax.plot(b, f(b), "ko", markersize=10, alpha=0.7)
    ax.text(
        b + 0.2,
        f(b) - 0.5,
        f"$(b, f(b))$",
        fontsize=18,
        va="bottom",
        ha="left",
    )

    c = 0.5 * (a + b)

    ax.vlines(x=c, ymin=line(c), ymax=line(c + 1), lw=2, ls="--", color="gray")
    ax.hlines(y=line(c + 1), xmin=c, xmax=c + 1, lw=2, ls="--", color="gray")

    ax.text(
        x=0.5 * (2 * c + 1),
        y=line(c + 1) + 0.5,
        s="$1$",
        fontsize=18,
        va="bottom",
        ha="center",
    )

    plt.annotate(
        text="$\\displaystyle\\frac{f(b) - f(a)}{b - a}$",
        xy=(c, 0.5 * (line(c) + line(c + 1))),
        xytext=(c - 2, 8),
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
