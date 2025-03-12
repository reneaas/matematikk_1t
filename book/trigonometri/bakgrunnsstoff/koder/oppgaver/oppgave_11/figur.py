from casify import *


def make_circle_arc(center, radius, start_angle, end_angle, n=1024):
    import numpy as np

    angles = np.linspace(start_angle, end_angle, n)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


def main(dirname, save):
    # TODO: write code here
    import plotmath
    import matplotlib.pyplot as plt
    import numpy as np

    A = (0, 0)
    angle = np.pi / 3
    r = 3
    M = (r, r * np.tan(angle))
    B = (6, 0)
    C = (3, np.sqrt(6**2 - 3**2))

    M = (3, 3**0.5)

    plt.plot(*A, "ko", markersize=8, alpha=0.7)
    plt.plot(*B, "ko", markersize=8, alpha=0.7)
    plt.plot(*C, "ko", markersize=8, alpha=0.7)
    plt.plot(*M, "ko", markersize=8, alpha=0.7)

    plt.plot([A[0], M[0]], [A[1], M[1]], "k-")
    plt.plot([M[0], B[0]], [M[1], B[1]], "k-")
    plt.plot([B[0], C[0]], [B[1], C[1]], "k-")
    plt.plot([C[0], A[0]], [C[1], A[1]], "k-")
    plt.plot([M[0], C[0]], [M[1], C[1]], "k-")

    plt.text(
        x=A[0] - 0.1,
        y=A[1],
        s="$A$",
        fontsize=20,
        ha="right",
        va="top",
    )

    plt.text(
        x=B[0] + 0.1,
        y=B[1],
        s="$B$",
        fontsize=20,
        ha="left",
        va="top",
    )

    plt.text(
        x=C[0],
        y=C[1] + 0.1,
        s="$C$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    plt.text(
        x=M[0],
        y=M[1] - 0.3,
        s="$M$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ex = np.array([1, 0])
    AM = np.array(M) - np.array(A)
    AC = np.array(C) - np.array(A)
    start_angle = np.arccos(np.dot(AM, ex) / (np.linalg.norm(AM) * np.linalg.norm(ex)))
    end_angle = np.arccos(np.dot(AC, ex) / (np.linalg.norm(AC) * np.linalg.norm(ex)))

    print(np.degrees(start_angle), np.degrees(end_angle))

    x, y = make_circle_arc(
        center=A,
        radius=0.8,
        start_angle=start_angle,
        end_angle=end_angle,
    )
    plt.plot(x, y, "k-")

    BM = np.array(M) - np.array(B)
    BC = np.array(C) - np.array(B)

    start_angle = np.arccos(np.dot(BM, ex) / (np.linalg.norm(BM) * np.linalg.norm(ex)))
    end_angle = np.arccos(np.dot(BC, ex) / (np.linalg.norm(BC) * np.linalg.norm(ex)))

    x, y = make_circle_arc(
        center=B,
        radius=0.8,
        start_angle=start_angle,
        end_angle=end_angle,
    )

    plt.plot(x, y, "k-")

    CA = np.array(A) - np.array(C)
    CB = np.array(B) - np.array(C)

    ey = np.array([0, 1])
    start_angle = np.pi / 2 + np.arccos(
        np.dot(CA, ey) / (np.linalg.norm(CA) * np.linalg.norm(ey))
    )
    end_angle = np.pi / 2 + np.arccos(
        np.dot(CB, ey) / (np.linalg.norm(CB) * np.linalg.norm(ey))
    )

    print(end_angle)

    x, y = make_circle_arc(
        center=C,
        radius=1,
        start_angle=-np.pi / 2 - np.pi / 6,
        end_angle=-np.pi / 2 + np.pi / 6,
    )

    plt.plot(x, y, "k-")

    plt.text(
        x=C[0] + 0.15,
        y=C[1] - 1.4,
        s="$30^\\circ$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.text(
        x=C[0] - 0.15,
        y=C[1] - 1.4,
        s="$30^\\circ$",
        fontsize=20,
        ha="right",
        va="center",
    )

    plt.text(
        x=A[0] + 0.7,
        y=A[1] + 0.8,
        s="$30^\\circ$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.text(
        x=B[0] - 0.6,
        y=B[1] + 0.8,
        s="$30^\\circ$",
        fontsize=20,
        ha="right",
        va="center",
    )

    plt.text(
        x=0.5 * (A[0] + C[0]) - 0.3,
        y=0.5 * (A[1] + C[1]),
        s="$6$",
        fontsize=20,
        ha="left",
        va="bottom",
    )

    plt.axis("equal")
    plt.axis("off")

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
