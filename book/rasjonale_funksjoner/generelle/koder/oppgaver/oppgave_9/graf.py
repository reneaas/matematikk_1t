import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    @np.vectorize
    def f(x):
        if x != -1:
            return (x - 2) / (x + 1)
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
    x1 = -1
    x_vals = np.linspace(-24, x1, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7, label="$f$")

    x_vals = np.linspace(x1, 24, 1024)
    ax.plot(x_vals, f(x_vals), color="teal", lw=2, alpha=0.7)

    # Draw vertical asymptotes
    ax.vlines(x=x1, ymin=-100, ymax=100, color="red", linestyle="--", lw=1.5)
    ax.hlines(y=1, xmin=-100, xmax=100, color="blue", linestyle="--", lw=1.5)

    ax.plot(2, 0, "ko", markersize=8, alpha=0.7)

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
