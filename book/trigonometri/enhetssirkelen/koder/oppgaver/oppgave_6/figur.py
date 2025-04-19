import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):

    fig, ax = plotmath.plot(
        functions=[],
        fn_labels=False,
        ticks=False,
        grid=False,
    )

    def make_circle(radius):
        theta = np.linspace(0, 2 * np.pi, 1024)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    def make_circle_arc(radius, start, end):
        theta = np.linspace(start, end, 1024)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    ax.set_xlabel("$x$", loc="right", fontsize=16)
    ax.set_ylabel("$y$", loc="top", fontsize=16)

    r = 1

    x, y = make_circle(radius=r)
    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)

    angle = 50
    angle = np.deg2rad(angle)
    ax.plot([0, r * np.cos(angle)], [0, r * np.sin(angle)], color="black", lw=1.5)

    angle = 50
    angle = np.deg2rad(angle)
    x, y = make_circle_arc(radius=0.2, start=0, end=angle)
    ax.plot(x, y, color="black", lw=1)

    x0 = r * np.cos(angle)
    y0 = r * np.sin(angle)
    ax.plot(x0, y0, "ko", markersize=8, alpha=0.7)

    ax.text(
        x=0.3,
        y=0.1,
        s="$50^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
    )

    dx = 0.05
    ax.text(
        x=x0 + dx,
        y=y0,
        s="$P(0.64, 0.77)$",
        fontsize=18,
        ha="left",
        va="bottom",
    )

    plt.axis("equal")

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
