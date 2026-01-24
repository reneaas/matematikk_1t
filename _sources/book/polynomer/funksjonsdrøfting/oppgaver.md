# Oppgaver: Funksjonsdrøfting


:::::::::::::::{exercise} Oppgave 1
En tredjegradsfunksjon $f$ er gitt ved

$$
f(x) = x^3 - 12x + 2.
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.


::::{answer}
* Toppunkt i $(-2, 18)$
* Bunnpunkt i $(2, -14)$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til eventuelle vendepunkter på grafen til $f$.

::::{answer}
Vendepunkt i $(0, 2)$.
::::

:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
En funksjon $f$ er gitt ved

$$
f(x) = x^3 - 6x^2 + 3.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.


::::{answer}
* Toppunkt i $(0, 3)$
* Bunnpunkt i $(4, -29)$.
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem koordinatene til eventuelle vendepunkter på grafen til $f$.


::::{answer}
Vendepunkt i $(2, -13)$.

::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem likningene til eventuelle vendetangenter til grafen til $f$.


::::{answer}
$$
y = -12x + 11
$$
::::


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::



En tredjegradsfunksjon $f$ er gitt ved

$$
f(x) = ax^3 + bx^2 + cx + d
$$

Om funksjonen får du vite at

* Grafen til $f$ har et toppunkt i $(-1, 4)$.
* Grafen til $f$ har et vendepunkt i $(2, 1)$.

Bestem $a$, $b$, $c$ og $d$.

::::{answer}
$$
a = \dfrac{1}{18} \and b = -\dfrac{1}{3} \and c = -\dfrac{5}{6} \and d = \dfrac{32}{9}
$$
::::
:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


En tredjegradsfunksjon $g$ er gitt ved

$$
g(x) = ax^3 + bx^2 + cx + d
$$

Om funksjonen $g$ får du vite at
* Grafen til $g$ har et bunnpunkt i $(1, -2)$.
* Grafen til $g$ har en vendetangent i punktet $(3, g(3))$ med likningen $y = \dfrac{9}{2}x - \dfrac{19}{2}$.


Bestem $g(x)$.


::::{answer}
$$
g(x) = -\dfrac{3}{8}x^3 + \dfrac{27}{8}x^2 - \dfrac{45}{8}x + \dfrac{5}{8}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::



En tredjegradsfunksjon $h$ er gitt ved


$$
h(x) = ax^3 + bx^2 + cx + d
$$

Om funksjonen $h$ får du vite at

* Grafen til $h$ har et bunnpunkt i $(3, -28)$.
* Grafen til $h$ har et vendepunkt i $(1, -12)$.

Bestem $a$, $b$, $c$ og $d$.


::::{answer}
$$
a = 1 \and b = -3 \and c = -9 \and d = -1
$$
::::


:::::::::::::


:::::::::::::{tab-item} d

:::{cas-popup}
---
layout: sidebar
---
:::



En tredjegradsfunksjon $p$ er gitt ved

$$
p(x) = ax^3 + bx^2 + cx + d
$$

Om funksjonen $p$ får du vite at
* Grafen til $p$ har stasjonære punkter i $(-3, p(-3))$ og $(1, p(1))$.
* Grafen til $p$ har en vendetangent i punktet $(-1, p(-1))$ med likningen $y = -12x - 21$.


Bestem $p(x)$.


::::{answer}
$$
p(x) = x^3 + 3x^2 - 9x - 20
$$
::::

:::::::::::::


::::::::::::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
En fjerdegradsfunksjon $f$ er gitt ved

$$
f(x) = x^4 - 4x^3 + 10.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.


::::{answer}
Bunnpunkt i $(3, -17)$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til eventuelle vendepunkter på grafen til $f$.


::::{answer}
Vendepunkter i $(0, 10)$ og $(2, -6)$.
::::

:::::::::::::


::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5
En funksjon $f$ er gitt ved

$$
f(x) = x^3 + 4x^2 - 3x - 18
$$

Avgjør hvilken av grafene nedenfor som viser grafen til $f$.


::::{multi-plot2}
---
rows: 2
cols: 2
ticks: off
ymax: 20
ymin: -20
fontsize: 30
---
:::{plot}
function: (x - 2)**2 * (x + 3)
text: 5, 15, "A", center-center, bbox
:::

:::{plot}
function: (x - 2) * (x + 3)**2
text: 5, 15, "B", center-center, bbox
:::

:::{plot}
function: -(x - 2)**2 * (x + 3)
text: 5, 15, "C", center-center, bbox
:::

:::{plot}
function: x**3 + 6 * x**2 - 18
text: 5, 15, "D", center-center, bbox
:::



::::


::::{answer}
Graf B.
::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
En funksjon $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 + 1.
$$

Avgjør hvilken av grafene nedenfor som viser grafen til $f$.


::::{multi-plot2}
---
rows: 2
cols: 2
ymin: -10
ymax: 10
ticks: off
fontsize: 30
---
:::{plot}
function: -x**3 + 3 * x**2 - 1
text: 5, 8, "A", center-center, bbox
:::

:::{plot}
function: x**3 + 3 * x**2 - 4
text: 5, 8, "B", center-center, bbox
:::


:::{plot}
function: x**3 - 3 * x**2 + 1
text: 5, 8, "C", center-center, bbox
:::


:::{plot}
function: x**3 - 6*x + 2
text: 5, 8, "D", center-center, bbox
:::

::::


::::{answer}
Graf C.
::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 7
For en funksjon $f$, er den deriverte $f'$ gitt ved

$$
f'(x) = x^3 - 2x^2 - x + 2.
$$

Avgjør hvilken av grafene nedenfor som viser grafen til $f$.

::::{multi-plot2}
---
rows: 2
cols: 2
ymin: -8
ymax: 8
ticks: off
grid: off
fontsize: 30
---
:::{plot}
function: 1/4 * x**4 + 2/3 * x**3 - 1/2 * x**2 - 2*x - 5
text: 5, 6, "A", center-center, bbox
:::

:::{plot}
function: -(1/4 * x**4 + 2/3 * x**3 - 1/2 * x**2 - 2*x - 5)
text: 5, 6, "B", center-center, bbox
:::

:::{plot}
function: 1/4 * x**4 - 2/3 * x**3 - 1/2 * x**2 + 2*x - 5
text: 5, 6, "C", center-center, bbox
:::

:::{plot}
function: -(1/4 * x**4 - 2/3 * x**3 - 1/2 * x**2 + 2*x - 5)
text: 5, 6, "D", center-center, bbox
:::

::::


::::{answer}
Graf C.
::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
Funksjonen $f$ er gitt ved

$$
f(x) = 2x^3 - 3x^2 - 12x + 6.
$$

Avgjør hvilken av grafene nedenfor som viser grafen til $f'$.


::::{multi-plot2}
---
rows: 2
cols: 2
ymax: 16
ymin: -16
ticks: off
fontsize: 30
---

:::{plot}
function: -6 * (x - 2) * (x + 1)
text: 5, 15, "A", center-center, bbox 
:::


:::{plot}
function: -6 * (x + 2) * (x - 1)
text: 5, 15, "B", center-center, bbox 
:::

:::{plot}
function: 6 * (x + 2) * (x - 1)
text: 5, 15, "C", center-center, bbox 
:::

:::{plot}
function: 6 * (x - 2) * (x + 1)
text: 5, 15, "D", center-center, bbox 
:::

::::


::::{answer}
Graf D.
::::


:::::::::::::::

