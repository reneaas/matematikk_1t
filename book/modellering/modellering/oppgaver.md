# Oppgaver: Modeller


:::{margin} Tips: Oppgave 1 
I oppgaver hvor du skal vise at modell er en god modell, så er det ofte lurt å bare utføre regresjon med datamateriale du har fått og velge den samme modelltypen som er oppgitt.

---

For å lage en polynomfunksjon som en regresjonsmodell, kan du bruke `RegPoly(data, polynomgrad)`. 
:::

:::::::::::::::{exercise} Oppgave 1

:::{cas-popup}
:::

Tabellen nedenfor viser hvor mange bagetter en kantine har solgt hver av de siste sju ukene, og hvor stort overskudd salget har gitt.

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
Vi bruker regresjon med en polynomfunksjon av grad $2$ siden den oppgitte modellen er en andregradsfunksjon:

:::{figure} ./figurer/oppgaver/oppgave_1/a/sol.png
---
class: no-click, adaptive-figure
width: 100%
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

:::{figure} ./figurer/oppgaver/oppgave_1/b/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

som betyr at $O'(x) = 0$ når $x \approx 283.56$. Kantina må derfor produsere og selges ca. 284 bagetter for at overskuddet skal bli størst mulig. Vi ser at overskuddet da er 

$$
O(283.56) \approx 4459 \, \text{kr}
$$



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
class: no-click, adaptive-figure
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
class: no-click, adaptive-figure
---
:::

som gir at $O'(235) \approx 8.74$ kr per bagett. Den praktiske tolkningen av dette tallet er at dersom kantina øker antall bagetter de produserer og selger fra $235$ til $236$, så vil overskuddet øke med ca $8.74$ kr.
::::

:::::::::::::

::::::::::::::

:::::::::::::::