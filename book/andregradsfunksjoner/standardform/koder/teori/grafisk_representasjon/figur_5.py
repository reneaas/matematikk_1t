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
    y0 = 4
    c = a * x0**2 + y0

    def f(x):
        return a * (x - x0) ** 2 + y0

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-2,
        xmax=8,
        ymin=-1,
        ymax=18,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
        fontsize=24,
    )

    x_symmetry = -b / (2 * a)
    x_symmetry = x0

    red = plotmath.COLORS.get("red")
    ax.vlines(x=x_symmetry, ymin=-20, ymax=20, color=red, lw=2.5, ls="--")

    # plt.annotate(
    #     text=" \n Symmetrilinje \n $x = \\displaystyle -\\frac{b}{2a}$",
    #     xy=(x_symmetry, -0.5),
    #     xytext=(-5, 0.5),
    #     fontsize=24,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=+0.2",
    #     ),
    #     bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    # )

    # ax.plot(0, c, "ko", markersize=10, alpha=0.7)

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

    # plt.annotate(
    #     text="Ekstremalpunkt",
    #     xy=(x_symmetry, f(x_symmetry)),
    #     xytext=(-3.9, 4),
    #     fontsize=24,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=+0.3",
    #     ),
    #     bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    # )

    # plt.annotate(
    #     text="$1^2 \\cdot a$",
    #     xy=(x_symmetry + 1, 0.5 * (f(x_symmetry) + f(x_symmetry + 1))),
    #     xytext=(4, 0.5),
    #     fontsize=24,
    #     arrowprops=dict(
    #         arrowstyle="->",
    #         lw=2,
    #         color="black",
    #         alpha=0.7,
    #         connectionstyle="arc3,rad=+0.3",
    #     ),
    #     bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
    #     horizontalalignment="left",
    #     verticalalignment="center",
    # )

    plotmath.annotate(
        xy=(x_symmetry + 1, 0.5 * (f(x_symmetry) + f(x_symmetry + 1))),
        xytext=(6, 3),
        s="$1^2 \\cdot a$",
        arc=+0.1,
        fontsize=24,
    )

    ax.text(
        x=0.5 * (2 * x_symmetry + 1),
        y=f(x_symmetry) - 0.7,
        s="$1$",
        fontsize=24,
        ha="center",
        va="top",
    )

    ax.hlines(
        y=f(x_symmetry),
        xmin=x_symmetry + 1,
        xmax=x_symmetry + 2,
        color="gray",
        lw=2.5,
        ls="--",
    )

    ax.vlines(
        x=x_symmetry + 2,
        ymin=f(x_symmetry),
        ymax=f(x_symmetry + 2),
        color="gray",
        ls="--",
        lw=2.5,
    )

    plotmath.annotate(
        xy=(x_symmetry + 2, 0.5 * (f(x_symmetry) + f(x_symmetry + 2))),
        xytext=(6, 7.5),
        s="$2^2 \\cdot a$",
        arc=+0.3,
        fontsize=24,
    )

    plotmath.make_bar(
        xy=(x_symmetry, f(x_symmetry) - 0.5),
        length=1,
        orientation="horizontal",
    )

    plotmath.make_bar(
        xy=(x_symmetry, f(x_symmetry) - 1.9),
        length=2,
        orientation="horizontal",
    )

    ax.text(
        x=0.5 * (2 * x_symmetry + 2),
        y=f(x_symmetry) - 2.2,
        s="$2$",
        fontsize=24,
        ha="center",
        va="top",
    )

    ax.hlines(
        y=f(x_symmetry),
        xmin=x_symmetry + 2,
        xmax=x_symmetry + 3,
        color="gray",
        lw=2.5,
        ls="--",
    )

    ax.vlines(
        x=x_symmetry + 3,
        ymin=f(x_symmetry),
        ymax=f(x_symmetry + 3),
        color="gray",
        ls="--",
        lw=2.5,
    )

    plotmath.make_bar(
        xy=(x_symmetry, f(x_symmetry) - 3.5),
        length=3,
        orientation="horizontal",
    )

    plotmath.annotate(
        xy=(x_symmetry + 3, 0.5 * (f(x_symmetry) + f(x_symmetry + 3))),
        xytext=(6, 12),
        s="$3^2 \\cdot a$",
        arc=-0.3,
        fontsize=24,
    )

    ax.text(
        x=0.5 * (2 * x_symmetry + 3),
        y=f(x_symmetry) - 4,
        s="$3$",
        fontsize=24,
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
