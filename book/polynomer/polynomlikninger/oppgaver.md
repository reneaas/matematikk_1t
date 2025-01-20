# Oppgaver: Polynomlikninger


:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 + 4x^2 + x - 6
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Skriv ned alle *mulige* heltallsrøtter til $f$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}. 
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
De mulige heltallsrøttene til $f$ er tall som deler konstantleddet $-6$. Alle hele tall som deler $-6$ er gitt ved 

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}. 
$$
:::::::::::::

:::::::::::::{tab-item} b
Ta utgangspunkt i listen fra **a** og finn én rot til $f(x)$. 

Bruk polynomdivisjon til å faktorisere $f(x)$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
Én mulighet er $x = 1$, som gir

$$
x^3 + 4x^2 + x - 6 = (x - 1)(x^2 + 5x + 6)
$$

:::

::::{admonition} Løsning
---
class: solution, dropdown
---
En av røttene til $f(x)$ er $x = 1$. Det kan vi se enten med et Horner-skjema eller vanlig polynomdivisjon:

````{tab} Horner-skjema

:::{figure} ./koder/oppgaver/oppgave_1/b.svg
---
width: 50%
class: no-click
---
:::

````

````{tab} Vanlig polynomdivisjon

:::{figure} ./koder/oppgaver/oppgave_1/b_polydiv.svg
---
width: 90%
class: no-click
---
:::

````

Dette betyr at 

$$
(x^3 + 4x^2 + x - 6) = (x - 1)(x^2 + 5x + 6)
$$

::::

:::::::::::::

:::::::::::::{tab-item} c
Finn resten av nullpunktene til $f$. 

Hvis nullpunktene er heltallige, sjekk at de også er en del av listen fra **a**.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 1 \or x = -2 \or x = -3
$$
:::


:::{admonition} Løsning
---
class: answer, dropdown
---
Vi bruker $abc$-formelen med andregradspolynomet for å finne de resterende røttene til $f$:

$$
x^2 + 5x + 6 = 0
$$

som gir 

$$
x = \dfrac{-5 \pm \sqrt{5^2 - 4 \cdot 1 \cdot 6}}{2} = \dfrac{-5 \pm \sqrt{1}}{2} = \dfrac{-5 \pm 1}{2}
$$

som gir 

$$
x = -2 \or x = -3. 
$$

Samtidig fant vi tidligere at $x = 1$ også var en rot, så dermed har vi 

$$
x = 1 \or x = -2 \or x = -3
$$
:::

:::::::::::::




::::::::::::::



:::::::::::::::


---

:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-2
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 - 4x + 12. 
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem alle røttene til $f(x)$ og faktoriser $f(x)$ i lineære faktorer.

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 2 \or x = -2 \or x = 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Tegn et fortegnsskjema for $f(x)$. 


::::{admonition} Fasit
---
class: dropdown, answer
---

:::{figure} ./figurer/oppgaver/oppgave_2/b.svg
---
width: 100%
class: no-click
---
:::

::::

:::::::::::::


:::::::::::::{tab-item} c
Lag en **skisse** av grafen til $f$. Marker nullpunktene. 


::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/oppgaver/oppgave_2/c.svg
---
width: 80%
class: no-click
---
:::

::::


:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten $f(x) \geq 0$. 


::::{admonition} Fasit
---
class: answer, dropdown
---

$$
x \in [-2, 2] \cup [3, \to \rangle
$$

::::

:::::::::::::

::::::::::::::




:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-2
---
En tredjegradsfunksjon er gitt ved 

$$
f(x) = -2x^3 + 14x^2 - 14x - 30. 
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem alle røttene til $f(x)$. 

> Husk å se på en tredjegradslikning der den ledende koeffisienten er $1$ når du leter etter heltallsrøtter.


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -1 \or x = 3 \or x = 5. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten $f(x) \leq 0$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
-1 \leq x \and x \leq 3 \or 5 \leq x. 
$$
::::
:::::::::::::

::::::::::::::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 4 
---
class: problem-level-2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Løs tredjegradslikningen 

$$
x^3 - x^2 - 2x + 2 = 0. 
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 1 \or x = -\sqrt{2} \or x = \sqrt{2}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Løs ulikheten 

$$
x^3 - x^2 - 2x + 2 > 0. 
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -\sqrt{2}, 1 \rangle \cup \langle \sqrt{2}, \to \rangle
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
En likning er gitt ved

$$
x^3 - 3x - 2 = (x + 1)(ax^2 + bx + c). 
$$



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$, $b$ og $c$ slik at likningen er en **identitet**.


:::{admonition} Fasit
---
class: dropdown, answer
---
Én mulighet er 

$$
x^3 - 3x - 2 = (x + 1)(x^2 - x - 2). 
$$

som gir

$$
a = 1 \and b = -1 \and c = -2.
$$


:::

:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten 

$$
x^3 - 3x - 2 < 0. 
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle \gets, 2\rangle \setminus \{-1\}. 
$$
:::

:::::::::::::

::::::::::::::


:::::::::::::::








:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
En fjerdegradslikning er gitt ved 

$$
x^4 + 3x^3 - 15x^2 - 19x + 30 = 0.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en liste over alle *mulige* heltallige løsninger til likningen. 

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 5, \pm 6, \pm 10, \pm 15, \pm 30\}.
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Finn én løsning til likningen og faktoriser fjerdegradspolynomet i én lineær faktor og et tredjegradspolynom. 

::::{admonition} Fasit
---
class: dropdown, answer
---
$x = 1$ løser likningen. Fjerdegradspolynomet kan da skrives som 

$$
(x^4 + 3x^3 - 15x^2 - 19x + 30) = (x - 1)(x^3 + 4x^2 - 11x - 30).
$$
::::


:::::{admonition} Løsning
---
class: dropdown, solution
---
$x = 1$ er en løsning til likningen så vi kan se fra et Horner-skjema eller vanlig polynomdivisjon:

````{tab} Horner-skjema

:::{figure} ./koder/oppgaver/oppgave_6/b.svg
---
width: 70%
class: no-click
---
:::

````

````{tab} Vanlig polynomdivisjon

:::{figure} ./koder/oppgaver/oppgave_6/b_polydiv.svg
---
width: 100%
class: no-click
---
:::

````

som gir $0$ i rest og 

$$
\dfrac{x^4 + 3x^3 - 15x^2 - 19x + 30}{x - 1} = x^3 + 4x^2 - 11x - 30.
$$

Dermed er 

$$
(x^4 + 3x^3 - 15x^2 - 19x + 30) = (x - 1)(x^3 + 4x^2 - 11x - 30).
$$

:::::




:::::::::::::


:::::::::::::{tab-item} c
Finn én rot i tredjegradspolynomet og faktoriser polynomet i én lineær faktor og et andregradspolynom. 

::::{admonition} Fasit
---
class: dropdown, answer
---
$x = -2$ er en rot i tredjegradspolynomet $(x^3 + 4x^2 - 11x - 30)$. Polynomet kan da skrives som

$$
(x^3 + 4x^2 - 11x - 30) = (x + 2)(x^2 + 2x - 15).
$$
::::

:::::{admonition} Løsning
---
class: dropdown, solution
---
$x = -2$ løser likningen. Vi kan se dette fra et Horner-skjema eller vanlig polynomdivisjon:

````{tab} Horner-skjema

:::{figure} ./koder/oppgaver/oppgave_6/c.svg
---
width: 70%
class: no-click
---
:::

````

````{tab} Vanlig polynomdivisjon

:::{figure} ./koder/oppgaver/oppgave_6/c_polydiv.svg
---
width: 90%
class: no-click
---
:::

````

som gir $0$ i rest. Dermed er 

$$
\dfrac{x^3 + 4x^2 - 11x - 30}{x + 2} = x^2 + 2x - 15.
$$

Altså kan vi skrive

$$
x^3 + 4x^2 - 11x - 30 = (x + 2)(x^2 + 2x - 15).
$$
:::::


:::::::::::::


:::::::::::::{tab-item} d
Bestem alle løsningene til likningen.


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 1 \or x = -2 \or x = 3 \or x = -5
$$
::::

:::::::::::::

::::::::::::::



:::::::::::::::