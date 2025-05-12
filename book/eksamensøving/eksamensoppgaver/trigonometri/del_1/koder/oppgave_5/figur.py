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
    fig, ax = plt.subplots(figsize=(3, 4))

    A = (0, 0)
    B = (1, 0)
    C = (1, 3**0.5)

    plotmath.plot_polygon(
        A,
        B,
        C,
        alpha=0.05,
    )

    angle = 60
    start = 0
    end = start + angle
    x0, y0 = make_angle_arc(A, radius=0.3, start_angle=start, end_angle=end)
    ax.plot(x0, y0, color="black", lw=1.5)

    ax.text(
        x=A[0] + 0.45,
        y=A[1] + 0.2,
        s=r"$60^\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    angle = 30
    start = 90 + 180
    end = start - angle
    x0, y0 = make_angle_arc(C, radius=0.4, start_angle=start, end_angle=end)
    ax.plot(x0, y0, color="black", lw=1.5)

    ax.text(
        x=C[0] - 0.12,
        y=C[1] - 0.55,
        s=r"$30^\circ$",
        fontsize=20,
        ha="center",
        va="center",
    )

    dx = dy = 0.2
    ax.plot([1, 1 - dx], [dy, dy], color="black", lw=1.5)
    ax.plot([1 - dx, 1 - dx], [0, dy], color="black", lw=1.5)

    ax.text(
        x=0.5 * (A[0] + C[0]) - 0.05,
        y=0.5 * (A[1] + C[1]) + 0.05,
        s="$2$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    ax.text(
        x=0.5 * (B[0] + C[0]) + 0.05,
        y=0.5 * (B[1] + C[1]),
        s=r"$\sqrt{3}$",
        fontsize=20,
        ha="left",
        va="center",
    )

    ax.text(
        x=0.5 * (A[0] + B[0]),
        y=0.5 * (A[1] + B[1]) - 0.05,
        s="$1$",
        fontsize=20,
        ha="center",
        va="top",
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
