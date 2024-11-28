# Den deriverte

::::{admonition} Læringsmål
---
class: tip
---
* Kunne regne ut den deriverte til en andregradsfunksjon.
* Kunne redegjøre for sammenhengen mellom den deriverte, momentan vekstfart og stigningstallet til tangenter. 
::::

## Den deriverte til en andregradsfunksjon

Når vi definerte momentan vekstfart, så vi på dette som stigningstallet til tangenter som gikk gjennom et punkt på grafen til en andregradsfunksjon. Vi oppdaget så en måte å regne ut dette stigningstallet ved hjelp av en sekant. Siden $f'(x)$ varierer med $x$, er det naturlig å tenke på $f'$ som en funksjon i seg selv med tett tilknytning til $f$. 

::::{admonition} Definisjon: den deriverte
---
class: theory
---
Den momentane vekstfarten til $f$ i et punkt $x$ skrives som $f'(x)$. Vi kaller $f'$ for **den deriverte** til $f$. 

Vi tolker $f'(x)$ som funksjonsverdien til den deriverte i $x$.
::::

## Grafisk representasjon 

Den deriverte $f'(x)$ gir oss den momentane vekstfarten i et punkt $x$ på grafen til $f$. Siden vi kan variere $x$, betyr det at vi kan tolke $f'(x)$ som en funksjonsverdi i et punkt $x$. Da er det naturlig å undersøke noen grafiske egenskaper ved $f'$ og hvordan disse henger sammen med grafen til $f$. 

:::::{admonition} Utforsk 1
---
class: explore
---
Under vises en animasjon som viser sammenhengen mellom tangenter til grafen til $f(x) = x^2$, og grafen til den deriverte $f'$. 

Grafen til $f$ er vist til venstre og grafen til $f'$ blir tegnet til høyre ut ifra tangentene til $f$.

1. Se på animasjonen.
2. Hva er $f'(x)$ i symmetrilinja til $f$? 
3. Overbevis deg selv om at du kan forklare sammenhengen mellom tangentene til grafen til $f$ og grafen til $f'$. 
4. Kan du bestemme $f'(x)$ ut ifra grafen til animasjonen?

:::{video} ./koder/animasjoner/media/videos/den_deriverte2/1440p60/den_deriverte2.mp4
---
width: 95%
---
:::
:::::

---

:::::{admonition} Underveisoppgave 1
---
class: check
---
I {numref}`fig-andregradsfunksjoner-vekstfart-den-deriverte-underveisoppgave-1` vises grafen til 

$$
f(x) = (x - 1)^2.  
$$

Lag en skisse av grafen til $f'$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/f.svg
---
name: fig-andregradsfunksjoner-vekstfart-den-deriverte-underveisoppgave-1
width: 80%
class: no-click
---
viser grafen til $f(x) = (x - 1)^2$.
:::

:::{admonition} Hint
---
class: hints, dropdown
---
Hva vet du om $f'(x)$ i symmetrilinja? Bruk dette som utgangspunkt for å lage skissen av grafen til $f'$.
:::

::::{admonition} Fasit
---
class: dropdown, answer
---

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/f_derivert.svg
---
name: fig-andregradsfunksjoner-vekstfart-den-deriverte-underveisoppgave-1-fasit
width: 80%
class: no-click
---
viser grafen til $f'$ for $f(x) = (x - 1)^2$.
:::
::::

:::::



## Algebraisk representasjon

Fra Utforsk 1 kan vi konkludere at grafen til $f'$ er en lineær funksjon når $f$ er en andregradsfunksjon. Kan det tenkes at vi kan finne en helt generell sammenheng mellom funksjonsuttrykkene $f(x)$ og $f'(x)$?

:::::{admonition} Utforsk 2
---
class: explore
---
Den momentane vekstfarten $f'(x)$ i et punkt $x$ på grafen til $f$ kan bestemmes ved å regne ut gjennomsnittlig vekstfart i et intervall med $x$ som midtpunkt. 

Bruk denne strategien til å finne en generell formel ved å regne ut den gjennomsnittlige vekstfarten i intervallet $[x - 1, x + 1]$ for 

$$
f(x) = ax^2 + bx + c
$$


::::{admonition} Løsning 
---
class: dropdown, solution
---
$$
f'(x) = \dfrac{f(x + 1) - f(x - 1)}{(x + 1) - (x - 1)} = \dfrac{f(x + 1) - f(x - 1)}{2}
$$

Vi kan regne ut de to funksjonsverdiene:

\begin{align*}
    f(x + 1) &= a(x + 1)^2 + b(x + 1) + c \\
    \\
    f(x - 1) &= a(x - 1)^2 + b(x - 1) + c
\end{align*}

Så setter vi det inn i formelen for den momentane vekstfarten:

\begin{align*}
    f'(x) &= \dfrac{f(x + 1) - f(x - 1)}{2} \\
    \\
    &= \dfrac{a(x + 1)^2 + b(x + 1) + c - a(x - 1)^2 - b(x - 1) - c}{2} \\
    \\
    &= \dfrac{a(x + 1)^2 - a(x - 1)^2 + b(x + 1) - b(x - 1)}{2} \\
    \\
    &= \dfrac{a\left((x + 1)^2 - (x - 1)^2\right) + bx + b - bx + b}{2} \\
    \\
    &= \dfrac{a(x + 1 + x - 1)(x + 1 - (x - 1)) + 2b}{2} \\
    \\
    &= \dfrac{a(2x)\cdot(2) + 2b}{2} \\
    \\
    &= \dfrac{4ax + 2b}{2} \\
    \\
    & = 2ax + b
\end{align*}

Dermed er den momentane vekstfarten i $x$ generelt gitt ved 

$$
f'(x) = 2ax + b.
$$

Denne funksjonen kaller vi for **den deriverte** til $f$ og skriver $f'(x)$. Denne gir oss den momentane vekstfarten til $f$ i $x$.
::::
:::::

---

:::::{admonition} Oppsummering: den deriverte
---
class: summary, dropdown
---
Den deriverte $f'(x)$ til en andregradsfunksjon $f(x) = ax^2 + bx + c$ er gitt ved 

$$
f'(x) = 2ax + b.
$$

Den deriverte til en andregradsfunksjon er altså en lineær funksjon med stigningstall $2a$ og konstantledd $b$.
:::::

---

:::::{admonition} Eksempel 1
---
class: example
---
En andregradsfunksjon er gitt ved 

$$
f(x) = x^2 - 2x + 3. 
$$

Bestem $f'(x)$. 

::::{admonition} Løsning
---
class: solution
---
Den deriverte til $f(x) = ax^2 + bx + c$ er gitt ved 

$$
f'(x) = 2ax + b. 
$$

Fra $f(x)$ kan vi lese av at $a = 1$ og $b = -2$. Dermed er

$$
f'(x) = 2\cdot 1 \cdot x + (-2) = 2x - 2.
$$
::::
:::::

---


::::{admonition} Underveisoppgave 2
---
class: check
---
Bestem den deriverte til 

$$
f(x) = 3x^2 + 4x + 1.
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f'(x) = 6x + 4
$$
:::
::::


## Fortegnslinje for den deriverte
I mange tilfeller vil det bli nyttig å kunne tolke fortegnslinjer for $f'(x)$ for å avgjøre:
* Hvor grafen til $f$ stiger eller synker
* Hvor grafen til $f$ har topp- eller bunnpunkt. 

:::::::::::::::{admonition} Tolkning av fortegnslinjen til den deriverte
---
class: summary
---
Fra fortegnslinjen til $f'(x)$ kan vi lese av:
* Hvor grafen til $f$ stiger eller synker – dette kaller vi for grafens **monotoniegenskaper**.
* Hvor grafen til $f$ har et topp- eller bunnpunkt.

::::::::::::::{tab-set}
:::::::::::::{tab-item} Konveks graf
:::{figure} ./figurer/teori/fortegnslinjer/konveks_graf.svg
---
width: 80%
class: no-click
---
:::

:::{figure} ./figurer/teori/fortegnslinjer/konveks_fortegnslinje.svg
---
width: 100%
class: no-click
---
:::
:::::::::::::

:::::::::::::{tab-item} Konkav graf
:::{figure} ./figurer/teori/fortegnslinjer/konkav_graf.svg
---
width: 80%
class: no-click
---
:::

:::{figure} ./figurer/teori/fortegnslinjer/konkav_fortegnslinje.svg
---
width: 100%
class: no-click
---
:::
:::::::::::::
::::::::::::::

:::::::::::::::

<!-- ## Fortegnlinjer for den deriverte

Når vi jobber med den deriverte, kan vi tegne fortegnslinjer enten direkte fra grafen til $f$ eller fra $f'(x)$ for å avgjøre om grafen til $f$ har et topp- eller bunnpunkt.  -->