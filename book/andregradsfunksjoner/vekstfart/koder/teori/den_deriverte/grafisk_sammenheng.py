import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x + 1) ** 2 - 3

    def g(x):
        return 2 * (x + 1)

    # List of functions and their labels.
    functions = [f, g]

    fn_labels = ["$f$", "$f'$"]

    figs, axes = plotmath.multiplot(
        functions=functions,
        fn_labels=fn_labels,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        xstep=1,
        ystep=1,
        ticks=False,
        rows=1,
        cols=2,
        figsize=(10, 4),
    )

    def make_tangent_fn(x0):
        slope = g(x0)

        def tangent_line(x):
            return slope * (x - x0) + f(x0)

        return tangent_line

    ax1, ax2 = axes

    x0 = 1  # Point of tangency
    tangent_fn = make_tangent_fn(x0)

    x = np.linspace(-10, 10, 1024)
    color = plotmath.COLORS.get("red")
    ax1.plot(x, tangent_fn(x), color=color, lw=2.5)

    ax1.vlines(x=-1, ymin=-10, ymax=10, color="gray", lw=2.5, ls="--", alpha=0.8)

    # Add an annotation from ax1 to ax2
    # plt.annotate(
    #     "",
    #     xy=(0.5, 0.5),
    #     xycoords=ax2.transData,
    #     xytext=(0.5, 0.5),
    #     textcoords=ax1.transData,
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

    # Add an annotation from ax2 to ax1
    plt.annotate(
        "",
        xy=(-1, f(-1)),
        xycoords=ax1.transData,
        xytext=(-1, 0),
        textcoords=ax2.transData,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
    )

    # plt.annotate(
    #     text="Symmetrilinje $x = x_0$",
    #     xy=(x0, 4),
    #     xytext=(x0 - 5.5, 4),
    #     fontsize=25,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=-0.2",
    #     ),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    #     bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5, alpha=0.9),
    # )

    plt.show()

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
    main(dirname=dirname, save=False)
