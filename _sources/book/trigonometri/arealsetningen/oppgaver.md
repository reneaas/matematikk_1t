# Oppgaver: Arealsetningen


:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: svs=(3, 30, 2), angles=A, color=blue, angle-color=red, angle-radius=25, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric)
fontsize: 30
:::



Bestem arealet av trekanten.


:::{clear}
:::


::::{answer}
$$
T = \dfrac{3}{2}.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: svs=(2, 45, 5), angles=A, color=blue, angle-color=red, angle-radius=25, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric)
fontsize: 30
:::

Bestem arealet av trekanten.



:::{clear}
:::


::::{answer}
$$
T = \dfrac{5\sqrt{2}}{2}.
$$
::::

:::::::::::::



:::::::::::::{tab-item} c
:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: svs=(5, 60, 3), angles=A, color=blue, angle-color=red, angle-radius=25, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric)
fontsize: 30
:::

Bestem arealet av trekanten.



:::{clear}
:::

::::{answer}
$$
T = \dfrac{15\sqrt{3}}{4}.
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 2
---
aids: true
---

:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: svs=(2, 53, 3), angles=all, color=blue, angle-color=red, angle-radius=20, side-labels=(AB=numeric, CA=numeric, BC=numeric), angle-labels=(A=numeric, B=numeric, C=numeric)
fontsize: 30
nocache:
:::

:::{cas-popup}
:::


I figuren til høyre vises en trekant $\triangle ABC$.


:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet av trekanten ut ifra hjørne $A$.


:::::::::::::



:::::::::::::{tab-item} b
Bestem arealet av trekanten ut ifra hjørne $B$.


:::::::::::::



:::::::::::::{tab-item} c
Bestem arealet av trekanten ut ifra hjørne $C$.



:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I en trekant $\triangle ABC$ er $AB = 8$, $AC = 6$ og $\angle A = 30\degree$.

Bestem arealet av trekanten.
:::::::::::::



:::::::::::::{tab-item} b
I en trekant $\triangle ABC$ er $AB = 5$, $BC = 7$ og $\angle B = 45\degree$.

Bestem arealet av trekanten.
:::::::::::::


:::::::::::::{tab-item} c
I en trekant $\triangle ABC$ er $BC = 10$ og $AC = 8$ og $\angle C = 120\degree$.

Bestem arealet av trekanten.
:::::::::::::



::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4

:::{plot}
axis: equal
align: right
axis: off
width: 100%
let: Ax = 0
let: Ay = 0
let: v = 150 * pi / 180
let: Bx = 6
let: By = 0
let: Cx = Bx
let: Cy = 6 * sin(v)
let: Dx = 6 * cos(v)
let: Dy = 6 * sin(v)
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
line-segment: (Bx, By), (Dx, Dy), dashed, gray
let: ds = 0.5
line-segment: (Cx - ds, Cy), (Cx - ds, Cy - ds), solid, gray
line-segment: (Cx - ds, Cy - ds), (Cx, Cy - ds), solid, gray
angle-arc: (Ax, Ay), 0.5, 0, 150
text: 1.2 * cos(pi / 6), 1.2 * sin(pi / 6), "$150^\circ$", center-center
text: 0.5 * (Ax + Bx), 0, "$6$", bottom-center
text: 0.5 * (Ax + Dx), 0.5 * (Ay + Dy), "$6$", bottom-left
fontsize: 30
:::


I figuren til høyre vises en firkant $ABCD$.


Bestem arealet av firkanten.



:::{clear}
:::

::::{answer}
$$
T = 18 + \dfrac{9 \sqrt{3}}{2}
$$
::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5

:::{plot}
nocache:
fontsize: 30
width: 100%
align: right
axis: off
axis: equal
let: Ax = 0
let: Ay = 0
let: Bx = 10
let: By = 0
let: Cx = Bx + 15 * cos(pi/3)
let: Cy = By + 15 * sin(pi/3)
let: Dx = 0
let: Dy = 10
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
angle-arc: (Bx, By), 2, 180, 60
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
let: v = 120 * pi/180
let: r = 2.8
text: Bx + r * cos(v), By + r * sin(v), "$120^\circ$", center-center
text: 0.5 * (Ax + Bx), 0.5 * (Ay + By), "$10$ m", bottom-center
text: 0.5 * (Bx + Cx), 0.5 * (By + Cy), "$15$ m", bottom-right
text: 0, 0.5 * (Ay + Dy), "$10$ m", center-left
let: ds = 1.5
line-segment: (Ax + ds, Ay), (Ax + ds, Ay + ds), solid, gray
line-segment: (Ax + ds, Ay + ds), (Ax, Ay + ds), solid, gray
:::


I figuren til høyre vises en skisse av en boligtomt.


Bestem arealet av tomten.

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 6
Nedenfor vises en sirkel med radius $2$. Punktet $S$ er sentrum i sirkelen. Trekanten $\triangle CAB$ er bygget opp av to mindre trekanter $\triangle SAB$ og $\triangle SBC$. 


:::{plot}
fontsize: 26
axis: off
axis: equal
width: 50%
circle: (0, 0), 2, blue
let: Sx = 0
let: Sy = 0
let: Ax = 2
let: Ay = 0
let: Bx = 2 * cos(2*pi / 3)
let: By = 2 * sin(2*pi / 3)
let: Cx = -2
let: Cy = 0
point: (Sx, Sy)
point: (Ax, Ay)
point: (Bx, By)
point: (Cx, Cy)
let: ds = 0.1
text: Sx, Sy - ds, "$S$", bottom-center
text: Ax + ds, Ay, "$A$", center-right
text: Bx, By, "$B$", top-left
text: Cx - ds, Cy, "$C$", center-left
line-segment: (Sx, Sy), (Ax, Ay), solid, black
line-segment: (Sx, Sy), (Bx, By), solid, black
line-segment: (Sx, Sy), (Cx, Cy), solid, black
line-segment: (Ax, Ay), (Bx, By), solid, black
line-segment: (Bx, By), (Cx, Cy), solid, black
let: r = 0.3
angle-arc: (Sx, Sy), r, 0, 120
text: 1.5 * r * cos(pi/3), 1.5 * r * sin(pi/3), "$120^\circ$", center-center
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet av $\triangle SAB$.


:::::::::::::



:::::::::::::{tab-item} b
Bestem arealet av $\triangle CAB$. 


:::::::::::::



::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 7
I figuren nedenfor vises en firkant $ABCD$. I firkanten er $\angle C = 150\degree$. 

:::{plot}
nocache:
width: 60%
figsize: (5, 5)
axis: off
axis: equal
let: a = 5
let: Ax = 0
let: Ay = 0
let: Bx = sqrt(13) * a
let: By = 0
let: Cx = Ax + 2 * a * cos(pi/6)
let: Cy = Ay + 2 * a * sin(pi/6)
let: Dx = 0
let: Dy = a
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
line-segment: (Ax, Ay), (Cx, Cy), dashed, gray
let: ds = 1
line-segment: (Dx + ds, Dy), (Dx + ds, Dy - ds), solid, gray
line-segment: (Dx + ds, Dy - ds), (Dx, Dy - ds), solid, gray
text: -0.2, 0.5 * (Ay + Dy), "$a$", center-left
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "$2a$", top-left
text: 0.5 * (Bx + Cx), 0.5 * (By + Cy), "$\sqrt{3} a$", top-right
let: r = 1.2
angle-arc: (Cx, Cy), r, 180, 180 + 150
text: Cx, Cy - 1.8 * r, "$150^\circ$", center-center
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en eksakt verdi for $CD$.


:::::::::::::


:::::::::::::{tab-item} b
Bestem en eksakt verdi for arealet av firkanten.


:::::::::::::


::::::::::::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 8
:::{plot}
width: 100%
align: right
axis: off
axis: equal
circle: (0, 0), 6, black
let: N = 6
repeat: n=0..N-1; line-segment: (6 * cos(2 * n * pi / N), 6 * sin(2 * n * pi / N)), (6 * cos(2 * (n + 1) * pi / N), 6 * sin(2 * (n + 1) * pi / N)), solid, blue
repeat: n=0..N-1; line-segment: (0, 0), (6 * cos(2 * n * pi / N), 6 * sin(2 * n * pi / N)), dashed, gray
let: r = 1.2
angle-arc: (0, 0), r, 0, 360 / N
text: 1.5 * r * cos(pi / 6), 1.5 * r * sin(pi / 6), "$v$", center-center
fontsize: 30
:::

I figuren til høyre vises en sirkel med radius $2$. En sekskant der alle sidene er like lange er innskrevet i sirkelen.



:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem vinkelen $v$.


::::{answer}
$$
v = 60 \degree.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem en eksakt verdi for arealet til sekskanten.

::::{answer}
$$
T = 24 \sqrt{3}.
$$
::::

:::::::::::::



::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 9
:::{plot}
width: 100%
align: right
axis: off
axis: equal
circle: (0, 0), 6, black
let: N = 12
repeat: n=0..N-1; line-segment: (6 * cos(2 * n * pi / N), 6 * sin(2 * n * pi / N)), (6 * cos(2 * (n + 1) * pi / N), 6 * sin(2 * (n + 1) * pi / N)), solid, blue
repeat: n=0..N-1; line-segment: (0, 0), (6 * cos(2 * n * pi / N), 6 * sin(2 * n * pi / N)), dashed, gray
let: r = 2
angle-arc: (0, 0), r, 0, 360 / N
text: 1.5 * r * cos(pi / 12), 1.5 * r * sin(pi / 12), "$v$", center-center
fontsize: 30
:::

En 12-kant der alle sidene er like lange er innskrevet i en sirkel.

Arealet av 12-kanten er $120$.



:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem vinkelen $v$.


::::{answer}
$$
v = 30 \degree.
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
Bestem en eksakt verdi for diameteren til sirkelen.


::::{answer}
$$
4 \cdot \sqrt{10}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 10

:::{interactive-graph} 
width: 40%
align: right
interactive-var: N, 3, 108, 106
interactive-var-start: 3
circle: (0, 0), 1, black
repeat: n=0..N-1; line-segment: (cos(2 * n * pi / N), sin(2 * n * pi / N)), (cos(2 * (n + 1) * pi / N), sin(2 * (n + 1) * pi / N)), solid, blue
repeat: n=0..N-1; line-segment: (0, 0), (cos(2 * n * pi / N), sin(2 * n * pi / N)), dashed, gray
axis: equal
axis: off
:::

En regulær $N$-kant innskrevet i en sirkel med radius $1$ er vist i figuren til høyre, der du kan endre på verdien til $N$.



:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en funksjon $T(n)$ for arealet til en slik $N$-kant.


::::{answer}
$$
T(n) = \dfrac{n}{2} \cdot \sin \left( \dfrac{360\degree}{n} \right).
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

Arkimedes levde ca. 250 år før vår tidsregning. Han beregnet arealet av innskrevet $108$-kant.

Bestem arealet Arkimedes fant. 
:::::::::::::


::::::::::::::


:::::::::::::::

