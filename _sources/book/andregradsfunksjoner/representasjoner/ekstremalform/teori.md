# Ekstremalform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en andregradsfunksjon på ekstremalform, og lese av ekstremalpunktet fra funksjonsuttrykket.
* Kunne bestemme $f(x)$ på ekstremalform fra graf. 
* Kunne finne standardform fra ekstremalform.
* Kunne finne ekstremalform fra nullpunktsform, og kunne beskrive sammenhengen mellom nullpunkter og symmetrilinje.
* Kunne bestemme om et ekstremalpunkt er et topp- eller bunnpunkt fra ekstremalformen til en andregradsfunksjon.
::: 

Før vi ser på hva ekstremalformen til en andregradsfunksjon er, må vi først definere noen nye begreper. 

:::::::::::::::{admonition} Ekstremalpunkter, toppunkter og bunnpunkter
---
class: theory
---
**Ekstremalpunkt** er en fellesbetegnelse for **toppunkt** og **bunnpunkt**. Et ekstremalpunkt kan enten være et toppunkt eller et bunnpunkt.

Under vises det grafisk hva et toppunkt og et bunnpunkt er for en andregradsfunksjon.
::::::::::::::{tab-set}
:::::::::::::{tab-item} Bunnpunkt
Grafen til en andregradsfunksjon har et bunnpunkt når den er **konveks** $\smile$ (den har "smilefjes").

:::{figure} ./figurer/teori/bunnpunkt.svg
---
width: 80%
class: no-click
---
:::
:::::::::::::

:::::::::::::{tab-item} Toppunkt
Grafen til en andregradsfunksjon har et toppunkt når den er **konkav** $\frown$ (den har et "surt fjes").
:::{figure} ./figurer/teori/toppunkt.svg
---
width: 80%
class: no-click
---
:::
:::::::::::::
::::::::::::::

:::::::::::::::

---

:::::::::::::::::{admonition} Eksempel 1
---
class: example
---

Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-representasjoner-ekstremalform-eksempel-1`.

1. Bestem hva slags ekstremalpunkt $f$ har.
2. Bestem koordinatene til ekstremalpunktet til $f$.


:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-andregradsfunksjoner-representasjoner-ekstremalform-eksempel-1
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
:::


:::{admonition} Løsning
---
class: solution
---
1. Siden grafen til $f$ er *konkav* $\frown$, har $f$ et toppunkt.
2. Det høyeste punktet på grafen er $(-1, 2)$. Dette er ekstremalpunktet til $f$.
:::

:::::::::::::::::

---


## Ekstremalform: algebraisk og grafisk

Ekstremalformen til en andregradsfunksjon er en tredje måte å skrive en andregradsfunksjon på. Ekstremalformen inneholder informasjon om ekstremalpunktet til funksjonen.

:::::{admonition} Ekstremalform
---
class: theory
---
Ekstremalformen til en andregradsfunksjon $f$ er gitt ved

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 80%
class: no-click
---
:::

* Hvis $a > 0$ er grafen til $f$ konveks $\smile$ og har et bunnpunkt.
* Hvis $a < 0$ er grafen til $f$ konkav $\frown$ og har et toppunkt.
* Linja $x = x_0$ er symmetrilinja til $f$. Grafen er speilet rundt denne linja!
---

::::{figure} ./figurer/teori/grafisk_representasjon.svg
---
width: 80%
class: no-click
---
:::

:::::

---

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Under vises noen eksempler på andregradsfunksjoner med grafen og tilhørende funksjonsuttrykk skrevet på ekstremalform. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} $f$
Grafen til $f$ har et bunnpunkt i $(-1, -3)$ og har derfor en symmetrilinje $x = -1$. <br> Ekstremalformen til $f$ er gitt ved

$$
f(x) = (x + 1)^2 - 3
$$

:::{figure} ./figurer/eksempler/eksempel_2/f.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::

:::::::::::::{tab-item} $g$
Grafen til $g$ har et toppunkt i $(2, 1)$ og har derfor en symmetrilinje $x = 2$. <br> Ekstremalformen til $g$ er gitt ved 

$$
g(x) = -\dfrac{1}{2}(x - 2)^2 + 1
$$

:::{figure} ./figurer/eksempler/eksempel_2/g.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::

:::::::::::::{tab-item} $h$
Grafen til $h$ har et bunnpunkt i $(-1, 1)$ og har derfor symmetrilinje $x = -1$. <br> Ekstremalformen til $h$ er gitt ved

$$
h(x) = 2(x + 1)^2 + 1
$$

:::{figure} ./figurer/eksempler/eksempel_2/h.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::

::::::::::::::


:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::

:::::::::::::::

---

## Bestemme $f(x)$ fra graf

Vi skal se på hvordan vi kan gå fra grafen til en andregradsfunksjon til et funksjonsuttrykk for ved hjelp av ekstremalformen. 

:::::::::::::::{admonition} Eksempel 3
---
class: example
---
Grafen til en andregradsfunksjon er vist i {numref}`fig-andregradsfunksjoner-representasjoner-ekstremalform-eksempel-3`.

Bestem ekstremalformen til $f(x)$.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-andregradsfunksjoner-representasjoner-ekstremalform-eksempel-3
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
:::  

::::{admonition} Løsning
---
class: solution
---
Vi starter fra ekstremalformen til $f(x)$:

$$
f(x) = a(x - x_1)^2 + y_1
$$

Fra grafen til $f$ kan vi lese av at det har et bunnpunkt i $(1, -2)$ som betyr at 

$$
(x_1, y_1) = (1, -2).
$$

Vi setter dette inn i ekstremalformen til $f$:

$$
f(x) = a(x - 1)^2 - 2
$$

Nå må vi ha ett punkt til for å bestemme $a$. Vi kan se at grafen går gjennom punkt $(3, 0)$ som betyr at 

\begin{align*}
    f(3) &= 0 \\
    \\
    a(3 - 1)^2 - 2 &= 0 \\
    \\
    4a - 2 &= 0 \\
    \\
    4a &= 2 \\
    \\
    a &= \dfrac{1}{2}
\end{align*}

Dermed er 

$$
f(x) = \dfrac{1}{2}(x - 1)^2 - 2
$$
::::

:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-representasjoner-ekstremalform-underveisoppgave-2`.

Bestem ekstremalformen til $f(x)$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg 
---
name: fig-andregradsfunksjoner-representasjoner-ekstremalform-underveisoppgave-2
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = -3(x + 2)^2 + 4
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Vi starter fra ekstremalformen til $f(x)$:

$$
f(x) = a(x - x_1)^2 + y_1
$$

Vi kan lese fra grafen til $f$ at det har et toppunkt i $(-2, 4)$ som betyr at

$$
f(x) = a(x - (-2))^2 + 4 = a(x + 2)^2 + 4
$$

Vi trenger ett punkt til for å bestemme $a$. Vi kan se at grafen går gjennom punkt $(-1, 1)$ som gir 

\begin{align*}
    f(-1) &= 1 \\
    \\
    a(-1 + 2)^2 + 4 &= 1 \\
    \\
    a(1)^2 + 4 &= 1 \\
    \\
    a + 4 &= 1 \\
    \\
    a &= -3
\end{align*}

Dermed er 

$$
f(x) = -3(x + 2)^2 + 4
$$
:::

:::::::::::::::


## Fra nullpunktsform til ekstremalform

Vi skal nå se på hvordan vi kan gå fra nullpunktsformen til ekstremalformen til en andregradsfunksjon. 


:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Her skal du utforske sammenhengen mellom nullpunktsformen og ekstremalformen til en andregradsfunksjon.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Se på grafene under. 

1. Kan du se en sammenheng om hvor nullpunktene ligger i forhold til symmetrilinja? 
2. Kan du beskrive sammenhengen generelt? 

::::::::::::{tab-set}
:::::::::::{tab-item} Graf A
:::{figure} ./figurer/utforsk/utforsk_1/a/graf_A.svg
---
width: 80%
class: no-click
---
:::
:::::::::::

:::::::::::{tab-item} Graf B
:::{figure} ./figurer/utforsk/utforsk_1/a/graf_B.svg
---
width: 80%
class: no-click
---
:::
:::::::::::

:::::::::::{tab-item} Graf C
:::{figure} ./figurer/utforsk/utforsk_1/a/graf_C.svg
---
width: 80%
class: no-click
---
:::
:::::::::::
::::::::::::

:::{admonition} a: Oppsummering
---
class: dropdown, summary
---
1. Det er like lang avstand fra symmetrilinja til hvert nullpunkt på $x$-aksen.
2. Symmetrilinja ligger **midt** mellom nullpunktene.
:::

:::::::::::::

:::::::::::::{tab-item} b
Under vises funksjonsuttrykkene til grafene skrevet på nullpunktsform og ekstremalform.
Se på uttrykkene. 

1. Kan du finne en formel for symmetrilinja til grafene ut ifra nullpunktene?
2. Kan du bruke dette til å regne ut ekstremalpunktet også?

::::::::::::{tab-set}
:::::::::::{tab-item} Graf A

$$
f(x) = (x - 1)(x + 3) = (x + 1)^2 - 4
$$

:::::::::::

:::::::::::{tab-item} Graf B

$$
f(x) = -\dfrac{1}{2}(x + 3)(x - 5) = -\dfrac{1}{2}(x - 1)^2 + \dfrac{9}{2}
$$

:::::::::::

:::::::::::{tab-item} Graf C
$$
f(x) = \dfrac{1}{4}(x + 2)(x - 4) = \dfrac{1}{4}(x - 1)^2 - 4
$$
:::::::::::
::::::::::::

:::{admonition} b: Oppsummering
---
class: dropdown, summary
---
1. Symmetrilinja $x_0$ er gjennomsnittet av nullpunktene $x_1$ og $x_2$. Det vil si at

$$
x_0 = \dfrac{x_1 + x_2}{2}
$$

2. For å finne ekstremalpunktet, regner vi ut $y_0 = f(x_0)$. Da har vi ekstremalpunktet $(x_0, y_0)$.
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---

> Jobb med Utforsk 1 **før** du ser på oppsummeringen under!

:::::::::::::::{admonition} Oppsummering: fra nullpunktsform til ekstremalform
---
class: summary, dropdown
---
For å bytte fra nullpunktsformen til ekstremalformen til en andregradsfunksjon, følger vi disse stegene:

1. Bestem symmetrilinja $x_0$ til funksjonen ved å regne ut gjennomsnittet av nullpunktene $x_1$ og $x_2$:

:::{figure} ./figurer/teori/nullpunkter_og_symmetrilinje.svg
---
width: 40%
class: no-click
---
:::

2. Regn ut $y_0 = f(x_0)$ for å finne $y$-koordinaten til ekstremalpunktet.

:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 3
---
class: check
---
Nullpunktsformen til en andregradsfunksjon er gitt ved

$$
f(x) = -2(x - 1)(x + 3)
$$

Bestem ekstremalformen til $f(x)$. 

::::::::::::::{admonition} Fasit
---
class: answer, dropdown
---

$$
f(x) = -2(x + 1)^2 - 8
$$

::::::::::::::


::::::::::::::{admonition} Løsning
---
class: solution, dropdown
---
Nullpunktene til $f(x)$ er 

$$
x = 1 \quad \lor \quad x = -3
$$

Symmetrilinja er gjennomsnittet av nullpunktene som gir 

$$
x_0 = \dfrac{1 + (-3)}{2} = \dfrac{-2}{2} = -1.
$$

$y$-koordinaten til ekstremalpunktet er

$$
y_0 = f(x_0) = f(-1) = -2\cdot (-1 - 1) \cdot (-1 + 3) = -2\cdot (-2)\cdot (2) = -8.
$$

Dermed er ekstremalformen til $f(x)$ gitt ved

$$
f(x) = -2(x + 1)^2 - 8
$$
::::::::::::::
:::::::::::::::

## Fra ekstremalform til standardform

Vi skal nå se på hvordan vi kan gå fra ekstremalformen til standardformen til en andregradsfunksjon.



::::{admonition} Eksempel 4
---
class: example
---
En andregradsfunksjon er gitt ved 

$$
f(x) = (x - 1)^2 + 3
$$

Bestem standardformen til $f(x)$. 

:::{admonition} Hint: Algebraisk lov 1
---
class: hints, dropdown
---
Vi bruker den algebraiske loven for multiplikasjon av to parenteser i utregningen under:

$$
(a + b)^2 = (a + b)(a + b)
$$
:::

:::{admonition} Hint: Algebraisk lov 2
---
class: hints, dropdown
---
Vi bruker den algebraiske loven for multiplikasjon av to parenteser i utregningen under:

$$
(a + b)(c + d) = ac + ad + bc + bd
$$
:::

:::{admonition} Løsning
---
class: solution
---
\begin{align*}
f(x) &= (x - 1)^2 + 3 \\
\\
&= \textcolor{red}{(x - 1)(x - 1)} + 3 \\
\\ 
&= \textcolor{red}{x^2 - x - x + (-1)\cdot (-1)} + 3 \\
\\
&= x^2 - 2x + 1 + 3 \\
\\
&= x^2 - 2x + 4
\end{align*}

Dermed er standardformen til $f(x)$ gitt ved 

$$
f(x) = x^2 - 2x + 4
$$
:::
::::

---

::::{admonition} Underveisoppgave 4
---
class: check
---
Bestem standardformen til 

$$
f(x) = (x + 3)^2 + 4.
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = x^2 + 6x + 13
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
\begin{align*}
    f(x) &= (x + 3)^2 + 4 \\
    \\
    &= \textcolor{red}{(x + 3)(x + 3)} + 4 \\
    \\
    &= \textcolor{red}{x^2 + 3x + 3x + 3^2} + 4 \\
    \\
    &= \textcolor{red}{x^2 + 6x + 9} + 4 \\
    \\
    &= x^2 + 6x + 13
\end{align*}

Dermed er standardformen til $f(x)$ gitt ved 

$$
f(x) = x^2 + 6x + 13
$$
:::

::::

