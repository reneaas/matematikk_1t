# Lineære-over-lineære 

::::{admonition} Læringsmål
---
class: tip
---
* Kunne representere lineære-over-lineære rasjonale funksjoner algebraisk, grafisk og med fortegnslinjer.
* Kunne bestemme $f(x)$ for rasjonale funksjoner der tellergrad og nevnergrad er 1.
* Kunne bestemme asymptotene til rasjonale funksjoner.
* Kunne bestemme nullpunkter og løse ulikheter med rasjonale funksjoner.
::::

En **rasjonal funksjon** er en funksjon som kan skrives som en brøk der telleren og nevneren er polynomer.

:::::{admonition} Definisjon: Rasjonale funksjoner
---
class: theory
---
En rasjonal funksjon $f$ er en funksjon som kan skrives som

$$
f(x) = \dfrac{P(x)}{Q(x)}
$$

der $P(x)$ og $Q(x)$ er polynomer. 

Graden til $P$ kaller vi for **tellergraden** til $f$ og graden til $Q$ kaller vi for **nevnergraden** til $f$.
:::::


## Algebraisk og grafisk representasjon


Vi skal først konsentrere oss om rasjonale funksjoner der tellergraden og nevnergraden er $1$. 
Det vil si der både teller og nevner er lineære polynomer. Vi skal kalle dette for **lineære-over-lineære** rasjonale funksjoner.

:::::{summary} Lineære-over-lineære rasjonale funksjoner
En rasjonal funksjon $f$ der teller $P(x)$ og nevner $Q(x)$ er lineære polynomer kan alltid skrives som

:::{figure} ./figurer/teori/annoterte_figurer/linear_rational_function.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::


:::{plot}
width: 80%
fontsize: 18
function: (x + 1) / (x - 2), f, (-15, 15) \ {2}
xmin: -6.5
xmax: 8
ymin: -7
ymax: 10
ticks: off
hline: 1, dashed
vline: 2, dashed
annotate: (-6, 5), (-1, 1), "Horisontal asymptote $y = a$", -0.3
annotate: (2.5, -5), (2, -2), "Vertikal asymptote $x = c$", 0.3
point: (-1, 0)
annotate: (-5, -3), (-1, 0), "Nullpunkt $x = b$"
:::


Grafen til $f$ er en **hyperbel** med 
* En horisontal asymptote med likningen $y = a$.
* En vertikal asymptote med likningen $x = c$.
* Et nullpunkt i $x = b$. 


:::::




:::::::::::::::{exercise} Underveisoppgave 1
I den interaktive figuren nedenfor vises grafen til en rasjonal funksjon 

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

:::{interactive-graph} 
interactive-var: a, -4, 4, 9
interactive-var: b, -4, 4, 9
interactive-var: c, -4, 4, 9
interactive-var-start: a=1, b=2, c=-1
function: a*(x - b) / (x - c), f, (-10, 10) \ {c}
xmin: -8
xmax: 8
ymin: -8
ymax: 8
hline: a, dashed
vline: c, dashed
point: (b, 0)
width: 70%
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$, $b$ og $c$ slik at grafen til $f$ har 

1. En horisontal asymptote med likningen $y = 2$.
2. En vertikal asymptote med likningen $x = -1$.
3. Et nullpunkt i $x = 3$.


::::{answer}
$$
a = 2 \and b = 3 \and c = -1
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$, $b$ og $c$ slik at grafen til $f$ har 

1. En horisontal asymptote med likningen $y = -1$.
2. En vertikal asymptote med likningen $x = 2$.
3. Skjærer $x$-aksen i $x = 1$.


::::{answer}
$$
a = -1 \and b = 1 \and c = 2
$$
::::
:::::::::::::





::::::::::::::



:::::::::::::::



---

## Fra graf til $f(x)$

Vi går løs på et eksempel. 

:::::::::::::::{example} Eksempel 1
I figuren nedenfor vises grafen til en lineær-over-lineær rasjonal funksjon $f$. 

Bestem $f(x)$.


:::{plot}
width: 80%
fontsize: 18
function: 2*(x - 3) / (x + 1), f, (-15, 15) \ {-1}
xmin: -9
xmax: 9
ymin: -8
ymax: 8
vline: -1, dashed
hline: 2, dashed
:::


::::{admonition} Løsning
---
class: solution
---
En rasjonal funksjon der teller og nevner er lineære polynomer, kan alltid skrives som

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

der $y = a$ er den horisontale asympoten, $x = b$ er nullpunktet og $x = c$ er den vertikale asymptoten. 

* Horisontal asymptote er $y = 2$, så $a = 2$.
* Nullpunktet er $x = 3$, så $b = 3$.
* Vertikal asymptote er $x = -1$, så $c = -1$.

Dermed er $f(x)$ gitt ved 

$$
f(x) = \dfrac{2\cdot (x - 3)}{x - (-1)} = \dfrac{2x - 6}{x + 1}
$$
::::

:::::::::::::::

---


:::::::::::::::{exercise} Quiz 1


:::{quiz}
Q: Hvilken funksjon hører til grafen? ![{width: 60%}](./figurer/quiz/quiz_1/spm_1/graf.svg)
+ $$f(x) = \dfrac{-(x - 1)}{x - 2}$$
- $$f(x) = \dfrac{-(x + 1)}{x - 2}$$
- $$f(x) = \dfrac{2(x - 1)}{x + 1}$$
- $$f(x) = \dfrac{-(x - 2)}{x - 1}$$

Q: Hvilken funksjon hører til grafen? ![{width: 60%}](./figurer/quiz/quiz_1/spm_2/graf.svg)
+ $$f(x) = \dfrac{2(x + 2)}{x + 3}$$
- $$f(x) = \dfrac{2(x + 2)}{x - 3}$$
- $$f(x) = \dfrac{3(x + 2)}{x - 2}$$
- $$f(x) = \dfrac{3(x - 2)}{x + 2}$$

Q: Hvilken funksjon hører til grafen? ![{width: 60%}](./figurer/quiz/quiz_1/spm_3/graf.svg)
+ $$f(x) = \dfrac{-3(x + 1)}{x - 2}$$
- $$f(x) = \dfrac{2(x + 1)}{x + 3}$$
- $$f(x) = \dfrac{2(x + 3)}{x + 1}$$
- $$f(x) = \dfrac{3(x - 2)}{x + 1}$$

Q: Hvilken funksjon hører til grafen? ![{width: 60%}](./figurer/quiz/quiz_1/spm_4/graf.svg)
+ $$f(x) = \dfrac{-2(x - 3)}{x + 1}$$
- $$f(x) = \dfrac{2(x - 1)}{x - 3}$$
- $$f(x) = \dfrac{3(x + 1)}{x + 2}$$
- $$f(x) = \dfrac{-2(x + 1)}{x - 3}$$

:::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
I figuren nedenfor vises grafen til en rasjonal funksjon $f$.

Bestem $f(x)$.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/graf.svg
---
width: 90%
class: no-click, adaptive-figure
---
viser grafen til en rasjonal funksjon $f$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = \dfrac{2(x - 3)}{x + 1}
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
En rasjonal funksjon kan skrives som:

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

der $y = a$ er den horisontale asymptoten, $x = b$ er nullpunktet og $x = c$ er den vertikale asymptoten.

* Horisontal asymptote er $y = 2$, så $a = 2$.
* Nullpunktet til $f$ er $x = 3$, så $x_1 = 3$.
* Vertikal asymptote er $x = -1$, så $x_\infty = -1$.

Dermed er $f(x)$ gitt ved

$$
f(x) = \dfrac{2(x - 3)}{x + 1}
$$
::::


:::::::::::::::


## Bestemme egenskaper fra $f(x)$

:::::{admonition} Eksempel 2
---
class: example
---
En rasjonal funksjon $f$ er gitt ved

$$
f(x) = \dfrac{2x + 6}{x - 1}
$$

Bestem nullpunktet og asymptotene til $f$.

::::{admonition} Løsning
---
class: solution
---
Vi kan skrive om uttrykket til $f(x)$ ved å faktorisere telleren:

$$
f(x) = \dfrac{2x + 6}{x - 1} = \dfrac{2(x + 3)}{x - 1} 
$$

som betyr at vi kan lese av nullpunktet og asymptotene til $f$:


* Horisontal asymptote: $y = 2$. 
* Vertikal asymptote: $x = 1$.
* Nullpunkt: $x = -3$.

::::
:::::


---


:::::::::::::::{exercise} Underveisoppgave 3
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{3x + 6}{x - 1}
$$

Bestem 

* Nullpunktet til $f$
* Likningen for den vertikale asymptoten til $f$
* Likningen for den horisontale asymptoten til $f$


::::{answer}
* Nullpunktet er $x = -2$
* Vertikal asymptote er $x = 1$
* Horisontal asymptote er $y = 3$
::::

::::{solution}
Generelt er en lineær-over-lineær rasjonal funksjon gitt ved 

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

Vi har at 

$$
f(x) = \dfrac{3x + 6}{x - 1} = \dfrac{3(x + 2)}{x - 1}
$$

Sammenlikninger vi det generelle uttrykket med $f(x)$ så ser vi at 

* Nullpunktet er $x = -2$
* Vertikal asymptote er $x = 1$
* Horisontal asymptote er $y = 3$

::::

:::::::::::::::

---

## Fra $f(x)$ til graf

Vi går løs på et eksempel der vi lager en skisse av grafen til en lineær rasjonal funksjon.


:::::::::::::::{admonition} Eksempel 3
---
class: example
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{-2x + 4}{x + 3}
$$

Lag en skisse av grafen til $f$. 

:::::{admonition} Løsning
---
class: solution
---
Vi starter med å bestemme egenskapene til $f$ ved å skrive om $f(x)$ så vi kan lese av nullpunktet og asymptotene:

$$
f(x) = \dfrac{-2x + 4}{x + 3} = \dfrac{-2(x - 2)}{x + 3}
$$

som betyr at 

* $y = -2$ er en horisontal asymptote.
* $x = 2$ er et nullpunkt.
* $x = -3$ er en vertikal asymptote. 

Vi tegner en fortegnslinje der vi passer på å få med at $x = -3$ et **bruddpunkt**: 

:::{figure} ./figurer/eksempler/eksempel_3/fortegnslinje.svg
---
name: fig-lineære-rasjonale-funksjoner-eksempel-3-fortegnslinje
width: 90%
class: no-click, adaptive-figure
---
viser fortegnsskjema for $f(x) = (-2x + 4) / (x + 3)$. Bruddpunktene til $f(x)$ er markert med et kryss "$\times$" i fortegnslinja.
::: 

Ut ifra fortegnslinja til $f(x)$ kan vi se at $f(x) < 0$ når $x < -3$ og $x > 2$ og at $f(x) > 0$ når $-2 < x < 3$. 
Samler vi dette med opplysningene om nullpunktet og asymptotene til $f$, kan vi lage en skisse av grafen til $f$ som følger:

:::{figure} ./figurer/eksempler/eksempel_3/graf.svg
---
name: fig-lineære-rasjonale-funksjoner-eksempel-3-graf
width: 90%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $f(x) = (-2x + 4) / (x + 3)$ med nullpunktet $x = 2$, den vertikale asymptoten $x = -3$ og den horisontale asymptoten $y = -2$.
::: 

:::::

:::::::::::::::
