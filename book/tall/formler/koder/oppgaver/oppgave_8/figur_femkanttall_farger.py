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
        """Plot dots showing pentagonal numbers using L-shaped building blocks."""
        x_positions = []
        y_positions = []

        # Build the pattern using L-shaped units that share a corner
        # Each pentagonal number can be seen as adding L-shaped layers

        for layer in range(n):
            if layer == 0:
                # First dot at origin
                x_positions.append(0)
                y_positions.append(0)
            else:
                # Add L-shaped pattern extending from the shared corner
                # This creates the pattern where each "layer" adds specific dots

                # Horizontal arm of the L
                for i in range(layer + 1):
                    x = i * spacing
                    y = layer * spacing
                    if not (x == 0 and y == 0):  # Don't duplicate origin
                        x_positions.append(x)
                        y_positions.append(y)

                # Vertical arm of the L (excluding the corner which is already added)
                for j in range(layer):
                    x = layer * spacing
                    y = j * spacing
                    x_positions.append(x)
                    y_positions.append(y)

                # Add the characteristic "pentagon extension" dots
                # These create the pentagonal growth pattern
                if layer >= 2:
                    # Add extra dots that make it pentagonal rather than square
                    for i in range(layer - 1):
                        # Diagonal-ish extensions
                        x = (i + 1) * spacing
                        y = (layer + 1) * spacing
                        x_positions.append(x)
                        y_positions.append(y)

        # Center the pattern
        if x_positions:
            x_center = sum(x_positions) / len(x_positions)
            y_center = sum(y_positions) / len(y_positions)
            x_positions = [x - x_center for x in x_positions]
            y_positions = [y - y_center for y in y_positions]

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
    main(dirname=dirname, save=False)
