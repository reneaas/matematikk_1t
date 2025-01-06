# Oppgaver: Polynomfunksjoner

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
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
class: no-click
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
class: no-click
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
class: no-click
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
class: no-click
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

:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
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
class: no-click
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
Bruk CAS til å bestemme $f(x)$. 
> Som vanlig, velg mellom CAS i Geogebra eller Python. 

````{tab} Python

:::{raw} html
---
file: ./python/oppgaver/oppgave_2/b.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

:::{code-block} python
---
linenos: true
---
from casify import *

f = funksjon("a * x**3 + b * x**2 + c * x + d")

koeffs = løs("f(-3) = -2", "f(-2) = 3", "f(-1) = 2", "f(0) = 1")

print(koeffs)
:::

**Utskrift**:

:::{code-block} console
a = 1 ∧ b = 3 ∧ c = 1 ∧ d = 1
:::

**Koeffisienter**:

$$
a = 1 \and b = 3 \and c = 1 \and d = 1.
$$

**Funksjonsuttrykk**:

$$
f(x) = x^3 + 3x^2 + x + 1. 
$$
::::

````


````{tab} Geogebra

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_2/b.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**Koeffisienter**:

$$
a = 1 \and b = 3 \and c = 1 \and d = 1.
$$

**Funksjonsuttrykk**:

$$
f(x) = x^3 + 3x^2 + x + 1. 
$$
::::

````


:::::::::::::
::::::::::::::

:::::::::::::::



:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
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

:::{figure} ./figurer/oppgaver/oppgave_3/b.svg
---
width: 100%
class: no-click
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

:::{figure} ./figurer/oppgaver/oppgave_3/c.svg
---
width: 80%
class: no-click
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

:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
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

:::{figure} ./figurer/oppgaver/oppgave_4/b.svg
---
width: 100%
class: no-click
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

:::{figure} ./figurer/oppgaver/oppgave_4/c.svg
---
width: 80%
class: no-click
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


:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
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

:::{figure} ./figurer/oppgaver/oppgave_5/b.svg
---
width: 100%
class: no-click
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
:::{figure} ./figurer/oppgaver/oppgave_5/c.svg
---
width: 80%
class: no-click
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
