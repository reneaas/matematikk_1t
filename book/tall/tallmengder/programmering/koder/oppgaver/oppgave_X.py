import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """
    Draw three ‘diamond’ figures side by side.
    Each diamond of order n has p(n) = 2n^2 + 2n + 1 small squares,
    arranged so row k (–n ≤ k ≤ n) has 2(n – |k|)+1 squares.
    """
    alpha = 0.2
    s = 1  # side length of each small square
    orders = [1, 2, 3]  # n=1,2,3
    n_max = max(orders)

    def draw_diamond(ax, n):
        for k in range(-n, n + 1):
            row_len = 2 * (n - abs(k)) + 1
            # center each row horizontally:
            x0 = -row_len * s / 2
            y0 = k * s
            for j in range(row_len):
                A = (x0 + j * s, y0)
                B = (x0 + (j + 1) * s, y0)
                C = (x0 + (j + 1) * s, y0 + s)
                D = (x0 + j * s, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha)

    # --- set up subplots ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(9, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # draw each diamond
    for ax, n in zip(axs, orders):
        draw_diamond(ax, n)
        ax.set_aspect("equal")
        ax.axis("off")

    # annotate and fix limits so that scale is identical
    lim = (n_max + 0.5) * s
    # annotate and fix limits so that each figure fully contains its diamond
    for i, ax in enumerate(axs):
        n = orders[i]
        # horizontal half‐width = (2n+1)/2 · s = (n + 0.5)*s
        x_half = (n + 0.5) * s
        # vertical extent: bottom at y=−n·s, top at y=(n+1)·s
        y_min = -n * s
        y_max = (n + 1) * s

        ax.set_xlim(-x_half, x_half)
        ax.set_ylim(y_min, y_max)
        ax.text(
            x=0,
            y=-4,
            s=f"Figur {i+1}",
            fontsize=16,
            ha="center",
            va="bottom",
        )

    # save or show
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
