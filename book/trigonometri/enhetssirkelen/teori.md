# Enhetssirkelen

:::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive hvordan $\cos v$ og $\sin v$ henger sammen med koordinatene til et punkt $P$ på enhetssirkelen.
* Kunne bruke enhetssirkelen til å bestemme $\cos v$ og $\sin v$ for vinkler $v \in [0, 360\degree\rangle$
* Kunne begrunne og bruke ulike trigonometriske identiteter til å bestemme ulike verdier for $\cos v$ og $\sin v$.
:::




Vi har sett at $\sin v$ og $\cos v$ er forholdstall i rettvinklede trekanter. Fordi alle rettvinklede trekanter med samme vinkel $v$ er formlike, vil $\sin v$ og $\cos v$ være lik uansett hvor stor eller liten trekanten er.

Men trekanter som *ikke* er rettvinklede kan jo også være formlike. Her skal vi utvide definisjonen av $\sin v$ og $\cos v$ slik at de fungerer for trekanter uavhengig om rettvinklede eller ikke.


## Enhetssirkelen 
Vi forestiller oss at vi tar en trekant og plasserer den i et koordinatsystem der det éne hjørnet alltid er plassert i origo, den ene kateten ligger alltid på $x$-aksen og hypotenusen har lengde $1$. Da vil det ene hjørnet alltid ligge på en sirkel med radius $1$ og sentrum i origo. Denne sirkelen kaller vi for **enhetssirkelen**. 



:::::::::::::::{summary} Enhetssirkelen
Enhetssirkelen er en sirkel med radius $1$ og sentrum i origo. 

Vi lar $v$ være vinkelen vi får dersom vi tegner en vinkelbue fra $x$-aksen til linjestykket $OP$. Da vil koordinatene til punktet $P$ være gitt ved $P(\cos v, \sin v)$.


::::{multi-plot2}
---
rows: 1
cols: 2
---
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

:::{plot}
circle: (0, 0), 1, blue, solid
let: v = 60
let: Px = cos(v * pi / 180)
let: Py = sin(v * pi / 180)
point: (Px, Py)
line-segment: (0, 0), (Px, Py), solid, red
text: Px, Py, "$P(\cos v, \sin v)$", top-right
text: 0.5 * Px, 0.5 * Py, "$1$", top-left
angle-arc: (0, 0), 0.2, 0, v, red
let: u = 30
text: 0.25 * cos(u / 180 * pi), 0.15 * sin(u / 180 * pi), "$v$", top-right
axis: equal
grid: off
ticks: off
nocache:
fontsize: 28
:::

::::


:::::::::::::::



---



:::::::::::::::{example} Eksempel 1

:::{plot}
width: 100%
align: right
circle: (0, 0), 1, blue, solid
let: v = 60
let: Px = cos(v * pi / 180)
let: Py = sin(v * pi / 180)
point: (Px, Py)
line-segment: (0, 0), (Px, Py), solid, red
text: Px, Py, "$P$", top-right
text: 0.5 * Px, 0.5 * Py, "$1$", top-left
angle-arc: (0, 0), 0.2, 0, v, red
let: u = 30
text: 0.25 * cos(u / 180 * pi), 0.15 * sin(u / 180 * pi), "$60^\circ$", top-right
axis: equal
grid: off
ticks: off
nocache:
fontsize: 28
line-segment: (cos(v * pi / 180), 0), (Px, Py), dashed, gray
let: ds = 0.1
line-segment: (cos(v * pi / 180) - ds, 0), (cos(v * pi / 180) - ds, ds), solid, gray
line-segment: (cos(v * pi / 180) - ds, ds), (cos(v * pi / 180), ds), solid, gray
:::



Enhetssirkelen vises til høyre med et linjestykke $OP$ tegnet inn som har vinkelen $60\degree$ med $x$-aksen.

Bestem koordinatene til punktet $P$. 


:::{clear}
:::

::::{solution}
---
dropdown: 0
---

:::{plot}
width: 100%
align: right
fontsize: 28
axis: equal
axis: off
let: v = 60 * pi / 180
let: Px = cos(v)
let: Py = sin(v)
triangle: points=((0, 0), (Px, 0), (Px, Py)), angles=(A, B), corner-labels=none, angle-radius=60, side-labels=(CA=exact), side-text=(AB="$x$", BC="$y$"), angle-labels=(A=exact)
point: (Px, Py)
text: Px, Py, "$P$", top-right
:::

Trekanten som er tegnet inn i enhetssirkelen er vist til høyre. Her kan vi se at 

$$
\cos 60\degree = \frac{x}{1} = x \qog \sin 60\degree = \frac{y}{1} = y
$$

Altså er koordinatene til punktet $P$ gitt ved $P(\cos 60\degree, \sin 60\degree)$. De eksakte verdiene er

$$
\cos 60\degree = \frac{1}{2} \qog \sin 60\degree = \frac{\sqrt{3}}{2}
$$

Ergo er punktet $P\left(\dfrac{1}{2}, \dfrac{\sqrt{3}}{2}\right)$.

::::


:::::::::::::::




---




:::::::::::::::{example} Eksempel 2
:::{plot}
width: 100%
align: right
circle: (0, 0), 1, blue, solid
let: v = 150
let: Px = cos(v * pi / 180)
let: Py = sin(v * pi / 180)
point: (Px, Py)
line-segment: (0, 0), (Px, Py), solid, red
text: Px, Py, "$P$", top-left
text: 0.5 * Px, 0.5 * Py, "$1$", top-right
angle-arc: (0, 0), 0.2, 0, v, red
angle-arc: (0, 0), 0.25, v, 180, red
let: u = 70
text: 0.25 * cos(u / 180 * pi), 0.15 * sin(u / 180 * pi), "$150^\circ$", top-right
axis: equal
grid: off
ticks: off
nocache:
fontsize: 28
line-segment: (cos(v * pi / 180), 0), (Px, Py), dashed, gray
let: ds = 0.1
line-segment: (cos(v * pi / 180) + ds, 0), (cos(v * pi / 180) + ds, ds), solid, gray
line-segment: (cos(v * pi / 180) + ds, ds), (cos(v * pi / 180), ds), solid, gray
:::


I enhetssirkelen til høyre vises et linjestykke $OP$ som har vinkelen $150\degree$ med $x$-aksen.

Bestem $\cos 150\degree$ og $\sin 150\degree$.



:::{clear}
:::


::::{solution}
---
dropdown: 0
---
:::{plot}
width: 100%
align: right
fontsize: 28
axis: equal
axis: off
let: v = 150 * pi / 180
let: Px = cos(v)
let: Py = sin(v)
triangle: points=((0, 0), (Px, 0), (Px, Py)), angles=(A, B), corner-labels=none, angle-radius=60, side-labels=(CA=exact), side-text=(AB="$x$", BC="$y$"), angle-labels=(A=exact)
point: (Px, Py)
text: Px, Py, "$P$", top-left
:::

Den rettvinklede trekanten som er tegnet inn i enhetssirkelen har en vinkel på 

$$
v = 180\degree - 150\degree = 30\degree
$$

Derfor vil sidelengdene i den rettvinklede trekanten være gitt ved 

$$
\cos 30\degree = \frac{x}{1} = x \qog \sin 30\degree = \frac{y}{1} = y
$$

Punktet $P$ på enhetssirkelen vil være gitt ved $P(\cos 150\degree, \sin 150\degree)$ per definisjon. Vi vet at $x$-koordinaten er negativ, slik at

$$
\cos 150\degree = -\cos 30\degree = -\frac{\sqrt{3}}{2}
$$

Videre er $y$-koordinaten positiv, slik at

$$
\sin 150\degree = \sin 30\degree = \frac{1}{2}
$$


::::

:::::::::::::::






## Trigonometriske identiteter
I mange sammenhenger kan vi bruke trigonometriske identiteter til å bestemme verdier for $\sin v$ og $\cos v$ gitt at vi kjenner til noen andre verdier for $\sin v$ og $\cos v$. Vi skal se på noen av de mest grunnleggende identitetene her.

### Pytagoras' identitet

Pytagoras' identitet har fått navnet sitt fordi den er en direkte konsekvens av Pytagoras' setning.


:::::::::::::::{summary} Pytagoras' identitet

:::{plot}
width: 100%
align: right
circle: (0, 0), 1, blue, solid
let: v = 60
let: Px = cos(v * pi / 180)
let: Py = sin(v * pi / 180)
point: (Px, Py)
line-segment: (0, 0), (Px, Py), solid, red
text: Px, Py, "$P(\cos v, \sin v)$", top-right
text: 0.5 * Px, 0.5 * Py, "$1$", top-left
angle-arc: (0, 0), 0.2, 0, v, red
let: u = 30
text: 0.25 * cos(u / 180 * pi), 0.15 * sin(u / 180 * pi), "$v$", top-right
axis: equal
grid: off
ticks: off
nocache:
fontsize: 28
line-segment: (cos(v * pi / 180), 0), (Px, Py), dashed, red
let: ds = 0.1
line-segment: (cos(v * pi / 180) - ds, 0), (cos(v * pi / 180) - ds, ds), solid, gray
line-segment: (cos(v * pi / 180) - ds, ds), (cos(v * pi / 180), ds), solid, gray
:::



For alle vinkler $v$, så gjelder

$$
\boxed{(\cos v)^2 + (\sin v)^2 = 1}
$$


:::{clear}
:::

> Vi skriver ofte at $\sin^2 v = (\sin v)^2$ og $\cos^2 v = (\cos v)^2$ for å spare litt plass.

:::::::::::::::



---



:::::::::::::::{example} Eksempel 3
For en vinkel $v$, så er $\sin v = \dfrac{2}{3}$.

Bestem en eksakt verdi for $\cos v$.


::::{solution}
---
dropdown: 0
---
For alle vinkler, så gjelder Pytagoras' identitet

$$
(\cos v)^2 + (\sin v)^2 = 1
$$

Vi vet at $\sin v = \dfrac{2}{3}$, slik at

$$
(\cos v)^2 + \left(\frac{2}{3}\right)^2 = 1
$$

$$
(\cos v)^2 + \frac{4}{9} = 1
$$

$$
(\cos v)^2 = 1 - \frac{4}{9} = \frac{5}{9}
$$

$$
\cos v = \pm \sqrt{\frac{5}{9}} = \pm \frac{\sqrt{5}}{3}
$$

::::


:::::::::::::::




### Komplementvinkler


:::::::::::::::{summary} Sinus og cosinus til komplementvinkler

:::{plot}
axis: off
axis: equal
fontsize: 32
width: 100%
align: right
let: v = 30 * pi / 180
let: Px = cos(v)
let: Py = sin(v)
triangle: points=((0, 0), (Px, 0), (Px, Py)), angles=(A, B, C), corner-labels=none, angle-radius=80, side-labels=(CA=exact), side-text=(AB="$x$", BC="$y$"), angle-text=(A="$v$", C="$90^\circ - v$"), angle-offset=24, label-offset=24
:::


For alle vinkler $v$, så gjelder følgende to identiteter

$$
\boxed{
\begin{align*}
\\
\sin(90\degree - v) &= \cos v \\
\\
\cos(90\degree - v) &= \sin v \\
\\
\end{align*}
}
$$
:::::::::::::::


<!-- 
### Supplementvinkler




:::::::::::::::{summary} Sinus til supplementvinkler

:::::::::::::::




:::::::::::::::{summary} Cosinus til supplementvinkler

::::::::::::::: -->