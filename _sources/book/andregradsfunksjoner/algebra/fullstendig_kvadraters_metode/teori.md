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
Til nå har vi sett at ulike måtene å skrive en andregradsfunksjon på gir oss ulik informasjon om funksjonen:

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

## Fullstendige kvadraters metode

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

:::::{admonition} Fullstendige kvadraters metode
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




Nå er det **din tur**!

````{admonition} Underveisoppgave 1
:class: check
Bruk fullstendig kvadraters metode til å skrive om andregradsfunksjonen

$$
g(x) = x^2 - 4x + 2.
$$

```{admonition} Løsning
:class: solution, dropdown
Vi har 

\begin{equation*}
\begin{split}
x^2 - 4x + 2 & = x^2 - 4x + \underbrace{\left(\frac{-4}{2}\right)^2 - \left(\frac{-4}{2}\right)^2}_{\text{Legger til og trekker fra }(b/2)^2} + 2 \\
\\
&= \underbrace{x^2 - 4x + 2^2}_{\text{2.kvadratsetning}} - 2^2 + 2 = (x - 2)^2 - 4 + 2 \\
\\
& = (x - 2)^2 - 2.
\end{split}
\end{equation*}
```
````

## Fullstendig kvadraters metode for å løse andregradslikninger
Vi kan bruke fullstendig kvadraters metode for å løse andregradslikninger av typen

$$
x^2 + bx + c = 0.
$$

Metoden funker som følger:

Steg 1:
: Skriv om andregradsuttrykket med fullstendig kvadraters metode.

Steg 2:
: Prøv å bruke konjugatsetningen til å faktorisere uttrykket. Hvis tilleggsleddet er positivt, er dette umulig og likningen har ingen reelle løsninger. Hvis tilleggsleddet er negativt, kan vi faktorisere uttrykket og løse likningen. Hvis tilleggsleddet er null, har du allerede faktorisert uttrykket fullstendig.

Steg 3:
: Bruk produktregelen til å løse likningen $x^2 + bx + c = 0$ med det faktoriserte uttrykket.


```{admonition} Påminnelse: konjugatsetningen
:class: note, margin
$$
p^2 - q^2 = (p - q)(p + q)
$$
```


Vi tar et eksempel:

```{admonition} Eksempel 2: Fullstendig kvadraters metode og andregradslikninger
:class: example

La oss si vi vil løse likningen

$$
f(x) = x^2 - 4x - 5 = 0, 
$$

Steg 1:
: Vi bruker fullstendig kvadraters metode for å skrive om andregradsuttrykket:
\begin{equation*}
\begin{split}
x^2 - 4x - 5 & = x^2 - 4x + \underbrace{\left(\frac{-4}{2}\right)^2 - \left(\frac{-4}{2}\right)^2}_{\text{Legger til og trekker fra }(b/2)^2} - 5 \\
\\
&= \underbrace{x^2 - 4x + 2^2}_{\text{2.kvadratsetning}} - 2^2 - 5 = (x - 2)^2 - 4 - 5 \\
\\
& = (x - 2)^2 - 9.
\end{split}
\end{equation*}

Steg 2:
: Vi kan merke oss at her er tilleggsleddet negativt, som betyr at vi kan faktorisere uttrykket ved å bruke konjugatsetningen som følger:

$$
f(x) = (x - 2)^2 - 9 = \underbrace{(x - 2)^2}_{p^2} - \underbrace{3^2}_{q^2}= \underbrace{(x - 2 - 3)}_{(p - q)} \cdot \underbrace{(x - 2 + 3)}_{(p + q)} = (x - 5)(x + 1).
$$

Steg 3:
: Nå bruker vi produktregelen til å løse likningen $f(x) = 0$:

$$
(x - 5)(x + 1) = 0 \quad \Leftrightarrow \quad x - 5 = 0 \quad \lor \quad x + 1 = 0,
$$

som gir løsningene 

$$
x = 5 \quad \lor \quad x = -1.
$$
```

**Din tur**!

````{admonition} Underveisoppgave 2
:class: check
Løs likningen 

$$
x^2 - x - 2 = 0.
$$


```{admonition} Løsning
:class: solution, dropdown
Steg 1:
: Vi bruker fullstendig kvadraters metode for å skrive om andregradsuttrykket:

\begin{equation*}
\begin{split}
x^2 - x - 2 & = x^2 - x + \left(\frac{-1}{2}\right)^2 - \left(\frac{-1}{2}\right)^2 - 2 \\
\\
& = \underbrace{x^2 - x + \left(\frac{1}{2}\right)^2}_{=(x - 1/2)^2} - \left(\frac{1}{2}\right)^2 - 2 = \left(x - \frac{1}{2}\right)^2 - \frac{1}{4} - 2 \\
\\
& = \left(x - \frac{1}{2}\right)^2 - \frac{9}{4}.
\end{split}
\end{equation*}

Steg 2:
: Vi bruker konjugatsetningen for å faktorisere andregradsuttrykket fullstendig:

\begin{equation*}
\begin{split}
\left(x-\frac{1}{2}\right)^2 - \frac{9}{4} & = \left(x-\frac{1}{2}\right)^2 - \left(\frac{3}{2}\right)^2 \\
\\
& = \left(x-\frac{1}{2} - \frac{3}{2}\right)\left(x-\frac{1}{2} + \frac{3}{2}\right) \\
\\
& = (x-2)(x+1).
\end{split}
\end{equation*}

Steg 3
: Nå er andregradsuttrykket fullstendig faktorisert, så vi kan løse likningen ved å bruke produktregelen:

$$
(x - 2)(x + 1) = 0 \quad \Leftrightarrow \quad x - 2 = 0 \quad \lor \quad x + 1 = 0,
$$

som gir løsningene

$$
x = 2 \quad \lor \quad x = -1.
$$
```
````

## Antall løsninger

Vi kan bruke fullstendig kvadraters metode til å avgjøre hvor mange løsninger en andregradslikning har, eller sagt på en annen måte, hvor mange nullpunkter en andregradsfunksjon har.

```{admonition} Setning: Antall løsninger for en andregradslikning
:class: theory
Gitt en andregradsfunksjon på formen

$$
f(x) = x^2 + bx + c,
$$

så har likningen $f(x) = 0$:
* To løsninger hvis $c - (b/2)^2 < 0$.
* Én løsning hvis $c - (b/2)^2 = 0$.
* Ingen løsninger hvis $c - (b/2)^2 > 0$.
```


La oss se på et eksempel der vi ser alle tre tilfellene oppstå:

```{admonition} Eksempel 3: Antall løsninger for en andregradslikning
:class: example

To løsninger
: Vi tar for oss andregradslikningen $x^2 + x - 6 = 0$. Fullfører vi kvadratet, får vi

$$
x^2 + x - 6 = x^2 + x + \left(\frac{1}{2}\right)^2 - \left(\frac{1}{2}\right)^2 - 6 = \left(x + \frac{1}{2}\right)^2 - \frac{1}{4} - 6 = \left(x + \frac{1}{2}\right)^2 - \frac{25}{4}.
$$

Siden tilleggsleddet er negativt, kan vi bruke konjugatsetningen og må nødvendigvis ende opp med to forskjellige lineære faktorer. Dermed har likningen to løsninger.

Én løsning
: Vi tar for oss andregradslikningen $x^2 - 4x + 4 = 0$. Fullfører vi kvadratet, får vi

$$
x^2 - 4x + 4 = x^2 - 4x + 2^2 - 2^2 + 4 = (x - 2)^2 - 4 + 4 = (x - 2)^2.
$$

Her er tilleggsleddet null, så vi har bare én løsning. Dette er ikke så overraskende siden vi effektivt her har bare gjort en tungvint måte å bruke 2.kvadratsetning på. 

Ingen løsninger
: Vi tar for oss andregradslikningen $x^2 + 2x + 2 = 0$. Fullfører vi kvadratet, får vi

$$
x^2 + 2x + 1 - 1 + 2 = (x + 1)^2 - 1 + 2 = (x + 1)^2 + 1.
$$

Her kan vi ikke bruke konjugatsetningen fordi tilleggsleddet er positivt. Dermed har likningen ingen reelle løsninger.

```

---

## Fullstendige kvadrater

Vi har allerede sett at vi kan skrive om et andregradsuttrykk på formen $ax^2 + bx + c$ til en form som er lettere å jobbe med. Dette gjør vi ved å fullføre kvadrater. 1. og 2.kvadratsetning er eksempler på fullstendige kvadrater. Det kan vi se i {numref}`fullstendig_kvadrat`.

:::{figure} ./figurer/teori/fullstendig_kvadrat.svg
---
width: 80%
---
Viser 1.kvadratsetning geometrisk. Et kvadrat med areal $(a + b)^2$ har samme areal som summen av arealene til to kvadrater med areal $a^2$ og $b^2$, og to rektangler med areal $ab$. Dermed får vi $(a + b)^2 = a^2 + 2ab + b^2$. Det er herfra begrepet *fullstendig kvadrat* kommer fra.
:::