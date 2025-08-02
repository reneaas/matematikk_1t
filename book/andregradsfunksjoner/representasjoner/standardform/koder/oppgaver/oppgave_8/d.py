import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions

    a = -1
    b = 2
    c = 0

    def p(x):
        return a * (x**2) + b * x + c

    # List of functions and their labels.
    functions = [p]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
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

    x_symmetri = -b / (2 * a)
    ekstremalpunkt = (x_symmetri, p(x_symmetri))
    y_skjæring = (0, c)

    ax.plot(*ekstremalpunkt, "ko", markersize=10, alpha=0.7)

    ax.plot(*y_skjæring, "ko", markersize=10, alpha=0.7)

    red = plotmath.COLORS.get("red")
    ax.vlines(x=x_symmetri, ymin=-20, ymax=20, color=red, lw=1.5, ls="--")

    plt.annotate(
        text=f"Toppunkt $({ekstremalpunkt[0]:.0f}, {ekstremalpunkt[1]:.0f})$",
        xy=ekstremalpunkt,
        xytext=(3, 3),
        fontsize=18,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text=f"Symmetrilinje $x = {x_symmetri:.0f}$",
        xy=(x_symmetri, 3),
        xytext=(-6, 4),
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
        text=f"Skjæring med $y$-aksen \n $(0, {y_skjæring[1]})$",
        xy=y_skjæring,
        xytext=(-6, -4),
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
