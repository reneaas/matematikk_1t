import plotmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def main(dirname, save):
    a = 1  # small triangle side
    n_stories = 25  # number of layers
    h = a * np.sqrt(3) / 2

    # precompute rows...
    rows = []
    for j in range(1, n_stories + 1):
        row = []
        row_count = 2 * j - 1
        row_length = j * a
        x_offset = (n_stories * a - row_length) / 2
        y = (n_stories - j) * h
        for k in range(row_count):
            x = x_offset + k * (a / 2)
            if k % 2 == 0:
                tri = [(x, y), (x + a, y), (x + a / 2, y + h)]
            else:
                tri = [(x + a / 2, y), (x, y + h), (x + a, y + h)]
            row.append(tri)
        rows.append(row)

    # create figure with transparent background
    fig, ax = plt.subplots(figsize=(8, 8), facecolor="none")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.patch.set_alpha(0)

    def update(frame):
        ax.clear()
        ax.set_aspect("equal")
        ax.axis("off")
        ax.patch.set_alpha(0)
        for r in range(frame + 1):
            for tri in rows[r]:
                pts = tri + [tri[0]]
                ax.plot(*zip(*pts), color="black", lw=1)
        return (ax,)

    if save:
        update(n_stories - 1)
        plt.tight_layout()
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(dirname=dirname, fname=fname)
    else:
        anim = FuncAnimation(
            fig, update, frames=n_stories, interval=200, blit=True, repeat=False
        )
        gif_path = f"{dirname}/animasjon.gif"
        writer = PillowWriter(fps=10)
        # pass transparent and high dpi to save frames
        anim.save(
            gif_path,
            writer=writer,
            savefig_kwargs={"transparent": True, "facecolor": "none", "dpi": 200},
        )
        print(f"Saved animation → {gif_path}")
        plt.show()
