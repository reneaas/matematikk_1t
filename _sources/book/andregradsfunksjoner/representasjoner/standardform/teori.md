# Standardform


:::{goals} Læringsmål
* Kunne representere en andregradsfunksjon på standardform, og kunne lese av koeffisientene.
* Kunne avgjøre den grafiske formen til en andregradsfunksjon ut fra koeffisientene.
* Kunne bestemme koeffisientene til en andregradsfunksjon ved hjelp av lineære likningssystemer.
:::

Akkurat som når vi jobbet med lineære funksjoner, så kan vi representere en andregradsfunksjon på flere måter som gir oss ulike opplysninger om grafen til funksjonen. Her skal vi se på det vi kaller for **standardform**. Standardformen gir oss informasjon om hvilken vei grafen til funksjonen vender, hvor den skjærer $y$-aksen og hvor symmetrilinja til grafen er. Det er det neste vi skal se nærmere på.

## Algebraisk og grafisk representasjon


:::{margin} Ekstremalpunkt
Ekstremalpunkt er en fellesbetegnelse på toppunkter og bunnpunkter.
:::


:::::::::::::::{summary} Standardform

En andregradsfunksjon $f$ kan representeres algebraisk på standardform ved:

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 50%
class: no-click, adaptive-figure
---
:::

Grafen til $f$ kan da representeres slik:


:::{figure} ./figurer/teori/grafisk_representasjon/figur_3.svg
---
class: no-click, adaptive-figure
width: 75%
---
:::

Grafen til $f$ vil ha form som en **parabel** der koeffisientene har følgende betydning på grafens form:
* Hvis $a > 0$, så er grafen **konveks** {poly-icon}`smile` (grafen smiler og har et **bunnpunkt**). Hvis $a < 0$, så er grafen **konkav** {poly-icon}`frown` (surt fjes og har et **toppunkt**).
* Verdien til $a$ er gitt ved hvor mye $y$-verdien endrer seg når vi går én enhet langs $x$-aksen vekk fra ekstremalpunktet.
* Grafen har en **symmetrilinje** gitt ved $x = -\dfrac{b}{2a}$
* Grafen skjærer $y$-aksen i punktet $(0, c)$


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
width: 70%
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

Vi ser at grafen til $f$ har et bunnpunkt i $(-1, -9)$. Går vi én enhet langs $x$-aksen til høyre finner vi grafen i $(0, -8)$ som betyr at $y$-verdien har økt med $1$. Da får vi at $a = 1$.

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -8)$ som betyr at $c = -8$.

Symmetrilinja til grafen til $f$ er $x = -1$ som betyr at

$$
x = -\dfrac{b}{2a} \liff -1 = -\dfrac{b}{2 \cdot 1} \liff b = 2.
$$

Dermed er

$$
f(x) = ax^2 + bx + c = x^2 + 2x - 8
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
width: 70%
---
:::

::::{answer}
$$
f(x) = -x^2 + 4x + 1.
$$
::::

::::{solution}
Vi skriver $f(x)$ på standardform:

$$
f(x) = ax^2 + bx + c.
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, 1)$ som betyr at $c = 1$. 

Vi ser at grafen til $f$ har et toppunkt i $(2, 5)$. Går vi én enhet langs $x$-aksen mot høyre, finner vi grafen i punktet $(3, 4)$. Vi ser at $y$-verdien synker med $-1$ som betyr at $a = -1$. 

Symmetrilinja til grafen til $f$ er $x = 2$ som betyr at

$$
x = -\dfrac{b}{2a} \liff 2 = -\dfrac{b}{2 \cdot (-1)} \liff b = 4.
$$

Dermed er

$$
f(x) = -x^2 + 4x + 1.
$$

::::


:::::::::::::::


---

Det er ikke alltid vi kan lese av verdien til $a$ direkte. Det gjør at vi heller ikke enkelt kan bestemme verdien til $b$ siden de to koeffisientene er bundet sammen ved likningen for symmetrilinja. Da kan vi sette opp en likning ut ifra et punkt på grafen til $f$ og bestemme verdien til $a$ og deretter bestemme verdien til $b$.

La oss se på et eksempel:


:::::::::::::::{example} Eksempel 3
I figuren nedenfor vises grafen til en andregradsfunksjon $f$.

Bestem $f(x)$.

:::{figure} ./figurer/eksempler/eksempel_3/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::{solution}
---
dropdown: 0
---
Vi skriver $f(x)$ på standardform: 

$$
f(x) = ax^2 + bx + c
$$

Vi ser grafen til $f$ skjærer $y$-aksen i $(0, -4)$ som betyr at $c = -4$.

Grafen til $f$ har en symmetrilinje $x = 3$ som betyr at

$$
x = -\dfrac{b}{2a} \liff 3 = -\dfrac{b}{2a} \liff b = -6a.
$$

Med opplysningene vi har lest av så langt, kan vi skrive om $f(x)$ til

$$
f(x) = ax^2 - 6ax - 4.
$$

Vi ser at grafen har et toppunkt i $(3, 8)$ som vi kan bruke til å sette opp en likning for $a$:

$$
f(3) = 8 \liff a \cdot 3^2 - 6a \cdot 3 - 4 = 8
$$

som vi forenkler til

$$
9a - 18a = 12 \liff -9a = 12 \liff a = -\dfrac{12}{9} = -\dfrac{4}{3}.
$$

Så kan vi regne ut verdien til $b$:

$$
b = -6a = -6 \cdot \left(-\dfrac{4}{3}\right) = 8.
$$

Dermed er koeffisientene til $f(x)$ gitt ved

$$
a = -\dfrac{4}{3} \and b = 8 \and c = -4,
$$

så vi kan skrive ned $f(x)$ ved

$$
f(x) = -\dfrac{4}{3}x^2 + 8x - 4.
$$

::::

:::::::::::::::





### CAS
En annen måte å finne $f(x)$ på er å sette opp et likningssystem for koeffisientene $a$, $b$ og $c$ som vi løser med CAS. Dette er spesielt nyttig i situasjoner hvor vi verken kan lese av symmetrilinje eller skjæring med $y$-aksen. Det skal du se nærmere på i Utforsk 1. 

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

