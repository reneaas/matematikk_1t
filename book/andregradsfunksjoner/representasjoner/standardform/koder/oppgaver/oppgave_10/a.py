import plotmath


def main(dirname, save):
    #
    # Define functions
    a = -1 / 2
    b = 2
    c = 1

    def f(x):
        return a * x**2 + b * x + c

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-3,
        xmax=7,
        ymin=-6,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x0 = -b / (2 * a)
    ekstremalpunkt = (x0, f(x0))

    ax.plot(*ekstremalpunkt, "ko", markersize=10, alpha=0.7)
    ax.text(
        ekstremalpunkt[0],
        ekstremalpunkt[1] + 0.3,
        f"$({ekstremalpunkt[0]:.0f}, {ekstremalpunkt[1]:.0f})$",
        fontsize=18,
        va="bottom",
        ha="center",
    )

    ax.plot(0, c, "ko", markersize=10, alpha=0.7)
    ax.text(
        0 - 0.2,
        c,
        f"$({0}, {c})$",
        fontsize=18,
        va="center",
        ha="right",
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
