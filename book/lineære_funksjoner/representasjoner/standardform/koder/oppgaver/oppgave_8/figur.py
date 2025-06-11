import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        slope = -2
        intercept = 4
        return slope * x + intercept

    def g(x):
        slope = 1
        intercept = -5
        return slope * x + intercept

    # List of functions and their labels.
    functions = [f, g]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=7,
        ymin=-6,
        ymax=5,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    A = (2, 0)
    B = (5, 0)
    C = (3, -2)

    ax.plot(*A, "ko", markersize=8)
    ax.plot(*B, "ko", markersize=8)
    ax.plot(*C, "ko", markersize=8)

    ax.text(
        A[0] + 0.1,
        A[1] + 0.4,
        r"$(2, 0)$",
        fontsize=20,
        color="black",
    )

    ax.text(
        B[0] + 0.1,
        B[1] - 0.6,
        r"$(5, 0)$",
        fontsize=20,
        color="black",
    )

    ax.text(
        C[0] + 0.3,
        C[1] - 0.3,
        r"$(3,-2)$",
        fontsize=20,
        color="black",
    )

    A = (3, -2)
    B = (0, 4)
    C = (0, -5)

    plotmath.plot_polygon(
        A,
        B,
        C,
        ax=ax,
        alpha=0.8,
        color=plotmath.COLORS.get("skyblue"),
        edges=False,
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
