# Grafisk løsning

:::{admonition} Læringsmål
---
class: tip
---
* Kunne uttrykke mengden av flere deler av tallinja ved hjelp av ulikheter og intervaller.
* Kunne løse andregradsulikheter grafisk.
:::

Prinsippet bak løsning av andregradsulikheter grafisk er tilsvarende som de vi har brukt når vi jobbet med lineære ulikheter. Vi trenger imidlertid noen flere verktøy for å kunne uttrykke løsningene på en god måte. Derfor blir det først litt mer mengdelære her.

## Mengdelære
Vi trenger litt mer teori om mengder for å kunne uttrykke løsningene til ulikheter på en god måte.

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Med andregradsulikheter får vi ofte flere deler av tallinja som en løsning. Disse delene er ikke sammenhengende slik at vi får "hull" i tallinja vi må "ta bort". Da trenger vi skrivemåter for å uttrykke oss på en god måte.

Under vises tre forskjellige mengder på tallinja som vi uttrykker med ulik notasjon (skrivemåter).
Vi kan uttrykke mengden av $x$-verdier ved hjelp av ulikheter eller intervaller.

> Legg merke til at vi bruker symbolet "$\cup$" når vi vil si "eller" i forbindelse med intervaller, mens vi bruker symbolet "$\lor$" når vi vil si "eller" i forbindelse med ulikheter.

::::::::::::::{tab-set}
:::::::::::::{tab-item} Mengde 1

På tallinja i {numref}`fig-andregradsulikheter-eksempel-1-mengde-1` har vi markert to områder. 

Her tenker vi oss at endepunktene **ikke** er inkludert her.

::::::::::::{tab-set}
:::::::::::{tab-item} Ulikhet
$$
x < - 1 \, \lor \, x > 1
$$
:::::::::::

:::::::::::{tab-item} Intervall
$$
x \in \langle \gets, -1 \rangle \textcolor{red}{\cup} \langle 1, \to \rangle
$$

:::::::::::
::::::::::::


:::{figure} ./figurer/eksempler/eksempel_1/mengde_1.svg
---
name: fig-andregradsulikheter-eksempel-1-mengde-1
width: 100%
class: no-click, adaptive-figure
---
viser to områder på tallinja som er fargelagt med rød farge.
:::
:::::::::::::

:::::::::::::{tab-item} Mengde 2

På tallinja i {numref}`fig-andregradsulikheter-eksempel-1-mengde-2` har vi markert to områder. 

Her tenker vi oss at endepunktene **er inkludert**.

::::::::::::{tab-set}
:::::::::::{tab-item} Ulikhet
$$
x \leq -3 \, \lor \, x \geq 2
$$
:::::::::::

:::::::::::{tab-item} Intervall
$$
x \in \langle \gets, -3] \textcolor{red}{\cup}  [2, \to \rangle
$$
:::::::::::

::::::::::::


:::{figure} ./figurer/eksempler/eksempel_1/mengde_2.svg
---
name: fig-andregradsulikheter-eksempel-1-mengde-2
width: 100%
class: no-click, adaptive-figure
---
viser to områder på tallinja som er fargelagt med rød farge.
:::

:::::::::::::

:::::::::::::{tab-item} Mengde 3
På tallinja i {numref}`fig-andregradsulikheter-eksempel-1-mengde-3` har vi markert to områder. 

Her tenker vi oss at endepunktet $x = 1$ **er inkludert**, men $x = 4$ er **ikke inkludert**.

::::::::::::{tab-set}
:::::::::::{tab-item} Ulikhet
$$
x \leq 1 \, \lor \, x > 4
$$
:::::::::::

:::::::::::{tab-item} Intervall
$$
x \in \langle \gets, 1] \textcolor{red}{\cup} \langle 4, \to \rangle
$$
:::::::::::
::::::::::::


:::{figure} ./figurer/eksempler/eksempel_1/mengde_3.svg
---
name: fig-andregradsulikheter-eksempel-1-mengde-3
width: 100%
class: no-click, adaptive-figure
---
viser to områder på tallinja som er fargelagt med rød farge.
:::
:::::::::::::
::::::::::::::

Vi har også en alternativ og effektiv skrivemåte hvor vi tenker oss at vi tar hele tallinja og "kutter" vekk en del av den. Eksempelet under vises hvordan dette kan skrives:

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Vi bruker intervallene fra Eksempel 1 som utgangspunkt.

> Vi bruker symbolet "$\setminus$" for å si "uten". Dette "kutter" vekk en del av tallinja.

::::::::::::::{tab-set}
:::::::::::::{tab-item} Mengde 1


::::::::::::{tab-set}
:::::::::::{tab-item} Alternativ 1
$$
x \in \langle \gets, -1 \rangle \cup \langle 1, \to \rangle
$$
:::::::::::

:::::::::::{tab-item} Alternativ 2
$$
x \in \mathbb{R} \setminus [-1, 1]
$$

:::::::::::
::::::::::::

:::{figure} ./figurer/eksempler/eksempel_1/mengde_1.svg
---
name: fig-andregradsulikheter-eksempel-1-mengde-1-alternativ
width: 100%
class: no-click, adaptive-figure
---
viser to områder på tallinja som er fargelagt med rød farge.
:::

:::::::::::::

:::::::::::::{tab-item} Mengde 2

::::::::::::{tab-set}
:::::::::::{tab-item} Alternativ 1
$$
x \in \langle \gets, -3] \cup [2, \to \rangle
$$
:::::::::::

:::::::::::{tab-item} Alternativ 2
$$
x \in \mathbb{R} \setminus \langle-3, 2\rangle
$$
:::::::::::

::::::::::::

:::{figure} ./figurer/eksempler/eksempel_1/mengde_2.svg
---
name: fig-andregradsulikheter-eksempel-1-mengde-2-alternativ
width: 100%
class: no-click, adaptive-figure
---
viser to områder på tallinja som er fargelagt med rød farge.
:::

:::::::::::::

:::::::::::::{tab-item} Mengde 3

::::::::::::{tab-set}
:::::::::::{tab-item} Alternativ 1
$$
x \in \langle \gets, 1] \cup \langle 4, \to \rangle
$$
:::::::::::

:::::::::::{tab-item} Alternativ 2
$$
x \in \mathbb{R} \setminus \langle -1, 4]
$$
:::::::::::
::::::::::::

:::{figure} ./figurer/eksempler/eksempel_1/mengde_3.svg
---
name: fig-andregradsulikheter-eksempel-1-mengde-3-alternativ
width: 100%
class: no-click, adaptive-figure
---
viser to områder på tallinja som er fargelagt med rød farge.
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Ta quizen! Flere svaralternativer kan være riktige.

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::

:::::::::::::::



:::::::::::::::

## Ulikheter

Vi starter med å se på noen typiske eksempler i Utforsk 1.

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Under vises grafisk løsning av tre andregradsulikheter. 

::::::::::::::{tab-set}
:::::::::::::{tab-item} Eksempel 1
En ulikhet er gitt ved

$$
x^2 - 4x + 3 > 0. 
$$

{numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-1` viser grafen til $f(x) = x^2 - 4x + 3$. Vi er ute etter alle verdier for $x$ der grafen til $f$ ligger **over** $x$-aksen. 

Grafen til $f$ skjærer $x$-aksen i $x = 1$ og $x = 3$. Vi kan se at $f(x) > 0$ når $x < 1$ og $x > 3$. Derfor er løsningen til ulikheten

$$
x < 1 \, \lor \, x > 3 \quad \iff \quad x \in \langle \gets, 1 \rangle \cup \langle 3, \to \rangle
$$


:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-andregradsulikheter-grafisk-løsning-eksempel-1
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = x^2 - 4x + 3$. Løsningsmengden der grafen til $f$ ligger over $x$-aksen er fargelagt med rød farge.
:::


:::::::::::::

:::::::::::::{tab-item} Eksempel 2
En ulikhet er gitt ved

$$
-2x^2 + 4x + 4 > -2.
$$

{numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-2` viser grafene til $f(x) = -2x^2 + 4x + 4$ og linja $y = -2$. 

Vi er ute etter alle verdier for $x$ der grafen til $f$ ligger **over** linja $y = -2$. Dette kan vi se er tilfelle når $x < 0$ og $x > 2$. Derfor er løsningen til ulikheten

$$
x < 0 \, \land \, x > 2 \quad \iff \quad x \in \langle 0, 2 \rangle.
$$

::::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-andregradsulikheter-grafisk-løsning-eksempel-2
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = -2x^2 + 4x + 4$ og linja $y = -2$. Løsningsmengden til $f(x) > -2$ er markert i rødt på $x$-aksen.
::::

:::::::::::::

:::::::::::::{tab-item} Eksempel 3
En ulikhet er gitt ved 

$$
x^2 + 5x + 1 \leq -x - 4. 
$$

{numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-3` viser grafene til $f(x) = x^2 + 5x + 1$ og $g(x) = -x - 4$. 

Vi er ute etter alle verdier for $x$ der grafen til $f$ ligger **under eller på** grafen til $g$. Vi kan se at dette er tilfelle når $x \geq -5$ og $x \leq -1$. Derfor er løsningen til ulikheten

$$
x \geq -5 \, \land \, x \leq -1 \quad \iff \quad x \in [-5, -1].
$$

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-andregradsulikheter-grafisk-løsning-eksempel-3
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = x^2 + 5x + 1$ og $g(x) = -x - 4$. Løsningsmengden til $f(x) \leq g(x)$ er markert i rødt på $x$-aksen.
:::

:::::::::::::
::::::::::::::

:::::::::::::::

---


::::::{admonition} Underveisoppgave 2
---
class: check
---
I {numref}`fig-andregradsfunksjoner-andregradsulikheter-grafisk-løsning-underveisoppgave-2` vises grafene til

$$
f(x) = x^2 + x + 1 \quad \text{og} \quad g(x) = -x + 4.
$$

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
---
name: fig-andregradsfunksjoner-andregradsulikheter-grafisk-løsning-underveisoppgave-2
width: 80%
class: no-click, adaptive-figure
---
Viser grafene til $f(x) = x^2 + x + 1$ og $g(x) = -x + 4$.
:::


Bruk figuren til å løse ulikheten 

$$
f(x) > g(x).
$$

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \mathbb{R} \setminus [-3, 1] \quad \iff \quad x \in \langle \gets, -3 \rangle \cup \langle 1, \to \rangle
$$
:::

:::{tab-item} Ulikheter
$$
x < -3 \, \lor \, x > 1
$$
:::
::::
:::::