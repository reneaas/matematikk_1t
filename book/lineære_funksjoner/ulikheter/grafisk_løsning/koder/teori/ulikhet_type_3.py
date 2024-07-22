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

a = 1
b = -3

c = -2
d = 1

x_sol = (-b + d) / (a - c)

xlim = (-4, 6)
ylim = (-5, 5)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))


# ax + b > k eller ax + b >= k
j = 1
ax[j].plot(x, f(x, a=a, b=b), color="teal", lw=2, alpha=0.7, label="$f(x) = ax + b$")
ax[j].plot(x, f(x, a=c, b=d), color="purple", lw=2, alpha=0.7, label="$g(x) = cx + d$") 
ax[j].plot(x_sol, f(x_sol, a, b), "ko", markersize=8, alpha=0.7)
ax[j].plot(x_sol, 0, "k|", markersize=15, alpha=0.7)

ax[j].spines["left"].set_position("zero")
ax[j].spines["right"].set_color("none")
ax[j].spines["bottom"].set_position("zero")
ax[j].spines["top"].set_color("none")

ax[j].plot(1, 0, ">k", transform=ax[j].get_yaxis_transform(), clip_on=False)
ax[j].plot(0, 1, "^k", transform=ax[j].get_xaxis_transform(), clip_on=False)

ax[j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")

ax[j].set_xticks([])
ax[j].set_yticks([])
ax[j].set_ylim(*ylim)
ax[j].set_xlim(*xlim)



ax[j].text(
    s="$ax + b > cx + d$ \n eller \n $ax + b \\geq cx + d$",
    x=2.2,
    y=4,
    fontsize=16,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    horizontalalignment="center",
    verticalalignment="center",
)


ax[j].annotate(
    text="Løsningsmengde",
    xy=(x_sol + 0.1, 0),
    xytext=(3.8, -3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(x_sol + 2, 0),
    xytext=(3.8, -3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(5.5, 0),
    xytext=(3.8, -3),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].hlines(0, x_sol, 8, color="red", alpha=0.3, lw=8)
ax[j].vlines(x_sol, 0, f(x_sol, a, b), color="black", alpha=0.5, linestyle="--")
# ax[j].legend(fontsize=16, loc="upper right", bbox_to_anchor=(0, 1), fancybox=True, framealpha=0.7)





# ax + b < 0 eller ax + b <= 0
j = 0
ax[j].plot(x, f(x, a=a, b=b), color="teal", lw=2, alpha=0.7, label="$f(x) = ax + b$")
ax[j].plot(x, f(x, a=c, b=d), color="purple", lw=2, alpha=0.7, label="$g(x) = cx + d$") 
ax[j].plot(x_sol, f(x_sol, a, b), "ko", markersize=8, alpha=0.7)
ax[j].plot(x_sol, 0, "k|", markersize=15, alpha=0.7)

ax[j].spines["left"].set_position("zero")
ax[j].spines["right"].set_color("none")
ax[j].spines["bottom"].set_position("zero")
ax[j].spines["top"].set_color("none")

ax[j].plot(1, 0, ">k", transform=ax[j].get_yaxis_transform(), clip_on=False)
ax[j].plot(0, 1, "^k", transform=ax[j].get_xaxis_transform(), clip_on=False)

ax[j].set_xlabel(r"$x$", fontsize=16, loc="right")
ax[j].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")




# ax[j].set_xticks([-b/a], labels=[r"$x_1$"], fontsize=16)
ax[j].set_xticks([])
ax[j].set_yticks([])
ax[j].set_ylim(*ylim)
ax[j].set_xlim(*xlim)


ax[j].text(
    s="$ax + b < cx + d$ \n eller \n $ax + b \\leq cx + d$",
    x=2.2,
    y=4,
    fontsize=16,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=2),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(x_sol - 0.1, 0),
    xytext=(-1, -2),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(x_sol - 2, 0),
    xytext=(-1, -2),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].annotate(
    text="Løsningsmengde",
    xy=(-3.5, 0),
    xytext=(-1, -2),
    fontsize=16,
    arrowprops=dict(arrowstyle="->", lw=2, color="black", alpha=0.7),
    horizontalalignment="center",
    verticalalignment="center",
)

ax[j].hlines(0, -8, x_sol, color="red", alpha=0.3, lw=8)

ax[j].vlines(x_sol, 0, f(x_sol, a, b), color="black", alpha=0.5, linestyle="--")



plt.legend(fontsize=14, loc="upper center", bbox_to_anchor=(0, 1), fancybox=True, framealpha=0.7)


plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("../../figurer/teori/ulikhet_type_3.svg")

plt.show()
