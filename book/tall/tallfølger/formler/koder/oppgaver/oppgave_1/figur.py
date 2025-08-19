import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *odd numbers* using dots arranged in two columns, mirrored across x-axis.

    The *n*-th figure shows the n-th odd number (2n-1) as dots in two columns
    with their mirror image below. The number of dots is the **linear** polynomial

        p(n) = 2n - 1,

    yielding the sequence 1, 3, 5, 7, 9, … (OEIS A005408).
    """

    dot_size = 250  # size of each dot

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw symmetric pattern of dots ───────────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_odd_number_dots(ax, spacing: float, n: int) -> None:
        """Plot dots in two columns for the n-th odd number, mirrored across x-axis."""
        # Calculate the n-th odd number
        odd_number = 2 * n - 1

        x_positions = []
        y_positions = []

        # For odd numbers, arrange in two columns with one dot left over
        pairs = (odd_number - 1) // 2  # number of pairs

        # Place pairs of dots in two columns (original pattern)
        for i in range(pairs):
            # Left column
            x_positions.append(-spacing / 2)
            y_positions.append(i * spacing)
            # Right column
            x_positions.append(spacing / 2)
            y_positions.append(i * spacing)

        # Place the extra odd dot (can be in the middle or at the top)
        if odd_number % 2 == 1:  # Always true for odd numbers, but just to be clear
            x_positions.append(0)  # Center the odd dot
            y_positions.append(pairs * spacing)  # Place it at the top

        # Create mirror image across x-axis
        x_positions_mirror = x_positions.copy()
        y_positions_mirror = [-y for y in y_positions]

        # Combine original and mirror
        x_positions.extend(x_positions_mirror)
        y_positions.extend(y_positions_mirror)

        # Center the entire pattern vertically
        if pairs > 0:
            y_center = (pairs * spacing) / 2
            y_positions = [y - y_center for y in y_positions]

        # Plot all dots at once
        color = plotmath.COLORS.get("blue")
        ax.scatter(x_positions, y_positions, s=dot_size, color=color, alpha=1)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 4  # show n = 1, 2, 3, 4, 5 (odd numbers: 1, 3, 5, 7, 9)
    fig, axs = plt.subplots(
        1,
        max_n - 1,
        figsize=(12, 4),  # ~2.8″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    spacing = 1  # distance between dots

    for i, n in enumerate(range(2, max_n + 1)):
        draw_odd_number_dots(axs[i], spacing=spacing, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")

        # Add figure label
        odd_number = 2 * n - 1
        ax.text(
            x=0,
            y=-5.5 * spacing,
            s=f"Figur {n - 1}",
            fontsize=30,
            ha="center",
            va="center",
            weight="bold",
        )

        # Set limits to accommodate the largest pattern
        limit = 1.5 * max_n * spacing
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, 0.5 * limit)

    # ──────────────────────────────────────────────────────────────────
    # Output ───────────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    plt.tight_layout()
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
