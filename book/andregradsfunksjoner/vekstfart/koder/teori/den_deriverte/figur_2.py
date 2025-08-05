import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x + 1) ** 2 - 3

    dfdx = lambda x: 2 * (x + 1)

    x0 = 1

    slope = dfdx(x0)

    def line(x):
        return slope * (x - x0) + f(x0)

    def g(x):
        return f(x) - line(x)

    # List of functions and their labels.
    functions = [g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f - T$"],
        xmin=-5,
        xmax=4,
        ymin=-6,
        ymax=8,
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
    ax.plot(x0, g(x0), "ko", markersize=10, alpha=0.7)
    ax.text(
        x0,
        g(x0) - 0.3,
        f"$(x_0, 0)$",
        fontsize=25,
        va="top",
        ha="center",
    )

    plt.annotate(
        text="Symmetrilinje $x = x_0$",
        xy=(x0, 4),
        xytext=(x0 - 5.5, 4),
        fontsize=25,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="left",
        verticalalignment="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5, alpha=0.9),
    )

    ax.vlines(x=x0, ymin=-10, ymax=10, color="gray", lw=2.5, ls="--", alpha=0.8)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(25)  # Set to desired font size

    ax.yaxis.label.set_size(25)  # Set y-axis label font size
    ax.xaxis.label.set_size(25)  # Set x-axis label font size
    ax.legend(fontsize=25)

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
