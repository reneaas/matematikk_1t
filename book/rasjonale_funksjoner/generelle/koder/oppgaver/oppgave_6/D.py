import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != -1:
            return (x - 1) ** 2 / (x + 1)
        else:
            return None

    def g(x):
        return x - 3

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        xmin=-12,
        xmax=12,
        ymin=-16,
        ymax=16,
        ticks=False,
    )

    # Plot the function
    x1 = -1
    x_vals = np.linspace(-24, x1, 1024)
    ax.plot(
        x_vals,
        f(x_vals),
        color=plotmath.COLORS.get("blue"),
        lw=2.5,
        label="$\\mathrm{D}$",
    )

    x_vals = np.linspace(x1, 24, 1024)
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

    ax.plot(1, 0, "ko", markersize=8, alpha=0.7)

    x = np.linspace(-20, 20, 1024)
    ax.plot(x, g(x), color=plotmath.COLORS.get("red"), linestyle="--", lw=2, alpha=0.7)

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
