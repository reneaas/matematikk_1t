import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions

    def p(x):
        return (x - 1) ** 2

    def q(x):
        return x + 2

    def skrå_asymptote(x):
        return x - 4

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
        xmin=-8,
        xmax=8,
        ymin=-20,
        ymax=12,
        ticks=False,
    )

    vertical_asymptote = -2

    x1 = np.linspace(-10, vertical_asymptote, 1024)
    x2 = np.linspace(vertical_asymptote, 10, 1024)

    ax.plot(x1, f(x1), color="teal", lw=2, alpha=0.7, label="$f$")
    ax.plot(x2, f(x2), color="teal", lw=2, alpha=0.7)
    ax.plot(1, 0, "ko", markersize=8, alpha=0.7)

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

    ax.annotate(
        text="Skrå asymptote",
        xy=(2, -2),
        xytext=(1, -10),
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
    )

    ax.annotate(
        text="Vertikal asymptote \n $x = x_\\infty$",
        xy=(-2, -2),
        xytext=(-7, 4),
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
    )

    ax.annotate(
        text="Nullpunkt \n $x = x_1$",
        xy=(1, 0),
        xytext=(2, 6),
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

    ax.legend(fontsize=16)

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
