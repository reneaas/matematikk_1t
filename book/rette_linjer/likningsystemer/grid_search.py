import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rc('text', usetex=True)

# Define the range for x and y values
x_values = np.linspace(-4, 4, 9)
y_values = np.linspace(-4, 4, 9)
x_values, y_values = np.meshgrid(x_values, y_values)
x_values = x_values.flatten()
y_values = y_values.flatten()

# Set up the plot
fig, ax = plt.subplots()
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

x = np.linspace(-5, 5, 1024)

ax.plot(x, x - 1, label=r'$x - y = 1$', lw=2, color="teal", alpha=0.7)
ax.plot(x, -x + 1, label=r'$x + y = 1$', lw=2, color="purple", alpha=0.7)
# ax.legend(fontsize=16)

xticks = list(np.arange(-4, 5, 1))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-4, 5, 1))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)


# Point to animate (initially empty)
point, = ax.plot([], [], 'ko', markersize=15)

plt.xlim(-3, 3)
plt.ylim(-4, 4)

# Initialize the animation
def init():
    point.set_data([], [])
    return point,

# Update function for the animation
def update(frame):
    x = x_values[frame]
    y = y_values[frame]
    point.set_data(x, y)  # Average the y-values to show the midpoint
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    plt.xticks(xticks, fontsize=16)
    plt.yticks(yticks, fontsize=16)
    return point,


plt.grid(True, linestyle="--", alpha=0.7)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.tight_layout()

progress_callback = lambda i, n: print(f"Writing progress: {(i+1) / n * 100 :.1f} %", end="\r")
ani = FuncAnimation(fig, update, frames=range(len(x_values)), init_func=init, blit=True, repeat=False)
ani.save("grid_search.gif", writer="imagemagick", fps=1, progress_callback=progress_callback)
plt.close()
