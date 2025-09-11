# Dev



<!-- :::{multi-plot}
width: 100%
functions: (2*x - 1) / (x + 2), (x**2 - 4) / (x**2 - 1), (x - 1) / (x + 1), (x**2 + 2*x + 1) / (x - 1)
function-names: A, B, C, D
domains: (-20, 20) \ {-2}, (-20, 20) \ {-1, 1}, (-20, 20) \ {-1}, (-20, 20) \ {1}
rows: 2
cols: 2
ticks: off
xmin: -10
xmax: 10
ymin: -15
ymax: 15
vlines: -2, (-1, 1), -1, 1
hlines: 2, 1, 1, None
lines: None, None, None, (1, 3)
:::



:::{plot}
width: 80%
function: (2*x - 1) / (x + 2), (-10, 10) \ {-2}
:::


:::{plot}
width: 80%
function: x**3 - 3*x + 2
point: (0, 2)
line: -3, (0, 2)
:::



---



:::{plot}
width: 80%
function: x, (0, 4), blue
function: 4, (4, 6), red
function: -2*(x - 6) + 4, (6, 8), epic
xmin: -1
xmax: 9
ymin: -1
ymax: 9
xlabel: $t / \mathrm{ s}$
ylabel: $s / \mathrm{ m}$
nocache:
:::


:::{plot}
width: 80%
function: x, (0, 4), blue
function: 4, (4, 6), red
function: -2*(x - 6) + 4, (6, 8), epic
xmin: -1
xmax: 9
ymin: -1
ymax: 9
xlabel: $t / \mathrm{ s}$
ylabel: $s / \mathrm{ m}$
nocache:
annotate: (2, 5), (2, 2), "Del 1", +0.3
annotate: (5, 7), (5, 4), "Del 2"
annotate: (8, 4), (7, 2), "Del 3" 
:::



:::{plot}
width: 80%
function: 1, (0, 4), blue
function: 0, (4, 6), red
function: -2, (6, 8), epic
xmin: -1
xmax: 9
ymin: -4
ymax: 4
xlabel: $t / \mathrm{ s}$
ylabel: $v / (\mathrm{m/s})$
annotate: (2, 3), (2, 1), "Positiv fart"
annotate: (6, 1.5), (5, 0), "I ro"
annotate: (5, -3), (7, -2), "Negativ fart"
:::



:::{plot}
width: 80%
function: 2*x, (0, 2), blue
function: (x - 2) + 4, (2, 4), blue
function: 6, (4, 5), blue
function: -2*(x - 5) + 6, (5, 6), blue
function: 4, (6, 7), blue
function: -4*(x - 7) + 4, (7, 8), blue
ymin: -1
ymax: 9
xmin: -1
xmax: 9
xlabel: $t / \mathrm{ s}$
ylabel: $s / \mathrm{ m}$
:::


:::{plot}
width: 80%
function: 2, (0, 2), blue
function: 1, (2, 4), blue
function: 0, (4, 5), blue
function: -2, (5, 6), blue
function: 0, (6, 7), blue
function: -4, (7,8), blue
xmin: -1
xmax: 9
ymin: -6
ymax: 6
xlabel: $t / \mathrm{ s}$
ylabel: $v / (\mathrm{m/s})$
:::




:::{plot}
width: 80%
function: 2, (0, 2), blue
function: 1*(x - 2) + 2, (2, 3), blue
function: 3, (3, 4), blue
function: -3*(x - 4) + 3, (4, 6), blue
function: -3, (6, 8), blue
function: 1.5*(x - 8) - 3, (8, 10), blue
function: 0, (10, 11), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
ymin: -6
ymax: 6
xmin: -1
xmax: 11
:::


:::{plot}
width: 80%
function: 0, (0, 2), blue
function: 1, (2, 3), blue
function: 0, (3, 4), blue
function: -3, (4, 6), blue
function: 0, (6, 8), blue
function: 3/2, (8, 10), blue
function: 0, (10, 11), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
ymin: -4
ymax: 4
xmin: -1
xmax: 11
:::


:::{plot}
width: 80%
function: x + 2, (0, 3), blue
function: 5, (3, 5), blue
function: -4*(x - 5) + 5, (5, 7), blue
function: -3, (7, 9), blue
ymin: -4
ymax: 8
xmin: -7
xmax: 11
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
annotate: (-4.5, 6), (0, 2), "Startposisjon"
annotate: (1, 6.5), (2, 4), "Positiv fart"
annotate: (6, 6), (4, 5), "I ro"
annotate: (7, 3), (5.5, 3), "Negativ fart"
text: -1, 0.5, "Positiv posisjon", bbox
text: -0.6, -2, "Negativ posisjon", bbox
ticks: off
point: (0, 2)
:::



:::{plot}
width: 80%
function: 2, (0, 1), blue
function: 0, (1, 3), blue
function: -1, (3, 5), blue
function: 1, (5, 7), blue 
function: 0, (7, 8), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
ymin: -4
ymax: 4
xmin: -1
xmax: 9
lw: 3
:::


:::{plot}
width: 80%
function: 2*x + 1, (0, 1), blue
function: 3, (1, 3), blue
function: -1*(x - 3) + 3, (3, 5), blue
function: 1*(x - 5) + 1, (5, 7), blue
function: 3, (7, 8), blue
ymin: -5
ymax: 5
xmin: -1
xmax: 9
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
lw: 3
:::


:::{plot}
width: 80%
function: 2*x + 1 - 2, (0, 1), blue
function: 3 - 2, (1, 3), blue
function: -1*(x - 3) + 3 - 2, (3, 5), blue
function: 1*(x - 5) + 1 - 2, (5, 7), blue
function: 3 - 2, (7, 8), blue
ymin: -5
ymax: 5
xmin: -1
xmax: 9
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
lw: 3
:::



:::{plot}
width: 80%
function: 2, (0, 6), red, v(t)
fill-polygon: (0, 0), (6, 0), (6, 2), (0, 2), blue, 0.3
vline: 6, 0, 2, black, dashdot
text: 4, 0.8, "$s = v \cdot t$", bbox
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
ymin: -1
ymax: 4
xmin: -1
xmax: 8
lw: 2.5
ticks: off
bar: (6.2, 0), 2, vertical
text: 6.2, 1, "$v$", center-right
bar: (0, -0.2), 6, h
text: 3, -0.2, $t$, bottom-center
:::


:::{plot}
width: 80%
function: 2*x, (0, 6), blue, s(t)
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
ymin: -1
ymax: 14
xmin: -1
xmax: 9
ticks: off
:::



:::{plot}
width: 80%
function: x, (0, 5), red
vline: 5, 0, 5, dashdot, black
xmin: -1
xmax: 6
ymin: -1
ymax: 6
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
bar: (5.2, 0), 5, v
bar: (0, -0.2), 5, h
fill-polygon: (0, 0), (5, 0), (5, 5), blue, 0.3
text: 3, -0.2, "$t$", bottom-center
text: 5.2, 2.5, "$v(t)$", center-right
ticks: off
:::


:::{plot}
width: 80%
function: x, (0, 5), red
vline: 5, 0, 5, dashdot, black
xmin: -1
xmax: 6
ymin: -1
ymax: 6
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
bar: (5.2, 0), 5, v
bar: (0, -0.2), 5, h
fill-polygon: (0, 0), (5, 0), (5, 5), blue, 0.3
text: 3, -0.2, "$t$", bottom-center
text: 5.2, 2.5, "$v(t)$", center-right
text: 4.5, 1.2, "$s(t) = \frac{1}{2} \cdot v(t) \cdot t$", bbox
ticks: off
:::



:::{plot}
width: 80%
function: x, (0, 4), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
ymin: -1
ymax: 6
xmin: -1
xmax: 4.5
:::


:::{plot}
width: 80%
function: 1/2 * x**2, (0, 4), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
ymin: -1
ymax: 9
xmin: -1
xmax: 4.5
:::


:::{plot}
width: 80%
function: 1/2 * x**2 + 2, (0, 4), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
ymin: -1
ymax: 12
xmin: -1
xmax: 4.5
:::


:::{plot}
width: 80%
function: 1/2 * x**2 - 3, (0, 4), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
ymin: -4
ymax: 9
xmin: -1
xmax: 4.5
:::


:::{plot}
width: 80%
function: x, (0, 5), red
vline: 5, 0, 5, dashdot, black
xmin: -1
xmax: 6
ymin: -1
ymax: 6
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
bar: (5.2, 0), 5, v
bar: (0, -0.2), 5, h
fill-polygon: (0, 0), (5, 0), (5, 5), blue, 0.3
text: 3, -0.2, "$t$", bottom-center
text: 5.2, 2.5, "$v(t) = a \cdot t$", center-right
text: 4.5, 1.2, "$s(t) = \frac{1}{2} \cdot a \cdot t \cdot t$", bbox
ticks: off
:::


:::{plot}
width: 80%
function: x, (0, 3), blue
function: -2*(x - 3) + 3, (3, 6), blue
function: -3, (6, 8), blue
function: 3*(x - 8) - 3, (8, 9), blue
xmin: -1
xmax: 11
ymin: -6
ymax: 6
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
:::


:::{plot}
width: 80%
function: 2, (0, 3), blue
function: 0, (3, 4), blue
function: -1, (4, 5), blue
function: 0, (5, 6), blue
function: -2, (6, 8), blue 
function: 0, (8, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 11
lw: 3.5
:::




:::{plot}
width: 80%
function: x + 2, (0, 2), blue
function: 4, (2, 3), blue
function: 2*(x - 3) + 4, (3, 5), blue
xmin: -1
xmax: 11
ymin: -7
ymax: 10
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
lw: 3
:::


:::{plot}
width: 80%
function: 0, (5, 6), blue
function: -3, (6, 7), blue
function: -2, (7, 9), blue
function: 1, (9, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 11
ymin: -5
ymax: 5
lw: 3
:::



:::{plot}
width: 80%
function: x, (0, 3), blue
function: 3, (3, 7), blue
function: -(x - 7) + 3, (7, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 11
ymin: -2
ymax: 5
lw: 3
:::



:::{plot}
width: 80%
function: 2, (0, 2), blue
function: (x - 2) + 2, (2, 4), blue,
function: 4, (4, 6), blue
function: -4*(x - 6) + 4, (6, 7), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 9
ymin: -5
ymax: 5
lw: 3
:::



:::{plot}
width: 80%
function: 5, (0, 4), blue
function: -1.5*(x - 4) + 5, (4, 6), blue
function: 2, (6, 10), blue
function: 2*(x - 10) + 2, (10, 12), blue
function: 6, (12, 16), blue
function: -3 * (x - 16) + 6, (16, 18), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -2
xmax: 20
ymin: -2
ymax: 7
xstep: 2
::: -->




:::{plot}
width: 80%
function: (x - 3)**2 + 1, f, (-10, 10), blue
:::







