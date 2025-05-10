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
    # Define original corner points
    a = 1
    x = 2 * np.sqrt(3) * a
    y = (np.sin(np.deg2rad(75)) / np.sin(np.deg2rad(45))) * x
    z = (np.sin(np.deg2rad(60)) / np.sin(np.deg2rad(45))) * x

    A0 = (0, 0)
    B0 = (z, 0)
    D0 = (y * np.cos(np.deg2rad(45)), y * np.sin(np.deg2rad(45)))
    angle = 180 - 75 - 30
    angle = np.deg2rad(angle)
    C0 = (B0[0] + 2 * a * np.cos(angle), B0[1] + 2 * a * np.sin(angle))

    # Rotate corners
    A = rotate_point(A0, rotation_deg)
    B = rotate_point(B0, rotation_deg)
    C = rotate_point(C0, rotation_deg)
    D = rotate_point(D0, rotation_deg)

    # Plot polygon
    plotmath.plot_polygon(A, B, D, alpha=0.03)
    plotmath.plot_polygon(B, C, D, alpha=0.03)
    ax = plt.gca()
    ax.axis("off")
    ax.axis("equal")

    # Angle arc at A
    start = 0
    end = 45
    x0, y0 = make_angle_arc(A0, radius=0.6, start_angle=start, end_angle=end)
    pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    x2, y2 = zip(*pts2)
    ax.plot(x2, y2, color="black")
    tx, ty = rotate_point((A0[0] + 0.9, A0[1] + 0.4), rotation_deg)
    ax.text(tx, ty, r"$45^\circ$", fontsize=20, ha="center", va="center")

    # Angle arc at B
    start = 180
    end = 180 - 75
    x0, y0 = make_angle_arc(B0, radius=0.4, start_angle=start, end_angle=end)
    pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    x2, y2 = zip(*pts2)
    ax.plot(x2, y2, color="black")
    tx, ty = rotate_point((B0[0] - 0.6, B0[1] + 0.4), rotation_deg)
    ax.text(tx, ty, r"$75^\circ$", fontsize=20, ha="center", va="center")

    # Angle arc at D
    # start = 60 + 180
    # end = 60 + 180 + 120
    # x0, y0 = make_angle_arc(D0, radius=0.4, start_angle=start, end_angle=end)
    # pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    # x2, y2 = zip(*pts2)
    # ax.plot(x2, y2, color="black")
    # tx, ty = rotate_point((D0[0] + 0.3, D0[1] - 0.6), rotation_deg)
    # ax.text(tx, ty, r"$120^\circ$", fontsize=20, ha="center", va="center")

    # Angle arc at C
    start = 180 - 75 - 30 + 180
    end = start - 120
    x0, y0 = make_angle_arc(C0, radius=0.3, start_angle=start, end_angle=end)
    pts2 = [rotate_point((x0[i], y0[i]), rotation_deg) for i in range(len(x0))]
    x2, y2 = zip(*pts2)
    ax.plot(x2, y2, color="black")
    tx, ty = rotate_point((C0[0] - 0.55, C0[1] - 0.15), rotation_deg)
    ax.text(tx, ty, r"$120^\circ$", fontsize=20, ha="center", va="center")

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

    # CD
    mid_cd = ((C0[0] + D0[0]) / 2, (C0[1] + D0[1]) / 2)
    tx, ty = rotate_point(mid_cd, rotation_deg)
    ax.text(tx, ty, r"$2a$", fontsize=20, ha="left", va="bottom")

    # BC
    mid_bc = ((B0[0] + C0[0]) / 2 + 0.3, (B0[1] + C0[1]) / 2)
    tx, ty = rotate_point(mid_bc, rotation_deg)
    ax.text(tx, ty, r"$2a$", fontsize=20, ha="center", va="center")

    # Label corners

    ax.text(A[0], A[1], r"$A$", fontsize=20, ha="right", va="top")
    ax.text(B[0], B[1], r"$B$", fontsize=20, ha="left", va="center")
    ax.text(C[0], C[1], r"$C$", fontsize=20, ha="left", va="bottom")
    ax.text(D[0], D[1], r"$D$", fontsize=20, ha="right", va="bottom")

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
    main(dirname=dirname, save=True, rotation_deg=40)
