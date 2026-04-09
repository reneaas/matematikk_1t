# Oppgaver: Enhetssirkelen


:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{plot}
align: right
width: 100%
circle: (0, 0), 1, blue, solid
let: v = 36 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "({cos(v):.2f}, {sin(v):.2f})", top-right
angle-arc: (0, 0), 0.3, 0, 36, red
text: 0.35 * cos(v / 2), 0.25 * sin(v / 2), "$36^\circ$", top-right
fontsize: 28
grid: off
:::


Bruk figuren til høyre til å bestemme

* $\cos 36\degree$
* $\sin 36\degree$
* $\tan 36\degree$



:::{clear}
:::

::::{answer}
* $\cos 36 \degree = 0.81$
* $\sin 36 \degree = 0.59$
* $\tan 36 \degree = \dfrac{0.59}{0.81} = \dfrac{59}{81}$
::::

:::::::::::::



:::::::::::::{tab-item} b

:::{plot}
align: right
width: 100%
circle: (0, 0), 1, blue, solid
let: v = 72 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "({cos(v):.2f}, {sin(v):.2f})", top-right
angle-arc: (0, 0), 0.3, 0, 72, red
text: 0.35 * cos(v / 2), 0.25 * sin(v / 2), "$72^\circ$", top-right
fontsize: 28
grid: off
:::

Bruk figuren til å bestemme 

* $\cos 72\degree$
* $\sin 72\degree$
* $\tan 72\degree$



:::{clear}
:::

::::{answer}
* $\cos 72\degree = 0.31$
* $\sin 72\degree = 0.95$
* $\tan 72\degree = \dfrac{0.95}{0.31} = \dfrac{95}{31}$
::::


:::::::::::::



:::::::::::::{tab-item} c
:::{plot}
align: right
width: 100%
circle: (0, 0), 1, blue, solid
let: v = 140 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "({cos(v):.2f}, {sin(v):.2f})", top-left
angle-arc: (0, 0), 0.3, 0, 140, red
text: 0.35 * cos(v / 2), 0.25 * sin(v / 2), "$140^\circ$", top-right
fontsize: 28
grid: off
:::

Bruk figuren til å bestemme 

* $\cos 140\degree$
* $\sin 140\degree$
* $\tan 140\degree$



:::{clear}
:::

::::{answer}
* $\cos 140\degree = -0.77$
* $\sin 140\degree = 0.64$
* $\tan 140\degree = \dfrac{0.64}{-0.77} = -\dfrac{64}{77}$
::::


:::::::::::::




::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{plot}
align: right
width: 100%
circle: (0, 0), 1, blue, solid
let: v = 30 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "$P(x, y)$", top-right
angle-arc: (0, 0), 0.3, 0, 30, red
text: 0.35 * cos(v / 2), 0.2 * sin(v / 2), "$30^\circ$", top-right
fontsize: 28
grid: off
:::


Bestem koordinatene til punktet $P$ på enhetssirkelen vist til høyre.



:::{clear}
:::

::::{answer}
$$
P\left(\dfrac{\sqrt{3}}{2}, \dfrac{1}{2}\right)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
:::{plot}
align: right
width: 100%
circle: (0, 0), 1, blue, solid
let: v = 45 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "$P(x, y)$", top-right
angle-arc: (0, 0), 0.3, 0, 45, red
text: 0.35 * cos(v / 2), 0.2 * sin(v / 2), "$45^\circ$", top-right
fontsize: 28
grid: off
:::


Bestem koordinatene til punktet $P$ på enhetssirkelen vist til høyre.



:::{clear}
:::


::::{answer}
$$
P\left(\dfrac{\sqrt{2}}{2}, \dfrac{\sqrt{2}}{2}\right)
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
:::{plot}
align: right
width: 100%
circle: (0, 0), 1, blue, solid
let: v = 60 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "$P(x, y)$", top-right
angle-arc: (0, 0), 0.3, 0, 60, red
text: 0.35 * cos(v / 2), 0.2 * sin(v / 2), "$60^\circ$", top-right
fontsize: 28
grid: off
:::


Bestem koordinatene til punktet $P$ på enhetssirkelen vist til høyre.



:::{clear}
:::

::::{answer}
$$
P\left(\dfrac{1}{2}, \dfrac{\sqrt{3}}{2}\right)
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
:::{plot}
width: 60%
circle: (0, 0), 1, blue, solid
let: v = 120 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
let: ds = 0.15
line-segment: (cos(v), sin(v)), (0, sin(v)), red, dashed
line-segment: (0, sin(v) - ds), (-ds, sin(v) - ds), solid, gray
line-segment: (-ds, sin(v) - ds), (-ds, sin(v)), solid, gray
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "$P(x, y)$", top-left
angle-arc: (0, 0), 0.3, 0, 120, red
text: 0.35 * cos(v / 2), 0.2 * sin(v / 2), "$120^\circ$", top-right
fontsize: 28
grid: off
nocache:
ticks: off
:::

I enhetssirkelen ovenfor er det tegnet inn et punkt $P$ som ligger på sirkelen med en vinkel på $120\degree$ med $x$-aksen.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til punktet $P$ på enhetssirkelen vist ovenfor.

::::{answer}
$$
P\left(-\dfrac{1}{2}, \dfrac{\sqrt{3}}{2}\right)
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Bestem eksakte verdier for 

* $\cos 120\degree$
* $\sin 120\degree$
* $\tan 120\degree$


::::{answer}
$$
\cos 120\degree = -\dfrac{1}{2}
$$

$$
\sin 120 \degree = \dfrac{\sqrt{3}}{2}
$$

$$
\tan 120 \degree = -\sqrt{3}
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
:::{plot}
width: 60%
circle: (0, 0), 1, blue, solid
let: v = 135 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
let: ds = 0.15
line-segment: (cos(v), sin(v)), (0, sin(v)), red, dashed
line-segment: (0, sin(v) - ds), (-ds, sin(v) - ds), solid, gray
line-segment: (-ds, sin(v) - ds), (-ds, sin(v)), solid, gray
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "$P(x, y)$", top-left
angle-arc: (0, 0), 0.3, 0, 135, red
text: 0.35 * cos(v / 2), 0.25 * sin(v / 2), "$135^\circ$", top-right
fontsize: 28
grid: off
nocache:
ticks: off
:::

I enhetssirkelen ovenfor er det tegnet inn et punkt $P$ som ligger på sirkelen med en vinkel på $135\degree$ med $x$-aksen.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til punktet $P$.



::::{answer}
$$
P\left(-\dfrac{\sqrt{2}}{2}, \dfrac{\sqrt{2}}{2}\right)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem eksakte verdier for

* $\cos 135\degree$
* $\sin 135\degree$
* $\tan 135\degree$



::::{answer}
* $\cos 135\degree = -\dfrac{\sqrt{2}}{2}$
* $\sin 135\degree = \dfrac{\sqrt{2}}{2}$
* $\tan 135\degree = -1$
::::


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5
:::{plot}
width: 60%
circle: (0, 0), 1, blue, solid
let: v = 150 * pi / 180
line-segment: (0, 0), (cos(v), sin(v)), red
let: ds = 0.15
line-segment: (cos(v), sin(v)), (0, sin(v)), red, dashed
line-segment: (0, sin(v) - ds), (-ds, sin(v) - ds), solid, gray
line-segment: (-ds, sin(v) - ds), (-ds, sin(v)), solid, gray
point: (cos(v), sin(v))
axis: equal
text: cos(v), sin(v), "$P(x, y)$", top-left
angle-arc: (0, 0), 0.2, 0, 150, red
text: 0.25 * cos(v / 2), 0.15 * sin(v / 2), "$150^\circ$", top-right
fontsize: 28
grid: off
nocache:
ticks: off
:::

I enhetssirkelen ovenfor er det tegnet inn et punkt $P$ som ligger på sirkelen med en vinkel på $150\degree$ med $x$-aksen.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til punktet $P$. 


::::{answer}
$$
P\left(-\dfrac{\sqrt{3}}{2}, \dfrac{1}{2}\right)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem eksakte verdier for

* $\cos 150\degree$
* $\sin 150\degree$
* $\tan 150\degree$

::::{answer}
* $\cos 150\degree = -\dfrac{\sqrt{3}}{2}$
* $\sin 150\degree = \dfrac{1}{2}$
* $\tan 150\degree = -\dfrac{1}{\sqrt{3}} = -\dfrac{\sqrt{3}}{3}$
::::

:::::::::::::


::::::::::::::


:::::::::::::::





