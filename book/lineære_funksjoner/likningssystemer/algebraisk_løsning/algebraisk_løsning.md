# Algebraisk løsning

Du har kanskje tidligere lært om ulike løsningsstrategier for å løse lineære likningssystemer algebraisk. I dette kapittelet skal vi ta for oss to løsningsmetoder for likningssystemer.

```{admonition} Læringsmål: algebraisk løsning av lineære likningssystemer
:class: tip
Etter dette delkapittelet, er målet at du skal kunne:
* Løse lineære likningssystemer med to variabler ved hjelp av innsettingsmetoden.
* Løse lineære likningssystemer med to variabler ved hjelp av addisjonsmetoden.
* Kunne uttrykke løsningen av et lineært likningssystem som et likningssystem eller som en løsningsmengde.
* Kunne anvende likningssystemer til å
    * Bestemme koeffisientene til en lineær funksjon.
    * Løse praktiske problemer.
```


## Innsettingsmetoden

Før vi går løs på et eksempel, skal vi gi en kort beskrivelse av innsettingsmetoden.

````{admonition} Innsettingsmetoden
:class: theory
Gitt to lineære likninger med to variabler $x$ og $y$, gjør vi følgende:

Steg 1:
: Løs én av likningene med hensyn på $y$. 

Steg 2
: Plugg uttrykket for $y$ inn i den andre likningen og løs likningen for $x$.

Steg 3
: Plugg verdien for $x$ inn i én av likningene og regn ut verdien til $y$.


Merk at beskrivelsen over fungerer også motsatt (bytt rollen til $x$ og $y$ i alle stegene).

````

Vi starter med å se på et eksempel på hvordan vi kan løse et likningssystem med to variabler ved hjelp av innsettingsmetoden. Vi skal gi en 

`````{admonition} Eksempel 1: innsettingsmetoden
:class: example
Vi tar for oss likningssystemet
```{math}
\begin{align*}
2x + y & = 5 \label{1a} \quad\quad\quad \tag{1a} \\
x - y & = 1 \label{1b} \quad\quad\quad \tag{1b} 
\end{align*}
```

**Løsning:**<br>

Steg 1
: Vi løser likningen $\eqref{1b}$ med hensyn på $y$:

$$
x - y = 1 \quad \Leftrightarrow \quad y = x - 1.
$$

Steg 2
: Vi plugger inn $y = x - 1$ i likning $\eqref{1a}$ som gir:

$$
2x + \underbrace{x - 1}_{y} = 5
$$

som vi kan skrive om enklere som

$$
2x = 6 \quad \Leftrightarrow \quad x = 3.
$$

Steg 3
: Nå plugger vi inn løsningen vår for $x$ i enten likning $\eqref{1a}$ eller $\eqref{1b}$ (det spiller ingen rolle hvilken, så vi velger den som gir minst regning). Vi velger å plugge inn i likning $\eqref{1b}$ siden vi allerede løst denne likningen for $y$:

$$
y = 3 - 1 = 2.
$$

Vi kan uttrykke løsningen av likningsystemet på to måter, enten som et likningssystem eller som en løsningsmengde:

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = -1 \quad \land \quad y = 4.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \{(-1, 4)\}.
$$
```
````
`````

Så er det **din tur**!

``````{admonition} Underveisoppgave 1
:class: check

Bruk innsettingsmetoden til å løse likningssystemet

$$
\begin{align*}
3x + 2y & = 5 \label{2a} \quad\quad\quad \tag{2a} \\
-2x + y & = 6 \label{2b} \quad\quad\quad \tag{2b}
\end{align*}
$$


`````{admonition} Fasit
:class: dropdown, solution
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = -1 \quad \land \quad y = 4.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \{(-1, 4)\}.
$$
```
````
`````

`````{admonition} Løsning
:class: dropdown, solution

Steg 1
: Vi løser likning $\eqref{2b}$ med hensyn på $y$:

$$
-2x + y = 6 \quad \Leftrightarrow \quad y = 2x + 6.
$$

Steg 2
: Vi plugger uttrykket for $y$ inn i likning $\eqref{2a}$:

$$
3x + 2\cdot \underbrace{(2x + 6)}_{y} = 5 \quad \Leftrightarrow \quad 3x + 4x + 12 = 5 \quad \Leftrightarrow \quad 7x = -7 \quad \Leftrightarrow \quad x = -1.
$$

Steg 3
: Vi plugger verdien for $x$ inn i likning $\eqref{2b}$ for å regne ut den tilhørende verdien til $y$:

$$
y = 2\cdot (-1) + 6 = 4.
$$

Dermed er løsningen av likningssystemet

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = -1 \quad \land \quad y = 4.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \{(-1, 4)\}.
$$
```
````

`````
``````

## Addisjonsmetoden

Addisjonsmetoden er en annen måte for å løse lineære likningssystemer med to variabler. 

```{admonition} Begrepsforklaring: multiplum
:class: note, margin
Begrepet **multiplum** betyr så så mange ganger av noe. For eksempel er $2x$ et multiplum av $x$ der $2$ er multiplumet. Men det er også $x/2$, der $1/2$ er multiplumet. Noen definisjoner begrenser det til å bare gjelde heltall, men vi skal ta oss friheten til å bruke det for alle reelle tall.
```

```{admonition} Addisjonsmetoden
:class: theory
Gitt to lineære likninger med to variabler $x$ og $y$, gjør vi følgende:

Steg 1:
: Legg til et **multiplum** av en av likningene til den andre likningen slik at én av variablene forsvinner. Løs likningen for den gjenværende variabelen.

Steg 2
: Plugg inn løsningene i én av likningene for å bestemme verdien til den siste variabelen.
```


Vi går løs på et eksempel:

```{admonition} Forkortelser: V.S. og H.S.
:class: note, margin
Forkortelsene under står for:

V.S.
: Venste side.

H.S. 
: Høyre side.

```
````{admonition} Eksempel 2: addisjonsmetoden
:class: example
Et likningssystem er gitt ved

$$
\begin{align*}
    x + 3y & = -7 \label{3a} \quad\quad\quad \tag{3a} \\
    3x - 2y & = 12 \label{3b} \quad\quad\quad \tag{3b} 
\end{align*}
$$

Bruk addisjonsmetoden til å løse likningssystemet.

**Løsning:**<br>

Steg 1
: Vi kan ta likning $\eqref{3a}$ og gange den med $3$ for å så trekke det fra likning $\eqref{3b}$ for at $x$ skal forsvinne:

$$
\underbrace{3x - 2y}_{\text{V.S. Likning } \eqref{3b}} - 3\cdot\underbrace{(x + 3y)}_{\text{V.S. Likning } \eqref{3a}} =\underbrace{12}_{\text{H.S. Likning } \eqref{3b}} -  3\cdot \underbrace{(-7)}_{\text{H.S. Likning } \eqref{3a}}
$$

som gir

$$
3x - 2y - 3x - 9y = 12 + 21,
$$

som kan skrive om til

$$
-11y = 33 \quad \Leftrightarrow \quad y = -3.
$$

Steg 2
: Vi plugger inn verdien for $y$ inn i en av likningene for å bestemme verdien til $x$. Vi velger likning $\eqref{3a}$:

$$
x + 3\cdot(-3) = -7 \quad \Leftrightarrow \quad x - 9 = -7 \quad \Leftrightarrow \quad x = 2.
$$

Dermed er løsningen av likningssystemet

$$
(x, y) \in \{(2, -3)\}.
$$
````
Så er det **din tur**!

``````{admonition} Underveisoppgave 2
:class: check
Bruk addisjonsmetoden til å løse likningssystemet

$$
\begin{align*}
    4x + y & = 1 \label{4a} \quad\quad\quad \tag{4a} \\
    -2x - 5y & = 4 \label{4b} \quad\quad\quad \tag{4b}
\end{align*}
$$



`````{admonition} Fasit
:class: dropdown, solution
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = \frac{1}{2} \quad \land \quad y = -1.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(\frac{1}{2}, -1\right)\right\}
$$
```
````
`````

`````{admonition} Løsning
:class: dropdown, solution
Vi kan legge til et multiplum av likning $\eqref{4a}$ til likning $\eqref{4b}$ for at $x$ skal forsvinne. Legger vi til $5$ ganget med likning $\eqref{4a}$ til likning $\eqref{4b}$ oppnår vi dette:

$$
5\cdot \underbrace{(4x + y)}_{\text{V.S. likning } \eqref{4a}} + \underbrace{(-2x - 5y)}_{\text{V.S. likning } \eqref{4b}} = 5\cdot \underbrace{1}_{\text{H.S. likning } \eqref{4a}} + \underbrace{4}_{\text{H.S. likning } \eqref{4b}}, 
$$

eller skrevet uten annotasjoner

$$
5(4x + y) + (-2x - 5y) = 5\cdot 1 + 4,
$$

som vi kan skrive om til

$$
20x + 5y - 2x - 5y = 9 \quad \Leftrightarrow \quad 18x = 9 \quad \Leftrightarrow \quad x = \frac{9}{18} = \frac{1}{2}.
$$

Så plugger vi verdien inn i likning $\eqref{4a}$ for å finne verdien til $y$:

$$
4\cdot \frac{1}{2} + y = 1 \quad \Leftrightarrow \quad 2 + y = 1 \quad \Leftrightarrow \quad y = -1.
$$

Altså er løsningen av likningssystemet gitt ved 

$$
x = \frac{1}{2} \quad \land \quad y = -1.
$$
`````

``````

## Anvendelser
Lineære likningssystemer dukker opp i mange praktiske situasjoner. Vi skal se på hvordan vi går fra en praktisk situasjon til et lineært likningssystem.


::::{admonition} Eksempel 3: fra praktisk situasjon til likningssystem
---
class: example
---
Anna skal plante trær i en park. Hun skal plante to forskjellige typer som tar opp ulik plass. Eiketrær trenger 4 kvadratmeter plass, mens bjørketrær trenger 2 kvadratmeter plass. Anna har totalt 100 kvadratmeter til rådighet. Hun har bestemt seg for å plante 40 trær. 

Hvor mange av hver type tre skal hun plante?


:::{admonition} Løsning
---
class: solution
---
Vi lar $x$ være antall eiketrær og $y$ være antall bjørketrær. Siden det skal være 40 trær til sammen, kan vi sette opp den ene likningen som:

\begin{align*}
x + y &= 40 && \text{(Antall trær til sammen)}
\end{align*}

Ett eiketre tar opp 4 kvadratmeter og bjørketrær tar opp 2 kvadratmeter. Vi har 100 kvadratmeter til sammen, som betyr at vi kan sette opp den andre likningen som:

\begin{align*}
\underbrace{4x}_\text{Plass for eiketrær} + \underbrace{2y}_\text{Plass for bjørketrær} &= 100 && \text{(Totalt antall kvadratmeter)}
\end{align*}

Vi har altså likningssystemet

\begin{align*}
x + y & = 40 \\
4x + 2y & = 100
\end{align*}
:::
::::
