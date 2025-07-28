import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *centred plus‑sign numbers* (thin crosses).

    The *n*-th figure is a symmetric “+” with arm‑length *n* and thickness 1.
    The number of unit squares is the **linear** polynomial

        p(n) = 4 n + 1,

    yielding the sequence 1, 5, 9, 13, 17, … (OEIS A001844).
    """

    alpha = 0.25  # square transparency

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw centred plus sign of radius n ───────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_plus(ax, s: float, n: int) -> None:
        """Plot a + shaped polyomino whose arms extend n squares from centre."""
        # Vertical arm (x ≈ 0)
        for k in range(-n, n + 1):
            x0 = -0.5 * s  # centre the 1‑wide arm on x = 0
            y0 = k * s - 0.5 * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha)

        # Horizontal arm (y ≈ 0)
        for k in range(-n, n + 1):
            if k == 0:
                continue  # centre already filled by vertical loop
            x0 = k * s - 0.5 * s
            y0 = -0.5 * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha)

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 3  # show n = 0 … 3
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(8, 3),  # ~2.7″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    s = 1  # unit‑square side length

    for i, n in enumerate(range(1, max_n + 1)):
        draw_plus(axs[i], s=s, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")
        ax.text(
            x=0,
            y=-(max_n + 2) * s,
            s=f"Figur {i + 1}",
            fontsize=22,
            ha="center",
            va="center",
        )
        limit = (max_n + 0.5) * s
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
