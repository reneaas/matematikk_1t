# Grafisk løsning

::::{admonition} Læringsmål:
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Kunne løse andregradslikninger grafisk. 

::::

Å løse andregradslikninger grafisk, handler om å finne skjæringspunkter mellom grafen til en andregradsfunksjon og grafene til andre funksjoner. 


::::::::::::::::{admonition} Utforsk 1
---
class: explore
---

Under vises eksempler på tre ulike typer andregradslikninger. Vi har annotert likningene med $f(x)$ og $g(x)$ for å tildele en funksjon til uttrykkene i likningene så det er lettere å se samsvar med grafene.

Hvor hver likning, prøv å løse likningen ved hjelp av grafen. Sjekk svaret ditt med løsningen.

:::::::::::::::{tab-set} 
::::::::::::::{tab-item} $x^2 - x - 2 = 0$

$$
\underbrace{x^2 - x - 2}_{\displaystyle f(x)} = 0
$$


:::{figure} ./figurer/eksempler/eksempel_1/likning_1.svg
---
width: 80%
---
:::

---

:::{admonition} Løsning
---
class: solution, dropdown
---
Grafen skjærer $x$-aksen i $(-1, 0)$ og $(2, 0)$. Dermed er løsningen av likningen 

$$
x = -1 \quad \lor \quad x = 2.
$$
:::


::::::::::::::

::::::::::::::{tab-item} $x^2 - 4x + 5 = x + 1$

$$
\underbrace{x^2 - 4x + 5}_{\displaystyle f(x)} = \underbrace{x + 1}_{\displaystyle g(x)}
$$

:::{figure} ./figurer/eksempler/eksempel_1/likning_2.svg
---
width: 80%
---
:::

---

:::{admonition} Løsning
---
class: solution, dropdown
---
Grafene til $f$ og $g$ skjærer hverandre i punktene $(1, 2)$ og $(4, 5)$. Løsningen til likningen $f(x) = g(x)$ er $x$-koordinatene til skjæringspunktene. Dermed er løsningen

$$
x = 1 \quad \lor \quad x = 4.
$$
:::


::::::::::::::

::::::::::::::{tab-item} $x^2 + x - 2 = -\dfrac{2}{3}x^2 - \dfrac{7}{3}x + 3$

$$
\underbrace{x^2 + x - 2}_{\displaystyle f(x)} = \underbrace{-\dfrac{2}{3}x^2 - \dfrac{7}{3}x + 3}_{\displaystyle g(x)}
$$

:::{figure} ./figurer/eksempler/eksempel_1/likning_3.svg
---
width: 80%
---
:::

---

:::{admonition} Løsning
---
class: solution, dropdown
---
Grafene til $f$ og $g$ skjærer hverandre i punktene $(-3, 4)$ og $(1, 0)$. Løsningen til likningen $f(x) = g(x)$ er $x$-koordinatene til skjæringspunktene. Dermed er løsningen

$$
x = -3 \quad \lor \quad x = 1.
$$
:::

:::::::::::::::




::::::::::::::::

---

::::::::::::::::{admonition} Oppsummering: grafisk løsning av andregradslikninger
---
class: summary
---
For å løse en andregradslikning grafisk, tegner vi grafene til funksjonene som inngår i likningene og finner skjæringen mellom grafene. 

Under vises generell teori for de tre typene andregradslikninger som du så på i utforsk 1.

:::::::::::::::{tab-set}
::::::::::::::{tab-item} $ax^2 + bx + c = 0$

$$
f(x) = ax^2 + bx + c
$$

:::{figure} ./figurer/teori/ax^2+bx+c=0.svg
---
width: 80%
---
:::
::::::::::::::

::::::::::::::{tab-item} $ax^2 + bx + c = qx + r$

$$
f(x) = ax^2 + bx + c \quad \text{og} \quad g(x) = qx + r
$$

:::{figure} ./figurer/teori/ax^2+bx+c=qx+r.svg
---
width: 80%
---
:::

::::::::::::::

::::::::::::::{tab-item} $ax^2 + bx + c = px^2 + qx + r$

$$
f(x) = ax^2 + bx + c \quad \text{og} \quad g(x) = px^2 + qx + r
$$

:::{figure} ./figurer/teori/ax^2+bx+c=px^2+qx+r.svg
---
width: 80%
---
:::

::::::::::::::
:::::::::::::::


::::::::::::::::

---

::::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
I {numref}`fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-1` vises grafen til 

$$
f(x) = x^2 - x - 6. 
$$

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Bruk grafen til å løse likningen 

$$
x^2 - x - 6 = 0
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -2 \quad \lor \quad x = 3.
$$
:::

:::::

:::::{tab-item} b
Bruk grafen til å løse likningen 

$$
x^2 - x - 6 = -4
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -1 \quad \lor \quad x = 2.
$$
:::
:::::

:::::{tab-item} c
Bruk grafen til å løse likningen 

$$
x^2 - x - 6 = 6
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -3 \quad \lor \quad x = 4.
$$
:::
:::::

::::::

---

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-1
width: 80%
---
viser grafen til $f(x) = x^2 - x - 6$.
:::

::::::::::::::::

---

::::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
I {numref}`fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-2` vises grafene til

$$
f(x) = -x^2 + x + 6 \quad \text{og} \quad g(x) = x - 3.
$$

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Bruk {numref}`fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-2` til å løse likningen

$$
-x^2 + x + 6 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -2 \quad \lor \quad x = 3.
$$
:::
:::::

:::::{tab-item} b
Bruk {numref}`fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-2` til å løse likningen

$$
-x^2 + x + 6 = 4
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \quad \lor \quad x = 2.
$$
:::
:::::

:::::{tab-item} c
Bruk {numref}`fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-2` til å løse likningen

$$
-x^2 + x + 6 = x - 3
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \quad \lor \quad x = 3.
$$
:::
:::::

::::::

---

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-andregradsfunksjoner-andregradslikninger-grafisk-underveisoppgave-2
width: 80%
---
viser grafene til $f(x) = -x^2 + x + 6$ og $g(x) = x - 3$.
:::

::::::::::::::::


