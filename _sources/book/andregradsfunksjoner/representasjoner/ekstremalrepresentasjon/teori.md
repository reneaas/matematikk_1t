# Ekstremalform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en andregradsfunksjon på ekstremalform, og lese av ekstremalpunktet fra funksjonsuttrykket.
* Kunne finne standardform fra ekstremalform.
* Kunne bestemme $f(x)$ på ekstremalform fra graf. 
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
1. Siden grafen til $f$ er *konkav* $\frown$, har $f$ et bunnpunkt.
2. Det høyeste punktet på grafen er $(-1, 2)$. Dette er ekstremalpunktet til $f$.
:::

:::::::::::::::::

---


## Algebraisk representasjon

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

* Hvis $a > 0$ er grafen til $f$ konveks $\smile$ har et bunnpunkt.
* Hvis $a < 0$ er grafen til $f$ konkav $\frown$ og har et toppunkt.
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
Grafen til $f$ har et bunnpunkt i $(-1, -3)$. Ekstremalformen til $f$ er gitt ved

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
Grafen til $g$ har et toppunkt i $(2, 1)$. Ekstremalformen til $g$ er gitt ved 

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
Grafen til $h$ har et bunnpunkt i $(-1, 1)$. Ekstremalformen til $h$ er gitt ved

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

