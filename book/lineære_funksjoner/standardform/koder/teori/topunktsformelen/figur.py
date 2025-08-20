import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * x + 1

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=4,
        ymin=-1,
        ymax=8,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        lw=2.5,
        domain=False,
    )

    x0 = 1
    y0 = f(x0)
    x1 = 3
    y1 = f(x1)

    dx = dy = 0.1
    ax.plot(
        x0,
        y0,
        "ko",
        markersize=10,
        alpha=0.8,
    )

    ax.text(
        x=x0 - dx,
        y=y0 + dy,
        s="$(x_1, y_1)$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    ax.plot(
        x1,
        y1,
        "ko",
        markersize=10,
        alpha=0.8,
    )

    ax.text(
        x=x1 - dx,
        y=y1 + dy,
        s="$(x_2, y_2)$",
        fontsize=20,
        ha="right",
        va="bottom",
    )

    ax.hlines(
        y=y0,
        xmin=x0,
        xmax=x1,
        color="blue",
        ls="--",
        lw=2,
        alpha=0.8,
    )

    ax.text(
        x=(x0 + x1) / 2,
        y=y0 - 0.7,
        s="$\\Delta x$",
        fontsize=20,
        ha="center",
        va="bottom",
    )

    ax.vlines(
        x=x1,
        ymin=y0,
        ymax=y1,
        color="blue",
        ls="--",
        lw=2,
        alpha=0.8,
    )

    ax.text(
        x=x1 + 0.2,
        y=(y0 + y1) / 2,
        s="$\\Delta y$",
        fontsize=20,
        ha="left",
        va="center",
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
