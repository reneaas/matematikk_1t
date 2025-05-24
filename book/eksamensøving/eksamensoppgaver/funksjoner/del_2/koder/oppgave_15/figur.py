import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x, a=1 / 4):
        return a * x**2

    def make_tangent_fn(x0, h=1e-5):
        slope = 2 * (1 / 4) * x0
        y0 = f(x0)

        def tangent_fn(x):
            return slope * (x - x0) + y0

        return tangent_fn

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-2,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )
    a = 1 / 4
    ax.hlines(y=-1 / (4 * a), xmin=-10, xmax=10, color="black", lw=2)
    x0 = 3.5
    P = (0, 1 / (4 * a))
    Q = (x0, -1 / (4 * a))
    R = (x0, f(x0))

    ax.plot(x0, -1 / (4 * a), "ko", markersize=8, alpha=0.7)

    x = np.linspace(-10, 10, 1024)
    T = make_tangent_fn(x0=x0)
    ax.plot(x, T(x), color="black", lw=2, ls="--")
    ax.plot(x0, f(x0), "ko", markersize=8, alpha=0.7)

    # Innkommende stråle
    plt.annotate(
        "",  # No text
        xy=(x0, f(x0)),  # Arrow tip
        xytext=(x0, 9),  # Arrow base
        arrowprops=dict(
            facecolor="red",
            arrowstyle="->,head_length=0.5,head_width=0.3",
            alpha=0.7,
            lw=2,
            color="red",
        ),
    )

    # Reflektert stråle
    plt.annotate(
        "",  # No text
        xy=P,  # Arrow tip
        xytext=(x0, f(x0)),  # Arrow base
        arrowprops=dict(
            facecolor="red",
            arrowstyle="->,head_length=0.5,head_width=0.3",
            alpha=0.7,
            lw=2,
            color="red",
        ),
    )

    ax.plot(*zip(P, Q), color="black", lw=2, ls="-")
    ax.plot(*zip(Q, R), color="black", lw=2, ls="-")
    # ax.plot(*zip(P, R), color="black", lw=2, ls="-")

    ax.plot(*P, "ko", markersize=8, alpha=0.7)

    ax.text(
        x=P[0] - 0.2,
        y=P[1],
        s="$P(0, k)$",
        fontsize=20,
        ha="right",
        va="center",
    )

    ax.text(
        x=Q[0],
        y=Q[1] - 0.2,
        s="$Q(s, -k)$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.text(
        x=R[0] + 0.2,
        y=R[1],
        s="$R(s, f(s))$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.plot(0.5 * x0, 0, "ko", markersize=8, alpha=0.7)

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
