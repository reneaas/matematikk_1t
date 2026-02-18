# Potensfunksjoner

:::::{admonition} Læringsmål
---
class: tip
---
* Kan beskrive egenskapene til potensfunksjoner og bruke dem til å belyse praktiske situasjoner.
:::::

Potensfunksjoner brukes for å beskrive en sammenheng der en størrelse $y$ er proporsjonal eller omvendt proporsjonal med en potens av en annen størrelse $x$. Det viser seg at svært mange situasjoner i naturvitenskapene kan beskrives av potensfunksjoner. 


:::::::::::::::{admonition} Potensfunksjoner
---
class: summary
---
En potensfunksjon $f$ er en funksjon på formen

$$
f(x) = a \cdot x^b 
$$

der $a, b \in \mathbb{R} \setminus \{0\}$ er konstanter. I figuren nedenfor vises ulike potensfunksjoner for ulike verdier av $b$. 

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
name: fig-potensfunksjoner-teori-graf
width: 90%
class: no-click, adaptive-figure
---
viser grafene til potensfunksjoner med samme verdi av $a$, men ulike verdier av $b$. 
:::

:::::::::::::::

---

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Nedenfor vises noen eksempler på potensfunksjoner.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} Funksjon 1

$$
f(x) = 2 \cdot x^3
$$

:::{figure} ./figurer/eksempler/eksempel_2/funksjon_1.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{tab-item} Funksjon 2

$$
f(x) = 3 \cdot x^{1/2} = 3 \sqrt{x}
$$

:::{figure} ./figurer/eksempler/eksempel_2/funksjon_2.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{tab-item} Funksjon 3

$$
f(x) = 10 \cdot x^{-2} = \frac{10}{x^2}
$$

:::{figure} ./figurer/eksempler/eksempel_2/funksjon_3.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


:::::::::::::

::::::::::::::

:::::::::::::::


---


## Modellering med potensfunksjoner

Potensfunksjoner er godt egnet for situasjoner der en størrelse er proporsjonal med en potens av en annen størrelse. I neste eksempel skal vi se på en slik situasjon. 


:::::::::::::::{admonition} Eksempel 3
---
class: example 
---
:::{figure} ./figurer/eksempler/eksempel_3/planetbane.svg
---
width: 55%
class: no-click, adaptive-figure
align: right
---
:::

Perioden til en planet er tiden det tar for en planet å gjennomføre et fullt omløp i banen sin rundt solen. 

Nedenfor vises en tabell over periodene til noen av planetene i solsystemet og deres avstand til solen. Avstandene er gitt i astronomiske enheter (AU) som er avstanden fra solen til jorden.

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

Lag en modell $P$ som gir perioden til en planet i $P(x)$ år når avstanden til solen er $x$ AU på formen 

$$
P(x) = a \cdot x^b
$$

::::::::::::::{admonition} Løsning
---
class: solution
---


````{tab} Geogebra

<br>

:::{raw} html
---
file: ./ggb/eksempler/eksempel_3/eksempel_3.html
---
:::

````


````{tab} Python 

<br>

:::{raw} html
---
file: ./python/eksempler/eksempel_3.html
---
:::

````


::::::::::::::
:::::::::::::::


