# Grafisk løsning 

:::::{admonition} Oppsummering
---
class: summary, dropdown
---
Skrå linjer i planet
: Skrå linjer i planet kan skrives på to måter:
    * $y = ax + b$
    * $Ax + By = C$

Grafisk løsning av likningssystemer
: Løsningen til et lineært likningssystem er koordinatene til skjæringspunktene mellom linjene som representerer likningene i likningssystemet.

Logisk *og*
: Hvis linjene definert av likningene i et likningssystem skjærer hverandre i punktet $(x_1, y_1)$, skriver vi løsningen av likningssystemet som

    $$
    x = x_1 \quad \land \quad y = y_1
    $$

    der vi leser $\land$ som "*og samtidig*".
:::::

På samme måte som vi løste likninger, kan vi også løse likningssystemer grafisk. 


:::{admonition} Læringsmål: grafisk løsning av lineære likningssystemer
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Kunne veksle mellom ulike former for likninger for linjer i planet.
* Løse lineære likningssystemer grafisk.
* Kunne uttrykke løsningen av et lineært likningssystem som et likningssystem eller som en løsningsmengde.
:::

## Linjer på formen $Ax + By = C$

Frem til nå, har vi jobbet med linjer på formen $y = ax + b$ og sett at disse samsvarer med lineære funksjoner. Men dette er ikke den mest generelle formen for linjer. Nå skal vi se på en mer generell form.

::::{admonition} Generelle linjer
---
class: theory
---
En linje i planet er alle punkter $(x, y)$ som oppfyller en likning på formen

$$
Ax + By = C,
$$

der $A, B, C \in \mathbb{R}$ er konstanter.

::::

::::{admonition} Eksempel 1: linjer på formen $Ax + By = C$
---
class: example
name: lineære-likningssystemer-grafisk-eksempel-1
---
En linje på formen $2x + 3y = 6$ kan skrives om til formen $y = ax + b$ med litt algebra:

\begin{align*}
    2x + 3y & = 6 \\
    \\
    2x \textcolor{red}{- 2x} + 3y & = \textcolor{red}{- 2x} + 6 && \text{Trekker fra $2x$ på hver side} \\
    \\
    3y & = -2x + 6 \\
    \\
    \frac{\cancel{3}y}{\cancel{\textcolor{red}{3}}} & = \frac{-2x}{\textcolor{red}{3}} + \frac{\cancelto{\displaystyle \textcolor{teal}{2}}{6}}{\cancel{\textcolor{red}{3}}} && \text{Deler med $3$} \\
    \\
    y & = -\frac{2}{3}x + 2
\end{align*}

Men det betyr at 

$$
2x + 3y = 6 \quad \iff \quad y = -\frac{2}{3}x + 2.
$$

::::


::::{admonition} Eksempel 2: linjer på formen $Ax + By = C$
---
class: example
name: lineære-likningssystemer-grafisk-eksempel-2
---
En fordel med den generelle formen på likningen $Ax + Bx = C$, er at den lar oss beskrive alle type linjer:

````{tab-set}
```{tab-item} Skrå linjer
Form på likning:
: $y = ax + b$

:::{figure} ./figurer/eksempler/eksempel_2/skrå_linje.svg 
---
width: 80%
name: fig-lineære-likningssystemer-grafisk-eksempel-2a
---
viser en skrå linje $y = -\dfrac{1}{2}x + 3$ som også kan skrives på formen $x + 2y = 6$.
:::

```

```{tab-item} Horisontale linjer
Form på likning:
: $y = \text{konstant}$

:::{figure} ./figurer/eksempler/eksempel_2/horisontal_linje.svg 
---
width: 80%
name: fig-lineære-likningssystemer-grafisk-eksempel-2b
---
viser en horisontal linje $y = 3$.
:::
```

```{tab-item} Vertikale linjer
Form på likning:
: $x = \text{konstant}$

:::{figure} ./figurer/eksempler/eksempel_2/vertikal_linje.svg 
---
width: 80%
name: fig-lineære-likningssystemer-grafisk-eksempel-2c
---
viser en vertikal linje $x = -2$. 
:::

```

````
::::

## Grafisk løsning av likningssystemer


::::{admonition} Symbolforklaring: $\land$
---
class: sidenote, margin
---
Symbolet $\land$ betyr "*og samtidig*". Når vi skriver 

$$
x = 2 \quad \land \quad y = 3,
$$

mener vi at $x = 2$ *og samtidig* er $y = 3$. 
::::

:::::{admonition} Grafisk løsning av likningssystemer
---
class: theory
---
Gitt et lineært likningssystem 

\begin{align*}
    Ax + By & = C \\
    Dx + Ey & = F
\end{align*}

er løsningen av likningssystemer skjæringspunktet $(x_1, y_1)$ mellom de to linjene. Se {numref}`fig-lineære-likningssystemer-grafisk-løsning`.

:::{figure} ./figurer/teori/grafisk_løsning.svg
---
name: fig-lineære-likningssystemer-grafisk-løsning
width: 80%
---
Løsningen av likningssystemet $Ax + By = C \, \land \, Dx + Ey = F$ er skjæringspunktet $(x_1, y_1)$ mellom de to linjene. 
:::

Løsningen skriver vi enten som et likningssystem eller som en løsningsmengde:

$$
\underbrace{x = x_1 \quad \land \quad y = y_1}_{\text{Likningssystem}} \quad \text{eller} \quad \underbrace{(x, y) \in \{(x_1, y_1)\}}_{\text{Løsningsmengde}}. 
$$

:::::
Vi starter med å se på et eksempel:

:::::{admonition} Eksempel 3: grafisk løsning av likningssystemer
---
class: example
---
Løs likningssystemet grafisk

\begin{align*}
    -2x + y & = 1 \tag{1}\label{eq-lineære-likningssystemer-grafisk-eksempel-3a} \\
    x + y & = 4  \tag{2}\label{eq-lineære-likningssystemer-grafisk-eksempel-3b} \\
\end{align*}

::::{admonition} Løsning
---
class: solution
---

For å løse likningssystemet grafisk, skriver vi om de to likningene til formen $y = ax + b$ så vi kan tolke de som lineære funksjoner:

For likning $\eqref{eq-lineære-likningssystemer-grafisk-eksempel-3a}$:

\begin{align*}
    -2x + y & = 1 \\
    \\
    -2x \textcolor{red}{+ 2x} + y & = 1 \textcolor{red}{+ 2x} && \text{Trekker fra $2x$ på hver side} \\
    \\
    y & = 2x + 1
\end{align*}

Og tilsvarende for likning $\eqref{eq-lineære-likningssystemer-grafisk-eksempel-3b}$:

\begin{align*}
    x + y & = 4 \\
    \\
    x \textcolor{red}{- x} + y & = 4 \textcolor{red}{-x} && \text{Trekker fra $x$ på hver side} \\
    \\
    y & = -x + 4
\end{align*}

Dermed får vi at likningssystemet kan skrives som

\begin{align*}
    y & = 2x + 1 \\
    y & = -x + 4
\end{align*}

For å løse likningssystemet grafisk, tolker vi de to linjene som lineære funksjoner

$$
f(x) = 2x + 1 \quad \text{og} \quad g(x) = -x + 4.
$$

så finner vi skjæringspunktet mellom linjene.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: lineære-likningssystemer-grafisk-eksempel-3
width: 80%
---
Grafene til de lineære funksjonene $f(x) = 2x + 1$ og $g(x) = -x + 4$. Skjæringspunktet mellom de to grafene svarer til løsningen av likningssystemet. 
:::

Løsningen av likningssystemet svarer til koordinatene til skjæringspunktet mellom de to lineære funksjonene. Vi kan lese av at dette er $(x, y) = (1, 3)$. Da kan vi uttrykke løsningen av likningssystemet enten som et likningssystem eller som en løsningsmengde:

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 1 \quad \land \quad y = 3.
$$
```

```{tab-item} Løsning som løsningsmengde 
$$
(x, y) \in \{(1, 3)\}.
$$
```
````
::::

:::::

``````{admonition} Underveisoppgave 1
:class: check

Bruk figuren under til å løse likningssystemet 

\begin{align}
4x + 3y &= 9 \\
x - 2y &= 5 \\
\end{align}

Uttrykk løsningen som
1. Et likningssystem
2. En løsningsmengde

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: lineære-likningssystemer-grafisk-underveisoppgave-1
width: 80%
---

Grafisk representasjon av likningssystemet
:::

`````{admonition} Fasit
:class: solution, dropdown

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 3 \quad \land \quad y = -1.
$$
```

```{tab-item} Løsning som løsningsmengde
$$
(x, y) \in \{(3, -1)\}.
$$
```
````


`````

`````{admonition} Løsning
:class: solution, dropdown
Fra figuren ser vi at de to linjene skjærer hverandre i $(x, y) = (3, -1)$. Dermed er løsningen av likningssystemet

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 3 \quad \land \quad y = -1.
$$
```

```{tab-item} Løsning som løsningsmengde
$$
(x, y) \in \{(3, -1)\}.
$$
```
````


`````
``````

<!-- ## Antall løsninger
På samme måte som en lineær likning kan ha ingen, én eller uendelig mange løsninger, kan også lineære likningssystemer ha ingen, én eller uendelig mange løsninger. 

## Likningssystem med flere enn to variabler
Et likningssystem kan ha flere enn to variabler, men disse likningssystemene vil være vanskelige å tegne opp i et todimensjonalt koordinatsystem, ettersom vi har en variabel representert langs hver akse. For likningssystemer med flere enn to variabler vil vi som regel heller velge en algebraisk løsningsmetode.  -->
