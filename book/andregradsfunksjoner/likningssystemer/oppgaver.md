# Oppgaver: Ikke-lineære likningssystemer


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 - 2x + y &= 4\\
    \\
    -x + y &= 2
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/a.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
x = -1 \and y = 1 \or x = 2 \and y = 4.
$$
::::

::::{solution}
Vi ser fra figuren at grafene til likningene skjærer hverandre i punktene $(-1, 1)$ og $(2, 4)$. Løsningen av likningssystemet er derfor 

$$
x = -1 \and y = 1 \or x = 2 \and y = 4.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b

Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 + x - y &= 2\\
    \\
    -2x + y &= 4
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/b.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
x = -2 \and y = 0 \or x = 3 \and y = 10.
$$
::::

::::{solution}
Grafene til likningene skjærer hverandre i punktene $(-2, 0)$ og $(3, 10)$. Løsniingen av likningssystemet er derfor

$$
x = -2 \and y = 0 \or x = 3 \and y = 10.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 + 2x - y - 1 &= 0\\
    \\
    3x - y &= -1
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/c.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
x = -1 \and y = -2 \or x = 2 \and y = 7.
$$
::::


::::{solution}
Grafene skjærer hverandre i punktene $(-1, -2)$ og $(2, 7)$. Løsningen av likningssystemet er derfor

$$
x = -1 \and y = -2 \or x = 2 \and y = 7.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d

Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 - 2x + y &= -1\\
    \\
    2x + y &= 3
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/d.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
x = 2 \and y = -1
$$
::::

::::{solution}
Grafene skjærer hverandre i ett punkt: $(2, -1)$. Løsningen av likningssystemet er derfor

$$
x = 2 \and y = -1
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
Bruk Geogebra til å løse likningssystemene grafisk. 


::::{hints} Hvordan løser jeg likningssystemer grafisk med Geogebra? 
Et likningssystem er gitt ved 

\begin{align*}
    2x - y &= 3 \\
    x^2 - 2y - y &= 3
\end{align*}

Nedenfor ser du en gif som viser hvordan man løser likningen med grafvinduet i Geogebra. Vi trykker på {ggb-icon}`mode_intersect` (Skjæring mellom to objekt) etterfulgt av å trykke på hver graf for å finne skjæringspunktet.

:::{figure} ./videoer/grafisk_løsning.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::

Skjæringspunktene mellom de to grafene er $(4, 5)$ og $(0, -3)$ som betyr at løsningen av likningssystemet er

$$
x = 4 \and y = 5 \or x = 0 \and y = -3
$$

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

\begin{align*}
-x^2 + x + y &= 1 \\
\\
3x + y &= 4
\end{align*}


::::{answer}
$$
x = -3 \and y = 13 \or x = 1 \and y = 1
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/a.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(-3, 13)$ og $(1, 1)$. Da er løsningen av likningssystemet gitt ved 

$$
x = -3 \and y = 13 \or x = 1 \and y = 1
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
:::{ggb-popup}
---
layout: sidebar
---
:::

\begin{align*}
x^2 - x - y &= 3 \\
\\
x - y &= -5
\end{align*}

::::{answer}
$$
x = -2 \and y = 3 \or x = 4 \and y = 9
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/b.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(-2, 3)$ og $(4, 9)$. Da er løsningen av likningssystemet gitt ved

$$
x = -2 \and y = 3 \or x = 4 \and y = 9
$$

::::

:::::::::::::



:::::::::::::{tab-item} c
:::{ggb-popup}
---
layout: sidebar
---
:::

\begin{align*}
x^2 + 2x - y &= 0 \\
\\
-2x + y &= 1
\end{align*}


::::{answer}
$$
x = -1 \and y = -1 \or x = 1 \and y = 3
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/c.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(-1, -1)$ og $(1, 3)$. Da er løsningen av likningssystemet gitt ved

$$
x = -1 \and y = -1 \or x = 1 \and y = 3
$$
::::


:::::::::::::


:::::::::::::{tab-item} d

:::{ggb-popup}
---
layout: sidebar
---
:::


\begin{align*}
-x^2 + x - y &= -1 \\
\\
2x + y &= 1
\end{align*}


::::{answer}
$$
x = 0 \and y = 1 \or x = 3 \and y = -5
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/d.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(0, 1)$ og $(4, -7)$. Da er løsningen av likningssystemet gitt ved

$$
x = 0 \and y = 1 \or x = 4 \and y = -7
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
Løs likningssystemene algebraisk. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

\begin{align*}
    x^2 - 2x + y &= 4\\
    \\
    -x + y &= 2
\end{align*}

::::{answer}
$$
x = -1 \and y = 1 \or x = 2 \and y = 4.
$$
::::


::::{solution}
Vi løser likning 2 for $y$:

$$
-x + y = 2 \liff y = x + 2
$$

Deretter setter vi inn uttrykket for $y$ i likning 1:

$$
x^2 - 2x + (x + 2) = 4
$$

$$
x^2 - x - 2 = 0
$$

Nå kan vi bruke $abc$-formelen for å finne verdiene for $x$: 

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{1 \pm \sqrt{1 + 8}}{2} = \frac{1 \pm 3}{2}
$$

som gir løsningene 

$$
x = -1 \or x = 2.
$$

Hver verdi for $x$ gir oss en verdi for $y$. Vi bruker at $y = x + 2$ og setter inn verdiene for $x$. Når $x = -1$, så får vi

$$
y = -1 + 2 = 1
$$

Når $x = 2$, så får vi

$$
y = 2 + 2 = 4.
$$

Dermed er løsningen av likningssystemet

$$
x = -1 \and y = 1 \or x = 2 \and y = 4.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b

\begin{align*}
    x^2 + x - y &= 2\\
    \\
    -2x + y &= 4
\end{align*}


::::{answer}
$$
x = -2 \and y = 0 \or x = 3 \and y = 10.
$$
::::


::::{solution}
Vi løser likning 2 for $y$:

$$
-2x + y = 4 \liff y = 2x + 4
$$

Deretter setter vi inn uttrykket for $y$ i likning 1:

$$
x^2 + x - (2x + 4) = 2
$$

Så forenkler vi likningen så mye som mulig:

$$
x^2 - x - 6 = 0
$$

Nå kan vi bruke $abc$-formelen for å finne verdiene for $x$:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{1 \pm \sqrt{1 + 24}}{2} = \frac{1 \pm 5}{2}
$$

som gir løsningene

$$
x = -2 \or x = 3.
$$

Hver verdi for $x$ gir oss en verdi for $y$. Vi bruker at $y = 2x + 4$ og setter inn verdiene for $x$. Når $x = -2$, så får vi

$$
y = 2 \cdot (-2) + 4 = -4 + 4 = 0
$$

Når $x = 3$, så får vi

$$
y = 2 \cdot 3 + 4 = 6 + 4 = 10.
$$

Dermed er løsningen av likningssystemet

$$
x = -2 \and y = 0 \or x = 3 \and y = 10.
$$
::::


:::::::::::::


:::::::::::::{tab-item} c

\begin{align*}
    3x - y &= -1 \\
    \\
    x^2 + 2x - y &= 1\\
\end{align*}


::::{answer}
$$
x = -1 \and y = -2 \or x = 2 \and y = 7.
$$
::::


::::{solution}
Vi løser likning 1 for $y$:

$$
3x - y = -1 \liff y = 3x + 1
$$

Deretter setter vi inn uttrykket for $y$ i likning 2:

$$
x^2 + 2x - (3x + 1) = 1
$$

Så forenkler vi likningen så mye som mulig:

$$
x^2 - x - 2 = 0
$$

Nå kan vi bruke $abc$-formelen for å finne verdiene for $x$:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{1 \pm \sqrt{1 + 8}}{2} = \frac{1 \pm 3}{2}
$$

som gir løsningene

$$
x = -1 \or x = 2.
$$

Hver verdi for $x$ gir oss en verdi for $y$. Vi bruker at $y = 3x + 1$ og setter inn verdiene for $x$. Når $x = -1$, så får vi

$$
y = 3 \cdot (-1) + 1 = -3 + 1 = -2
$$

Når $x = 2$, så får vi

$$
y = 3 \cdot 2 + 1 = 6 + 1 = 7.
$$

Dermed er løsningen av likningssystemet

$$
x = -1 \and y = -2 \or x = 2 \and y = 7.
$$
::::


:::::::::::::


:::::::::::::{tab-item} d

\begin{align*}
    x^2 - 2x + y &= -1\\
    \\
    2x + y &= 3
\end{align*}


::::{answer}
$$
x = 2 \and y = -1.
$$
::::


::::{solution}
Vi løser likning 2 for $y$:

$$
2x + y = 3 \liff y = -2x + 3
$$

Deretter setter vi inn uttrykket for $y$ i likning 1:

$$
x^2 - 2x + (-2x + 3) = -1
$$

Så forenkler vi likningen så mye som mulig:

$$
x^2 - 4x + 4 = 0
$$

Vi kan faktorisere likningen med 2.kvadratsetning: 

$$
(x - 2)^2 = 0
$$

Det betyr at løsningen for $x$ er

$$
x = 2.
$$

Den tilhørende $y$-verdien finner vi ved å bruke at $y = -2x + 3$:

$$
y = -2 \cdot 2 + 3 = -4 + 3 = -1.
$$

Dermed er løsningen av likningssystemet

$$
x = 2 \and y = -1.
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
Bruk CAS til å løse likningssystemene. 

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

\begin{align*}
-x^2 + 3x + 4y &= 0 \\
\\
-x + 2y &= -2
\end{align*}


::::{answer}
$$
x = 4 \and y = 1 \or x = 1 \and y = -\dfrac{1}{2}
$$
::::

::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/a.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er

$$
x = 4 \and y = 1 \or x = 1 \and y = -\dfrac{1}{2}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::

\begin{align*}
2x^2 - 3x - y &= 2 \\
\\
2x - y &= -5
\end{align*}


::::{answer}
$$
x = -1 \and y = 3 \or x = \dfrac{7}{2} \and y = 12.
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/b.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er 

$$
x = -1 \and y = 3 \or x = \dfrac{7}{2} \and y = 12.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


\begin{align*}
-x^2 + y &= 2 \\
\\
x + 4y &= 8
\end{align*}


::::{answer}
$$
x = 0 \and y = 2 \or x = -\dfrac{1}{4} \and y = \dfrac{33}{16}
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/c.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er

$$
x = 0 \and y = 2 \or x = -\dfrac{1}{4} \and y = \dfrac{33}{16}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::


\begin{align*}
2x - y &= 3 \\
\\
x^2 - 3 &= y + 2x
\end{align*}


::::{answer}
$$
x = 0 \and y = -3 \or x = 4 \and y = 5.
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/d.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er 

$$
x = 0 \and y = -3 \or x = 4 \and y = 5.
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---

:::{margin} Tips: Oppgave 5
Det kan være lurt å løse likningene med hensyn på $y$ slik at du kan gjenkjenne likningene som funksjonsuttrykk. 
:::


:::::::::::::::{exercise} Oppgave 5
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør hvilken av figurene nedenfor du kan bruke til å løse likningssystemet 


\begin{align*}
x^2 - 2x + y &= -2 \\
x - y &= 0
\end{align*}



Løs likningssystemet ved hjelp av riktig figur. 

:::{figure} ./figurer/oppgaver/oppgave_5/a/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
Figur C. 
::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør hvilken av figurene nedenfor du kan bruke til å løse likningssystemet 


\begin{align*}
x^2 - 6x - y &= -5\\
x - y &= 5
\end{align*}



Løs likningssystemet ved hjelp av riktig figur. 

:::{figure} ./figurer/oppgaver/oppgave_5/b/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
Figur A. 
::::


:::::::::::::



:::::::::::::{tab-item} c
Avgjør hvilken av figurene nedenfor du kan bruke til å løse likningssystemet 


\begin{align*}
x^2 + 2x + y &= 1 \\
x^2 - 4x - y &= 3
\end{align*}



Løs likningssystemet ved hjelp av riktig figur. 

:::{figure} ./figurer/oppgaver/oppgave_5/c/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
Figur D.
::::


:::::::::::::




::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et likningssystem du kan bruke figuren nedenfor til å løse

:::{figure} ./figurer/oppgaver/oppgave_6/a.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::


:::::::::::::{tab-item} b
Lag et likningssystem du kan bruke figuren nedenfor til å løse

:::{figure} ./figurer/oppgaver/oppgave_6/b.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::



:::::::::::::{tab-item} c
Lag et likningssystem du kan bruke figuren nedenfor til å løse

:::{figure} ./figurer/oppgaver/oppgave_6/c.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7
---
level: 2
---
Bruk CAS til å forutsi hva som skrives ut av programmene nedenfor.


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

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 == 4*y and x - 2*y == -4:
            print((x, y))


:::

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 + 2*x - y == 3 and 6*x - y == 7:
            print((x, y))


:::

:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 + y == 5 and 3*x + y == 7:
            print((x, y))


:::

:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 - 3*y == 16 and x - y == 2:
            print((x, y))


:::

:::::::::::::



::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
---
level: 2
---
Anna har skrevet et program for å løse et likningssystem. Programmet er vist nedenfor.

:::{code-block} python
---
linenos:
---
for x in range(-100, 101):
    for y in range(-100, 101):
        if x**2 + y**2 == 25 and x + y == 5:
            print((x, y))


:::


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

Løs likningssystemet grafisk. 

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

Løs likningssystemet med CAS. 

:::::::::::::


:::::::::::::{tab-item} c
Løs likningssystemet algebraisk. 


:::::::::::::


::::::::::::::
:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 9
---
level: 3
---
:::{cas-popup}
---
layout: sidebar
---
:::


Et likningssystem er gitt ved 

\begin{align*}
-x^2 + y &= k
\\
4x + y &= 5
\end{align*}




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a


Bestem $k$ slik at likningssystemet har nøyaktig én løsning.


::::{answer}
$$
k = 9
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
For hvilke verdier av $k$ har likningssystemet to løsninger? 


::::{answer}
$$
k > 9
$$
::::


:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
---
level: 3
---

:::{cas-popup}
---
layout: sidebar
---
:::


Et likningssystem er gitt ved 


\begin{align*}
x^2 + kx + y &= 0
\\
x + y &= 2
\end{align*}


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $k$ slik at likningssystemet har nøyaktig én løsning.


::::{answer}
$$
k = -1 \or k = 3.
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
For hvilke verdier av $k$ vil likningsystemet ikke ha noen løsning?


::::{answer}
$$
k \in \langle \gets, -1 \rangle \cup \langle 3, \gets \rangle
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::{margin} Tips: Oppgave 11
Det kan være lurt å tenke deg at du roterer grafen 90 grader og deretter speiler den. Da kan du bruke teorien du har lært om andregradsfunksjoner. Deretter må du bytte om på variablene $x$ og $y$ slik at du får riktig symmetrilinje og form langs $x$-aksen. 
:::


:::::::::::::::{exercise} Oppgave 11
---
level: 3
---
Grafen til en andregradsfunksjon kalles for en **parabel**. Men en parabel må ikke være en funksjon. For at grafen skal være en funksjon, så kan det bare finnes én $y$-verdi for hver $x$-verdi. Hvis parabelen derimot ligger langs $x$-aksen, så har den flere $y$-verdier for hver $x$-verdi. Da er ikke grafen en funksjon, men en **kurve**.

I figuren nedenfor vises en slik **parabel**. 


:::{figure} ./figurer/oppgaver/oppgave_11/a.svg
---
class: no-click, adaptive-figure
width: 90%
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem likningen til parabelen på standardform:

$$
x = ay^2 + by + c
$$


:::::::::::::

:::::::::::::{tab-item} b
Bestem likningen til parabelen på ekstremalpunktssform:

$$
x = a(y - y_0)^2 + x_0
$$

:::::::::::::


:::::::::::::{tab-item} c
Bestem likningen til parabelen på nullpunktsform:

$$
x = a(y - y_1)(y - y_2)
$$

:::::::::::::

::::::::::::::

:::::::::::::::



