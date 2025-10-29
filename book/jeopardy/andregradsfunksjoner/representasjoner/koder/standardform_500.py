import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x + 1) ** 2) + 4

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
        fontsize=20,
        figsize=None,
    )

    ax.plot(0, 3, "ko", ms=8)
    ax.plot(-3, 0, "ko", ms=8)
    ax.plot(1, 0, "ko", ms=8)
    ax.text(
        x=0,
        y=3,
        s="$(0, 3)$",
        fontsize=20,
        va="bottom",
        ha="left",
    )

    ax.text(
        x=-3,
        y=0,
        s="$(-3, 0)$",
        fontsize=20,
        va="bottom",
        ha="right",
    )
    ax.text(
        x=1,
        y=0,
        s="$(1, 0)$",
        fontsize=20,
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
