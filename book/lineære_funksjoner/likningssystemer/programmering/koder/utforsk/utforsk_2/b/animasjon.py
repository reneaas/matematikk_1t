import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotmath
import matplotlib as mpl
import sys
import pathlib
import shutil
import subprocess

# Ensure matplotlib uses the correct path to ImageMagick
mpl.rcParams["animation.convert_path"] = "/opt/homebrew/bin/magick"

# Debug path to magick
print("Magick path found by shutil:", shutil.which("magick"))


def find_repo_root(current_path):
    current_path = pathlib.Path(current_path).resolve()
    while current_path != current_path.parent:
        if (current_path / ".git").is_dir():
            return str(current_path)
        current_path = current_path.parent
    raise FileNotFoundError("No .git directory found in any parent directories.")


# Get script directory and repository root
current_dir = str(pathlib.Path(__file__).resolve().parent)
repo_root = find_repo_root(current_dir)

# Build figure directory path
parts = current_dir.split("/")
for i in range(len(parts)):
    if parts[~i] == "koder":
        parts[~i] = "figurer"
        break
dirname = "/".join(parts)

plt.rc("text", usetex=True)
fontsize = 20

# Define coordinate grid
x_min = -3
x_max = 1
n_x = len([i for i in range(x_min, x_max + 1)])

y_min = -1
y_max = 2
n_y = len([i for i in range(y_min, y_max + 1)])

x_values = np.linspace(x_min, x_max, n_x)
y_values = np.linspace(y_min, y_max, n_y)
x_values, y_values = np.meshgrid(x_values, y_values)
x_values = x_values.T.flatten()
y_values = y_values.T.flatten()

# Set up plot
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.set_xlabel(r"$x$", fontsize=fontsize, loc="right")
ax.set_ylabel(r"$y$", fontsize=fontsize, loc="top", rotation="horizontal")

xticks = list(np.arange(-3, 4, 1))
xticks.remove(0)
yticks = list(np.arange(-3, 4, 1))
yticks.remove(0)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.tick_params(labelsize=fontsize)

(point,) = ax.plot([], [], "ko", markersize=10)
ax.set_facecolor("none")
fig.patch.set_alpha(0)


# Animation update function
def init():
    point.set_data([], [])
    return (point,)


def update(frame):
    x = x_values[: frame + 1]
    y = y_values[: frame + 1]
    point.set_data(x, y)
    for txt in ax.texts:
        txt.set_visible(False)
    bbox_props = dict(
        boxstyle="round,pad=0.3", edgecolor="black", facecolor="white", alpha=0.7
    )
    x_coord = 0.5
    y_coord = -3.5
    align = "left" if x[0] >= 0 else "right"
    ax.text(
        x=x_coord,
        y=y_coord,
        s=f"$(x, y) = ({x[-1]:.0f}, {y[-1]:.0f})$",
        fontsize=fontsize,
        color="blue",
        ha=align,
        bbox=bbox_props,
    )
    return (point,)


plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()

# Output directory
fig_dir = pathlib.Path(dirname)
fig_dir.mkdir(parents=True, exist_ok=True)
frame_dir = fig_dir / "frames_tmp"
frame_dir.mkdir(parents=True, exist_ok=True)

# Render each frame to transparent PNG
print("Rendering frames...")
for i in range(len(x_values)):
    update(i)
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    frame_path = frame_dir / f"frame_{i:03}.png"
    plt.savefig(frame_path, transparent=True, dpi=600)
    print(f"Saved {frame_path}", end="\r")

plt.close()

# Build GIF using ImageMagick
print("\nCreating GIF with ImageMagick...")
gif_name = f"{fig_dir}/{pathlib.Path(__file__).stem}.gif"
cmd = f'magick convert -delay 100 -loop 0 "{frame_dir}/frame_*.png" "{gif_name}"'
subprocess.run(cmd, shell=True, check=True)

# Clean up temporary frames
print("Cleaning up frames...")
shutil.rmtree(frame_dir)

print(f"✅ GIF created: {gif_name}")
