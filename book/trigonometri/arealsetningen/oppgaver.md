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
triangle: svs=(3, 30, 2), angles=A, color=blue, angle-color=red, angle-radius=60, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric), label-offset=24, angle-offset=24
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


::::{solution}
$$
T = \dfrac{1}{2} \cdot 3 \cdot 2 \cdot \sin(30\degree) = \dfrac{1}{3} \cdot 3 \cdot 2 \cdot \dfrac{1}{2} = \dfrac{3}{2}.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: svs=(2, 45, 5), angles=A, color=blue, angle-color=red, angle-radius=60, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric), label-offset=24, angle-offset=24
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

::::{solution}
$$
T = \dfrac{1}{2} \cdot 2 \cdot 5 \cdot \sin(45\degree) = \dfrac{1}{2} \cdot 2 \cdot 5 \cdot \dfrac{\sqrt{2}}{2} = \dfrac{5\sqrt{2}}{2}.
$$
::::

:::::::::::::



:::::::::::::{tab-item} c
:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: svs=(5, 60, 3), angles=A, color=blue, angle-color=red, angle-radius=60, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric), label-offset=24, angle-offset=24
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



::::{solution}
$$
T = \dfrac{1}{2} \cdot 5 \cdot 3 \cdot \sin (60\degree) = \dfrac{1}{2} \cdot 5 \cdot 3 \cdot \dfrac{\sqrt{3}}{2} = \dfrac{15\sqrt{3}}{4}.
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
triangle: svs=(2, 53, 3), angles=all, color=blue, angle-color=red, angle-radius=70, side-labels=(AB=numeric, CA=numeric, BC=numeric), angle-labels=(A=numeric, B=numeric, C=numeric), label-offset=24, angle-offset=40
fontsize: 30
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


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_2/a.png
---
class: no-click, adaptive-figure
width: 60%
---
:::
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem arealet av trekanten ut ifra hjørne $B$.


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_2/b.png
---
class: no-click, adaptive-figure
width: 60%
---
:::
::::

:::::::::::::



:::::::::::::{tab-item} c
Bestem arealet av trekanten ut ifra hjørne $C$.

::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_2/c.png
---
class: no-click, adaptive-figure
width: 60%
---
:::
::::

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


::::{answer}
$$
12
$$
::::


::::{solution}
$$
T = \dfrac{1}{2}\cdot AB \cdot AC \cdot \sin(\angle A) = \dfrac{1}{2} \cdot 8 \cdot 6 \cdot \sin(30\degree) = 12.
$$
::::



:::::::::::::



:::::::::::::{tab-item} b
I en trekant $\triangle ABC$ er $AB = 5$, $BC = 7$ og $\angle B = 45\degree$.

Bestem arealet av trekanten.


::::{answer}
$$
\dfrac{35\sqrt{2}}{4}
$$
::::


::::{solution}
$$
\begin{align*}
T &= \dfrac{1}{2} \cdot AB \cdot BC \cdot \sin(\angle B) \\
\\
&= \dfrac{1}{2} \cdot 5 \cdot 7 \cdot \sin(45\degree) \\
\\
&= \dfrac{1}{2} \cdot 5 \cdot 7 \cdot \dfrac{\sqrt{2}}{2} \\
\\
&= \dfrac{35\sqrt{2}}{4}.
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
I en trekant $\triangle ABC$ er $BC = 10$ og $AC = 8$ og $\angle C = 120\degree$.

Bestem arealet av trekanten.


::::{answer}
$$
20 \sqrt{3}
$$
::::


::::{solution}
$$
\begin{align*}
T &= \dfrac{1}{2} \cdot BC \cdot AC \cdot \sin(\angle C) \\
\\
&= \dfrac{1}{2} \cdot 10 \cdot 8 \cdot \sin(120\degree) \\
\\
&= \dfrac{1}{2} \cdot 10 \cdot 8 \cdot \dfrac{\sqrt{3}}{2} \\
\\
&= 20 \sqrt{3}.
\end{align*}
$$
::::


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
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0
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
line-segment: (Bx - ds, By), (Bx - ds, By + ds), solid, gray
line-segment: (Bx - ds, By + ds), (Bx, By + ds), solid, gray
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


::::{solution}
Vi regner ut arealet av $\triangle ABD$ først:

$$
\begin{align*}
T_{\triangle ABD} &= \dfrac{1}{2} \cdot 6 \cdot 6 \cdot \sin 150\degree \\
\\
&= \dfrac{1}{2} \cdot 6 \cdot 6 \cdot \dfrac{1}{2} \\
\\
&= 9.
\end{align*}
$$

Sidelengden $BC$ vil være det samme som høyden i $\triangle ABD$. Derfor har vi at

$$
BC = 6 \cdot \sin(150\degree) = 3.
$$

Sidelengden $CD$ vil være

$$
CD = 6 + 6 \cdot \cos(180\degree - 150\degree) = 6 + 6 \cdot \cos(30\degree) = 6 + 6 \cdot \dfrac{\sqrt{3}}{2} = 6 + 3\sqrt{3}.
$$

Arealet av $\triangle BCD$ vil være

$$
\begin{align*}
T_{\triangle BCD} &= \dfrac{1}{2} \cdot BC \cdot CD \\
\\
&= \dfrac{1}{2} \cdot 3 \cdot (6 + 3\sqrt{3}) \\
\\
&= \dfrac{18 + 9 \sqrt{3}}{2}
\end{align*}
$$

Det samlede arealet av firkanten er da


$$
\begin{align*}
T_{ABCD} &= T_{\triangle ABD} + T_{\triangle BCD} \\
\\
&= 9 + \dfrac{18 + 9 \sqrt{3}}{2} \\
\\
&= 9 + 9 + \dfrac{9 \sqrt{3}}{2} \\
\\
&= 18 + \dfrac{9 \sqrt{3}}{2}.
\end{align*}
$$
::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5

:::{cas-popup}
---
layout: sidebar
---
:::


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
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0
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

:::{clear}
:::

::::{answer}
$$
\dfrac{175 + 75\sqrt{3}}{2}~\mathrm{m^2}
$$
::::


::::{solution}
Vi trekker en diagonal $BD$ slik at vi deler opp firkanten i to trekanter $\triangle ABD$ og $\triangle BCD$.

Trekanten $\triangle ABD$ er en rettvinklet og likebeint trekant. Fra det kan vi hente ut at
1. De andre vinklene i trekanten er $45 \degree$. Altså er $\angle ABD = \angle BDA = 45\degree$.
2. Arealet blir bare $\dfrac{1}{2} AB \cdot AD$.


Altså har vi at

$$
T_{\triangle ABD} = \dfrac{1}{2} \cdot 10 \cdot 10 = 50.
$$


La oss nå fokusere på trekanten $\triangle BCD$. Vi vet at 

$$
\angle B = \angle ABD + \angle DBC
$$

Vi trenger $\angle DBC$ som vi kan finne ved å sette inn de andre kjente vinklene:

$$
120 \degree = 45\degree + \angle DBC  \liff \angle DBC = 75\degree.
$$

Videre kan vi finne $BD$ ved hjelp av Pytagoras' setning:

$$
BD^2 = 10^2 + 10^2 = 200 \liff BD = 10 \sqrt{2}.
$$

Nå kan vi bruke arealsetningen for å finne arealet av $\triangle BCD$:

:::{figure} ./figurer/oppgaver/oppgave_5/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Altså kan vi skrive arealet til $\triangle BCD$ som

$$
T_{\triangle BCD} = -\dfrac{1}{2}\left(-75\sqrt{3} - 75\right) = \dfrac{75\sqrt{3} + 75}{2}.
$$

Det samlede arealet av tomten er da

$$
\begin{align*}
T_{ABCD} &= T_{\triangle ABD} + T_{\triangle BCD} \\
\\
&= 50 + \dfrac{75\sqrt{3} + 75}{2} \\
\\
&= \dfrac{100 + 75\sqrt{3} + 75}{2} \\
\\
&= \dfrac{175 + 75\sqrt{3}}{2}
\end{align*}
$$

der arealet er i $\mathrm{m^2}$ siden alle lengdene i figuren er i meter.

::::



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


::::{answer}
$$
T_{\triangle SAB} = \sqrt{3}
$$
::::


::::{solution}
Siden radius i sirkelen er $2$, så vet vi at 

$$
SA = SB = 2
$$

Da blir arealet av $\triangle SAB$:

$$
\begin{align*}
T_{\triangle SAB} &= \dfrac{1}{2} \cdot SA \cdot SB \cdot \sin(120\degree) \\
\\
&= \dfrac{1}{2} \cdot 2 \cdot 2 \cdot \dfrac{\sqrt{3}}{2} \\
\\
&= \sqrt{3}.
\end{align*}
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem arealet av $\triangle CAB$. 


::::{answer}
$$
T_{\triangle CAB} = 2\sqrt{3}
$$

::::


::::{solution}
Trekant $\triangle CAB$ er samme høyde som $\triangle SAB$, men dobbelt så stor grunnlinje siden $CA = 2 \cdot SA$. Derfor vil arealet av trekanten være

$$
T_{\triangle CAB} = 2 \cdot T_{\triangle SAB} = 2 \cdot \sqrt{3} = 2\sqrt{3}.
$$
::::

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

::::{answer}
$$
CD = \sqrt{3} \cdot a
$$
::::


::::{solution}
Vi bruker Pytagoras' setning på trekant $\triangle ACD$:

$$
AC^2 = AD^2 + CD^2 
$$

$$
(2a)^2 = a^2 + CD^2
$$

$$
4a^2 = a^2 + CD^2
$$

$$
CD^2 = 3a^2
$$

$$
CD = \sqrt{3} \cdot a.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem en eksakt verdi for arealet av firkanten.

::::{answer}
$$
\dfrac{\sqrt{3} + 3}{2} \cdot a^2
$$
::::


::::{solution}
Vi kan regne ut arealet av $\triangle ACD$ direkte siden vi kan tenke på $AD$ som grunnlinje og $CD$ som høyde:

$$
T_{\triangle ACD} = \dfrac{1}{2} \cdot AD \cdot CD = \dfrac{1}{2} \cdot a \cdot \sqrt{3} \cdot a = \dfrac{\sqrt{3}}{2} \cdot a^2.
$$

Så snur vi oss til trekant $\triangle ABC$. Vinkelen i hjørne $C$ er $\angle C = 150\degree$. Siden trekant $\triangle ACD$ er en rettvinklet trekant der den korteste kateten er halvparten av hypotenusen, så følger det at

$$
\angle ACD = 30 \degree
$$

Så da kan vi bestemme $\angle BCA$ i trekant $\triangle ABC$ ved å bruke at 

$$
\angle C = \angle ACD + \angle BCA 
$$

$$
150 \degree = 30 \degree + \angle BCA \liff \angle BCA = 120\degree.
$$

Nå har har vi nok informasjon til å bestemme arealet av $\triangle ABC$:

$$
\begin{align*}
T_{\triangle ABC} &= \dfrac{1}{2} \cdot AC \cdot BC \cdot \sin(\angle BCA) \\
\\
&= \dfrac{1}{2} \cdot 2a \cdot \sqrt{3} \cdot a \cdot \sin(120\degree) \\
\\
&= \dfrac{1}{2} \cdot 2a \cdot \sqrt{3} \cdot a \cdot \dfrac{\sqrt{3}}{2} \\
\\
&= \dfrac{3}{2} \cdot a^2.
\end{align*}
$$

Det samlede arealet av firkanten er da

$$
\begin{align*}
T_{ABCD} &= T_{\triangle ACD} + T_{\triangle ABC} \\
\\
&= \dfrac{\sqrt{3}}{2} \cdot a^2 + \dfrac{3}{2} \cdot a^2 \\
\\
&= \dfrac{\sqrt{3} + 3}{2} \cdot a^2.
\end{align*}
$$
::::


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


::::{solution}
Vinkelen $v$ er én av de 6 like store sentralvinklene i sirkelen. De seks vinklene må samme summeres til $360\degree$ siden dette er antall grader i en sirkel. Dermed har vi:

$$
6v = 360\degree \liff v = \dfrac{360\degree}{6} = 60\degree.
$$
::::



:::::::::::::


:::::::::::::{tab-item} b
Bestem en eksakt verdi for arealet til sekskanten.

::::{answer}
$$
T = 6 \sqrt{3}.
$$
::::


::::{solution}
Arealet av én trekant $T_1$ i sekskanten kan vi finne ved arealsetningen. Vi vet at sidelengdene som spenner ut vinkelen $v$ er like radius i sirkelen som er lik $2$. Dermed får vi:

$$
T_1 = \dfrac{1}{2} \cdot 2 \cdot 2 \cdot \sin 60\degree = 2 \cdot \dfrac{\sqrt{3}}{2} = \sqrt{3}.
$$

Sekskanten består av 6 slike trekanter, så arealet av sekskanten blir

$$
T = 6 \cdot T_1 = 6 \cdot \sqrt{3} = 6\sqrt{3}.
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


::::{solution}
Vinkelen $v$ er én av de 12 like store sentralvinklene i sirkelen. De tolv vinklene må samme summeres til $360\degree$ siden dette er antall grader i en sirkel. Dermed har vi:

$$
12v = 360\degree \liff v = \dfrac{360\degree}{12} = 30\degree.
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


::::{solution}
Vi vet at arealet av $12$-kanten er $120$. Da vil én av de tolv trekantene har arealet

$$
T_1 = \dfrac{120}{12} = 10.
$$

Videre vil arealsetningen gi oss at

$$
T_1 = \dfrac{1}{2}r^2 \cdot \sin(30\degree) = \dfrac{1}{2}r^2 \cdot \dfrac{1}{2} = \dfrac{r^2}{4}
$$

der $r$ er radius i sirkelen. Vi setter de to uttrykkene lik hverandre som gir likningen

$$
\dfrac{r^2}{4} = 10 \liff r^2 = 40 \liff r = 2 \cdot \sqrt{10}.
$$

Diameteren $d$ i sirkelen er det dobbelte av radius, så vi har at

$$
d = 2r = 4 \cdot \sqrt{10}.
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
Bestem en funksjon $T(N)$ for arealet til en slik $N$-kant.


::::{answer}
$$
T(N) = \dfrac{N}{2} \cdot \sin \left( \dfrac{360\degree}{N} \right).
$$
::::


::::{solution}
Sentralvinkelen $v$ utgjør én av $N$ like stor vinkler i sirkelen som tilsammen må summeres til $360\degree$. Dermed har vi at

$$
N\cdot v = 360\degree \liff v = \dfrac{360\degree}{N}.
$$

Arealet $T_1$ av én enkelt trekant vil da være

$$
T_1 = \dfrac{1}{2} \cdot 1^2 \cdot \sin \left( \dfrac{360\degree}{N} \right) = \dfrac{1}{2} \cdot \sin \left( \dfrac{360\degree}{N} \right).
$$

Vi har $N$ slike trekanter i $N$-kanten får vi

$$
T(N) = N \cdot T_1 = N \cdot \dfrac{1}{2} \cdot \sin \left( \dfrac{360\degree}{N} \right) = \dfrac{N}{2} \cdot \sin \left( \dfrac{360\degree}{N} \right).
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


::::{answer}
$$
T(108) \approx 3.13982
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_10/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

som gir oss en grei tilnærming til $\pi$.
::::


:::::::::::::


::::::::::::::


:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 11
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Gitt en trekant $ABC$ der $AB = 3 \sqrt{2}$, $AC = 8$ og $\angle A = 45\degree$.

Bestem arealet av trekanten.


::::{answer}
$$
T_{\triangle ABC} = 12.
$$
::::


::::{solution}
Arealet av trekanten er

$$
\begin{align*}
T_{\triangle ABC} &= \dfrac{1}{2} \cdot AB \cdot AC \cdot \sin(\angle A) \\
\\
&= \dfrac{1}{2} \cdot 3 \sqrt{2} \cdot 8 \cdot \sin(45\degree) \\
\\
&= \dfrac{1}{2} \cdot 3 \sqrt{2} \cdot 8 \cdot \dfrac{\sqrt{2}}{2} \\
\\
&= 12.
\end{align*}
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Gitt en trekant PQR der $PQ = 3 \sqrt{2}$, $PR = 8$ og $\angle P = 140\degree$.

Avgjør hvilke av trekantene $ABC$ og $PQR$ som har størst areal.


::::{answer}
Trekant $ABC$ har størst areal.
::::

::::{solution}
Arealet av trekant $PQR$ vil være gitt ved

$$
T_{\triangle PQR} = \dfrac{1}{2} PQ \cdot PR \cdot \sin \angle P
$$

Siden $PQ = AB$ og $PR = AC$, så kan vi skrive arealet av trekant $PQR$ som

$$
T_{\triangle PQR} = \dfrac{1}{2} \cdot AB \cdot AC \cdot \sin \angle P
$$

Det som bestemme hvilken trekant som har størst areal, vil være sinusverdien. Vi har at

$$
\sin 140\degree = \sin (180\degree - 140\degree) = \sin 40\degree < \sin 45\degree.
$$

Altså må trekant $ABC$ ha størst areal.
::::

:::::::::::::


::::::::::::::
:::::::::::::::

