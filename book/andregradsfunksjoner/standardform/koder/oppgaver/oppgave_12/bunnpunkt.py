import plotmath
import numpy as np
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt


def make_circle(x0, y0, r):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = x0 + r * np.cos(theta)
    y = y0 + r * np.sin(theta)
    return x, y


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return (x - 4) ** 2 + 2

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-1,
        xmax=8,
        ymin=-2,
        ymax=16,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        fontsize=20,
    )

    points = [i for i in range(1, 7, 1)]
    labels = [f"$x_{i}$" for i in range(1, len(points) + 1)]

    ax.set_xticks(points)
    ax.set_xticklabels(labels, fontsize=20)

    ax.set_xlabel("$x$", fontsize=20, loc="right")
    ax.set_ylabel("$y$", fontsize=20, loc="top")

    for point in points:
        if f(point) > 0:
            ax.vlines(
                x=point,
                ymin=0,
                ymax=f(point),
                color="black",
                linestyle="--",
                alpha=0.5,
            )
        else:
            ax.vlines(
                x=point,
                ymin=f(point),
                ymax=0,
                color="black",
                linestyle="--",
                alpha=0.5,
            )

    dy = 0.5
    dx = 2
    # ax.arrow(
    #     x=2,
    #     y=10,  # Start point
    #     dx=1,
    #     dy=-3,  # Direction and length
    #     head_width=0.2,  # Width of arrow head
    #     head_length=0.3,  # Length of arrow head
    #     fc="black",  # Fill color
    #     ec="black",  # Edge color
    #     length_includes_head=True,
    # )  # Length includes the head

    start = (2, 10)  # (x, y) of start point
    end = (3, 6)  # (x, y) of end point
    # arrow = ConnectionPatch(
    #     xyA=start,  # start point
    #     xyB=end,  # end point
    #     coordsA="data",  # coordinate system for start point
    #     coordsB="data",  # coordinate system for end point
    #     axesA=ax,  # reference axes
    #     axesB=ax,  # reference axes
    #     arrowstyle="->",  # arrow style
    #     shrinkB=0,  # don't shrink the end
    #     mutation_scale=20,  # arrow head size
    #     fc="black",  # fill color
    #     ec="black",  # edge color
    # )

    # ax.add_patch(arrow)

    for point in points:
        if point < 4:
            ax.plot(point, f(point), "bo", markersize=8)
        else:
            ax.plot(point, f(point), "ro", markersize=8)

    x, y = make_circle(x0=4, y0=-1, r=0.5)
    ax.plot(x, y, color="red", linestyle="--", alpha=1)

    plt.annotate(
        text="$f(x) > f(x + 1)$",
        xy=(1, f(1)),
        xytext=(1, 14),
        fontsize=20,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text="$f(x) > f(x + 1)$",
        xy=(2, f(2)),
        xytext=(1, 14),
        fontsize=20,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=-0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text="$f(x) \\leq f(x + 1)$",
        xy=(4, f(4)),
        xytext=(4, 10),
        fontsize=20,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    plt.annotate(
        text="$f(x) \\leq f(x + 1)$",
        xy=(5, f(5)),
        xytext=(4, 10),
        fontsize=20,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
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
