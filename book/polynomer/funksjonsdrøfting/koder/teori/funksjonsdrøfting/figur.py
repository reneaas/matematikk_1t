import plotmath


def main(dirname, save):
    #
    # Define functions

    def f(x):
        return -((x + 1) ** 2) * (x - 2) ** 3 + 3

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=3,
        ymin=-6,
        ymax=15,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    import sympy

    f_expr = "-((x + 1) ** 2) * (x - 2) ** 3 + 3"
    f_expr = sympy.sympify(f_expr)

    x_extremalpunkter = sympy.solve(f_expr.diff())
    x_extremalpunkter = [float(x) for x in x_extremalpunkter]

    y_extremalpunkter = [f(x) for x in x_extremalpunkter]
    point_names = ["a", "b", "c"]

    for i, (x, y) in enumerate(zip(x_extremalpunkter, y_extremalpunkter)):
        ax.plot(x, y, "ko", markersize=8)

        # name = point_names[i]
        # ax.text(
        #     x + 0.1,
        #     y + 0.5,
        #     f"$({name}, f({name}))$",
        #     fontsize=16,
        #     color="black",
        # )

    ax.text(
        x=x_extremalpunkter[0] - 0.5,
        y=y_extremalpunkter[0] - 1.5,
        s="Bunnpunkt",
        fontsize=16,
        color="black",
    )

    ax.text(
        x=x_extremalpunkter[1],
        y=y_extremalpunkter[1] + 1,
        s="Toppunkt",
        fontsize=16,
        color="black",
    )

    ax.text(
        x=x_extremalpunkter[2],
        y=y_extremalpunkter[2] + 1,
        s="Terassepunkt",
        fontsize=16,
        color="black",
        ha="center",
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
