# Oppgaver: Polynomfunksjoner

:::::::::::::::{exercise} Oppgave 1
---
level: 1
---


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

Grafen til en tredjegradsfunksjon $f$ er vist i {numref}`fig-polynomer-polynomfunksjoner-oppgave-1-a`.

Bestem $f(x)$.

:::{figure} ./figurer/oppgaver/oppgave_1/a.svg
---
name: fig-polynomer-polynomfunksjoner-oppgave-1-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $f$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = \dfrac{1}{2}(x + 2)(x - 1)(x - 3)
$$
::::

:::::::::::::

:::::::::::::{tab-item} b

Grafen til en tredjegradsfunksjon $g$ er vist i {numref}`fig-polynomer-polynomfunksjoner-oppgave-1-b`.

Bestem $g(x)$.

:::{figure} ./figurer/oppgaver/oppgave_1/b.svg
---
name: fig-polynomer-polynomfunksjoner-oppgave-1-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $g$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(x) = -\dfrac{1}{4}(x - 3)^2(x + 2)
$$
::::

:::::::::::::

:::::::::::::{tab-item} c

Grafen til en tredjegradsfunksjon $h$ er vist i {numref}`fig-polynomer-polynomfunksjoner-oppgave-1-c`.

Bestem $h(x)$.

:::{figure} ./figurer/oppgaver/oppgave_1/c.svg
---
name: fig-polynomer-polynomfunksjoner-oppgave-1-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $h$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) = -\dfrac{1}{2}(x + 2)(x + 3)(x - 1)
$$
::::

:::::::::::::

:::::::::::::{tab-item} d

Grafen til en tredjegradsfunksjon $p$ er vist i {numref}`fig-polynomer-polynomfunksjoner-oppgave-1-d`.

Bestem $p(x)$.

:::{figure} ./figurer/oppgaver/oppgave_1/d.svg
---
name: fig-polynomer-polynomfunksjoner-oppgave-1-d
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $p$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
p(x) = -(x + 2)^3
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Grafen til en tredjegradsfunksjon $f$ gitt ved 

$$
f(x) = ax^3 + bx^2 + cx + d, 
$$

er vist i 

:::{figure} ./figurer/oppgaver/oppgave_2/graf.svg
---
name: fig-polynomer-polynomfunksjoner-oppgave-2
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $f$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Sett opp en likningssystem for koeffisientene uttrykt ved $f(x)$. 

> Det vil si, én av likningene blir $f(-3) = -2$ siden grafen går gjennom $(-3, -2)$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(-3) = -2 \and f(-2) = 3 \and f(-1) = 2 \and f(0) = 1. 
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
> Her skal du bruke CAS til å bestemme koeffisientene til $f(x)$.

Bestem $f(x)$.

:::{cas-popup} 350 500
:::


::::{answer}
$$
f(x) = x^3 + 3x^2 + x + 1. 
$$
::::

::::{solution}
Vi skriver inn et generelt funksjonsuttrykk og likningene i CAS, og løser deretter likningssystemet:

:::{figure} ./figurer/oppgaver/oppgave_2/sol.png
---
width: 60%
class: no-click, adaptive-figure
---
:::

som betyr at 

$$
a = 1 \and b = 3 \and c = 1 \and d = 1.
$$

Dermed er 

$$
f(x) = x^3 + 3x^2 + x + 1. 
$$
::::



:::::::::::::
::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
---
level: 2
---
> Bruk CAS til å bestemme funksjonsuttrykkene for hver av funksjonene nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Grafen til en tredjegradsfunksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$.

:::{cas-popup} 350 500
:::


:::{figure} ./figurer/oppgaver/oppgave_3/a.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::

:::::::::::::{tab-item} b
Grafen til en tredjegradsfunksjon $g$ er vist i figuren nedenfor.

Bestem $g(x)$.

:::{cas-popup} 350 500
:::


:::{figure} ./figurer/oppgaver/oppgave_3/b.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{tab-item} c
Grafen til en tredjegradsfunksjon $h$ er vist i figuren nedenfor.

Bestem $h(x)$.

:::{cas-popup} 350 500
:::


:::{figure} ./figurer/oppgaver/oppgave_3/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{tab-item} d
Grafen til en tredjegradsfunksjon $p$ er vist i figuren nedenfor.

Bestem $p(x)$.

:::{cas-popup} 350 500
:::


:::{figure} ./figurer/oppgaver/oppgave_3/d.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::

::::::::::::::



:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 4
---
level: 2
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = -(x + 1)(x - 1)(x - 2).
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktene til $f$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 0 \liff x = -1 \or x = 1 \or x = 2.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Tegn en fortegnslinje for $f(x)$ inkludert faktorene til $f$.

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/oppgaver/oppgave_4/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::

:::::::::::::{tab-item} c
Lag en **skisse** av grafen til $f$. 


::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/oppgaver/oppgave_4/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::

:::::::::::::{tab-item} d
Løs ulikheten 

$$
f(x) > 0. 
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle \gets, -1 \rangle \cup \langle 1, 2 \rangle.
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 5
---
level: 2
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = (x - 1)^2 (x + 3)
$$

::::::::::::::{tab-set} 
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktene til $f$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 0 \liff x = 1 \or x = -3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Tegn et fortegnsskjema for $f(x)$. 

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/oppgaver/oppgave_5/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::


:::::::::::::


:::::::::::::{tab-item} c
Tegn en **skisse** av grafen til $f$.

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/oppgaver/oppgave_5/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten

$$
f(x) > 0. 
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
> Det holder med ett av alternativene under.

$$
x \in \langle -3, \to \rangle \setminus \{1\} \liff x > -3 \and x \neq 1.
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
En fjerdegradsfunksjon $f$ er gitt ved

$$
f(x) = (x + 1)^2(x - 2)(x - 3). 
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktene til $f$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 0 \liff x = -1 \or x = 2 \or x = 3.
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
Tegn et fortegnsskjema for $f(x)$, inkludert faktorene i $f(x)$.

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/oppgaver/oppgave_6/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::

:::::::::::::{tab-item} c
Tegn en **skisse** av grafen til $f$.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_6/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::


:::::::::::::

:::::::::::::{tab-item} d
Løs ulikheten 

$$
f(x) \leq 0. 
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
> Det holder med ett av alternativene under. 

$$
x \in [2, 3] \cup \{-1\} \liff -2 \leq x \leq 3 \or x = -1.
$$
:::

:::::::::::::

::::::::::::::

:::::::::::::::
