import plotmath
import matplotlib.pyplot as plt
import numpy as np
import sympy


def make_circle_arc(x0, y0, radius, start_angle, end_angle):
    theta = np.linspace(start_angle, end_angle, 1024)
    x = x0 + radius * np.cos(theta)
    y = y0 + radius * np.sin(theta)
    return x, y


def main(dirname, save):
    fontsize = 22
    # List of functions and their labels.
    functions = []

    fig, ax = plt.subplots()

    A = (0, 0)
    B = (4, 0)
    C = (4, 3)

    plotmath.plot_polygon(*[A, B, C], ax=ax, show_vertices=False)

    dx = dy = 0.1
    ax.text(
        x=A[0] - dx,
        y=A[1],
        s="$A$",
        fontsize=fontsize,
        verticalalignment="center",
        horizontalalignment="right",
    )

    ax.text(
        x=B[0] + dx,
        y=B[1],
        s="$B$",
        fontsize=fontsize,
        verticalalignment="center",
        horizontalalignment="left",
    )

    ax.text(
        x=C[0] + dx,
        y=C[1],
        s="$C$",
        fontsize=fontsize,
        verticalalignment="bottom",
        horizontalalignment="left",
    )

    dy = C[1] - B[1]
    dx = B[0] - A[0]
    angle = np.pi - np.arctan(dy / dx) - np.pi / 2
    radius = 0.5
    x, y = make_circle_arc(
        x0=C[0],
        y0=C[1],
        radius=radius,
        start_angle=-np.pi / 2,
        end_angle=-np.pi / 2 - angle,
    )
    ax.plot(x, y, color="black")

    AB = sympy.sqrt((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2)
    AC = sympy.sqrt((A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2)
    BC = sympy.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)
    AB = sympy.latex(AB)
    AC = sympy.latex(AC)
    BC = sympy.latex(BC)

    dx = dy = 0.1
    ax.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - dy,
        s=f"${AB}$",
        ha="center",
        va="top",
        fontsize=fontsize,
    )

    ax.text(
        x=0.5 * (A[0] + C[0]),
        y=0.5 * (A[1] + C[1]),
        s=f"${AC}$",
        ha="right",
        va="bottom",
        fontsize=fontsize,
    )

    dx = 0.1
    ax.text(
        x=0.5 * (B[0] + C[0]) + dx,
        y=0.5 * (B[1] + C[1]),
        s=f"${BC}$",
        ha="left",
        va="center",
        fontsize=fontsize,
    )

    dx = dy = 0.3
    plt.plot([B[0], B[0] - dx], [B[1] + dy, B[1] + dy], color="black")
    plt.plot([B[0] - dx, B[0] - dx], [B[1], B[1] + dy], color="black")

    # ax.set_xlim(0, 100)
    # ax.axis("equal")
    plt.xlim(-1, max(A[0], B[0], C[0]) + 1)
    plt.axis("equal")
    plt.tight_layout()
    ax.axis("off")

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
