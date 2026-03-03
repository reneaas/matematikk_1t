# Oppgaver: Potensfunksjoner


:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I figuren nedenfor vises grafene til potensfunksjonene

$$
f(x) = x^2 \qog g(x) = x^{1/2} \qog h(x) = x^{-1}
$$

Koble sammen riktig funksjon med riktig graf.


:::{plot}
nocache:
width: 70%
function: x**2, (0, 6), A, blue
function: x**-1, (0, 6), B, red
function: x**0.5, (0, 6), C, green
xmin: 0
ymin: 0
:::



::::{admonition} Fasit
---
class: answer, dropdown
---
* Graf A tilhører $f$.
* Graf B tilhører $h$.
* Graf C tilhører $g$.
::::


:::::::::::::


:::::::::::::{tab-item} b
I figuren nedenfor vises grafene til potensfunksjonene

$$
f(x) = x^{-1} \quad\quad g(x) = 2\cdot x^{-1} \quad\quad h(x) = 4 \cdot x^{-2}
$$

Koble sammen riktig funksjon med riktig graf.


:::{plot}
nocache: 
width: 70%
function: 4 * x**-2, (0, 5), A, blue
function: x**-1, (0, 5), B, red
function: 2 * x**-1, (0, 5), C, teal
xmin: 0
ymin: 0
xmax: 5
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
* Graf A tilhører $h$.
* Graf B tilhører $f$.
* Graf C tilhører $g$.
::::

:::::::::::::


:::::::::::::{tab-item} c
I figuren nedenfor vises grafene til tre funksjoner gitt ved

$$
f(x) = x^{1/3} \quad\quad g(x) = 2 x^{1/2} \quad\quad h(x) = 2 x^{2/3}
$$

Koble sammen riktig funksjon med riktig graf.


:::{plot}
width: 70%
function: 2 * x**(2/3), (0, 6), A, blue
function: x**(1/3), (0, 6), B, red
function: 2 * x**(1/2), (0, 6), C, teal
xmin: 0
ymin: 0
xmax: 5
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
* Graf A tilhører $h$.
* Graf B tilhører $f$.
* Graf C tilhører $g$.
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
En kule med radius $r$ har et overflatearealet $A \propto r^2$.

Hvor mange ganger større blir overflatearealet radius dobles?


::::{answer}
$4$ ganger større.
::::
:::::::::::::

:::::::::::::{tab-item} b
En kule med radius $r$ har et volum $V \propto r^3$.

Hvor mange ganger større blir volumet dersom radius dobles?

::::{answer}
$8$ ganger større.
::::
:::::::::::::



:::::::::::::{tab-item} c
Forholdet mellom volumet og overflatearealet til en kule er $\dfrac{V}{A}$. 

Hvor mange ganger større blir dette forholdet dersom radius firedobles?

::::{answer}
$4$ ganger større.
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
Den elektriske kraften $F$ mellom to elektriske ladninger oppfyller $F \propto r^{-2}$ der $r$ er avstanden mellom de to elektriske ladningene. 

Hvor mange ganger svakere blir kraften dersom avstanden mellom ladningene blir tre ganger så stor?

::::{answer}
$\dfrac{1}{9}$ svakere.
::::
:::::::::::::


:::::::::::::{tab-item} b
Tyngdekraften $G$ mellom to planeter er $G \propto r^{-2}$ der $r$ er avstanden mellom de to planetene.

Hvor mange ganger sterkere blir tyngdekraften dersom avstanden mellom de to planetene halveres? 

::::{answer}
$4$ ganger sterkere.
::::

:::::::::::::


:::::::::::::{tab-item} c
Bevegelsesenergien $E$ til en stein med fart $v$ tilfredsstiller $E \propto v^2$.


Hvor manger ganger større blir bevegelsesenergien dersom farten blir fire ganger så stor?

::::{answer}
$16$ ganger så stor.
::::


:::::::::::::


::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 4

:::{plot}
nocache:
figsize: (3, 3)
width: 60%
axis: off
axis: equal
align: left
let: r = 1
let: dr = 1.2
let: R = 2
let: v = pi/4
circle: (0, 0), r, solid, orange, fill
circle: (0, 0), R, dashed, gray
text: 0, 0, "Sola", center-center
circle: (R * cos(v), R * sin(v)), 0.3, solid, teal, fill
text: R * cos(v), R * sin(v), "Planet", top-right
vector: R * cos(v), R * sin(v), -dr * sin(v), dr * cos(v), black
:::

:::{cas-popup}
---
layout: sidebar
---
:::



:::{clear}
:::

Perioden til en planet er tiden det tar for planeten å gjennomføre en runde rundt solen. 

Nedenfor vises en tabell over periodene til noen av planetene i solsystemet vårt og deres avstand til solen. Avstandene er gitt i astronomiske enheter (AU) der $1 \text{ AU} = 149.6$ millioner km er avstanden fra jorden til solen.


:::{table}
labels: Planet, Avstand (AU), Periode (År)
Merkur, 0.39, 0.24
Venus, 0.72, 0.62
Mars, 1.52, 1.88
Jupiter, 5.20, 11.86
Saturn, 9.58, 29.46
:::




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell på formen

$$
P(x) = a \cdot x^b
$$

som viser sammenhengen mellom perioden $P(x)$ i år og avstanden $x$ i AU. 


::::{solution}
Vi utfører regresjon med en potensmodell:


:::{figure} ./figurer/oppgaver/2/a/regresjon.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Altså er modellen vår

$$
P(x) = 1 \cdot x^{1.5}
$$

::::

:::::::::::::



:::::::::::::{tab-item} b
Hva er perioden til jorda, ifølge modellen din? 



::::{solution}
Jorden er en avstand $x = 1$ AU fra solen. Dermed er perioden til jorden gitt ved $P(1)$. Vi regner ut og bruker {ggb-icon}`mode_numeric` for å få en numerisk verdi:

:::{figure} ./figurer/oppgaver/2/b/sol.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Altså er $P(1) \approx 1$ år som stemmer overens med det vi vet om jorden.

::::
:::::::::::::


:::::::::::::{tab-item} c
Neptun er den planeten som ligger lengst unna solen med en avstand på ca. $30.1 \, \mathrm{AU}$. 

Hvor lang tid bruker Neptun på én runde rundt solen, ifølge modellen din? 


::::{solution}
Siden Neptun ligger $30.1$ AU fra solen, så er $x = 30.1$. Perioden er da gitt ved $P(30.1)$. Vi regner ut og bruker {ggb-icon}`mode_numeric` for å få en numerisk verdi:


:::{figure} ./figurer/oppgaver/2/c/sol.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Altså bruker Neptun ca. 167 år på én runde rundt solen, ifølge modellen vår. 


::::
:::::::::::::


:::::::::::::{tab-item} d
Pluto er en dvergplanet som bruker hele 247.94 år på én runde rundt solen.

Hvor langt unna solen er Pluto, ifølge modellen din? 

:::::::::::::


:::::::::::::{tab-item} e
Johannes Kepler var en astronom som levde rundt år 1600. Han oppdaget en lov som vi i dag kaller for Keplers 3.lov:

> For perioden $P$ og avstanden $x$ til en planet, så er $P^2$ proporsjonal med $x^3$. Det betyr at det finnes en konstant $k$ slik at $P^2 = k \cdot x^3$.


Undersøk om modellen din stemmer med Keplers 3.lov.

:::::::::::::



::::::::::::::
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
figsize: (3, 3)
align: left
axis: off
axis: equal
width: 70%
let: v = pi / 6
let: u = -pi / 6
let: l = 3
let: dr = 0.5
let: L = 3
line-segment: (-L, 0), (L, 0), solid, gray
line-segment: (0, 0), (l * sin(v), -l * cos(v)), solid, blue
circle: ((l + dr) * sin(v), -(l + dr) * cos(v)), dr, solid, red, fill
line-segment: (0, 0), (l * sin(u), -l * cos(u)), dashed, blue
circle: ((l + dr) * sin(u), -(l + dr) * cos(u)), dr, dashed, red, fill
angle-arc: (0, 0), l + dr, 270 + 30, 270 - 30, dashed, gray 
text: 0.5 * l, -0.5 * l, "$\ell$", top-right
point: (0, 0)
:::


:::{clear}
:::

Tiden det tar for en pendel å svinge frem og tilbake én gang kalles for perioden til pendelen.


I tabellen nedenfor vises perioden til en pendel for ulike snorlengder $\ell$. 


:::{table}
---
transpose:
---
labels: Snorlengde (meter), Periode (sekunder)
0.1, 0.69
0.3, 1.17
0.5, 1.44
0.8, 1.82
1.0, 2.08
1.3, 2.27
1.6, 2.53
2.0, 2.80
:::




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell $T$ på formen

$$
T(x) = a \cdot x^{b}
$$

der $T(x)$ er perioden i sekunder for en pendel med en snorlengde på $x$ meter.

:::::::::::::


:::::::::::::{tab-item} b
Hva er perioden til en pendel med en snorlengde på $1.5$ meter, ifølge modellen din?



:::::::::::::


:::::::::::::{tab-item} c


På Universitetet i Oslo, er en såkalt **Foucaults pendel** bygget for å demonstrere at jorden roterer. Pendelen sin periode er omtrent på $7.5$ sekunder. Pendelen er ca. $20$ cm over bakken på sitt laveste.

Hvor høyt er taket over bakken der pendelen henger?


:::{figure} ./bilder/oppgaver/oppgave_3/pendel.jpeg
---
class: no-click
width: 50%
align: right
---
:::
:::::::::::::


:::::::::::::{tab-item} d
Fra fysikken, er perioden $T$ til en pendel med snorlengde $L$ omtrentlig gitt ved formelen

$$
T = 2\pi \sqrt{\dfrac{L}{g}}
$$

der $g = 9.82 \, \mathrm{m/s^2}$ (meter per sekund per sekund) er tyngdeakselerasjonen i Oslo.

Undersøk om modellen din samsvarer med denne formelen.

:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6

:::{cas-popup}
---
layout: sidebar
---
:::


:::{plot}
width: 70%
align: left
figsize: (3, 3)
axis: off
axis: equal
let: r = 0.5
let: h = 3
let: L = 2
line-segment: (-L, 0), (L, 0), solid, gray
line-segment: (0, h), (0, r), dashed, gray
circle: (0, h), r, solid, blue, fill
circle: (0, r), r, dashed, blue, fill
text: 0, 0, "Bakken", bottom-center
vector: 2*r, h, 0, -2*r
text: -2*r, h, "Kule", center-left
:::


:::{clear}
:::


Når en kule blir sluppet fra forskjellige høyder, vil det ta lenger og lenger tid før kulen treffer bakken.

I tabellen nedenfor vises tiden det tar for en kule å treffe bakken når den slippes fra ulike høyder.

:::{table}
---
transpose:
---
labels:  Høyde (meter), Tid (sekunder)
0.5, 0.32
1.0, 0.47
1.5, 0.58
2.0, 0.63
2.5, 0.72
3.0, 0.82
:::




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell $T$ på formen

$$
T(x) = a \cdot x^{b}
$$

der $T(x)$ er tiden i sekunder det tar for en kule å treffe bakken når den slippes $x$ meter over bakken.

:::::::::::::



:::::::::::::{tab-item} b
Hvor lang tid tar det før en kule treffer bakken dersom den slippes fra $10$ meter, ifølge modellen?


:::::::::::::


:::::::::::::{tab-item} c
En kule ble sluppet fra en bro og traff bakken etter $3$ sekunder.

Hvor høy var broen?


:::::::::::::


:::::::::::::{tab-item} d
En modell fra fysikken forutsier at tiden $t$ det tar for en kule å treffe bakken når den slippes fra en høyde $h$ er gitt ved formelen

$$
t = \sqrt{\dfrac{2h}{g}}
$$

der $g = 9.82 \, \mathrm{m/s^2}$ (meter per sekund per sekund) er tyngdeakselerasjonen i Oslo.

Undersøk om modellen din samsvarer med denne formelen.

::::::::::::::


:::::::::::::::
