# Eksempelsett


## Oppgaver 
> Oppgavesettet nedenfor vil likne på en eksamen, med unntak av at oppgavesettet ikke tar for seg trigonometri. Oppgavesettet er delt inn i to deler:
> 1. Del 1: Uten hjelpemidler (3 timer)
> 2. Del 2: Med hjelpemidler (2 timer)


### Del 1: Uten hjelpemidler


:::::::::::::::{exercise} Oppgave 1 (6 poeng)

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 3x - 4
$$

Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.


::::{answer}
$(-1, 0)$ og $(4, 0)$.
::::

:::::::::::::


:::::::::::::{tab-item} b
En andregradsfunksjon $g$ er gitt ved

$$
g(x) = 2(x - 1)^2 - 8
$$

Bestem nullpunktene til $g$.

::::{answer}
$$
x = -1 \or x = 3
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
En andregradsfunksjon $h$ er gitt ved

$$
h(x) = \dfrac{1}{2}(x + 4)(x - 3)
$$

Bestem koordinatene til bunnpunktet til $h$.

::::{answer}
$$
\left(-\dfrac{1}{2}, -\dfrac{49}{8}\right)
$$
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2 (2 poeng)
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{16x + 4}{4x - 8}
$$

Bestem likningene til asymptotene til $f$.

::::{answer}
* Horisontal asymptote: $y = 4$
* Vertikal asymptote: $x = 2$
::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 3 (2 poeng)
En likning er gitt ved

$$
a(x + 1)^2 + b = -2(x + 4)(x - c)
$$

Bestem $a$, $b$ og $c$ slik at likningen er en identitet.


::::{answer}
$$
a = -2 \and b = 18 \and c = 2
$$
::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4 (4 poeng)
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
x^3 - 3x^2 - x + 3 = 0
$$

::::{answer}
$$
x = -1 \or x = 1 \or x = 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 - x + 3
$$

Hvilken av figurene nedenfor viser grafen til $f$?

Husk å begrunne svaret ditt.

::::{multi-plot2}
---
rows: 2
cols: 2
ticks: off
fontsize: 26
---
:::{plot}
width: 100%
function: -(x + 1) * (x - 1) * (x - 3)
text: -5, 4, "A", center-center, bbox
:::


:::{plot}
width: 100%
function: (x + 1) * (x - 1) * (x + 3)
text: -5, 4, "B", center-center, bbox
:::


:::{plot}
width: 100%
function: (x + 1) * (x - 1) * (x - 3)
text: -5, 4, "C", center-center, bbox
:::


:::{plot}
width: 100%
function: -(x + 1) * (x - 1) * (x + 3)
text: -5, 4, "D", center-center, bbox
:::


::::


::::{answer}
Graf C.
::::

:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5 (2 poeng)
Alma jobber med en følge av figurer som vist nedenfor. Hver sidekant i figurene har lengde $2$.

Hun vil bruke programmering til å regne ut den samlede omkretsen til de $10$ første figurene i følgen.



::::{multi-plot2}
---
rows: 1
cols: 3
---
:::{plot}
width: 100%
let: N = 3
let: L = 1
def: x(n) = L * cos(2 * pi * n / N)
def: y(n) = L * sin(2 * pi * n / N)
repeat: n=0..N-1; line-segment: (x(n), y(n)), (x(n + 1), y(n + 1)), solid, blue
repeat: n=0..N-1; point: (x(n), y(n))
ticks: off
axis: off
axis: equal
:::

:::{plot}
width: 100%
let: N = 4
let: L = 1
def: x(n) = L * cos(2 * pi * n / N)
def: y(n) = L * sin(2 * pi * n / N)
repeat: n=0..N-1; line-segment: (x(n), y(n)), (x(n + 1), y(n + 1)), solid, blue
repeat: n=0..N-1; point: (x(n), y(n))
ticks: off
axis: off
axis: equal
:::

:::{plot}
width: 100%
let: N = 5
let: L = 1
def: x(n) = L * cos(2 * pi * n / N)
def: y(n) = L * sin(2 * pi * n / N)
repeat: n=0..N-1; line-segment: (x(n), y(n)), (x(n + 1), y(n + 1)), solid, blue
repeat: n=0..N-1; point: (x(n), y(n))
ticks: off
axis: off
axis: equal
:::
::::


Hva må Alma bytte ut `????`{l=python} med i programmet sitt nedenfor for å løse oppgaven sin?

:::{code-block} python
---
linenos:
---
lengde = 2
sum_omkrets = 0
for n in range(1, 11):
    sum_omkrets = ????

print(sum_omkrets)
:::


::::{answer}
`sum_omkrets = sum_omkrets + (n + 2) * lengde`{l=python}
::::


:::::::::::::
::::::::::::::




:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 6 (4 poeng)
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

* Tangenten i punktet $(2, f(2))$ har stigningstall $4$.
* Tangenten i punktet $(4, f(4))$ har stigningstall $-4$. 

:::{plot}
width: 70%
function: -2 * (x - 3)**2 + 8, f
xmin: -0.5
xmax: 7
ymin: -8
ymax: 16
ticks: off
let: a = 2
tangent: a, f, solid, red
let: b = 4
tangent: b, f, solid, red
nocache:
point: (a, f(a))
text: a, f(a), "$({a}, f({a}))$", top-left
point: (b, f(b))
text: b, f(b), "$({b}, f({b}))$", top-right
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f'(x)$.


::::{answer}
$$
f'(x) = -4(x - 2) + 4 = -4x + 12
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Tangentene skjærer hverandre i punktet $(3, 10)$.

Bestem $f(x)$.


::::{answer}
$$
f(x) = -2x^2 + 12x - 10
$$
::::
:::::::::::::

::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 7 (2 poeng)
Grafen til en rasjonal funksjon $f$ er vist i figuren nedenfor.

Bestem et mulig uttrykk for $f(x)$.

:::{plot}
width: 70%
function: (x**2 - 4) / (x + 1)
line: 1, -1, dashed, red
point: (-2, 0)
point: (2, 0)
vline: -1, dashed, red
:::


::::{answer}
$$
f(x) = x - 1 + \dfrac{-3}{x + 1}
$$
::::


:::::::::::::::





### Del 2: Med hjelpemidler


:::::::::::::::{exercise} Oppgave 1 (8 poeng)
---
aids: true
---

:::{figure} ./bilder/blacksmithing.png
---
class: no-click
width: 40%
align: right
---
:::


En smed berarbeider et metallstykke. Funksjonen $T$ gitt ved 

$$
T(x) = 500 \cdot 0.95^x + 20, \quad x > 0
$$

viser temperaturen $T(x)$ grader celsius i metallstykket $x$ minutter etter at smeden tar det ut av ovnen.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hva er temperaturen i metallstykket idet det blir tatt ut av ovnen?


::::{answer}
$520~\degree\mathrm{C}$. 
::::
:::::::::::::



:::::::::::::{tab-item} b
Metallet kan bare bearbeides så lenge temperaturen i metallet er mer enn $150 \degree\mathrm{C}$. 


Hvor lang tid har smeden på seg til å bearbeide metallstykket etter det blir at ut av ovnen?

::::{answer}
Ca. $26$ minutter.

::::

:::::::::::::



:::::::::::::{tab-item} c
Bestem stigningstallet til linja som går gjennom punktene $(0, T(0))$ og $(10, T(10))$.

Gi en praktisk tolkning av svaret.

::::{answer}
* Stigningstallet er $-20.06$.
* Praktisk tolkning: Temperaturen til metallet stykket synker i gjennomsnitt med $20~\degree\mathrm{C}$ per minutt de første 10 minuttene etter at smeden tar ut metallstykket av ovnen.
::::

:::::::::::::


:::::::::::::{tab-item} d
Hva er temperaturen til omgivelsene til metallstykket, ifølge modellen?

::::{answer}
Temperaturen til omgivelsene er $20~\degree\mathrm{C}$.

::::

:::::::::::::


::::::::::::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2 (2 poeng)
---
aids: true
---

Til en konsert, ble det solgt billetter til to forskjellige priser:

:::{table}
width: 50%
labels: Type billett, Pris
Ordinær, 300 kr
Student, 200 kr
:::

<br>

Det ble til sammen solgt 250 billetter, og de totale inntektene var 58 000 kr.


Hvor mange av hver type billett ble solgt?


::::{answer}
$170$ studentbilletter og $80$ ordinære billetter.
::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 3 (4 poeng)
---
aids: true
---

Grunnflaten til en bygning skal ha en form som er består av et rektangel og en halvsirkel som vist i figuren nedenfor. 

Omkretsen $\mathcal{O}$ og arealet $A$ av en sirkel med radius $r$ er gitt ved

$$
\mathcal{O} = 2 \pi r \quad \text{og} \quad A = \pi r^2
$$

Omkretsen til bygningen skal være $100$ meter.


:::{plot}
figsize: (6, 3)
width: 70%
fontsize: 26
let: a = 40
let: b = 20
let: r = b / 2
def: x(t) = a + r * cos(t)
def: y(t) = b / 2 + r * sin(t)
line-segment: (0, 0), (a, 0), solid, blue
line-segment: (a, 0), (a, b), dashed, gray
line-segment: (a, b), (0, b), solid, blue
line-segment: (0, 0), (0, b), solid, blue
curve: x(t), y(t), (-pi / 2, pi / 2), solid, blue
text: 0.5 * a, 0, "$x$", bottom-center
text: 0 - 0.5, 0.5 * b, "$y$", center-left
axis: off
axis: equal
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet av grunnflaten til bygningen dersom $x = 40$ meter.

::::{answer}
$$
A(40) \approx 334.96
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem en eksakt verdi for det største mulige arealet grunnflaten til bygget kan ha.


::::{answer}
$$
A_\mathrm{størst} = \dfrac{5000}{\pi + 4}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 4 (6 poeng)
---
aids: true
---

> Oppgaven er endret litt siden sist du kanskje så denne fordi den forrige oppgaven ville gitt "uendelig" areal på datamaskinen. 

Nedenfor vises en figurfølge med fargelagte likesidete trekanter. Den første trekanten har areal $1$.

::::{multi-plot2}
---
rows: 1
cols: 4
---

:::{plot}
width: 100%
nocache:
figsize: (6, 6)
let: L = 6
let: h = sqrt(3) * L / 2
axis: off
axis: equal
lw: 1

macro: tri(x1, y1, x2, y2, x3, y3, color, alpha)
    fill-polygon: (x1, y1), (x2, y2), (x3, y3), color, alpha
    line-segment: (x1, y1), (x2, y2), solid, black
    line-segment: (x2, y2), (x3, y3), solid, black
    line-segment: (x3, y3), (x1, y1), solid, black
endmacro

use: tri(-L/2, 0, L/2, 0, 0, h, #7dd3fc, 0.3)
:::


:::{plot}
width: 100%
figsize: (6, 6)

let: L = 6
let: h = sqrt(3) * L / 2
axis: off
axis: equal
lw: 1

macro: tri(x1, y1, x2, y2, x3, y3, color, alpha)
    fill-polygon: (x1, y1), (x2, y2), (x3, y3), color, alpha
    line-segment: (x1, y1), (x2, y2), solid, black
    line-segment: (x2, y2), (x3, y3), solid, black
    line-segment: (x3, y3), (x1, y1), solid, black
endmacro

macro: bump(x1, y1, x2, y2, color, alpha)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2
    use: tri(p1x, p1y, ax, ay, p2x, p2y, color, alpha)
endmacro

line-segment: (-L/2, 0), (L/2, 0), solid, gray
line-segment: (L/2, 0), (0, h), solid, gray
line-segment: (0, h), (-L/2, 0), solid, gray

use: bump(-L/2, 0, L/2, 0, #7dd3fc, 0.70)
use: bump(L/2, 0, 0, h, #7dd3fc, 0.70)
use: bump(0, h, -L/2, 0, #7dd3fc, 0.70)
:::


:::{plot}
width: 100%
figsize: (6, 6)
let: L = 6
let: h = sqrt(3) * L / 2
axis: off
axis: equal
lw: 1

macro: tri(x1, y1, x2, y2, x3, y3, color, alpha)
    fill-polygon: (x1, y1), (x2, y2), (x3, y3), color, alpha
    line-segment: (x1, y1), (x2, y2), solid, black
    line-segment: (x2, y2), (x3, y3), solid, black
    line-segment: (x3, y3), (x1, y1), solid, black
endmacro

macro: bump(x1, y1, x2, y2, color, alpha)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2
    use: tri(p1x, p1y, ax, ay, p2x, p2y, color, alpha)
endmacro

macro: edge0(x1, y1, x2, y2, color)
    line-segment: (x1, y1), (x2, y2), solid, color
endmacro

macro: edge1(x1, y1, x2, y2, color)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2

    use: edge0(x1, y1, p1x, p1y, color)
    use: edge0(p1x, p1y, ax, ay, color)
    use: edge0(ax, ay, p2x, p2y, color)
    use: edge0(p2x, p2y, x2, y2, color)
endmacro

macro: refine(x1, y1, x2, y2, color, alpha)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2

    use: bump(x1, y1, p1x, p1y, color, alpha)
    use: bump(p1x, p1y, ax, ay, color, alpha)
    use: bump(ax, ay, p2x, p2y, color, alpha)
    use: bump(p2x, p2y, x2, y2, color, alpha)
endmacro

use: edge1(-L/2, 0, L/2, 0, gray)
use: edge1(L/2, 0, 0, h, gray)
use: edge1(0, h, -L/2, 0, gray)

use: refine(-L/2, 0, L/2, 0, #38bdf8, 0.75)
use: refine(L/2, 0, 0, h, #38bdf8, 0.75)
use: refine(0, h, -L/2, 0, #38bdf8, 0.75)
:::


:::{plot}
width: 100%
figsize: (6, 6)
axis: off
nocache:
axis: equal

let: L = 6
let: h = sqrt(3) * L / 2

macro: tri(x1, y1, x2, y2, x3, y3, color, alpha)
    fill-polygon: (x1, y1), (x2, y2), (x3, y3), color, alpha
    line-segment: (x1, y1), (x2, y2), solid, black
    line-segment: (x2, y2), (x3, y3), solid, black
    line-segment: (x3, y3), (x1, y1), solid, black
endmacro

macro: bump(x1, y1, x2, y2, color, alpha)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2
    use: tri(p1x, p1y, ax, ay, p2x, p2y, color, alpha)
endmacro

macro: edge0(x1, y1, x2, y2, color)
    line-segment: (x1, y1), (x2, y2), solid, color
endmacro

macro: edge1(x1, y1, x2, y2, color)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2

    use: edge0(x1, y1, p1x, p1y, color)
    use: edge0(p1x, p1y, ax, ay, color)
    use: edge0(ax, ay, p2x, p2y, color)
    use: edge0(p2x, p2y, x2, y2, color)
endmacro

macro: refine(x1, y1, x2, y2, color, alpha)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2

    use: bump(x1, y1, p1x, p1y, color, alpha)
    use: bump(p1x, p1y, ax, ay, color, alpha)
    use: bump(ax, ay, p2x, p2y, color, alpha)
    use: bump(p2x, p2y, x2, y2, color, alpha)
endmacro

macro: edge2(x1, y1, x2, y2, color)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2

    use: edge1(x1, y1, p1x, p1y, color)
    use: edge1(p1x, p1y, ax, ay, color)
    use: edge1(ax, ay, p2x, p2y, color)
    use: edge1(p2x, p2y, x2, y2, color)
endmacro

macro: refine2(x1, y1, x2, y2, color, alpha)
    let: p1x = (2*x1 + x2) / 3
    let: p1y = (2*y1 + y2) / 3
    let: p2x = (x1 + 2*x2) / 3
    let: p2y = (y1 + 2*y2) / 3
    let: dx = (x2 - x1) / 3
    let: dy = (y2 - y1) / 3
    let: ax = p1x + dx / 2 + sqrt(3) * dy / 2
    let: ay = p1y - sqrt(3) * dx / 2 + dy / 2

    use: refine(x1, y1, p1x, p1y, color, alpha)
    use: refine(p1x, p1y, ax, ay, color, alpha)
    use: refine(ax, ay, p2x, p2y, color, alpha)
    use: refine(p2x, p2y, x2, y2, color, alpha)
endmacro

use: edge2(-L/2, 0, L/2, 0, gray)
use: edge2(L/2, 0, 0, h, gray)
use: edge2(0, h, -L/2, 0, gray)

use: refine2(-L/2, 0, L/2, 0, #7dd3fc, 0.80)
use: refine2(L/2, 0, 0, h, #7dd3fc, 0.80)
use: refine2(0, h, -L/2, 0, #7dd3fc, 0.80)
:::
::::

La $T_n$ være antall fargelagte trekanter i figur $n$ og la $A_n$ være arealet til én slik trekant i figur $n$. La $F_n$ være arealet til det fargelagte området i figur $n$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en oversikt som vist nedenfor. Fyll ut verdiene som mangler.



:::{table}
width: 60%
labels: Figur $n$, $T_n$, $A_n$, $F_n$
$1$, $1$, $1$, $1 \cdot 1$ 
$2$, , , $3 \cdot \dfrac{1}{9}$,
$3$, ,
$4$, ,
:::


::::{answer}
:::{table}
width: 60%
labels: Figur $n$, $T_n$, $A_n$, $F_n$
$1$, $1$, $1$, $1 \cdot 1$ 
$2$, $3$, $\dfrac{1}{9}$, $3 \cdot \dfrac{1}{9}$
$3$, $3 \cdot 4 = 12$, $\dfrac{1}{9^2}$, $12 \cdot \dfrac{1}{9^2}$ 
$4$, $3 \cdot 4^2$ = 48, $\dfrac{1}{9^3}$, $48 \cdot \dfrac{1}{9^3}$
:::
::::




:::::::::::::


:::::::::::::{tab-item} b 
Bestem en formel for $F_n$ for $n = 3, 4, 5 \ldots$. 


::::{answer}
Vi har at $F_1 = 1$ og $F_2 = 3 \cdot \dfrac{1}{9}$. Formelen for $n = 3, 4, 5, \ldots$ kan beskrives ved

$$
F_n = T_n \cdot A_n = 3 \cdot 4^{n - 2} \cdot \dfrac{1}{9^{n - 1}}\quad \text{ for } \quad n \geq 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Figurfølgen består av $100$ figurer som følger samme mønster som de fire første figurene ovenfor.

Lag et program som regner ut det samlede arealet av de fargelagte trekantene av de $100$ første figurene i følgen.


:::{interactive-code}
# Din kode her


:::


::::{answer}
:::{code-block} python
---
linenos:
---
samlet_areal = 1 + 3 * 1 / 9 # n = 1 og n = 2
for n in range(3, 101): # n = 3, 4, ..., 100
    T = 3 * 4**(n - 2)
    A = 1 / 9**(n - 1)
    samlet_areal = samlet_areal + T * A
    
print(samlet_areal)
:::

som gir utskriften

:::{code-block} console
1.5999999999999994
:::

Det samlede arealet er altså ca. $1.6$. 
::::


:::::::::::::
::::::::::::::





:::::::::::::::