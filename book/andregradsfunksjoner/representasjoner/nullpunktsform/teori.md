# Nullpunktsform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en andregradsfunksjon på nullpunktsform.
* Kunne finne standardform fra nullpunktsform.
* Kunne bestemme $f(x)$ på nullpunktsform fra graf. 
::: 

En annen veldig nyttig måte å representere en andregradsfunksjon er på **nullpunktsform**. Nullpunktsformen uttrykker funksjonen ved hjelp av nullpunktene til funksjonen. Som vi kanskje oppdaget når vi så på standardform, så var det slik at andregradsfunksjoner kan ha to, ett eller ingen nullpunkter. Derfor kan ikke alle andregradsfunksjoner skrives på nullpunktsform. 


::::{admonition} Andregradsfunksjon: nullpunktsform
---
class: theory
---
Nullpunktsformen til en andregradsfunksjon er gitt ved 

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

---

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

---

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Under vises tre andregradsfunksjoner og deres nullpunktsform *hvis* den eksisterer. 


::::::::::::::{tab-set} 
---
class: tabs-parts
---
:::::::::::::{tab-item} $f$
Grafen til $f$ skjærer $x$-aksen i to punkter, så vi kan skrive $f$ på nullpunktsform.

$$
f(x) = (x - 1)(x + 2)
$$

:::{figure} ./figurer/eksempler/eksempel_1/f.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = (x - 1)(x + 3)$. Grafen skjærer $x$-aksen i to punkter og kan derfor skrives på nullpunktsform.
:::

:::::::::::::

:::::::::::::{tab-item} $g$
Grafen til $g$ skjærer $x$-aksen i ett punkt, så vi kan skrive $g$ på nullpunktsform, men vi må bruke det **samme nullpunktet to ganger**! 

$$
g(x) = -2(x + 1)(x + 1) = -2(x + 1)^2 
$$

:::{figure} ./figurer/eksempler/eksempel_1/g.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $g(x) = -2(x + 1)^2$. Grafen skjærer $x$-aksen i ett punkt og kan derfor skrives på nullpunktsform. Vi må bruke det samme nullpunktet to ganger!
:::

:::::::::::::

:::::::::::::{tab-item} $h$

Grafen til $h$ skjærer ikke $x$-aksen og har derfor ikke nullpunkter. Vi kan derfor ikke skrive $h$ på nullpunktsform.

$$
h(x) = x^2 + x + 1
$$


:::{figure} ./figurer/eksempler/eksempel_1/h.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $h(x) = x^2 + x + 1$. Grafen har ingen nullpunkter og kan derfor ikke skrives på nullpunktsform.
:::

:::::::::::::
::::::::::::::



:::::::::::::::


---

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
En andregradsfunksjon er gitt ved

$$
f(x) = 2(x - 1)(x + 3)
$$

Bestem nullpunktene til $f$.

:::{admonition} Løsning
---
class: solution
---
$f(x) = 2(x - 1)(x + 3)$ er skrevet på nullpunktsform. Generelt er nullpunktsformen

$$
f(x) = a(x - x_1)(x - x_2)
$$

så vi må skrive om uttrykket litt for å lese av nullpunktene:

$$
f(x) = 2(x - 1)(x + 3) = 2(x - \textcolor{red}{1})(x - \textcolor{red}{(-3)})
$$

Nullpunktene til $f$ er derfor

$$
x = 1 \quad \lor \quad x = -3
$$

Merk at vi skriver "$\lor$" som betyr "eller". Dette brukes fordi $f(x) = 0$ kan bare være null for én $x$-verdi av gangen. 
:::

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

## Bestemme $f(x)$ 

Vi kan bruke nullpunktsformen til å bestemme $f(x)$ fra grafen til en andregradsfunksjon.

:::::{admonition} Eksempel 3
---
class: example
---

Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-representasjoner-nullpunktsform-eksempel-3`. 

Bestem nullpunktsformen til $f(x)$. 

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-andregradsfunksjoner-representasjoner-nullpunktsform-eksempel-3
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::

:::{admonition} Løsning
---
class: solution
---
Vi bruker nullpunktsformen til $f(x)$ som er 

$$
f(x) = a(x - x_1)(x - x_2). 
$$

Fra grafen til $f$ kan vi lese av at nullpunktene er 

$$
x = -1 \quad \lor \quad x = 3
$$

Vi setter inn verdiene til nullpunktene og får

$$
f(x) = a(x - (-1))(x - 3) = a(x + 1)(x - 3)
$$

Nå mangler vi bare å bestemme $a$. Dette kan vi gjøre ved å finne ett punkt til på grafen til $f$. For eksempel ser vi at grafen går gjennom $(1, 2)$. Dette gir oss en likning vi kan løse for å bestemme $a$:

\begin{align*}
    f(1) &= 2 \\
    \\
    a\cdot (1 + 1) \cdot (1 - 3) &= 2 \\
    \\
    a\cdot 2 \cdot(-2) &= 2 \\
    \\
    -4a &= 2 \\
    \\
    a &= -\frac{1}{2}
\end{align*}

Altså er 

$$
f(x) = -\frac{1}{2}(x + 1)(x - 3)
$$

:::



:::::

---


::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-representasjoner-nullpunktsform-underveisoppgave-2`.

Bestem nullpunktsformen til $f(x)$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-andregradsfunksjoner-representasjoner-nullpunktsform-underveisoppgave-2
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 2(x + 3)(x - 1)
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med nullpunktsformen til en andregradsfunksjon

$$
f(x) = a(x - x_1)(x - x_2)
$$

Fra grafen til $f$ kan vi lese av at nullpunktene er

$$
x = -3 \quad \lor \quad x = 1
$$

Vi setter inn nullpunktene som gir oss 

$$
f(x) = a(x - (-3))(x - 1) = a(x + 3)(x - 1)
$$

Nå må vi bestemme $a$. Vi finner ett punkt til på grafen til $f$. Vi kan se at grafen går gjennom $(0, -6)$, som gir oss likningen vi kan løse for å bestemme $a$:

\begin{align*}
    f(0) &= -6 \\
    \\
    a\cdot (0 + 3)\cdot (0 - 1) &= -6 \\
    \\
    a\cdot 3\cdot (-1) &= -6 \\
    \\
    -3a &= -6 \\
    \\
    a &= 2
\end{align*}

Altså er 

$$
f(x) = 2(x + 3)(x - 1)
$$
::::

::::::::::::

## Fra nullpunktsform til standardform

Vi kan gå fra nullpunktsformen til standardformen til en andregradsfunksjon.

::::::::::::{admonition} Eksempel 4
---
class: example
---
En andregradsfunksjon er gitt ved 

$$
f(x) = (x - 1)(x + 3)
$$

Bestem standardformen til $f(x)$.

::::{admonition} Hint: Algebraisk lov
---
class: hints, dropdown
---
Vi bruker den algebraiske loven for multiplikasjon av to parenteser i utregningen under:

$$
(a + b)(c + d) = ac + ad + bc + bd
$$
::::

:::::{admonition} Løsning
---
class: solution
---
\begin{align*}
    f(x) &= (x - 1)(x + 3) \\
    \\
    &= x^2 + 3x - x - 3 \\
    \\
    &= x^2 + 2x - 3
\end{align*}

Dermed er standardformen til $f(x)$ gitt ved 

$$
f(x) = x^2 + 2x - 3
$$
:::::
::::::::::::

---


::::::::::::{admonition} Underveisoppgave 3
---
class: check
---
En andregradsfunksjon er gitt ved 

$$
f(x) = (x + 2)(x - 4)
$$

Bestem standardformen til $f(x)$.

::::{admonition} Fasit
---
class: answer, dropdown
---

$$
f(x) = x^2 - 2x - 8
$$

::::

::::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
    f(x) &= (x + 2)(x - 4) \\
    \\
    &= x^2 - 4x + 2x - 8 \\
    \\
    &= x^2 - 2x - 8
\end{align*}

Dermed er standardformen til $f(x)$ gitt ved 

$$
f(x) = x^2 - 2x - 8
$$
::::

::::::::::::

