# $abc$-formelen

På dette tidspunktet har vi gjort nok forberedelser til å kunne komme fram til en helt generell løsning for *alle* andregradslikninger når de er skrevet på formen

$$
ax^2 + bx + c = 0.
$$

Løsningen av likningen kalles ofte for **$abc$-formelen** fordi den inneholder koeffisientene $a$, $b$ og $c$. Vi skal første presentere den generelle løsningen og deretter utlede den ved hjelp av teknikkene vi har sett på så langt.

## Den generelle løsningen

:::{admonition} Setning: $abc$-formelen
---
class: theory
---
Gitt en andregradslikning på formen

$$
ax^2 + bx + c = 0 \, ,
$$

der den generelle løsningen gitt ved

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \, .
$$
:::

Vi tar et eksempel før vi utleder formelen og viser at den stemmer.

:::{admonition} Eksempel 1: $abc$-formelen
---
class: example
---

Vi tar for oss andregradslikningen

$$
x^2 - 4x - 5 = 0.
$$

Her ser vi at $a = 1$, $b = -4$ og $c = -5$. Vi plugger dette inn i $abc$-formelen og får:


$$
x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4\cdot 1 \cdot (-5)}}{2\cdot 1} = \frac{4 \pm \sqrt{16 + 20}}{2} = \frac{4 \pm \sqrt{36}}{2} = \frac{4 \pm 6}{2} 
= \begin{cases}
5 \\
-1
\end{cases}
$$

Vi finner altså at løsningene av andregradslikningen er

$$
x = 5 \quad \lor \quad x = -1.
$$
:::

Nå kan du prøve deg på en oppgave for å teste forståelsen din!

::::{admonition} Underveisoppgave 1
---
class: check
---

Bruk $abc$-formelen til å finne løsningene av andregradslikningen

$$
x^2 - 3x - 4 = 0.
$$

:::{admonition} Løsning
---
class: solution, dropdown
---

Vi ser at $a = 1$, $b = -3$ og $c = -4$. Vi plugger dette inn i $abc$-formelen og får:

\begin{equation*}
\begin{split}
x & = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{-(-3) \pm \sqrt{(-3)^2 - 4\cdot 1 \cdot (-4)}}{2\cdot 1} \\
\\
& = \frac{3 \pm \sqrt{9 + 16}}{2} = \frac{3 \pm \sqrt{25}}{2} = \frac{3 \pm 5}{2}
= \begin{cases}
4 \\
-1
\end{cases}
\end{split}
\end{equation*}

Løsningene av andregradslikningen er dermed

$$
x = 4 \quad \lor \quad x = -1.
$$
:::
::::


## Utledning av $abc$-formelen
Du har vært med på å gjøre alt forarbeidet som skal til for å komme fram til $abc$-formelen. Vi tar strategien vi brukte for å løse andregradslikninger med fullstendig kvadaters metode og konjugatsetningen, men vi gjør det helt generelt slik at vi har løst alle andregradslikninger én gang for alle. 

::::{admonition} Utledning av $abc$-formelen
---
class: theory
---

Du kan prøve å utlede $abc$-formelen selv før du ser på løsningen under. Du skal få noen hint for stegene underveis under som du kan velge å se på eller ikke. Det er helt greit å ta en titt på et hint og så prøve å bruke det til å komme videre. Kanskje står du fast etter hvert, og da har du flere hint du kan se på! **Prøv!**

Først av alt, så skal vi finne den generelle løsningen av den generelle andregradslikningen

$$
ax^2 + bx + c = 0.
$$


:::{admonition} Hint 1
---
class: hints, dropdown
---
Del hele likningen med $a$.
:::

:::{admonition} Hint 2
---
class: hints, dropdown
---
Fullfør kvadratet på venstre side.
:::

:::{admonition} Hint 3
---
class: hints, dropdown
---
Skriv om uttrykket slik at det ligner på konjugatsetningen. Faktoriser deretter med konjugatsetningen.
Det kan være lurt å innføre variabler $p$ og $q$ slik at du lettere kan se sammenhengen med konjugatsetningen

$$
p^2 - q^2 = (p - q)(p + q).
$$
:::

:::{admonition} Hint 4
---
class: hints, dropdown
---
Når du har faktorisert, kan du bruke produktregelen for å finne løsningene til likningen.
:::


:::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med den generelle andregradslikningen

$$
ax^2 + bx + c = 0,
$$

og så deler hele likningen med $a$:

$$
x^2 + \frac{b}{a}x + \frac{c}{a} = 0.
$$

Deretter fullfører vi kvadratet på venstre side:

$$
x^2 + \frac{b}{a}x + \frac{c}{a} = \left(x + \frac{b}{2a}\right)^2 - \left(\frac{b}{2a}\right)^2 + \frac{c}{a} = \left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a^2}.
$$

Nå sitter vi igjen med likningen

$$
\left(x + \frac{b}{2a}\right)^2 - \frac{b^2 - 4ac}{4a^2} = 0,
$$

Vi kan få bruk konjugatsetningen ved å skrive om litt:

$$
\left(x + \frac{b}{2a}\right)^2 - \left(\sqrt{\frac{b^2 - 4ac}{4a^2}}\right)^2 = 0.
$$

Vi husker på at konjugatsetningen kan uttrykkes som $p^2 - q^2 = (p - q)(p + q)$, for to reelle tall $p$ og $q$. Vi kan derfor tolke uttrykket over som at

$$
p^2 = \left(x + \frac{b}{2a}\right)^2 \quad \text{og} \quad q^2 = \left(\sqrt{\frac{b^2 - 4ac}{4a^2}}\right)^2,
$$

slik at vi kan plugge inn i konjugatsetningen:

$$
\left(x + \frac{b}{2a} + \sqrt{\frac{b^2 - 4ac}{4a^2}}\right)\left(x + \frac{b}{2a} - \sqrt{\frac{b^2 - 4ac}{4a^2}}\right) = 0.
$$

Vi kan skrive dette litt enklere ved å regne ut kvadratroten i nevneren:

$$
\left(x + \frac{b}{2a} + \frac{\sqrt{b^2 - 4ac}}{2a}\right)\left(x + \frac{b}{2a} - \frac{\sqrt{b^2 - 4ac}}{2a}\right) = 0.
$$

Nå har vi faktorisert andregradsuttrykket fullstendig, og vi kan bruke produktregelen til å løse likningen som gir

$$
x + \frac{b}{2a} + \frac{\sqrt{b^2 - 4ac}}{2a} = 0 \quad \lor \quad x + \frac{b}{2a} - \frac{\sqrt{b^2 - 4ac}}{2a} = 0.
$$

Dette gir løsningene

$$
x = -\frac{b}{2a} + \frac{\sqrt{b^2 - 4ac}}{2a} \quad \lor \quad x = -\frac{b}{2a} - \frac{\sqrt{b^2 - 4ac}}{2a},
$$

som vi kan skrive enda enklere som

$$
x = \frac{-b + \sqrt{b^2 - 4ac}}{2a} \quad \lor \quad x = \frac{-b - \sqrt{b^2 - 4ac}}{2a}.
$$

Vi ser at det som skiller to løsningene er $\pm$, så vi kan samle løsningene til én formel:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a},
$$

som er $abc$-formelen.
:::
::::

## Antall løsninger
Vi kan bruke $abc$-formelen til å bestemme hvor mange løsninger en andregradslikning har. 

:::{admonition} Setning: Antall løsninger for en andregradslikning
---
class: theory
---

Gitt en andregradslikning på formen

$$
ax^2 + bx + c = 0,
$$

definerer vi **diskriminanten** $D$ som

$$
D = b^2 - 4ac.
$$

Antall løsninger andregradslikningen har, er bestemt av følgende betingelser:

| Antall løsninger | Betingelse |
|------------------|------------|
| To løsninger | $D > 0$ |
| Én løsning | $D = 0$ |
| Ingen løsninger | $D < 0$ | 

:::

Vi tar et eksempel.


::::{admonition} Eksempel 2: antall løsninger
---
class: example
---
Bestem $k$ slik at andregradslikningen

$$
x^2 + kx + 6 = 0
$$

har én løsning. 

:::{admonition} Løsning
---
class: solution
---
Vi ser at $a = 1$, $b = k$ og $c = 6$. Vi må kreve at diskriminanten $D = 0$ for at vi skal få én løsning. Da får vi:

$$
D = b^2 - 4ac = k^2 - 4\cdot 1 \cdot 6 = k^2 - 24 = 0 \quad \Rightarrow \quad k = \pm \sqrt{24} = \pm 2\sqrt{6}.
$$
:::
::::


