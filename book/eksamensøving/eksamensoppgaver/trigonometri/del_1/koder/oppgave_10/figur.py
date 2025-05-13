import plotmath
import numpy as np
import matplotlib.pyplot as plt


def make_angle_arc(center, radius, start_angle, end_angle):
    start_angle = np.deg2rad(start_angle)
    end_angle = np.deg2rad(end_angle)
    theta = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y


def main(dirname, save):
    # TODO: write code here
    fig, ax = plt.subplots(figsize=(3, 3))

    A = (0, 0)
    B = (8, 0)
    C = (8, 6)

    plotmath.plot_polygon(
        A,
        B,
        C,
        alpha=0.05,
    )

    angle = np.arcsin(3 / 5)
    angle = np.rad2deg(angle)
    start = 0
    end = start + angle
    x0, y0 = make_angle_arc(A, radius=1.2, start_angle=start, end_angle=end)
    ax.plot(x0, y0, color="black", lw=1.5)

    # ax.text(
    #     x=A[0] + 0.45,
    #     y=A[1] + 0.2,
    #     s=r"$60^\circ$",
    #     fontsize=20,
    #     ha="center",
    #     va="center",
    # )

    # ax.text(
    #     x=C[0] - 0.12,
    #     y=C[1] - 0.55,
    #     s=r"$30^\circ$",
    #     fontsize=20,
    #     ha="center",
    #     va="center",
    # )

    dx = dy = 0.8
    ax.plot([B[0], B[0] - dx], [dy, dy], color="black", lw=1.5)
    ax.plot([B[0] - dx, B[0] - dx], [0, dy], color="black", lw=1.5)

    # Label vertices
    ax.text(
        x=A[0] - 0.5,
        y=A[1] - 0.5,
        s="$A$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=B[0] + 0.5,
        y=B[1] - 0.5,
        s="$B$",
        fontsize=20,
        ha="center",
        va="center",
    )

    ax.text(
        x=C[0] + 0.5,
        y=C[1] + 0.5,
        s="$C$",
        fontsize=20,
        ha="center",
        va="center",
    )

    plt.axis("off")
    plt.axis("equal")
    plt.tight_layout()

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
