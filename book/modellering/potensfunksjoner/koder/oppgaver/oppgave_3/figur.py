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

    angle1 = 60
    angle1 = np.radians(angle1)

    length = np.linspace(0, 1)
    x = length * np.cos(angle1)
    y = -length * np.sin(angle1)

    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2)

    radius = 0.1

    l = length[-1] + radius
    x0 = l * np.cos(angle1)
    y0 = -l * np.sin(angle1)

    x, y = circle(x0, y0, radius)

    ax.plot(x, y, color=plotmath.COLORS.get("red"), lw=2.5)
    ax.fill(x, y, color=plotmath.COLORS.get("red"), alpha=0.5)
    # pendel1 = circle()

    # fig.set_size_inches(3, 2)

    angles = np.linspace(np.radians(120), np.radians(60), 1024)
    x = l * np.cos(angles)
    y = -l * np.sin(angles)

    ax.plot(x, y, color="gray", lw=1.5, ls="--")

    angle1 = 120
    angle1 = np.radians(angle1)

    length = np.linspace(0, 1)
    x = length * np.cos(angle1)
    y = -length * np.sin(angle1)

    ax.plot(x, y, color=plotmath.COLORS.get("blue"), lw=2, ls="--", alpha=0.6)

    radius = 0.1

    l = length[-1] + radius
    x0 = l * np.cos(angle1)
    y0 = -l * np.sin(angle1)

    x, y = circle(x0, y0, radius)

    ax.plot(x, y, color=plotmath.COLORS.get("red"), lw=2.5, ls="--", alpha=0.6)
    ax.fill(x, y, color=plotmath.COLORS.get("red"), alpha=0.2)

    plt.xlim(-2, 2)

    plt.axis("equal")
    plt.axis("off")

    ax.text(
        x=0.5,
        y=-0.5,
        s="Pendel",
        fontsize=20,
    )

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
