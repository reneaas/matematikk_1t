import plotmath


def main(dirname, save):
    #
    # Define functions
    def h(x):
        return x**2 - 6 * x + 9

    # List of functions and their labels.
    functions = [h]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-3,
        xmax=8,
        ymin=-3,
        ymax=12,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    ax.plot(1, 4, "ko", markersize=10, alpha=0.7)
    ax.text(
        1 + 0.2,
        4,
        f"$({1}, {4})$",
        fontsize=18,
        va="bottom",
        ha="left",
    )

    ax.plot(5, 4, "ko", markersize=10, alpha=0.7)
    ax.text(
        5 + 0.2,
        4,
        f"$({5}, {4})$",
        fontsize=18,
        va="top",
        ha="left",
    )

    ax.plot(0, 9, "ko", markersize=10, alpha=0.7)
    ax.text(
        0 + 0.2,
        9,
        f"$({0}, {9})$",
        fontsize=18,
        va="bottom",
        ha="left",
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
