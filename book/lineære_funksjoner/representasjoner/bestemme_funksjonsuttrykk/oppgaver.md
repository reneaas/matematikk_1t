# Oppgaver: Bestemme funksjonsuttrykk til lineære funksjoner


::::{admonition} Oppgave 1 
---
class: problem-level-1
---
Fyll ut tabellen under.


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

::::{admonition} Oppgave 2
---
class: problem-level-1 
---

Deloppgave 1

: Grafen til en lineær funksjon $f$ har stigningstall $2$ og går gjennom punktet $(1, 2)$. <br> Bestem $f(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$f(x)=2x$$
:::

<br>

Deloppgave 2
: Grafen til en lineær funksjon $g$ har stigningstall $-3$ og går gjennom punktet $(2, 1)$. <br> Bestem $g(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---

$$
g(x) = -3x + 7
$$

:::

<br>

Deloppgave 3
: Grafen til en lineær funksjon $h$ har stigningstall $1/2$ og går gjennom punktet $\left(3, -\dfrac{1}{2}\right)$. <br> Bestem $h(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) = \dfrac{1}{2}x - 2
$$
:::


::::

---

::::{admonition} Oppgave 3
---
class: problem-level-1
---
Grafen til en lineær funksjon $g$ går gjennom punktene $(1, 2)$ og $(5, 6)$.

Deloppgave 1
: Bestem stigningstallet til $g$.

:::{admonition} Fasit
---
class: answer, dropdown
---
Stigningstallet er $1$. 
:::
:::{admonition} Løsningsforslag
---
class: solution, dropdown
---
Vi bruker topunktsformelen og får: 

$$ a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{6-2}{5-1}=\dfrac{4}{4}=1$$

:::
<br>

Deloppgave 2
: Bestem $g(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$g(x) = x + 1$
:::
:::{admonition} Løsningsforslag
---
class: solution, dropdown
---
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
:::
::::

---

::::{admonition} Oppgave 4
---
class: problem-level-2
---

Deloppgave 1
: En lineær funksjon $f$ har stigningstall $7$ og skjærer $x$-aksen i $x = 2$. <br> Bestem $f(x)$.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 7x - 14
$$

:::

<br>

Deloppgave 2
: En lineær funksjon $g$ har stigningstall $3$ og skjærer $x$-aksen i $x = -2$. <br> Bestem $g(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---

$$
g(x) = 3x + 6
$$

:::

<br>

Deloppgave 3
: En lineær funksjon $h$ skjærer gjennom linja $y = 2$ når $x = 3$ og skjærer $x$-aksen i $x = 4$. <br> Bestem $h(x)$.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) = -3x + 12
$$
:::

::::

---

::::{admonition} Oppgave 5
---
class: problem-level-2
---
En lineær funksjon er gitt ved 

$$
f(x) = 3x - 2.
$$

En annen lineær funksjon $g$ går gjennom punktene $(1, -1)$ og $(3, f(3))$.

Deloppgave 1
: Bestem stigningstallet til $g$.

:::{admonition} Fasit
---
class: answer, dropdown
---
Stigningstallet til $g(x)$ er $4$. 
:::
:::{admonition} Løsningsforslag
---
class: solution, dropdown
---
Vi finner først $f(3)=2\cdot 3 - 2 = 9-2 = 7$. 

Deretter bruker vi topunktsformelen og får: 

$$ a = \dfrac{7-(-1)}{3-1}=\dfrac{7+1}{2}=\dfrac{8}{2}=4 $$

Stigningstallet til $g(x)$ er $4$. 
:::

<br>

Deloppgave 2
: Bestem $g(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$g(x) = 4x-5$. 
:::

:::{admonition} Løsningsforslag
---
class: solution, dropdown
---
Vi bruker ettpunktsformelen når vi kjenner stigningstallet $a = 4$ og punktet $(1, -1)$ og får 

\begin{align}
y - y_1 &= a(x - x_1) \\
y - (-1) &= 4(x-1) \\
y + 1 &= 4x - 4 \\
y +1 \textcolor{red}{-1} &= 4x - 4  \textcolor{red}{-1}\\
y &= 4x - 5
\end{align}

Vi får da at $g(x) = 4x-5$. 
:::
::::

---

::::{admonition} Oppgave 6
---
class: problem-level-2
---
Grafen til en lineær funksjon $f$ er vist i {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-6`.

Bestem $f(x)$.

:::{figure} ./figurer/oppgaver/oppgave_6.svg
---
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-6
width: 80%
---
viser grafen til en lineær funksjon $f$ og to punkter på grafen.
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -2x + 1
$$
:::
::::


---

::::{admonition} Oppgave 7
---
class: problem-level-2
---
Grafen til en lineær funksjon $g$ er vist i {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-7`.

Bestem hvor grafen til $g$ skjærer $y$-aksen. 

:::{figure} ./figurer/oppgaver/oppgave_7.svg
---
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-7
width: 80%
---
viser grafen til en lineær funksjon $g$, og to punkter på grafen.
:::

:::{admonition} Fasit
---
class: answer, dropdown
---

:::
::::

---

::::{admonition} Oppgave 8
---
class: problem-level-2
---
Grafen til en lineær funksjon $h$ er vist i {numref}`fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-8`.
Stigningstallet til $h$ er $1/2$.

Bestem $x_2$.

:::{figure} ./figurer/oppgaver/oppgave_8.svg
---
name: fig-lineære-funksjoner-representasjoner-bestemme-funksjonsuttrykk-oppgave-8
width: 80%
---
viser grafen til en lineær funksjon $h$ og to punkter på grafen.
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x_2 = 3
$$
:::
::::

::::{admonition} Oppgave 8
---
class: problem-level-2
---

Under vises et program som regner ut funksjonsuttrykket til et lineær funksjon $f$. <br> Men! Kodelinjene er plassert i tilfeldig rekkefølge. 

Deloppgave 1
: Løs puslespillet ved å sette kodelinjene i riktig rekkefølge. <br> Forutsi hva som skrives ut av programmet. Kjør programmet og sjekk svaret! 

<br>

:::{raw} html
---
file: interaktiv_kode/oppgaver/oppgave_6.html
---
:::

<br>

Deloppgave 2
: Endre programmet slik at det finner funksjonsuttrykket til en lineær funksjon som går gjennom punktene $(1, 2)$ og $(3, 6)$. <br> Sjekk at programmet finner riktig funksjon ved regning.

:::{admonition} Løsningsforslag
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
<br>

Deloppgave 3
: Kan du forklare kodelinjen `b = y1 - a * x1`{l=python}? <br> Hva representerer variabelen `b`{l=python}? <br> Kan du komme fram til formelen?

:::{admonition} Løsningsforslag
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
y &= ax + \textcolor{red}{(y_1 - a \cdot x_1)} && \text{Ganget ut parentesen}
\end{align*}

Sammenligner vi med den generelle måten å skrive en lineær funksjon på:

$$
y = ax + b
$$

må dette bety at det som står i rødt representerer konstantleddet $b$. Dermed har vi at

$$
b = y_1 - a \cdot x_1
$$

Linjen `b = y1 - a * x1`{l=python} regner derfor ut konstantleddet til funksjonen. 
:::
::::

