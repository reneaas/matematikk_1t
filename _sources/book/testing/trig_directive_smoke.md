# Trig directive: smoke test

Below are a few minimal examples to validate the trig directive parses, renders, labels, and caches correctly.

:::{trig}
name: trig-smoke-1
width: 60%
figsize: (4, 3)
axis: equal
triangle: T, (0, 0), (4, 0), (2, 3), solid, blue
fill: T, blue, 0.12
show_vertices: T
label-sides: T, numeric
label-angles: T, numeric
:::

:::{trig}
width: 60%
figsize: (4, 4)
axis: equal
triangle: U, (0, 0), (2*sqrt(3), 0), (0, 2), dashed, red
label-sides: U, exact
label-angles: U, exact
:::

:::{trig}
name: trig-right-angle
width: 60%
figsize: (4, 3)
axis: equal
triangle: R, (0, 0), (3, 0), (0, 4), solid, green
label-sides: R, numeric
label-angles: R, numeric
:::
