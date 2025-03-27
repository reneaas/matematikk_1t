import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x + 1) * (x - 6) ** 2 / 9

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=8,
        ymin=-1,
        ymax=8,
        ticks=True,
    )

    x = np.linspace(0, 6, 7)

    for i in range(len(x) - 1):
        x0 = x[i]
        x1 = x[i + 1]

        y0 = 0
        y1 = f(x0)
        A = (x0, y0)
        B = (x1, y0)
        C = (x1, y1)
        D = (x0, y1)
        plotmath.plot_polygon(A, B, C, D, color="teal", alpha=0.1)

    plt.text(
        x=6,
        y=6,
        s="6 rektangler",
        fontsize=20,
        ha="center",
        va="center",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.5"),
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    plt.title("6 rektangler", loc="center", fontsize=16)
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
