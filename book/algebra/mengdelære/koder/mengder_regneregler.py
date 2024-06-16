import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rc("text", usetex=True)
plt.rcParams.update({
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})


def circle(x, y, r):
    angles = np.linspace(0, 2*np.pi, 1024)
    x = x + r*np.cos(angles)
    y = y + r*np.sin(angles)
    return x, y

def circle_fn(r, x0, y0):
    x = np.linspace(x0 - r, x0 + r, 1024)
    y_upper = np.sqrt(r**2 - (x - x0)**2) + y0
    y_lower = -np.sqrt(r**2 - (x - x0)**2) + y0
    return x, y_upper, y_lower


# Figur for A snitt B


# plt.plot(*circle(-1, 0, 2), color="blue")
# plt.plot(*circle(1, 0, 2), color="red")

# x1, y1_upper, y1_lower = circle_fn(2, -1, 0)
# x2, y2_upper, y2_lower = circle_fn(2, 1, 0)

# plt.fill_between(x2, y1_upper, 0, where=y1_upper>y2_upper, color="blue", alpha=0.3)

x1, y1 = circle(-1, 0, 2)
x2, y2 = circle(1, 0, 2)

plt.fill(*circle(-1, 0, 2), color="blue", alpha=0.3)
plt.fill(*circle(1, 0, 2), color="red", alpha=0.3)


plt.text(
    x=-2,
    y=0,
    s=r"$A$",
    fontsize=22,
    ha="center",
    va="center",
)

plt.text(
    x=2,
    y=0,
    s=r"$B$",
    fontsize=22,
    ha="center",
    va="center",
)

# plt.title(r"$A \cap B$", fontsize=18)
plt.axis("equal")
plt.axis("off")
plt.show()