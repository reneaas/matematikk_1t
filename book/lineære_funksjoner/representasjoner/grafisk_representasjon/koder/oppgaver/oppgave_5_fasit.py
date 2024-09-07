def main(dirname, save=False):

    # Define functions
    def f(x):
        return -2 * x + 4

    def g(x):
        return -2 * x + 2

    def h(x):
        return -x + 2

    def r(x):
        return x + 2

    # List of functions and their labels.
    import numpy as np

    np.random.seed(1000)
    idx = np.random.permutation(4)
    functions = [f, g, h, r]
    functions = [functions[i] for i in idx]
    fn_labels = [r"$f$", r"$g$", r"$h$", r"$r$"]
    fn_labels = [fn_labels[i] for i in idx]

    # Create the math figure
    fig, ax = make_figure(
        functions=functions,
        fn_labels=fn_labels,  # Set `None` hvis du ikke vil ha labels.
        xmin=-3,
        xmax=4,
        ymin=-3,
        ymax=5,
        ticks=False,
    )

    # Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        savefig(dirname=dirname, fname=fname)  # Lagrer figuren i `dirname`-directory

    if not save:
        import matplotlib.pyplot as plt

        plt.show()


if __name__ == "__main__":

    import sys
    import os

    def find_repo_root(current_path):
        while current_path != os.path.dirname(
            current_path
        ):  # Stop when you reach the filesystem root
            if os.path.isdir(os.path.join(current_path, ".git")):
                return current_path
            current_path = os.path.dirname(current_path)
        raise FileNotFoundError("No .git directory found in any parent directories.")

    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Find the root of the GitHub repository (where .git is located)
    repo_root = find_repo_root(current_dir)

    # Add the GitHub repository root to sys.path
    sys.path.append(repo_root)

    # Now you can import modules from the GitHub repo root
    from python_templates.plot_utils import make_figure, savefig

    # Set `save=True` to save figure. `save=False` to display figure.
    dirname = "../../figurer/oppgaver/"
    main(dirname=dirname, save=True)
