import plotmath
import numpy as np


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 1 / x

    def make_tangent_fn(a, h=1e-7):
        def tangent_fn(x):
            return f(a) + (f(a + h) - f(a)) / h * (x - a)

        return tangent_fn

    # List of functions and their labels.

    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=4,
        ymin=-1,
        ymax=4,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=(0, 6),
    )

    s = 1
    ax.plot(s, f(s), "ko", markersize=8, alpha=0.7)
    ax.text(
        x=s + 0.05,
        y=f(s),
        s=r"$(s, f(s))$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    T = make_tangent_fn(s)
    x = np.linspace(-2, 6, 1024)
    ax.plot(x, T(x), lw=2, color="black", alpha=0.8)

    A = (2 * s, 0)
    B = (0, 2 / s)

    ax.plot(*A, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=A[0] - 0.05,
        y=A[1] - 0.05,
        s=r"$A$",
        fontsize=20,
        ha="right",
        va="top",
    )
    ax.plot(*B, "ko", markersize=8, alpha=0.7)
    ax.text(
        x=B[0] - 0.05,
        y=B[1] - 0.05,
        s=r"$B$",
        fontsize=20,
        ha="right",
        va="top",
    )

    ax.text(
        x=-0.05,
        y=-0.05,
        s="$O$",
        fontsize=20,
        ha="right",
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
