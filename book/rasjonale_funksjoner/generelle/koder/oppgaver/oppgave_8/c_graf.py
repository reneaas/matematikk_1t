import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != 2 and x != -3:
            return (x**2 - 8 * x + 12) / ((x - 2) * (x + 3))
        else:
            return None

    def g(x):
        return (x - 6) / (x + 3)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-15,
        xmax=15,
        ymin=-10,
        ymax=10,
        ticks=False,
    )

    # Plot the function
    x1 = -3
    x2 = 2
    x_vals = np.linspace(-24, x1, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7, label="$f$")

    x_vals = np.linspace(x1, x2, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7)

    x_vals = np.linspace(x2, 24, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7)

    # Draw vertical asymptotes
    ax.vlines(x=x1, ymin=-100, ymax=100, color="red", linestyle="--", lw=1.5)

    # Draw holes in the graph
    ax.plot(x2, g(x2), "x", color="red", markersize=20, alpha=1)

    ax.annotate(
        text="Hull i grafen i $x = 2$",
        xy=(x2, g(x2)),
        xytext=(6, -6),
        fontsize=16,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.2",
        ),
        horizontalalignment="center",
        verticalalignment="center",
    )

    dx = dy = 0.5
    ax.text(
        x=x1 - dx,
        y=-5,
        s=f"$x = {x1}$",
        fontsize=16,
        color="red",
        ha="right",
        va="center",
    )

    # plot horisontal asymptote

    ax.hlines(y=1, xmin=-100, xmax=100, color="blue", linestyle="--", lw=1.5)
    ax.text(
        x=6,
        y=1 + dy,
        s=r"$y = 1$",
        fontsize=16,
        color="blue",
        ha="center",
        va="bottom",
    )

    # Plot zeros
    ax.plot(6, 0, "ko", markersize=8, alpha=0.7)

    ax.text(
        x=6,
        y=-dy,
        s=r"$(6, 0)$",
        fontsize=16,
        color="black",
        ha="left",
        va="top",
    )

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
