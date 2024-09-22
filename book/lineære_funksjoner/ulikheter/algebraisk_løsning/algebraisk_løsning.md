# Algebraisk løsning

:::{admonition} Læringsmål: algebraisk løsning av lineære ulikheter
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Løse lineære ulikheter algebraisk.
:::

Når vi jobber med lineære ulikheter, kan vi i stor grad bruke de samme metodene som vi bruker for å løse lineære likninger. Vi kan 
* legge til og trekke fra et tall på begge sider av ulikheten
* gange og dele med et tall på begge sider av ulikheten/*

/*Unntaket til dette er når vi skal gange eller dele med et negativt tall, da må vi snu ulikhetstegnet.


::::{admonition} Eksempel 1: ulikhet på formen $ax + b > 0$ 
---
class: example
---
Løs ulikheten under algebraisk.

$$
2x - 3 > 0
$$


:::{admonition} Løsning
---
class: solution
---
Vi bruker samme strategi som for lineære likninger.

\begin{align*}
2x - 3 &> 0 \\
& \Updownarrow \\
2x - 3 \textcolor{red}{ + 3} &> \textcolor{red}{ + 3} && \text{Legger til $3$ på hver side} \\
& \Updownarrow \\
2x &> 3 \\
& \Updownarrow \\
\dfrac{\cancel{2}x}{\cancel{\textcolor{red}{2}}} &> \dfrac{3}{\textcolor{red}{2}} && \text{Deler med $2$ på hver side} \\
& \Updownarrow \\
x &> \dfrac{3}{2}
\end{align*}

Vi kan oppgi løsningen enten som en ulikhet eller som en løsningsmengde

$$
\underbrace{x > \dfrac{3}{2}}_\text{Ulikhet} \quad \text{eller} \quad \underbrace{x \in \left \langle \dfrac{3}{2}, \to \right \rangle}_\text{Løsningsmengde}
$$
:::

::::

::::::{admonition} Underveisoppgave 1
---
class: check
---
Løs ulikheten under algebraisk. Oppgi løsningen både som en ulikhet og en løsningsmengde.

$$
3x + 4 \leq 0
$$



:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Ulikhet
$$
x \leq -\dfrac{4}{3}
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left \langle \gets, -\dfrac{4}{3} \right ]
$$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
3x + 4 &\leq 0 \\
& \Updownarrow \\
3x + 4 \textcolor{red}{ - 4} &\leq \textcolor{red}{ - 4} && \text{Trekker fra $4$ på hver side} \\
& \Updownarrow \\
3x &\leq -4 \\
& \Updownarrow \\
\dfrac{\cancel{3}x}{\cancel{\textcolor{red}{3}}} &\leq \dfrac{-4}{\textcolor{red}{3}} && \text{Deler med $3$ på hver side} \\
& \Updownarrow \\
x &\leq -\dfrac{4}{3} \\
& \Updownarrow \\
x & \in \left \langle \gets, -\dfrac{4}{3} \right ]
\end{align*}
:::::
::::::


:::::{admonition} Snu ulikhetstegnet når vi ganger med et negativt tall
---
class: discussion, margin
---
Å snu ulikhetstegnet når vi ganger med et negativt tall har en logisk årsak. Tenk deg at vi ser på en ulikhet som ser sann, for eksempel

$$
3 < 5
$$

Hvis vi nå *bare* ganger med $-1$ på begge sider, får vi

$$
-3 < -5
$$

Men dette er ikke lenger en sann påstand. Snur vi derimot ulikhetstegnet, får vi en sann påstand

$$
-3 > -5
$$

Sånn kan vi forstå hvorfor vi snur ulikhetstegnet når vi ganger med et negativt tall.
:::::

::::::{admonition} Eksempel 2: ulikhet på formen $ax + b < cx + d$
---
class: example
---
Løs ulikheten

$$
2x + 3 < 3x - 4
$$

algebraisk. 

:::::{admonition} Løsning
---
class: solution
---
\begin{align*}
2x + 3 &< 3x - 4 \\
& \Updownarrow \\
2x \textcolor{red}{ - 3x} + 3 \textcolor{red}{ - 2x} &< 3x \textcolor{red}{ - 3x} - 4 && \text{Trekk fra $3x$ på hver side} \\
& \Updownarrow \\
-x + 3 &< -4 \\
& \Updownarrow \\
-x + 3 \textcolor{red}{- 3} &< -4 \textcolor{red}{- 3} && \text{Trekk fra $3$ på hver side} \\
& \Updownarrow \\
-x &< -7 \\
& \Updownarrow \\
-x \textcolor{red}{\cdot (-1)} &> -7 \textcolor{red}{\cdot (-1)} && \text{Ganger med (-1) og snur ulikhetstegnet} \\
& \Updownarrow \\
x &> 7
\end{align*}
:::::

::::::



::::::{admonition} Underveisoppgave 2
---
class: check
---
Løs ulikheten

$$
5x - 3 \geq -2x + 4
$$

algebraisk. 

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Ulikhet
$$
x \geq 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left [1, \to \right \rangle
$$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
5x - 3 &\geq -2x + 4 \\
& \Updownarrow \\
5x \textcolor{red}{ + 2x} - 3 \textcolor{red}{ + 3} &\geq -2x \textcolor{red}{ + 2x} + 4 && \text{Legger til $2x$ på hver side} \\
& \Updownarrow \\
7x - 3 &\geq 4 \\
& \Updownarrow \\
7x - 3 \textcolor{red}{ + 3} &\geq 4 \textcolor{red}{ + 3} && \text{Legger til $3$ på hver side} \\
& \Updownarrow \\
7x &\geq 7 \\
& \Updownarrow \\
\dfrac{\cancel{7}x}{\cancel{\textcolor{red}{7}}} &\geq \dfrac{7}{\textcolor{red}{7}} && \text{Deler med $7$ på hver side} \\
& \Updownarrow \\
x &\geq 1
\end{align*}

Vi kan oppgi løsningen enten som en ulikhet eller som en løsningsmengde

::::{tab-set}
:::{tab-item} Ulikhet
$$
x \geq 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left [1, \to \right \rangle
$$
:::
::::
:::::
::::::


## Oppgaver 

::::{admonition} Oppgave 1 
---
class: problem-level-1
---
Løs ulikhetene

Deloppgave 1
: $ x - 1 > 0$

`````{admonition} Fasit
:class: dropdown, answer
````{tab-set}
```{tab-item} Løsning som ulikhet
$$
x > 1
$$
```

```{tab-item} Løsningsmengde
$$
v \in \langle 1, \to \rangle
$$
```
````
`````

<br>

Deloppgave 2
: $ 2x - 3 \geq 1$

`````{admonition} Fasit
:class: dropdown, answer
````{tab-set}
```{tab-item} Løsning som ulikhet
$$
x \geq 2
$$
```

```{tab-item} Løsningsmengde
$$
x \in [ 2, \to \rangle
$$
```
````
`````

<br>

Deloppgave 3
: $ -x - 2 > -1$

`````{admonition} Fasit
:class: dropdown, answer
````{tab-set}
```{tab-item} Løsning som ulikhet
$$
 x < -1
$$
```

```{tab-item} Løsningsmengde
$$
x \in \langle \gets, -1 \rangle
$$
```
````
`````
::::

::::{admonition} Oppgave 2 
---
class: problem-level-2
---
Løs ulikhetene.

Deloppgave 1
: $ x + 1 > 2x + 4 $

`````{admonition} Fasit
:class: dropdown, answer
````{tab-set}
```{tab-item} Løsning som ulikhet
$$
x < -3
$$
```

```{tab-item} Løsningsmengde
$$
x \in \langle \gets, -3 \rangle
$$
```
````
`````
<br>

Deloppgave 2
: $ x + 1 < -x + 2 $

`````{admonition} Fasit
:class: dropdown, answer
````{tab-set}
```{tab-item} Løsning som ulikhet
$$
x < \frac{1}{2}
$$
```

```{tab-item} Løsningsmengde
$$
x \in \langle \gets, \frac{1}{2} \rangle
$$
```
````
`````
<br>

Deloppgave 3

: $1 - x < 1 + x$

`````{admonition} Fasit
:class: dropdown, answer
````{tab-set}
```{tab-item} Løsning som ulikhet
$$
x > 0
$$
```

```{tab-item} Løsningsmengde
$$
x \in \langle 0, \to \rangle
$$
```
````
`````

::::

::::{Admonition} Oppgave 3
---
class: problem-level-2
---
Løs ulikheten

$$ x + 1 \leq x + 3$$

`````{admonition} Fasit
:class: dropdown, answer
$$
x \in \mathbb{R}
$$

Tips: Hvis dette virker ulogisk, kan du forsøke å løse ulikheten grafisk!

`````
::::

::::{Admonition} Oppgave 4
---
class: problem-level-2
---
Sett opp ulikheter som har følgende løsningsmengder: 

`````{admonition} Tips
:class: dropdown, hint
Her finnes det flere mulige svar på hver oppgave. 

`````
Deloppgave 1
: $ \langle \gets, 4 \rangle $

<br>

Deloppgave 2
: $ [2, \to \rangle $

<br>

Deloppgave 3
: $ \langle \gets, -2]$

::::
