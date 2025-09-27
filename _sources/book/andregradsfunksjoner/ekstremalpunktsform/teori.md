# Ekstremalpunktsform

:::{goals} Læringsmål
* Kunne bestemme $f(x)$ på ekstremalpunktsform og kunne bruke denne til å bestemme grafiske egenskaper ved funksjonen.
* Kunne veksle mellom ekstremalpunktsform og standardform.
* Kunne bestemme ekstremalpunktsformen fra graf.
:::


Standardformen til en andregradsfunksjon ga oss informasjon om funksjonens form, hvor den den skjærer $y$-aksen. Vi kunne også bestemme symmetrilinja til grafen ved litt regning. 


Nå skal vi se på en annen representasjon som vi kaller for **ekstremalpunktsform**. **Ekstremalpunkt** er en fellesbetegnelse på toppunkt og bunnpunkt. Denne representasjonen gir oss informasjon om funksjonens topp- eller bunnpunkt, symmetrilinje og grafens form. 



## Grafisk og algebraisk representasjon


:::{margin}
Når vi så på standardformen $f(x) = ax^2 + bx + c$, så vi at vi kunne bestemme grafens symmetrilinje ved å bruke formelen

$$
x_0 = -\frac{b}{2a}
$$
:::

:::::::::::::::{summary} Ekstremalpunktsform
Ekstremalpunktsformen til en andregradsfunksjon $f$ er gitt ved

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 65%
class: no-click, adaptive-figure
---
:::

> Merk at konstanten $a$ er den samme som i standardformen! 

* Hvis $a > 0$ er grafen til $f$ konveks {poly-icon}`smile` og har et bunnpunkt.
* Hvis $a < 0$ er grafen til $f$ konkav {poly-icon}`frown` og har et toppunkt.
* Linja $x = x_0$ er symmetrilinja til $f$. Grafen er speilet rundt denne linja!


:::{plot}
width: 80%
function: (x - 2)**2 + 1, f
xmin: -2
xmax: 6
ymin: -2
ymax: 6
ticks: off
annotate: (2.5, -1), (2, 1), "Ekstremalpunkt $(x_0, y_0)$", -0.3
point: (2, 1)
vline: 2, -10, 10
annotate: (-1.5, -1), (2, 3), "Symmetrilinje $x = x_0$", -0.3
:::


:::::::::::::::


La oss se på et eksempel der vi ser på den grafiske sammenhengen med det algebraiske uttrykket for ekstremalpunktsformen.

:::::::::::::::{example} Eksempel 1
Nedenfor vises fire eksempler på grafene til andregradsfunksjoner og deres ekstremalpunktsform.


::::::::::::::{grid} 1 1 2 2
---
gutter: 2
---
:::::::::::::{grid-item-card}
$$
f(x) = (x - 1)^2 - 4
$$
^^^

:::{plot}
width: 100%
function: (x - 1)**2 - 4, f
point: (1, -4)
text: 1, -4, "$(1, -4)$", bottom-right
vline: 1, -10, 10
fontsize: 26
:::


:::::::::::::


:::::::::::::{grid-item-card}
$$
g(x) = -2(x + 3)^2 + 1
$$

^^^

:::{plot}
width: 100%
function: -2*(x + 3)**2 + 1, g
point: (-3, 1)
text: -3, 1, "$(-3, 1)$", top-left
vline: -3, -10, 10
fontsize: 26
:::


:::::::::::::


:::::::::::::{grid-item-card}
$$
h(x) = -\frac{1}{2}(x - 2)^2 - 1
$$
^^^

:::{plot}
width: 100%
function: -0.5 * (x - 2)**2 - 3, h
point: (2, -3)
text: 2, -3, "$(2, -3)$", top-right
vline: 2, -10, 10
fontsize: 26
xmin: -2
xmax: 8
ymin: -8
ymax: 4
:::

:::::::::::::


:::::::::::::{grid-item-card}
$$
p(x) = (x + 1)^2 + 2
$$
^^^


:::{plot}
width: 100%
function: (x + 1)**2 + 2, p
point: (-1, 2)
text: -1, 2, "$(-1, 2)$", bottom-left
vline: -1, -10, 10
fontsize: 26
:::

:::::::::::::
::::::::::::::





:::::::::::::::


---


:::::::::::::::{explore} Utforsk 1
Nedenfor vises et interaktivt vindu der en andregradsfunksjon $f$ er skrevet på ekstremalpunktsform 

$$
f(x) = a (x - x_0)^2 + y_0
$$

Du kan variere verdiene til $a$, $x_0$ og $y_0$ for å se hvordan grafen endrer seg. 

Endre på verdiene og lag figurene som er vist i Eksempel 1.

:::{ggb} 720 600
---
material_id: wapc5yua
---
:::

:::::::::::::::



---



## Fra graf til $f(x)$ på ekstremalpunktsform


Når vi har en graf, kan vi bestemme ekstremalpunktsformen når vi kjenner til ekstremalpunktet og ett punkt til på grafen. 
La oss se på et eksempel:


:::::::::::::::{example} Eksempel 2
Grafen til en andregradsfunksjon $f$ er vist nedenfor.

Bestem $f(x)$ på ekstremalpunktsform.



:::{plot}
width: 70%
function: 2*(x - 1)**2 - 8, f
ymin: -10
:::




::::{solution}
---
dropdown: 0 
---
Vi ser fra grafen at ekstremalpunktet er $(1, -8)$. Det betyr at vi kan skrive $f(x)$ på ekstremalpunktsform som

$$
f(x) = a(x - 1)^2 - 8.
$$


Flytter vi oss én enhet til høyre langs $x$-aksen fra ekstremalpunktet, ser vi at funksjonsverdien øker med $2$. Det betyr at $a = 2$. Dermed er

$$
f(x) = 2(x - 1)^2 - 8.
$$

::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
Grafen til en andregradsfunksjon $f$ er vist nedenfor.

Bestem $f(x)$ på ekstremalpunktsform.


:::{plot}
width: 70%
function: -(x + 1)**2 + 4, f
:::



::::{answer}
$$
f(x) = -(x + 1)^2 + 4.
$$
::::


::::{solution}
Vi ser at grafen til $f$ har et ekstremalpunkt i $(-1, 4)$ som betyr at vi kan skrive $f(x)$ på ekstremalpunktsform som

$$
f(x) = a(x - (-1))^2 + 4 = a(x + 1)^2 + 4.
$$

Flytter vi oss én enhet til høyre langs $x$-aksen fra ekstremalpunktet, ser vi at funksjonsverdien synker med $1$. Det betyr at $a = -1$. Dermed er

$$
f(x) = -(x + 1)^2 + 4.
$$

::::

:::::::::::::::




## Fra standardform til ekstremalpunktsform
Nå skal vi se hvordan vi kan skrive om en andregradsfunksjon fra standardform til ekstremalpunktsform. Diagrammet oppsummerer strategien: 

:::{figure} ./figurer/teori/diagram.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

La oss se på et eksempel:

:::::::::::::::{example} Eksempel 3
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = x^2 - 4x + 3.
$$

Bestem $f(x)$ på ekstremalpunktsform.


::::{solution}
---
dropdown: 0
---
Ekstremalpunktsformen til $f(x)$ er gitt ved

$$
f(x) = a(x - x_0)^2 + y_0,
$$

der $y_0 = f(x_0)$ og $x_0$ er symmetrilinja til grafen. Vi kan bestemme $x_0$ med formelen: 

$$
x_0 = -\frac{b}{2a} \, ,
$$

og siden $a = 1$ og $b = -4$, så får vi:

$$
x_0 = -\frac{-4}{2 \cdot 1} = 2.
$$

Deretter bestemmer vi $y_0$ ved å sette $x = 2$ i funksjonsuttrykket:

$$
y_0 = f(2) = 2^2 - 4 \cdot 2 + 3 = 4 - 8 + 3 = -1.
$$

Dermed er ekstremalpunktsformen til $f(x)$ gitt ved

$$
f(x) = (x - 2)^2 - 1.
$$

::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
En andregradsfunksjon $f$ er gitt ved


$$
f(x) = 2x^2 - 8x + 6.
$$

Bestem $f(x)$ på ekstremalpunktsform.


::::{answer}
$$
f(x) = 2(x - 2)^2 - 2.
$$
::::

::::{solution}
Koeffisientene til $f(x)$ er

$$
a = 2 \and b = -8 \and c = 6.
$$

Symmetrilinja er derfor

$$
x_0 = -\dfrac{b}{2a} = -\dfrac{-8}{2 \cdot 2} = 2.
$$

Deretter bestemmer vi $y_0$ ved å sette $x = 2$ i funksjonsuttrykket:

$$
y_0 = f(2) = 2 \cdot 2^2 - 8 \cdot 2 + 6 = 8 - 16 + 6 = -2.
$$

Dermed er ekstremalpunktsformen til $f(x)$ gitt ved

$$
f(x) = a(x - x_0)^2 + y_0 = 2(x - 2)^2 - 2.
$$
::::

:::::::::::::::


## Fra ekstremalpunktsform til standardform
Vi kan også veksle fra ekstremalpunktsform til standardform. Dette gjør vi ved å gange ut parentesen og samle leddene:

:::{margin} Husk: Kvadratsetninger
$$
(a + b)^2 = a^2 + 2ab + b^2
$$

$$
(a - b)^2 = a^2 - 2ab + b^2
$$
:::

:::::::::::::::{example} Eksempel 4
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -3(x - 1)^2 + 2
$$

Bestem $f(x)$ på standardform.

::::{solution}
---
dropdown: 0
---
Vi ganger ut parentesen før vi samler leddene:

\begin{align*}
f(x) &= -3(x - 1)^2 + 2 \\
\\
&= -3(x^2 - 2x + 1) + 2 \\
\\
&= -3x^2 + 6x - 3 + 2 \\
\\
&= -3x^2 + 6x - 1.
\end{align*}

::::

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 3
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = 2(x + 3)^2 - 5.
$$

Bestem $f(x)$ på standardform.

::::{answer}
$$
f(x) = 2x^2 + 12x + 13.
$$
::::

::::{solution}
Vi ganger ut parentesen og samler leddene:

\begin{align*}
f(x) &= 2(x + 3)^2 - 5 \\
\\
&= 2(x^2 + 6x + 9) - 5 \\
\\
&= 2x^2 + 12x + 18 - 5 \\
\\
&= 2x^2 + 12x + 13.
\end{align*}

::::



:::::::::::::::


## Sammenlikning av standardform og ekstremalpunktsform

Det kan være nyttig å oppsummere forskjellen mellom standardform og ekstremalpunktsform for å belyse hva slags opplysninger de to representasjonene gir oss: 


:::::::::::::::{grid} 1 1 2 2
---
gutter: 2
---

::::::::::::::{grid-item-card} 
Standardform

^^^

:::{figure} ../standardform/figurer/teori/algebraisk_uttrykk.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

---

:::{figure} ../standardform/figurer/teori/grafisk_representasjon/figur_1.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

---

**Hva kan vi lese av?**
* Grafens form bestemmes av $a$. 
* Forteller oss umiddelbart hvor grafen skjærer $y$-aksen.
* Symmetrilinja kan bestemmes med formelen $x_0 = -\dfrac{b}{2a}$.



::::::::::::::


::::::::::::::{grid-item-card}
Ekstremalpunktsform
^^^

:::{figure} figurer/teori/algebraisk_uttrykk.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

---

:::{figure} figurer/teori/grafisk_representasjon.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

---

**Hva kan vi lese av?**
* Grafens form bestemmes av $a$.
* Forteller oss umiddelbart hvor grafen har et toppunkt eller bunnpunkt.
* Forteller oss umiddelbart hvor grafen har symmetrilinje.

::::::::::::::

:::::::::::::::
