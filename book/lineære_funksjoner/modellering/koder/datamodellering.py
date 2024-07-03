import numpy as np
import matplotlib.pyplot as plt

#plt.rc("text", usetex=True)

x = np.array([15, 30, 45, 60, 75, 90])
y = np.array([18, 25, 55, 78, 90, 120])

a, b = np.polyfit(x, y, 1)

fig, ax = plt.subplots()
# ax.plot(x, y, color="black", alpha=0.7)
# Plot punktene
ax.plot(x, y, color="black", alpha=0.7, marker="o", linestyle="none")

# Plott grafene til tre modeller
x = np.linspace(-10, 130, 1024)
ax.plot(x, a*x + b, color="blue", lw=1.5, linestyle="-", alpha=0.7)
ax.plot(x, a*x + (b+6), color="red", lw=1.5, linestyle="-", alpha=0.7)
ax.plot(x, (a+0.5)*x + b, color="green", lw=1.5, linestyle="-", alpha=0.7)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.set_xlabel(r"$x$", fontsize=16, loc="right")
ax.set_ylabel(r"$y$", fontsize=16, loc="top", rotation="horizontal")


xticks = list(np.arange(-15, 100, 15))
xticks.remove(0)
plt.xticks(xticks, fontsize=16)

yticks = list(np.arange(-20, 160, 20))
yticks.remove(0)
plt.yticks(yticks, fontsize=16)

plt.ylim(-10, 150)
plt.xlim(-10, 100)

plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Lagrer figuren i vektorformat
plt.savefig("/home/eva/matematikk_1t/book/rette_linjer/modellering/figurer/datamodellering.svg")

plt.show()
