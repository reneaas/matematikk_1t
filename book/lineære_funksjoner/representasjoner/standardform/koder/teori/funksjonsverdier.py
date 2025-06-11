import plotmath
import matplotlib.pyplot as plt


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
        xmin=-2,
        xmax=4,
        ymin=-2,
        ymax=8,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        domain=False,
    )

    x0 = 3
    y0 = f(x0)

    ax.plot(x0, y0, "ko", markersize=8, alpha=0.7)
    ax.hlines(y0, 0, x0, color="blue", linestyle="--", lw=1.5)
    ax.vlines(x0, 0, y0, color="blue", linestyle="--", lw=1.5)

    ax.text(
        x=x0 + 0.2,
        y=y0 - 0.2,
        s=f"$({x0}, f({x0}))$",
        fontsize=20,
        color="red",
    )

    plt.tick_params(axis="both", which="major", labelsize=20)

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
