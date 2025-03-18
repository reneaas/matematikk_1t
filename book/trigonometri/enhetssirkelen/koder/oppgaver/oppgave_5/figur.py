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

    ax.set_xlabel("$\\cos u$", loc="right", fontsize=16)
    ax.set_ylabel("$\\sin u$", loc="top", fontsize=16)

    r = 1

    x, y = make_circle(radius=r)
    ax.plot(x, y, color="teal", lw=2)

    angle = 240
    angle = np.deg2rad(angle)
    ax.plot([0, r * np.cos(angle)], [0, r * np.sin(angle)], color="black", lw=1.5)
    ax.plot(
        [r * np.cos(angle), 0],
        [r * np.sin(angle)] * 2,
        color="black",
        lw=1.5,
        linestyle="--",
    )

    dx = dy = 0.1
    ax.plot(
        [0, -dx],
        [r * np.sin(angle) + dy, r * np.sin(angle) + dy],
        color="black",
        lw=1.5,
    )

    ax.plot(
        [-dx, -dx],
        [r * np.sin(angle) + dy, r * np.sin(angle)],
        color="black",
        lw=1.5,
    )

    angle = 240
    angle = np.deg2rad(angle)
    x, y = make_circle_arc(radius=0.2, start=0, end=angle)
    ax.plot(x, y, color="black", lw=1)

    ax.text(
        x=-0.2,
        y=0.2,
        s="$240^\\circ$",
        fontsize=16,
        ha="center",
        va="center",
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
