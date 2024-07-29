# Algebraisk løsning

:::{admonition} Læringsmål: algebraisk løsning av lineære likninger
---
class: tip
---
Etter å gått gjennom dette delkapittelet, er målet at du skal kunne:
* Løse lineære likninger algebraisk på formen
    * $ax + b = 0$
    * $ax + b = k$
    * $ax + b = cx + d$
* Kunne uttrykke løsningen av en likning som
    * En likning
    * En løsningsmengde
:::

Å løse likninger algebraisk, handler om å jobbe med likningene symbolsk og bruke algebraiske lover til å isolere variabelen i likningen, hvis mulig. Vi kaller dette å bestemme løsningen. Grovt sett er det fire regneoperasjoner vi kan gjøre med likninger:
1. Legge til noe på begge sider av likningen.
2. Trekke fra noe på begge sider av likningen.
3. Gange med noe på begge sider av likningen.
4. Dele på noe på begge sider av likningen.

Det er viktig å understreke at vi må gjøre samme regneoperasjon på **begge sider**, i alle ledd.


## Likninger av typen $ax + b = 0$

Vi tar et eksempel:

:::{admonition} Flytte og bytte
---
class: sidenote, margin
---
I {ref}`eksempel 1 <lineære-likninger-algebraisk-løsning-example-1>` har vi trekt fra samme tall på hver side i første steg. Men tidligere har du kanskje lært "flytte og bytte"-regelen. Denne regelen kommer fra at man legger til eller trekker fra samme tall på hver side av likningen.  
:::

::::{admonition} Eksempel 1
---
class: example
name: lineære-likninger-algebraisk-løsning-example-1
---
Løs likningen

$$
3x + 6 = 0.
$$

Målet vårt er å finne ut hvilken verdi av $x$ som gjør at likningen er sann. 


\begin{align*}
3x + 6 &= 0 \\
& \Updownarrow \\
3x + 6 \textcolor{red}{-6} &= 0 \textcolor{red}{-6} && \text{Trekker fra $6$ på begge sider}\\
& \Updownarrow \\
3x &= -6 \\
& \Updownarrow \\
\frac{\bcancel{3}x}{\bcancel{\textcolor{red}{3}}} &= \frac{\cancelto{\displaystyle \textcolor{teal}{-2}}{-6}}{\cancel{\textcolor{red}{3}}} && \text{Deler med 3 på begge sider}\\
& \Updownarrow \\
x &= -2
\end{align*}

Over har vi uttrykt løsningen vår som en likning. Noen ganger er dette ryddigst, andre ganger er det ryddigere å uttrykke løsningen som en løsningsmengde - spesielt når likningen har mer enn én løsning. Vi oppgir løsningen som enten som en likning eller som en løsningsmengde:

$$
\underbrace{x = -2}_{\text{likning}} \quad \Leftrightarrow \quad \underbrace{x \in \{-2\}}_{\text{løsningsmengde}}
$$

Vi velger oss typisk den skrivemåten som er enklest å lese.
::::



**Din tur!**

::::{admonition} Underveisoppgave 1
---
class: check
---
Løs likningen

$$ 
4x - 2 = 0.
$$

Uttrykk løsningen som 
* En likning
* En løsningsmengde

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \dfrac{1}{2} \quad \Leftrightarrow \quad x \in \left\{\dfrac{1}{2}\right\}.
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
\begin{align*}
4x - 2 &= 0 \\
& \Updownarrow \\
4x - 2 \textcolor{red}{+2} &= 0 \textcolor{red}{+2} && \text{Legger til $2$ på begge sider}\\
& \Updownarrow \\
4x &= 2 \\
& \Updownarrow \\
\frac{\bcancel{4}x}{\bcancel{\textcolor{red}{4}}} &= \frac{2}{\textcolor{red}{4}} && \text{Deler med 4 på begge sider}\\
& \Updownarrow \\
x &= \dfrac{1}{2} \\
& \Updownarrow \\
x &\in \left\{\dfrac{1}{2}\right\}
\end{align*}
:::
::::

## Likninger på formen $ax + b = k$

Vi går løs på et eksempel på denne typen lineære likning også:

::::{admonition} Stryk med pil
---
class: sidenote, margin
---
Når du ser notasjonen 

$$
\cancelto{\displaystyle 2}{4}
$$

betyr dette at vi sitter igjen med en faktor $2$ etter å ha stryket $4$ mot noe. For eksempel:

$$
\frac{5}{2} \cdot \textcolor{red}{4} = \dfrac{5}{\cancel{2}} \cdot \cancelto{\displaystyle 2}{\textcolor{red}{4}} = 5\cdot \textcolor{red}{2}
$$

::::

:::::{admonition} Eksempel 2
---
class: example
name: lineære-likninger-algebraisk-løsning-example-2
---
Vi skal løse likningen

$$
5x + 2 = -3.
$$

Målet vårt er å bestemme hvilken verdi av $x$ som gjør at likningen er sann, så vi skal isolere $x$ på en side av likningen.

\begin{align*}
5x + 2 &= -3 \\
& \Updownarrow \\
5x + 2 \textcolor{red}{-2} &= -3 \textcolor{red}{-2} && \text{Trekker fra $2$ på begge sider}\\
& \Updownarrow \\
5x &= -5 \\
& \Updownarrow \\
\frac{\bcancel{5}x}{\bcancel{\textcolor{red}{5}}} &= \frac{\cancelto{\displaystyle -1}{-5}}{\cancel{\textcolor{red}{5}}} && \text{Deler med 5 på begge sider}\\
& \Updownarrow \\
x &= -1
\end{align*}

Altså er løsningen

::::{tab-set}
:::{tab-item} Likning
$$
x = -1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \{-1\}
$$
:::
::::
:::::

Så er det **din tur**!

::::::{admonition} Underveisoppgave 2
---
class: check
---
Løs likningen 

$$
-3x + 5 = 4.
$$

Uttrykk løsningen som 
* En likning
* En løsningsmengde

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Likning
$$
x = \dfrac{1}{3}
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left\{\dfrac{1}{3}\right\}
$$
:::
::::

:::::

:::::{admonition} Løsning
---
class: dropdown, solution
---

\begin{align*}
-3x + 5 &= 4 \\
& \Updownarrow \\
-3x + 5 \textcolor{red}{-5} &= 4 \textcolor{red}{-5} && \text{Trekker fra $5$ på begge sider}\\
& \Updownarrow \\
-3x &= -1 \\
& \Updownarrow \\
\frac{\bcancel{-3}x}{\bcancel{\textcolor{red}{-3}}} &= \frac{-1}{\textcolor{red}{-3}} && \text{Deler med $-3$ på begge sider}\\
& \Updownarrow \\
x &= \dfrac{1}{3}
\end{align*}

Altså er løsningen

::::{tab-set}
:::{tab-item} Likning
$$
x = \dfrac{1}{3}
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left\{\dfrac{1}{3}\right\}
$$
:::
::::
:::::
::::::

## Likninger på formen $ax + b = cx + d$
Vi går løs på den siste varianten av lineære likninger, men løsningsstrategien er fortsatt den samme! 


:::::{admonition} Eksempel 3
---
class: example
name: lineære-likninger-algebraisk-løsning-example-3
---
Vi skal løse likningen

$$
\dfrac{3x}{4} - \dfrac{1}{2} = x + \dfrac{3}{2}.
$$

Målet vårt er å få $x$ alene. Det betyr i praksis at vi får alle ledd med $x$ over på én side av likningen. Typisk når en likning inneholder brøker, er det lurt å gange bort alle brøkene først.  

\begin{align*}
\dfrac{3x}{4} - \dfrac{1}{2} &= x + \dfrac{3}{2} \\
& \Updownarrow \\
\dfrac{3x}{\cancel{4}} \cdot \cancel{\textcolor{red}{4}} - \dfrac{1}{\cancel{2}} \cdot \cancelto{\displaystyle 2}{\textcolor{red}{4}} &= \textcolor{red}{4}\cdot x + \dfrac{3}{\cancel{2}} \cdot \cancelto{\displaystyle 2}{\textcolor{red}{4}} && \text{Ganger med $4$ på begge sider}\\
& \Updownarrow \\
3x - 1\cdot \textcolor{red}{2} &= 4x + 3\cdot \textcolor{red}{2} && \text{Restfaktorer etter ganging med brøkene}\\
& \Updownarrow \\
3x \textcolor{red}{-3x} - 2 &= 4x \textcolor{red}{-3x} + 6 && \text{Trekker fra $3x$ på begge sider}\\
& \Updownarrow \\
-2 &= x + 6 \\
& \Updownarrow \\
-2 \textcolor{red}{-6} &= x + 6 \textcolor{red}{-6} && \text{Trekker fra $6$ på begge sider}\\
& \Updownarrow \\
-8 &= x
\end{align*}

En god vane er å **sette prøve** på svaret når du har løst likningen. Det vil si å sette inn løsningen din i den opprinnelige likningen for å verifisere at du har regnet riktig.
Vi gjør som følger, vi sette inn verdien av $x$ på venstre side (V.S) og høyre side (V.S) og sjekker at vi får samme verdi:

::::{grid}
:gutter: 1

:::{grid-item-card} V.S: $\dfrac{3x}{4} - \dfrac{1}{2}$
$$
\dfrac{3\cdot \textcolor{red}{(-8)}}{4} - \dfrac{1}{2} = \dfrac{-24}{4} - \dfrac{2}{4} = -\dfrac{\cancelto{\displaystyle 13}{26}}{\cancelto{\displaystyle 2}{4}} = -\dfrac{13}{2}
$$
:::

:::{grid-item-card} H.S: $x + \dfrac{3}{2}$
$$
\textcolor{red}{(-8)} + \dfrac{3}{2} = -\dfrac{16}{2} + \dfrac{3}{2} = -\dfrac{13}{2}
$$
:::
::::

Altså får vi samme verdi på begge sider av den opprinnelige likningen med $x = -8$, som betyr at løsningen er

::::{tab-set}
:::{tab-item} Likning
$$
x = -8
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \{-8\}
$$
:::
::::
:::::

**Din tur**!

::::::{admonition} Underveisoppgave 3
---
class: check
---
Løs likningen 

$$
-\dfrac{2x}{3} + 3 = x - 2.
$$

Sett prøve på svaret ditt.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 3
$$
::::


:::::{admonition} Løsning
---
class: dropdown, solution
---

\begin{align*}
-\dfrac{2x}{3} + 3 &= x - 2 \\
& \Updownarrow \\
-\dfrac{2x}{\cancel{3}} \cancel{\textcolor{red}{\cdot 3}} + 3 \textcolor{red}{\cdot 3} &= x \textcolor{red}{\cdot 3} - 2 \textcolor{red}{\cdot 3} && \text{Ganger med 3 på begge sider}\\
& \Updownarrow \\
-2x + 9 &= 3x - 6\\
& \Updownarrow \\
-2x \textcolor{red}{- 3x} + 9 &= 3x \textcolor{red}{- 3x} - 6 && \text{Trekker fra $3x$ på begge sider}\\
& \Updownarrow \\
-5x + 9 &= -6 \\
& \Updownarrow \\
-5x + 9 \textcolor{red}{-9} &= -6 \textcolor{red}{-9} && \text{Trekker fra $9$ på begge sider}\\
& \Updownarrow \\
-5x &= -15 \\
& \Updownarrow \\
\frac{\bcancel{-5}x}{\bcancel{\textcolor{red}{-5}}} &= \frac{\cancelto{\displaystyle 3}{-15}}{\cancel{\textcolor{red}{-5}}} && \text{Deler med $-5$ på begge sider}\\
& \Updownarrow \\
x &= 3
\end{align*}

Til slutt setter vi prøve på svaret:

::::{grid}

:::{grid-item-card} V.S: $-\dfrac{2x}{3} + 3$
$$
-\dfrac{2\cdot \textcolor{red}{3}}{3} + 3 = -2 + 3 = 1
$$
:::

:::{grid-item-card} H.S: $x - 2$
$$
\textcolor{red}{3} - 2 = 1
$$
:::
::::
:::::


::::::


## Oppgaver

:::::{admonition} Oppgave 1
---
class: problem-level-1
---
Hvilke av linjene under er likninger?

1. $4$
2. $x+4$
3. $4x$
4. $x = 4$
5. $x + 4 = 9$
6. $4x = 16$ 
7. $4\left(x+1\right) = 4x + 4$

:::{admonition} Fasit
---
class: answer, dropdown
---

Linje 1-3 er uttrykk, mens linje 4-6 er likninger. Linje 7 er en identitet, fordi løsningsmengden er $L = \mathbb{R}$, altså er likningen oppfylt for alle reelle tall. 
:::
:::::


:::::{admonition} Oppgave 2 
---
class: problem-level-1
---
Løs likningene under og sett prøve på svaret.

Oppgave 2a
: $$ 2x = 4$$

:::{admonition} Fasit: 2a
---
class: dropdown, answer
---

````{tab-set}
```{tab-item} Likning
$$
x = 2
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{2\}
$$
```
````
:::

Oppgave 2b
: $$2x + 2 = 4$$

:::{admonition} Fasit: 2b
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = 1
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{1\}
$$
```
````
:::

Oppgave 2c
: $$2x + 2 = x + 4$$

:::{admonition} Fasit: 2c
---
class: dropdown, answer
---

````{tab-set}
```{tab-item} Likning
$$
x = 2
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{2\}
$$
```
````
:::

Oppgave 2d
: $$2x - 2 = x + 4$$

:::{admonition} Fasit: 2d
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = 6
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{6\}
$$
```
````
:::

Oppgave 2e
: $$\dfrac{x}{2} = 4$$

:::{admonition} Fasit: 2e
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = 8
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{8\}
$$
```
````
:::

Oppgave 2f
: $$\dfrac{x}{2} + 3 = 4$$


:::{admonition} Fasit: 2f
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = 2
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{2\}
$$
```
````
:::
:::::


:::::{admonition} Oppgave 3
---
class: problem-level-2
---
Løs likningene.

Oppgave 3a
: $$ 3x + 9 = 3(x + 3)$$

:::{admonition} Fasit: 3a
---
class: dropdown, answer
---
Likningen er en identitet, så løsningen er $x \in \mathbb{R}$. Venstre og høyre side er like for alle reelle tall.
:::

Oppgave 3b
: $$ 3x - (x - 2) = (2x - 1) - (3x + 9)$$

:::{admonition} Fasit: 3b
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = -4
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{-4\}
$$
```
````
:::

Oppgave 3c
: $$ \dfrac{x}{2}−\left(\dfrac{x}{3}+\dfrac{1}{2}\right)=𝑥−2\left(\dfrac{x}{4}−1\right)$$

:::{admonition} Fasit: 3c
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = -\dfrac{15}{2}
$$
```

```{tab-item} Løsningsmengde
$$
x \in \left\{-\dfrac{15}{2}\right\}
$$
```
````
:::


Oppgave 3d
: $$ \dfrac{1}{2} \left(x-4\right)-\left(\dfrac{2x}{3}-1\right)=\dfrac{1}{3} \left(x-1\right)+\dfrac{x}{6}$$

:::{admonition} Fasit: 3d
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Likning
$$
x = -1
$$
```

```{tab-item} Løsningsmengde
$$
x \in \{-1\}
$$
```
````
:::
:::::
