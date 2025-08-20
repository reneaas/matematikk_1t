import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise the sequence *4n + 2* using dots arranged in a specific pattern.

    The *n*-th figure shows the value 4n + 2 as dots arranged in groups.
    The number of dots is the **linear** polynomial

        p(n) = 4n + 2,

    yielding the sequence 6, 10, 14, 18, 22, …
    """

    dot_size = 100  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw 4n + 2 pattern ──────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_4n_plus_2_dots(ax, spacing: float, n: int) -> None:
        """Plot dots in a pattern showing 4n + 2."""
        # Calculate 4n + 2
        total_dots = 4 * n + 2

        x_positions = []
        y_positions = []

        # Pattern: arrange as 4 columns with n dots each, plus 2 extra dots
        # Place the 4n dots in 4 columns
        for col in range(4):
            for row in range(n):
                x = (col - 1.5) * spacing  # Center the 4 columns around x=0
                y = row * spacing
                x_positions.append(x)
                y_positions.append(y)

        # Place the 2 extra dots - one above each of the middle columns
        x_positions.append(-0.5 * spacing)  # Above column 1 (left-middle)
        y_positions.append(n * spacing)

        x_positions.append(0.5 * spacing)  # Above column 2 (right-middle)
        y_positions.append(n * spacing)

        # Center the entire pattern vertically
        if n > 0:
            y_center = (n * spacing) / 2
            y_positions = [y - y_center for y in y_positions]

        # Plot all dots at once
        color = plotmath.COLORS.get("purple")
        ax.scatter(x_positions, y_positions, s=dot_size, color=color, alpha=1)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 4  # show n = 1, 2, 3, 4 (values: 6, 10, 14, 18)
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(14, 4),  # ~3.5″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        draw_4n_plus_2_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        value = 4 * n + 2
        ax.text(
            x=0,
            y=-3 * spacing,
            s=f"Figur {n}",
            fontsize=24,
            ha="center",
            va="center",
            weight="bold",
        )

        # Set limits to accommodate the largest pattern
        limit = 3 * spacing
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
