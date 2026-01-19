# Oppgaver: Polynomlikninger


:::::::::::::::{exercise} Oppgave 1

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


::::{answer}
$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}. 
$$
::::

::::{solution}
De mulige heltallsrøttene til $f$ er tall som deler konstantleddet $-6$. Alle hele tall som deler $-6$ er gitt ved 

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}. 
$$
:::::::::::::

:::::::::::::{tab-item} b
Ta utgangspunkt i listen fra **a** og finn én rot til $f(x)$. 

Bruk polynomdivisjon til å faktorisere $f(x)$. 

:::{answer}
Én mulighet er $x = 1$, som gir

$$
x^3 + 4x^2 + x - 6 = (x - 1)(x^2 + 5x + 6)
$$

:::

::::{solution}
En av røttene til $f(x)$ er $x = 1$. Det kan vi se enten med et Horner-skjema eller vanlig polynomdivisjon:

````{tab} Horner-skjema

:::{figure} ./koder/oppgaver/oppgave_1/b.svg
---
width: 50%
class: no-click, adaptive-figure
---
:::

````

````{tab} Vanlig polynomdivisjon

:::{figure} ./koder/oppgaver/oppgave_1/b_polydiv.svg
---
width: 90%
class: no-click, adaptive-figure
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


:::{answer}
$$
x = 1 \or x = -2 \or x = -3
$$
:::


:::{solution}
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

:::::::::::::::{exercise} Oppgave 2
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

::::{answer}
$$
x = 2 \or x = -2 \or x = 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Tegn et fortegnsskjema for $f(x)$. 


::::{answer}

:::{figure} ./figurer/oppgaver/oppgave_2/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::


:::::::::::::{tab-item} c
Lag en **skisse** av grafen til $f$. Marker nullpunktene. 


::::{answer}

:::{figure} ./figurer/oppgaver/oppgave_2/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::


:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten $f(x) \geq 0$. 


::::{answer}
$$
x \in [-2, 2] \cup [3, \to \rangle
$$

::::

:::::::::::::

::::::::::::::




:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 3
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


::::{answer}
$$
x = -1 \or x = 3 \or x = 5. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten $f(x) \leq 0$. 

::::{answer}
$$
-1 \leq x \and x \leq 3 \or 5 \leq x. 
$$
::::
:::::::::::::

::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 4 
::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Løs tredjegradslikningen 

$$
x^3 - x^2 - 2x + 2 = 0. 
$$

::::{answer}
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

::::{answer}
$$
x \in \langle -\sqrt{2}, 1 \rangle \cup \langle \sqrt{2}, \to \rangle
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
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


::::{answer}
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

::::{answer}
$$
x \in \langle \gets, 2\rangle \setminus \{-1\}. 
$$
:::

:::::::::::::

::::::::::::::


:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 6
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 + 2x^2 - 5x - 6
$$

I hvilke punkter skjærer grafen til funksjonen $x$-aksen?



::::{answer}
$$
x = -3 \or x = -1 \or x = 2.
$$
::::

::::{solution}
De mulige heltallige røttene til $f(x)$ er 

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}.
$$

Vi prøver oss fram til vi finner en rot:

:::{horner}
---
p: x^3 + 2x^2 - 5x - 6
x: 1
width: 60%
---
:::

Det funket ikke med $x = 1$, så vi går videre:

:::{horner}
---
p: x^3 + 2x^2 - 5x - 6
x: -1
width: 60%
---
:::

Her fikk vi $0$ i rest, så $x = -1$ er en rot. Vi kan dermed faktorisere $f(x)$ som

$$
f(x) = (x + 1)(x^2 + x - 6).
$$

Vi bestemmer røttene til andregradspolynomet med $abc$-formelen:

$$
x = \dfrac{-1 \pm \sqrt{1^2 - 4 \cdot 1 \cdot (-6)}}{2 \cdot 1} = \dfrac{-1 \pm \sqrt{25}}{2} = \dfrac{-1 \pm 5}{2}
$$

som gir

$$
x = 2 \or x = -3.
$$


Altså skjærer grafen til $f$ gjennom $x$-aksen i punktene 

$$
x = -3 \or x = -1 \or x = 2.
$$
::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7
Funksjonen $f$ er gitt ved

$$
f(x) = 2x^3 + x^2 - 18x - 9
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at divisjonen $f(x) : (x - 3)$ går opp.


::::{solution}
:::{polydiv}
---
p: 2x^3 + x^2 - 18x - 9
q: x - 3
width: 70%
---
:::

::::

:::::::::::::



:::::::::::::{tab-item} b
Gjør beregninger og vurder hvilken av grafene nedenfor som kan være grafen til $f$.



::::{multi-plot2}
---
rows: 1
cols: 3
fontsize: 30
---

:::{plot}
function: (x + 3) * (x - 3) * (2*x - 1), A
xmin: -5
xmax: 5
ymin: -20
ymax: 30
ticks: off
:::


:::{plot}
function: (x + 3) * (x - 3) * (2*x + 1), B
xmin: -5
xmax: 5
ymin: -30
ymax: 20
ticks: off
:::


:::{plot}
function: (x + 3) * (x - 1/2) * (2*x + 1), C
xmin: -5
xmax: 5
ymin: -20
ymax: 20
ticks: off
:::

::::


::::{answer}
Graf B.
::::

:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 8
Gitt likningen 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x + a)(x - b)
$$

Bestem $a$ og $b$ slik at likningen blir en identitet.


::::{answer}
$$
a = 2 \and b = 6 \or a = -6 \and b = -2
$$
::::


::::{solution}
Vi utfører polynomdivisjonen 

$$
(x^3 - 5x^2 - 8x + 12) : (x - 1)
$$

for å bestemme andregradspolynomet i faktoriseringen:


:::{polydiv}
---
p: x^3 - 5x^2 - 8x + 12
q: x - 1
width: 70%
---
:::

Altså er 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x^2 - 4x - 12).
$$

Vi bestemmer røttene til andregradspolynomet med $abc$-formelen:

$$
x = \dfrac{4 \pm \sqrt{(-4)^2 - 4 \cdot 1 \cdot (-12)}}{2 \cdot 1} = \dfrac{4 \pm \sqrt{16 + 48}}{2} = \dfrac{4 \pm 8}{2}
$$

som gir løsningene

$$
x = 6 \or x = -2.
$$

Altså vil vi kunne skrive

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x + 2)(x - 6).
$$

Dermed må vi ha at

$$
a = 2 \and b = 6 \or a = -6 \and b = -2
$$

for at likningen skal bli en identitet.


::::


:::::::::::::::






---





:::::::::::::::{exercise} Oppgave 9
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
class: no-click, adaptive-figure
---
:::

````

````{tab} Vanlig polynomdivisjon

:::{figure} ./koder/oppgaver/oppgave_6/b_polydiv.svg
---
width: 100%
class: no-click, adaptive-figure
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
class: no-click, adaptive-figure
---
:::

````

````{tab} Vanlig polynomdivisjon

:::{figure} ./koder/oppgaver/oppgave_6/c_polydiv.svg
---
width: 90%
class: no-click, adaptive-figure
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