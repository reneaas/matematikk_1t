import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *rectangular numbers* n(n+1) using colored rectangles.

    The *n*-th figure shows an n×(n+1) rectangle with the lower diagonal in red
    and the upper diagonal in blue. This demonstrates that rectangular numbers
    are twice the triangular numbers. The number of dots is the **quadratic** polynomial

        p(n) = n(n + 1),

    yielding the sequence 2, 6, 12, 20, 30, … (OEIS A002378).
    """

    dot_size = 100  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw rectangular pattern with colored diagonals ───────────
    # ──────────────────────────────────────────────────────────────────
    def draw_rectangular_dots(ax, spacing: float, n: int) -> None:
        """Plot dots in an n×(n+1) rectangle with colored diagonals."""
        # Calculate n(n+1)
        total_dots = n * (n + 1)

        x_positions_red = []
        y_positions_red = []
        x_positions_blue = []
        y_positions_blue = []

        # Create n×(n+1) rectangle
        # We'll make it n rows and (n+1) columns
        for row in range(n):
            for col in range(n + 1):
                x = col * spacing
                y = row * spacing

                # Determine color based on diagonal
                # Lower triangle (including diagonal): red
                # Upper triangle: blue
                if col <= row:
                    x_positions_red.append(x)
                    y_positions_red.append(y)
                else:
                    x_positions_blue.append(x)
                    y_positions_blue.append(y)

        # Center the entire pattern
        x_center = n * spacing / 2
        y_center = (n - 1) * spacing / 2

        x_positions_red = [x - x_center for x in x_positions_red]
        y_positions_red = [y - y_center for y in y_positions_red]
        x_positions_blue = [x - x_center for x in x_positions_blue]
        y_positions_blue = [y - y_center for y in y_positions_blue]

        # Plot red dots (lower triangle)
        if x_positions_red:
            color_red = plotmath.COLORS.get("red")
            ax.scatter(
                x_positions_red, y_positions_red, s=dot_size, color=color_red, alpha=1
            )

        # Plot blue dots (upper triangle)
        if x_positions_blue:
            color_blue = plotmath.COLORS.get("blue")
            ax.scatter(
                x_positions_blue,
                y_positions_blue,
                s=dot_size,
                color=color_blue,
                alpha=1,
            )

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 4  # show n = 1, 2, 3, 4 (values: 2, 6, 12, 20)
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(8, 2),  # ~4″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        draw_rectangular_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        value = n * (n + 1)
        triangular = n * (n + 1) // 2
        ax.text(
            x=0,
            y=-3 * spacing,
            s=f"Figur {n}",
            fontsize=20,
            ha="center",
            va="center",
            weight="bold",
        )

        # Add the formula value
        # ax.text(
        #     x=0,
        #     y=-3.8 * spacing,
        #     s=f"{n}×{n+1} = {value} prikker",
        #     fontsize=16,
        #     ha="center",
        #     va="center",
        #     style="italic",
        # )

        # Add triangular number connection
        # ax.text(
        #     x=0,
        #     y=-4.6 * spacing,
        #     s=f"2 × T_{n} = 2 × {triangular} = {value}",
        #     fontsize=14,
        #     ha="center",
        #     va="center",
        #     color="gray",
        # )

        # Set limits to accommodate the largest pattern
        limit = (max_n + 1) * spacing / 2 + 0.5
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
