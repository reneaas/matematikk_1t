import plotmath
import numpy as np


def main(dirname, save):

    def f(x):
        return (x + 1) * (x - 1) * (x - 2) / 3

    def make_secant_fn(f, x0, x1):
        def secant(x):
            return f(x0) + (f(x1) - f(x0)) / (x1 - x0) * (x - x0)

        return secant

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-3,
        xmax=6,
        ymin=-4,
        ymax=6,
        ticks=False,
    )

    r = 1.5
    x = 3
    ax.plot(r, f(r), "ko", markersize=8, alpha=0.7)
    ax.plot(x, f(x), "ko", markersize=8, alpha=0.7)

    dx = dy = 0.2
    ax.text(
        x=r,
        y=f(r) - dy,
        s=r"$(r, f(r))$",
        fontsize=16,
        va="top",
        ha="left",
    )

    ax.text(
        x=x + dx,
        y=f(x),
        s=r"$(x, f(x))$",
        fontsize=16,
        va="top",
        ha="left",
    )

    secant = make_secant_fn(f, r, x)

    x_vals = np.linspace(-6, 6, 1024)

    ax.plot(x_vals, secant(x_vals), lw=2.5)

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
