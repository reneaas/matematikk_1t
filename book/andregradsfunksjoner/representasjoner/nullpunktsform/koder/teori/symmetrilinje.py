import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    x1 = 1
    x2 = 5
    x0 = (x1 + x2) / 2

    def f(x):
        return (x - x1) * (x - x2)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    ax.plot(x1, 0, "ko", markersize=10, alpha=0.7)
    ax.plot(x2, 0, "ko", markersize=10, alpha=0.7)

    ax.vlines(x=x0, ymin=-10, ymax=10, color=plotmath.COLORS.get("red"), lw=2, ls="--")

    ax.text(
        x1 - 0.1,
        0 - 0.1,
        f"$(x_1, 0)$",
        fontsize=18,
        va="top",
        ha="right",
    )

    ax.text(
        x2,
        0 - 0.3,
        f"$(x_2, 0)$",
        fontsize=18,
        va="top",
        ha="left",
    )

    plt.annotate(
        text="\n Symmetrilinje \n $x_0 = \\displaystyle \\frac{x_1 + x_2}{2}$",
        xy=(x0, 4),
        xytext=(0.5, 4),
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
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.8),
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
