import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *triangular numbers* using dots arranged in triangular patterns.

    The *n*-th figure is a triangular arrangement of dots with *n* rows.
    The number of dots is the **quadratic** polynomial

        T(n) = n(n+1)/2,

    yielding the sequence 1, 3, 6, 10, 15, … (OEIS A000217).
    """

    dot_size = 100  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw triangular pattern of dots ──────────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_triangular_dots(ax, spacing: float, n: int) -> None:
        """Plot dots arranged in a triangular pattern with n rows."""
        x_positions = []
        y_positions = []

        for row in range(n):
            # Number of dots in this row (row 0 has 1 dot, row 1 has 2 dots, etc.)
            dots_in_row = row + 1

            # Center the row horizontally
            row_width = (dots_in_row - 1) * spacing
            x_start = -row_width / 2

            # Position from top to bottom
            y = (
                (n - 1 - row) * spacing * 0.866
            )  # 0.866 ≈ sin(60°) for equilateral triangle spacing

            for col in range(dots_in_row):
                x = x_start + col * spacing
                x_positions.append(x)
                y_positions.append(y)

        # Plot all dots at once
        color = plotmath.COLORS.get("red")
        ax.scatter(x_positions, y_positions, s=dot_size, color=color, alpha=1)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 3  # show n = 1, 2, 3, 4
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(8, 3),  # ~3″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        draw_triangular_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        # ax.text(
        #     x=0,
        #     y=-(max_n + 1) * spacing,
        #     s=f"Figur {n}",
        #     fontsize=20,
        #     ha="center",
        #     va="center",
        #     weight="bold",
        # )

        # Add formula (commented out for cleaner look)
        triangular_number = n * (n + 1) // 2
        ax.text(
            x=0,
            y=-(max_n + 0.5) * spacing,
            s=f"$T_{n} = {triangular_number}$",
            fontsize=16,
            ha="center",
            va="center",
            style="italic",
        )

        # Set limits to accommodate the largest triangle
        limit = (max_n + 0.5) * spacing
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
