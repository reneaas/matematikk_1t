:::::::::::::::{admonition} Oppgave 1
---
class: exercise
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 3x - 4.
$$

Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for gyldig strategi.
* Inntil 1 poeng for riktig svar.
:::::

:::::{admonition} Fasit
---
class: answer, dropdown
---
Grafen til $f$ skjærer $x$-aksen i $x = -1$ og $x = 4$.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $f$ skjærer $x$-aksen når $f(x) = 0$. Bruker $abc$-formelen til å finne røttene til $f(x)$:

$$
x = \dfrac{-(-3)\pm \sqrt{(-3)^2 - 4\cdot 1 \cdot (-4)}}{2\cdot 1} = \dfrac{3 \pm \sqrt{9 + 16}}{2} = \dfrac{3 \pm 5}{2}.
$$

som gir 

$$
x = 4 \or x = -1. 
$$

Dermed skjærer grafen til $f$ gjennom $x$-aksen i $x = -1$ og $x = 4$.
:::::

:::::::::::::


:::::::::::::{tab-item} b
En andregradsfunksjon $g$ er gitt ved 

$$
g(x) = -(x + 3)(x - 5).
$$

Bestem ekstremalpunktet til $g$.

:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for gyldig strategi.
* Inntil 1 poeng for riktig svar.

Det gis full uttelling om bare $x$-koordinaten er oppgitt, men det gis også full uttelling om en $y$-koordinat er oppgitt i tillegg, selv hvis feil $y$-koordinat er oppgitt. <br>
Det er forvirring rundt definisjonen av ekstremalpunkt (trolig på grunn av Geogebra), men det er formelt sett bare $x$-koordinaten til et bunn- eller toppunkt.
:::::



:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 1.
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Ekstremalpunktet $x_0$ til $g$ svarer til symmetrilinja til grafen som vi kan finne ved å ta gjennomsnittet av nullpunktene. Vi har at 

$$
g(x) = 0 \liff (x + 3)(x - 5) = 0 \liff x = -3 \or x = 5.
$$

som betyr at 

$$
x_0 = \dfrac{(-3) + 5}{2} = \dfrac{2}{2} = 1.
$$

Dermed er ekstremalpunktet til $g$ i $x = 1$.

:::::

:::::::::::::


:::::::::::::{tab-item} c
En andregradsfunksjon $h$ er gitt ved 

$$
h(x) = -(x + 2)^2 + 5 \quad \text{der} \quad D_h = \mathbb{R}.
$$

Bestem verdimengden til $h$.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for gyldig strategi.
* Inntil 1 poeng for riktig svar.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) \in \langle \gets, 5].
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Verdimengden til $h$ vil være alle verdier $h(x)$ vi kan få fra $x \in D_h = \mathbb{R}$. Siden definisjonsmengden er alle reelle tall, må vi avgjøre hvilke verdier $h(x)$ kan ta helt generelt. Siden $h$ er en andregradsfunksjon, følger det at den enten har et topp- eller bunnpunkt. Siden den ledende koeffisienten til $h$ er negativ, har den et toppunkt. Videre er $h(x)$ skrevet på ekstremalform

$$
h(x) = -(x + 2)^2 + 5,
$$

som betyr at vi kan lese av toppunktet som $(-2, 5)$. Dermed er $h(x) \leq 5$ for alle $x \in D_h$. Verdimengden til $h$ er derfor 

$$
h(x) \in \langle \gets, 5].
$$
:::::


:::::::::::::

::::::::::::::


:::::::::::::::





---





:::::::::::::::{admonition} Oppgave 2
---
class: exercise
---

Nedenfor vises en trekant $\triangle ABC$. 

:::{figure} ./figurer/del_1/oppgave_2/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å bestemme $AC$ med en gyldig strategi.
* Inntil 1 poeng for å bestemme $\tan 60 \degree$ med en gyldig strategi.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\tan 60 \degree = \sqrt{3}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
I figuren har vi at 

$$
\tan 60 \degree = \dfrac{AB}{AC} = \dfrac{2\sqrt{3}}{AC}
$$

siden $AB$ er motstående katet og $AC$ er hosliggende katet til $\angle C$. Vi kan bruke Pytagoras' setning til å bestemme $AC$: 

$$
AC^2 + (2\sqrt{3})^2 = 4^2 \liff AC^2 + 12 = 16 \liff AC^2 = 4
$$

dermed er 

$$
AC = 2. 
$$

Da følger det at

$$
\tan 60 \degree = \dfrac{2\sqrt{3}}{AB} = \dfrac{2\sqrt{3}}{2} = \sqrt{3}.
$$

:::::


:::::::::::::::





---





:::::::::::::::{admonition} Oppgave 3
---
class: exercise
---
Grafen til en andregradsfunksjon $f$ er vist i figuren nedenfor.

:::{figure} ./figurer/del_1/oppgave_3/figur.svg
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
Bestem $f(x)$.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å velge en gyldig fremgangsmåte.
* 1 poeng for å bestemme riktig $f(x)$.
:::::

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -(x + 2)(x - 4) = -x^2 + 2x + 8.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $f$ skjærer $x$-aksen i $x = - 2$ og $x = 4$ som betyr at vi kan skrive $f(x)$ på nullpunktsform:

$$
f(x) = a(x + 2)(x - 4). 
$$

Grafen til $f$ skjærer $y$-aksen i $y = 8$ som betyr at 

$$
f(0) = 8 \liff a(0 + 2)(0 - 4) = 8 \liff -8a = 8 \liff a = -1.
$$

Dermed følger det at 

$$
f(x) = -(x + 2)(x - 4) = -x^2 + 2x + 8.
$$
:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem likningen til tangenten i $(3, f(3))$. 


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å velge en gyldig fremgangsmåte.
* 1 poeng for riktig likning for tangenten.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -4x + 17.
$$
:::::


::::::{admonition} Løsning
---
class: solution, dropdown
---
:::::{tab-set}
::::{tab-item} Strategi 1: Den deriverte
For å bestemme likningen til tangenten i $(3, f(3))$ må vi finne $y$-koordinaten til punktet og stigningstallet til tangenten.

$$
y_1 = f(3)  = -(3 + 2)(3 - 4) = 5.
$$

Stigningstallet $a$ til tangenten er gitt ved den deriverte i $x = 3$:

\begin{align*}
f'(x) &= -2x + 2 \\
\\
a = f'(3) &= -2(3) + 2 = -6 + 2 = -4.
\end{align*}

Vi bruker ettpunktsformelen til å bestemme likningen 

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - 5 &= -4(x - 3) \\
    \\
    y - 5 &= -4x + 12 \\
    \\
    y &= -4x + 17.
\end{align*}

Altså er likningen til tangenten

$$
y = -4x + 17.
$$

::::

::::{tab-item} Strategi 2: Polynomdivisjon
Resten i polynomdivisjonen $f(x) : (x - 3)^2$ gir oss uttrykket for tangenten i $x = 3$.


:::{figure} ./koder/del_1/oppgave_3/polydiv.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra resten i polynomdivisjonen finner vi at likningen er 

$$
y = -4x + 17.
$$

::::
:::::
::::::

:::::::::::::

::::::::::::::

:::::::::::::::






---





:::::::::::::::{admonition} Oppgave 4
---
class: exercise
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 - 1}{x^2 - 2x + 1}
$$

Avgjør hvilken graf som tilhører $f$.

Husk å forklare hvordan du kommer fram til svaret ditt.


:::{clickable-figure} ./figurer/del_1/oppgave_4/merged_figure.svg
---
width: 100%
---
:::


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 2 poeng for å bestemme relevante egenskaper for $f$.
* Inntil 1 poeng for å bestemme riktig graf ut ifra egenskapene.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
Graf B. 
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi nullpunktsfaktoriserer teller- og nevnerpolynomet i $f(x)$:

$$
f(x) = \dfrac{x^2 - 1}{x^2 - 2x + 1} = \dfrac{(x + 1)(x - 1)}{(x - 1)^2} = \dfrac{x + 1}{x - 1}
$$

der vi brukte konjugatsetningen i tellerpolynomet og 2.kvadratsetning i nevnerpolynomet. Ettersom vi nå har forkortet bort alle felles faktorer, kan vi bestemme $f$ sine nullpunkter og asymptoter.

Fra tellerpolynomet i det fortkortede uttrykket får vi at 

$$
f(x) = 0 \liff x + 1 = 0 \liff x = -1
$$

som betyr at $f$ har et nullpunkt i $x = -1$. Fra nevnerpolynomet får vi at 

$$
x - 1 = 0  \liff x = 1
$$

som betyr at $f$ har en vertikal asymptote i $x = 1$. Siden ledende koeffisient for teller og nevnerpolynomet er $1$ og polynomeme er av samme grad, følger det at den horisontale asymptoten er $y = 1$.

Graf $B$ er den eneste grafen som samtidig har
* et nullpunkt for $x < 0$
* en vertikal asymptote når $x > 0$
* en horisontal asymptote der $y > 0$.

Dermed må graf B gære grafen til $f$. 

:::::

:::::::::::::::







---





:::::::::::::::{admonition} Oppgave 5
---
class: exercise
---
I figuren nedenfor til venstre vises en sirkel med radius $1$ og en trekant som har to hjørner på sirkelen.

I figuren nedenfor til høyre vises en trekant $\triangle ABC$. 

:::{figure} ./figurer/del_1/oppgave_5/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Bestem arealet av $\triangle ABC$.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å sette opp riktig formel for arealet med arealsetningen.
* Inntil 1 poeng for å bestemme $\sin 120 \degree$ med en gyldig strategi.
* Bruk av formlikhet for å bestemme arealet kan også gi full uttelling. 
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
Arealet er $4\sqrt{3}$.
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Først kan vi merke oss at $\triangle ABC$ er likebeint siden $\angle A = 120\degree$ og $\angle B = 30 \degree$ som betyr at 

$$
\angle C = 180 \degree - 30\degree - 120 \degree = 30 \degree.
$$

Dermed følger det at $AB = AC = 4$. Vi kan derfor bruke arealsetningen med utgangspunkt i hjørne $A$:

$$
T_{\triangle ABC} = \dfrac{1}{2}\cdot AB \cdot AC \cdot \sin \angle A = \dfrac{1}{2} \cdot 4 \cdot 4 \cdot \sin 120\degree = 8 \cdot \sin 120 \degree. 
$$

Fra figuren med enhetssirkelen, har vi fått oppgitt et punkt på enhetssirkelen som svarer til en vinkel på $120 \degree$. Da vil $y$-koordinaten til dette punktet være $\sin 120\degree$. Dermed har vi at 

$$
\sin 120 \degree = \dfrac{\sqrt{3}}{2}.
$$

Da følger det at arealet av $\triangle ABC$ er

$$
T_{\triangle ABC} = 8 \cdot \dfrac{\sqrt{3}}{2} = 4\sqrt{3}.
$$
:::::

:::::::::::::::








---




:::::::::::::::{admonition} Oppgave 6
---
class: exercise
---
En elev jobber med en funksjon $f$. Grafen til $f$ er vist i figuren nedenfor. 

:::{figure} ./figurer/del_1/oppgave_6/figur.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

Eleven har skrevet programmet nedenfor

:::{code-block} python
---
linenos:
---
def f(x):
    return x**3 + x**2 - 5 * x + 3


for x in range(0, 6):
    print(f(x))
:::

som ga utskriften

:::{code-block} console
3
0
5
24
63
128
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem én mulighet for verdiene til $a$, $b$ og $c$ slik at likningen nedenfor er en identitet.

$$
x^3 + x^2 - 5x + 3 = (x - a)(x - b)(x - c). 
$$



:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å velge en gyldig fremgangsmåte.
* 1 poeng for å bestemme én mulighet for $a$, $b$ og $c$.
:::::

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = -3 \and b = c = 1
$$
:::::



:::::{admonition} Løsning
---
class: solution, dropdown
---
Programmet til eleven bruker en for-løkke som går gjennom verdiene $x \in \{0, 1, 2, \ldots, 5\}$. Fra utskriften kan vi se at den 2. verdien som skrives ut er $0$ som betyr at $f(1) = 0$. Dermed er $x = 1$ et nullpunkt. 

Fra figuren kan vi se at det positive nullpunktet til $f$ også er et bunnpunkt som betyr at det er et dobbelt nullpunkt. Da vet vi at $(x - 1)^2 | f(x)$ og polynomdivisjonen $f(x) : (x - 1)^2$ vil gå opp: 


:::{figure} ./koder/del_1/oppgave_6/polydiv.svg
---
width: 80%
class: no-click, adaptive-figure, polydiv-figure
---
:::


Fra polynomdivisjonen følger det at 

$$
(x^3 + x^2 - 5x + 3) = (x + 3)(x - 1)^2
$$

som betyr at én mulighet for verdiene til $a$, $b$ og $c$ er

$$
a = -3 \and b = c = 1.
$$

:::::





:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten $f(x) < 0$.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å velge en gyldig fremgangsmåte.
* Inntil 1 poeng for riktig svar.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle \gets, -3 \rangle.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra grafen til $f$, kan vi se at $f(x) < 0$ når for alle verdier av $x$ som ligger på nedsiden av det negative nullpunktet til $f$. Det negative nullpunktet til $f$ er $x = -3$. 

Dermed kan vi konkludere at 

$$
f(x) < 0 \liff x \in \langle \gets, -3 \rangle.
$$
:::::

:::::::::::::

::::::::::::::



:::::::::::::::