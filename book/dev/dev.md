# Dev




:::{plot}
width: 70%
function: -2*x + 4, f
:::




:::::::::::::::{exercise} Oppgave 1

I figuren nedenfor ser du en graf.

:::{plot}
width: 70%
function: 2*x - 1, f
:::


:::::::::::::::



:::::::::::::::{exercise} Oppgave 2

:::{plot}
width: 400
function: 2*x + 1, f
align: right
fontsize: 26
nocache:
lw: 3.5
:::

I figuren til høyre ser du grafen til en lineær funksjon $f$.

Bestem $f(x)$. 




:::::::::::::::



:::::::::::::::{exercise} Oppgave 2

:::{figure} ./figurer/figur.svg
---
class: no-click, adaptive-figure
width: 100%
align: right
---
:::

I figuren til høyre ser du grafen til en lineær funksjon $f$.

Bestem $f(x)$. 




:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3


:::{plot}
width: 70%
axis: off, equal
hline: 0, -6, 6, solid
vline: 0, 0, 2, dashed, gray
point: (0, 2)
:::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4


:::{signchart}
width: 100%
function: (x - 2)*(x + 2)*(x - 1)**2/(x + 1)**3, f(x)
:::


:::::::::::::::




:::::::::::::::{exercise} Oppgave 5

:::{plot}
width: 80%
ticks: off
axis: off
xmin: -20
xmax: 500
ymax: 100
ymin: -100
lw: 1
figsize: (7, 5)
function: 70/75**2 * (x - 75)**2, (0, 150), blue
function: -70/75**2 * (x - (75 * sqrt(2) + 75))**2 + 70, (75 * sqrt(2), 75 * sqrt(2) + 150), blue
function: 70/75**2 * (x - (2 * 75 * sqrt(2) + 75))**2, (2 * 75 * sqrt(2), 2 * 75 * sqrt(2) + 150), blue
function: -70/75**2 * (x - (3 * 75 * sqrt(2) + 75))**2 + 70, (3 * 75 * sqrt(2), 3 * 75 * sqrt(2) + 150), blue
function: -70/75**2 * (x - 75)**2, (0, 150), blue
function: 70/75**2 * (x - (75 * sqrt(2) + 75))**2 - 70, (75 * sqrt(2), 75 * sqrt(2) + 150), blue
function: -70/75**2 * (x - (2 * 75 * sqrt(2) + 75))**2, (2 * 75 * sqrt(2), 2 * 75 * sqrt(2) + 150), blue
function: 70/75**2 * (x - (3 * 75 * sqrt(2) + 75))**2 - 70, (3 * 75 * sqrt(2), 3 * 75 * sqrt(2) + 150), blue
vline: 0, -70, 70, solid, blue
hline: -70, 0, 3 * 75 * sqrt(2) + 150, solid, blue
vline: 3 * 75 * sqrt(2) + 150, -70, 70, solid, blue
hline: 70, 0, 3 * 75 * sqrt(2) + 150, solid, blue
hline: 0, 75 * sqrt(2), 75 * sqrt(2) + 150, solid, blue
hline: 0, 3 * 75 * sqrt(2), 3 * 75 * sqrt(2) + 150, solid, blue
hline: 35, 0, 3 * 75 * sqrt(2) + 150, dashed, gray
hline: 0, 0, 3 * 75 * sqrt(2) + 150, dashed, gray
bar: (0, 80), 150, horizontal
text: 75, 85, "150 cm", top-center
bar: (-12, 35), 35, vertical 
text: -12, 52.5, "35 cm", center-left
bar: (480, 0), 70, vertical
text: 480, 35, "70 cm", center-right
nocache:
:::



:::::::::::::::



:::{plot}
width: 70%
function: x**2 - 3*x + 2, f, (0, 2*sqrt(5)), red
point: (3 + 1, f(3) - 2)
point: (1, f(1))
text: sqrt(2) + 1, f(3) - 2, "$(3 + 1, f(3) - 2)$", center-center
annotate: (-sqrt(3), f(2) + sqrt(2)), (sqrt(2) + 1, f(3) - 3), "Sjekk her a", -0.3
annotate: (-4, 4), (1, 1), "Sjekk her b", 0.3
nocache:
:::


:::{plot}
width: 70%
line-segment: (-sqrt(3) - 2, exp(-2) + 1), (sqrt(2) + 2, 2*sqrt(4) - 2), dashed, gray
nocache:
:::




:::{plot}
width: 70%
circle: (0, 0), 1
circle: (2, -sqrt(2)), 2*sqrt(2), dashed, red
nocache:
:::


:::{plot}
width: 70%
axis: equal
circle: (0, 0), 1
ellipse: (0, 0), 1, 2, dashed, red
nocache:
:::


:::{plot}
width: 70%
axis: equal
curve: 2 * sin(-t), 5 * cos(t), (0, 2*pi), solid, red
vector: 0, 0, 5*cos(pi/6), 5*sin(pi/6), red
angle-arc: (0, 0), 1.2, 0, 30
nocache:
:::



---


:::{plot}
branched-function: 2*x + 1, (-2, 1), 3, [1, 3)
xmin: -12
xmax: 12
ymin: -5
ymax: 15
grid: true
ticks: true
fontsize: 20
width: 70%
:::