import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return 2*x - 1


def circle(x0, y0, r):
    theta = np.linspace(0, 2*np.pi, 1024)
    x = r * np.cos(theta) + x0
    y = r * np.sin(theta) + y0
    return x, y


def bernoulli_lemniscate(a):
    theta = np.linspace(0, 2*np.pi, 1024)
    x = a * np.cos(theta) / (1 + np.sin(theta)**2)
    y = a * np.cos(theta) * np.sin(theta) / (1 + np.sin(theta)**2)
    return x, y

def g(x):
    return x**3 - 3*x

def logaritmic_spiral(a, b, w):
    theta = np.linspace(a, b, 4096)
    r = np.exp(theta)
    x = r * np.cos(w * theta)
    y = r * np.sin(w * theta)
    return x, y






fig, ax = plt.subplots(2, 2, figsize=(10, 8))


# Graf 1 (0, 0)
i = 0
j = 0

a = -5
b = 7
x = np.linspace(a, b, 1024)
ax[i, j].plot(x, f(x), color="teal", lw=2, alpha=0.7, label="$A$")

ax[i, j].spines["left"].set_position("zero")
ax[i, j].spines["right"].set_color("none")
ax[i, j].spines["bottom"].set_position("zero")
ax[i, j].spines["top"].set_color("none")

ax[i, j].plot(1, 0, ">k", transform=ax[i, j].get_yaxis_transform(), clip_on=False)
ax[i, j].plot(0, 1, "^k", transform=ax[i, j].get_xaxis_transform(), clip_on=False)

ax[i, j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[i, j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-2, 5, 1))
xticks.remove(0)
ax[i, j].set_xticks(xticks)

yticks = list(np.arange(-2, 6, 1))
yticks.remove(0)
ax[i, j].set_yticks(yticks)

ax[i, j].set_xlim(-3, 5)
ax[i, j].set_ylim(-2, 6)

ax[i, j].tick_params(labelsize=16)

ax[i, j].grid(True, linestyle="--", alpha=0.6)

ax[i, j].legend(fontsize=16, loc="upper right")



# Graf 2 (0, 1)
i = 0
j = 1

x, y = bernoulli_lemniscate(a=2)
ax[i, j].plot(x, y, color="teal", lw=2, alpha=0.7, label="$B$")

ax[i, j].spines["left"].set_position("zero")
ax[i, j].spines["right"].set_color("none")
ax[i, j].spines["bottom"].set_position("zero")
ax[i, j].spines["top"].set_color("none")

ax[i, j].plot(1, 0, ">k", transform=ax[i, j].get_yaxis_transform(), clip_on=False)
ax[i, j].plot(0, 1, "^k", transform=ax[i, j].get_xaxis_transform(), clip_on=False)

ax[i, j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[i, j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-2, 3, 1))
xticks.remove(0)
ax[i, j].set_xticks(xticks)

yticks = list(np.arange(-1, 2, 1))
yticks.remove(0)
ax[i, j].set_yticks(yticks)

ax[i, j].set_xlim(-3, 3)
ax[i, j].set_ylim(-2, 2)

ax[i, j].tick_params(labelsize=16)

ax[i, j].grid(True, linestyle="--", alpha=0.6)

ax[i, j].legend(fontsize=16, loc="upper right")



# Graf 3 (1, 0)
i = 1
j = 0

# x, y = logaritmic_spiral(a=-10, b=0, w=10)
# ax[i, j].plot(x, y, color="teal", lw=2, alpha=0.7, label="$C$")

ax[i, j].vlines(x=-1, ymin=-5, ymax=5, color="teal", lw=2, alpha=0.7, label="$C$")

ax[i, j].spines["left"].set_position("zero")
ax[i, j].spines["right"].set_color("none")
ax[i, j].spines["bottom"].set_position("zero")
ax[i, j].spines["top"].set_color("none")

ax[i, j].plot(1, 0, ">k", transform=ax[i, j].get_yaxis_transform(), clip_on=False)
ax[i, j].plot(0, 1, "^k", transform=ax[i, j].get_xaxis_transform(), clip_on=False)

ax[i, j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[i, j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-3, 4, 1))
xticks.remove(0)
ax[i, j].set_xticks(xticks)

yticks = list(np.arange(-4, 5, 1))
yticks.remove(0)
ax[i, j].set_yticks(yticks)

ax[i, j].set_xlim(-4, 4)
ax[i, j].set_ylim(-5, 5)


ax[i, j].tick_params(labelsize=16)

ax[i, j].grid(True, linestyle="--", alpha=0.6)

ax[i, j].legend(fontsize=16, loc="upper right")



# Graf 4 (1, 1)
i = 1
j = 1

# a = -2
# b = 2
# x = np.linspace(a, b, 1024)
# ax[i, j].plot(x, g(x), color="teal", lw=2, alpha=0.7, label="$D$")
ax[i, j].hlines(y=-1, xmin=-5, xmax=5, color="teal", lw=2, alpha=0.7, label="$D$")

ax[i, j].spines["left"].set_position("zero")
ax[i, j].spines["right"].set_color("none")
ax[i, j].spines["bottom"].set_position("zero")
ax[i, j].spines["top"].set_color("none")

ax[i, j].plot(1, 0, ">k", transform=ax[i, j].get_yaxis_transform(), clip_on=False)
ax[i, j].plot(0, 1, "^k", transform=ax[i, j].get_xaxis_transform(), clip_on=False)

ax[i, j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[i, j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-3, 4, 1))
xticks.remove(0)
ax[i, j].set_xticks(xticks)

yticks = list(np.arange(-4, 5, 1))
yticks.remove(0)
ax[i, j].set_yticks(yticks)

ax[i, j].set_xlim(-4, 4)
ax[i, j].set_ylim(-5, 5)

ax[i, j].tick_params(labelsize=16)

ax[i, j].grid(True, linestyle="--", alpha=0.6)

ax[i, j].legend(fontsize=16, loc="upper right")


# plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/underveisoppgaver/funksjonsbegrepet/funksjonsgraf_vs_kurve_oppgave1.svg")

plt.show()
