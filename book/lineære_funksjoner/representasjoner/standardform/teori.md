# Standardform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en lineær funksjon på standardform og beskrive sammenhengen med den grafiske representasjonen.
* Kunne bytte fra en representasjon til en annen.
:::


## Koordinatsystemet og funksjonsverdier

Et viktig verktøy i praksis er koordinatsystemet siden vi ofte visualiserer grafen til funksjoner der. 

:::::::::::::::{theory} Koordinatsystemet

Koordinatsystemet består av to tallinjer som vi kaller for **akser**. De to aksene er:
* $x$-aksen (den horisontale aksen - også kalt *førsteaksen*).
* $y$-aksen (den vertikale aksen - også kalt *andreaksen*).

Punktet der aksene møtes kaller vi for **origo**. Origo har koordinatene $(0, 0)$.

For å finne et punkt $(x, y)$ i koordinatsystemet, går vi $x$ plasser parallelt med $x$-aksen og $y$ plasser parallelt med $y$-aksen. Da står vi på punktet $(x, y)$. 
Vi kaller $x$-verdien til punktet for $x$-koordinaten og $y$-verdien for $y$-koordinaten.

I figuren nedenfor vises en konkret eksempel med punktet $(3, 2)$.

:::{figure} ./figurer/teori/koordinatssystem.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser et koordinatsystem med punktet $(3, 2)$. For å finne punktet går vi $3$ plasser parallelt med $x$-aksen og $2$ plasser parallelt med $y$-aksen. 
:::


:::::::::::::::

---


:::::::::::::::{underveisoppgave} Underveisoppgave 1
I figuren nedenfor vises et koordinatsystem med seks punkter $A$, $B$, $C$, $D$, $E$ og $F$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Sett sammen riktig koordinater $(x, y)$ med riktig punktnavn.

:::{pair-puzzle}
$A$ : $(1, 2)$
$B$ : $(-2, 3)$
$C$ : $(3, -1)$
$D$ : $(-5, -3)$
$E$ : $(4, 4)$
$F$ : $(2, -4)$
:::


:::::::::::::::

Du har kanskje tidligere lært at en lineær funksjon $f$ er en funksjon på formen

$$
f(x) = a\cdot x + b
$$


der $a$ og $b$ er konstanter. Vi kaller $f(x)$ for **funksjonsverdien** til $f$ i $x$ der vi tenker oss at vi erstatter $x$ med et tall. Det er også vanlig å kalle $f(x)$ for **funksjonsuttrykket** til $f$ når vi ikke tenker på noe spesielt tall for $x$. 

:::::::::::::::{theory} Funksjonsverdier: Algebraisk og grafisk
For en lineær funksjon $f$ kan vi bestemme funksjonsverdier $f(x)$ på to måter:
1. **Algebraisk**: Vi setter inn verdien til $x$ i funksjonsuttrykket $f(x)$.
2. **Grafisk**: Vi leser av et punkt $(x, y)$ på grafen til $f$ der $y = f(x)$.

Nedenfor vises et eksempel på hvordan vi kan bestemme $f(3)$ for 

$$
f(x) = 2\cdot x + 1.
$$

:::::{grid}
---
gutter: 3
---
::::{grid-item-card}
---
columns: 5
---
**Algebraisk**

^^^

> Vi erstatter verdien til $x$ med $3$ i funksjonsuttrykket $f(x)$ og regner ut:

$$
f(\textcolor{red}{3}) = 2 \cdot \textcolor{red}{3} + 1 = 6 + 1 = 7.
$$
::::


::::{grid-item-card}
**Grafisk**

^^^

> Klikk på figuren for å se nærmere!

:::{clickable-figure} ./figurer/teori/funksjonsverdier.svg
---
width: 100%
---
viser at linjen $x = 3$ skjærer grafen til $f$ i punktet $(3, 7)$ som betyr at $y = 7$ når $x = 3$. Dermed er $f(3) = 7$.
:::
::::

:::::


:::::::::::::::


---


:::::::::::::::{underveisoppgave} Underveisoppgave 2
En lineær funksjon $f$ er gitt ved 

$$
f(x) = -2\cdot x + 1
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Regn ut $f(2)$ og $f(-1)$. 


::::{answer}

\begin{align*}
    f(2) &= -3 \\
    \\
    f(-1) &= 3
\end{align*}
::::

::::{solution}
\begin{align*}
    f(\textcolor{red}{2}) &= -2\cdot \textcolor{red}{2} + 1 = -4 + 1 = -3, \\
    \\
    f(\textcolor{red}{-1}) &= -2\cdot (\textcolor{red}{-1}) + 1 = 2 + 1 = 3. 
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} b
Nedenfor vises grafen til $f$. 

Bruk grafen til å bestemme $f(-2)$ og $f(1)$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{answer}
\begin{align*}
    f(-2) &= 5 \\
    \\
    f(1) &= -1
\end{align*}
::::

::::{solution}
Linjen $x = -2$ skjærer grafen til $f$ i punktet $(-2, 5)$ som betyr at $f(-2) = 5$.

Linjen $x = 1$ skjærer grafen til $f$ i punktet $(1, 1)$ som betyr at $f(1) = 1$.

::::

:::::::::::::

::::::::::::::



:::::::::::::::




## Representasjon: Standardform


En **representasjon** er en måte å beskrive noe på. En lineær funksjon kan representeres på flere måter, for eksempel med en formel som vi gjerne kaller for en **algebraisk representasjon**. En lineær funksjon kan også representeres grafisk med en **graf**. Det finnes flere representasjoner, men disse er de to viktigste. Videre kan vi skrive den algebraiske representasjonen på en måte som gir oss umiddelbar informasjon om grafen til $f$. Her skal vi fokusere på en algebraisk representasjon vi kaller for **standardform**.


:::::::::::::::{theory} Standardform: Algebraisk representasjon

En lineær funksjon $f$ kan skrives på **standardform** som

:::{figure} ./figurer/teori/algebraisk/standardform.svg
---
width: 70%
class: no-click, adaptive-figure
:::

* Verdien til $a$ er hvor mye $f(x)$ endrer seg når vi øker $x$ med $1$. Vi kaller $a$ for **stigningstallet** til grafen til $f$.
* Verdien til $b$ er $y$-koordinaten til skjæringspunktet mellom grafen til $f$ og $y$-aksen. Vi kaller ofte $b$ for **konstantleddet** til $f(x)$.


:::{figure} ./figurer/teori/grafisk_representasjon/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::::

---

:::::::::::::::{explore} Utforsk 2
Nedenfor vises grafen til en lineær funksjon $f$ i et interakivt vindu der $f(x)$ er gitt ved

$$
f(x) = ax + b.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
1. Juster verdien til $a$ og undersøk hva som skjer med grafen til $f$.
2. Hvordan kan man lese av hvilken verdi $a$ har fra grafen til $f$?

:::::::::::::


:::::::::::::{tab-item} b
1. Juster verdien til $b$ og undersøk hva som skjer med grafen til $f$.
2. Hvordan kan man lese av hvilken verdi $b$ har fra grafen til $f$?

:::::::::::::

::::::::::::::


:::{ggb} 720 600
---
material_id: ryesqwej
toolbar: "false"
---
:::


:::::::::::::::




---

:::::::::::::::{exercise} Quiz 1
:::{quiz}
Q: Hva stigningstallet til $f(x) = 2\cdot x + 1$?
+ $2$
- $2x$
- $1$
- $2\cdot x$

Q: Hva stigningstallet til $f(x) = x + 3$?
+ $1$
- $x$
- $3$
- $1\cdot x$

Q: Grafen til $f(x) = 3x - 2$ skjærer $y$-aksen i...
+ $(0, -2)$
- $(3, 0)$
- $(2, 0)$
- $(0, 3)$

Q: Konstantleddet til $f(x) = -x + 3$ er ...
+ $3$
- $-1$
- $-3$
- $1$

Q: Stigningstallet til $f(x) = -x + 3$ er ...
+ $-1$
- $-x$
- $3$
- $1$
:::
:::::::::::::::




---






:::::::::::::::{underveisoppgave} Underveisoppgave 3
Nedenfor vises grafen til en lineær funksjon $f$. 

Bestem $f(x)$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{answer}
$$
f(x) = 3\cdot x - 2
$$
::::


::::{solution}
Vi starter med $f(x)$ på standardform:

$$
f(x) = a\cdot x + b
$$

Fra grafen til $f$ kan vi lese av at den skjærer $y$-aksen i $(0, -2)$ som betyr at $b = -2$. Øker vi $x$ med $1$, så vil $y$-verdien til grafen øke med $3$ som betyr at $a = 3$. Dermed får vi 

$$
f(x) = 3 \cdot x - 2. 
$$
::::


:::::::::::::::



## Topunktsformelen

Vi vet allerede nå at vi kan bestemme stigningstallet $a$ til en lineær funksjon ved å sjekke hvor mye $f(x)$ endrer seg når vi øker $x$ med $1$. Men vi vet ikke alltid funksjonsverdier til $f$ i $x$-verdier som ligger en avstand $1$ fra hverandre. Da trenger vi en annen metode for å bestemme stigningstallet. 


:::::::::::::::{explore} Utforsk 3
Nedenfor vises grafen til en lineær funksjon $f$ i et interakivt vindu. Her kan du variere avstanden på $x$-aksen mellom to punkter $A$ og $B$ som ligger på grafen til $f$.

Anna mener at hvis en funksjon går gjennom punktene $(x_0, y_0)$ og $(x_1, y_1)$, så kan vi bruke formelen 

$$
a = \dfrac{y_1 - y_0}{x_1 - x_0}
$$

til å regne ut stigningstallet $a$ til grafen til $f$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Ut ifra figuren nedenfor, kan du si hva stigningstallet til grafen til $f$ er?

::::{answer}
$$
a = 2
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Vi lar punktet $A = (x_0, y_0)$. Hvilket punkt er dette i figuren nedenfor? 

::::{answer}
$$
A = (1, 3)
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
Endre på verdien til $x_1$ slik at $x_1 = 3$. 

Prøv ut formelen til Anna og sjekk om du får det samme svaret som i **oppgave a**. 

::::{solution}
Når $x_1 = 3$, er punktet $B = (3, 7)$. Med formelen til Anna får vi derfor

$$
a = \dfrac{7 - 3}{3 - 1} = \dfrac{4}{2} = 2.
$$

Så vi får det samme svaret som i **oppgave a**.
::::

:::::::::::::


:::::::::::::{tab-item} d
Endre på verdien til $x_1$ slik at $x_1 = -2$. 

Prøv ut formelen til Anna og sjekk om du får det samme svaret som i **oppgave a**. 

::::{solution}
Når vi endrer på $x_1$ til å bli $x_1 = -2$, så får vi punktet $B = (-2, -3)$. Med formelen til Anna får vi derfor

$$
a = \drac{-3 - 3}{-2 - 1} = \dfrac{-6}{-3} = 2.
$$

Igjen, får vi samme svar som i **oppgave a**.
::::

:::::::::::::

::::::::::::::


:::{ggb} 720 700
---
material_id: uxmuj9p5
---
:::

:::::::::::::::


---



:::::::::::::::{summary} Topunktsformelen
Hvis grafen til en lineær funksjon $f$ går gjennom punktene $(x_1, y_1)$ og $(x_2, y_2)$, så er stigningstallet $a$ gitt ved 

$$
a = \dfrac{\Delta y}{\Delta x} = \dfrac{y_2 - y_1}{x_2 - x_1}
$$


der vi har definert

$$
\Delta y = y_2 - y_1 \qog \Delta x = x_2 - x_1
$$

Vi leser symbolet $\Delta$ som "endring i" slik at $\Delta y$ betyr "endring i $y$-verdien" og $\Delta x$ betyr "endring i $x$-verdien".

:::{figure} ./figurer/teori/topunktsformelen/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::



:::::::::::::::

---



:::::::::::::::{underveisoppgave} Underveisoppgave 4
Grafen til en lineær funksjon $f$ går gjennom punktene $(-1, 2)$ og $(2, 5)$. 

Bestem stigningstallet $a$ til grafen til $f$ ved hjelp av topunktsformelen.

::::{answer}
$$
a = 1
$$
::::


::::{solution}
$$
a = \dfrac{5 - 2}{2 - (-1)} = \dfrac{3}{3} = 1
$$
::::


:::::::::::::::










