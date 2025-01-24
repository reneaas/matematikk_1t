import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):

    # List of functions and their labels.
    functions = []

    plt.figure()

    theta = np.linspace(0, 2 * np.pi, 1024)
    y1 = 4
    a = 2
    b = 1
    x = a * np.cos(theta)
    y = b * np.sin(theta) + y1

    plt.plot(x, y, color="teal", lw=2)

    y2 = -4
    y = b * np.sin(theta) + y2

    plt.plot(x, y, color="teal", lw=2)

    plt.plot([a, a], [y1, y2], color="teal", lw=2)
    plt.plot([-a, -a], [y1, y2], color="teal", lw=2)

    plt.plot([0, a], [y1, y1], color="black", lw=1.5)

    plt.text(
        x=a / 2,
        y=y1,
        s="$r$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    plt.text(
        x=a + 0.2,
        y=0.5 * (y1 + y2),
        s="$h$",
        fontsize=20,
        ha="left",
        va="center",
    )
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.tight_layout()
    plt.axis("off")

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
