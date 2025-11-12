# Oppgaver: Andregradslikninger

:::::::::::::::{exercise} Oppgave 1
---
level: 1
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

Bruk figuren til å løse likningen

$$
f(x) = 0
$$


:::{plot}
width: 70%
function: (x + 3) * (x - 1), f
:::


::::{answer}
$$
x = -3 \or x = 1
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Grafen til en andregradsfunksjon $g$ er vist i figuren nedenfor.

Bruk figuren til å løse likningen:

$$
g(x) = 0
$$

:::{plot}
width: 70%
function: (x - 1)**2, g
:::


::::{answer}
$$
x = 1
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Grafen til en andregradsfunksjon $h$ er vist i figuren nedenfor.

Bruk figuren til å løse likningen

$$
h(x) = 0
$$

:::{plot}
width: 70%
function: -(x - 2) * (x+2), h
:::


::::{answer}
$$
x = -2 \or x = 2
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Grafen til en andregradsfunksjon $p$ er vist i figuren nedenfor.

Bruk figuren til å løse likningen:

$$
p(x) = 0
$$

:::{plot}
width: 70%
function: 0.5 * (x + 4) * (x - 3), p
ymin: -7
:::



::::{answer}

$$
x = -4 \or x = 3
$$
::::

:::::::::::::
::::::::::::::

:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 2
---
level: 1
---

::::{hints} Hvordan løser jeg en likning grafisk med Geogebra?
Nedenfor vises en gif som viser hvordan man løser likningen 

$$
x^2 - 4x + 3 = -2x + 6
$$

Vi trykker på {ggb-icon}`mode_intersect` (Skjæring mellom to objekt) etterfulgt av å trykke på hver graf for å finne skjæringspunktet.

:::{figure} ./videoer/grafisk_løsning.gif
---
class: no-click, adaptive-figure
width: 100%
---
Løsningen er $x$-koordinatene til skjæringspunktene. Altså $x = -1 \or x = 3$.
:::

::::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
---
:::



Løs likningen nedenfor grafisk. 

$$
2x^2 + 2x - 12 = 0
$$


::::{answer}
$$
x = -3 \or x = 2
$$
::::


::::{solution}
Vi skriver inn likningene for venstre og høyre side av likningen og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktene. Se figuren nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_2/a.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at skjæringspunktene er $(-3, 0)$ og $(2, 0)$. Det er $x$-koordinatene som er løsningen av likningen, som betyr at løsningen er

$$
x = -3 \or x = 2
$$

::::

:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::

Løs likningen nedenfor grafisk. 

$$
2x^2 - 4x = -2
$$


::::{answer}
$$
x = 1
$$
::::

::::{solution}
Vi skriver inn likningene for venstre og høyre side av likningen og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktene. Se figuren nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_2/b.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at det er ett skjæringspunkt mellom grafene gitt ved $(1, -2)$. Det er $x$-koordinaten som er løsningen av likningen, som betyr at løsningen er

$$
x = 1
$$

::::

:::::::::::::


:::::::::::::{tab-item} c

:::{ggb-popup}
---
layout: sidebar
---
:::

Løs likningen nedenfor grafisk.

$$
x^2 + 2x - 2 = 4x + 6
$$


::::{answer}
$$
x = -2 \or x = 4
$$
::::

::::{solution}
Vi skriver inn likningene for venstre og høyre side av likningen og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktene. Se figuren nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_2/c.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at skjæringspunktene er $(-2, -2)$ og $(4, 22)$. Det er $x$-koordinatene som er løsningene av likningen, som betyr at løsningen er

$$
x = -2 \or x = 4
$$

::::

:::::::::::::


:::::::::::::{tab-item} d

:::{ggb-popup}
---
layout: sidebar
---
:::


Løs likningen nedenfor grafisk.

$$
4x^2 - 12x + 6 = -2x^2 + 5x - 1
$$


::::{answer}
$$
x \approx 0.5 \or x \approx 2.33.
$$
::::

::::{solution}
Vi skriver inn likningene for venstre og høyre side av likningen og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktene. Se figuren nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_2/d.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at skjæringspunktene er $(0.5, 1)$ og $(2.33, -0.22)$. Det er $x$-koordinatene som er løsningene av likningen, som betyr at løsningen er

$$
x \approx 0.5 \or x \approx 2.33.
$$

> Her bruker vi $\approx$ fordi vi bare finner en tilnærmet verdi for $x$-koordinatene og ikke nødvendigvis den eksakte verdien. 

::::

:::::::::::::



::::::::::::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 3
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
x^2 - 4 = 0
$$


::::{answer}
$$
x = \pm 2
$$
::::


::::{solution}
$$
x^2 - 4 = 0 \liff x^2 = 4 \liff x = \pm\sqrt{4}
$$

som betyr at 

$$
x = \pm 2
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs likningen

$$
x^2 - 1 = 0
$$


::::{answer}
$$
x = \pm 1
$$
::::


::::{solution}
$$
x^2 - 1 = 0 \liff x^2 = 1 \liff x = \pm \sqrt{1}
$$

som betyr at 

$$
x = \pm 1
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Løs likningen

$$
x^2 - 16 = 0
$$


::::{answer}
$$
x = \pm 4
$$
::::


::::{solution}
$$
x^2 - 16 = 0 \liff x^2 = 16 \liff x = \pm \sqrt{16} 
$$

som betyr at

$$
x = \pm 4
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Løs likningen

$$
x^2 - 2 = 0
$$

::::{answer}
$$
x = \pm \sqrt{2}
$$
::::

::::{solution}
$$
x^2 - 2 = 0 \liff x^2 = 2 \liff x = \pm \sqrt{2}
$$
::::

:::::::::::::



::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
x^2 - 5x = 0.
$$


::::{answer}
$$
x = 0 \or x = 5
$$
::::


:::::::::::::

:::::::::::::{tab-item} b
Løs likningen

$$
x^2 + 2x = 0.
$$

::::{answer}
$$
x = 0 \or x = -2
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningen

$$
x^2 - 10x = 0.
$$

::::{answer}
$$
x = 0 \or x = 10
$$
::::

:::::::::::::

:::::::::::::{tab-item} d
Løs likningen

$$
-x^2 + x = 0. 
$$


::::{answer}
$$
x = 0 \or x = 1
$$
::::

:::::::::::::
::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
---
level: 1
---
Løs likningene med {popup}`$abc$-formelen. <En likning på formen $ax^2 + bx + c = 0$ har løsningen $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$>`

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
$$
x^2 - 5x + 6 = 0
$$

:::{answer}
$$
x = 2 \or x = 3
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
$$
x^2 - 3x - 4 = 0
$$

:::{answer}
$$
x = -1 \or x = 4
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
$$
x^2 - x - 6 = 0
$$

:::{answer}
$$
x = -2 \or x = 3
$$
:::
:::::::::::::

:::::::::::::{tab-item} d
$$
x^2 - 4x - 5 = 0
$$

:::{answer}
$$
x = -1 \or x = 5
$$
:::
:::::::::::::

::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---

Løs likningene ved hjelp av {popup}`$abc$-formelen. <En likning på formen $ax^2 + bx + c = 0$ har løsningen $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$>`

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
2x^2 - 5x + 2 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \dfrac{1}{2} \or x = 2
$$
:::

:::::::::::::


:::::::::::::{tab-item} b

$$
3x^2 - 7x + 2 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \left\{\dfrac{1}{3}, 2\right\}
$$
:::

:::::::::::::

:::::::::::::{tab-item} c

$$
-x^2 + 9x + 12 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \or x = 4
$$
:::

:::::::::::::


:::::::::::::{tab-item} d

$$
\dfrac{1}{2}x^2 - \dfrac{3}{4}x - \dfrac{1}{2} = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -\dfrac{1}{2} \or x = 2
$$
:::

:::::::::::::

::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
---
level: 2
---
> Noen ganger jobber vi med andregradslikninger som vi må skrive om til formen $ax^2 + bx + c = 0$ før vi kan bruke $abc$-formelen. 

Løs likningene med $abc$-formelen.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
x^2 + x + 1 = x + 5
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -2 \, \lor \, x = 2
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
$$
x^2 + x - 3 = -2x + 1
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -4 \, \lor \, x = 1
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
$$
-x^2 + x + 3 = 3x - 1
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -2 \, \lor \, x = 1
$$
::::
:::::::::::::


:::::::::::::{tab-item} d
$$
2x^2 + 5x - 1 = -2x + 3
$$

::::{answer}
$$
x = \dfrac{1}{2} \or x = -4. 
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 8
---
level: 2
---
Løs likningene med CAS.

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

$$
x^2 + 2x + 1 = 0. 
$$


:::::::::::::

:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

$$
x^2 - 3x + 2 = -x + 6
$$


:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

$$
-x^2 + 3x + 1 = 2x - 7
$$


:::::::::::::

:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

$$
-3x^2 + 4x + 6 = -3x + 10
$$


:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9
---
level: 2
---

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

Nedenfor vises et program som løser en andregradslikning. 

Bruk CAS til å bestemme verdiene programmet skriver ut og sjekk svaret ditt nedenfor.

:::{clear}
:::

:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if -x**2 + 3*x + 4 == 0:
        print(x)


:::

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

Nedenfor vises et program som løser en andregradslikning. 

Bruk CAS til å bestemme verdiene programmet skriver ut og sjekk svaret ditt nedenfor.

:::{clear}
:::

:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if x**2 - x - 12 == 0:
        print(x)


:::

:::::::::::::



:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Nedenfor vises et program som løser en andregradslikning. 

Bruk CAS til å bestemme verdiene programmet skriver ut og sjekk svaret ditt nedenfor.

:::{clear}
:::

:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if x**2 + 3*x + 11 == -3*x + 2:
        print(x)


:::

:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::

Nedenfor vises et program som løser en andregradslikning. 

Bruk CAS til å bestemme verdiene programmet skriver ut og sjekk svaret ditt nedenfor.

:::{clear}
:::

:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if x**2 + x - 20 == -x**2 + 3*x + 40:
        print(x)


:::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
---
level: 2
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet og bruk det til å løse likningen

$$
x^2 + 2x - 8 = 0.
$$


:::{interactive-code}
for x in range(????):
    if ????:
        print(x)



:::


::::{answer}
:::{code-block} python
---
linenos:
---
for x in range(-10, 11):
    if x**2 + 2*x - 8 == 0:
        print(x)

:::
::::


:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet og bruk det til å løse likningen

$$
x^2 + 2x - 3 = 0.
$$


:::{interactive-code}
for x in range(????):
    if ????:
        print(x)



:::


::::{answer}
:::{code-block} python
---
linenos:
---
for x in range(-10, 11):
    if x**2 + 2*x - 3 == 0:
        print(x)

:::
::::

:::::::::::::



:::::::::::::{tab-item} c
Fyll ut programmet og bruk det til å løse likningen

$$
x^2 - x - 3 = -3x + 12
$$


:::{interactive-code}
for x in range(????):
    if ????:
        print(x)



:::


::::{answer}
:::{code-block} python
---
linenos:
---
for x in range(-10, 11):
    if x**2 - x - 3 == -3*x + 12:
        print(x)

:::
::::

:::::::::::::



:::::::::::::{tab-item} d
Fyll ut programmet og bruk det til å løse likningen

$$
-x^2 + 6x + 7 = x^2 - 4x - 5
$$


:::{interactive-code}
for x in range(????):
    if ????:
        print(x)



:::


::::{answer}
:::{code-block} python
---
linenos:
---
for x in range(-10, 11):
    if -x**2 + 6*x + 7 == x**2 - 4*x - 5:
        print(x)

:::
::::

:::::::::::::






::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 11
---
level: 3
---
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



Bestem $a$ og $b$ slik at likningen er en identitet.

$$
x^2 + 6x - 7 = (x - a)(x - b)
$$

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



Bestem $a$, $b$ og $c$ slik at likningen er en identitet.

$$
-x^2 - 7x - 12 = a(x - b)(x - c)
$$

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::



Bestem $a$, $b$ og $c$ slik at likningen er en identitet.

$$
2x^2 - 18 = a(x - b)(x - c)
$$

:::::::::::::


:::::::::::::{tab-item} d

:::{cas-popup}
---
layout: sidebar
---
:::



Bestem $a$, $b$ og $c$ slik at likningen er en identitet.

$$
-3x^2 + 12x = a(x - b)(x - c)
$$

:::::::::::::

::::::::::::::
:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 12
---
level: 3
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem diskriminanten $D$ for likningen

$$
x^2 + 10x + 25 = 0
$$

og avgjør hvor mange løsninger likningen har.


:::::::::::::


:::::::::::::{tab-item} b
Bestem diskriminanten $D$ for likningen

$$
-x^2 + 3x + 8 = 0
$$

og avgjør hvor mange løsninger likningen har.
:::::::::::::


:::::::::::::{tab-item} c
Bestem diskriminanten $D$ for likningen

$$
2x^2 - 3x + 5 = x + 7
$$

og avgjør hvor mange løsninger likningen har.
:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 13
---
level: 3
---

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

En andregradslikning er gitt ved

$$
x^2 + kx + 6 = 0.
$$


Bestem $k$ slik at likningen har én løsning.
:::::::::::::


:::::::::::::{tab-item} b


:::{cas-popup}
---
layout: sidebar
---
:::


En andregradsfunksjon er gitt ved 

$$
f(x) = kx^2 + kx - 2 \qder k \neq 0. 
$$

Bestem $k$ slik at grafen til $f$ skjærer $x$-aksen én gang. 

:::::::::::::


:::::::::::::{tab-item} c


:::{cas-popup}
---
layout: sidebar
---
:::


En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 2kx + k, \qder k \in \real
$$


Bestem $k$ slik at $f$ har nøyaktig ett nullpunkt.

:::::::::::::



::::::::::::::



:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 14
---
level: 3
---
Grafen til en andregradsfunksjon $f$ er vist nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_14/figur.svg
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


Bestem $f(x)$. 
:::::::::::::


:::::::::::::{tab-item} b
Bruk grafen til å løse likningen

$$
f(x) = 0
$$


:::::::::::::


:::::::::::::{tab-item} c
Bruk $abc$-formelen til å løse likningen

$$
f(x) = 0
$$

:::::::::::::


:::::::::::::{tab-item} d

:::{cas-popup}
---
layout: sidebar
---
:::



Bruk CAS til å løse likningen

$$
f(x) = 14
$$

:::::::::::::


:::::::::::::{tab-item} e
Skriv et program som løser likningen

$$
f(x) = 8
$$

:::{interactive-code}
# Din kode her 



:::

:::::::::::::


::::::::::::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 15
---
level: 4
---
Vi går ut ifra en helt generell andregradslikning 

$$
ax^2 + bx + c = 0.
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Forklar at vi kan skrive om likningen til

$$
a(x - x_0)^2 + y_0 = 0
$$

og bestem $x_0$ og $y_0$ uttrykt ved $a$, $b$ og $c$.


:::::::::::::


:::::::::::::{tab-item} b
Forklar at løsningene av likningen er 

$$
x = x_0 \pm \sqrt{-\frac{y_0}{a}}.
$$

Bruk dette til å utlede $abc$-formelen. 
:::::::::::::
::::::::::::::


:::::::::::::::



