# Oppsummering: Trigonometri

::::::::{grid}
---
gutter: 2
columns: 12
---
::::::{grid-item-card}
---
columns: 6
---
**Sinus, cosinus og tangens**
^^^
:::{plot}
figsize: (6, 3)
axis: off
axis: equal
width: 100%
let: s = 6
let: Ax = 0
let: Ay = 0
let: v = 30 * pi / 180
let: Bx = s * cos(v)
let: By = 0
let: Cx = s * cos(v)
let: Cy = s * sin(v)
triangle: points=((Ax, Ay), (Bx, By), (Cx, Cy)), angles=(A, B), angle-radius=70, angle-text=(A="$v$")
nocache:
fontsize: 30
let: ds = 0.3
text: 0.5 * (Ax + Bx), -ds, "Hosliggende katet", bottom-center
text: Bx + ds, 0.5 * (By + Cy), "Motstående\\ \,katet", center-right
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "Hypotenus", top-left
:::

$$
\begin{align*}
\sin v &= \dfrac{\mathrm{mot}}{\mathrm{hyp}} \\
\\
\cos v &= \dfrac{\mathrm{hos}}{\mathrm{hyp}} \\
\\
\tan v &= \dfrac{\mathrm{mot}}{\mathrm{hos}} = \dfrac{\sin v}{\cos v}
\end{align*}
$$



::::::


::::::{grid-item-card}
---
columns: 6
---
**Enhetssirkelen**
^^^
:::{plot}
circle: (0, 0), 1, blue, solid
let: v = 120
let: Px = cos(v * pi / 180)
let: Py = sin(v * pi / 180)
point: (Px, Py)
text: Px, Py, "$P(\cos v, \sin v)$", top-left
line-segment: (0, 0), (Px, Py), solid, red
text: 0.5 * Px, 0.5 * Py, "$1$", bottom-left
angle-arc: (0, 0), 0.2, 0, v, red
text: 0.25 * cos(v * 180 / pi / 2), 0.15 * sin(v * 180 / pi / 2), "$v$", top-right
axis: equal
grid: off
ticks: off
nocache:
fontsize: 28
:::

$$
\begin{align*}
x &= \cos v \\
\\
y &= \sin v
\end{align*}
$$



::::::


::::::{grid-item-card}
---
columns: 6
---
**Identiteter**
^^^

$$
\begin{align*}
\sin (180\degree - v) &= \sin v \\
\\
\cos (180\degree - v) &= -\cos v \\
\\
\sin(90\degree - v) &= \cos v \\
\\
\cos(90\degree - v) &= \sin v
\end{align*}
$$




::::::


::::::{grid-item-card}
---
columns: 6
---
**Arealsetningen**
^^^
:::{plot}
width: 50%
ticks: off
axis: off
axis: equal 
triangle: svs=(3, 45, 4), angles=all, color=blue, angle-color=red, angle-radius=80, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24, corner-offset=24
fontsize: 50
nocache:
:::

$$
\begin{align*}
T &= \dfrac{1}{2} \cdot b \cdot c \cdot \sin A && (\mathrm{hjørne \, A})\\
\\
T &= \dfrac{1}{2} \cdot a \cdot c \cdot \sin B && (\mathrm{hjørne \, B})\\
\\
T &= \dfrac{1}{2} \cdot a \cdot b \cdot \sin C && (\mathrm{hjørne \, C})
\end{align*}
$$


::::::


::::::{grid-item-card}
---
columns: 6
---
**Sinussetningen**
^^^
:::{plot}
width: 50%
ticks: off
axis: off
axis: equal 
triangle: svs=(3, 45, 4), angles=all, color=blue, angle-color=red, angle-radius=80, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24, corner-offset=24
fontsize: 50
nocache:
:::

$$
\dfrac{\sin A}{a} = \dfrac{\sin B}{b} = \dfrac{\sin C}{c}
$$




::::::

::::::{grid-item-card}
---
columns: 6
---
**Cosinussetningen**
^^^
:::{plot}
width: 50%
ticks: off
axis: off
axis: equal 
triangle: svs=(3, 45, 4), angles=all, color=blue, angle-color=red, angle-radius=80, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24, corner-offset=24
fontsize: 50
nocache:
:::

$$
\begin{align*}
a^2 &= b^2 + c^2 - 2\cdot b \cdot c \cdot \cos A \\
\\
b^2 &= a^2 + c^2 - 2\cdot a \cdot c \cdot \cos B \\
\\
c^2 &= a^2 + b^2 - 2\cdot a \cdot b \cdot \cos C
\end{align*}
$$




::::::


::::::{grid-item-card}
---
columns: 12
---
**Eksakte verdier**
^^^

:::{table}
---
transpose: true
---
labels: $v$, $\cos v$, $\sin v$
$0^{\circ}$, $1$, $0$
$30^{\circ}$, $\dfrac{\sqrt{3}}{2}$, $\dfrac{1}{2}$
$45^{\circ}$, $\dfrac{\sqrt{2}}{2}$, $\dfrac{\sqrt{2}}{2}$
$60^{\circ}$, $\dfrac{1}{2}$, $\dfrac{\sqrt{3}}{2}$
$90^{\circ}$, $0$, $1$
:::




::::::

::::::::