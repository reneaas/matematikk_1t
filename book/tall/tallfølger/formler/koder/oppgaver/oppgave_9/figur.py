import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    alpha = 0.6

    def draw_diamond_cross(ax, s, n):
        """
        Creates a diamond-cross pattern that grows outward.
        The pattern forms a cross with diamond endpoints.
        For n=1: central cross
        For n=2: cross extends 1 step in each direction
        For n=3: cross extends 2 steps in each direction
        """

        # Center cross - always present
        center_positions = [(0, 0)]

        # Horizontal arm extends n-1 steps in each direction
        for i in range(1, n):
            center_positions.extend([(-i, 0), (i, 0)])

        # Vertical arm extends n-1 steps in each direction
        for j in range(1, n):
            center_positions.extend([(0, -j), (0, j)])

        # Add diamond tips at the ends (only for n > 1)
        if n > 1:
            # Diamond tips at the four cardinal directions
            tip_distance = n - 1
            diamond_tips = [
                # North diamond
                (0, tip_distance + 1),
                (-1, tip_distance),
                (1, tip_distance),
                # South diamond
                (0, -(tip_distance + 1)),
                (-1, -tip_distance),
                (1, -tip_distance),
                # East diamond
                (tip_distance + 1, 0),
                (tip_distance, -1),
                (tip_distance, 1),
                # West diamond
                (-(tip_distance + 1), 0),
                (-tip_distance, -1),
                (-tip_distance, 1),
            ]
            center_positions.extend(diamond_tips)

        # Draw all squares
        for i, j in center_positions:
            A = (i * s, j * s)
            B = ((i + 1) * s, j * s)
            C = ((i + 1) * s, (j + 1) * s)
            D = (i * s, (j + 1) * s)

            color = plotmath.COLORS.get("blue")
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

    # --- merge into one figure ---
    fig, axs = plt.subplots(
        1,
        4,
        figsize=(8, 3),  # 3″ per subplot
        sharex=True,
        sharey=True,  # same data‐to‐pixel scale
        constrained_layout=True,
    )

    # draw each with the same s=1
    s = 1
    draw_diamond_cross(axs[0], s=s, n=1)
    draw_diamond_cross(axs[1], s=s, n=2)
    draw_diamond_cross(axs[2], s=s, n=3)
    draw_diamond_cross(axs[3], s=s, n=4)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")  # 1 unit = 1 unit
        ax.axis("off")
        ax.text(
            x=0,  # Center horizontally
            y=-4 * s,  # Position below the figure
            s=f"Figur {i+1}",
            fontsize=22,
            ha="center",
            va="center",
        )
        # fix axis‐limits so each square shows at the same scale
        # ax.set_xlim(-1, (4 + 1) * 1)  # max_n=4 in this example
        # ax.set_ylim(-(4 + 1) * 1, (4) * 1)

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
    main(dirname=dirname, save=False)
