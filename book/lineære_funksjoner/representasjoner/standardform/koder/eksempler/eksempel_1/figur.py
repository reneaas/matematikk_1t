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
        xmin=-3,
        xmax=6,
        ymin=-6,
        ymax=8,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
    )

    x0 = 2
    y0 = f(x0)

    ax.hlines(y=y0, xmin=0, xmax=x0, color=plotmath.COLORS.get("red"), lw=2.5, ls="--")
    ax.vlines(x=x0, ymin=0, ymax=y0, color=plotmath.COLORS.get("red"), lw=2.5, ls="--")

    ax.plot(x0, y0, "ko", markersize=10, alpha=0.8)
    # ax.text(
    #     x=x0 + 0.2,
    #     y=y0,
    #     s=f"$({x0}, f({x0})) = ({x0}, {y0})$",
    #     fontsize=20,
    #     ha="left",
    #     va="top",
    # )

    plt.annotate(
        text=f"$\\left({x0}, f({x0})\\right)$",
        xy=(x0, f(x0)),
        xytext=(3, 2),
        fontsize=20,
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color="black",
            alpha=0.7,
            connectionstyle="arc3,rad=+0.3",
        ),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black", lw=1.5),
        horizontalalignment="left",
        verticalalignment="center",
    )

    fontsize = 20
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(fontsize)  # Set to desired font size

    ax.yaxis.label.set_size(fontsize)  # Set y-axis label font size
    ax.xaxis.label.set_size(fontsize)  # Set x-axis label font size

    ax.legend(fontsize=fontsize)

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
