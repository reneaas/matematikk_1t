import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):

    def make_circle(radius):
        theta = np.linspace(0, 2 * np.pi, 1024)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    def make_n_gon(n, radius):
        theta = np.linspace(0, 2 * np.pi, n + 1)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    x, y = make_circle(radius=1)
    plt.plot(x, y, color="black", lw=1.5)

    x, y = make_n_gon(n=6, radius=2 / np.sqrt(3))
    plt.plot(x, y, color="teal", lw=2.5, alpha=0.8)

    l = 2 / np.sqrt(3)
    A = (0, 0)
    B = (l, 0)
    C = (l * np.cos(np.pi / 3), l * np.sin(np.pi / 3))

    plotmath.plot_polygon(
        A,
        B,
        C,
        ax=plt.gca(),
        color="teal",
        show_vertices=True,
    )

    # plt.plot([0, 1], [0, 0], "k-", lw=1.5)
    # plt.plot([0, np.cos(np.pi / 3)], [0, np.sin(np.pi / 3)], "k-", lw=1.5)

    def make_circle_arc(radius, start, stop, n=1024):
        theta = np.linspace(start, stop, n)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return x, y

    x, y = make_circle_arc(radius=0.2, start=0, stop=np.pi / 3)

    plt.plot(x, y, "k-", lw=1)

    plt.text(
        x=0.3 * np.cos(np.pi / 6),
        y=0.08,
        s=r"$u$",
        fontsize=16,
        ha="center",
        va="bottom",
    )

    plt.axis("off")
    plt.axis("equal")

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
