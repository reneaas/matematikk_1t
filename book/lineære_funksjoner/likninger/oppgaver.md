# Oppgaver: Lineære likninger


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
I figuren nedenfor vises grafen til $f(x) = x + 3$. 


:::{figure} ./figurer/oppgaver/oppgave_1/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk figuren til å løse likningen

$$
x + 3 = 0 
$$


::::{answer}
$$
x = -3
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk figuren til å løse likningen

$$
x + 3 = 4
$$


::::{answer}
$$
x = 1
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bruk figuren til å løse likningen

$$
x + 3 = -2
$$

::::{answer}
$$
x = -5
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Bruk figuren til å løse likningen

$$
x + 3 = 5
$$

::::{answer}
$$
x = 2
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
Løs likningene nedenfor algebraisk.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

$$
x - 2 = 0
$$

::::{answer}
$$
x = 2
$$
::::

:::::::::::::

:::::::::::::{tab-item} b

$$
x - 2 = 4
$$

::::{answer}
$$
x = 6
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

$$
-2x + 4 = 8
$$

::::{answer}
$$
x = -2
$$
::::

:::::::::::::


:::::::::::::{tab-item} d


$$
-4x + 6 = 7x
$$

::::{answer}
$$
x = -\dfrac{6}{11}
$$
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
I programmet nedenfor løses en likning. 

1. Bestem hvilken likning programmet løser.
2. Hvilke verdier er det programmet prøver ut for $x$? 
3. Bestem verdien programmet skriver ut og sjekk svaret ditt ved å kjøre programmet.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if x + 5 == 0:
        print(x)
:::


::::{answer}
1. Programmet løser likningen $x + 5 = 0$.
2. Programmet prøver ut verdiene $x \in \set{-10, -9, \ldots, 9, 10}$.
3. Programmet skriver ut verdien $-5$. 

::::


:::::::::::::

:::::::::::::{tab-item} b

I programmet nedenfor løses en likning. 

1. Bestem hvilken likning programmet løser.
2. Bestem verdien programmet skriver ut og sjekk svaret ditt ved å kjøre programmet.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if x - 2 == 8:
        print(x)
:::



:::::::::::::


:::::::::::::{tab-item} c
I programmet nedenfor løses en likning. 

1. Bestem hvilken likning programmet løser.
2. Bestem verdien programmet skriver ut og sjekk svaret ditt ved å kjøre programmet.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if -x + 8 == 3*x:
        print(x)
:::
:::::::::::::

:::::::::::::{tab-item} d

I programmet nedenfor løses en likning. 

1. Bestem hvilken likning programmet løser.
2. Bestem verdien programmet skriver ut og sjekk svaret ditt ved å kjøre programmet.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if 2*x - 4 == 3*x + 1:
        print(x)
:::

:::::::::::::

::::::::::::::

:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 4
---
level: 2
---
Grafene til to lineære funksjoner $f$ og $g$ er vist i figuren nedenfor. Funksjonsuttrykkene er gitt ved 

$$
f(x) = 2x - 3 \quad \text{og} \quad g(x) = -3x - 6.
$$


:::{figure} ./figurer/oppgaver/oppgave_4/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


Løs likningene nedenfor ved hjelp av figuren der det er mulig. Hvis ikke må du bruke en annen metode.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
f(x) = 0
$$

::::{answer}
$$
x = 2
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Løs likningen

$$
g(x) = 3
$$


::::{answer}
$$
x = -3
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningen

$$
f(x) = g(x)
$$


::::{answer}
$$
x = -1
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Løs likningen

$$
g(x) = -2
$$

::::{answer}
$$
x = -\dfrac{4}{3}
$$
::::

:::::::::::::

::::::::::::::





:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
---
level: 2
---
En lineær funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{1}{2}x + 3. 
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem i hvilket punkt grafen til $f$ skjærer $x$-aksen.

::::{answer}
$$
(-6, 0)
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Bestem i hvilket punkt grafen til $f$ skjærer linja $y = 2$. 

::::{answer}
$$
(-2, 2)
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
En annen lineær funksjon $g$ er gitt ved 

$$
g(x) = 2x.
$$

Bestem i hvilket punkt grafen til $f$ og $g$ skjærer hverandre.

::::{answer}
$$
(6, 6)
$$
::::


:::::::::::::
::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
Bruk CAS til å løse likningene nedenfor.


::::{hints} Hvordan løser jeg en likning med CAS?
Nedenfor ser du en *gif* som viser hvordan man kan løse en likning med CAS. Du trenger bare å åpne CAS-vinduet og gjøre slik det vises i *gif-en*.

:::{figure} ./videoer/cas-likninger.gif
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::


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
4x + 2 = 0
$$

:::::::::::::

:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


$$
2x - 3 = 5
$$

:::::::::::::

:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


$$
3x + 4 = 2x + 7
$$
:::::::::::::

:::::::::::::{tab-item} d

:::{cas-popup}
---
layout: sidebar
---
:::


$$
\dfrac{3}{2}x - 1 = 2x + 4
$$


> For å lage en brøk i CAS, skriver du bare telleren etterfulgt av skråstrek `/`. Deretter kan du skrive nevneren. 

:::::::::::::


::::::::::::::



:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 7
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det løser likningen

$$
-4x + 3 = -2x + 5
$$

:::{interactive-code}
for x in range(????):
    if ????:
        print(x)


:::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det løser likningen

$$
3x - 7 = 2x + 5
$$


:::{interactive-code}
for x in range(????):
    if ????:
        print(x)


:::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det løser likningen

$$
2x + 4 = 10
$$

:::{interactive-code}
for x in range(????):
    if ????:
        print(x)


:::
:::::::::::::


:::::::::::::{tab-item} d
Fyll ut programmet nedenfor slik at det løser likningen

$$
3x + 2 = 2x + 7
$$

:::{interactive-code}
for x in range(????):
    if ????:
        print(x)


:::

:::::::::::::

::::::::::::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 8
---
level: 2
---
To lineære funksjoner er gitt ved 

$$
f(x) = 3x - 2 \quad \text{og} \quad g(x) = -2x + 4.
$$


:::{cas-popup}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk CAS til å løse likningen

$$
f(x) = 0
$$

:::::::::::::


:::::::::::::{tab-item} b
Bruk CAS til å løse likningen 

$$
f(x) = 2
$$

:::::::::::::

:::::::::::::{tab-item} c
Bruk CAS til å løse likningen

$$
f(x) = g(x)
$$

:::::::::::::
::::::::::::::


:::::::::::::::










