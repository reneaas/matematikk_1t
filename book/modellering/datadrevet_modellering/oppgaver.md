# Oppgaver: Datadrevet modellering



:::::::::::::::{exercise} Oppgave 1
---
aids: true
---
Tabellen nedenfor viser hvor mange bagetter en kantine har solgt hver av de siste sju ukene, og hvor stort overskudd salget har gitt


:::{table}
---
transpose:
---
labels: Solgte bagetter, Overskudd (kroner)
100, 1450
130, 2300
160, 3050
175, 3365
190, 3720
220, 4140
235, 4175
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene ovenfor til å vise at funksjonen $O$ gitt ved 

$$
O(x) = -0.09x^2 + 51.04x - 2776.98
$$

er en god modell for hvor stort overskuddet blir en i løpet av en uke når kantinen produserer og selger $x$ bagetter i løpet av uka.

:::::::::::::


:::::::::::::{tab-item} b
Hvor mange bagetter må kantinen produsere og selge i løpet av en uke for at overskuddet skal bli størst mulig, ifølge modellen?

Hvor stor blir dette overskuddet?
:::::::::::::


:::::::::::::{tab-item} c
Bestem stigningstallet til den rette linjen som går gjennom punktene $(100, O(100))$ og $(200, O(200))$. 

Gi en praktisk tolkning av svaret.
:::::::::::::


:::::::::::::{tab-item} d
Bestem den momentane vekstfarten når $x = 235$. 

Gi en praktisk tolkning av svaret.
:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
---
aids: true
---

:::{plot}
figsize: (3, 3)
width: 60%
axis: off
axis: equal
align: right
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

Perioden til en planet er tiden det tar for planeten å gjennomføre en runde rundt solen. 

Nedenfor vises en tabell over periodene til noen av planetene i solsystemet vårt og deres avstand til solen. Avstandene er gitt i astronomiske enheter (AU) der $1 \text{ AU} = 149.6$ millioner km er avstanden fra jorden til solen.


:::{clear}
:::

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


:::::::::::::



:::::::::::::{tab-item} b
Hva er perioden til jorda, ifølge modellen din? 


:::::::::::::


:::::::::::::{tab-item} c
Neptun er den planeten som ligger lengst unna solen med en avstand på ca. $30.1 \, \mathrm{AU}$. 

Hvor lang tid bruker Neptun på én runde rundt solen, ifølge modellen din? 


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





:::::::::::::::{exercise} Oppgave 3
---
aids: true
---

Tabellen nedenfor viser antallet registrerte tilfeller av kikhoste i Norge noen måneder i perioden januar 2023 - oktober 2024.


:::{table}
---
transpose:
---
labels: Måned, Antall registrerte tilfeller
Januar 2023, 29
Mai 2023, 93
Oktober 2023, 164
Februar 2024, 284
August 2024, 1035
Oktober 2024, 1657
:::


<br>


La $x$ være antall måneder etter desember 2022, det vil si at $x = 1$ tilsvarer januar 2023, $x = 3$ tilsvarer mars 2023, og så videre.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene ovenfor til å vise at funksjonen $K$ gitt ved 

$$
K(x) = 27.8 \cdot 1.2^x
$$

er en god modell for antall registrerte tilfeller av kikhoste i Norge i perioden januar 2023 - oktober 2024.



:::::::::::::


:::::::::::::{tab-item} b
Bestem stigningstallet til den rette linjen som gjennom punktene $(4, K(4))$ og $(21, K(21))$. <br> Gi en praktisk tolkning av svaret du får.


:::::::::::::


:::::::::::::{tab-item} c
Hvor mange tilfeller av kikhoste vil bli registrert i Norge i mai 2025 ifølge modellen?



:::::::::::::

::::::::::::::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 4
---
aids: true
---


En fabrikk har en vanntank. Vannet i tanken skal tappes ut.

Anta at funksjonen $V$ gitt ved 

$$
V(x) = 2000 - 2000\cdot \left(1 - \dfrac{x}{40}\right)^2 \, , \quad 0 \leq x \leq 40
$$

kan brukes som en modell for hvor mange liter vann $V(x)$ som er tappet ut av tanken $x$ minutter etter tappingen startet.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $V(0)$. Gi en praktisk tolkning av svaret.



:::::::::::::


:::::::::::::{tab-item} b
Bestem verdimengden til $V$.



:::::::::::::


:::::::::::::{tab-item} c
Hvor lang tid vil det ta før halvparten av vannet er tappet ut av tanken?


:::::::::::::


:::::::::::::{tab-item} d
Bestem stigningstallet til den rette linjen som går gjennom punktene $(0, V(0))$ og $(30, V(30))$. Gi en praktisk tolkning av svaret du får. 


:::::::::::::


:::::::::::::{tab-item} e
Undersøk om det noen gang vil tappes ut mer enn 105 liter vann i løpet av ett minutt.



:::::::::::::

::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5
---
aids: true
---

En gruppe statistikere har sett på hvordan folketallet i et område har endret seg siden 1960, og laget en modell $F$ gitt ved 

$$
F(x) = \dfrac{1}{1000}\cdot \left(0.027 x^3 - 5.8 x^2 + 220x + 7900\right), \quad x \in [0, 80]
$$

for folketallet $F(x)$ tusen innbyggere i området $x$ år etter 1960.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis hvordan du på to ulike måter kan bestemme når folketallet var høyest ifølge modellen.


:::::::::::::


:::::::::::::{tab-item} b
Bestem stigningstallet til den rette linjen som går gjennom punktene $(30, F(30))$ og $(70, F(70))$. Gi en praktisk tolkning av dette stigningstallet.


:::::::::::::


:::::::::::::{tab-item} c
Når vil folketallet avta raskest ifølge modellen? 



:::::::::::::

::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6
---
aids: true
---

Strømmen som holder vannet i et hagebasseng varmt, blir slått av.

Anta at funksjonen $T$ gitt ved 

$$
T(x) = 3.5 + 34.5 \cdot 0.87^x,  \quad x \geq 0
$$

kan brukes som en modell for temperaturen $T(x) \degree \mathrm{C}$ i vannet $x$ timer etter at strømmen er slått av.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hva er temperaturen i vannet når strømmen blir slått av?


:::::::::::::


:::::::::::::{tab-item} b
Hvor lang tid vil det ta før temperaturen i vannet er under $20\degree \mathrm{C}$?


:::::::::::::


:::::::::::::{tab-item} c
Bestem stigningstallet til den rette linjen som går gjennom punktene $(0, T(0))$ og $(4, T(4))$. 

Gi en praktisk tolkning av svaret.
:::::::::::::


:::::::::::::{tab-item} d
Vil temperaturen i vannet noen gang synke med mer enn $5\degree\mathrm{C}$ i løpet av én time?

:::::::::::::


:::::::::::::{tab-item} e
Gi en praktisk tolkning av tallet $3.5$ i modellen.


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
---
aids: true
---

Lufttrykk måles ofte i hektopascal (hPa). Jo høyere over havet vi befinner oss, jo lavere er lufttrykket. Lufttrykket ved havets overflate er ca. 1000 hPa.


Når lufttrykket er lavere enn 1000 hPa, vil kokepunktet for vann være lavere enn $100 \degree \mathrm{C}$. Se tabellen nedenfor.

:::{table}
---
transpose:
---
labels: Lufttrykk (hPa), Kokepunkt for vann ($\mathrm{^\circ C}$)
1000, 100
500, 81.4
200, 60.1
80, 41.5
40, 29
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en modell $K$ på formen 

$$
K(x) = a \cdot x^b
$$

som tilnærmet viser sammenhengen mellom lufttrykket $x$ hPa og kokepunktet $K(x) \, \degree \mathrm{C}$. 


:::::::::::::

:::::::::::::{tab-item} b
Nedenfor vises en samtale mellom to elever.

:::{dialogue}
---
name1: Ari
name2: Lisa
speaker1: left
speaker2: right
---
Ari: Et egg blir ikke hardkokt dersom temperaturen i vannet er lavere enn $85 \, \degree\mathrm{C}$. Betyr det at det ikke går an å få egg hardkokte på et høyt fjell?
Lisa: Det kommer vel an på hvor høyt fjellet er?
Ari: Jeg vil lage en modell som viser hvor høyt lufttrykket er $x$ kilometer over havets overflate. Jeg har lært at lufttrykket minker med ca. $12 \, \%$ per km.
Lisa: Jeg har lært at lufttrykket halveres for hver $5.5$ km. Jeg vil ta utgangspunkt i dette og lage en modell på samme form som den du lager, Ari.
:::

<br>

Lag modellen til Ari og Lisa.



:::::::::::::


:::::::::::::{tab-item} c
Omtrent hvor høyt over havet er det mulig å få egg hardkokte?




:::::::::::::

::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 8
---
aids: true
---


Sofie og Malene dro på hyttetur, og da de ankom hytta, var temperaturen i stua $2.0 \degree \mathrm{C}$. De skrudde på varmen stilte termostaten på $20 \degree \mathrm{C}$. 

Tabellen nedenfor viser temperaturen i stua $x$ minutter etter at de skrudde på varmen.


:::{table}
---
transpose:
---
labels: Tid (minutter), Temperatur ($\mathrm{^\circ C}$)
1, 2.0
5, 3.7
10, 5.3
20, 8.0
30, 10.2
50, 13.4
80, 16.4
120, 18.4
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell på formen

$$
T(x) = a \cdot b^x 
$$

som gir temperaturen $T(x)$ i grader Celsius i stua $x$ minutter etter at varmen er skrudd på.
:::::::::::::



:::::::::::::{tab-item} b
Anslå gyldighetsområdet til modellen $T$.
:::::::::::::



:::::::::::::{tab-item} c
Sofie og Malene har fått en annen idé.


:::{dialogue}
---
name1: Sofie
name2: Malene
speaker1: left
speaker2: right
---
Sofie: Jeg tror kanskje det er bedre å velge en modell på formen $T(x) = a \cdot b^x + c$ siden temperaturen skal nærme seg $20 ^\circ \mathrm{C}$ etter hvert.
Malene: Men det får vi jo ikke laget med regresjon i Geogebra.
Sofie: Sant, men $T(x) - c = a \cdot b^x$ er jo en eksponentialfunksjon, og det kan vi jo lage med regresjon i Geogebra.
Malene: Ah, da kan vi jo bare trekke fra verdien til $c$ fra temperaturene i tabellen.
Sofie: Og så bare plusser vi på $c$ igjen på modellen vår etterpå. Det er jo smart! 
Malene: Men hva er verdien til $c$? Hmm..
:::

<br>

Ta utgangspunkt i diskusjonen til Sofie og Malene og lag en modell på formen 

$$
T(x) = a \cdot b^x + c
$$



:::::::::::::



::::::::::::::


:::::::::::::::