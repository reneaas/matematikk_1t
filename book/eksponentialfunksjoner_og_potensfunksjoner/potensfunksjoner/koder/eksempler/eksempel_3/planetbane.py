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

    x_sol, y_sol = circle(0, 0, 2)

    ax.plot(x_sol, y_sol, color="black", lw=1.5)
    plt.fill(x_sol, y_sol, color="orange", alpha=0.5)

    x_planet, y_planet = circle(
        x0=4 * np.cos(np.pi / 4), y0=4 * np.sin(np.pi / 4), r=0.5
    )
    ax.plot(x_planet, y_planet, color="teal", lw=1.5)
    plt.fill(x_planet, y_planet, color="teal", alpha=0.5)

    x_orbit, y_orbit = circle(x0=0, y0=0, r=4)
    ax.plot(x_orbit, y_orbit, color="black", lw=1, linestyle="--")

    plt.text(x=0, y=0, s="Sola", fontsize=16, ha="center", va="center")

    plt.quiver(
        4 * np.cos(np.pi / 4),
        4 * np.sin(np.pi / 4),
        -2 * np.sin(np.pi / 4),
        2 * np.cos(np.pi / 4),
        color="black",
        scale=1,
        scale_units="xy",
        angles="xy",
        width=0.005,
    )

    plt.text(
        x=5 * np.cos(np.pi / 4),
        y=4.2 * np.sin(np.pi / 4),
        s="Planet",
        fontsize=16,
    )

    plt.axis("equal")
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
