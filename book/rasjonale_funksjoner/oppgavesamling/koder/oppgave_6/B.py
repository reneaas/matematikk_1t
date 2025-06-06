import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != -3 and x != 3:
            return (x**2 - 1) / (x**2 - 9)
        else:
            return None

    # List of functions and their labels.
    functions = [f]

    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        ticks=False,
    )

    # Plot the function
    x1 = -3
    x2 = 3
    x_vals = np.linspace(-24, x1, 1024)
    ax.plot(
        x_vals,
        f(x_vals),
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
        label="$\\mathrm{B}$",
    )

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

    # Draw horisontal asymptote
    ax.hlines(
        y=1, xmin=-100, xmax=100, color=plotmath.COLORS.get("red"), linestyle="--", lw=2
    )

    ax.plot(-1, 0, "ko", markersize=8, alpha=0.7)
    ax.plot(1, 0, "ko", markersize=8, alpha=0.7)

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
