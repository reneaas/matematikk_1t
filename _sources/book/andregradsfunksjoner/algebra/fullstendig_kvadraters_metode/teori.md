# Fullstendige kvadraters metode

:::{admonition} Læringsmål: Fullstendig kvadraters metode
---
class: tip
---
Etter denne seksjonen, er målet at du skal:
* Kunne bruke fullstendig kvadraters metode til å skrive om et andregradsuttrykk fra standardform til ekstremalform. 
* Kunne bruke konjugatsetningen til å skrive om et andregradsuttrykk fra ekstremalform til nullpunktsform.
* Kunne bestemme om en andregradsfunksjon har nullpunkter ved hjelp av fullstendig kvadraters metode og konjugatsetningen.
:::

:::::::::::::::{admonition} Repetisjon
---
class: reminder, full-width
---
Til nå har vi sett at ulike måter å skrive en andregradsfunksjon på gir oss ulik informasjon om funksjonen:

::::::::::::::{grid}
---
gutter: 1
---

:::::::::::::{grid-item-card} Standardform

:::{figure} ./figurer/teori/standardform/algebraisk_uttrykk.svg
---
width: 100%
---
:::

* $a$ forteller om grafen er konveks $\smile$ eller konkav $\frown$.
* $b$ gir forskyvningen til grafen langs $x$-aksen.
* $c$ forteller hvor grafen skjærer $y$-aksen.

:::::::::::::

:::::::::::::{grid-item-card} Nullpunktsform

:::{figure} ./figurer/teori/nullpunktsform/algebraisk_uttrykk.svg
---
width: 100%
---
:::

* $a$ forteller om grafen er konveks $\smile$ eller konkav $\frown$.
* $x_1$ og $x_2$ forteller hvor grafen skjærer $x$-aksen.

:::::::::::::

:::::::::::::{grid-item-card} Ekstremalform

:::{figure} ./figurer/teori/ekstremalform/algebraisk_uttrykk.svg
---
width: 100%
---
:::

* $a$ forteller om grafen er konveks $\smile$ eller konkav $\frown$.
* Gir oss ekstremalpunktet $(x_1, y_1)$.
* Gir oss symmetrilinja $x = x_1$.

:::::::::::::



:::::::::::::::

Så langt har vi sett av vi kan gå fra nullpunktsformen og fra ekstremalformen til standardformen – men å gå motsatt vei er ikke like rett frem. Her skal vi utvikle verktøy for å gå motsatt vei!

## Fra standardform til ekstremalform – fullstendige kvadraters metode

Fullstendige kvadraters metode lar oss skrive om et andregradsuttrykk på formen

$$
x^2 + bx + c
$$

fra standardform til ekstremalform. Det er ikke et uhell at $a = 1$ i uttrykket – men det kommer vi tilbake til senere. 

Den fungerer i to steg:
1. Legg til og trekk fra et tall så du får inn en kvadratsetning.
2. Faktoriser med kvadratsetningen. 

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Under følger tre eksempler på bruk av fullstendig kvadraters metode. Les gjennom eksemplene nøye og prøv å svare på følgende spørsmål:

1. Hvilket tall er det man legger til og trekker fra?
2. Kan du gi en beskrivelse av metoden?
3. Kan du finne en generell formel for hvordan man metoden funker med $x^2 + bx + c$?

Se i oppsummeringsboksen når du har lest eksemplene og prøvd å komme fram til en generell beskrivelse av metoden.

::::::::::::::{tab-set}
:::::::::::::{tab-item} Eksempel 1
\begin{align*}
    x^2 + 6x + 8 &= x^2 + 6x + \textcolor{red}{\left(\dfrac{6}{2}\right)^2} - \textcolor{red}{\left(\dfrac{6}{2}\right)^2} + 8 && \text{Legger til $0$}\\
    \\
    &= \underbrace{x^2 + 6x + \textcolor{red}{3^2}}_{\text{1.kvadratsetning}} - \textcolor{red}{3^2} + 8 && \text{Forenkler}\\
    \\
    &= (x + 3)^2 - 9 + 8 && \text{Faktoriserte med 1.kvadratsetning}\\
    \\
    &= (x + 3)^2 - 1.
\end{align*}

:::::::::::::

:::::::::::::{tab-item} Eksempel 2
\begin{align*}
    x^2 - 4x + 1 &= x^2 - 4x + \textcolor{red}{\left(\dfrac{-4}{2}\right)^2} - \textcolor{red}{\left(\dfrac{-4}{2}\right)^2} + 1 && \text{Legger til $0$}\\
    \\
    &= \underbrace{x^2 - 4x + \textcolor{red}{2^2}}_{\text{2.kvadratsetning}} - \textcolor{red}{2^2} + 1 && \text{Forenkler}\\
    \\
    &= (x - 2)^2 - 4 + 1 && \text{Faktoriserte med 2.kvadratsetning}\\
    \\
    &= (x - 2)^2 - 3.
\end{align*}
:::::::::::::

:::::::::::::{tab-item} Eksempel 3
\begin{align*}
    x^2 + 3x - 2 &= x^2 + 3x + \textcolor{red}{\left(\dfrac{3}{2}\right)^2} - \textcolor{red}{\left(\dfrac{3}{2}\right)^2} - 2 && \text{Legger til $0$}\\
    \\
    &= \underbrace{x^2 + 3x + \textcolor{red}{\left(\dfrac{3}{2}\right)^2}}_{\text{1.kvadratsetning}} - \textcolor{red}{\left(\dfrac{3}{2}\right)^2} - 2 && \text{Forenkler}\\
    \\
    &= (x + 3/2)^2 - 9/4 - 2 && \text{Faktoriserte med 1.kvadratsetning}\\
    \\
    &= (x + 3/2)^2 - 17/4.
\end{align*}

:::::::::::::

::::::::::::::


::::::::::::::


:::::::::::::::

Før du leser oppsummeringsboksen under, kan du prøve å anvende metoden i underveisoppgaven under!

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bruk fullstendige kvadraters metode på andregradsuttrykkene under.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
x^2 + 2x + 3
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x + 1)^2 + 2
$$
:::

:::::::::::::

:::::::::::::{tab-item} b
$$
x^2 - 10x + 3
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x - 5)^2 - 22
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
$$
x^2 + 12x + 17
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x + 6)^2 - 19
$$
:::
:::::::::::::

::::::::::::::


:::::::::::::::



---

---

:::::{admonition} Sjekk meg⚠️ – Oppsummering: Fullstendige kvadraters metode
---
class: summary, dropdown
---
For et andregradsuttrykk $x^2 + bx + c$ kan vi skrive skrive om uttrykket til ekstremalform med følgende omskrivning:

$$
x^2 + \textcolor{red}{b}x + c = \underbrace{x^2 + \textcolor{red}{b}x + \left(\dfrac{\textcolor{red}{b}}{2}\right)^2}_{\text{kvadratsetning}} - \left(\dfrac{\textcolor{red}{b}}{2}\right)^2 + c = \left(x + \dfrac{b}{2}\right)^2 - \left(\dfrac{b}{2}\right)^2 + c.
$$

Med andre ord, vi gjør følgende:
1. Legger til og trekker fra $\left(\dfrac{b}{2}\right)^2$.
2. Faktoriserer med 1. eller 2.kvadratsetning.

:::::

## Fra ekstremalform til nullpunktsform

Nå vet vi hvordan vi kan bruke fullstendige kvadraters metode til å gå fra standardform til ekstremalform. Det neste steget i prosessen er å gå fra ekstremalform til nullpunktsform – dette oppnår vi ved å bruke konjugatsetningen.


::::{admonition} Repetisjon: konjugatsetningen
---
class: reminder
---
For to tall $a, b \in \mathbb{R}$ har vi at

$$
(a + b)(a - b) = a^2 - b^2. 
$$
::::

Vi tar et eksempel.

:::::{admonition} Eksempel 1
---
class: example
---
En andregradsfunksjon er skrevet på ekstremalform:

$$
f(x) = (x + 3)^2 - 4 
$$

Bestem nullpunktsformen til $f(x)$. 

::::{admonition} Løsning
---
class: solution
---
Vi bruker konjugatsetningen:

$$
a^2 - b^2 = (a + b)(a - b) 
$$

til å skrive om uttrykket:

\begin{align*}
    f(x) &= (x + 3)^2 - 4 \\
    \\
    &= \underbrace{(x + 3)^2}_{\displaystyle a^2} - \underbrace{2^2}_{\displaystyle b^2} && \text{Setter $a = x + 3$ og $b = 2$}\\
    \\
    &= \underbrace{(x + 3 + 2)}_{\displaystyle (a + b)} \cdot \underbrace{(x + 3 - 2)}_{\displaystyle (a - b)} && \text{Konjugatsetningen}\\
    \\
    &= (x + 5)(x + 1).
\end{align*}

Altså er nullpunktsformen til $f(x)$ gitt ved 

$$
f(x) = (x + 5)(x + 1).
$$
::::
:::::

---

:::::{admonition} Underveisoppgave 2
---
class: check 
---
Skriv om $f(x)$ fra ekstremalformen 

$$
f(x) = (x - 2)^2 - 9
$$

til nullpunktsform.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = (x + 1)(x - 5)
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
\begin{align*}
    f(x) &= (x - 2)^2 - 9 \\
    \\
    &= \underbrace{(x - 2)^2}_{\displaystyle a^2} - \underbrace{3^2}_{\displaystyle b^2} && \text{Setter $a = x - 2$ og $b = 3$}\\
    \\
    &= \underbrace{(x - 2 + 3)}_{\displaystyle (a + b)} \cdot \underbrace{(x - 2 - 3)}_{\displaystyle (a - b)} && \text{Konjugatsetningen}\\
    \\
    &= (x + 1)(x - 5).
\end{align*}
:::

:::::



## Antall løsninger

Vi kan bruke strategiene vi har sett på her til å bestemme om hvor mange nullpunkter en andregradsfunksjon har. Vi tar et eksempel med to, én og ingen løsninger.

:::::::::::::::{admonition} Eksempel 2
---
class: example 
---
::::::::::::::{tab-set}

:::::::::::::{tab-item} To løsninger
En andregradsfunksjon er gitt ved

$$
f(x) = x^2 + 2x - 3
$$

Vi bruker først fullstendig kvadraters metode til å bestemme ekstremalformen:

\begin{align*}
    f(x) &= x^2 + 2x - 3 \\
    \\
    &= x^2 + 2x + 1 - 1 - 3 && \text{Legger til og trekker fra $1$}\\
    \\
    &= (x + 1)^2 - 4 && \text{Faktoriserte med 1.kvadratsetning}.
\end{align*}

Så prøver vi å bruke konjugatsetningen:

\begin{align*}
    f(x) &= (x + 1)^2 - 4 \\
    \\
    &= (x + 1)^2 - 2^2\\
    \\
    &= (x + 1 + 2)(x + 1 - 2) && \text{Konjugatsetningen}\\
    \\
    &= (x + 3)(x - 1).
\end{align*}

Altså ser vi at $f$ har nullpunktene 

$$
x = -3 \quad \lor \quad x = 1.
$$
:::::::::::::

:::::::::::::{tab-item} Én løsning
En andregradsfunksjon er gitt ved 

$$
f(x) = x^2 + 4x + 4
$$

Vi bruker først fullstendig kvadraters metode til å bestemme ekstremalformen:

\begin{align*}
    f(x) &= x^2 + 4x + 4 \\
    \\
    &= x^2 + 4x + 2^2 - 2^2 + 4 && \text{Legger til og trekker fra $4^2$}\\
    \\
    &= (x + 4)^2 && \text{Faktoriserte med 1.kvadratsetning}.
\end{align*}

Prøver vi å bruke konjugatsetingen her, får vi

\begin{align*}
    f(x) &= (x + 4)^2 \\
    \\
    &= (x + 4)^2 - 0^2 \\
    \\
    &= (x + 4 + 0)(x + 4 - 0) && \text{Konjugatsetningen}\\
    \\
    &= (x + 4)^2.
\end{align*}

Dermed har $f$ bare $x = -4$ som nullpunkt.
:::::::::::::

:::::::::::::{tab-item} Ingen løsninger

En andregradsfunksjon er gitt ved

$$
f(x) = x^2 + 2x + 3
$$

Vi bruker først fullstendig kvadraters metode til å bestemme ekstremalformen:

\begin{align*}
    f(x) &= x^2 + 2x + 3 \\
    \\
    &= x^2 + 2x + 1 - 1 + 3 && \text{Legger til og trekker fra $1$}\\
    \\
    &= (x + 1)^2 + 2 && \text{Faktoriserte med 1.kvadratsetning}.
\end{align*}

Her kan vi ikke skrive om uttrykket ved hjelp av konjugatsetningen $a^2 - b^2 = (a + b)(a - b)$ siden konstantleddet ikke er positivt. Dermed har $f$ ingen nullpunkter.
:::::::::::::
::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 3
---
class: check
---
For hver av andregradsfunksjonene under, bestem hvor mange nullpunkter funksjonen har.
::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
$$
f(x) = x^2 + 6x + 9
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
Ett nullpunkt.
:::
:::::::::::::

:::::::::::::{tab-item} b
$$
g(x) = x^2 - 4x - 5
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
To nullpunkter.
:::
:::::::::::::

:::::::::::::{tab-item} c
$$
h(x) = x^2 - 4x + 5
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
Ingen nullpunkter.
:::
:::::::::::::
::::::::::::::


:::::::::::::::


<!-- ---

## Fullstendige kvadrater

Vi har allerede sett at vi kan skrive om et andregradsuttrykk på formen $ax^2 + bx + c$ til en form som er lettere å jobbe med. Dette gjør vi ved å fullføre kvadrater. 1. og 2.kvadratsetning er eksempler på fullstendige kvadrater. Det kan vi se i {numref}`fullstendig_kvadrat`.

:::{figure} ./figurer/teori/fullstendig_kvadrat.svg
---
width: 80%
---
Viser 1.kvadratsetning geometrisk. Et kvadrat med areal $(a + b)^2$ har samme areal som summen av arealene til to kvadrater med areal $a^2$ og $b^2$, og to rektangler med areal $ab$. Dermed får vi $(a + b)^2 = a^2 + 2ab + b^2$. Det er herfra begrepet *fullstendig kvadrat* kommer fra.
::: -->