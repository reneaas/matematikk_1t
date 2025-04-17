import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 2 * x - 1

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=6,
        ymin=-2,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        lw=2.5,
        alpha=0.8,
        domain=False,
    )

    x1 = 1
    y1 = f(x1)
    ax.plot(x1, y1, color="black", alpha=0.7, marker="o")

    ax.text(x1, y1 + 0.1, r"$(x_1, y_1)$", fontsize=16, ha="right", va="bottom")
    x2 = 3
    y2 = f(x2)
    ax.plot(x2, y2, color="black", alpha=0.7, marker="o")
    ax.text(x2, y2 + 0.1, r"$(x, y)$", fontsize=16, ha="right", va="bottom")

    ax.plot([x1, x2], [y1, y1], linestyle="--", color="blue", alpha=0.8)
    ax.plot([x2, x2], [y1, y2], linestyle="--", color="blue", alpha=0.8)

    ax.text(
        (x1 + x2) / 2,
        y1 - 0.3,
        r"$x - x_1$",
        fontsize=16,
        ha="center",
        va="center",
    )
    ax.text(
        x2 + 0.3,
        (y1 + y2) / 2,
        r"$y - y_1$",
        fontsize=16,
        ha="left",
        va="center",
    )

    ax.set_xticks(
        [x1, x2],
        [r"$x_1$", r"$x$"],
        fontsize=16,
    )

    ax.set_yticks(
        [y1, y2],
        [r"$y_1$", r"$y$"],
        fontsize=16,
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
