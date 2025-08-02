# Standardform


:::{admonition} Læringsmål
---
class: tip
---
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
class: no-click, adaptive-figure
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
class: explore
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
Effekten til $b$ er påvirket av fortegnet til $a$. Du finner ett vindu med $a > 0$ og ett med $a < 0$.

1. Hva skjer med grafen når $b = 0$?
2. Hva skjer med grafen når $b > 0$? 
3. Hva skjer med grafen når $b < 0$?

::::::::::::{tab-set}
:::::::::::{tab-item} Når $a > 0$

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/b_1.html
---
:::

:::::::::::

:::::::::::{tab-item} Når $a < 0$

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/b_2.html
---
:::

:::::::::::

::::::::::::


:::{admonition} Oppsummering: Koeffisient $b$
---
class: summary, dropdown
---

````{tab} $a > 0$
1. Når $b = 0$, vil grafen være symmetrisk om $y$-aksen. 
2. Når $b > 0$, forskyver vi grafen til venstre for $y$-aksen.
3. Når $b < 0$, forskyver vi grafen til høyre for $y$-aksen. 

````

````{tab} $a < 0$
1. Når $b = 0$, vil grafen være symmetrisk om $y$-aksen. 
2. Når $b > 0$, forskyver vi grafen til høyre for $y$-aksen.
3. Når $b < 0$, forskyver vi grafen til venstre for $y$-aksen. 
````

Effekten til $b$ er altså motsatt når $a < 0$ sammenlignet med når $a > 0$.
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

> Jobb med Utforsk 1 **før** du ser på oppsummeringen under.

:::::::::::::::{admonition} Oppsummering: koeffisienter og graf
---
class: summary
---
Påvirkningen til koeffisientene til en andregradsfunksjon $f(x) = ax^2 + bx + c$ kan oppsummeres som:

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} Koeffisient $a$

$a$ bestemmer om grafen er konveks (smiler $\smile$ ) eller konkav (surt fjes $\frown$). 

:::{figure} ./figurer/utforsk/utforsk_1/a.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::

:::::::::::::{tab-item} Koeffisient $b$
Bestemmer forskyvningen av grafen fra $y$-aksen. Fortegnet til $a$ bestemmer hvilken retning $b > 0$ og $b < 0$ gir.


::::::::::::{tab-set}
:::::::::::{tab-item} $a > 0$

:::{figure} ./figurer/utforsk/utforsk_1/b_1.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::

:::::::::::{tab-item} $a < 0$

:::{figure} ./figurer/utforsk/utforsk_1/b_2.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::

::::::::::::

:::::::::::::

:::::::::::::{tab-item} Koeffisient $c$
Bestemmer hvor grafen skjærer $y$-aksen.

:::{figure} ./figurer/utforsk/utforsk_1/c.svg
---
width: 100%
class: no-click, adaptive-figure
---
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
class: no-click, adaptive-figure
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

Vi har tre ukjente koeffisienter – vi må derfor ha tre likninger for å kunne bestemme $a$, $b$ og $c$. 

Fra {numref}`fig-andregradsfunksjoner-representasjoner-standardform-eksempel-2`, kan vi lese av at grafen til $f$ går gjennom punktene $(0, -6)$ og $(-2, 0)$ og $(3, 0)$. Dette betyr at $f(x)$ må oppfylle likningssystemet:

\begin{align*}
    f(0) &= -6 && \text{Punktet $(0, -6)$} \\
    \\
    f(-2) &= 0 && \text{Punktet $(-2, 0)$} \\
    \\
    f(3) &= 0 && \text{Punktet $(3, 0)$}
\end{align*}


Vi løser likningssystemet med CAS: 

:::{figure} ./figurer/eksempler/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::



Dermed er 

$$
a = 1 \and b = -1 \and c = -6.
$$

Da følger det at

$$
f(x) = a\cdot x^2 + b \cdot x + c = x^2 - x - 6.
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
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::


:::{cas-popup} 420 500
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

Vi trenger tre likninger fordi vi har tre ukjente koeffisienter. Vi kan lese av grafen til $f$ går gjennom punktene $(-1, 0)$, $(2, 0)$ og $(1, 2)$. Da kan vi sette opp likningssystemet:

\begin{align*}
    f(-1) &= 0 && \text{Punktet $(-1, 0)$} \\
    \\
    f(2) &= 0 && \text{Punktet $(2, 0)$} \\
    \\
    f(1) &= 2 && \text{Punktet $(1, 2)$}
\end{align*}

Vi løser likningssystemet med CAS:

:::{figure} ./figurer/underveisoppgaver/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::



Altså er 

$$
a = -1 \and b = 1 \and c = 2
$$

som betyr at 

$$
f(x) = ax^2 + bx + c = -x^2 + x + 2.
$$

::::::::::::::

:::::::::::::::