import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    a = -1
    b = 2
    c = 4
    d = -6

    def f(x):
        return a * x**3 + b * x**2 + c * x + d

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-10,
        ymax=10,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x_antisymmetry = -b / (3 * a)

    red = plotmath.COLORS.get("red")
    ax.vlines(x=x_antisymmetry, ymin=-20, ymax=20, color=red, lw=2.5, ls="--")

    plt.annotate(
        text=" \n Anti-symmetrilinje \n $x = \\displaystyle -\\frac{b}{3a}$",
        xy=(x_antisymmetry, 8),
        xytext=(2, 7),
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

    ax.plot(x_antisymmetry, f(x_antisymmetry), "ko", markersize=10, alpha=0.7)

    plt.annotate(
        text="Vendepunkt",
        xy=(x_antisymmetry, f(x_antisymmetry)),
        xytext=(3, -4),
        fontsize=20,
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
        x=-5,
        y=-3,
        s="$a < 0$",
        fontsize=20,
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
