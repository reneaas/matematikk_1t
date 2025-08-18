def main(dirname, save):
    import plotmath
    import numpy as np
    import matplotlib.pyplot as plt

    def circle(x0, y0, r):
        theta = np.linspace(0, 2 * np.pi, 1024)
        x = r * np.cos(theta) + x0
        y = r * np.sin(theta) + y0
        return x, y

    fig, ax = plt.subplots()

    # plot roof

    ax.hlines(y=0, xmin=-1, xmax=1, color="gray", lw=2.5)
    høyde = 1
    x, y = circle(0, høyde, r=0.1)

    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)
    ax.fill(x, y, color=plotmath.COLORS.get("blue"), alpha=0.2)

    ax.vlines(x=0, ymin=0, ymax=høyde, color="gray", lw=1.5, ls="--")

    plt.quiver(
        0.2,
        høyde + 0.1,
        0,
        -0.4,
        color="black",
        scale=1,
        scale_units="xy",
        angles="xy",
        width=0.01,
    )

    x, y = circle(0, 0.1, r=0.1)

    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5, ls="--", alpha=0.6)
    ax.fill(x, y, color=plotmath.COLORS.get("blue"), alpha=0.2)

    ax.text(
        x=-0.6,
        y=høyde,
        s="Kule",
        fontsize=20,
    )

    ax.text(
        x=-0.8,
        y=0.05,
        s="Bakken",
        fontsize=20,
    )

    plt.xlim(-2, 2)

    plt.axis("equal")
    plt.axis("off")

    fig.set_size_inches(4, 2)

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
