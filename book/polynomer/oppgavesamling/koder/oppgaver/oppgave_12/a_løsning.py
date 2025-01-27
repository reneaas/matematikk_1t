import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -((x - 3) ** 2) + 4

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=["$f$"],
        xmin=-2,
        xmax=6,
        ymin=-2,
        ymax=6,
        ticks=False,
    )

    ax.plot(3, f(3), "ko", markersize=8, alpha=0.7)
    dy = dx = 0.2
    ax.text(
        x=3,
        y=f(3) + dy,
        s="$(3, f(3))$",
        fontsize=16,
        ha="center",
        va="bottom",
    )

    ax.plot(5, 0, "ko", markersize=8, alpha=0.7)
    dx = dy = 0.1
    ax.text(
        x=5 + dx,
        y=0 + dy,
        s="$(5, 0)$",
        fontsize=16,
        ha="left",
        va="bottom",
    )

    ax.plot(1, 0, "ko", markersize=8, alpha=0.7)
    dx = dy = 0.1
    ax.text(
        x=1 - dx,
        y=0 + dy,
        s="$(1, 0)$",
        fontsize=16,
        ha="right",
        va="bottom",
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
