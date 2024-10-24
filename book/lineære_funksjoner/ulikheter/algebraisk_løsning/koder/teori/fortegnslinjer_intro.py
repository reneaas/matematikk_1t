import signchart


def main(dirname, save):

    f = "x - 2"

    signchart.make_sign_chart(
        f=f,
        fn_name="f(x)",
        include_factors=False,
        small_figsize=True,
    )

    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        signchart.savefig(dirname=dirname, fname=fname)

    else:
        signchart.show()


# NOTE: Ikke endre på noe under denne linjen
if __name__ == "__main__":

    import sys
    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    dirname = current_dir.replace("koder", "figurer")
    main(dirname=dirname, save=True)
