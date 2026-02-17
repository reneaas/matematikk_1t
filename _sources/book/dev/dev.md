# Dev


:::{plot}
width: 70%
function: -x**2 + 16, f, (-4, 4)
tangent: 2, f, solid, red
point: (2, f(2))
point: (0, 20)
point: (5, 0)
point: (0, 0)
ymin: -1
ymax: 22
ticks: off
text: 0, 0, "$O$", bottom-left
text: 5, 0, "$A$", bottom-left
text: 0, 20, "$B$", center-left
text: 2, f(2), "$(a, f(a))$", top-right
fill-polygon: (0, 0), (5, 0), (0, 20), blue, 0.2
nocache:
:::



:::{plot}
handdrawn: true
function: sin(x), f(x)
:::

:::{plot}
width: 70%
function: -x**3 + 4 * x**2, (0, 4), f
point: (0, 0)
point: (2, 0)
point: (2, f(2))
point: (0, f(2))
polygon: (0, 0), (2, 0), (2, f(2)), (0, f(2))
fill-polygon: (0, 0), (2, 0), (2, f(2)), (0, f(2)), blue, 0.2
ticks: off
xmin: -0.5
xmax: 4.5
ymin: -1
ymax: 11
text: 0, 0, "$A$", bottom-left
text: 2, 0, "$B(k, 0)$", bottom-right
text: 2, f(2), "$C$", top-center
text: 0, f(2), "$D$", top-left
:::

:::{plot}
function: 2 * x**3 - x**2 - 4*x + 8, (0, 2), h, blue
xmin: -0.5
xmax: 2.5
ymin: -1
ymax: 14
ticks: off
:::

:::{plot}
function: 2 * x**3 - x**2 - 4*x + 8, (0, 2), h, blue
xmin: -0.5
xmax: 2.5
ymin: -1
ymax: 14
ticks: off
line-segment: (0, h(0)), (0.5, h(0)), dashed, gray
text: 0.5 * 0.5, h(0), "$\Delta x$", top-center
line-segment: (0.5, h(0)), (0.5, h(0.5)), dashed, gray
text: 0.5, 0.5 * (h(0) + h(0.5)), "$\Delta y_1$", center-right
line-segment: (0, h(0)), (0.5, h(0.5)), solid, black
text: 0.5 * 0.5, 0.5 * (h(0) + h(0.5)), "$\ell_1$", bottom-left
line-segment: (0.5, h(0.5)), (1, h(1)), solid, black
text: 0.5 * (0.5 + 1), 0.5 * (h(0.5) + h(1)), "$\ell_2$", bottom-left
line-segment: (1, h(1)), (1.5, h(1.5)), solid, black
text: 0.5 * (1 + 1.5), 0.5 * (h(1) + h(1.5)), "$\ell_3$", top-left
line-segment: (1.5, h(1.5)), (2, h(2)), solid, black
text: 0.5 * (1.5 + 2), 0.5 * (h(1.5) + h(2)), "$\ell_4$", top-left
point: (0, h(0))
point: (0.5, h(0.5))
point: (1, h(1))
point: (1.5, h(1.5))
point: (2, h(2))
line-segment: (1.5, h(1.5)), (2, h(1.5)), dashed, gray
line-segment: (2, h(1.5)), (2, h(2)), dashed, gray
text: 2, 0.5 * (h(1.5) + h(2)), "$\Delta y_4$", center-right
text: 1.75, h(1.5), "$\Delta x$", bottom-center
handdrawn: true
nocache:
:::


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
function: 2 * x**3 - x**2 - 4*x + 8, (0, 2), h, blue
xmin: -0.5
xmax: 2.5
ymin: -1
ymax: 14
ticks: off
:::

:::{plot}
function: 2 * x**3 - x**2 - 4*x + 8, (0, 2), h, blue
xmin: -0.5
xmax: 2.5
ymin: -1
ymax: 14
ticks: off
line-segment: (0, h(0)), (0.5, h(0)), dashed, gray
text: 0.5 * 0.5, h(0), "$\Delta x$", top-center
line-segment: (0.5, h(0)), (0.5, h(0.5)), dashed, gray
text: 0.5, 0.5 * (h(0) + h(0.5)), "$\Delta y_1$", center-right
line-segment: (0, h(0)), (0.5, h(0.5)), solid, black
text: 0.5 * 0.5, 0.5 * (h(0) + h(0.5)), "$\ell_1$", bottom-left
line-segment: (0.5, h(0.5)), (1, h(1)), solid, black
text: 0.5 * (0.5 + 1), 0.5 * (h(0.5) + h(1)), "$\ell_2$", bottom-left
line-segment: (1, h(1)), (1.5, h(1.5)), solid, black
text: 0.5 * (1 + 1.5), 0.5 * (h(1) + h(1.5)), "$\ell_3$", top-left
line-segment: (1.5, h(1.5)), (2, h(2)), solid, black
text: 0.5 * (1.5 + 2), 0.5 * (h(1.5) + h(2)), "$\ell_4$", top-left
point: (0, h(0))
point: (0.5, h(0.5))
point: (1, h(1))
point: (1.5, h(1.5))
point: (2, h(2))

:::
::::




:::{plot}
width: 70%
ellipse: (0, 4), 2, 0.7, solid, black
line-segment: (0, 0), (2, 4), solid, black
line-segment: (0, 0), (-2, 4), solid, black
nocache:
vline: 0, 0, 4, dashed, gray
hline: 4, 0, 2, dashed, gray
text: 0, 2, "$h$", center-right
text: 1, 4, "$r$", top-center
text: 1, 2, "$\ell$", bottom-right
figsize: (4, 4)
xmin: -3
xmax: 3
ymin: -1
ymax: 5
ticks: off
axis: off
line-segment: (0.3, 4), (0.3, 3.7), solid, gray
line-segment: (0, 3.7), (0.3, 3.7), solid, gray
:::



:::{plot}
width: 70%
function: -2 * (x + 1)**2 + 8, f
ymax: 10
xmax: 4
:::


:::{plot}
width: 70%
function: (x - 3) * (x + 2) * (x - 1), f'
yticks: off
grid: off
ymax: 10
ymin: -6
xmax: 5
xmin: -5
:::


::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 26
---
:::{plot}
function: -(1 / 4 * x**4 - 2 / 3 * x**3 - 5 / 2 * x**2 + 6*x) - 4
ymin: -14
ymax: 10
xmax: 5
xmin: -5
yticks: off
grid: off
text: 4, 8, "A", bbox
:::

:::{plot}
function: 0.25 * (x + 2)**2 * (x - 1) * (x - 3)
ymin: -14
ymax: 10
xmax: 5
xmin: -5
yticks: off
grid: off
text: 4, 8, "B", bbox
:::

:::{plot}
function: 1 / 4 * x**4 - 2 / 3 * x**3 - 5 / 2 * x**2 + 6*x + 3
ymin: -14
ymax: 10
xmax: 5
xmin: -5
yticks: off
grid: off
text: 4, 8, "C", bbox
:::

:::{plot}
function: -0.5 * (1 / 4 * x**4 - 2 / 3 * x**3 - 5 / 2 * x**2 + 6*x)
ymin: -14
ymax: 10
xmax: 5
xmin: -5
yticks: off
grid: off
text: 4, 8, "D", bbox
:::

::::



:::{plot}
width: 70%
function: 2*(x**2 - 4) / (x**2 - 1), f
ymax: 12
ymin: -12
vline: -1, dashed, red
vline: 1, dashed, red
hline: 2, dashed, red
ystep: 2
:::



