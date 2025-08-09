# Polynomfunksjoner

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bestemme nullpunktene til polynomfunksjoner grafisk eller ved hjelp av nullpunktsformen.
* Kunne tegne fortegnslinjer for en polynomfunksjon og skissere grafen.
* Kunne bestemme $f(x)$ for polynomfunksjoner. 
:::

Vi har allerede møtt på to polynomfunksjoner – lineære funksjoner og andregradsfunksjoner. Nå skal vi gå løs på helt generelle polynomfunksjoner.

:::::{admonition} Definisjon: Polynomfunksjon
---
class: theory
---
Et **polynom** $f(x)$ er en sum av ledd på formen $a_n x^n$ der $a_n$ er koeffisienten til leddet og $n \in \{0, 1, 2, \ldots\}$ 

Den største verdien av $n$ i summen kalles for **graden** til polynomet.

En **polynomfunksjon** $f$ er en funksjon der funksjonsuttrykket $f(x)$ er et polynom. 

:::::
 

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Nedenfor ser du fire eksempler på polynomfunksjoner med ulik grad.


::::::::::::::{grid} 1 1 2 2
---
gutter: 2
---
:::::::::::::{grid-item-card}
Grad 1 (lineær funksjon)
^^^

$$
f(x) = 2x + 3
$$

:::{figure} ./figurer/eksempler/eksempel_1/grad_1.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{grid-item-card}
Grad 2 (andregradsfunksjon)
^^^

$$
f(x) = x^2 - 2x - 3
$$


:::{figure} ./figurer/eksempler/eksempel_1/grad_2.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{grid-item-card}
Grad 3 (tredjegradsfunksjon)
^^^

$$
f(x) = x^3 - 2x^2 - x + 2
$$


:::{figure} ./figurer/eksempler/eksempel_1/grad_3.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::


:::::::::::::{grid-item-card}
Grad 4 (fjerdegradsfunksjon)
^^^

$$
f(x) = x^4 + 3x^3 - x^2 - 3x + 4
$$


:::{figure} ./figurer/eksempler/eksempel_1/grad_4.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::

::::::::::::::


:::::::::::::::

## Tredjegradsfunksjoner


Tredjegradsfunksjoner vil fungere som en "lekemodell" for alle polynomfunksjoner av høyere grad. Mange av teknikkene vi anvender på tredjegradsfunksjoner vil også fungere på polynomfunksjoner av høyere grad. Vi kommer til å oppdage at tredjegradsfunksjoner ikke har et like ryddig system som vi har hatt når vi har jobbet med lineære funksjoner og andregradsfunksjoner. 

### Standardform

Akkurat som før, har vi en standardform for tredjegradsfunksjoner også:


:::{margin} Hva med betydningen til $c$?
Konstanten $c$ har ikke en opplagt betydning vi kan peke på her og nå. 
Senere vil vi ha flere verktøy til å bedre forstå hva $c$ betyr for grafen til en tredjegradsfunksjon.
:::


:::::::::::::::{summary} Tredjegradsfunksjoner (standardform)
En **tredjegradsfunksjon** $f$ er en funksjon der $f(x)$ er et tredjegradspolynom. Vi kan generelt skrive 

$$
f(x) = ax^3 + bx^2 + cx + d,
$$

der $a, b, c, d \in \mathbb{R}$ er koeffisientene til polynomet. 

* Hvis $a > 0$ har grafen til $f$ form som {poly-icon}`cubicup`. Hvis $a < 0$ har grafen til $f$ form som {poly-icon}`cubicdown`.
* Grafen til $f$ har en **anti-symmetrilinje** $x_0 = -\dfrac{b}{3a}$.
* Grafen til $f$ har et vendepunkt i $(x_0, f(x_0))$. 
* Grafen til $f$ skjærer $y$-aksen i $(0, d)$. 


:::{figure} ./figurer/teori/standardform/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


:::::::::::::::

---

Å bestemme $f(x)$ på standardform for en tredjegradsfunksjon er mye arbeid hvis det skal gjøres for hånd. Vi har 4 ukjente koeffisienter, som betyr at vi må ha 4 likninger! Vi starter heller med å se på hvordan vi gjør det med CAS: 


:::::::::::::::{example} Eksempel 2

:::{figure} ./figurer/eksempler/eksempel_2/figur.svg
---
class: no-click, adaptive-figure
width: 80%
align: right
---
:::

Til høyre vises grafen til en tredjegradsfunksjon $f$. 


I gif-en nedenfor viser vi hvordan man kan bestemme $f(x)$ fra grafen til en tredjegradsfunksjon $f$. Punktene som brukes i gif-en er markert på grafen til høyre.


:::{figure} ./videoer/cas_bestemme_funksjonsuttrykk.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::

Fra utskriften får vi at 

$$
a = 1 \and b = 0 \and c = -2 \and d = 2
$$

som gir 

$$
f(x) = x^3 - 2x + 2.
$$


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1

:::{cas-popup}
---
layout: sidebar
---
:::


Grafen til en tredjegradsfunksjon $f$ er vist i figuren nedenfor.

Bruk CAS til å bestemme $f(x)$. 


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
f(x) = -x^3 - 5x^2 - 7x - 3.
$$
::::


::::{solution}
Vi trenger 4 punkter på grafen til $f$ for å bestemme $f(x)$. Fra figuren ser vi at grafen til $f$ går gjennom disse punktene:

$$
(-3, 0) \qog (-2, -1) \qog (-1, 0) \qog (0, -3)
$$

Da kan vi bruke CAS til å bestemme koeffisientene til $f(x)$:


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at 

$$
a = -1 \and b = -5 \and c = -7 \and d = -3.
$$

Det betyr at $f(x)$ kan skrives som 

$$
f(x) = ax^3 + bx^2 + cx + d = -x^3 - 5x^2 - 7x - 3.
$$


::::


:::::::::::::::




### Nullpunktsform
Akkurat som for lineære funksjoner og andregradsfunksjoner, så kan vi skrive en tredjegradsfunksjon på nullpunktsform. Vi skal se at en tredjegradsfunksjon enten har ett, to eller tre nullpunkter. Dette gir oss tre mulige måter å faktorisere funksjonsuttrykket til en tredjegradsfunksjon på.

#### Tre nullpunkter

Når en tredjegradsfunksjon har tre nullpunkter, så gjelder følgende: 

:::{margin}
Som før, er konstanten $a$ den samme som i standardformen!
:::

:::::::::::::::{summary} Nullpunktsform med tre nullpunkter
En tredjegradsfunksjon $f$ med tre nullpunkter $x_1, x_2, x_3$ kan skrives på nullpunktsform som

$$
f(x) = a(x - x_1)(x - x_2)(x - x_3)
$$

* Hvis $a > 0$ så er formen til grafen {poly-icon}`cubicup`. Hvis $a < 0$ så er formen til grafen {poly-icon}`cubicdown`.

:::{figure} ./figurer/teori/nullpunktsform/tre_nullpunkter.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::::

---

La oss se på et eksempel der vi bestemmer $f(x)$ fra grafen til en tredjegradsfunksjon med tre nullpunkter:

:::::::::::::::{example} Eksempel 3
Grafen til en tredjegradsfunksjon er vist i figuren nedenfor.


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
Vi skriver $f(x)$ på nullpunktsform med tre nullpunkter:

$$
f(x) = a(x - x_1)(x - x_2)(x - x_3). 
$$

Vi ser fra grafen til $f$ at den skjærer $x$-aksen i $(-1, 0)$, $(1, 0)$ og $(2, 0)$. Vi setter inn $x$-verdiene i uttrykket og får: 

$$
f(x) = a(x + 1)(x - 1)(x - 2).
$$

Nå trenger vi ett punkt til på grafen til $f$ for å bestemme konstanten $a$. Vi ser at grafen skjærer $y$-aksen i $(0, 2)$. Da får vi likningen:

$$
f(0) = 2 \liff a(0 + 1)(0 - 1)(0 - 2) = 2.
$$

Vi forenkler dette til 

$$
a \cdot 1 \cdot (-1) \cdot (-2) = 2 \liff 2a = 2 \liff a = 1.
$$

Dermed er 

$$
f(x) = (x + 1)(x - 1)(x - 2).
$$

::::



:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
Grafen til en tredjegradsfunksjon $f$ er vist i figuren nedenfor. 

Bestem $f(x)$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::{answer}
$$
f(x) = -2(x + 2)(x + 1)(x - 3).
$$
::::


::::{solution}
Vi skriver $f(x)$ på nullpunktsform med tre nullpunkter:

$$
f(x) = a(x - x_1)(x - x_2)(x - x_3).
$$

Vi ser at grafen til $f$ skjærer $x$-aksen når

$$
x = -2 \qog x = -1 \qog x = 3
$$

Vi setter inn verdiene i uttrykket og får:

$$
f(x) = a(x + 2)(x + 1)(x - 3)
$$

Vi trenger ett punkt til på grafen til $f$ for å bestemme $a$. Vi ser at grafen skjærer $y$-aksen i $(0, 12)$. Da får vi likningen:

$$
f(0) = 12 \liff a(0 + 2)(0 + 1)(0 - 3) = 12
$$

Vi forenkler dette til 

$$
a \cdot 2 \cdot 1 \cdot (-3) = 12 \liff -6a = 12 \liff a = -2.
$$

Dermed er

$$
f(x) = -2(x + 2)(x + 1)(x - 3).
$$

::::


:::::::::::::::


---

#### To nullpunkter
En tredjegradsfunksjon kan også ha to nullpunkter. Da gjelder følgende:


:::::::::::::::{summary} Nullpunktsform med to nullpunkter
En tredjegradsfunksjon med to nullpunkter $x_1$ og $x_2$, der $x_1$ også er et ekstremalpunkt, kan skrives på nullpunktsform som

$$
f(x) = a(x - x_1)^2(x - x_2)
$$

* Vi kaller $x_1$ for et **dobbelt** nullpunkt.
* $a > 0$ gir grafen formen {poly-icon}`cubicup` og $a < 0$ gir grafen formen {poly-icon}`cubicdown`

:::{figure} ./figurer/teori/nullpunktsform/to_nullpunkter.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::



:::::::::::::::


---

La oss se på et eksempel der vi bestemmer $f(x)$ fra grafen til en tredjegradsfunksjon med to nullpunkter:


:::::::::::::::{example} Eksempel 4

:::{figure} ./figurer/eksempler/eksempel_4/figur.svg
---
class: no-click, adaptive-figure
width: 100%
align: right
---
:::


Til høyre vises grafen til en tredjegradsfunksjon $f$.

Bestem $f(x)$.

:::{clear}
:::

::::{solution}
---
dropdown: 0
---
Vi ser at grafen til $f$ har et dobbelt nullpunkt i $(3, 0)$ siden grafen både har et nullpunkt og et ekstremalpunkt der. Grafen til $f$ har også et nullpunkt i $(-2, 0)$ som betyr at vi kan skrive $f(x)$ på nullpunktsform som

$$
f(x) = a(x - x_1)^2(x - x_2) = a(x - 3)^2(x + 2)
$$


Vi trenger ett punkt til på grafen til $f$ for å bestemme $a$. Vi ser at grafen skjærer $y$-aksen i $(0, 18)$. Da får vi likningen:

$$
f(0) = 18 \liff a(0 - 3)^2(0 + 2) = 18.
$$

Vi forenkler dette til 

$$
a \cdot (-3)^2 \cdot 2 = 18 \liff 18a = 18 \liff a = 1.
$$

Dermed er 

$$
f(x) = (x - 3)^2(x + 2)
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/figur.svg
---
class: no-click, adaptive-figure
width: 90%
align: right
---
:::

Grafen til en tredjegradsfunksjon $f$ er vist i figuren til høyre.

Bestem $f(x)$.


:::{clear}
:::


::::{answer}
$$
f(x) = -2(x + 1)^2(x - 1)
$$
::::


::::{solution}
Fra grafen til $f$ kan vi se at $f$ har et dobbelt nullpunkt i $(-1, 0)$ siden både er et nullpunkt og et ekstremalpunkt. Vi ser også at $(1, 0)$ er et nullpunkt siden grafen skjærer $x$-aksen der. Da kan vi skrive $f(x)$ på nullpunktsform som

$$
f(x) = a(x + 1)^2(x - 1)
$$

Vi trenger ett punkt til på grafen til $f$ for å bestemme $a$. Vi ser at grafen skjærer $y$-aksen i $(0, 2)$. Da får vi likningen:

$$
f(0) = 2 \liff a(0 + 1)^2(0 - 1) = 2
$$

Vi forenkler dette til 

$$
a \cdot 1^2 \cdot (-1) = 2 \liff -a = 2 \liff a = -2.
$$
Dermed er

$$
f(x) = -2(x + 1)^2(x - 1)
$$
::::



:::::::::::::::


---

#### Ett nullpunkt
Når en tredjegradsfunksjon $f$ har ett nullpunkt, så kan vi skrive $f(x)$ som et produkt av et førstegradspolynom og et andregradspolynom:

:::::::::::::::{summary} Nullpunktsform med ett nullpunkt
En tredjegradsfunksjon med ett nullpunkt $x_1$ kan skrives på nullpunktsform som

$$
f(x) = (x - x_1)(ax^2 + bx + c)
$$

* $a > 0$ gir grafen formen {poly-icon}`cubicup` og $a < 0$ gir grafen formen {poly-icon}`cubicdown`


:::{figure} ./figurer/teori/nullpunktsform/ett_nullpunkt.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::::

---

La oss se på et eksempel der vi bestemmer $f(x)$ fra grafen til en tredjegradsfunksjon med ett nullpunkt:

:::::::::::::::{example} Eksempel 5
Grafen til en tredjegradsfunksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$. 


:::{figure} ./figurer/eksempler/eksempel_5/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{solution}
---
dropdown: 0
---
Siden grafen til $f$ bare har ett nullpunkt, så skriver vi $f(x)$ på formen 

$$
f(x) = (x - x_1)(ax^2 + bx + c). 
$$

Vi ser grafen skjærer $x$-aksen i $(1, 0)$ som betyr at $x_1 = 1$. Da kan vi skrive

$$
f(x) = (x - 1)(ax^2 + bx + c). 
$$

Nå trenger vi tre punkter på grafen til $f$ for å bestemme $a$, $b$ og $c$. Vi ser at grafen skjærer $y$-aksen i $(0, -1)$. Det betyr at 

$$
f(0) = -1 \liff (0 - 1) \cdot (a \cdot 0^2 + b \cdot 0 + c) = -1
$$

som kan forenkles til 

$$
(-1) \cdot c = -1 \liff c = 1.
$$

Altså er $f(x) = (x - 1)(ax^2 + bx + 1)$. 


Vi trenger to likninger til for å bestemme $a$ og $b$. Vi ser at grafen til $f$ går gjennom punktet $(2, 1)$ som gir likningen 

$$
f(2) = 1 \liff (2 - 1)(a \cdot 2^2 + b \cdot 2 + 1) = 1
$$

som vi forenkler til 

$$
1 \cdot (4a + 2b + 1) = 1 \liff 4a + 2b + 1 = 1
$$

$$
4a + 2b = 0 \liff 2a + b = 0 \liff b = -2a. 
$$

Vi ser også at grafen går gjennom $(3, 5)$ som gir likningen 

$$
f(3) = 5 \liff (3 - 1)(a \cdot 3^2 + b \cdot 3 + 1) = 5
$$

som vi forenkler til 

$$
2(9a + 3b + 1) = 5 \liff 18a + 6b + 2 = 5
$$

$$
18a + 6b = 3 \liff 6a + 2b = 1
$$

Så bruker vi at $b = -2a$ som gir 

$$
6a + 2\cdot (-2a) = 1 \liff 6a - 4a = 1 \liff 2a = 1
$$

som betyr at 

$$
a = \dfrac{1}{2} \and b = -2a = -2\cdot \dfrac{1}{2} = -1
$$

Dermed er 

$$
f(x) = (x - 1)\left(\dfrac{1}{2}x^2 - x + 1\right). 
$$


::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 4
En tredjegradsfunksjon $f$ er vist i figuren nedenfor. 

Bestem $f(x)$.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
f(x) = (x + 3)\left(-\dfrac{1}{4}x^2 + x - 2\right).
$$
::::


::::{solution}
Vi ser at grafen til $f$ har ett nullpunkt i $(-3, 0)$. Da kan vi skrive $f(x)$ på formen

$$
f(x) = (x + 3)(ax^2 + bx + c). 
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -6)$ som gir 

$$
f(0) = -6 \liff (0 + 3)(a \cdot 0^2 + b \cdot 0 + c) = -6
$$

som kan forenkles til

$$
3c = -6 \liff c = -2.
$$

Dermed er $f(x) = (x + 3)(ax^2 + bx - 2)$.

Vi ser at grafen går gjennom punktet $(1, -5)$ som gir likningen 

$$
f(1) = -5 \liff (1 + 3) \cdot (a \cdot 1^2 + b \cdot 1 - 2) = -5
$$

som kan forenkles til

$$
4(a + b - 2) = -5 \liff 4a + 4b - 8 = -5
$$

som gir

$$
4a + 4b = 3
$$

Vi ser også at grafen går gjennom $(2, -5)$ som gir likningen

$$
f(2) = -5 \liff (2 + 3)(a \cdot 2^2 + b \cdot 2 - 2) = -5
$$

som vi forenkler til

$$
5(4a + 2b - 2) = -5 \liff 4a + 2b - 2 = -1
$$

$$
4a + 2b = 1 
$$

Da har vi likningene 

$$
4a + 4b = 3 \and 4a + 2b = 1
$$

Vi tar den første likningen og trekker fra den andre:

$$
(4a + 4b) - (4a + 2b) = 3 - 1 \liff 2b = 2 \liff b = 1.
$$

Så bestemmer vi $a$ ved å sette inn verdien til $b$. Vi velger den første av de to likningene:

$$
4a + 4 \cdot 1 = 3 \liff 4a + 4 = 3 \liff 4a = -1 \liff a = -\dfrac{1}{4}.
$$

Dermed er 

$$
f(x) = (x + 3)\left(ax^2 + bx - 2\right) = (x + 3)\left(-\dfrac{1}{4}x^2 + x - 2\right).
$$

::::


:::::::::::::::

