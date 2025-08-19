import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    a = 1
    b = -4
    c = -6

    def f(x):
        return a * x**2 + b * x + c

    a = 1.5
    x0 = 1.5
    y0 = 2
    c = a * x0**2 + y0

    def f(x):
        return a * (x - x0) ** 2 + y0

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-2,
        ymax=9,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x_symmetry = -b / (2 * a)
    x_symmetry = x0

    red = plotmath.COLORS.get("red")
    ax.vlines(x=x_symmetry, ymin=-20, ymax=20, color=red, lw=2.5, ls="--")

    plt.annotate(
        text=" \n Symmetrilinje \n $x = \\displaystyle -\\frac{b}{2a}$",
        xy=(x_symmetry, -0.5),
        xytext=(-5, 0.5),
        fontsize=20,
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

    ax.plot(0, c, "ko", markersize=10, alpha=0.7)
    # ax.text(
    #     x=0 - 0.2,
    #     y=c,
    #     s="$(0, c)$",
    #     fontsize=25,
    #     ha="right",
    #     va="center",
    #     color="black",
    # )

    plt.annotate(
        text="Skjæring med $y$-aksen \n $(0, c)$",
        xy=(0, c),
        xytext=(-6, 8),
        fontsize=20,
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

    ax.plot(x_symmetry, f(x_symmetry), "ko", markersize=10, alpha=0.7)
    # ax.text(
    #     x=x_symmetry,
    #     y=f(x_symmetry),
    #     s="Bunnpunkt",
    #     fontsize=25,
    #     ha="left",
    #     va="top",
    #     color="black",
    # )

    ax.hlines(
        y=f(x_symmetry),
        xmin=x_symmetry,
        xmax=x_symmetry + 1,
        color="gray",
        ls="--",
        lw=2.5,
    )

    ax.vlines(
        x=x_symmetry + 1,
        ymin=f(x_symmetry),
        ymax=f(x_symmetry + 1),
        color="gray",
        ls="--",
        lw=2.5,
    )

    plt.annotate(
        text="Ekstremalpunkt",
        xy=(x_symmetry, f(x_symmetry)),
        xytext=(-3.9, 4),
        fontsize=20,
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
        text="$a$",
        xy=(x_symmetry + 1, 0.5 * (f(x_symmetry) + f(x_symmetry + 1))),
        xytext=(4, 2),
        fontsize=20,
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

    ax.text(
        x=0.5 * (2 * x_symmetry + 1),
        y=f(x_symmetry) - 0.5,
        s="$1$",
        fontsize=20,
        ha="center",
        va="top",
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
