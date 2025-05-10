import plotmath
import numpy as np
import matplotlib.pyplot as plt
import math


def rotate_point(p, angle_deg, origin=(0, 0)):
    """
    Rotate point p=(x,y) around origin by angle_deg degrees.
    """
    theta = math.radians(angle_deg)
    ox, oy = origin
    px, py = p
    qx = ox + math.cos(theta) * (px - ox) - math.sin(theta) * (py - oy)
    qy = oy + math.sin(theta) * (px - ox) + math.cos(theta) * (py - oy)
    return (qx, qy)


def make_angle_arc(center, radius, start_angle, end_angle):
    start_angle = np.deg2rad(start_angle)
    end_angle = np.deg2rad(end_angle)
    theta = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y


def main(dirname, save, rotation_deg=0):
    a = 1

    A0 = (0, 0)
    B0 = (a, 0)

    angle = 180 - 30 - 75
    angle = np.deg2rad(angle)
    BC = np.sqrt(2) * a
    C0 = (B0[0] + BC * np.cos(angle), B0[1] + BC * np.sin(angle))

    AD = a
    angle = 120
    D0 = (AD * np.cos(np.deg2rad(angle)), AD * np.sin(np.deg2rad(angle)))

    # Rotate corners
    A = rotate_point(A0, rotation_deg)
    B = rotate_point(B0, rotation_deg)
    C = rotate_point(C0, rotation_deg)
    D = rotate_point(D0, rotation_deg)

    # Plot polygon
    plotmath.plot_polygon(A, B, C, D, alpha=0.03)
    ax = plt.gca()
    ax.plot(*zip(B, D), color="black", ls="--")
    ax.axis("off")
    ax.axis("equal")

    # Angle arc at A
    start = 0
    end = 120
    x0, y0 = make_angle_arc(A0, radius=0.1, start_angle=start, end_angle=end)
    pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    x2, y2 = zip(*pts2)
    ax.plot(x2, y2, color="black")
    tx, ty = rotate_point((A0[0] + 0.1, A0[1] + 0.15), rotation_deg)
    ax.text(tx, ty, r"$120^\circ$", fontsize=20, ha="center", va="center")

    # Angle arc at B
    start = 180 - 30
    end = start - 75
    x0, y0 = make_angle_arc(B0, radius=0.15, start_angle=start, end_angle=end)
    pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    x2, y2 = zip(*pts2)
    ax.plot(x2, y2, color="black")
    tx, ty = rotate_point((B0[0] - 0.05, B0[1] + 0.2), rotation_deg)
    ax.text(tx, ty, r"$75^\circ$", fontsize=20, ha="center", va="center")

    # Angle arc at BDA
    start = 120 + 180
    end = start + 30
    x0, y0 = make_angle_arc(D0, radius=0.25, start_angle=start, end_angle=end)
    pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    x2, y2 = zip(*pts2)
    ax.plot(x2, y2, color="black")
    tx, ty = rotate_point((D0[0] + 0.25, D0[1] - 0.25), rotation_deg)
    ax.text(tx, ty, r"$30^\circ$", fontsize=20, ha="center", va="center")

    # Side labels
    # AB = 4
    # mid_ab = ((A0[0] + B0[0]) / 2, (A0[1] + B0[1]) / 2 - 0.5)
    # tx, ty = rotate_point(mid_ab, rotation_deg)
    # ax.text(tx, ty, r"$10$", fontsize=20, ha="center", va="center")

    # BC = 8
    # mid_bc = ((B0[0] + C0[0]) / 2 + 0.5, (B0[1] + C0[1]) / 2)
    # tx, ty = rotate_point(mid_bc, rotation_deg)
    # ax.text(tx, ty, r"$5$", fontsize=20, ha="center", va="center")

    # AD = 4
    # mid_ad = ((A0[0] + D0[0]) / 2 - 0.5, (A0[1] + D0[1]) / 2)
    # tx, ty = rotate_point(mid_ad, rotation_deg)
    # ax.text(tx, ty, r"$6$", fontsize=20, ha="center", va="center")

    # BC
    mid_bc = ((B0[0] + C0[0]) / 2 + 0.15, (B0[1] + C0[1]) / 2)
    tx, ty = rotate_point(mid_bc, rotation_deg)
    ax.text(tx, ty, r"$\sqrt{2} \cdot a$", fontsize=20, ha="center", va="center")

    # Label corners

    ax.text(A[0], A[1], r"$A$", fontsize=20, ha="right", va="top")
    ax.text(B[0], B[1], r"$B$", fontsize=20, ha="left", va="top")
    ax.text(C[0], C[1], r"$C$", fontsize=20, ha="left", va="bottom")
    ax.text(D[0], D[1], r"$D$", fontsize=20, ha="right", va="center")

    plt.tight_layout()

    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(dirname=dirname, fname=fname)
    else:
        plotmath.show()


if __name__ == "__main__":
    import pathlib

    # Determine figure output directory
    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break
    dirname = "/".join(parts)

    # Call with desired rotation, e.g. 30°
    main(dirname=dirname, save=True, rotation_deg=0)
