# Spesielle andregradslikninger

:::{admonition} Læringsmål: spesielle andregradslikninger
---
class: tip
---
Etter å ha gått gjennom denne delen, er målet at du skal:
* Kunne løse spesielle andregradslikninger algebraisk.
:::

Det krever en del verktøy før vi er i stand til å løse *alle* andregradslikninger algebraisk. Her skal vi se på noen spesielle andregradslikninger som vi kan løse med noen enkle triks. Senere skal vi se på hvordan vi kan løse andregradslikninger generelt – men triksene vi lærer her vil være raskere å bruke på de likningene vi skal se på nå. 

## Produktregelen for likninger

Vi starter med en nyttig setning:

:::::{admonition} Setning: produktregelen
---
class: theory
---
Hvis $A$ og $B$ er to tall og

$$
A \cdot B = 0,
$$

så er

$$
A = 0 \quad \text{eller} \quad B = 0.
$$

Vi skriver dette som

$$
A \cdot B = 0 \quad \iff \quad A = 0 \quad \lor \quad B = 0,
$$

der vi leser $\lor$ som "eller". 
:::::

---

:::::{admonition} Eksempel 1
---
class: example
---
En andregradslikning er gitt ved

$$
(x - 1)(x + 2) = 0. 
$$

Bestem løsningen.

::::{admonition} Løsning
---
class: solution
---
Vi kan bruke produktregelen ved å tenke på hver faktor som to tall $A$ og $B$: 

$$
\underbrace{(x - 1)}_{\displaystyle A} \cdot \underbrace{(x + 2)}_{\displaystyle B} = 0. 
$$

Altså står det egentlig bare $A \cdot B = 0$, som betyr at 

\begin{align*}
    A = 0 \quad & \lor \quad B = 0 \\
    \\
    x - 1 = 0 \quad & \lor \quad x + 2 = 0 \\
    \\
    x = 1 \quad & \lor \quad x = -2.
\end{align*}
::::

:::::

---

Når er det **din tur**!

::::::::::{admonition} Underveisoppgave 1
---
class: check
---

:::::::::{tab-set}
---
class: tabs-parts
---
::::::::{tab-item} a
Bruk produktregelen til å løse likningen

$$
(x + 2)(x - 4) = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -2 \quad \lor \quad x = 4.
$$
:::
::::::::

::::::::{tab-item} b
Bruk produktregelen til å løse likningen

$$
x\left(x + 2\right) = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 0 \quad \lor \quad x = -2.
$$
:::

::::::::

::::::::{tab-item} c
Bruk produktregelen til å løse likningen

$$
(-x + 4)(x + 3) = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 4 \quad \lor \quad x = -3.
$$
:::

::::::::

:::::::::
::::::::::

---

I underveisoppgave 1 møtte du på en spesiell andregradslikning som har en sammenheng med en annen skrivemåte. Utvider vi parentesen, finner vi at 

$$
x(x + 2) = 0 \quad \iff \quad x^2 + 2x = 0.
$$

Med andre ord er dette også likninger som er egnet for å løses med produktregelen, så lenge vi faktoriserer først. Vi tar et eksempel:


:::{admonition} Vi deler **aldri** med $x$
---
class: sidenote, margin
---
Hvis vi deler med $x$, så vil vi miste løsningen $x = 0$. Hver gang vi deler med $x$, dør det både en hund 🐕 og en katt 🐈. Vi deler derfor **aldri** med $x$!
:::

:::::{admonition} Eksempel 2
---
class: example
---
Løs likningen

$$
4x^2 + 16x = 0.
$$

::::{admonition} Løsning
---
class: solution
---
Vi løser denne i to steg:
1. Faktorisere ut en faktor $4x$ fra uttrykket.
2. Løser likningen med produktregelen.

\begin{align*}
    4x^2 + 16x &= 0 \\
    \\
    \textcolor{red}{4x} \cdot x + \textcolor{red}{4x} \cdot 4 & = 0 && \text{Faktoriser med felles faktor i hvert ledd} \\ 
    \\
    4x(x + 4) &= 0 && \text{Faktoriserer ut en faktor $4x$} \\
    \\
    4x = 0 & \quad \lor \quad x + 4 = 0 && \text{Bruker produktregelen} \\
    \\
    x = 0 & \quad \lor \quad x = -4.
\end{align*}

::::
:::::

Når er det **din tur**!

::::::::::{admonition} Underveisoppgave 2
---
class: check
---

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Løs likningen 

$$
x^2 - 2x = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 0 \quad \lor \quad x = 2.
$$
:::
:::::

:::::{tab-item} b
Løs likningen 

$$
3x^2 - 6x = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 0 \quad \lor \quad x = 2.
$$
:::
:::::

:::::{tab-item} c
Løs likningen

$$
-2x^2 + 8x = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 0 \quad \lor \quad x = 4.
$$
:::

:::::

::::::

::::::::::

---

## Kvadratrot for å løse andregradslikninger

Kvadratrot er en annen strategi som fungerer på noen andregradslikninger. Vi går løs på et eksempel.

:::::::::{admonition} Eksempel 3
---
class: example
---
Løs likningen

$$
x^2 - 9 = 0.
$$

:::::{admonition} Løsning
---
class: solution
---
Først kan vi skrive om likningen 

\begin{align*}
    x^2 - 9 &= 0 \\
    \\
    x^2 &= 9 \\
\end{align*}

Vi leter etter et tall $x$ slik at $x^2 = 9$. Dette finnes to slik tall som vi kan prøve ut:

$$
(-3)^2 = 9 \quad \text{og} \quad 3^2 = 9.
$$

Så både $x = -3$ og $x = 3$ vil være løsninger av likningen. 

Men dette er det samme som å si at 

$$
x^2 = 9 \quad \iff \quad x = \pm \sqrt{9} = \pm 3 \quad \iff \quad x = -3 \quad \lor \quad x = 3.
$$

der $\pm$-symbolet betyr "pluss eller minus". 

:::::


:::::::::

---

:::::::::{admonition} Underveisoppgave 3
---
class: check
---
::::::::{tab-set}
---
class: tabs-parts
---
:::::::{tab-item} a
Løs likningen 

$$
x^2 = 4.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \pm 2. 
$$
:::
:::::::

:::::::{tab-item} b
Løs likningen 

$$
x^2 - 25 = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \pm 5. 
$$
:::
:::::::

:::::::{tab-item} c
Løs likningen 

$$
x^2 + 16 = 0.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \emptyset.
$$

Det finnes ingen løsning. 
:::
:::::::
::::::::
:::::::::

