import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here

    A = (0, 0)
    C = (2 * np.cos(np.pi / 6), 2 * np.sin(np.pi / 6))
    B = (C[0], 0)

    AD = np.sqrt(7)
    CD = 3
    AC = 2

    D_angle = np.arccos((AC**2 - AD**2 - CD**2) / (-2 * AD * CD))

    CAD = np.pi - np.pi / 3 - D_angle

    D = [AD * np.cos(CAD + np.pi / 6), AD * np.sin(CAD + np.pi / 6)]
    D = tuple(D)

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        color="teal",
        alpha=0.05,
    )

    plt.text(
        x=0,
        y=-0.2,
        s="$A$",
        fontsize=20,
        ha="center",
    )

    plt.text(
        x=B[0] + 0.1,
        y=-0.2,
        s="$B$",
        fontsize=20,
        ha="right",
    )

    plt.text(
        x=C[0] + 0.2,
        y=C[1],
        s="$C$",
        fontsize=20,
        ha="right",
        va="center",
    )

    plt.text(
        x=D[0] - 0.2,
        y=D[1],
        s="$D$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=-0.2,
        s="$\\sqrt{3}$",
        fontsize=20,
        ha="center",
    )

    plt.text(
        x=B[0] + 0.1,
        y=0.5 * (B[1] + C[1]),
        s="$1$",
        fontsize=20,
        va="center",
    )

    plt.text(
        x=-0.7,
        y=0.45 * np.sqrt(7),
        s="$\\sqrt{7}$",
        fontsize=20,
        ha="center",
    )

    theta = np.linspace(3 * np.pi / 2 - np.pi / 3, 3 * np.pi / 2, 1024)
    r = 0.3
    x = C[0] + r * np.cos(theta)
    y = C[1] + r * np.sin(theta)

    plt.plot(x, y, color="black", lw=0.8)

    theta = np.linspace(3 * np.pi / 2 - np.pi / 3, 3 * np.pi / 2 - 2 * np.pi / 3, 1024)
    r = 0.3
    x = C[0] + r * np.cos(theta)
    y = C[1] + r * np.sin(theta)

    plt.plot(x, y, color="black", lw=0.8)

    plt.text(
        x=C[0] - 0.45,
        y=C[1] - 0.25,
        s=r"$120^\circ$",
        fontsize=20,
        ha="center",
    )

    dx = dy = 0.2
    x, y = B

    plt.plot([x - dx, x], [y, y], color="black", lw=0.8)
    plt.plot([x - dx, x - dx], [y, y + dy], color="black", lw=0.8)
    plt.plot([x - dx, x], [y + dy, y + dy], color="black", lw=0.8)

    plt.axis("equal")
    plt.axis("off")

    # NOTE: Automatically saves with correct file format and filename.
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
