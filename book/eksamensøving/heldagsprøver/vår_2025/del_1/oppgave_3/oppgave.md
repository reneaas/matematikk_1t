:::::::::::::::{admonition} Oppgave 3
---
class: check
---
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

:::{figure} ./figurer/del_1/oppgave_3/figur.svg
---
width: 80%
class: no-click
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f(x)$.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å velge en gyldig fremgangsmåte.
* 1 poeng for å bestemme riktig $f(x)$.
:::::

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -(x + 2)(x - 4) = -x^2 + 2x + 8.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $f$ skjærer $x$-aksen i $x = - 2$ og $x = 4$ som betyr at vi kan skrive $f(x)$ på nullpunktsform:

$$
f(x) = a(x + 2)(x - 4). 
$$

Grafen til $f$ skjærer $y$-aksen i $y = 8$ som betyr at 

$$
f(0) = 8 \liff a(0 + 2)(0 - 4) = 8 \liff -8a = 8 \liff a = -1.
$$

Dermed følger det at 

$$
f(x) = -(x + 2)(x - 4) = -x^2 + 2x + 8.
$$
:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem likningen til tangenten i $(3, f(3))$. 


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å bestemme $AC$ med en gyldig strategi.
* 1 poeng for riktig likning for tangenten.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -4x + 17.
$$
:::::


::::::{admonition} Løsning
---
class: solution, dropdown
---
:::::{tab-set}
::::{tab-item} Strategi 1: Den deriverte
For å bestemme likningen til tangenten i $(3, f(3))$ må vi finne $y$-koordinaten til punktet og stigningstallet til tangenten.

$$
y_1 = f(3)  = -(3 + 2)(3 - 4) = 5.
$$

Stigningstallet $a$ til tangenten er gitt ved den deriverte i $x = 3$:

\begin{align*}
f'(x) &= -2x + 2 \\
\\
a = f'(3) &= -2(3) + 2 = -6 + 2 = -4.
\end{align*}

Vi bruker ettpunktsformelen til å bestemme likningen 

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    y - 5 &= -4(x - 3) \\
    y - 5 &= -4x + 12 \\
    y &= -4x + 17.
\end{align*}

Altså er likningen til tangenten

$$
y = -4x + 17.
$$

::::

::::{tab-item} Strategi 2: Polynomdivisjon
Resten i polynomdivisjonen $f(x) : (x - 3)^2$ gir oss uttrykket for tangenten i $x = 3$.

:::{figure} ./koder/del_1/oppgave_3/polydiv.svg
---
width: 80%
class: no-click
---
:::

Fra resten i polynomdivisjonen finner vi at likningen er 

$$
y = -4x + 17.
$$

::::
:::::
::::::

:::::::::::::

::::::::::::::

:::::::::::::::

