import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

plt.rc("text", usetex=True)

def f(x, a, b):
    return a*x + b


k = 2

x_min = -8
x_max = 8


x = np.linspace(x_min, x_max, 1024)

a = 2
b = -1

xlim = (-4, 6)
ylim = (-5, 5)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))


# ax + b > k eller ax + b >= k
j = 1
ax[j].plot(x, f(x, a=a, b=b), color="teal", lw=2, alpha=0.7)
ax[j].plot(((k-b)/a), k, "ko", markersize=8, alpha=0.7)
ax[j].plot(((k-b)/a), 0, "k|", markersize=15, alpha=0.7)
ax[j].hlines(k, -8, 8, color="purple", alpha=0.7, lw=2)

ax[j].spines["left"].set_position("zero")
ax[j].spines["right"].set_color("none")
ax[j].spines["bottom"].set_position("zero")
ax[j].spines["top"].set_color("none")

ax[j].plot(1, 0, ">k", transform=ax[j].get_yaxis_transform(), clip_on=False)
ax[j].plot(0, 1, "^k", transform=ax[j].get_xaxis_transform(), clip_on=False)

ax[j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[j].set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")

ax[j].set_xticks([])
ax[j].set_yticks([])
ax[j].set_ylim(*ylim)
ax[j].set_xlim(*xlim)



ax[j].text(
    s=r"$ax + b > k$ eller $ax + b \geq k$",
    x=0,
    y=4,
    fontsize=16,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[j].annotate(
    text="Løsningsmengde",
    xy=((k-b)/a + 0.1, 0),
    xytext=(3, -3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=((k-b)/a + 2, 0),
    xytext=(3, -3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(5.5, 0),
    xytext=(3, -3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].hlines(0, (k-b)/a, 8, color="red", alpha=0.3, lw=8)
ax[j].vlines((k-b)/a, 0, k, color="black", alpha=0.5, linestyle="--")



# ax + b < 0 eller ax + b <= 0
j = 0
ax[j].plot(x, f(x, a=a, b=b), color="teal", lw=2, alpha=0.7)
ax[j].plot(((k-b)/a), k, "ko", markersize=8, alpha=0.7)
ax[j].plot(((k-b)/a), 0, "k|", markersize=15, alpha=0.7)
ax[j].hlines(k, -8, 8, color="purple", alpha=0.7, lw=2)

ax[j].spines["left"].set_position("zero")
ax[j].spines["right"].set_color("none")
ax[j].spines["bottom"].set_position("zero")
ax[j].spines["top"].set_color("none")

ax[j].plot(1, 0, ">k", transform=ax[j].get_yaxis_transform(), clip_on=False)
ax[j].plot(0, 1, "^k", transform=ax[j].get_xaxis_transform(), clip_on=False)

ax[j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[j].set_ylabel(r"$f(x)$", fontsize=16, loc="top", rotation="horizontal")




# ax[j].set_xticks([-b/a], labels=[r"$x_1$"], fontsize=16)
ax[j].set_xticks([])
ax[j].set_yticks([])
ax[j].set_ylim(*ylim)
ax[j].set_xlim(*xlim)


ax[j].text(
    s=r"$ax + b < k$ eller $ax + b \leq k$",
    x=3,
    y=-4,
    fontsize=16,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=((k-b)/a - 0.1, 0),
    xytext=(-1, 3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=((k-b)/a - 2, 0),
    xytext=(-1, 3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(-3.5, 0),
    xytext=(-1, 3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].hlines(0, -8, (k-b)/a, color="red", alpha=0.3, lw=8)

ax[j].vlines((k-b)/a, 0, k, color="black", alpha=0.5, linestyle="--")


plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/ulikhet_type_2.svg")

plt.show()
