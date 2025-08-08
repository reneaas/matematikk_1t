import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    a = 1
    b = -2
    c = -3

    def f(x):
        return a * x**2 + b * x + c

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
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

    x_symmetry = -b / (2 * a)

    red = plotmath.COLORS.get("red")
    ax.vlines(x=x_symmetry, ymin=-20, ymax=20, color=red, lw=1.5, ls="--")

    plt.annotate(
        text=" \n Symmetrilinje \n $x = \\displaystyle -\\frac{b}{2a}$",
        xy=(x_symmetry, 2),
        xytext=(-5.5, 3),
        fontsize=25,
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
    ax.text(
        x=0 - 0.2,
        y=c,
        s="$(0, c)$",
        fontsize=25,
        ha="right",
        va="center",
        color="black",
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

    plt.annotate(
        text="Bunnpunkt",
        xy=(x_symmetry, f(x_symmetry)),
        xytext=(3, -3),
        fontsize=25,
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

    ax.text(
        x=3,
        y=5,
        s="$a > 0$",
        fontsize=25,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
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
