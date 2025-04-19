import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != 2 and x != -2:
            return 6 * x / (x**2 - 4) ** 2
        else:
            return None

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-10,
        xmax=10,
        ymin=-10,
        ymax=10,
        ticks=False,
    )

    # Plot the function
    x1 = -2
    x2 = 2
    x_vals = np.linspace(-24, x1, 1024)
    ax.plot(x_vals, f(x_vals), color=plotmath.COLORS.get("blue"), lw=2.5, label="$f$")

    x_vals = np.linspace(x1, x2, 1024)
    ax.plot(x_vals, f(x_vals), color=plotmath.COLORS.get("blue"), lw=2.5)

    x_vals = np.linspace(x2, 24, 1024)
    ax.plot(x_vals, f(x_vals), color=plotmath.COLORS.get("blue"), lw=2.5)

    # Draw vertical asymptotes
    ax.vlines(
        x=x1,
        ymin=-100,
        ymax=100,
        color=plotmath.COLORS.get("red"),
        linestyle="--",
        lw=2,
    )
    ax.vlines(
        x=x2,
        ymin=-100,
        ymax=100,
        color=plotmath.COLORS.get("red"),
        linestyle="--",
        lw=2,
    )

    dx = 0.5
    ax.text(
        x=-2 - dx,
        y=5,
        s="$x=-2$",
        fontsize=16,
        color="red",
        ha="right",
        va="center",
    )

    ax.text(
        x=2 + dx,
        y=-5,
        s="$x=2$",
        fontsize=16,
        color="red",
        ha="left",
        va="center",
    )

    ax.plot(0, 0, "ko", markersize=8, alpha=0.7)

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
