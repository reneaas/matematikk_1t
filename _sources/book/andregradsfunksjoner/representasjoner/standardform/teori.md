# Standardform


:::{goals} Læringsmål
* Kunne representere en andregradsfunksjon på standardform, og kunne lese av koeffisientene.
* Kunne avgjøre den grafiske formen til en andregradsfunksjon ut fra koeffisientene.
* Kunne bestemme koeffisientene til en andregradsfunksjon ved hjelp av lineære likningssystemer.
:::

Akkurat som når vi jobbet med lineære funksjoner, så kan vi representere en andregradsfunksjon på flere måter som gir oss ulike opplysninger om grafen til funksjonen. Her skal vi se på det vi kaller for **standardform**. Standardformen gir oss informasjon om hvilken vei grafen til funksjonen vender, hvor den skjærer $y$-aksen og hvor symmetrilinja til grafen er. Det er det neste vi skal se nærmere på.

## Algebraisk og grafisk representasjon


:::::::::::::::{summary} Standardform

En andregradsfunksjon $f$ kan representeres algebraisk på standardform ved:

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 50%
class: no-click, adaptive-figure
---
:::

Grafen til $f$ vil ha form som en **parabel** der koeffisientene har følgende betydning på grafens form:
* Hvis $a > 0$, så er grafen **konveks** {poly-icon}`smile` (grafen smiler). Hvis $a < 0$, så er grafen **konkav** {poly-icon}`frown` (surt fjes)
* Grafen har en **symmetrilinje** gitt ved $x = -\dfrac{b}{2a}$
* Grafen skjærer $y$-aksen i punktet $(0, c)$

Se figuren nedenfor.

:::{clickable-figure} ./figurer/teori/grafisk_representasjon/merged_figure.svg
---
width: 100%
---
:::


:::::::::::::::

La oss se på et eksempel der vi regner ut de ulike egenskapene og sammenlikner med grafen.


:::::::::::::::{example} Eksempel 1
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = 2x^2 - 4x + 1
$$

Bestem følgende egenskaper til grafen til $f$:
* Grafens form (konveks eller konkav)
* Symmetrilinje
* Koordinatene til topp- eller bunnpunktet
* Skjæringspunktet med $y$-aksen

Lag en skisse av grafen til $f$.


::::{solution}
---
dropdown: 0
---
Koeffisientene til $f(x)$ er $a = 2$ og $b = -4$ og $c = 1$. 

Grafens form
: Grafen er konveks {poly-icon}`smile` (den smiler) fordi $a > 0$.

Symmetrilinje
: Symmetrilinja til $f$ er gitt ved $x = \dfrac{-b}{2a} = \dfrac{-(-4)}{2 \cdot 2} = \dfrac{4}{4} = 1$.

Bunn- eller toppunkt
: Siden grafen er konveks, så har grafen et bunnpunkt. Bunnpunktets $x$-koordinat er det samme som symmetrilinja, altså $x = 1$. For å finne $y$-koordinaten til bunnpunktet, setter vi $x = 1$ inn i funksjonen:

    $$
    f(1) = 2 \cdot 1^2 - 4 \cdot 1 + 1 = 2 - 4 + 1 = -1
    $$
: Dermed er bunnpunktet $(1, -1)$.

Skjæringspunkt med $y$-aksen
: Skjæringspunktet med $y$-aksen er $(0, c) = (0, 1)$.

Nå har vi nok opplysninger til å tegne en skisse av grafen til $f$:

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 4x + 3
$$

Bestem følgende egenskaper til grafen til $f$:
* Grafens form (konveks eller konkav)
* Symmetrilinje
* Koordinatene til topp- eller bunnpunktet
* Skjæringspunktet med $y$-aksen

Lag en skisse av grafen til $f$.


::::{solution}
Koeffisientene til $f(x)$ er $a = -1$, $b = 4$ og $c = 3$.

Grafens form
: Grafen er konkav {poly-icon}`frown` (surt fjes) fordi $a < 0$.

Symmetrilinje
: Symmetrilinja til $f$ er gitt ved

    $$
    x = \dfrac{-b}{2a} = \dfrac{-4}{2 \cdot (-1)} = \dfrac{-4}{-2} = 2.
    $$

Topp- eller bunnpunkt
: Siden grafen er konkav, så har grafen et toppunkt. Toppunktets $x$-koordinat er det samme som symmetrilinja, altså $x = 2$. For å finne $y$-koordinaten til toppunktet, setter vi $x = 2$ inn i funksjonen:

    $$
    f(2) = -2^2 + 4 \cdot 2 + 3 = -4 + 8 + 3 = 7.
    $$

: Dermed er toppunktet $(2, 7)$. 

Skjæringspunkt med $y$-aksen
: Siden $c = 3$, så er skjæringspunktet med $y$-aksen $(0, 3)$.

Nå har vi nok opplysninger til å tegne en skisse av grafen til $f$:


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/figur.svg
---
class: no-click, adaptive-figure
width: 90%
---
:::

::::

:::::::::::::::


---


## Fra graf til $f(x)$

Så langt har vi sett hvordan vi kan skisse grafen til en andregradsfunksjon $f$ ut ifra standardformen til $f(x)$. Det er naturlig å lure på om vi kan gå motsatt vei også. Her skal vi se på to strategier:
1. **Bruke egenskapene til $f$**
2. **CAS**


### Bestemme $f(x)$ ut ifra egenskapene til grafen til $f$
Når vi har grafen til en andregradsfunksjon $f$, kan vi bruke følgende egenskaper til å bestemme $f(x)$:
* Skjæringspunktet med $y$-aksen bestemmer konstantleddet $c$.
* Symmetrilinja gir en sammenheng mellom $a$ og $b$. 
* Ett punkt til på grafen til å bestemme $a$ og $b$. 

La oss se på et eksempel:

:::::::::::::::{example} Eksempel 2
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$. 

:::{figure} ./figurer/eksempler/eksempel_2/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

::::{solution}
---
dropdown: 0
---
Standardformen til $f(x)$ er gitt ved 

$$
f(x) = ax^2 + bx + c.
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -8)$ som betyr at $c = -8$. 

Vi ser at symmetrilinja til $f$ er $x = -1$ som betyr at 

$$
x = -\dfrac{b}{2a} \liff -1 = -\dfrac{b}{2a} \liff b = 2a.
$$

Med opplysningene vi har funnet så langt, kan vi derfor skrive om $f(x)$ til 

$$
f(x) = ax^2 + 2ax - 8.
$$

Nå trenger vi bare å lese av ett punkt til på grafen for å sette opp en likning som vi kan løse for $a$. Vi ser at grafen til $f$ går gjennom punktet $(2, 0)$. Dermed kan vi sette opp likningen

$$
f(2) = 0 \liff a \cdot 2^2 + 2a \cdot 2 - 8 = 0 
$$

som vi forenkle til 

$$
4a + 4a - 8 = 0 \liff 8a - 8 = 0 \liff a = 1.
$$


Nå vet vi at koeffisientene til $f(x)$ er 

$$
a = 1 \and b = 2a = 2 \cdot 1 = 2 \and c = -8.
$$

Dermed er $f(x)$ gitt ved

$$
f(x) = x^2 + 2x - 8.
$$
::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 2
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/figur.svg
---
class: no-click, adaptive-figure
width: 90%
---
:::

::::{answer}
$$
f(x) = -x^2 + 6x - 5.
$$
::::

::::{solution}
Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -5)$ som betyr at $c = -5$.

Vi ser at symmetrilinja til $f$ er $x = 3$ som betyr at 

$$
x = -\dfrac{b}{2a} \liff 3 = -\dfrac{b}{2a} \liff b = -6a.
$$

Med opplysningene vi har funnet så langt, kan vi derfor skrive om $f(x)$ til

$$
f(x) = ax^2 + bx + c = ax^2 - 6ax - 5.
$$

Vi finner ett punkt til på grafen til $f$ slik at vi kan sette opp en likning som vi kan løse for $a$. Vi ser at grafen til $f$ går gjennom punktet $(1, 0)$ som betyr at 

$$
f(1) = 0 \liff a \cdot 1^2 - 6a \cdot 1 - 5 = 0
$$

som vi forenkler til

$$
-5a - 5 = 0 \liff -5a = 5 \liff a = -1.
$$

Dermed er koeffisientene til $f(x)$ gitt ved

$$
a = -1 \and b = -6a = -6 \cdot (-1) = 6 \and c = -5.
$$

Så funksjonsuttrykket til $f$ er 

$$
f(x) = -x^2 + 6x - 5.
$$

::::


:::::::::::::::



### CAS
En annen måte å finne $f(x)$ på er å sette opp et likningssystem for koeffisientene $a$, $b$ og $c$ som vi løser med CAS. Det skal du se nærmere på i Utforsk 1. 

:::::::::::::::{explore} Utforsk 1
Nedenfor vises grafen til en andregradsfunksjon $f$. Grafen går gjennom punktene $(-3, 0)$, $(2, 0)$ og $(0, 12)$.

:::{figure} ./figurer/utforsk/utforsk_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
viser grafen til $f$. Spesielt kan vi merke oss at grafen går gjennom punktene $(-3, 0)$, $(2, 0)$ og $(0, 12)$. 
:::


Nedenfor vises en gif som viser hvordan vi kan bruke CAS til å finne $f(x)$ ut ifra punktene som grafen går gjennom.

:::{figure} ./videoer/cas_standardform.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS til å bestemme koeffisientene til $f(x) = ax^2 + bx + c$ slik som det vises i gif-en over. 

Hva blir $f(x)$? 

::::{answer}
$$
f(x) = -2x^2 - 2x + 12
$$
::::
:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::

Grafen til en andregradsfunksjon $g$ går gjennom punktene $(0, 4)$, $(1, 3)$ og $(2, 0)$.

Bestem $g(x)$ med CAS.


::::{answer}
:::{figure} ./figurer/utforsk/utforsk_1/b.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

$$
g(x) = -x^2 + 4
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Grafen til en andregradsfunksjon $h$ går gjennom punktene $(0, 1)$, $(1, 0)$ og $(2, 3)$.

Bestem $h(x)$ med CAS.

::::{answer}
:::{figure} ./figurer/utforsk/utforsk_1/c.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

$$
h(x) = 2x^2 - 3x + 1
$$
::::
:::::::::::::


::::::::::::::

:::::::::::::::

