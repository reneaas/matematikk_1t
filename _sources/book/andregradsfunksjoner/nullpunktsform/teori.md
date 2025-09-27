# Nullpunktsform

:::{goals} Læringsmål
* Kunne representere en andregradsfunksjon på nullpunktsform og bruke denne formen til å bestemme grafiske egenskaper ved funksjonen.
* Kunne veksle mellom nullpunktsform og ekstremalpunktsform.
* Kunne veksle mellom nullpunktsform og standardform.
* Kunne bestemme nullpunktsformen fra graf. 
:::

Så langt har vi sett på to representasjoner av en andregradsfunksjon. Den første var standardformen som ga oss opplysninger om grafens form og skjæringspunkt med $y$-aksen. Vi kunne også regne ut symmetrilinja til grafen. Den andre var ekstremalpunktsformen som ga oss informasjon om topp- og bunnpunkt, symmetrilinje og grafens form.

Den tredje representasjonen vi skal se på er **nullpunktsform**. Nullpunktsformen gir oss informasjon om hvor grafen skjærer $x$-aksen, som kalles for **nullpunktene** til funksjonen. På lik linje som de to andre representasjonene, gir den oss også informasjon om grafens form. Vi kan også bestemme symmetrilinja, men som med standardformen vil det være et lite regnestykke involvert. 

## Grafisk og algebraisk representasjon


:::::::::::::::{summary} Nullpunktsform
Nullpunktsformen til en andregradsfunksjon $f$ er gitt ved

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

> Merk at konstanten $a$ er den samme som i standardformen og ekstremalpunktsformen! 

* $x = x_1$ og $x = x_2$ er nullpunktene til $f$
* Hvis $a > 0$ er grafen til $f$ konveks {poly-icon}`smile`. Hvis $a < 0$ er grafen til $f$ konkav {poly-icon}`frown`.

Se figuren nedenfor.

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::::



La oss se på et eksempel der vi ser på den grafiske sammenhengen med det algebraiske uttrykket for nullpunktsformen.



:::::::::::::::{example} Eksempel 1
Nedenfor vises fire eksempler på grafene til andregradsfunksjoner og deres nullpunktsform. Legg merke til at hvis grafen bare har ett nullpunkt, så er $x_1 = x_2$. Vi kaller det for et **dobbelt** nullpunkt.



::::::::::::::{grid} 1 1 2 2
---
gutter: 2
---
:::::::::::::{grid-item-card}
$$
f(x) = (x + 2)(x - 1)
$$
^^^
:::{figure} ./figurer/eksempler/eksempel_1/A.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

:::::::::::::


:::::::::::::{grid-item-card}
$$
g(x) = -2(x - 1)(x - 1) = -2(x - 1)^2
$$

^^^
:::{figure} ./figurer/eksempler/eksempel_1/B.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

:::::::::::::


:::::::::::::{grid-item-card}
$$
h(x) = -\frac{1}{2}(x + 2)(x - 4)
$$
^^^
:::{figure} ./figurer/eksempler/eksempel_1/C.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

:::::::::::::


:::::::::::::{grid-item-card}
$$
p(x) = 3 (x + 2)(x + 2) = 3(x + 2)^2
$$
^^^
:::{figure} ./figurer/eksempler/eksempel_1/D.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

:::::::::::::
::::::::::::::
:::::::::::::::


---



## Fra graf til nullpunktsform
Nullpunktsform gir oss et nytt verktøy for å bestemme funksjonsuttrykk ut ifra grafen til funksjonen. La oss se på et eksempel:


:::::::::::::::{example} Eksempel 2
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.


Bestem $f(x)$.


:::{figure} ./figurer/eksempler/eksempel_7/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{solution}
---
dropdown: 0
---
Vi ser at grafen til $f$ skjærer $x$-aksen i punktene $(-2, 0)$ og $(3, 0)$. Dermed er nullpunktene til $f$ gitt ved $x_1 = -2$ og $x_2 = 3$. Vi kan da skrive $f(x)$ på nullpunktsform:

$$
f(x) = a(x - (-2))(x - 3) = a(x + 2)(x - 3).
$$

Vi trenger ett punkt til for å bestemme verdien til $a$. Vi ser at grafen skjærer $y$-aksen i punktet $(0, 6)$ som betyr at

$$
f(0) = 6 \liff a(0 + 2)(0 - 3) = 6.
$$

som vi forenkler til

$$
-6a = 6 \liff a = -1.
$$

Dermed er $f(x)$ gitt ved

$$
f(x) = -1(x + 2)(x - 3) = -(x + 2)(x - 3).
$$
::::

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 1
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$ på nullpunktsform.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
f(x) = \dfrac{1}{2}(x + 1)(x - 4)
$$
::::


::::{solution}
Vi ser at grafen til $f$ skjærer $x$-aksen i punktene $(-1, 0)$ og $(4, 0)$. Dermed er nullpunktene til $f$ gitt ved $x_1 = -1$ og $x_2 = 4$. Vi kan da skrive $f(x)$ på nullpunktsform:

$$
f(x) = a(x - (-1))(x - 4) = a(x + 1)(x - 4).
$$

Vi trenger ett punkt til for å bestemme verdien til $a$. Vi ser at grafen skjærer $y$-aksen i punktet $(0, -2)$ som betyr at

$$
f(0) = -2 \liff a(0 + 1)(0 - 4) = -2.
$$

Vi forenkler dette til 

$$
-4a = -2 \liff a = \frac{1}{2}.
$$

Dermed er 

$$
f(x) = \frac{1}{2}(x + 1)(x - 4).
$$
::::


:::::::::::::::


## Fra ekstremalpunktsform til nullpunktsform
Her skal vi se på hvordan vi kan skrive om fra ekstremalpunktsform til nullpunktsform. Diagrammet nedenfor oppsummerer strategien:

:::{figure} ./figurer/teori/ekstremalpunktsform_til_nullpunktsform.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


La oss se på et eksempel:


:::{margin} Konjugatsetningen
Her trenger vi konjugatsetningen

$$
\textcolor{red}{a}^2 - \textcolor{RoyalBlue}{b}^2 = (\textcolor{red}{a} + \textcolor{RoyalBlue}{b})(\textcolor{red}{a} - \textcolor{RoyalBlue}{b})
$$
:::

:::::::::::::::{example} Eksempel 3
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = (x - 1)^2 - 4
$$

Bestem nullpunktsformen til $f(x)$. 

::::{solution}
---
dropdown: 0
---
Vi kan skrive $f(x)$ som 

$$
f(x) = \textcolor{red}{(x - 1)}^2 - \textcolor{RoyalBlue}{2}^2
$$

deretter kan vi bruke konjugatsetningen for å bestemme nullpunktsformen til uttrykket:

$$
f(x) = (\textcolor{red}{x - 1} + \textcolor{RoyalBlue}{2})(\textcolor{red}{x - 1} - \textcolor{RoyalBlue}{2}) = (x + 1)(x - 3)
$$

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 2
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = (x - 2)^2 - 9
$$

Bestem nullpunktsformen til $f(x)$. Hva er nullpunktene til $f$?


::::{answer}
$$
f(x) = (x + 1)(x - 5)
$$

Nullpunktene er $x = -1$ og $x = 5$. 
::::

::::{solution}
Vi bruker konjugatsetningen:

$$
f(x) = \textcolor{red}{(x - 2)}^2 - \textcolor{RoyalBlue}{3}^2 = (\textcolor{red}{x - 2} + \textcolor{RoyalBlue}{3})(\textcolor{red}{x - 2} - \textcolor{RoyalBlue}{3}) = (x + 1)(x - 5).
$$

Fra nullpunktsformen kan vi se at nullpunktene er gitt ved 

$$
x = -1 \or x = 5
$$

::::

:::::::::::::::



Som vi har sett før, så er det ikke sånn at alle andregradsfunksjoner skjærer $x$-aksen. Det betyr derfor at ikke alle andregradsfunksjoner kan skrives på nullpunktsform. Hvis en funksjon ikke har nullpunkter, så kan den ikke skrives på nullpunktsform. La oss se på et eksempel der det ikke er mulig:

:::::::::::::::{example} Eksempel 4
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = (x - 1)^2 + 2
$$

Vis at det ikke er mulig å skrive $f(x)$ på nullpunktsform.

::::{solution}
---
dropdown: 0
---
Vi kan merke oss at begge leddene har samme fortegn som betyr at vi ikke kan faktorisere uttrykket med konjugatsetningen siden konjugatsetningen er gitt ved 

$$
a^2 - b^2 = (a + b)(a - b)
$$

Det betyr derfor at det ikke er mulig å skrive om $f(x)$ til nullpunktsform og $f$ har derfor ingen nullpunkter.
::::

:::::::::::::::

## Fra nullpunktsform til ekstremalpunktsform
For å skrive om et uttrykk fra nullpunktsform til ekstremalpunktsform, må vi først vite hvordan vi finner symmetrilinja fra nullpunktsformen. Da trenger vi følgende setning:

:::::::::::::::{summary} Sammenheng mellom nullpunkter og symmetrilinje
Symmetrilinja $x_0$ ligger midt mellom nullpunktene. Vi kan finne denne ved å regne ut gjennomsnittet av nullpunktene $x_1$ og $x_2$:

$$
x_0 = \frac{x_1 + x_2}{2}
$$

Se figuren nedenfor.

:::{figure} ./figurer/teori/symmetrilinje.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::




::::::::::::::{admonition} Bevis
---
class: theory, dropdown
---
Symmetrilinja ligger midt mellom nullpunktene. Det betyr at avstanden fra symmetrilinja til hvert nullpunkt er like. Da har vi:

$$
x_0 - x_1 = x_2 - x_0
$$

$$
2x_0 = x_1 + x_2 
$$

$$
x_0 = \dfrac{x_1 + x_2}{2}
$$
::::::::::::::



:::::::::::::::

Strategien vi skal bruke er vist i diagrammet nedenfor:

:::{figure} ./figurer/teori/nullpunktsform_til_ekstremalpunktsform.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


La oss se på et eksempel:


:::::::::::::::{example} Eksempel 5
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = (x + 1)(x - 3)
$$

Bestem $f(x)$ på ekstremalpunktsform.

::::{solution}
---
dropdown: 0
---
Vi ser fra $f(x)$ at $a = 1$. Videre ser vi at nullpunktene er $x_1 = -1$ og $x_2 = 3$. Da finner vi symmetrilinja ved å ta gjennomsnittet av de to: 

$$
x_0 = \dfrac{x_1 + x_2}{2} = \dfrac{-1 + 3}{2} = 1.
$$

Så setter vi verdien inn i $f(x)$ for å bestemme $y$-koordinaten til ekstremalpunktet:

$$
y_0 = f(1) = (1 + 1)\cdot(1 - 3) = 2 \cdot (-2) = -4.
$$

Dermed er ekstremalformen til $f(x)$ gitt ved

$$
f(x) = a(x - x_0)^2 + y_0 = (x - 1)^2 - 4.
$$

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 3
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -3(x - 2)(x + 4)
$$

Bestem ekstremalformen til $f(x)$. 


::::{answer}
$$
f(x) = -3(x + 1)^2 - 27
$$
::::


::::{solution}
Vi bestemmer symmetrilinja ved å finne gjennomsnittet av nullpunktene som er gitt ved $x_1 = 2$ og $x_2 = -4$. Da får vi:

$$
x_0 = \frac{x_1 + x_2}{2} = \frac{2 + (-4)}{2} = \frac{-2}{2} = -1
$$

Så setter vi inn denne verdien i $f(x)$ for å bestemme $y$-koordinaten til ekstremalpunktet:

$$
y_0 = f(-1) = -3\cdot(-1 - 2)\cdot(-1 + 4) = -3\cdot(-3) \cdot 3 = -27.
$$

Fra $f(x)$ ser vi at $a = -3$, så da kan vi skrive om $f(x)$ til ekstremalpunktsform:

$$
f(x) = a(x - x_0)^2 + y_0 = -3(x + 1)^2 - 27.
$$

::::



:::::::::::::::


## Fra nullpunktsform til standardform
Vi kan også gå fra nullpunktsform til standardform. For å gjøre det ganger vi ut parentesene og trekker sammen leddene. La oss se på et eksempel:




:::::::::::::::{example} Eksempel 6
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -3(x - 1)(x + 2).
$$

Bestem $f(x)$ på standardform.

::::{solution}
---
dropdown: 0
---
:::{sidebar}
Regneregel: 

$$
(a + b)(c + d) = ac + ad + bc + bd
$$
:::


Vi ganger ut parentesene og samler leddene:
\begin{align*}
f(x) &= -3(x - 1)(x + 2) \\
\\
&= -3(x^2 + 2x - x - 2) \\
\\
&= -3(x^2 + x - 2) \\
\\
&= -3x^2 - 3x + 6.
\end{align*}

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 4
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = 2(x + 3)(x - 1).
$$

Bestem $f(x)$ på standardform.

::::{answer}
$$
f(x) = 2x^2 + 4x - 6
$$
::::

::::{solution}
Vi ganger ut parentesene og samler leddene:

\begin{align*}
f(x) &= 2(x + 3)(x - 1) \\
\\
&= 2(x^2 - x + 3x - 3) \\
\\
&= 2(x^2 + 2x - 3) \\
\\
&= 2x^2 + 4x - 6.
\end{align*}
::::

:::::::::::::::


## Fra standardform til nullpunktsform
For å gå fra standardform til nullpunktsform, må vi gå veien via ekstremalpunktsform. La oss se på et eksempel:

:::::::::::::::{example} Eksempel 7
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = x^2 - 4x + 3
$$

Bestem $f(x)$ på nullpunktsform.

::::{solution}
---
dropdown: 0
---
Vi starter med å finne ekstremalpunktet så vi kan skrive $f(x)$ på ekstremalpunktsform. Vi finner symmetrilinja ved å bruke formelen for symmetrilinja:

$$
x_0 = \frac{-b}{2a} = \frac{-(-4)}{2\cdot 1} = \frac{4}{2} = 2.
$$

Så setter vi inn denne verdien i $f(x)$ for å bestemme $y$-koordinaten til ekstremalpunktet:

$$
y_0 = f(2) = (2)^2 - 4\cdot(2) + 3 = 4 - 8 + 3 = -1.
$$

Dermed kan vi skrive $f(x)$ på ekstremalpunktsform:

$$
f(x) = a(x - x_0)^2 + y_0 = (x - 2)^2 - 1.
$$

Så bruker vi konjugatsetningen for å skrive om $f(x)$ til nullpunktsform:

$$
f(x) = (x - 2)^2 - 1^2 = (x - 2 + 1)(x - 2 - 1) = (x - 1)(x - 3).
$$

::::


:::::::::::::::



## Oppsummering av representasjonsformer
Nå har vi sett hvordan vi kan veksle mellom alle representasjonene. For å få oversikt over teorien så langt, kan vi bruke diagrammet nedenfor.



:::{figure} ./koder/teori/oppsummeringsdiagram/diagram.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


