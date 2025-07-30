import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
import plotmath  # If you plan to extend with custom animation helpers
import pathlib
import shutil
import subprocess
import sys

# Optional: Point to your ImageMagick install
mpl.rcParams["animation.convert_path"] = (
    shutil.which("magick") or "/opt/homebrew/bin/magick"
)


def set_axes(ax, xlabel="$x$", ylabel="$y$", fontsize=20):
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.set_xlabel(xlabel, fontsize=fontsize, loc="right")
    ax.set_ylabel(ylabel, fontsize=fontsize, loc="top", rotation="horizontal")


def main(dirname: str, save: bool = True):
    fontsize = 20

    # Define grid of points
    x_min, x_max, y_min, y_max = 0, 3, 0, 2
    x_values = np.arange(x_min, x_max + 1)
    y_values = np.arange(y_min, y_max + 1)
    x_grid, y_grid = np.meshgrid(x_values, y_values)
    x_flat = x_grid.T.flatten()
    y_flat = y_grid.T.flatten()

    # Set up plot
    fig, ax = plt.subplots()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)

    # Draw math-style axes
    set_axes(ax, xlabel=r"$x$", ylabel=r"$y$", fontsize=fontsize)

    ax.set_xticks([i for i in range(-3, 4) if i != 0])
    ax.set_yticks([i for i in range(-3, 4) if i != 0])
    ax.tick_params(labelsize=fontsize)

    (point,) = ax.plot([], [], "ko", markersize=10)
    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    def init():
        point.set_data([], [])
        return (point,)

    def update(frame):
        x = x_flat[: frame + 1]
        y = y_flat[: frame + 1]
        point.set_data(x, y)

        for txt in ax.texts:
            txt.set_visible(False)

        bbox_props = dict(
            boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7
        )

        ax.text(
            x=0.5,
            y=-3.5,
            s=f"$(x, y) = ({x[-1]:.0f}, {y[-1]:.0f})$",
            fontsize=fontsize,
            color="blue",
            ha="left" if x[-1] >= 0 else "right",
            bbox=bbox_props,
        )
        return (point,)

    if save:
        frame_dir = pathlib.Path(dirname) / "frames_tmp"
        frame_dir.mkdir(parents=True, exist_ok=True)

        print("Rendering frames...")
        for i in range(len(x_flat)):
            update(i)
            fig.patch.set_alpha(0)
            ax.set_facecolor("none")
            frame_path = frame_dir / f"frame_{i:03}.png"
            plt.savefig(frame_path, transparent=True, dpi=600)
            print(f"Saved {frame_path}", end="\r")
        plt.close()

        gif_path = pathlib.Path(dirname) / f"{pathlib.Path(__file__).stem}.gif"
        print(f"\nCreating GIF: {gif_path}")
        cmd = (
            f'magick convert -delay 100 -loop 0 "{frame_dir}/frame_*.png" "{gif_path}"'
        )
        subprocess.run(cmd, shell=True, check=True)

        print("Cleaning up frames...")
        shutil.rmtree(frame_dir)
        print(f"✅ GIF created: {gif_path}")
    else:
        ani = FuncAnimation(
            fig, update, frames=len(x_flat), init_func=init, blit=True, repeat=False
        )
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break
    dirname = "/".join(parts)

    main(dirname=dirname, save=True)
