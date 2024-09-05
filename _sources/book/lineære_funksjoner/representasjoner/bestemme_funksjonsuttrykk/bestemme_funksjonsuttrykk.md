# Bestemme funksjonsuttrykk

:::{admonition} Læringsmål
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:

* Kjenne til hvor mye informasjon man trenger for å bestemme funksjonsuttrykket til en lineær funksjon.
* Bestemme stigningstallet til en lineær funksjon med topunktsformelen.
* Bestemme funksjonsuttrykket til en lineær funksjon med ettpunktsformelen.
:::



## Lineære funksjoner: hva trengs?

:::{admonition} Lineære funksjoner: hva trengs?
---
class: theory
---
Funksjonsuttrykket til en lineær funksjon $f$ er bestemt av en av de to følgende punktene:
1. To punkter
2. Stigningstallet og ett punkt

:::

Vi kan altså bestemme funksjonsuttrykket dersom vi enten kjenner til to punkter på grafen til $f$, eller dersom vi kjenner til stigningstallet og ett punkt på grafen til $f$.

## Topunktsformelen
Typisk bestemmer vi funksjonsuttrykket til en lineær funksjon i to steg:

Steg 1
: Bestem stigningstallet $a$

Steg 2
: Bruk ettpunktsformelen til å bestemme funksjonsuttrykket (og dermed også konstantleddet $b$)

For å bestemme stigningstallet, bruker vi **topunktsformelen**:

:::{admonition} $\Delta$-symbolet
---
class: sidenote, margin
---
Symbolet $\Delta$ er en gresk bokstav som leses som "delta". Vi bruker den ofte for å representere *endringer*. Her for eksempel, er $\Delta x$ endringen i $x$-verdien. 

:::

::::{admonition} Topunktsformelen
---
class: theory
---
Hvis grafen til en lineær funksjon $f$ går gjennom to punkter $(x_1, y_1)$ og $(x_2, y_2)$, så er stigningstallet $a$ gitt ved

$$
a = \dfrac{\Delta y}{\Delta x} \, ,
$$ (eq:topunktsformelen)

der 

$$
\Delta x = x_2 - x_1 \quad \text{og} \quad \Delta y = y_2 - y_1.
$$

Her er $\Delta x$ endringen i $x$-verdiene og $\Delta y$ endringen i $y$-verdien. Se {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-topunktsformelen` for en illustrasjon.

```{figure} ./figurer/teori/topunktsformelen.svg
---
width: 80%
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-topunktsformelen
---
Viser en grafen til en lineær funksjon $f$ og to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på grafen. Endringen i $x$-verdien er $\Delta x = x_2 - x_1$, og endringen i $y$-verdien er $\Delta y = y_2 - y_1$ er illustrert som stiplede linjer.
```

::::

Vi tar et eksempel:

::::{admonition} Eksempel 1: topunktsformelen
---
class: example
---
En lineær funksjon $f$ går gjennom punktene $(1, 2)$ og $(7, 6)$. <br> Bestem stigningstallet til $f$.

:::{admonition} Løsning
---
class: solution
---
Vi bruker topunktsformelen med

$$
(x_1, y_1) = (1, 2) \quad \text{og} \quad (x_2, y_2) = (7, 6).
$$

Da får vi

$$
\Delta x = x_2 - x_1 = 7 - 1 = 6 \quad \text{og} \quad \Delta y = y_2 - y_1 = 6 - 2 = 4.
$$

Dermed blir stigningstallet

$$
a = \dfrac{4}{6} = \dfrac{2}{3} \, .
$$

:::

::::

Så er det **din tur**!



::::{admonition} Underveisoppgave 1
---
class: check
---
Under vises en tabell over noen lineære funksjoner der det er oppgitt to punkter som hver av grafene går gjennom. 

Fyll ut tabellen.

| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $(1, 2)$  | $(3, 4)$  |  |  |  |
| $g(x)$ | $(2, 3)$  | $(4, 1)$  |  |  |  |         
| $h(x)$ | $(0, 1)$  | $(2, 5)$  |  |  |  |          
| $p(x)$ | $(-2, 4)$ | $(1, -5)$ |  |  |  |         
| $q(x)$ | $(-1, 4)$ | $(3, 4)$  |  |  |  |          

:::{admonition} Fasit
---
class: solution, dropdown
---
| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $(1, 2)$  | $(3, 4)$  | $2$ | $2$ | $1$ |
| $g(x)$ | $(2, 3)$  | $(4, 1)$  | $2$ | $-2$ | $-1$ |         
| $h(x)$ | $(0, 1)$  | $(2, 5)$  | $2$  | $4$  | $2$ |          
| $p(x)$ | $(-2, 4)$ | $(1, -5)$ | $3$ | $-9$ | $-3$ |         
| $q(x)$ | $(-1, 4)$ | $(3, 4)$  | $4$  | $0$ | $0$ |   

:::

::::


## Ettpunktsformelen

Dersom vi kjenner til stigningstallet til en lineær funksjon $f$ og et punkt $(x_1, y_1)$ på grafen til $f$, kan vi bestemme funksjonsuttrykket til $f$ ved hjelp av **ettpunktsformelen**. 

Vi tar utgangspunkt i {numref}`fig-lineære-funksjoner-bestemme-funksjonsuttrykk-ettpunktsformelen`.


:::{figure} ./figurer/teori/ettpunktsformelen.svg
---
name: fig-lineære-funksjoner-bestemme-funksjonsuttrykk-ettpunktsformelen
:width: 80%
---
Viser en lineær funksjon et kjent punkt $(x_1, y_1)$ og et vilkårlig punkt $(x, y)$ er tegnet inn.
:::

Vi tenker oss at $(x_1, y_1)$ er et fast punkt, mens $(x, y)$ er et vilkårlig punkt på grafen til $f$. Da kan vi skrive stigningstallet $a$ som

$$
a = \frac{y - y_1}{x - x_1} \, .
$$

Stigningstallet vil være det samme uansett hvilke to punkter $a$ er regnet ut fra (siden det er en konstant). Dermed kan vi skrive om uttrykket som 

$$
a = \frac{y - y_1}{x - x_1} \quad \Leftrightarrow \quad y - y_1 = a(x - x_1)
$$


Dette er ettpunktsformelen.


:::{admonition} Ettpunktsformelen
---
class: theory
---
Dersom vi kjenner stigningstallet $a$ og et punkt $(x_1, y_1)$ på grafen til en lineær funksjon, kan vi bestemme funksjonsuttrykket til funksjonen ved hjelp av ettpunktsformelen

$$
y - y_1 = a(x - x_1).
$$
:::

Vi tar et eksempel

::::{admonition} Eksempel 2: ettpunktsformelen
---
class: example
---
En lineær funksjon $f$ har stigningstall $-2$ og går gjennom punktet $(1, 3)$. 

Bestem $f(x)$.

:::{admonition} Løsning
---
class: solution
---
Vi kjenner til stigningstallet $\textcolor{teal}{a = -2}$ og ett punkt $(\textcolor{red}{x_1}, \textcolor{purple}{y_1}) = (\textcolor{red}{1}, \textcolor{purple}{3})$. <br> Da kan vi bruke ettpunktsformelen som følger:

\begin{align*}
y - \textcolor{purple}{y_1} &= \textcolor{teal}{a}(x - \textcolor{red}{x_1}) \\
\\
y - \textcolor{purple}{3} & = \textcolor{teal}{-2}(x - \textcolor{red}{1}) \\
\\
y - 3 \textcolor{red}{+ 3} & = -2(x - 1) \textcolor{red}{+ 3} && \text{Legger til $3$ på hver side} \\
\\
y & = -2(x - 1) + 3 \\
\\
y & = -2x + 2 + 3 && \text{Utvider parentesen}\\
\\
y & = -2x + 5 && \text{Trekker sammen}.
\end{align*}

Dermed er 

$$
f(x) = -2x + 5.
$$


:::

::::

Og så er det **din tur**!

::::{admonition} Underveisoppgave 2
---
class: check
---
En lineær funksjon $g$ har stigningstall $4$ og går gjennom punktet $(-1, -3)$. 

Bestem $g(x)$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(x) = 4x + 1.
$$
:::


:::{admonition} Løsning
---
class: solution, dropdown
---
Vi har stigningstallet $a = 4$ og punktet $(x_1, y_1) = (-1, -3)$. <br> Da kan vi bruke ettpunktsformelen som følger:

\begin{align*}
y - y_1 &= a(x - x_1) \\
\\
y - (-3) &= 4(x - (-1)) \\
\\
y + 3 &= 4(x + 1) && \text{Åpner opp parenteser og endrer fortegn}\\
\\
y + 3 &= 4x + 4 && \text{Utvider parentesen.}\\
\\
y + 3 \textcolor{red}{- 3} &= 4x + 4 \textcolor{red}{- 3} && \text{Trekker fra $3$ på hver side.}\\
\\
y &= 4x + 1 && \text{Legger sammen.}
\end{align*}

Altså er 

$$
g(x) = 4x + 1.
$$

:::
::::
