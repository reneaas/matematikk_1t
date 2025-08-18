import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    alpha = 0.6

    def draw_corner(ax, s, n):
        # Calculate the center position for the 2x2 square to remove
        grid_size = n + 3
        center_start = grid_size // 2 - 1
        center_end = center_start + 1

        # Calculate offset to center the grid around origin
        offset = -grid_size / 2

        for i in range(grid_size):
            for j in range(grid_size):
                # Skip the center 2×2 square
                if center_start <= i <= center_end and center_start <= j <= center_end:
                    continue

                # Apply offset to center the grid
                A = ((i + offset) * s, (j + offset) * s)
                B = ((i + 1 + offset) * s, (j + offset) * s)
                C = ((i + 1 + offset) * s, (j + 1 + offset) * s)
                D = ((i + offset) * s, (j + 1 + offset) * s)

                color = plotmath.COLORS.get("blue")
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

    # --- merge into one figure ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(8, 3.5),  # 3″ per subplot
        sharex=True,
        sharey=True,  # same data‐to‐pixel scale
        constrained_layout=True,
    )

    # draw each with the same s=1
    s = 1
    draw_corner(axs[0], s=s, n=1)
    draw_corner(axs[1], s=s, n=3)
    draw_corner(axs[2], s=s, n=5)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")  # 1 unit = 1 unit
        ax.axis("off")
        ax.text(
            x=0,
            y=-5 * s,
            s=f"Figur {i+1}",
            fontsize=22,
            ha="center",
            va="center",
        )
        # fix axis‐limits so each square shows at the same scale
        # ax.set_xlim(-1, (4 + 1) * 1)  # max_n=4 in this example
        # ax.set_ylim(-(4 + 1) * 1, (4) * 1)

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
