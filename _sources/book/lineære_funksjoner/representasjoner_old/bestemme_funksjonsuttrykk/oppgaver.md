# Oppgaver: Bestemme funksjonsuttrykk til lineære funksjoner


::::{admonition} Oppgave 1 
---
class: problem-level-1
---
Fyll ut tabellen nedenfor.


| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $(5, -3)$  | $(9, 5)$  |  |  |  |
| $g(x)$ | $(3, 2)$  | $(7, 2)$  |  |  |  |
| $h(x)$ | $(1, 1)$  | $(5, 5)$  |  |  |  |
| $p(x)$ | $(2, -4)$ |  $(-2, 4)$ |  |  |  |
| $q(x)$ | $(0, 3)$  | $(4, 1)$  |  |  |  |

:::{admonition} Fasit
---
class: answer, dropdown
---
| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $(5, -3)$  | $(9, 5)$  | $4$ | $8$ | $2$ |
| $g(x)$ | $(3, 2)$  | $(7, 2)$  | $4$ | $0$ | $0$ |
| $h(x)$ | $(1, 1)$  | $(5, 5)$  | $4$ | $4$ | $1$ |
| $p(x)$ | $(2, -4)$ |  $(-2, 4)$ | $-4$ | $8$ | $-2$ |
| $q(x)$ | $(0, 3)$  | $(4, 1)$  | $4$ | $-2$ | $-\dfrac{1}{2}$ |
:::
::::





---





:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1 
---
> Bruk {popup}`ettpunktsformelen<$$y - y_1 = a(x - x_1)$$>` til å bestemme funksjonsuttrykkene i oppgavene nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Grafen til en lineær funksjon $f$ har stigningstall $2$ og går gjennom punktet $(1, 2)$.

Bestem $f(x)$.

::::{answer}
$$
f(x) = 2x
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Grafen til en lineær funksjon $g$ har stigningstall $-3$ og går gjennom punktet $(2, 1)$. 

Bestem $g(x)$.

::::{answer}
$$
g(x) = -3x + 7
$$
::::


:::::::::::::



:::::::::::::{tab-item} c
Grafen til en lineær funksjon $h$ har stigningstall $1/2$ og går gjennom punktet $\left(3, -\dfrac{1}{2}\right)$. 

Bestem $h(x)$.


::::{answer}
$$
h(x) = \dfrac{1}{2}x - 2
$$
::::

:::::::::::::


::::::::::::::



:::::::::::::::




---




:::{admonition} Nyttige formler
---
class: hints, margin, dropdown
---
$$
a = \dfrac{y_2 - y_1}{x_2 - x_1}
$$

$$
y - y_1 = a(x - x_1)
$$
:::


:::::::::::::::{problem} Oppgave 3
---
level: 1
---
Grafen til en lineær funksjon $g$ går gjennom punktene $(1, 2)$ og $(5, 6)$.
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem stigningstallet til $g$.

::::{answer}
$$
a = 1
$$
::::



::::{solution}
Vi bruker topunktsformelen: 

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{6-2}{5-1} = \dfrac{4}{4} = 1
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem $g(x)$.

::::{answer}
$$
g(x) = x + 1
$$
::::


::::{solution}
Vi bruker ettpunktsformelen og får: 
\begin{align*}
y - y_1 &= a(x - x_1) \\
\\
y - 2 &= 1(x-1) \\
\\
y - 2 &= x - 1 \\
\\
y - 2 \textcolor{red}{+2} &= x - 1 \textcolor{red}{+2} \\
\\
y &=  x - 1 + 2 \\
\\
y &= x + 1 \\
\end{align*}

Dermed er 

$$
g(x) = x + 1
$$
::::

:::::::::::::





::::::::::::::

:::::::::::::::






---





:::::::::::::::{problem} Oppgave 4
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En lineær funksjon $f$ har stigningstall $7$ og skjærer $x$-aksen i $x = 2$. 
 
Bestem $f(x)$.


::::{answer}
$$
f(x) = 7x - 14
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
En lineær funksjon $g$ har stigningstall $3$ og skjærer $x$-aksen i $x = -2$.

Bestem $g(x)$.


::::{answer}
$$
g(x) = 3x + 6
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En lineær funksjon $h$ skjærer gjennom linja $y = 2$ når $x = 3$ og skjærer $x$-aksen i $x = 4$. 

Bestem $h(x)$.


::::{answer}
$$
h(x) = -2x + 8
$$
::::

:::::::::::::






::::::::::::::



:::::::::::::::







---



:::::::::::::::{problem} Oppgave 5
---
level: 2
---
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 3x - 2. 
$$

En **annen** lineær funksjon $g$ går gjennom punktene $(1, -1)$ og $(3, f(3))$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem stigningstallet til $g$.


::::{answer}
$$
a = 4
$$
::::


::::{solution}
Vi finner først 

$$
f(3) = 3\cdot 3 - 2 = 9 - 2 = 7.
$$ 

Deretter bruker vi topunktsformelen til å regne ut stigningstallet: 

$$
a = \dfrac{7 - (-1)}{3 - 1} = \dfrac{7 + 1}{2} = \dfrac{8}{2} = 4 
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $g(x)$.


::::{answer}
$$
g(x) = 4x - 5
$$
::::

::::{solution}
Vi bruker ettpunktsformelen med stigningstallet $a = 4$ og punktet $(1, -1)$ som gir:

\begin{align*}
y - y_1 &= a(x - x_1) \\
\\
y - (-1) &= 4(x - 1) \\
\\
y + 1 &= 4(x - 1) \\
\\
y + 1  &= 4x - 4 \\
\\
y &= 4x - 4 - 1 \\
\\
y &= 4x - 5 \\
\end{align*}

Altså er 

$$
g(x) = 4x - 5.
$$
::::

:::::::::::::




::::::::::::::
:::::::::::::::




---






:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
Grafene til to lineære funksjoner $f$ og $g$ er vist i {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-6`. Grafen til $f$ er parallell med grafen til $g$.

:::{figure} ./figurer/oppgaver/oppgave_6.svg
---
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-6
width: 80%
class: no-click, adaptive-figure
---
viser grafen til to lineære funksjoner $f$ og $g$. Grafen til $f$ og $g$ er parallelle.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f(x)$.

:::{answer}
$$
f(x) = -2x + 1
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $g(x)$. 

:::{answer}
$$
g(x) = -2x - 3
$$
:::

:::::::::::::

::::::::::::::


:::::::::::::::





---





:::::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---
Grafen til en lineær funksjon $g$ er vist i {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-7`.


:::{figure} ./figurer/oppgaver/oppgave_7.svg
---
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-7
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en lineær funksjon $g$, og to punkter på grafen.
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem hvor grafen til $g$ skjærer $y$-aksen.

:::{answer}
$$
y = -2
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
En annen funksjon $h$ er parallell med grafen til $g$ og skjærer $y$-aksen i $y = 2$. 

Bestem $h(x)$.


::::{answer}
$$
h(x) = 3x + 2
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::






::::{admonition} Oppgave 8
---
class: problem-level-3
---
Grafene til to lineære funksjoner $f$ og $g$ er vist i {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-8`. 
Avstanden fra origo til det nærmeste punktet på de to grafene er det samme. Grafene er parallelle.

Bestem $f(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_8.svg
---
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-8
width: 80%
class: no-click, adaptive-figure
---
viser grafene til to lineære funksjoner $f$ og $g$. Avstanden fra origo til det nærmeste punktet på de to grafene er det samme. Grafene er parallelle.
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = x + 2
$$
:::
::::

::::{admonition} Oppgave 9
---
class: problem-level-2
---
Under vises et program som regner ut funksjonsuttrykket til en lineær funksjon $f$, men programmet er plassert i tilfeldig rekkefølge.


`````{tab-set}
---
class: tabs-parts
---
````{tab-item} a
Løs puslespillet ved å sette kodelinjene i riktig rekkefølge. <br> Forutsi hva som skrives ut av programmet. Kjør programmet og sjekk svaret! 

````

````{tab-item} b
Endre programmet slik at det finner funksjonsuttrykket til en lineær funksjon som går gjennom punktene $(1, 2)$ og $(3, 6)$. <br> Sjekk at programmet finner riktig funksjon ved regning.

:::{admonition} Løsning
---
class: solution, dropdown
---
Vi finner først stigningstallet ved hjelp av topunktsformelen: 

$$ a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{6-2}{3-1}=\dfrac{4}{2}=2 $$

Deretter bruker vi ettpunktsformelen og får: 

\begin{align*}
y - y_1 &= a (x - x_1) \\
\\
y - 2 &= 2(x-1)\\
\\
y - 2 &= 2x - 2 \\
\\
y - 2 \textcolor{red}{+2} &= 2x - 2\textcolor{red}{+2} \\
\\
y &= 2x
\end{align*}

Vi ser at det gir funksjonen $y = f(x) = 2x$.
:::
````

````{tab-item} c
Kan du forklare kodelinjen `b = y1 - a * x1`{l=python}? <br> Hva representerer variabelen `b`{l=python}? <br> Kan du komme fram til formelen?

:::{admonition} Løsning
---
class: solution, dropdown
---
Ved å skrive om ettpunktsformelen, ser vi at
\begin{align*}
y - y_1 &= a(x - x_1) \\
\\
y - y_1 \textcolor{green}{+ y_1} &= a(x - x_1) \textcolor{green}{+ y_1} && \text{Legger til $y_1$ på hver side} \\
\\
y &= a(x - x_1) + y_1 \\
\\
y &= ax + \underbrace{\textcolor{red}{(y_1 - a \cdot x_1)}}_{\displaystyle b} && \text{Ganget ut parentesen}
\end{align*}

Vi kan se at det som står i rødt må være konstantleddet ved å sammenligne med den generelle formen:

$$
y = ax + b.
$$

Dermed har vi at

$$
b = y_1 - a \cdot x_1.
$$

Linjen `b = y1 - a * x1`{l=python} regner derfor ut konstantleddet til funksjonen. 
:::
````

`````


:::{raw} html
---
file: interaktiv_kode/oppgaver/oppgave_9.html
---
:::


::::

