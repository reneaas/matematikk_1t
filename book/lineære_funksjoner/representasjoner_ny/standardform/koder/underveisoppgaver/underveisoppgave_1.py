import plotmath


def main(dirname, save):

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=0.8,
        domain=False,
    )

    A = (1, 2)
    B = (-2, 3)
    C = (3, -1)
    D = (-5, -3)
    E = (4, 4)
    F = (2, -4)

    punkter = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}

    for punktnavn in punkter:
        x, y = punkter.get(punktnavn)
        ax.plot(x, y, "ko", markersize=8, alpha=0.7)

        ax.text(
            s=f"${punktnavn}$",
            x=x + 0.2,
            y=y - 0.2,
            fontsize=16,
            ha="left",
            va="bottom",
        )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
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
