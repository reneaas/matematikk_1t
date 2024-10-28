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


## Fullstendige kvadrater

Vi har allerede sett at vi kan skrive om et andregradsuttrykk på formen $ax^2 + bx + c$ til en form som er lettere å jobbe med. Dette gjør vi ved å fullføre kvadrater. 1. og 2.kvadratsetning er eksempler på fullstendige kvadrater. Det kan vi se i {numref}`fullstendig_kvadrat`.

```{figure} ./figurer/teori/fullstendig_kvadrat.svg
:name: fullstendig_kvadrat
:width: 80%
Viser 1.kvadratsetning grafisk. Et kvadrat med areal $(p + q)^2$ har samme areal som summen av arealene til to kvadrater med areal $p^2$ og $q^2$, og to rektangler med areal $pq$. Dermed får vi $(p + q)^2 = p^2 + 2pq + q^2$. Det er herfra begrepet *fullstendig kvadrat* kommer fra.
```

:::::{admonition} Bestemme nullpunkter og ekstremalpunkter til $f(x) = ax^2 + bx + c$
---
class: theory
---

$$
f(x) = ax^2 + bx + c \xarrow{\text{fullstendig kvadraters metode}} a(x + r)^2 + k \xarrow{\text{konjugatsetningen}} a(x - x_1)(x - x_2)
$$

:::::


## Fullstendige kvadraters metode

Fullstendig kvadraters metode er en måte å skrive om et andregradsuttrykk om fra standardform til ekstremalform. Da kan vi lese av ekstremalpunktet til funksjonen. Bruker 


```{admonition} Fullstendige kvadraters metode
:class: theory
Gitt en andregradsfunksjon

$$
f(x) = ax^2 + bx + c,
$$

kan vi alltid skrive om funksjonsuttrykket som

$$
f(x) = a(x + r)^2 + k,
$$

der 

$$
r = \frac{b}{2a} \quad \text{og} \quad k = c - \left(\frac{b}{2a}\right)^2.
$$
```


```{admonition} Algoritme: Fullstendige kvadraters metode
:class: theory
Gitt et andregradsuttrykk $x^2 + bx + c$. For å skrive dette uttrykket som et fullstendig kvadrat, gjør vi følgende:

Steg 1
: Legg til og trekk fra $(b / 2)^2$

$$
x^2 + bx + c = x^2 + bx + \underbrace{\left(\frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2}_{\text{Legg til og trekk fra } (b/2)^2} + c.
$$

Steg 2
: Bruk 1. eller 2.kvadratsetning til å faktorisere deler eller hele uttrykket.

$$
\underbrace{x^2 + bx + \left(\frac{b}{2}\right)^2}_{\text{1. eller 2.kvadratsetning}} - \left(\frac{b}{2}\right)^2 + c = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2 + c.
$$

Samlet, får vi

$$
x^2 + bx + c = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2 + c.
$$

```

Ser ut som skumle greier, så la oss ta et eksempel:


```{admonition} Eksempel 1: fullstendig kvadraters metode
:class: example
Gitt andregradsfunksjonen

$$
f(x) = x^2 + 6x + 8,
$$

så kan vi fullføre kvadratet som følger:

\begin{equation*}
\begin{split}
x^2 + 6x + 10 & = x^2 + 6x + \underbrace{\left(\frac{6}{2}\right)^2 - \left(\frac{6}{2}\right)^2}_{\text{Legger til og trekker fra }(b/2)^2} + 8 \\
\\
&= \underbrace{x^2 + 6x + 3^2}_{\text{1.kvadratsetning}} - 3^2 + 8 = (x + 3)^2 - 9 + 8 \\
\\
& = (x + 3)^2 - 1.
\end{split}
\end{equation*}

Vi kan altså skrive $f(x)$ som et fullstendig kvadrat minus et tilleggsledd. 
```

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