import plotmath
import matplotlib.pyplot as plt
import numpy as np


def hex_vertices(
    center: np.ndarray, radius: float, theta0: float = np.pi / 2
) -> np.ndarray:
    """Return the 5 vertices of a regular pentagon as an array of shape (5, 2).

    theta0 is the orientation; default points one vertex straight up.
    """
    angles = theta0 + 2 * np.pi * np.arange(5) / 5
    pts = np.c_[np.cos(angles), np.sin(angles)] * radius + center
    return pts


def draw_hex(
    ax, center: np.ndarray, radius: float, side_points: int = 0, dot_size: int = 80
):
    """Draw a regular pentagon with given center and radius.

    - side_points = 0: only vertices
    - side_points = 1: 1 circle per side (midpoint)
    - side_points = 2: 2 circles per side (at 1/3 and 2/3)

    Circles are drawn at vertices and at the specified positions on each side.
    Lines connect the circles along each side in order.
    """
    V = hex_vertices(center, radius)  # (5, 2)

    # Assemble points along each side in drawing order
    # For each edge Vi -> V(i+1)
    polys = []  # list of arrays of shape (n, 2) containing [Vi, ..., V(i+1)]
    points = []  # collect unique points to scatter later

    # Parameters t along the side for extra points
    if side_points == 0:
        ts = []
    elif side_points == 1:
        # Use 1/3 (not 1/2) so that Figure 3's points are a subset of Figure 4's (1/3, 2/3)
        ts = [1.0 / 3.0]
    elif side_points == 2:
        ts = [1.0 / 3.0, 2.0 / 3.0]
    else:
        # Generic spacing if someone passes >2
        ts = [j / (side_points + 1) for j in range(1, side_points + 1)]

    for i in range(5):
        v0 = V[i]
        v1 = V[(i + 1) % 5]
        # Points along the side
        side_pts = [v0 + t * (v1 - v0) for t in ts]
        poly = np.vstack([v0, *side_pts, v1])
        polys.append(poly)
        points.append(v0)
        points.extend(side_pts)
    # Add the final vertex once (to include V4 that isn't appended as v0 in the loop)
    points.append(V[-1])

    # Deduplicate scattered points via rounding-based key
    P = np.array(points)
    key = np.round(P, 10)
    _, idx = np.unique(key, axis=0, return_index=True)
    P = P[np.sort(idx)]

    # Draw polylines for each side
    for poly in polys:
        ax.plot(poly[:, 0], poly[:, 1], color="black", linewidth=2)

    # Draw circles
    color = plotmath.COLORS.get("blue", "tab:blue")
    ax.scatter(P[:, 0], P[:, 1], s=dot_size, color=color, edgecolor="black", zorder=3)


def build_hex_polys_and_points(center: np.ndarray, radius: float, side_points: int = 0):
    """Return (polylines, points) for a regular pentagon without drawing.

    - polylines: list of arrays, each array is the sequence of points along one side
      [V_i, (side points...), V_{i+1}].
    - points: array of shape (M, 2) containing all unique circles to plot
      (all 5 vertices + side points across all sides).
    """
    V = hex_vertices(center, radius)  # (5, 2)

    # Parameters t along the side for extra points
    if side_points == 0:
        ts = []
    elif side_points == 1:
        ts = [0.5]
    elif side_points == 2:
        ts = [1.0 / 3.0, 2.0 / 3.0]
    else:
        ts = [j / (side_points + 1) for j in range(1, side_points + 1)]

    polylines = []
    extra_pts = []
    for i in range(5):
        v0 = V[i]
        v1 = V[(i + 1) % 5]
        side_pts = [v0 + t * (v1 - v0) for t in ts]
        polylines.append(np.vstack([v0, *side_pts, v1]))
        extra_pts.extend(side_pts)

    # Unique points to scatter: all vertices + all side points
    if extra_pts:
        P = np.vstack([V, np.array(extra_pts)])
    else:
        P = V.copy()
    # Round to deduplicate robustly
    key = np.round(P, 10)
    _, idx = np.unique(key, axis=0, return_index=True)
    P = P[np.sort(idx)]

    return polylines, P


def main(dirname: str, save: bool = True) -> None:
    """Create four subplots:

    1) Single circle.
    2) One pentagon with vertex circles connected by lines.
    3) Previous pentagon + a larger pentagon around it sharing one vertex; larger has 1 circle per side.
    4) Previous two + another larger pentagon sharing the same vertex; this new one has 2 circles per side.
    """

    dot_size = 80

    fig, axs = plt.subplots(
        1,
        4,
        figsize=(9, 3),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Common settings
    ax_lim = 2.8
    theta_anchor = np.pi / 2 + 4 * np.pi / 5  # bottom-left vertex (234 degrees)

    # 1) Single circle (place at the common anchor vertex position)
    ax = axs[0]
    color = plotmath.COLORS.get("blue", "tab:blue")
    # Anchor unit vector (for the shared vertex)
    u = np.array([np.cos(theta_anchor), np.sin(theta_anchor)])
    v_anchor = np.array([0.0, 0.0]) + 1.0 * u  # with r1=1.0 and C1=(0,0)
    ax.scatter(
        [v_anchor[0]],
        [v_anchor[1]],
        s=dot_size,
        color=color,
        edgecolor="black",
        zorder=3,
    )
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)

    # Inner pentagon (common to figures 2, 3, 4)
    C1 = np.array([0.0, -0.5])
    r1 = 0.6
    # Reuse u, compute anchor from C1,r1 for later figures
    v_anchor = C1 + r1 * u

    # 2) Single pentagon with only vertex circles
    ax = axs[1]
    polys, P = build_hex_polys_and_points(C1, r1, side_points=0)
    for poly in polys:
        ax.plot(poly[:, 0], poly[:, 1], color="black", linewidth=2)
    color = plotmath.COLORS.get("blue", "tab:blue")
    ax.scatter(P[:, 0], P[:, 1], s=dot_size, color=color, edgecolor="black", zorder=3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)

    # 3) Inner pentagon + larger pentagon sharing one vertex, with 1 point per side
    ax = axs[2]
    # Build and draw polylines for both pentagons
    polys1, P1 = build_hex_polys_and_points(C1, r1, side_points=0)
    r2 = 2.0 * r1
    C2 = v_anchor - r2 * u  # ensures the vertex at theta_anchor coincides with v_anchor
    polys2, P2 = build_hex_polys_and_points(C2, r2, side_points=1)
    for poly in polys1 + polys2:
        ax.plot(poly[:, 0], poly[:, 1], color="black", linewidth=2)
    # Scatter deduped union of points
    P = np.vstack([P1, P2])
    key = np.round(P, 10)
    _, idx = np.unique(key, axis=0, return_index=True)
    P = P[np.sort(idx)]
    color = plotmath.COLORS.get("blue", "tab:blue")
    ax.scatter(P[:, 0], P[:, 1], s=dot_size, color=color, edgecolor="black", zorder=3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)

    # 4) Previous two + yet larger pentagon sharing the same vertex, with 2 points per side
    ax = axs[3]
    polys1, P1 = build_hex_polys_and_points(C1, r1, side_points=0)
    polys2, P2 = build_hex_polys_and_points(C2, r2, side_points=1)
    r3 = 3.0 * r1
    C3 = v_anchor - r3 * u
    polys3, P3 = build_hex_polys_and_points(C3, r3, side_points=2)
    for poly in polys1 + polys2 + polys3:
        ax.plot(poly[:, 0], poly[:, 1], color="black", linewidth=2)
    # Scatter deduped union of points
    P = np.vstack([P1, P2, P3])
    key = np.round(P, 10)
    _, idx = np.unique(key, axis=0, return_index=True)
    P = P[np.sort(idx)]
    color = plotmath.COLORS.get("blue", "tab:blue")
    ax.scatter(P[:, 0], P[:, 1], s=dot_size, color=color, edgecolor="black", zorder=3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)

    # Optional labels under each subplot (kept subtle, inside limits)
    labels = [
        "Figur 1",
        "Figur 2",
        "Figur 3",
        "Figur 4",
    ]
    for i, ax in enumerate(axs):
        ax.text(
            0,
            -ax_lim * 0.9,
            labels[i],
            ha="center",
            va="center",
            fontsize=20,
            weight="bold",
        )

    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(dirname=dirname, fname=fname)
    else:
        plotmath.show()


if __name__ == "__main__":
    import pathlib

    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)
    main(dirname=dirname, save=True)
