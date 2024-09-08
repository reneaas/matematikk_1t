# Grafisk representasjon av lineære funksjoner

:::{admonition} Læringsmål: Grafisk representasjon av lineære funksjoner
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Kunne lese av funksjonsverdier fra grafen til en lineær funksjon.
* Kunne lese av koeffisientene til en lineær funksjon fra grafen. 
* Kunne tegne grafen til en lineær funksjon.
:::

## Koordinatsystemet
Når vi jobber med funksjoner grafisk, kommer vi til å bruke koordinatsystemet og punkter i koordinatsystemet. Det er derfor viktig at vi kan lese og bruke koordinatssystemet godt før vi ser på grafisk representasjon av lineære funksjoner.


::::{admonition} Koordinatsystemet
---
class: theory
---
Koordinatsystemet består av to tallinjer som vi kaller for **akser**. De to aksene er:
* $x$-aksen (den horisontale aksen - også kalt *førsteaksen*).
* $y$-aksen (den vertikale aksen - også kalt *andreaksen*).

Punktet der aksene møtes kaller vi for **origo**. Origo har koordinatene $(0, 0)$.

For å finne et punkt $(x, y)$ i koordinatsystemet, går vi $x$ plasser parallelt med $x$-aksen og $y$ plasser parallelt med $y$-aksen. Da står vi på punktet $(x, y)$. 
Vi kaller $x$-verdien til punktet for $x$-koordinaten og $y$-verdien for $y$-koordinaten.

I {numref}`fig-koordinatsystem` viser vi et konkret eksempel med punktet $(3, 2)$.

:::{figure} figurer/teori/koordinatsystem.svg
---
width: 80%
name: fig-koordinatsystem
---
viser et koordinatsystem med punktet $(3, 2)$. For å finne punktet går vi $3$ plasser parallelt med $x$-aksen og $2$ plasser parallelt med $y$-aksen. 
:::
::::

---

::::{admonition} Underveisoppgave 1
---
class: check
---

I {numref}`fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-1` vises seks punkter $A$, $B$, $C$, $D$, $E$ og $F$. 

:::{figure} figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-1
width: 80%
---
viser seks punkter $A$, $B$, $C$, $D$, $E$ og $F$ i et koordinatsystem.
:::

Sett sammen riktig punkt med riktig koordinater.

:::{raw} html
---
file: ./pair_puzzles/underveisoppgaver/underveisoppgave_1.html
---
:::

::::

---

## Funksjonsverdier fra graf

Når er vi klare for å se på hvordan vi kan lese av funksjonsverdier fra grafen til en lineær funksjon.

::::{admonition} Funksjonsverdier fra graf
---
class: theory
---
Gitt grafen til en lineær funksjon $f$, kan vi lese av funksjonsverdien $f(x)$ ved å lese av $y$-koordinaten til et punkt $(x, y)$ på grafen til $f$. Ideen er illustrert i {numref}`fig-lineær-funksjoner-grafisk-representasjon-teori-1`.


:::{figure} figurer/teori/grafisk_representasjon.svg
---
width: 80%
name: fig-lineær-funksjoner-grafisk-representasjon-teori-1
---
viser grafen til en lineær funksjon $f$ og et punkt $(x, y) = (x, f(x))$ på grafen til $f$. Funksjonsverdien $f(x)$ leser vi av som $y$-koordinaten til punktet.
:::

::::

---

::::{admonition} Underveisoppgave 2
---
class: check
---

:::{figure} figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-2
width: 80%
---
vises grafen til en lineær funksjon $f$.
:::

Sett sammen funksjonsverdiene med riktig $y$-koordinat.

:::{raw} html
---
file: ./pair_puzzles/underveisoppgaver/underveisoppgave_2.html
---
:::

::::

---

## Koeffisientene til en lineær funksjon

Nå som vi vet hvordan vi leser av funksjonsverdier fra en graf, er det på tide å se på sammenhengen mellom grafen til en lineær funksjon og den algebraiske representasjonen av funksjonen. 
Det viser seg at koeffisientene $a$ og $b$ i en lineær funksjon $f(x) = ax + b$ har en grafisk tolkning som lar oss hente ut egenskapene til funksjonen fra grafen.


:::{admonition} "Stigningstall"
---
class: sidenote, margin
---
Merk at selv om $a$ kalles for "stigningstall", så kan $a$ også være negativ. I dette tilfellet vil grafen til $f$ gå nedover når $x$ øker.
:::

::::{admonition} Koeffisientene til en lineær funksjon
---
class: theory
---
For en lineær funksjon $f(x) = ax + b$, vil koeffisientene $a$ og $b$ ha følgende grafiske tolkning:

Stigningstall $a$
: Bestemmer hvor mye funksjonsverdien $f(x)$ endrer seg når vi øker $x$ med $1$. Det vil si når vi øker $x \to x + 1$. 

Konstantledd $b$
: Bestemmer hvor grafen til $f$ skjærer $y$-aksen. Det vil si hva funksjonsverdien er når $x = 0$. 


{numref}`fig-lineær-funksjoner-grafisk-representasjon-teori-2` viser en illustrasjon av sammenhengen mellom grafen til en lineær funksjon og koeffisientene $a$ og $b$.

:::{figure} figurer/teori/koeffisienter.svg
---
name: fig-lineær-funksjoner-grafisk-representasjon-teori-2
width: 80%
---
viser grafen til en lineær funksjon $f(x) = ax + b$. Stigningstallet $a$ bestemmer hvor mye funksjonsverdien endrer seg når vi øker $x$ med $1$. Konstantleddet $b$ bestemmer hvor grafen skjærer $y$-aksen.
:::


::::

---

Vi tar med noen eksempler så vi kan se sammenhengen tydligere:

::::{admonition} Eksempel 2: Koeffisienter og grafer
---
class: example
---

I fanene under vises eksempler på grafene til lineære funksjoner og hvordan disse henger sammen med koeffisientene $a$ og $b$ i funksjonsuttrykket.
````{tab-set}
```{tab-item} $f(x) = 2x + 1$

:::{figure} ./figurer/eksempler/eksempel_2/f.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-eksempel-1-f
width: 80%
---

viser grafen til $f(x) = 2x + 1$. Grafen skjærer $y$-aksen i $y = 1$ - derfor er $b = 1$. Når vi øker verdien til $x$ med $1$, øker funksjonsverdien med $2$ - derfor er $a = 2$.
:::

```

```{tab-item} $g(x) = x - 1$

:::{figure} ./figurer/eksempler/eksempel_2/g.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-eksempel-1-g
width: 80%
---

viser grafen til $g(x) = x - 1$. Grafen skjærer $y$-aksen i $y = -1$ - derfor er $b = -1$. Når vi øker verdien til $x$ med $1$, øker funksjonsverdien med $1$ - derfor er $a = 1$.
:::

```

```{tab-item} $h(x) = -4x + 3$

:::{figure} ./figurer/eksempler/eksempel_2/h.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-eksempel-1-h
width: 80%
---

viser grafen til $h(x) = -4x + 3$. Grafen skjærer $y$-aksen i $y = 3$ - derfor er $b = 3$. Når vi øker verdien til $x$ med $1$, synker funksjonsverdien med $4$ - derfor er $a = -4$.
:::

```

```{tab-item} $p(x) = -3x$

:::{figure} ./figurer/eksempler/eksempel_2/p.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-eksempel-1-p
width: 80%
---

viser grafen til $p(x) = -3x$. Grafen skjærer $y$-aksen i $y = 0$ - derfor er  $b = 0$. Når vi øker verdien til $x$ med $1$, synker funksjonsverdien med $3$ - derfor er $a = -3$.
:::

```
````

::::

---

Så er **din tur**!

::::{admonition} Underveisoppgave 3
---
class: check
---
I figur {numref}`fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-3` vises grafene til noen lineære funksjoner. 

:::{figure} figurer/underveisoppgaver/underveisoppgave_3.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-3
width: 80%
---
viser grafene til noen lineære funksjoner.
:::

Sett sammen riktig graf med riktig funksjonsuttrykk.


:::{raw} html
---
file: ./pair_puzzles/underveisoppgaver/underveisoppgave_3.html
---
:::

::::
