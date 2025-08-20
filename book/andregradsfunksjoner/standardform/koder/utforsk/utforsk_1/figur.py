import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -2 * (x - 2) * (x + 3)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-7,
        xmax=7,
        ymin=-6,
        ymax=13,
        ticks=True,
        xstep=1,
        ystep=2,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    punkt1 = (2, 0)
    punkt2 = (-3, 0)
    punkt3 = (0, 12)

    ax.plot(*punkt1, "ko", markersize=10, alpha=0.7)
    ax.plot(*punkt2, "ko", markersize=10, alpha=0.7)
    ax.plot(*punkt3, "ko", markersize=10, alpha=0.7)

    ax.text(
        x=punkt1[0] + 0.2,
        y=punkt1[1],
        s=f"$({punkt1[0]}, {punkt1[1]})$",
        fontsize=18,
        horizontalalignment="left",
        verticalalignment="bottom",
    )

    ax.text(
        x=punkt2[0] - 0.2,
        y=punkt2[1],
        s=f"$({punkt2[0]}, {punkt2[1]})$",
        fontsize=18,
        horizontalalignment="right",
        verticalalignment="bottom",
    )

    ax.text(
        x=punkt3[0] + 0.2,
        y=punkt3[1],
        s=f"$({punkt3[0]}, {punkt3[1]})$",
        fontsize=18,
        horizontalalignment="left",
        verticalalignment="center",
    )

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
