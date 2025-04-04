from casify import *


def make_circle_arc(radius, start, stop, n=1024):
    import numpy as np

    theta = np.linspace(start, stop, n)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import numpy as np

    angle = np.radians(30)
    l = 1 / np.cos(angle)
    A = (0, 0)
    B = (l, 0)
    C = (l * np.cos(np.pi / 3), l * np.sin(np.pi / 3))

    ax = draw_triangle(
        A,
        B,
        C,
        show=False,
        radius=0.15,
        fontsize=20,
        label_angles=(False, True, True),
        label_sides=("\\ell", "\\ell", "\\ell"),
        vertex_labels=("A", "B", "C"),
        numerical_len=False,
        alpha=0.05,
    )

    x, y = make_circle_arc(radius=1, start=-0.1, stop=np.pi / 3 + 0.1)

    ax.plot(x, y, color="black", lw=1.5, ls="--", alpha=0.4)

    mid_x = 0.5 * (B[0] + C[0])
    mid_y = 0.5 * (B[1] + C[1])

    ax.plot([0, mid_x], [0, mid_y], color="black", ls="--", lw=1.5)

    ax.text(
        x=0.45,
        y=0.38,
        s="$1$",
        fontsize=20,
        ha="left",
        va="top",
    )

    x, y = make_circle_arc(radius=0.2, start=0, stop=np.pi / 3)
    ax.plot(x, y, "k-", lw=1)

    ax.text(
        x=0.3 * np.cos(np.pi / 6),
        y=0.03,
        s="$30^\\circ$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    ax.text(
        x=0.20,
        y=0.16,
        s="$30^\\circ$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    dist = 0.05
    u = np.array([np.cos(np.pi / 6), np.sin(np.pi / 6)])
    u_normal = np.array([-u[1], u[0]])

    r_start = np.array([mid_x, mid_y])
    r_end = r_start - dist * u_normal
    ax.plot([r_start[0], r_end[0]], [r_start[1], r_end[1]], "k-", lw=1.5)

    r_start = np.array([mid_x, mid_y])
    r_start = r_start - dist * u
    r_end = r_start + dist * u_normal
    ax.plot([r_start[0], r_end[0]], [r_start[1], r_end[1]], "k-", lw=1.5)

    r_start, r_end = r_end, r_start
    r_end = r_start + dist * u
    ax.plot([r_start[0], r_end[0]], [r_start[1], r_end[1]], "k-", lw=1.5)

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory
    else:
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
