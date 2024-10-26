# Standardform


:::{admonition} Læringsmål
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:

* Kunne representere en andregradsfunksjon på standardform, og kunne lese av koeffisientene.
* Kunne avgjøre den grafiske formen til en andregradsfunksjon ut fra koeffisientene.
* Kunne bestemme koeffisientene til en andregradsfunksjon ved hjelp av lineære likningssystemer.
:::

## Algebraisk representasjon

::::{admonition} Andregradsfunksjon: standardform
---
class: theory
---
Standardformen til en andregradsfunksjon $f$ er gitt ved

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 80%
class: no-click
---
:::

Vi merker oss at koeffisienten $a$ kalles for **ledende koeffisient** fordi det er koeffisienten foran den største potensen av $x$. Altså er **ikke** $a$ "stigningstall" når vi snakker om andregradsfunksjoner.

::::

::::{admonition} Eksempel 1: Andregradsfunksjoner
---
class: example
---
I tabellen under vises en rekke andregradsfunksjoner og deres koeffisienter.

| Funksjon | $a$ | $b$ | $c$ |
|:----------|:-----:|:-----:|:-----:|
| $f(x) = 2x^2 + 3x + 1$ | $2$ | $3$ | $1$ |
| $g(x) = -x^2 + 4x - 2$ | $-1$ | $4$ | $-2$ |
| $h(x) = 3x^2 - 2x + 5$ | $3$ | $-2$ | $5$ |
| $p(x) = 2x^2$ | $2$ | $0$ | $0$ |
| $q(x) = x^2 - 3x$ | $1$ | $-3$ | $0$ |
| $r(x) = -x^2 + 4$ | $-1$ | $0$ | $4$ |
::::

Så er det din tur:

::::{admonition} Underveisoppgave 1
---
class: check
---
Fyll ut tabellen med koeffisientene eller funksjonsuttrykket til andregradsfunksjonene:

| Funksjon | $a$ | $b$ | $c$ |
|:----------|:-----:|:-----:|:-----:|
| $f(x) = 3x^2 + 2x + 1$ | | | |
| $g(x) = -2x^2 + 5x - 3$ | | | |
| $h(x) = $ | $-1$ | $6$ | $0$ |
| $p(x) = 3x^2$ | | | |
| $q(x) = x^2 - 2x$ | | | |
| $r(x) = $ | $-2$ | $0$ | $-5$ |

```{admonition} Løsning
:class: solution, dropdown

| Funksjon | $a$ | $b$ | $c$ |
|:----------|:-----:|:-----:|:-----:|
| $f(x) = 3x^2 + 2x + 1$ | $3$ | $2$ | $1$ |
| $g(x) = -2x^2 + 5x - 3$ | $-2$ | $5$ | $-3$ |
| $h(x) = -x^2 + 6x$ | $-1$ | $6$ | $0$ |
| $p(x) = 3x^2$ | $3$ | $0$ | $0$ |
| $q(x) = x^2 - 2x$ | $1$ | $-2$ | $0$ |
| $r(x) = -2x^2 - 5$ | $-2$ | $0$ | $-5$ |
```
::::

## Grafisk representasjon

Her skal vi se nærmere på hvordan grafen til en andregradsfunksjon ser ut og hvordan koeffisientene påvirker formen på grafen.


:::::::::::::::{admonition} Utforsk 1
---
class: explore, full-width
---

::::::::::::::{tab-set}
:::::::::::::{tab-item} Koeffisient: $a$

Under er en andregradsfunksjon vist der du kan variere verdien til koeffisienten $a$. 

1. Hva skjer med grafen når $a > 0$.
2. Hva skjer med grafen når $a < 0$.
3. Hva skjer med grafen når $|a|$ er stor eller liten? 


:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/a.html
---
:::

:::{admonition} Oppsummering: Koeffisient $a$
---
class: summary, dropdown
---
1. Grafen har et "smilefjes" når $a > 0$. Vi sier at grafen er **konveks**. 
2. Grafen har et "surt fjes" når $a < 0$. Vi sier at grafen er **konkav**.
3. Når $|a|$ er stor, vil grafen bli brattere og smalere. Når $|a|$ er liten, vil grafen få lavere stigning og bli bredere.
:::

:::::::::::::

:::::::::::::{tab-item} Koeffisient: $b$

1. Hva skjer med grafen når $b = 0$?
2. Hva skjer med grafen når $b > 0$? 
3. Hva skjer med grafen når $b < 0$?

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/b.html
---
:::

:::{admonition} Oppsummering: Koeffisient $b$
---
class: summary, dropdown
---
1. Når $b = 0$, vil grafen være symmetrisk om $y$-aksen. 
2. Når $b > 0$, skifter vi grafen til venstre for $y$-aksen.
3. Når $b < 0$, skrifter vi grafen til høyre for $y$-aksen. 
:::

:::::::::::::


:::::::::::::{tab-item} Koeffisient: $c$

1. Hva skjer med grafen når $c = 0$?
2. Hva bestemmer $c$ for grafen generelt? 

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/c.html
---
:::

:::{admonition} Oppsummering: Koeffisient $c$
---
class: summary, dropdown
---
1. Når $c = 0$, skjærer grafen gjennom origo. 
2. Verdien til $c$ bestemmer hvor grafen skjærer $y$-aksen. 
:::

:::::::::::::


::::::::::::::

:::::::::::::::

---

## Bestemme $f(x)$

Vi skal se nærmere på hvordan vi kan bruke lineære likningssystemer for å bestemme koeffisientene til en andregradsfunksjon.

:::::{admonition} Eksempel 2: Bestemme $f(x)$
---
class: example
---

Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-representasjoner-standardform-eksempel-2`.

Bestem $f(x)$.

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-andregradsfunksjoner-representasjoner-standardform-eksempel-2
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
:::

::::{admonition} Løsning
---
class: solution
---
En andregradsfunksjon kan skrives på standardform

$$
f(x) = ax^2 + bx + c.
$$

Vi har tre ukjente koeffisienter – vi må derfor ha tre likninger for å kunne bestemme $a$, $b$ og $c$. Fra grafen ser vi at 

$$
f(0) = -6 \quad \land \quad f(-2) = 0 \quad \land \quad f(3) = 0
$$

som gir oss likningssystemet:

$$
c = -6 \quad \land \quad 4a - 2b + c = 0 \quad \land \quad 9a + 3b + c = 0
$$

Siden $c = -6$, kan vi redusere likningssystemet til to likninger:

\begin{align*}
    4a - 2b - 6 &= 0 \quad\quad (\mathrm{I})\\
    \\
    9a + 3b - 6 &= 0 \quad\quad (\mathrm{II})\\
\end{align*}

Fra likning $\mathrm{I}$ får vi 

\begin{align*}
    4a - 2b - 6 &= 0 \\
    \\
    4a - 6 &= 2b \\
    \\
    \dfrac{4a}{2} - \dfrac{6}{2} &= \dfrac{2b}{2} \\
    \\
    2a - 3 &= b
\end{align*}

Setter vi dette inn i likning $\mathrm{II}$ får vi

\begin{align*}
    9a + 3(2a - 3) - 6 &= 0 \\
    \\
    9a + 6a - 9 - 6 &= 0 \\
    \\
    15a - 15 &= 0 \\
    \\
    15a &= 15 \\
    \\
    a &= 1
\end{align*}

Til slutt bestemmer vi $b$:

$$
b = 2a - 3 = 2 \cdot 1 - 3 = -1.
$$

Dermed er 

$$
a = 1 \quad \land \quad b = -1 \quad \land \quad c = -6
$$

som betyr at 

$$
f(x) = ax^2 + bx + c = x^2 - x - 6.
$$

::::

:::::

---

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-representasjoner-standardform-underveisoppgave-2`. 

Bestem $f(x)$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-andregradsfunksjoner-representasjoner-standardform-underveisoppgave-2
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
:::



::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -x^2 + x + 2.
$$
::::


::::::::::::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med standardformen til en andregradsfunksjon

$$
f(x) = ax^2 + bx + c. 
$$

Vi trenger tre likninger fordi vi har tre ukjente koeffisienter. Vi kan lese av at grafen skjærer $y$-aksen i $y = 2$ som betyr at $c = 2$. 

Vi kan også se at grafen går gjennom punktene $(-1, 0)$ og $(2, 0)$ som gir oss likningssystemet

$$
f(-1) = 0 \quad \land \quad f(2) = 0 \quad \land \quad f(0) = 2
$$

som når vi regner ut gir oss 

$$
a - b + c = 0 \quad \land \quad 4a + 2b + c = 0 \quad \land \quad c = 2
$$

Denne gangen løser vi likningssystemet med CAS. 


````{tab} Geogebra

:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_2.html
---
:::

````


````{tab} Python

:::{raw} html
---
file: ./python/underveisoppgaver/underveisoppgave_2.html
---
:::

Kjører vi programmet, får vi utskriften 

```console
{a: -1, b: 1, c: 2}
```

````

Altså er 

$$
a = -1 \quad \land \quad  b = 1 \quad \land \quad c = 2
$$

som betyr at 

$$
f(x) = ax^2 + bx + c = -x^2 + x + 2.
$$

::::::::::::::

:::::::::::::::