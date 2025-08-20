import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * x**2 - 4 * x + 1

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-5,
        xmax=7,
        ymin=-4,
        ymax=8,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    bunnpunkt = (1, -1)
    x_symmetri = 1
    y_skjæring = (0, 1)

    ax.plot(*bunnpunkt, "ko", markersize=10, alpha=0.7)

    ax.plot(*y_skjæring, "ko", markersize=10, alpha=0.7)

    red = plotmath.COLORS.get("red")
    ax.vlines(x=x_symmetri, ymin=-20, ymax=20, color=red, lw=1.5, ls="--")

    plt.annotate(
        text="Bunnpunkt $(1, -1)$",
        xy=bunnpunkt,
        xytext=(3, -2),
        fontsize=18,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text="Symmetrilinje $x = 1$",
        xy=(x_symmetri, 2),
        xytext=(3, 3),
        fontsize=18,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.2",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text="Skjæring med $y$-aksen \n $(0, 1)$",
        xy=y_skjæring,
        xytext=(-5, -2),
        fontsize=18,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
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
