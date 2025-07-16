import plotmath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


def main(dirname, save):
    #
    # Define function
    def f(x):
        return (x + 1) ** 2 - 3

    # choose point where we illustrate derivative
    x0 = 1.0

    # initial static plot of f(x)
    fig, ax = plotmath.plot(
        functions=[f],
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    # prepare sequence of h-values → 0
    hs = np.linspace(2.0, 0.01, 50)

    # placeholder artists for secant (red) and tangent (blue dashed)
    (secant_line,) = ax.plot([], [], color="red", lw=2, label="secant")
    (tangent_line,) = ax.plot([], [], color="blue", lw=2, ls="--", label="tangent")
    ax.legend(loc="upper left")

    def update(i):
        h = hs[i]
        # secant through (x0-h, f) and (x0+h, f)
        xs = np.array([x0 - h, x0 + h])
        ys = f(xs)
        secant_line.set_data(xs, ys)

        # tangent at x0: slope m = f'(x0) = 2(x0+1)
        m = 2 * (x0 + 1)
        x_vals = np.linspace(x0 - 2, x0 + 2, 100)
        y_vals = f(x0) + m * (x_vals - x0)
        tangent_line.set_data(x_vals, y_vals)

        return secant_line, tangent_line

    anim = FuncAnimation(
        fig, update, frames=len(hs), interval=200, blit=True, repeat=False
    )

    if save:
        gif_path = f"{dirname}/momentan_vekstfart.gif"
        writer = PillowWriter(fps=10)
        anim.save(gif_path, writer=writer, savefig_kwargs={"transparent": True})
        print(f"Saved animation → {gif_path}")
    else:
        plt.show()


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
