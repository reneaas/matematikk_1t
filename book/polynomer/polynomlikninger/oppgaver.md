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
Ta utgangspunkt i listen fra **a** og bruk Horner-skjema til å utføre polynomdivisjon og teste ut funksjonsverdier for å finne en rot til $f$.


::::{admonition} Fasit
---
class: answer, dropdown
---
En av røttene til $f$ er $x = 1$, som vi kan se med Horner-skjemaet under:

:::{figure} ./koder/oppgaver/oppgave_1/b.svg
---
width: 50%
class: no-click
---
:::

Dette betyr at 

$$
(x^3 + 4x^2 + x - 6) = (x - 1)(x^2 + 5x + 6)
$$

::::


::::{admonition} Løsning
---
class: answer, dropdown
---
Detaljert hvordan Horner-skjema lages:

:::{figure} ./koder/oppgaver/oppgave_1/b_tutor.svg
---
width: 50%
class: no-click
---
:::

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

::::::::::::::

:::::::::::::::





:::::::::::::::{admonition} Oppgave 5
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
Vi bruker et Horner-skjema og sjekker verdier i lista fra **a**:

:::{figure} ./koder/oppgaver/oppgave_4/b.svg
---
width: 70%
class: no-click
---
:::

som gir $0$ i rest og 

$$
\dfrac{x^4 + 3x^3 - 15x^2 - 19x + 30}{x - 1} = x^3 + 4x^2 - 11x - 30.
$$

Dermed er 

$$
(x^4 + 3x^3 - 15x^2 - 19x + 30) = (x - 1)(x^3 + 4x^2 - 11x - 30).
$$

::::{admonition} Detaljert Horner-skjema
---
class: dropdown, hints
---

:::{figure} ./koder/oppgaver/oppgave_4/b_tutor.svg
---
width: 80%
class: no-click
---
:::

::::

:::::




:::::::::::::


:::::::::::::{tab-item} c
Finn én rot i tredjegradspolynomet og faktoriser polynomet i én lineær faktor og et andregradspolynom. 

::::{admonition} Fasit
---
class: dropdown, answer
---
$x = -2$ er en rot i tredjegradspolynomet $(x^3 + 4x^2 - 11x - 30)$. Polynomet kan derfor skrives som

$$
(x^3 + 4x^2 - 11x - 30) = (x + 2)(x^2 + 2x - 15).
$$
::::

:::::{admonition} Løsning
---
class: dropdown, solution
---
Vi prøver ut flere verdier i lista fra **a**. Med $x = -2$, får vi følgende Horner-skjema:

:::{figure} ./koder/oppgaver/oppgave_4/c.svg
---
width: 70%
class: no-click
---
:::

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
Bestem alle løsningene til likningen. Sjekk at alle heltallige løsninger er en del av listen fra **a**.


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