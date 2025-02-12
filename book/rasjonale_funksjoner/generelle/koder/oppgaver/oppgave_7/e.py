import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != -2 and x != 2:
            return (x**2 - 16) / ((x + 2) * (x - 2))
        else:
            return None

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-12,
        xmax=12,
        ymin=-10,
        ymax=10,
        ticks=False,
    )

    # Plot the function
    x1 = -2
    x2 = 2
    x_vals = np.linspace(-24, x1, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7, label="$f$")

    x_vals = np.linspace(x1, x2, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7)

    x_vals = np.linspace(x2, 24, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7)

    # Draw vertical asymptotes
    ax.vlines(x=x1, ymin=-100, ymax=100, color="red", linestyle="--", lw=1.5)
    ax.vlines(x=x2, ymin=-100, ymax=100, color="red", linestyle="--", lw=1.5)

    dx = dy = 0.5
    ax.text(
        x=x1 - dx,
        y=5,
        s=r"$x = -2$",
        fontsize=16,
        color="red",
        ha="right",
        va="center",
    )

    ax.text(
        x=x2 + dx,
        y=5,
        s=r"$x = 2$",
        fontsize=16,
        color="red",
        ha="left",
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
    ax.plot(-4, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(4, 0, "ko", markersize=8, alpha=0.7)

    ax.text(
        x=-4,
        y=-dy,
        s=r"$(-4, 0)$",
        fontsize=16,
        color="black",
        ha="right",
        va="top",
    )

    ax.text(
        x=4,
        y=-dy,
        s=r"$(4, 0)$",
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
