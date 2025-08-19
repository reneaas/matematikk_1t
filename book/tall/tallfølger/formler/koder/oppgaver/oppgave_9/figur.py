import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname: str, save: bool = True) -> None:
    """Visualise *rectangular numbers* n(n+1) using colored rectangles.

    The *n*-th figure shows an n×(n+1) rectangle with the lower diagonal in red
    and the upper diagonal in blue. This demonstrates that rectangular numbers
    are twice the triangular numbers. The number of dots is the **quadratic** polynomial

        p(n) = n(n + 1),

    yielding the sequence 2, 6, 12, 20, 30, … (OEIS A002378).
    """

    dot_size = 80  # size of each dot

    def r(t):
        return t * np.array([np.cos(t), np.sin(t)])

    def draw_spiral_dots(ax, spacing, n):
        t = np.linspace(0, n * spacing, n + 1)

        r = lambda t: t * np.array([np.cos(t), np.sin(t)])
        ax.scatter(
            *r(t),
            s=dot_size,
            color=plotmath.COLORS.get("blue"),
            alpha=0.8,
            edgecolor="black",
        )

        r = lambda t: t * np.array(
            [np.cos(t + 2 * np.pi / 3), np.sin(t + 2 * np.pi / 3)]
        )
        ax.scatter(
            *r(t),
            s=dot_size,
            color=plotmath.COLORS.get("blue"),
            alpha=0.8,
            edgecolor="black",
        )

        r = lambda t: t * np.array(
            [np.cos(t + 4 * np.pi / 3), np.sin(t + 4 * np.pi / 3)]
        )
        ax.scatter(
            *r(t),
            s=dot_size,
            color=plotmath.COLORS.get("blue"),
            alpha=0.8,
            edgecolor="black",
        )

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 3  # show n = 1, 2, 3, 4 (values: 2, 6, 12, 20)
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(8, 3),  # ~4″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 0.3  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        # draw_rectangular_dots(axs[i], spacing=spacing, n=n)
        draw_spiral_dots(axs[i], spacing=spacing, n=n**2)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        value = n * (n + 1)
        triangular = n * (n + 1) // 2
        ax.text(
            x=0,
            y=-11 * spacing,
            s=f"Figur {n}",
            fontsize=20,
            ha="center",
            va="center",
            weight="bold",
        )

        # Set limits to accommodate the largest pattern
        limit = (max_n + 1) * spacing / 2 + 0.5
        ax.set_xlim(-n, n)
        ax.set_ylim(-n, n)

    # ──────────────────────────────────────────────────────────────────
    # Output ───────────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
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
