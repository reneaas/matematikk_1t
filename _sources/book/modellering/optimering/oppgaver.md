# Oppgaver: Optimering




:::::::::::::::{exercise} Oppgave 1
---
aids: true
---
Alma og Synne skal slå opp telt ved en elvebredde. De skal sette opp et tau rundt teltet for å holde dyr unna. 

De har $40$ meter med tau og vil sette opp tauet slik at det danner et rektangel der den éne siden er langs elvebredden. Se figuren nedenfor.

> Vannet er trygt slik at det ikke er noen alligatorer i elven, så det er ikke nødvendig å ha tau på den siden av teltet som vender mot elven!


:::{plot}
width: 70%
axis: off
figsize: (5, 2)
hline: 0, -10, 10, solid, blue
line-segment: (0, 0), (8, 0), black, solid
line-segment: (-4, 0), (-4, 5), black, solid
line-segment: (-4, 5), (4, 5), black, solid
line-segment: (4, 5), (4, 0), black, solid
text: 0, 0, "Elvebredde", bottom-center
annotate: (7, 6), (4, 5), "Tau", 0.5
text: -4, 0.5 * 5, "$y$", center-left
text: 0, 5, "$x$", top-center
axis: equal
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::

Lag en oversikt over arealet for ulike lengder på sidekantene og avgjør omtrent hvilken lengde på sidekantene som gir størst mulig areal.

:::{clear}
:::

:::{table}
width: 60%
labels: $x$, $y$, Areal
0, 20, 0
4, 18, 72
8, ,
...
40, , 
:::





::::{solution}
Siden vi vi har $40$ meter med tau, så vil vi ha at

$$
x + 2y = 40 \liff y = \dfrac{40 - x}{2}
$$

Arealet vil bare være 

$$
A = x \cdot y
$$

Da kan vi lage en oversikt som følger:


:::{figure} ./figurer/oppgaver/1/a/regneark_verdier.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

og oversikten med formler:



:::{figure} ./figurer/oppgaver/1/a/regneark_formler.png
---
class: no-click, adaptive-figure
width: 60%
---
:::




::::


:::::::::::::



:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::


Synne vil lage en grafisk framstilling som viser arealet av området for ulike lengder på sidekantene.

Lag en grafisk framstilling for Synne og bruk den til å bestemme hvilken lengde på sidekantene som gir størst mulig areal.


::::{answer}

:::{plot}
width: 80%
let: a = -1/2
let: b = 20
let: x0 = -b / (2*a)
function: x * (40 - x)  / 2, (0, 40), A
xmin: -5
xmax: 45
xstep: 5
ymin: -50
ymax: 300
ystep: 50
point: (x0, A(x0))
text: x0, A(x0), "$({x0}, {A(x0)})$", top-center
xlabel: $x / \mathrm{m}$
ylabel: $A(x) / \mathrm{m^2}$, -40
:::

::::



::::{solution}
Vi vet fra oppgave **a** at

$$
y = \dfrac{40 - x}{2}
$$

Arealet kan derfor behandles som en funksjon av $x$: 

$$
A = x \cdot y = x \cdot \dfrac{40 - x}{2}
$$

Altså er 

$$
A(x) = x \cdot \dfrac{40 - x}{2}
$$

Vi lager en grafisk framstilling og bruker {ggb-icon}`mode_extremum` til å finne koordinatene til ekstremalpunktet til grafen. 

:::{plot}
width: 80%
let: a = -1/2
let: b = 20
let: x0 = -b / (2*a)
function: x * (40 - x)  / 2, (0, 40), A
xmin: -5
xmax: 45
xstep: 5
ymin: -50
ymax: 300
ystep: 50
point: (x0, A(x0))
text: x0, A(x0), "$({x0}, {A(x0)})$", top-center
xlabel: $x / \mathrm{m}$
ylabel: $A(x) / \mathrm{m^2}$, -40
:::

::::


:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


Alma vil løse oppgaven helt eksakt. 

Bestem en eksakt verdi for sidelengdene som gir størst mulig areal.



:::{clear}
:::


::::{answer}
$$
x = 20 \and y = 10
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
align: right
width: 100%
function: (x**2 - 9)**4, (0, 3), f
xmin: -0.5
xmax: 3.5
ymin: -200
ymax: 7000
ticks: off
polygon: (0, 0), (1, 0), (1, f(1)), (0, f(1))
point: (0, 0)
point: (1, 0)
point: (1, f(1))
point: (0, f(1))
text: 1, f(1), "$(t, f(t))$", top-right
fontsize: 30
lw: 3.5
:::

Funksjonen $f$ er gitt ved

$$
f(x) = (x^2 - 9)^4 \qfor x \in \langle 0, 3 \rangle.
$$


Et rektangel har hjørnene $(0, 0)$, $(t, 0)$, $(t, f(t))$ og $(0, f(t))$. Se figuren til høyre.

:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::


Lag en systematisk oversikt som vist nedenfor. Fyll inn verdiene som mangler.


:::{clear}
:::


:::{table}
labels: $t$, Areal av rektangel
0, 0
0.5,
1, 4096
...
3,
:::


::::{answer}
Regneark med verdier:

:::{figure} ./figurer/oppgaver/2/a/regneark_verdier.png
---
class: no-click, adaptive-figure
width: 50%
---
:::

Oversikten med formlene som er brukt i regnearket:

:::{figure} ./figurer/oppgaver/2/a/regneark_formler.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

::::



:::::::::::::




:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::


Lag et funksjonsuttrykk som viser sammenhengen mellom $t$ og arealet av rektangelet.

Lag en grafisk framstilling av sammenhengen og bruk den til å bestemme det største mulige arealet rektangelet kan ha.



:::{clear}
:::

::::{answer}
:::{plot}
width: 70%
function: x * (x**2 - 9)**4, (0, 3), A
xmin: -0.5
xmax: 3.5
ymin: -0.5
ymax: 4200
ticks: off
point: (1, 4096)
text: 1, 4096, "$(1, 4096)$", top-right
:::

Størst mulig areal er $4096$ når $t = 1$.

::::


:::::::::::::



:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


Bestem en eksakt verdi for det største mulige arealet et slikt rektangel kan ha.

 
:::{clear}
:::

::::{answer}
$$
A_\mathrm{størst} = 4096
$$
::::
:::::::::::::



::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 3
---
aids: true
---

:::{plot}
align: right
width: 100%
let: k = 2
let: b = 9
function: -x**2 + b*x, (0, b), f
xmin: -1
xmax: 10
ymin: -1
ymax: 24
polygon: (0, 0), (k, 0), (k, f(k)), (0, f(k)), blue, 0.2
fontsize: 28
ticks: off
point: (0, 0)
point: (k, 0)
point: (k, f(k))
point: (0, f(k))
text: k, f(k), "$(k, f(k))$", bottom-right
text: k, 0, "$(k, 0)$", bottom-center
:::


Anna jobber med funksjonen $f$ gitt ved

$$
f(x) = -x^2 + 9x, \quad x \in [0, 9].
$$

Et rektangel har hjørnene $(0, 0)$, $(k, 0)$, $(k, f(k))$ og $(0, f(k))$. Se figuren til høyre.


:::{clear}
:::

Anna vil bruke programmering til å bestemme hvilken verdi av $k$ som gir størst mulig areal for rektangelet. Hun har skrevet disse funksjonene i programmet sitt:

```python
def f(x):
    return -x**2 + 9*x

def A(x):
    return x * f(x)
```

Hvilket program nedenfor kan Anna bruke for å løse oppgaven? 

::::{grid} 1 1 2 2
---
gutter: 2
---
:::{grid-item-card}
1)
^^^
```python
k = 0
while f(k) < f(k + 0.01):
    k = k + 0.01

print(k)
```
:::

:::{grid-item-card}
2)
^^^
```python
k = 0
while f(k) > f(k + 0.01):
    k = k + 0.01

print(k)
```
:::

:::{grid-item-card}
3)
^^^
```python
k = 0
while A(k) < A(k + 0.01):
    k = k + 0.01

print(k)
```
:::

:::{grid-item-card}
4)
^^^
```python
k = 0
while A(k) > A(k + 0.01):
    k = k + 0.01

print(k)
```
:::
::::


::::{answer}
Program 3.
::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
---
aids: true
---

:::{plot}
align: right
width: 100%
function: -x**2 + 9, (0, 3), f
xmin: -1
xmax: 4
ymax: 10
ymin: -1
ticks: off
polygon: (0, 0), (2, 0), (2, 5), blue, 0.2
point: (0, 0)
point: (2, 0)
point: (2, 5)
text: 0, 0, "$(0, 0)$", bottom-left
text: 2, 0, "$(k, 0)$", bottom-center
text: 2, 5, "$(k, f(k))$", top-right
fontsize: 28
:::

En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 9 \qder x \in [0, 3].
$$

En trekant har hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$. Se figuren nedenfor.



:::{clear}
:::

Lag et program som bestemmer det største mulige arealet trekanten kan ha.


:::{interactive-code}
# Din kode her


:::


::::{answer}
:::{code-block} python
---
linenos:
---
def f(x):
    return -x**2 + 9
    
def A(x):
    return x * f(x)
    
k = 0
while A(k) < A(k + 0.01):
    k = k + 0.01
    
print(A(k))
:::
::::


:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 5
---
aids: true
---

En tredjegradsfunksjon $f$ er gitt ved

$$
f(x) = -x^3 + 4x^2 \qder x \in [0, 4].
$$

En trekant har hjørner i punktene $(1, 0)$, $(4, 0)$ og $(1, f(1))$. Se figuren nedenfor.


:::{plot}
width: 70%
function: -x**3 + 4*x**2, (0, 4), f
xmin: -1
xmax: 5
ymax: 10
ymin: -1
yticks: off
grid: off
polygon: (1, 0), (4, 0), (1, 3), blue, 0.2
point: (1, 0)
point: (4, 0)
point: (1, 3)
text: 1, 3, "$(1, f(1))$", top-left
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::



Bestem arealet av trekanten.


:::{clear}
:::

::::{answer}
$$
\dfrac{9}{2}
$$
::::

:::::::::::::



:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



En trekant har hjørner i $(k, 0)$, $(4, 0)$, og $(k, f(k))$ der $k \in [0, 4]$. 

Bestem det største mulige arealet en slik trekant kan ha.


:::{clear}
:::

::::{answer}
$$
A_\mathrm{størst} = 8
$$
::::
:::::::::::::



::::::::::::::



:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 6
---
aids: true
---

:::{plot}
align: right
width: 100%
function: 8/(x**2 + 20), (0, 20), f
xmin: -1
xmax: 15
ymin: -0.1
ymax: 0.5
ystep: 0.1
point: (5, f(5))
point: (0, 0)
point: (0, f(5))
point: (5, 0)
polygon: (0, 0), (5, 0), (5, f(5)), (0, f(5)), blue, 0.2
text: 0, 0, "$(0, 0)$", bottom-left
text: 5, 0, "$(r, 0)$", bottom-center
text: 5, f(5), "$(r, f(r))$", top-right
text: 0, f(5), "$(0, f(r))$", top-left
ticks: off
fontsize: 28
:::

Anna jobber med funksjonen gitt ved

$$
f(x) = \dfrac{8}{x^2 + 20} \qder D_f = [0, \to \rangle
$$

Et rektangel har hjørnene $(0, 0)$, $(r, 0)$, $(r, f(r))$ og $(0, f(r))$.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::



Lag en systematisk oversikt over arealet for verdier av $r \in \{0, 1, 2, \ldots, 10\}$.

Bruk oversikten til å anslå hvilken verdi av $r$ som gir størst mulig areal.


:::{clear}
:::

::::{answer}
Fra oversikten nedenfor kan vi anslå at en verdi $r \in [4, 5]$ gir størst mulig areal.

Oversikt i regneark med verdier:

:::{figure} ./figurer/oppgaver/6/a/regneark_verdier.png
---
class: no-click, adaptive-figure
width: 60%
---
:::


Oversikt med formler:

:::{figure} ./figurer/oppgaver/6/a/regneark_formler.png
---
class: no-click, adaptive-figure
width: 60%
---
:::


::::

:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::



Lag en grafisk framstilling som viser sammenhengen mellom arealet $A(r)$ og $r$.

Bruk den grafiske framstillingen til å bestemme hvilken verdi av $r$ som gir størst mulig areal.


::::{answer}
:::{plot}
width: 70%
function: x * (8/(x**2 + 20)), (0, 18), A
xmin: -0.5
xmax: 14
ymin: -0.5
ymax: 1.5
ystep: 0.5
xstep: 2
point: (4.47, A(4.47))
text: 4.47, A(4.47), "$(4.47, {A(4.47):.2f})$", top-right
grid: off
:::

Arealet blir størst når $r \approx 4.47$ og det største arealet er omtrent $0.89$.

::::


:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem en eksakt verdi for det største arealet rektangelet kan ha.


:::{clear}
:::

::::{answer}
$$
A_\mathrm{størst} = \dfrac{2}{5} \sqrt{5}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Lag et program som finner det største mulige arealet et slikt rektangel kan ha.


:::{interactive-code}
# Din kode her


:::


::::{answer}
:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 20)
    
def A(x):
    return x * f(x)
    

x = 0
while A(x) < A(x + 0.01):
    x = x + 0.01
    
print(A(x))
:::
::::


:::::::::::::



::::::::::::::



:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 7
---
aids: true
---


En båt skal reise fra en øy $A$ til en øy $C$. 
Båten skal innom land i et punkt $B(x, 0)$ for å hente ferskvann. Punktet skal velges slik at reisen fra $A$ til $C$ blir så kort som mulig.

Kystlinjen starter i $S(0, 0)$ og er $9$ km lang. Øy $A$ ligger $2$ km fra land og øy $C$ ligger $4$ km fra land.

Se figuren nedenfor.


:::{plot}
figsize: (8, 4)
axis: equal
width: 70%
axis: off
let: ds = 0.4
hline: 0, -1, 10, solid
vline: 0, 0, 2, dashed, gray
vline: 9, 0, 4, dashed, gray
point: (0, 2)
point: (4, 0)
point: (9, 4)
line-segment: (0, 2), (4, 0), black, solid
line-segment: (4, 0), (9, 4), black, solid
line-segment: (0, ds), (ds, ds), black, solid
line-segment: (ds, 0), (ds, ds), black, solid
line-segment: (9 - ds, 0), (9 - ds, ds), black, solid
line-segment: (9, ds), (9 - ds, ds), black, solid
text: 4, 0, "$B(x, 0)$", bottom-right
text: 0, 2, "$A$", top-left
text: 9, 4, "$C$", top-right
lw: 1.5
point: (0, 0)
text: 0, -0.2, "$S(0, 0)$", bottom-left
bar: (0, -0.3), 4, horizontal
text: 2, -0.2, "$x$ km", bottom-center
bar: (0, -0.8), 9, horizontal
text: 4.5, -0.8, "9 km", bottom-center
bar: (-0.5, 0), 2, vertical
text: -0.5, 1, "2 km", center-left
bar: (9.5, 0), 4, vertical
text: 9.5, 2, "4 km", center-right
fontsize: 22
:::






::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::



Lag en oversikt som vist nedenfor. Fyll inn de manglende verdiene og bruk oversikten til å anslå hvilken verdi av $x$ som gir kortest mulig reisevei fra $A$ til $C$.

:::{clear}
:::


:::{table}
labels: $x$ (km), Reiselengde (km)
0, $\sqrt{4} + \sqrt{97} \approx 11.85$
1, $\sqrt{5} + \sqrt{80} \approx 11.18$
2, 
...
9,
:::



::::{answer}
Oversikt med verdier:


:::{figure} ./figurer/oppgaver/7/a/regneark_verdier.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Oversikt med formler:

:::{figure} ./figurer/oppgaver/7/a/regneark_formler.png
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::




:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::



Lag en modell $L(x)$ som viser sammenhengen mellom $x$ og reiselengden fra $A$ til $C$ når båten går innom land i punktet $B(x, 0)$.

Lag en grafisk framstilling som viser sammenhengen. 

Bruk den grafiske framstillingen til å anslå hvilken verdi av $x$ som gir kortest mulig reisevei fra $A$ til $C$.

::::{answer}
$$
L(x) = \sqrt{x^2 + 4} + \sqrt{(9 - x)^2 + 16}
$$

:::{plot}
width: 70%
figsize: (6, 6)
function: sqrt(x**2 + 2**2) + sqrt((9 - x)**2 + 4**2), (0, 9), L
xmin: -1
xmax: 10
ymin: 0
ymax: 14
ystep: 2
point: (3, L(3))
text: 3, L(3), "$(3, {L(3):.2f})$", top-right
grid: off
:::

Reiseveien er kortest når $x \approx 3$ km. Altså bør båten gå i land i $B(3, 0)$ for å få kortest mulig reisevei fra $A$ til $C$.

::::



:::::::::::::



:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::



Bestem en eksakt verdi for den korteste mulige reiseveien fra $A$ til $C$.


:::{clear}
:::

::::{answer}
$$
L_\mathrm{kortest} = 3\sqrt{13}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Lag et program som finner koordinatene til punktet $B$ som gir kortest reisevei.


:::{hints} Kvadratrot i Python
For å få kvadratrot i python har kan du importere `sqrt`{l=python}-funksjonen fra `math`{l=python}-biblioteket. For eksempel regner programmet nedenfor ut kvadratroten av $5$: 

```python
from math import sqrt

y = sqrt(5)
```

:::


:::{interactive-code}
# Din kode her

:::


::::{answer}
:::{code-block} python
---
linenos:
---
from math import sqrt

def L(x):
    return sqrt(x**2 + 2**2) + sqrt((9 - x)**2 + 4**2)
    

x = 0
while L(x) > L(x + 0.125):
    x = x + 0.125
    
B = (x, 0)
print(B)
:::

som gir utskriften $(3.0, 0)$. 
::::


:::::::::::::


::::::::::::::


:::::::::::::::




---





:::::::::::::::{exercise} Oppgave 8
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved 

$$
f(x) = ax^3 + bx^2, \quad x \in [0, 8]
$$

En trekant $\triangle ABC$ er dannet ved at $A$ er i origo, $B$ er er punkt på $x$-aksen og $C$ er et punkt på grafen til $f$ med samme $x$-koordinat som $B$.

:::{plot}
width: 60%
function: -2 * x**3 + 16 * x**2, (0, 8), f
xmin: -1
xmax: 9
ymin: -10
ymax: 160
polygon: (0, 0), (4, 0), (4, f(4)), blue, 0.2
ticks: off
point: (0, 0)
point: (4, 0)
point: (4, f(4))
text: 0, 0, "$A$", bottom-left
text: 4, 0, "$B$", bottom-right
text: 4, f(4), "$C$", top-left
fontsize: 26
:::

Om trekanten får du vite at:

* Arealet av trekanten er $7$ når koordinatene til $B$ er $(1, 0)$.
* Arealet av trekanten er størst når koordinatene til $B$ er $(6, 0)$.

Bestem $a$ og $b$. 


::::{answer}
$$
a = -2 \and b = 16
$$
::::

:::::::::::::::


---



::::::::::::::::{exercise} Oppgave 9
---
aids: true
---

Anna skal reise fra en holme som ligger $8$ km fra strandkanten. $12$ km fra det punktet på stranden som ligger nærmest holmen, ligger det en hytte. 
Anna kan ro med en fart på $2$ km/t og gå med en fart på $6$ km/t. Anna kan gå i land i hvilket som helst punkt $\ell$ på veien.

Se figuren nedenfor. 

:::{plot}
width: 70%
axis: off
xmin: -1
xmax: 13
ymax: 10
ymin: -2
point: (0, 8)
point: (4, 0)
point: (12, 0)
line-segment: (0, 8), (4, 0), blue, solid
hline: 0, -1, 13, solid, gray
vline: 0, 0, 8, dashed, gray
hline: 0, 4, 12, solid, red
text: 0, 8, "Holme", top-center
text: 12, 0, "Hytte", top-center
text: 4, 0, "$\ell$", top-right
bar: (-0.5, 0), 8, vertical
text: -0.5, 4, "8 km", center-left
bar: (0, -0.5), 4, horizontal
text: 2, -0.5, "$x$ km", bottom-center
bar: (0, -1.4), 12, horizontal
text: 6, -1.4, "12 km", bottom-center
text: 2, 4, "I vann", top-right
text: 8, -0.2, "På land", bottom-center
:::


:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem hvor lang tid Anna bruker til hytta dersom hun ror i land $6$ km fra det punktet på stranden som ligger nærmest holmen.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$6$ timer.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker Pytagoras' setning til å regne ut hvor langt Anna må ro for å komme i land $6$ km fra det punktet på stranden som ligger nærmest holmen. Da får vi at:

$$
L_\mathrm{robåt} = \sqrt{6^2 + 8^2} \, \mathrm{km} = \sqrt{100} \, \mathrm{km} = 10 \, \mathrm{km}.
$$

Siden Anna ror med en fart på $2$ km/t, bruker hun tiden

$$
T_\mathrm{robåt} = \frac{L_\mathrm{robåt}}{2 \, \mathrm{km/t}} = \frac{10 \, \mathrm{km}}{2 \, \mathrm{km/t}} = 5 \, \mathrm{t}
$$

til å ro til stranden. Hun må deretter gå $12 - 6 = 6$ km til hytta. Siden hun går med en fart på $6$ km/t, bruker hun tiden

$$
T_\mathrm{gåtur} = \frac{6 \, \mathrm{km}}{6 \, \mathrm{km/t}} = 1 \, \mathrm{t}
$$

til å gå til hytta. Den totale tiden hun bruker til hytta blir derfor

$$
T = T_\mathrm{robåt} + T_\mathrm{gåtur} = 5 \, \mathrm{t} + 1 \, \mathrm{t} = 6 \, \mathrm{t}.
$$

Altså bruker Anna $6$ timer. 

:::::

::::::::::::::


::::::::::::::{tab-item} b
Lag en modell $T$ som viser mange timer $T(x)$ Anna bruker på å reise til hytta dersom hun ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen. 

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T(x) = \dfrac{\sqrt{x^2 + 8^2}}{2} + \dfrac{12 - x}{6}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Hvis Anna ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen, må hun ro en avstand på

$$
L_\mathrm{robåt}(x) = \sqrt{x^2 + 8^2}
$$

Anna ror med en fart på $2$ km/t, så tiden hun bruker til å ro blir

$$
T_\mathrm{robåt}(x) = \frac{L_\mathrm{robåt}(x)}{2} = \frac{\sqrt{x^2 + 8^2}}{2}.
$$

Siden avstanden er 12 km fra punktet på strandlinja nærmest holmen bort til hytta, så må hun gå

$$
L_\mathrm{gåtur}(x) = 12 - x
$$

kilometer til hytta. Anna går med en fart på $6$ km/t, så tiden hun bruker til å gå blir

$$
T_\mathrm{gåtur}(x) = \frac{L_\mathrm{gåtur}(x)}{6} = \frac{12 - x}{6}.
$$

Dermed vil en modell for tiden Anna bruker til hytta når hun ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen være gitt ved

$$
T(x) = T_\mathrm{robåt}(x) + T_\mathrm{gåtur}(x) = \frac{\sqrt{x^2 + 8^2}}{2} + \frac{12 - x}{6}.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} c
Bestem hvor Anna må gå i land for at hun skal bruke minst mulig tid på å reise til hytta. <br>
Hva er den kortest tiden Anna kan bruke?


:::::{admonition} Fasit
---
class: answer, dropdown
---
Anna må gå i land ca. 2.83 km fra det punktet på stranden som ligger nærmest holmen for å få kortest mulig reisetid. Den korteste tiden Anna kan bruke på reisen er da ca. 5.77 timer.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å avgjøre hvor Anna må gå i land for å få kortest mulig reisetid, finner vi 
1. Ekstremalpunktet til $T$ ved å løse $T'(x) = 0$.
2. Regner ut $T(x)$ i ekstremalpunktet.

Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgaver/7/c/sol.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Dermed vil Anna måtte gå i land ca. 2.83 km fra det punktet på stranden som ligger nærmest holmen for å få kortest mulig reisetid. Den korteste tiden Anna kan bruke på reisen er da ca. 5.77 timer.

:::::

::::::::::::::

:::::::::::::::


::::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


:::{plot}
align: right
figsize: (6, 6)
axis: off
axis: equal
width: 100%
let: r = 2
let: h = sqrt(16 - r**2)
line-segment: (0, 0), (0, h), solid, black
line-segment: (0, 0), (r, 0), solid, black
ellipse: (0, 0), r, 0.2*r, dashed, blue
line-segment: (0, h), (r, 0), solid, blue
line-segment: (0, h), (-r, 0), solid, blue
text: 0.5 * r, -0.1, "$r$", center-center
text: 0, 0.5 * h, "$h$", center-left
text: 0.5 * r, 0.5 * h, "$9$", top-right
fontsize: 28
:::

En sirkulær kjegle med sidekant på $9$ er vist i figuren til høyre.

Volumet $V$ av en slik kjegle er gitt ved 

$$
V = \dfrac{\pi r^2 h}{3}
$$

der $r$ er radius i bunnen av kjeglen og $h$ er høyden til kjeglen.



Bestem en eksakt verdi for det største mulige volumet en slik kjegle kan ha.

:::{clear}
:::

::::{answer}
$$
V_\mathrm{størst} = 54\sqrt{3} \cdot \pi
$$
::::

::::{solution}
Vi har at 

$$
V = \dfrac{\pi r^2 h}{3} \and h^2 + r^2 = 9^2
$$

Vi skriver om den andre likningen til

$$
r^2 = 81 - h^2
$$

Så setter vi inn for $r^2$ i uttrykket for volumet slik at vi får:

$$
V(h) = \dfrac{\pi(81 - h^2)h}{3}
$$

For å bestemme en eksakt verdi for det største mulige volumet kjeglen kan ha:
1. Finner vi ekstremalpunktet ved å løse $V'(h) = 0$
2. Regner ut $V(h)$ i ekstremalpunktet.

Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgaver/10/sol.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Altså er det største mulige volumet en slik kjegle kan ha gitt ved 

$$
V_\mathrm{størst} = 54\sqrt{3} \cdot \pi
$$

::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 11
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::

En funksjon $f$ er gitt ved

$$
f(x) = -x^2 + 6x \qfor x \in [0, 6]
$$

Nedenfor vises grafen til $f$ sammen med et rektangel $ABCD$.

I rektangelet er $A(a, 0)$ og $D(a, f(a))$ der $a \in \langle 0, 3\rangle$. Punktet $C$ ligger på grafen til $f$.

Bestem en eksakt verdi for $a$ som gjør at arealet av rektangelet $ABCD$ er størst mulig.

:::{plot}
width: 70%
function: 6*x - x**2, (0, 6), f
polygon: (1, 0), (1, f(1)), (5, f(5)), (5, 0), blue, 0.2
xmin: -1
ymin: -1
ymax: 10
xmax: 7
ticks: off
point: (1, 0)
point: (1, f(1))
point: (5, f(5))
point: (5, 0)
text: 1, 0, "$A$", bottom-left
text: 1, f(1), "$D$", top-left
text: 5, f(5), "$C$", top-right
text: 5, 0, "$B$", bottom-right
:::



::::{answer}
$$
a = 3 - \sqrt{3}
$$
::::


::::{solution}
Funksjonen $f$ gir oss høyden til rektangelet. Koordinatene til $A$ er gitt ved $(a, 0)$ som betyr at høyden til rektangelet må være $f(a)$. Men vi må også avgjøre hva koordinatene til punktet $B$ er så vi vet hvor lang grunnlinja til rektangelet er. Men punktet $C$ må ha samme høyde $f(a)$ som betyr at $x$-koordinaten til både $B$ og $C$ kan bestemmes ved å løse likningen

$$
f(x) = f(a)
$$

som vi gjør med CAS: 

:::{figure} ./figurer/oppgaver/11/sol1.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså vil $f(x) = f(a)$ når 

$$
x = a \or x = 6 - a.
$$

Dermed vil arealet av rektangelet $ABCD$ være gitt ved

$$
A(a) = (6 - a - a) \cdot f(a) = (6 - 2a)f(a)
$$

For å bestemme den verdien av $a$ som gjør at arealet til rektangelet $ABCD$ er størst mulig, finner vi ekstremalpunktet ved å løse $A'(a) = 0$. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgaver/11/sol2.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Siden $a \in \langle 0, 3\rangle$, så er det største arealet av rektangelet $ABCD$ når 

$$
a = 3 - \sqrt{3}.
$$

::::

:::::::::::::::



---



::::::::::::::::{exercise} Oppgave 12
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


En takrenne skal lages i form av et åpent trapes ved å brette to sidekanter fra et flatt rektangel slik at alle sidelengder i takrenna er $10$ cm og takrennen har en høyde på $x$ cm. Se figuren nedenfor.


:::{plot}
width: 70%
axis: off
xmin: -8.5
xmax: 18.5
ymin: -2
ymax: 8
line-segment: (0, 0), (10, 0), black, solid
line-segment: (0, 0), (-8, 6), black, solid
line-segment: (10, 0), (18, 6), black, solid
text: 5, 0, "10 cm", bottom-center
text: -4, 3, "10 cm", center-left
text: 14.2, 3, "10 cm", center-right
hline: 6, -8, 18, dashed, gray
vline: 0, 0, 6, dashed, gray
vline: 10, 0, 6, dashed, gray
text: 0, 3, "$x$ cm", center-right
lw: 1.5
figsize: (6, 4)
:::



:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem tverrsnittsarealet $T$ av takrenna dersom høyden av takrenna er $6$ cm.



::::{answer}
$$
T = 108~\mathrm{cm^2}. 
$$
::::


::::{solution}
Takrenna består av to trekanter med grunnlinje 

$$
g = \sqrt{10^2 - 6^2} = \sqrt{64} = 8
$$

Rektangelet i midten har grunnlinje $10~\mathrm{cm}$ og høyde $6~\mathrm{cm}$. Dermed blir tverrsnittsarealet til takrenna

$$
T = \underbrace{10 \cdot 6}_{\mathrm{rektangel}} + \underbrace{2 \cdot \frac{1}{2} \cdot 8 \cdot 6}_{\mathrm{2 \, trekanter}} = 108
$$

Altså er tverrsnittsarealet $T$ av takrenna når høyden av takrenna er $6$ cm gitt ved $108~\mathrm{cm^2}$.
::::



::::::::::::::


::::::::::::::{tab-item} b
Lag en modell $T$ som gir tverrsnittsarealet $T(x)$ i $\mathrm{cm}^2$ når takrenna er $x$ cm høy.



::::{answer}
$$
T(x) = 10x + x\sqrt{100 - x^2}
$$
::::


::::{solution}
Når takrenna er $x$ cm høy, så vil grunnlinja til de to trekantene være

$$
\ell = \sqrt{10^2 - x^2} = \sqrt{100 - x^2}.
$$

Da blir tverrsnittsarealet til takrenna

$$
T(x) = \underbrace{10 \cdot x}_{\mathrm{rektangel}} + \underbrace{2 \cdot \frac{1}{2} \cdot \sqrt{100 - x^2} \cdot x}_{\mathrm{2 \, trekanter}} = 10x + x\sqrt{100 - x^2}.
$$
::::



::::::::::::::


::::::::::::::{tab-item} c
Bestem hvilken høyde som lar mest mulig vann strømme gjennom takrenna til enhver tid.

::::{answer}
$$
x = 5\sqrt{3} \, \mathrm{cm} \approx 8.66 \, \mathrm{cm}
$$
::::

::::{solution}
For å avgjøre hvilken høyde vi burde bruke for å få mest, må vi finne ekstremalpunktet til $T$ ved å løse $T'(x) = 0$. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgaver/12/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Fra utregningen finner vi at 

$$
x = 5 \sqrt{3} \approx 8.66
$$

gir det største mulige tverrsnittsarealet. Altså må høyden være ca. $8.66~\mathrm{cm}$ for at mest mulig vann skal kunne strømme gjennom takrenna til enhver tid.
::::
::::::::::::::

:::::::::::::::


::::::::::::::::



---






::::::::::::::::{exercise} Oppgave 13
---
aids: true
---


:::{plot}
width: 80%
axis: off, equal
xmin: -0.5
xmax: 10.5
ymax: 3
ymin: -1
lw: 1.5
hline: 0, 0, 10, solid, black
vline: 3, 0, 3, solid, black
vline: 7, 0, 3, solid, black
line-segment: (0, 0), (3, 3), black, solid
line-segment: (7, 3), (10, 0), black, solid
line-segment: (3, 3), (7, 3), black, solid
text: 1.5, 0, "$x$", bottom-center
text: 5, 0, "$y$", bottom-center
text: 8.5, 0, "$x$", bottom-center
text: 3, 1.5, "$x$", center-right
text: 7, 1.5, "$x$", center-left
text: 5, 3, "$y$", top-center
vline: 2.6, 0, 0.4, solid, black
hline: 0.4, 2.6, 3, solid, black
hline: 0.4, 7, 7.4, solid, black
vline: 7.4, 0, 0.4, solid, black
figsize: (7, 3)
:::



Else skal gjerde inn tre områder for å lage en grønnsakshage. Det største området skal ha form som et rektangel og de to minste som likebeinte rettvinklede trekanter. Se figuren ovenfor.

Else skal sette opp gjerde langs alle linjestykkene vist i figuren ovenfor. <br>
Hun har til sammen 100 m gjerde som hun vil bruke.

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Hvor stor blir arealet av grønnsakhagen dersom hun velger at katetene i trekantene skal være $8$ meter?


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A = 245.5 \, \mathrm{m}^2
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Først må vi bestemme hvor lange linjestykkene $y$ i figuren er. Vi vet at $x = 8$ meter. Til sammen summerer linjestykkene til $L = 100$ meter. Vi kan skrive den samlede lengden av linjestykkene som

$$
L = \underbrace{2x}_{\mathrm{kateter}} + \underbrace{2x + 2y}_{\mathrm{rektangel}} + \underbrace{2\sqrt{2}x}_{\mathrm{hypotenuser}} = 100
$$

der vi har brukt Pytagoras' setning til å finne at begge hypotenusene i de rettvinklede trekantene må være 

$$
h^2 = x^2 + x^2 \limplies h = \sqrt{2}x.
$$

Vi kan først løse likningen for $y$ slik at vi kan regne ut $y$ for en hver verdi av $x$:

$$
4x + 2y + 2\sqrt{2}x = 100 \liff 2x + y + \sqrt{2}x = 50
$$

som gir 

$$
y = 50 - (2 + \sqrt{2})x.
$$

Det samlede arealet til grønnsakhagen blir

\begin{align*}
    A &= A_{\mathrm{rektangel}} + 2A_{\mathrm{trekant}} \\
    \\
    &= xy + 2 \cdot \frac{1}{2}x^2 \\
    \\
    &= x\left(50 - (2 + \sqrt{2})x\right) + x^2 \\
    \\
    &= 50x - (2 + \sqrt{2})x^2 + x^2 \\
    \\
    &= 50x - (1 + \sqrt{2})x^2
\end{align*}


Vi kan definere en funksjon $A(x)$ i CAS og regne ut arealet for $x = 8$:

:::{figure} ./figurer/oppgave_7/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at arealet av grønnsakhagen er omtrent $A = 245.5 \, \mathrm{m}^2$ dersom katetene i trekantene er $8$ meter lange.


:::::

::::::::::::::

::::::::::::::{tab-item} b
Lag en oversikt som viser hvordan arealet av grønnsakhagen endrer seg dersom hun velger andre lengder på katetene. Av oversikten skal Else kunne se omtrent hvor lange katetene må være for at arealet av grønnsakhagen skal bli størst mulig.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker en grafisk framstilling av arealet $A(x)$ for å se hvordan arealet endrer seg med lengden på katetene. Vi kan bruke Geogebra-vinduet til å lage grafen til $A$ siden vi allerede har definert $A(x)$ i CAS.

:::{figure} ./figurer/oppgave_7/b.png
---
width: 100%
class: no-click, adaptive-figure
---
viser en grafisk fremstilling av arealet $A(x) \, \mathrm{m}^2$ på $y$-aksen når katetene i trekanten er $x$ meter lange. 
:::

Fra den grafiske framstillingen kan vi se at arealet er størst når katetene i trekanten er omtrent $x = 10$ meter lange fordi dette svarer til et toppunkt på grafen til $A$.
:::::


::::::::::::::


::::::::::::::{tab-item} c
Lag en modell $A$ som Else kan bruke for å regne ut arealet $A(x)$ av grønnsakhagen for ulike verdier av $x$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(x) = 50x - (1 + \sqrt{2})x^2.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi har allerede laget denne modellen i oppgave **a** som er gitt ved 

$$
A(x) = 50x - (1 + \sqrt{2})x^2.
$$
:::::

::::::::::::::


::::::::::::::{tab-item} d
Bruk modellen til å finne den lengden av katetene som vil gi det største arealet.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = (25\sqrt{2} - 25) \, \mathrm{m} \approx 10.36 \, \mathrm{m}.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme den kateten som gir størst mulig areal, bruker vi CAS og løser $A'(x) = 0$ for å bestemme $x$-koordinaten til toppunktet til $A$:

:::{figure} ./figurer/oppgave_7/d.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at arealet er størst når katetene i trekantene er 

$$
x = (25\sqrt{2} - 25) \, \mathrm{m} \approx 10.36 \, \mathrm{m}.
$$

Men *vet* vi at dette er et toppunkt? Ja, for den ledende koeffisienten til $A(x)$ er negativ, så vi *legger'n død* – og vi hadde strengt tatt grafen som viste det i oppgave **b** også.

:::::

::::::::::::::


::::::::::::::{tab-item} e
Bestem modellens gyldighetsområde.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
0 < x < \dfrac{50}{\sqrt{2} + 2}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Modellen er gyldig så lenge $A(x) > 0$ og $y > 0$. Vi løser den første ulikheten i CAS:


:::{figure} ./figurer/oppgave_7/e.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er $A(x) > 0$ når

$$
x \in \left\langle 0, 50 \sqrt{2} - 50 \right\rangle.
$$

Men vi må også sjekke at $y > 0$. Fra **a** vet vi at 

$$
y = 50 - (2 + \sqrt{2})x
$$

så vi løser ulikheten $y > 0$ i CAS:

:::{figure} ./figurer/oppgave_7/e2.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Kombinerer vi de to løsningene, ser vi at modellen er gyldig så lenge

$$
0 < x < \dfrac{50}{\sqrt{2} + 2}
$$

:::::


::::::::::::::

:::::::::::::::

::::::::::::::::




---






:::::::::::::::{exercise} Oppgave 14
---
aids: true
---

Isabel er industridesigner. Hun arbeider med et design på bokser med form som sylindre.


:::{plot}
width: 80%
ellipse: (0, 5), 3, 0.5, black, solid
ellipse: (0, 0), 3, 0.5, black, solid
line-segment: (-3, 0), (-3, 5), black, solid
line-segment: (3, 0), (3, 5), black, solid
figsize: (3, 4)
ymin: -1
axis: off
align: right
bar: (3.8, 0), 5, v
text: 3.8, 2.5, "$h$", center-right
bar: (0, 6), 3, h
text: 1.5, 6, "$r$", top-center
hline: 5, 0, 3, dashed, gray
:::

Formel for å regne ut volumet av en boks med radius $r$ og høyde $h$ er

$$
V = \pi r^2 h
$$

Formel for å regne ut arealet av overflaten av boksen er 

$$
\mathcal{O} = \pi  r^2 + 2\pi r  h
$$

Isabel lurer på hvor stor radius hun bør velge og hvor høye boksene må være, når hver boks skal ha 
* et volum $V$ på $450 \, \mathrm{cm}^3$
* minst mulige overflate $\mathcal{O}$

Isabel ser at når hun har gitt volum og radius, kan hun regne ut høyden ved å bruke formelen $V = \pi \cdot r^2 \cdot h$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::


Lag en oversikt som vist nedenfor. Gjør beregninger og fyll inn verdiene som mangler.

:::{clear}
:::

:::{table}
labels: Radius $r$ (cm), Høyde $h$ (cm), Overflate $\mathcal{O}$ ($\mathrm{cm}^2$), Volum $V$ ($\mathrm{cm}^3$) 
2, 35.8, 462.6, 450
4, , , 450
6, , , 450
8, , , 450
:::

:::::{solution}
Vi kan skrive om formelen for volum slik at vi kan bestemme høyden $h$ gitt et volum $V$ og en radius $r$ som:

$$
V = \pi \cdot r^2 \cdot h \liff h = \dfrac{V}{\pi \cdot r^2}
$$

Deretter lager vi et regneark der vi fyller ut tabellen:

:::{figure} ./figurer/oppgaver/oppgave_12/a_regneark.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

Nedenfor vises en oversikt over formlene som er brukt i regnearket:

:::{figure} ./figurer/oppgaver/oppgave_12/a_regneark_med_formler.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

:::::

:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::



Sett opp et funksjonsuttrykk Isabel kan bruke, og lag en grafisk framstilling som viser sammenhengen mellom radius og overflate.


:::{clear}
:::

:::::{solution}
Vi kan lage et funksjonsuttrykk $O(r)$ for overflaten $O$ av boksen for en gitt høyde $r$. Volumet $V = 450$, så vi kan sette opp et likningssystem for å bestemme $O(r)$. Vi løser likningssystemet med CAS:

:::{figure} ./figurer/oppgaver/oppgave_12/b_formel.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

som betyr at vi kan skrive 

$$
O(r) = \dfrac{\pi r^3 + 900}{r} \and h = \dfrac{450}{\pi r^2}.
$$

Deretter kan vi lage en grafisk framstilling av funksjonen $O(r)$: 

:::{plot}
width: 100%
function: (pi * x**3 + 900) / x, (0.0001, 100), blue
xmin: -2
xmax: 22
ymin: -1000
ymax: 5000
xstep: 2
ystep: 1000
xlabel: $r / \mathrm{cm}$
ylabel: $O(r) / \mathrm{cm}^2$, -50
:::





:::::

:::::::::::::


:::::::::::::{tab-item} c


:::{cas-popup}
:::


:::{ggb-popup}
:::



Hvor står må radius i boksene være for at overflaten skal bli minst mulig? <br>
Hvor stor blir overflaten da?

:::::{solution}
For å bestemme hvilken radius som gir minst mulig overflate, så kan vi løse likningen

$$
O'(r) = 0
$$

Deretter kan vi regne ut $O(r)$ i dette punktet. Vi gjør dette med CAS:

:::{figure} ./figurer/oppgaver/oppgave_12/c.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

Ut ifra den grafiske framstillingen fra **b** kan vi være sikre på at løsningen her gir et bunnpunkt og dermed den minste overflaten. Vi har da at boksen har minst overflate dersom 

$$
r \approx 5.23 \, \mathrm{cm}
$$

som gir en overflate på ca. $258 \, \mathrm{cm}^2$.



:::::

:::::::::::::

::::::::::::::




:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 15
---
aids: true
---

:::{plot}
align: right
width: 100%
ellipse: (0, 4), 2, 0.7, solid, black
line-segment: (0, 0), (2, 4), solid, black
line-segment: (0, 0), (-2, 4), solid, black
nocache:
vline: 0, 0, 4, dashed, gray
hline: 4, 0, 2, dashed, gray
text: 0, 2, "$h$", center-right
text: 1, 4, "$r$", top-center
text: 1, 2, "$\ell$", bottom-right
figsize: (4, 4)
xmin: -3
xmax: 3
ymin: -1
ymax: 5
ticks: off
axis: off
line-segment: (0.3, 4), (0.3, 3.7), solid, gray
line-segment: (0, 3.7), (0.3, 3.7), solid, gray
:::


En kjegle har radius $r$, høyde $h$ og sidelengde $\ell$.

Formlene for overflatearealet $A$ og volumet $V$ til kjeglen er gitt ved

$$
A = \pi r^2 + \pi r \ell \qog V = \frac{1}{3} \pi r^2 h.
$$

Sidelengden $\ell$ er gitt ved 

$$
\ell = \sqrt{r^2 + h^2}.
$$


En kjegle skal ha volumet $12\pi \, \mathrm{cm}^3$ og minst mulig overflate.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en oversikt som vist nedenfor. Gjør beregninger og fyll inn verdiene som mangler.


:::{table}
labels: Radius $r$ (cm), Høyde $h$ (cm), Overflate $A$ (cm$^2$), Volum $V$ (cm$^3$)
1, , , 12$\pi$
2, , , 12$\pi$
3, , , 12$\pi$
4, , , 12$\pi$
5, , , 12$\pi$
:::


:::::::::::::


:::::::::::::{tab-item} b
Sett opp et funksjonsuttrykk som viser sammenhengen mellom overflatearealet og radius.

Lag en grafisk framstilling av funksjonen.

:::::::::::::


:::::::::::::{tab-item} c
Hva må radius være for at overflaten skal bli minst mulig?

Hvor stort er overflatearealet da?
:::::::::::::


::::::::::::::



:::::::::::::::



---





:::::::::::::::{exercise} Oppgave 16
---
aids: true
---


:::{cas-popup}
---
layout: sidebar
---
:::



En kurve er gitt ved grafen til funksjonen $f(x) = x^2$. I samme figur er et punkt $P(6, 3)$. 
Et linjestykke $\ell$ går fra punktet $P$ til et punkt på grafen.

Bestem koordinatene til punktet på grafen som gjør at $\ell$ blir kortest mulig. Bestem et eksakt uttrykk for lengden av $\ell$ i dette tilfellet.

:::{plot}
width: 70%
function: x**2, f
point: (5, 3)
text: 5, 3, "$P(6, 3)$", top-right
ymin: -1 
ymax: 8
xmin: -3
hline: 3, 2.5, 5, dashed, gray
vline: 2.5, 3, f(2.5), dashed, gray
point: (2.5, f(2.5))
text: 2.5, f(2.5), "$(x, f(x))$", top-right
line-segment: (5, 3), (2.5, f(2.5)), red, solid
text: 3.7, 4.5, "$\ell$", top-right
ticks: off
polygon: (2.5, 3), (2.8, 3), (2.8, 3.4), (2.5, 3.4)
:::

::::{answer}
* Koordinatene til punktet på grafen er $(2, 4)$
* Lengden til linjestykket er da $\sqrt{17}$
::::


::::{solution}
Avstanden fra punktet $P(6, 3)$ til et punkt på grafen $(x, f(x))$ kan vi uttrykke ved hjelp av Pytagoras' setning:

$$
d(x) = \sqrt{(x - 6)^2 + (f(x) - 3)^2} = \sqrt{(x - 6)^2 + (x^2 - 3)^2}
$$


For å bestemme ekstremalpunktene til $d$, må vi løse $d'(x) = 0$ og sjekke at $d''(x) > 0 i punktet for å sikre at det er et bunnpunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_9/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $d'(x) = 0$ når $x = 2$. Vi ser også at $d''(2) > 0$ som betyr at $d$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $x = 2$ et bunnpunkt. Derfor vil linjestykket $\ell$ bli kortest mulig når det går fra $P(6, 3)$ til punktet $(2, f(2)) = (2, 4)$ på grafen. Vi ser også at $d(2) = \sqrt{17}$ som er lengden av linjestykket i dette tilfellet.

::::


:::::::::::::::




---





:::::::::::::::{exercise} Oppgave 17
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


En likebeint trekant skal innskrives i en sirkel med radius $1$. 

Bestem en eksakt verdi for det største arealet en slik trekant kan ha.


:::{plot}
width: 50%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
fontsize: 30
:::


::::{hints} Vanskelig å komme i gang? Her er en hjelpefigur!
Nedenfor vises en mindre rettvinklet trekant som er tegnet inn som du kan bruke for å hjelpe deg å finne et uttrykk for arealet av den store trekanten.

:::{plot}
width: 55%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
line-segment: (0, 0), (0, sin(-pi/4)), black, dashed
line-segment: (0, 0), (cos(pi + pi/4), sin(pi + pi/4)), black, dashed
text: 0.5 * (cos(pi + pi/4)), 0.5 * (sin(pi + pi/4)) + 0.15, "$1$", center-center
text: 0 + 0.1, 0.5 * sin(-pi/4), "$x$", center-center
text: 0.5 * cos(pi + pi/4), sin(pi + pi/4) - 0.1, "$\ell$", center-center
fontsize: 30
polygon: (0, sin(-pi/4)), (-0.15, sin(-pi/4)), (-0.15, sin(-pi/4) + 0.15), (0, sin(-pi/4) + 0.15)
:::
::::


::::{answer}
$$
\dfrac{3\sqrt{3}}{4}
$$
::::


::::{solution}
:::{plot}
align: right
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
line-segment: (0, 0), (0, sin(-pi/4)), black, dashed
line-segment: (0, 0), (cos(pi + pi/4), sin(pi + pi/4)), black, dashed
text: 0.5 * (cos(pi + pi/4)), 0.5 * (sin(pi + pi/4)) + 0.15, "$1$", center-center
text: 0 + 0.1, 0.5 * sin(-pi/4), "$x$", center-center
text: 0.5 * cos(pi + pi/4), sin(pi + pi/4) - 0.1, "$\ell$", center-center
fontsize: 30
polygon: (0, sin(-pi/4)), (-0.15, sin(-pi/4)), (-0.15, sin(-pi/4) + 0.15), (0, sin(-pi/4) + 0.15)
:::
Vi lager en hjelpefigur der vi lager en mindre rettvinklet som vi kan bruke til å finne et uttrykk for arealet av den store trekanten som vist til høyre.

Vi trenger å et uttrykk for grunnlinja og høyden til trekanten for å kunne finne et uttrykk for arealet.

Fra Pytagoras' setning har vi at 

$$
\ell^2 + x^2 = 1^2
$$

Vi kan løse denne likningen for $\ell$:

$$
\ell = \sqrt{1 - x^2}
$$

:::{clear}
:::

Grunnlinjen $g$ til den store trekanten er da $g = 2\ell$. 

Høyden til trekanten vil være $h = x + 1$. 

Arealet $A$ av trekanten kan da skrives som:

$$
A = \dfrac{g \cdot h}{2} = \dfrac{2\ell \cdot h}{2} = \ell \cdot h
$$

Setter vi inn uttrykket for $\ell$ og $h$, får vi funksjonen

$$
A(x) = \ell \cdot h = \sqrt{1 - x^2} \cdot (x + 1) = (x + 1)\sqrt{1 - x^2}
$$


For å bestemme det største arealet $A$ vi kan få, så løser vi $A'(x) = 0$ og sjekker at $A''(x) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:


:::{figure} ./figurer/oppgave_12/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $x = \dfrac{1}{2}$ er et ekstremalpunkt og vi ser at $A''\left(\dfrac{1}{2}\right) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $x = \dfrac{1}{2}$ et toppunkt. Derfor vil arealet $A$ bli størst mulig når $x = \dfrac{1}{2}$. Fra utskriften kan vi da også konkludere at det eksakte største arealet er

$$
A\left(\dfrac{1}{2}\right) = \dfrac{3\sqrt{3}}{4}
$$

::::


:::::::::::::::




---





:::::::::::::::{exercise} Oppgave 18
---
aids: true
---



:::{cas-popup}
---
layout: sidebar
---
:::


En kjegle med sirkulær grunnflate med radius $r$ og høyde $h$ er innskrevet i en kule med radius $1$. 

Volumet $V$ av en slik kjegle er gitt ved 

$$
V = \dfrac{\pi r^2 h}{3}
$$


Se figurene nedenfor.

::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
line-segment: (0, 1), (cos(-pi/6), sin(-pi/6))
line-segment: (0, 1), (cos(pi + pi/6), sin(pi + pi/6))
ellipse: (0, 0), 1, 0.2, gray, dashed
ellipse: (0, sin(-pi/6)), cos(-pi/6), 0.2, red, dashed
line-segment: (0, sin(-pi/6)), (cos(-pi/6), sin(-pi/6)), black, solid
text: 0.5 * cos(-pi/6), sin(-pi/6) - 0.1, "$\ell$", center-center
bar: (1.1, -0.5), 1.5, vertical
text: 1.05, 0.25, "$h$", center-right
fontsize: 30
lw: 3
:::

:::{plot}
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
line-segment: (0, 1), (cos(-pi/6), sin(-pi/6))
line-segment: (0, 1), (cos(pi + pi/6), sin(pi + pi/6))
line-segment: (0, sin(-pi/6)), (cos(-pi/6), sin(-pi/6)), black, solid
line-segment: (0, sin(-pi/6)), (-cos(-pi/6), sin(-pi/6)), black, dotted
line-segment: (0, 0), (cos(-pi/6), sin(-pi/6)), solid, black
line-segment: (0, 0), (0, sin(-pi/6)), solid, black
text: 0.5 * cos(-pi/6), sin(-pi/6) - 0.1, "$\ell$", center-center
bar: (1.1, -0.5), 1.5, vertical
text: 1.05, 0.25, "$h$", center-right
fontsize: 30
lw: 3
text: 0 - 0.1, 0.5 * sin(-pi/6), "$s$", center-center
text: 0.5 * cos(-pi/6), 0 - 0.1, "$1$", center-center
polygon: (0, sin(-pi/6)), (0.1, sin(-pi/6)), (0.1, sin(-pi/6) + 0.1), (0, sin(-pi/6) + 0.1)
line-segment: (0, 0), (0, 1), dotted, black
text: 0 + 0.1, 0.4, "$1$", center-left
:::
::::


Bestem det største volumet en slik kjegle kan ha. 


::::{answer}
$$
V_\text{størst} = \dfrac{32}{81}\pi
$$
::::

::::{solution}

Volumet av en kjegle er gitt ved 

$$
V = \dfrac{Gh}{3}
$$

der $G$ er arealet av grunnflaten og $h$ er høyden. Arealet av grunnflaten er gitt ved

$$
G = \pi r^2
$$

Høyden $h$ er gitt ved 

$$
h = 1 + \ell
$$

Fra figuren kan vi bruke Pytagoras' setning på den rettvinkla trekanten til å skrive opp sammenhengen:

$$
r^2 + \ell^2 = 1^2
$$

Fra dette finner vi at 

$$
\ell = \sqrt{1 - r^2}
$$

Det betyr at høyden er 

$$
h = 1 + \sqrt{1 - r^2}
$$

Dermed vil volumet av kjeglen kunne uttrykkes som en funksjon av $r$:

$$
V(r) = \dfrac{\pi r^2 \left(1 + \sqrt{1 - r^2}\right)}{3}
$$

Vi bruker CAS til å bestemme ekstremalpunktene til $V$ og avgjør hvilke av punktene som er toppunkter ved å sjekke at $V''(r) < 0$ i punktet:

:::{figure} ./figurer/oppgave_13/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Fra utskriften ser vi at $V'(r) = 0$ når 

$$
r = 0 \or r = \pm \dfrac{2\sqrt{2}}{3}
$$

Når $r = 0$ så er $V(r) = 0$ så dette er opplagt ikke det største volumet. Den eneste løsningen som gir mening er derfor $r = \dfrac{2\sqrt{2}}{3}$. Vi ser også at $V''\left(\dfrac{2\sqrt{2}}{3}\right) < 0$ som betyr at $V$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $r = \dfrac{2\sqrt{2}}{3}$ et toppunkt. Derfor vil volumet $V$ bli størst mulig når $r = \dfrac{2\sqrt{2}}{3}$. Fra utskriften kan vi da også konkludere at det eksakte største volumet er

$$
V_\text{størst} = \dfrac{32}{81}\pi
$$




::::
:::::::::::::::



---





:::::::::::::::{exercise} Oppgave 19
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


Fire byer $A$, $B$, $C$ og $D$ ligger plassert slik at de danner et kvadrat med sidelengde $10$ km. 

Vi skal lage en veiforbindelse mellom disse fire byene. Veilengden mellom de fire byene blir kortest mulig dersom vi lager veiene via to punkter $E$ og $F$. Se figuren nedenfor.

Vi lar $x$ være avstanden mellom $E$ og $F$. 

Bestem $x$ slik at den samlede veilengden mellom byene blir kortest mulig.


:::{plot}
width: 70%
point: (0, 0)
point: (10, 0)
point: (10, 10)
point: (0, 10)
axis: off
axis: equal
point: (5, 2)
point: (5, 8)
line-segment: (0, 0), (5, 2)
line-segment: (10, 0), (5, 2)
line-segment: (10, 10), (5, 8)
line-segment: (0, 10), (5, 8)
line-segment: (5, 2), (5, 8)
line-segment: (0, 0), (10, 0), dashed, gray
line-segment: (10, 0), (10, 10), dashed, gray
line-segment: (10, 10), (0, 10), dashed, gray
line-segment: (0, 10), (0, 0), dashed, gray
text: 0, 0, "$A$", bottom-left
text: 10, 0, "$B$", bottom-right
text: 10, 10, "$C$", top-right
text: 0, 10, "$D$", top-left
text: 5, 2, "$E$", bottom-center
text: 5, 8, "$F$", top-center
text: 5, 5, "$x$", center-right
text: 2.5, 1, "$s$", top-left
text: 10 - 2.5, 1, "$s$", top-right
text: 2.5, 9, "$s$", bottom-left
text: 10 - 2.5, 9, "$s$", bottom-right
text: 5, 0, "$10$", bottom-center
text: 10, 5, "$10$", center-right
:::



::::{answer}
$$
x = \dfrac{-10\sqrt{3} + 30}{3}
$$
::::




:::::::::::::::






----



:::::::::::::::{exercise} Oppgave 20
---
aids: true
---

En halvsirkel er gitt ved

$$
x^2 + y^2 = 4 \qder y \geq 0.
$$

Et rektangel har hjørnene $(-a, 0)$, $(a, 0)$, $(a, f(a))$ og $(-a, f(-a))$ der $f$ er funksjonen som beskriver halvsirkelen. 

Se figuren nedenfor.


:::{plot}
width: 70%
ticks: off 
xmin: -2.5
xmax: 2.5
ymin: -0.1
ymax: 2.5
function: sqrt(4 - x**2), (-2, 2), f
polygon: (-1.5, 0), (1.5, 0), (1.5, f(1.5)), (-1.5, f(-1.5)), blue, 0.2
point: (-1.5, 0)
point: (1.5, 0)
point: (1.5, f(1.5))
point: (-1.5, f(-1.5))
axis: equal
text: -1.5, 0, "$(-a, 0)$", bottom-center
text: 1.5, 0, "$(a, 0)$", bottom-center
text: 1.5, f(1.5), "$(a, f(a))$", top-right
text: -1.5, f(-1.5), "$(-a, f(-a))$", top-left
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::

Lag en systematisk oversikt over arealet av rektangelet for ulike verdier av $a \in [0, 2]$ og finn et estimat på hvilken verdi av $a$ som gir størst mulig areal.

:::::::::::::


:::::::::::::{tab-item} b
:::{ggb-popup}
---
layout: sidebar
---
:::

Lag en grafisk framstilling som viser sammenhengen mellom arealet $A(a)$ av rektangelet og $a$.

Bestem det største mulige arealet rektangelet kan ha.

:::::::::::::



:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Bestem en eksakt verdi for det største arealet rektangelet kan ha.
:::::::::::::


::::::::::::::





:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 21
---
aids: true
---

En trekant $\triangle PQM$ der $a \in \langle 0, 4\rangle$ er innskrevet i et større trekant $\triangle OBA$. Se figuren nedenfor.

:::{plot}
width: 70%
ticks: off
let: x = 2.4
point: (0, 4)
point: (8, 0)
point: (0, x)
point: (x, 0)
point: (4, 2)
let: dx = 0.15
let: dy = 0.15
line-segment: (0, 4), (8, 0), solid, black
polygon: (x, 0), (0, x), (4, 2), blue, 0.2
text: 0 - dx, x, "$P(0, a)$", center-left
text: x, -dy, "$Q(a, 0)$", bottom-center
text: -dx, -dy, "$O$", bottom-left
text: 8, dy, "$B(8, 0)$", top-right
text: 0 - dx, 4, "$A(0, 4)$", center-left
text: 4 + dx, 2 + dy, "$M(4, 2)$", top-right
xmin: -1.5
xmax: 9
ymin: -1
ymax: 5 
axis: equal
:::




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at arealet $T$ av den fargelangte trekanten er gitt ved 

$$
T(a) = -\dfrac{1}{2}a^2 + 3a
$$
:::::::::::::


:::::::::::::{tab-item} b
Bestem det største arealet trekanten kan ha.


:::::::::::::


::::::::::::::

:::::::::::::::













