# Oppgaver: <br> $abc$-formelen

:::::::::::::::{admonition} Oppsummering
---
class: summary
---

::::::::::::::{tab-set}

:::::::::::::{tab-item} $abc$-formelen

For en andregradslikning som er skrevet på formen

$$
ax^2 + bx + c = 0
$$

er løsningen

$$
x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

:::::::::::::

:::::::::::::{tab-item} Antall løsninger og diskriminanten

For en andregradslikning som er skrevet på formen

$$
ax^2 + bx + c = 0
$$

kan vi bestemme antall løsninger ved å regne ut diskriminanten

$$
D = b^2 - 4ac
$$

| Antall løsninger |Diskriminant $D$ |
|-------------------|---------------------|
| To løsninger      | $D > 0$             |
| Én løsning        | $D = 0$             |
| Ingen løsninger   | $D < 0$             |

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Løs likningene ved bruk av $abc$-formelen.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
$$
x^2 - 5x + 6 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 2 \, \lor \, x = 3
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
$$
x^2 - 3x - 4 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \{-1, 4\}
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
$$
x^2 - x - 6 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -2 \, \lor \, x = 3
$$
:::
:::::::::::::

:::::::::::::{tab-item} d
$$
x^2 - 4x - 5 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \, \lor \, x = 5
$$
:::
:::::::::::::

::::::::::::::
:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---

Løs likningene ved hjelp av $abc$-formelen.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
2x^2 - 5x + 2 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \dfrac{1}{2} \, \lor \, x = 2
$$
:::

:::::::::::::


:::::::::::::{tab-item} b

$$
3x^2 - 7x + 2 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \left\{\dfrac{1}{3}, 2\right\}
$$
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
For hver av likningene, bestem hvor mange løsninger likningen har ved hjelp av diskriminanten.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
x^2 - 8x + 16 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
Én løsning siden $D = 0$. 
:::

:::::::::::::

:::::::::::::{tab-item} b

$$
x^2 - 10x + 24 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
To løsninger siden $D > 0$.
:::

:::::::::::::

:::::::::::::{tab-item} c

$$
4x^2 + 5x + 8 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
Ingen løsning siden $D < 0$.
:::

:::::::::::::


::::::::::::::
:::::::::::::::


---


::::{admonition} Oppgave X
---
class: problem-level-2
---
Bestem $k$ slik at andregradslikningen

$$
x^2 + kx + 6 = 0
$$

har én løsning. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
k = \pm 2\sqrt{6}
$$
:::
::::

---


:::::::::::::::{admonition} Oppgave XX
---
class: problem-level-2
---
En elev har skrevet et program for å løse andregradslikninger med $abc$-formelen, men har rotet det til og har fått kodelinjene i tilfeldig rekkefølge.


:::{raw} html
---
file: ./python/abc_formelen/abc_formelen.html
---
:::

:::::::::::::::
