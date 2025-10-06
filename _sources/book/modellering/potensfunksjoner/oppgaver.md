# Oppgaver: Potensfunksjoner


:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I figuren nedenfor vises grafene til potensfunksjonene

$$
f(x) = x^2 \qog g(x) = x^{0.5} \qog h(x) = x^{-1}
$$

Koble sammen riktig funksjon med riktig graf.

:::{figure} ./figurer/oppgaver/oppgave_1/a.svg
---
width: 80%
class: no-click, adaptive-figure
---
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

:::{figure} ./figurer/oppgaver/oppgave_1/b.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafene til tre funksjoner.
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

:::{figure} ./figurer/oppgaver/oppgave_1/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafene til tre funksjoner.
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

::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2

:::{cas-popup}
---
layout: sidebar
---
:::



:::{figure} ./figurer/oppgaver/oppgave_2/figur.svg
---
width: 70%
class: no-click, adaptive-figure
align: left
---
:::


:::{clear}
:::

Perioden til en planet er tiden det tar for planeten å gjennomføre en full rundtur rundt solen. 

Nedenfor vises en tabell over periodene til noen av planetene i solsystemet vårt og deres avstand til solen. Avstandene er gitt i astronomiske enheter (AU) der $1 \text{ AU} = 149.6 \text{ millioner km}$ er avstanden fra jorden til solen.

| Planet | Avstand (AU) | Periode (år) |
|--------|:--------------:|:--------------:|
| Merkur | 0.39         | 0.24         |
| Venus  | 0.72         | 0.62         |
| Mars   | 1.52         | 1.88         |
| Jupiter| 5.20         | 11.86        |
| Saturn | 9.58         | 29.46        |
<!-- | Uranus | 19.22        | 84.01        |
| Neptun | 30.05        | 164.79       | -->

<br>



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

:::::::::::::



:::::::::::::{tab-item} b
Hva er perioden til jorda, ifølge modellen din? 


:::::::::::::


:::::::::::::{tab-item} c
Neptun er den planeten som ligger lengst unna solen med en avstand på ca. $30.33 \, \mathrm{AU}$. 

Hvor lang tid bruker Neptun på én runde rundt solen, ifølge modellen din? 
:::::::::::::


:::::::::::::{tab-item} d
Pluto er en dvergplanet som bruker hele 247.94 år på én runde rundt solen.

Hvor langt unna solen er Pluto, ifølge modellen din? 

:::::::::::::


:::::::::::::{tab-item} e
Johannes Kepler var en astronom som levde rundt år 1600. Han oppdaget en lov som vi i dag kaller for Keplers 3.lov:

> For perioden $P$ og avstanden $x$ til en planet, så er $P^2$ proporsjonal med $x^3$. Det betyr at det finnes en konstant $k$ slik at $P^2 = k \cdot x^3$.


Undersøk om modellen din samsvarer med Keplers 3.lov.

:::::::::::::



::::::::::::::
:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 3

:::{cas-popup}
---
layout: sidebar
---
:::



:::{figure} ./figurer/oppgaver/oppgave_3/figur.svg
---
class: no-click, adaptive-figure
width: 100%
align: left
---
:::

:::{clear}
:::

Tiden det tar for en pendel å svinge frem og tilbake én gang kalles for perioden til pendelen.


I tabellen nedenfor vises perioden til en pendel for ulike snorlengder. 



|Snorlengde (meter)| $0.1$ | $0.3$ | $0.5$ | $0.8$ | $1.0$ | $1.3$ | $1.6$ | $2.0$ |
|:-------------------|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|**Periode (sekunder)** | $0.69$ | $1.17$ | $1.44$ | $1.82$ | $2.08$ | $2.27$ | $2.53$ | $2.80$ |



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


:::::::::::::::{exercise} Oppgave 4

:::{cas-popup}
---
layout: sidebar
---
:::


:::{figure} ./figurer/oppgaver/oppgave_4/figur.svg
---
class: no-click, adaptive-figure
width: 100%
align: left
---
:::

:::{clear}
:::


Når en kule blir sluppet fra forskjellige høyder, vil det ta lenger og lenger tid før kulen treffer bakken.

I tabellen nedenfor vises tiden det tar for en kule å treffe bakken når den slippes fra ulike høyder.


| Høyde (meter) | $0.5$ | $1.0$ | $1.5$ | $2.0$ | $2.5$ | $3.0$ |
|:--------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **Tid (sekunder)** | $0.32$ | $0.47$ | $0.58$ | $0.63$ | $0.72$ | $0.82$ |



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


---


:::::::::::::::{exercise} Oppgave 5

:::{cas-popup}
---
layout: sidebar
---
:::



For å sende raketter til verdensrommet, så må rakettene minst oppnå en bestemt fart for å unnslippe jordens tyngdefelt. Vi kaller denne farten for **unnslipningsfarten**. Farten er avhengig både av hvor tung en planet er og hvor stor radius planeten har. 

I tabellen nedenfor vises unnslipningsfarten for ulike planter i solsystemet vårt og hvor tunge planetene er i antall jordmasser. Det betyr at 1 jordmasse er like tung som jorden, 2 jordmasser er dobbelt så tungt som jorden, og 0.1 er $10\%$ av jordens tyngde.


| Masse (jordmasser) | 0.06 | 0.815 | 1.0 | 0.1075 | 317.8 |
|:--|:---:|:---:|:---:|:---:|:---:|
| Unnslipningsfart (km/s) | 4.26 | 10.38 | 11.20 | 5.04 | 60.32 |

:::::::::::::::