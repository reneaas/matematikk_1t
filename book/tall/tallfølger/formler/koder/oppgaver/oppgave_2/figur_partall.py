import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *even numbers* using dots arranged in two equal columns.

    The *n*-th figure shows the n-th even number (2n) as dots in two columns
    with equal numbers in each column. The number of dots is the **linear** polynomial

        p(n) = 2n,

    yielding the sequence 2, 4, 6, 8, 10, … (OEIS A005843).
    """

    dot_size = 100  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw even number pattern ─────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_even_number_dots(ax, spacing: float, n: int) -> None:
        """Plot dots in two equal columns for the n-th even number."""
        # Calculate the n-th even number
        even_number = 2 * n

        x_positions = []
        y_positions = []

        # For even numbers, arrange in two equal columns
        dots_per_column = even_number // 2

        # Place dots in left column
        for i in range(dots_per_column):
            x_positions.append(-spacing / 2)
            y_positions.append(i * spacing)

        # Place dots in right column
        for i in range(dots_per_column):
            x_positions.append(spacing / 2)
            y_positions.append(i * spacing)

        # Center the entire pattern vertically
        if dots_per_column > 0:
            y_center = (dots_per_column - 1) * spacing / 2
            y_positions = [y - y_center for y in y_positions]

        # Plot all dots at once
        color = plotmath.COLORS.get("red")
        ax.scatter(x_positions, y_positions, s=dot_size, color=color, alpha=1)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 4  # show n = 1, 2, 3, 4 (even numbers: 2, 4, 6, 8)
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(12, 4),  # ~3″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(1, max_n + 1)):
        draw_even_number_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        even_number = 2 * n
        ax.text(
            x=0,
            y=-3 * spacing,
            s=f"Figur {n}",
            fontsize=20,
            ha="center",
            va="center",
            weight="bold",
        )

        # Add the even number value
        ax.text(
            x=0,
            y=-3.8 * spacing,
            s=f"{even_number} prikker",
            fontsize=16,
            ha="center",
            va="center",
            style="italic",
        )

        # Set limits to accommodate the largest pattern
        limit = 2 * spacing
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit * 2, limit * 2)

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
