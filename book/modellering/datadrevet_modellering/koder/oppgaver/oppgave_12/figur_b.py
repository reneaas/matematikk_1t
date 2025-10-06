import plotmath


def main(dirname, save):
    #
    # Define functions
    import numpy as np

    def O(r):
        return (np.pi * r**3 + 900) / r

    # List of functions and their labels.
    functions = [O]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=0,
        xmax=22,
        ymin=0,
        ymax=5000,
        ticks=True,
        xstep=2,
        ystep=1000,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=(0.00001, 40),
        fontsize=20,
        figsize=None,
        xlabel=r"$r$ / $\mathrm{cm}$",
        # ylabel=r"$O(r)$ / $\mathrm{cm}^2$",
    )

    ax.set_ylabel(
        r"$O(r)$ / $\mathrm{cm}^2$",
        fontsize=16,
        # loc="top",
        rotation="horizontal",
        horizontalalignment="left",
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
