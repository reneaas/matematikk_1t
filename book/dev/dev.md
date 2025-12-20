# Dev

:::{plot}
width: 100%
function: (x - 1)**2 - 4, f
tangent: 2, f
tangent: -1, f
point: (2, f(2))
point: (-1, f(-1))
ticks: off
text: 2, f(2), "$(2, f(2))$", bottom-right
text: -1, f(-1), "$(-1, f(-1))$", bottom-left
ymin: -8
:::


:::{plot}
width: 70%
function: 2 * (x - 1), f'
:::



:::{plot}
width: 70%
function: -2*(x + 3) * (x - 1), f
tangent: 1, f
tangent: -3, f
point: (1, f(1))
point: (-3, f(-3))
ymax: 12
ticks: off
text: -3, 0, "$A$", top-left
text: 1, 0, "$B$", top-right
:::


