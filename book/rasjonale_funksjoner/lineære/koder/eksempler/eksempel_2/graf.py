import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions

    def p(x):
        return (x + 2) * (x - 3)

    def q(x):
        return x - 2

    def skrå_asymptote(x):
        return x + 1

    @np.vectorize
    def f(x):
        if q(x) == 0:
            return None
        else:
            return p(x) / q(x)

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-10,
        ymax=10,
        ticks=False,
    )

    vertical_asymptote = 2
    zero1 = -2
    zero2 = 3

    x1 = np.linspace(-10, vertical_asymptote, 1024)
    x2 = np.linspace(vertical_asymptote, 10, 1024)

    ax.plot(x1, f(x1), color="teal", lw=2, alpha=0.7, label="$f$")
    ax.plot(x2, f(x2), color="teal", lw=2, alpha=0.7)
    ax.plot(zero1, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(zero2, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(0, f(0), "ko", markersize=8, alpha=0.7)

    ax.text(
        x=0 - 0.2,
        y=f(0),
        s=f"$(0, {int(f(0))})$",
        fontsize=16,
        ha="right",
        va="center",
    )

    ax.text(
        x=zero1 - 0.2,
        y=0 + 0.2,
        s=f"$({zero1}, 0)$",
        fontsize=16,
        ha="right",
        va="bottom",
    )

    ax.text(
        x=zero2 + 0.2,
        y=0 - 0.2,
        s=f"$({zero2}, 0)$",
        fontsize=16,
        ha="left",
        va="top",
    )

    ax.text(
        x=2 + 0.3,
        y=7,
        s="$x = 2$",
        fontsize=18,
        color="red",
        va="center",
        ha="left",
    )

    x = np.linspace(-10, 10, 1024)
    ax.plot(x, skrå_asymptote(x), linestyle="--", color="blue", lw=1.5, alpha=0.7)

    ax.vlines(
        x=vertical_asymptote,
        ymin=-20,
        ymax=20,
        linestyle="--",
        lw=1.5,
        color="red",
        alpha=0.7,
    )

    # ax.annotate(
    #     text="Nullpunkt $x = x_1$",
    #     xy=(x1, 0),
    #     xytext=(x1 - 5, -5),
    #     fontsize=18,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=+0.2",
    #     ),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    # )

    ax.legend(fontsize=16, loc="upper left")

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
