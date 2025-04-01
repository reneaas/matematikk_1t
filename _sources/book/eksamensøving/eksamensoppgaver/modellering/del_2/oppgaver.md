# Modellering (Del 2)

> Her kan du bruke digitale hjelpemidler som **CAS**, **graftegner** (Geogebra), **Python** og **regneark** til å løse oppgaver. 


:::::::::::::::{admonition} Oppgave 1 (Vår 2024)
---
class: check 
---
Tabellen nedenfor viser hvor mange bagetter en kantine har solgt hver av de siste sju ukene, og hvor stor overskudd salget har gitt.


| Solgte bagetter | 100 | 130 | 160 | 175 | 190 | 220 | 235 |
|------|---|---|---|---|---|---|---|
| Overskudd (kroner) | 1450 | 2300 | 3050 | 3365 | 3720 | 4140 | 4175 |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene ovenfor til å vise at funksjonen $O$ gitt ved 

$$
O(x) = -0.09x^2 + 51.04x - 2776.98
$$

er en god modell for hvor stort overskuddet en uke blir når kantinen produserer og selger $x$ bagetter i løpet av uken.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Først fyller vi inn datapunktene i et regneark:

:::{figure} ./oppgave_1/a/regneark.png
---
width: 30%
class: no-click
---
:::

Velger vi regresjonsanalyse og et polynom av grad $2$, får vi

:::{figure} ./oppgave_1/a/regresjonsmodell.png
---
width: 100%
class: no-click
---
:::

Vi kan altså se at 

$$
O(x) = -0.09x^2 + 51.04x - 2776.98
$$

er en god modell ut ifra regresjonsanalysen og datapunktene vi har brukt.

:::::

:::::::::::::

:::::::::::::{tab-item} b
Hvor mange bagetter må kantinen produsere og selge i løpet av en uke, ifølge modellen $O$, for at overskuddet skal bli størst mulig? 

Hvor stort blir dette overskuddet?

:::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $O$ vil ha et toppunkt siden $O$ er en andregradsfunksjon og ledende koeffisient er negativ. Da vil overskuddet blir størst mulig når $O'(x) = 0$. Vi løser likningen med CAS:

:::{figure} ./oppgave_1/b/sol.png
---
width: 100%
class: no-click
---
:::

som betyr at $O'(x) = 0$ når $x \approx 283.56$. Kantina må derfor produsere og selges ca. 284 bagetter for at overskuddet skal bli størst mulig.



:::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem stigningstallet til den rette linjen som går gjennom punktene $(100, O(100))$ og $(200, O(200))$. Gi en praktisk tolkning av svaret du får.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bestemmer stigningstallet til linja gjennom punktene $(100, O(100))$ og $(200, O(200))$ ved å regne ut den gjennomsnittlige vekstfarten til $O$ i intervallet $[100, 200]$. Dette gjør vi direkte med CAS:

:::{figure} ./oppgave_1/c/sol.png
---
width: 100%
class: no-click
---
:::

som gir oss ca. 24 kr per bagett. Den praktiske tolkning av tallet er at dersom kantina øker antall bagetter de produserer og selger fra $100$ til $200$, så vil overskuddet øke med ca $24$ kr per bagett i gjennomsnitt. 

:::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem den momentane vekstfarten når $x = 235$. Gi en praktisk tolkning av svaret du får.


::::{admonition} Løsning
---
class: solution, dropdown
---
Den momentane vekstfarten til $O$ i $x = 235$ er $O'(235)$. Vi regner ut dette med CAS:

:::{figure} ./oppgave_1/d/sol.png
---
width: 100%
class: no-click
---
:::

som gir at $O'(235) \approx 8.74$ kr per bagett. Den praktiske tolkningen av dette tallet er at dersom kantina øker antall bagetter de produserer og selger fra $235$ til $236$, så vil overskuddet øke med ca $8.74$ kr.
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 2 (Vår 2024)
---
class: check
---
Lufttrykk måles ofte i hektopascal (hPa). Jo høyere over havet vi befinner oss, jo lavere er lufttrykket. Lufttrykket ved havets overflate er ca. 1000 hPa.


Når lufttrykket er lavere enn 1000 hPa, vil kokepunktet for vann være lavere enn $100 \degree \mathrm{C}$. Se tabellen nedenfor.

| Lufttrykk $\left(\mathrm{hPa}\right)$ | Kokepunkt for vann $\left(\degree \mathrm{C}\right)$ |
|------|---|
| $1000$ | $100$ |
| $500$ | $81.4$ |
| $200$ | $60.1$ |
| $80$ | $41.5$ |
| $40$ | $29$ |


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


::::{admonition} Løsning
---
class: solution, dropdown
---
Først fyller vi inn datapunktene i et regneark:

:::{figure} ./oppgave_2/a/regneark.png
---
width: 30%
class: no-click
---
:::

deretter bruker vi regresjonsanalyse og velger **potens** som modellklasse:

:::{figure} ./oppgave_2/a/regresjonsmodell.png
---
width: 100%
class: no-click
---
:::

Modellen vår $K$ er derfor gitt ved 

$$
K(x) = 7.6 \cdot x^{0.38}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Nedenfor vises en samtale mellom to elever:

Ari 
: Betyr dette at det ikke går an å få egg hardkokte oppe på et høyt fjell? 
: Et egg blir ikke hardkokt dersom temperaturen i vannet er lavere enn $85 \, \degree \mathrm{C}$.

Lisa
: Det kommer vel an på hvor høyt fjellet er?

Ari
: Jeg vil lage en modell som viser hvor høyt lufttrykket er $x$ kilometer over havets overflate. Jeg har lært at lufttrykket minker med ca. $12 \, \%$ per km. 

Lisa
: Jeg har lært at lufttrykket halveres for hver $5.5$ km. Jeg vil ta utgangspunkt i dette og lage en modell på samme form som den du lager, Ari.

---

**Lag modellene for Ari og Lisa.**

::::{admonition} Løsning
---
class: solution, dropdown
---
Modellen til Ari er en eksponentiell modell der vekstfaktoren er $0.88$ siden det er $12 \%$ nedgang per kilometer. Vi kaller modellen for $A$. Da har vi at 

$$
A(x) = 1000 \cdot 0.88^x
$$

siden $x$ er antall kilometer over havet og lufttrykket er $1000 hPa$ ved havnivå.


Modellen til Lisa er også en eksponentiell modell der vi vet at lufttrykket halveres for hver $5.5$ km. Vi lar $L$ være modellen til Lisa. Da har vi at 

$$
L(x) = 1000 \cdot b^x
$$

Siden lufttrykket halveres for hver $5.5$ km, betyr det at 

$$
L(5.5) = 500. 
$$

Vi må bestemme $b$ slik at dette stemmer. Vi gjør det med CAS:

:::{figure} ./oppgave_2/b/sol_lisa.png
---
width: 100%
class: no-click
---
:::

Vi ser at $b \approx 0.88$ akkurat som i Ari sin modell. Det er altså ingen nevneverdig forskjell mellom de to modellene, de er bare beskrevet på forskjellig måte.
::::

:::::::::::::


:::::::::::::{tab-item} c
Omtrent hvor høyt over havet er det mulig å få egg hardkokte?


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi finner først ut hvilket lufttrykk $x$ som gir $K(x) = 85$. Vi løser likningen med CAS:

:::{figure} ./oppgave_2/c/sol_del1.png
---
width: 100%
class: no-click
---
:::

som betyr at vi må ha et lufttrykk på omtrent $574.76$ hPa. Vi kan så bestemme ved hvilken høyde over havet dette lufttrykket er ved å bruke Ari sin modell i CAS:


:::{figure} ./oppgave_2/c/sol_del2.png
---
width: 100%
class: no-click
---
:::

som forteller oss at kokepunktet er på $85 \degree \mathrm{C}$ når vi er omtrent $4.3$ km over havet. Dermed er dette den størst høyden vi kan være på for å kunne lage hardkokte egg.

:::::



:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 3 (Høst 2024)
---
class: check
---
Funksjonen $P$ gitt ved 

$$
P(x) = 3600 \cdot 0.85^x + 600
$$


er en modell som viser hvor mange personer som abonnerte på papirutgaven av en avis $x$ år etter 2010. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis hvordan du på to ulike måter kan finne ut hvor mange person som abonnerte på papirutgaven av avisen i 2010. 

:::::::::::::


:::::::::::::{tab-item} b
Bestem stigningstallet til den rette linjen som går gjennom punktene $(4, P(4))$ og $(14, P(14))$. Gi en praktisk tolkning av svaret du får.

:::::::::::::

:::::::::::::{tab-item} c
Bestem den momentane vekstfarten når $x = 10$. Gi en praktisk tolkning av svaret du får.

:::::::::::::


:::::::::::::{tab-item} d
I 2019 abonnerte 1000 personer på den digitale utgaven av avisen. Antallet personer som abonnerte på den digitale utgaven, økte med $5.5 \%$ hvert år fra 2019 til 2024.


I hvilket år var det for første gang flere personer som abonnerte på den digitale utgaven av avisen enn på papirutgaven?

:::::::::::::

::::::::::::::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 4 (Høst 2023)
---
class: check
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


:::::::::::::::{admonition} Oppgave 5 (Høst 2023)
---
class: check
---
Tabellen nedenfor viser antall personer i Norge som hadde fiske som hovedyrke noen år i perioden 1952 - 2022.

| År | 1952 | 1982 | 1992 | 2002 | 2012 | 2022 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Antall fiskere** | 65 956 |25 289 | 19 780 | 13 841 | 9 825 | 9 591 |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
La $x$ være antall år etter 1950 og bruk opplysningene i tabellen til å bestemme en modell $F$ som du mener kan brukes til å si noe om antall personer som har hatt fiske som hovedyrke i perioden 1952 - 2022.

:::::::::::::

:::::::::::::{tab-item} b
Hvor mange personer i Norge vil i 2050 ha fiske som hovedyrke ifølge modellen fra oppgave **a**? Vurder modellens gyldighetsområde.

:::::::::::::

::::::::::::::

:::::::::::::::


















