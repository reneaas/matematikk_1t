# Dev


:::{plot}
width: 70%
function: -2*(x + 2) * (x - 1) / ((x + 1) * (x - 2)), f
vline: -1, dashed, red
vline: 2, dashed, red
hline: -2, dashed, red
point: (-2, 0)
point: (1, 0)
yticks: off
ymin: -10
ymax: 10
grid: false
:::


::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
yticks: off
grid: off
ymin: -6
ymax: 6
xmin: -6
xmax: 6
---

:::{plot}
function: -(x + 2) * (x - 1)
point: (-2, 0)
point: (1, 0)
text: 5, 4, "A", bbox
:::

:::{plot}
function: (x - 2) * (x + 1)
point: (2, 0)
point: (-1, 0)
text: 5, 4, "B", bbox
:::

:::{plot}
function: -(x - 2) * (x + 1)
point: (2, 0)
point: (-1, 0)
text: 5, 4, "C", bbox
:::

:::{plot}
function: (x + 2)**2 * (x - 1)
point: (-2, 0)
point: (1, 0)
text: 5, 4, "D", bbox
:::

::::





::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
ticks: off
xmin: -8
xmax: 8
ymin: -8
ymax: 8
---
:::{plot}
function: -(x**2 - 4) / (x**2 + 1)
point: (-2, 0)
point: (2, 0)
hline: -1, dashed, red
text: 6, 6, "A", bbox
:::


:::{plot}
function: (x**2 + 1) / (x**2 - 4)
vline: -2, dashed, red
vline: 2, dashed, red
hline: 1, dashed, red
text: 6, 6, "B", bbox
:::


:::{plot}
function: (x**2 - 1) / (x**2 - 4)
point: (1, 0)
point: (-1, 0)
vline: -2, dashed, red
vline: 2, dashed, red
hline: 1, dashed, red
text: 6, 6, "C", bbox
:::


:::{plot}
function: -(x**2 - 4) / (x**2 - 1)
vline: -1, dashed, red
vline: 1, dashed, red
hline: -1, dashed, red
point: (-2, 0)
point: (2, 0)
text: 6, 6, "D", bbox
:::



::::



::::{multi-plot2}
---
rows: 2
cols: 2
ticks: off
fontsize: 25
---

:::{plot}
function: (x + 4)**2 * (x - 1) / (x**2 - 9)
:::



:::{plot}
function: (x + 3)**2 * (x - 1) / (x**2 - 9)
ymin: -25
ymax: 25
xmin: -15
xmax: 15
point: (1, 0)
point: (-3, 0)
:::


:::{plot}
function: -(x + 4)**2 * (x - 1) / (x**2 - 9)
:::


:::{plot}
function: (x - 3)**2 * (x - 1) / (x**2 - 9)
ymin: -25
ymax: 25
xmin: -15
xmax: 15
point: (1, 0)
point: (3, 0)
:::
::::

