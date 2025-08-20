import plotmath


def main(dirname, save):
    #
    # Define functions
    a = 2
    x0 = 1
    y0 = -4

    def f(x):
        return a * (x - x0) ** 2 + y0

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-3,
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
    )

    ax.plot(0, f(0), "ko", markersize=10, alpha=0.7)
    ax.plot(x0, y0, "ko", markersize=10, alpha=0.7)
    ax.vlines(x=x0, ymin=-10, ymax=10, color=plotmath.COLORS.get("red"), lw=2, ls="--")

    ax.text(
        0 - 0.2,
        f(0),
        f"$({0}, {f(0)})$",
        fontsize=18,
        va="top",
        ha="right",
    )

    ax.text(
        x0 + 0.2,
        y0,
        f"$({x0}, {y0})$",
        fontsize=18,
        va="top",
        ha="left",
    )

    ax.text(
        x=x0 + 0.2,
        y=4,
        s=f"$x = {x0}$",
        fontsize=18,
        va="center",
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
