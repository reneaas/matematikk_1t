import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 1 / x

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-0.5,
        xmax=4,
        ymin=-1,
        ymax=3,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        lw=2.5,
        domain=(0, 15),
    )

    k = 1.5
    A = (0, 0)
    B = (k, 0)
    C = (k, f(k))
    D = (0, f(k))

    plotmath.plot_polygon(
        A,
        B,
        C,
        D,
        alpha=0.2,
        color=plotmath.COLORS.get("blue"),
        show_vertices=True,
    )

    ax.text(
        x=k,
        y=0 - 0.1,
        s="$(k, 0)$",
        fontsize=20,
        ha="center",
        va="top",
    )

    ax.text(
        x=k,
        y=f(k) + 0.1,
        s="$(k, f(k))$",
        fontsize=20,
        ha="left",
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
