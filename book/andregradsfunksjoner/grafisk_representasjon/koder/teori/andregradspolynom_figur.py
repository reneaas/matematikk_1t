import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)

def f(x):
    return x**2 - 4


a = -4
b = 4


fig, axes = plt.subplots(1, 2, figsize=(10, 5))

x = np.arange(-3, 4)
axes[0].plot(x, f(x), color="teal", lw=2, alpha=0.7)
axes[0].scatter(x, f(x), color="black", marker="o", s=50)

x = np.linspace(-3, 3, 21)
axes[1].plot(x, f(x), color="teal", lw=2, alpha=0.7)
axes[1].scatter(x, f(x), color="black", marker="o", s=50)


axes[0].spines["left"].set_position("zero")
axes[0].spines["right"].set_color("none")
axes[0].spines["bottom"].set_position("zero")
axes[0].spines["top"].set_color("none")

axes[0].plot(1, 0, ">k", transform=axes[0].get_yaxis_transform(), clip_on=False)
axes[0].plot(0, 1, "^k", transform=axes[0].get_xaxis_transform(), clip_on=False)

axes[0].set_xlabel(r"$x$", fontsize=16, loc="right")
axes[0].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")



axes[1].spines["left"].set_position("zero")
axes[1].spines["right"].set_color("none")
axes[1].spines["bottom"].set_position("zero")
axes[1].spines["top"].set_color("none")

axes[1].plot(1, 0, ">k", transform=axes[1].get_yaxis_transform(), clip_on=False)
axes[1].plot(0, 1, "^k", transform=axes[1].get_xaxis_transform(), clip_on=False)

axes[1].set_xlabel(r"$x$", fontsize=16, loc="right")
axes[1].set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")



xticks = list(np.arange(-3, 4, 1))
xticks.remove(0)
axes[0].set_xticks(xticks)
axes[1].set_xticks(xticks)

yticks = list(np.arange(-4, 6, 1))
yticks.remove(0)
axes[0].set_yticks(yticks)
axes[1].set_yticks(yticks)

axes[0].tick_params(axis="both", labelsize=16)
axes[1].tick_params(axis="both", labelsize=16)

axes[0].set_xlim(-4, 4)
axes[0].set_ylim(-5, 6)

axes[1].set_xlim(-4, 4)
axes[1].set_ylim(-5, 6)

axes[0].grid(True, linestyle="--", alpha=0.6)
axes[1].grid(True, linestyle="--", alpha=0.6)


plt.tight_layout()

# Lagrer to versjoner av figuren.
plt.savefig("../../figurer/eksempler/andregradspolynom.png") 
plt.savefig("../../figurer/eksempler/andregradspolynom.pdf")
plt.savefig("../../figurer/eksempler/andregradspolynom.svg")

plt.show()
