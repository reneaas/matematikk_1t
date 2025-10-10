# Nullpunktsform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere og tolke en lineær funksjon på nullpunktsform.
* Kunne bytte mellom nullpunktsform og standardform. 
:::


Vi har så langt sett at vi kan representere en lineær funksjon $f$ på standardform. Standardformen forteller oss grafisk hvor mye grafen stiger eller synker, og hvor den skjærer $y$-aksen. Her skal vi se på en annen representasjonsform som vi skal kalle for **nullpunktsform**. Denne vil også fortelle oss hvor mye grafen til $f$ stiger eller synker, men vil i stedet fortelle oss hvor grafen til $f$ skjærer $x$-aksen – det vi kaller for **nullpunktet** til $f$ fordi det er der $f(x) = 0$.


## Algebraisk representasjon

:::{margin} Er nullpunktet $x = x_1$ eller $(x_1, 0)$?
Når vi beskriver nullpunkter, så sier vi ofte at $x = x_1$ er nullpunktet fremfor $(x_1, 0)$ fordi det er underforstått er $y$-koordinaten er $0$ i et nullpunkt. Det er ikke feil å si at nullpunktet $(x_1, 0)$, men det er mer vanlig å si at nullpunktet $x = x_1$.
:::

:::::::::::::::{summary} Nullpunktsform
En lineær funksjon $f$ kan skrives på nullpunktsform som følger:

:::{figure} ./figurer/teori/algebraisk_representasjon/nullpunktsform.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


:::{plot}
width: 80%
function: -2*(x - 2), f
ticks: off
xmin: -1
xmax: 4
point: (2, 0)
annotate: (1, -3), (2, 0), "Nullpunkt $(x_1, 0)$", -0.3
hline: 3, 0.5, 1.5
vline: 1.5, 1, 3
text: 1, 3, "$1$", top-center
text: 1.5, 2, "$a$", center-right
:::





:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
I figuren nedenfor vises grafen til en lineær funksjon $f$.


Bestem $f(x)$ på nullpunktsform.


:::{plot}
width: 70%
function: 2*(x - 1), f
:::


::::{solution}
---
dropdown: 0
---
Vi skriver $f(x)$ på nullpunktsform

$$
f(x) = a(x - x_1)
$$

Vi ser at grafen til $f$ skjærer $x$-aksen i $(1, 0)$ som betyr at $x_1 = 1$. 

Øker vi verdien til $x$ med $1$ fra $(1, 0)$, finner vi et punkt på grafen i $(2, 2)$. Det betyr at $y$-verdien har økt med $2$ og derfor er stigningstallet $a = 2$. 

Altså er 

$$
f(x) = a(x - x_1) = 2(x - 1)
$$
::::


:::::::::::::::


---




:::::::::::::::{exercise} Underveisoppgave 1
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$ på nullpunktsform.



:::{plot}
width: 70%
function: 3*(x + 1), f
:::


::::{answer}
$$
f(x) = 3(x + 1)
$$
::::


::::{solution}
Grafen til $f$ skjærer $x$-aksen i $(-1, 0)$ som betyr at $x_1 = -1$. Vi ser at dersom vi øker $x$ med $1$ enhet, så øker $y$-verdien med $3$ enheter. Derfor er stigningstallet $a = 3$. Altså er

$$
f(x) = a(x - x_1) = 3(x + 1)
$$
::::


:::::::::::::::





## Fra standardform til nullpunktsform


:::::::::::::::{example} Eksempel 2
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 4x + 5
$$

Bestem $f(x)$ på nullpunktsform.


::::{solution}
---
dropdown: 0
---
Nullpunktsformen er gitt ved 

$$
f(x) = a(x - x_1)
$$

Vi ser fra uttrykket at $a = 4$. Vi må nå bare finne $x_1$. Dette kan vi gjøre ved å løse likningen $f(x) = 0$ siden grafen til $f$ skjærer $x$-aksen der $f(x) = 0$. Da får vi: 

$$
f(x) = 0 
$$

$$
4x + 5 = 0
$$

$$
4x = -5
$$

$$
x = -\dfrac{5}{4}
$$

Dermed er $x_1 = -\dfrac{5}{4}$, og vi kan skrive $f(x)$ på nullpunktsform som

$$
f(x) = 4\left(x + \dfrac{5}{4}\right)
$$
::::

:::::::::::::::



:::::::::::::::{exercise} Underveisoppgave 2
En lineær funksjon $f$ er gitt ved 

$$
f(x) = -3\cdot x + 6
$$

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

::::{solution}
Vi løser likningen $f(x) = 0$: 

$$
f(x) = -3 \cdot x + 6
$$

$$
-3 \cdot x + 6 = 0
$$

$$
6 = 3x
$$

$$
x = 2
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $f(x)$ på nullpunktsform.

::::{answer}
$$
f(x) = -3 \cdot (x - 2)
$$
::::

::::{solution}
Siden nullpunktsformen til $f(x)$ er gitt ved 

$$
f(x) = -3 \cdot (x - 2)
$$

betyr det at nullpunktet til $f$ er gitt ved 

$$
x = 2.
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::


---

## Fra nullpunktsform til standardform


:::::::::::::::{example} Eksempel 3
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2(x + 3)
$$

Bestem $f(x)$ på standardform.


::::{solution}
---
dropdown: 0
---
Vi ganger ut parentesen for å finne $f(x)$ på standardform: 

$$
f(x) = 2(x + 3) = 2x + 6
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
En lineær funksjon $f$ er gitt ved

$$
f(x) = -2(x - 2)
$$

Bestem $f(x)$ på standardform. 


::::{answer}
$$
f(x) = -2x + 4
$$
::::

::::{solution}
Vi ganger ut parentesen for å finne $f(x)$ på standardform:

$$
f(x) = -2(x - 2) = -2x + 4
$$
::::
:::::::::::::::
