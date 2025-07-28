import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *square numbers* using dots arranged in square patterns.

    The *n*-th figure is a square arrangement of dots with side length *n*.
    The number of dots is the **quadratic** polynomial

        p(n) = n²,

    yielding the sequence 1, 4, 9, 16, 25, … (OEIS A000290).
    """

    dot_size = 100  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw square pattern of dots ──────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_square_dots(ax, spacing: float, n: int) -> None:
        """Plot n×n dots arranged in a square pattern."""
        # Calculate positions for centering the square
        offset = -(n - 1) * spacing / 2

        x_positions = []
        y_positions = []

        for i in range(n):
            for j in range(n):
                x = offset + i * spacing
                y = offset + j * spacing
                x_positions.append(x)
                y_positions.append(y)

        # Plot all dots at once
        color = plotmath.COLORS.get("blue")
        ax.scatter(x_positions, y_positions, s=dot_size, color=color, alpha=1)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 3  # show n = 1, 2, 3, 4
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(10, 3),  # ~2.5″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        draw_square_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label and dot count
        ax.text(
            x=0,
            y=-(max_n + 1) * spacing,
            s=f"Figur {n}",
            fontsize=20,
            ha="center",
            va="center",
            weight="bold",
        )

        # ax.text(
        #     x=0,
        #     y=-(max_n + 1.8) * spacing,
        #     s=f"$S_{n}$",
        #     fontsize=16,
        #     ha="center",
        #     va="center",
        #     style="italic",
        # )

        # Set limits to accommodate the largest square
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
