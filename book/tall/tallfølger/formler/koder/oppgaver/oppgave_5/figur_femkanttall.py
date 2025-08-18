import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname: str, save: bool = True) -> None:
    """Visualise *pentagonal numbers* (femkanttall) using dots arranged in pentagonal patterns.

    The *n*-th figure shows the n-th pentagonal number as dots arranged in a pentagonal shape.
    The number of dots is the **quadratic** polynomial

        p(n) = n(3n - 1)/2,

    yielding the sequence 1, 5, 12, 22, 35, … (OEIS A000326).
    """

    dot_size = 100  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw pentagonal pattern ──────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_pentagonal_dots(ax, spacing: float, n: int) -> None:
        """Plot dots in a pentagonal pattern for the n-th pentagonal number."""
        if n == 1:
            # Special case: just one dot at center
            ax.scatter([0], [0], s=dot_size, color=plotmath.COLORS.get("blue"), alpha=1)
            return

        x_positions = []
        y_positions = []

        # Pentagon vertices (pointing upward)
        angles = [np.pi / 2 + 2 * np.pi * i / 5 for i in range(5)]  # Start from top

        # Place center dot
        x_positions.append(0)
        y_positions.append(0)

        # Build pentagon layer by layer
        for layer in range(1, n):
            # For each layer, place dots along the pentagon edges
            layer_radius = layer * spacing

            # Calculate dots per edge for this layer
            dots_per_edge = layer

            for edge in range(5):
                # Start and end points of this edge
                start_angle = angles[edge]
                end_angle = angles[(edge + 1) % 5]

                start_x = layer_radius * np.cos(start_angle)
                start_y = layer_radius * np.sin(start_angle)
                end_x = layer_radius * np.cos(end_angle)
                end_y = layer_radius * np.sin(end_angle)

                # Place dots along this edge (excluding the end point to avoid duplicates)
                for i in range(dots_per_edge):
                    t = i / dots_per_edge
                    x = start_x + t * (end_x - start_x)
                    y = start_y + t * (end_y - start_y)
                    x_positions.append(x)
                    y_positions.append(y)

        # Plot all dots at once
        color = plotmath.COLORS.get("blue")
        ax.scatter(x_positions, y_positions, s=dot_size, color=color, alpha=1)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 4  # show n = 1, 2, 3, 4 (values: 1, 5, 12, 22)
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(9, 3),  # ~3.5″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        draw_pentagonal_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        pentagonal_number = n * (3 * n - 1) // 2
        ax.text(
            x=0,
            y=-4 * spacing,
            s=f"Figur {n}",
            fontsize=20,
            ha="center",
            va="center",
            weight="bold",
        )

        # Set limits to accommodate the largest pattern
        limit = max_n * spacing + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)

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
