import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import plotmath
import pathlib

# Enable LaTeX rendering
mpl.rcParams["text.usetex"] = True
mpl.rcParams["font.size"] = 18


def prime_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            if i == n:
                return [n]
            return [i] + prime_factors(n // i)


def get_tree_depth(node):
    if not node[1]:
        return 1
    return 1 + max(get_tree_depth(child) for child in node[1])


def plot_tree(
    node, x=0, y=0, ax=None, level=0, max_depth=3, branch_length=2, angle_deg=60
):
    angle_rad = np.radians(angle_deg)
    dx = branch_length * np.sin(angle_rad)
    dy = -branch_length * np.cos(angle_rad)

    if ax is None:
        fig, ax = plt.subplots()
        ax.axis("off")
        ax.set_aspect("equal")

    value, children = node
    ax.text(
        x,
        y,
        f"${value}$",
        ha="center",
        va="center",
        bbox=dict(
            boxstyle="circle,pad=0.3",
            facecolor="#e0f7fa",
            edgecolor=plotmath.COLORS.get("blue"),
            linewidth=1.5,
        ),
    )

    if children:
        offsets = [-dx, dx]
        for child, offset_x in zip(children, offsets):
            child_x = x + offset_x
            child_y = y + dy
            ax.plot([x, child_x], [y, child_y], color="#455a64", linewidth=1.2)
            plot_tree(
                child,
                x=child_x,
                y=child_y,
                ax=ax,
                level=level + 1,
                max_depth=max_depth,
                branch_length=branch_length,
                angle_deg=angle_deg,
            )

    if ax is not None and level == 0:
        total_dx = dx * (2 ** (max_depth - 1))
        ax.set_xlim(-total_dx, total_dx)
        ax.set_ylim(dy * (max_depth + 0.5), 1)


def save_step_figure(node, step, dirname, max_depth):
    fig, ax = plt.subplots()
    plot_tree(node, ax=ax, max_depth=max_depth)
    fig.set_size_inches(4, 3)
    ax.axis("off")
    plt.tight_layout()
    filename = f"{dirname}/step_{step:02d}.svg"
    fig.savefig(filename, bbox_inches="tight")
    plt.close(fig)


def build_full_tree(n):
    """Simple helper to compute full tree for depth estimation"""
    factors = prime_factors(n)
    if len(factors) == 1:
        return [n, []]
    left = factors[0]
    right = n // left
    return [n, [build_full_tree(left), build_full_tree(right)]]


def build_tree_stepwise(n, dirname):
    step_counter = [0]
    max_depth = get_tree_depth(build_full_tree(n))

    def helper(node):
        value = node[0]
        factors = prime_factors(value)
        if len(factors) == 1:
            return

        left = factors[0]
        right = value // left
        node[1].append([left, []])
        node[1].append([right, []])

        save_step_figure(tree, step_counter[0], dirname, max_depth)
        step_counter[0] += 1

        helper(node[1][0])
        helper(node[1][1])

    tree = [n, []]
    save_step_figure(tree, step_counter[0], dirname, max_depth)  # Root-only
    step_counter[0] += 1
    helper(tree)
    return tree


def main(dirname, save):
    n = 60
    if save:
        tree = build_tree_stepwise(n, dirname)
    else:
        tree = build_tree_stepwise(n, dirname=None)  # Won’t save, just show

    if not save:
        depth = get_tree_depth(tree)
        plot_tree(tree, max_depth=depth, angle_deg=30)
        plt.tight_layout()
        plt.gcf().set_size_inches(4, 3)
        plotmath.show()


if __name__ == "__main__":
    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break
    dirname = "/".join(parts)

    main(dirname=dirname, save=True)
