import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -(x**3) + 4 * x**2

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-1,
        xmax=5,
        ymin=-2,
        ymax=10,
        ticks=False,
        domain=[0, 4],
    )

    color = "teal"
    x0 = 1
    a = 0
    b = 4
    ax.plot([x0, b], [f(x0), 0], color="black", lw=1.5, alpha=0.7)
    ax.plot([b, x0], [0, 0], color="black", lw=1.5, alpha=0.7)
    ax.plot([x0, x0], [0, f(x0)], color="black", lw=1.5, alpha=0.7)

    A = [b, 0]
    B = [x0, f(x0)]
    C = [x0, 0]

    ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color=color, alpha=0.1)

    ax.plot(*A, "ko", markersize=8, alpha=0.7)
    ax.plot(*B, "ko", markersize=8, alpha=0.7)
    ax.plot(*C, "ko", markersize=8, alpha=0.7)

    dy = 0.2
    dx = 0.2

    ax.text(
        x=x0,
        y=f(x0) + dy,
        s="$(1, f(1))$",
        color="black",
        fontsize=16,
        ha="right",
        va="bottom",
    )

    ax.set_xticks([i for i in range(1, 5)])
    ax.tick_params(axis="x", labelsize=16)
    ax.grid(False)

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
