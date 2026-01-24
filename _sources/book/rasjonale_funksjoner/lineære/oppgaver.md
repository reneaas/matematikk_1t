# Oppgaver: <br> Lineære-over-lineære


:::::::::::::::{exercise} Oppgave 1


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
width: 60%
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$, $b$ og $c$ slik at grafen til $f$ har

1. En horisontal asymptote med likningen $y = 3$
2. En vertikal asymptote med likningen $x = -1$
3. Et nullpunkt i $x = 2$.


::::{answer}
$$
a = 3 \and b = 2 \and c = -1
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$, $b$ og $c$ slik at

1. Grafen til $f$ har en horisontal asymptote med likningen $y = -2$.
2. Grafen til $f$ skjærer $x$-aksen i $x = -3$.
3. Grafen til $f$ har en vertikal asymptote med likningen $x = 4$.


::::{answer}
$$
a = -2 \and b = -3 \and c = 4
$$
::::


:::::::::::::


::::::::::::::


:::::::::::::::


:::::::::::::::{exercise} Oppgave 2
Ta quizen!

::::::::{quiz-2}
:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist nedenfor.

:::{plot}
width: 60%
fontsize: 30
function: (x - 1) / (x - 2), f
point: (1, 0)
vline: 2, dashed
hline: 1, dashed
:::

Hvilket alternativ viser $f(x)$?

::::::{quiz-answer}
---
correct: true
---
$$
f(x) = \dfrac{x - 1}{x - 2}
$$
::::::


::::::{quiz-answer}
$$
f(x) = \dfrac{x + 1}{x - 2}
$$
::::::


::::::{quiz-answer}
$$
f(x) = \dfrac{-x + 1}{x - 2}
$$
::::::


::::::{quiz-answer}
$$
f(x) = \dfrac{x - 1}{x + 2}
$$
::::::

:::::::



:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist nedenfor.

:::{plot}
width: 70%
function: 2*(x - 3) / (x + 1), f, (-10, 10) \ {-1}
vline: -1, dashed
hline: 2, dashed
point: (3, 0)
xmin: -8
xmax: 8
ymin: -8
ymax: 8
:::

Hvilket alterantiv viser $f(x)$?

::::::{quiz-answer}
---
correct: true
---
$$
f(x) = \dfrac{2(x - 3)}{x + 1}
$$
::::::


::::::{quiz-answer}
$$
f(x) = \dfrac{3(x - 2)}{x + 1}
$$
::::::


::::::{quiz-answer}
$$
f(x) = \dfrac{x - 3}{x - 2}
$$
::::::


::::::{quiz-answer}
$$
f(x) = \dfrac{2(x + 1)}{x - 3}
$$
::::::


:::::::



:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist nedenfor.


:::{plot}
width: 70%
function: -3 * (x + 1) / x
vline: 0, dashed
hline: -3, dashed
point: (-1, 0)
xmin: -8
xmax: 8
ymin: -8
ymax: 8
:::

Hvilket alternativ viser $f(x)$?

::::::{quiz-answer}
---
correct: true
---
$$
f(x) = \dfrac{-3(x + 1)}{x}
$$
::::::

::::::{quiz-answer}
$$
f(x) = \dfrac{3(x + 1)}{x}
$$
::::::

::::::{quiz-answer}
$$
f(x) = \dfrac{-3(x - 1)}{x}
$$
::::::

::::::{quiz-answer}
$$
f(x) = \dfrac{-3(x + 1)}{x - 1}
$$
::::::


:::::::


:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist nedenfor.

:::{plot}
width: 70%
function: 2*x / (x + 3)
vline: -3, dashed
hline: 2, dashed
point: (0, 0)
xmin: -8
xmax: 8
ymin: -8
ymax: 8
:::

Hvilket alternativ viser $f(x)$?

::::::{quiz-answer}
---
correct: true
---
$$
f(x) = \dfrac{2x}{x + 3}
$$
::::::

::::::{quiz-answer}
$$
f(x) = \dfrac{2(x + 3)}{x}
$$
::::::

::::::{quiz-answer}
$$
f(x) = \dfrac{2x}{x - 3}
$$
::::::

::::::{quiz-answer}
$$
f(x) = \dfrac{(x + 3)}{2x}
$$
::::::


:::::::


::::::::

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 2
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I figuren nedenfor vises grafen til en rasjonal funksjon $f$.

Bestem $f(x)$.


:::{plot}
width: 80%
function: -(x - 1) / (x - 2), f
domain: (-10, 10) \ {2}
vline: 2, dashed
hline: -1, dashed
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = \dfrac{-(x - 1)}{x - 2}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
I figuren nedenfor vises grafen til en rasjonal funksjon $g$.

Bestem $g(x)$.

:::{plot}
width: 80%
function: 2*(x - 1) / (x - 3), g
domain: (-10, 10) \ {3}
hline: 2, dashed
vline: 3, dashed
xmax: 8
ymax: 8 
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
g(x) = \dfrac{2(x - 1)}{x - 3}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
I figuren nedenfor vises grafen til en rasjonal funksjon $h$.

Bestem $h(x)$.



:::{plot}
width: 80%
function: -2*(x + 1) / (x - 1), h
domain: (-10, 10) \ {1}
vline: 1, dashed
hline: -2, dashed
xmax: 8
ymin: -8
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
h(x) = \dfrac{-2(x + 2)}{x - 1}
$$
::::

:::::::::::::

:::::::::::::{tab-item} d
I figuren nedenfor vises grafen til en rasjonal funksjon $p$.

Bestem $p(x)$.


:::{plot}
width: 80%
function: (x - 3) / (x + 2), p
domain: (-10, 10) \ {-2}
vline: -2, dashed
hline: 1, dashed
xmin: -8
ymax: 8
:::




::::{admonition} Fasit
---
class: dropdown, answer
---
$$
p(x) = \dfrac{x - 3}{x + 2}
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
Ta quizen!

::::::::{quiz-2}
:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist i figuren nedenfor.


:::{plot}
width: 70%
function: 2*(x - 1) / (x + 3), f
vline: -3, dashed
hline: 2, dashed
point: (1, 0)
xmin: -8
xmax: 8
ymin: -8
ymax: 8
:::

Hvilket alternativ viser fortegnslinja til $f(x)$?


::::::{quiz-answer}
---
correct: true
---
:::{signchart-2}
width: 100%
function: 2*(x - 1) / (x + 3), f(x)
factors: false
fontsize: 35
:::

::::::


::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: 2*(x + 1) / (x - 3), f(x)
factors: false
fontsize: 35
:::

::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: -2*(x - 1) / (x + 3), f(x)
factors: false
fontsize: 35
:::

::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: -2*(x + 1) / (x - 3), f(x)
factors: false
fontsize: 35
:::

::::::





:::::::


:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ vises i figuren nedenfor.

:::{plot}
width: 70%
function: -2*(x + 3) / x, f
vline: 0, dashed
hline: -2, dashed
point: (-3, 0)
xmin: -8
xmax: 8
ymin: -8
ymax: 8
:::

Hvilket alternativ viser fortegnslinja til $f(x)$?

::::::{quiz-answer}
---
correct: true
---
:::{signchart-2}
width: 100%
function: -2*(x + 3) / x, f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: 2*(x + 3) / x, f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: -2*(x - 3) / x, f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: 2*(x - 3) / x, f(x)
factors: false
fontsize: 35
:::
::::::




:::::::



:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist i figuren nedenfor.

:::{plot}
width: 70%
function: x / (x + 2), f
vline: -2, dashed
hline: 1, dashed
point: (0, 0)
xmin: -8
xmax: 8
ymin: -8
ymax: 8
:::

Hvilket alternativ viser fortegnslinja til $f(x)$?

::::::{quiz-answer}
---
correct: true
---
:::{signchart-2}
width: 100%
function: x / (x + 2), f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: (x + 2) / x, f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: -x / (x + 2), f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: -(x + 2) / x, f(x)
factors: false
fontsize: 35
:::
::::::



:::::::


:::::::{quiz-question}
Grafen til en rasjonal funksjon $f$ er vist i figuren nedenfor.

:::{plot}
width: 70%
function: -3*(x - 2) / (x - 4), f
vline: 4, dashed
hline: -3, dashed
point: (2, 0)
xmin: -2
xmax: 14
ymin: -8
ymax: 8
:::

Hvilket alternativ viser fortegnslinja til $f(x)$?

::::::{quiz-answer}
---
correct: true
---
:::{signchart-2}
width: 100%
function: -3*(x - 2) / (x - 4), f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: 3*(x - 2) / (x - 4), f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: -3*(x + 2) / (x - 4), f(x)
factors: false
fontsize: 35
:::
::::::

::::::{quiz-answer}
:::{signchart-2}
width: 100%
function: 3*(x + 2) / (x - 4), f(x)
factors: false
fontsize: 35
:::
::::::



:::::::


::::::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{2(x - 3)}{x + 1}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktet til $f$.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 3.
$$
:::

:::::::::::::

:::::::::::::{tab-item} b
Bestem den vertikale og horisontale asymptoten til $f$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
* Horisontal asymptote: $y = 2$.
* Vertikal asymptote: $x = -1$.
:::
:::::::::::::



:::::::::::::{tab-item} c
Tegn en fortegnsskjema for $f(x)$.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_3/d.svg
---
width: 100%
class: no-click, adaptive-figure
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
Lag en skisse av grafen til $f$.

Skissen skal inneholde:
* Nullpunktet til $f$.
* Asymptotene til $f$.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_3/e.svg
---
width: 100%
class: no-click, adaptive-figure
:::
::::

:::::::::::::


::::::::::::::

:::::::::::::::




---





:::::::::::::::{exercise} Oppgave 4
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{-x + 2}{x - 4}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen $f(x) = 0$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 2.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem asymptotene til $f$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
* Horisontal asymptote: $y = -1$. 
* Vertikal asymptote: $x = 4$. 
::::

:::::::::::::


:::::::::::::{tab-item} c
Lag en skisse av grafen til $f$.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_4/c.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten $f(x) < 0$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \mathbb{R} \setminus [2, 4].
$$
::::

:::::::::::::
::::::::::::::

:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 5
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Om en rasjonal funksjon $f$ får du vite at:
* Grafen til $f$ har asymptotene $y = 2$ og $x = -4$. 
* Grafen til $f$ har et nullpunkt i $x = 1$.

Bestem et mulig uttrykk for $f(x)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = \dfrac{2(x - 1)}{x + 4}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Om en rasjonal funksjon $g$ får du vite at:
* Grafen til $g$ har en vertikal asymptote med likningen $x = -2$.
* Grafen til $g$ skjærer $x$-aksen i $x = 2$. 
* Grafen til $g$ skjærer $y$-aksen i $y = 6$. 

Bestem et mulig uttrykk for $g(x)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(x) = \dfrac{-6(x - 2)}{x + 2}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Om en rasjonal funksjon $h$ får du vite at:
* Grafen til $f$ har en horisontal asymptote med likningen $y = 4$.
* Grafen til $h$ skjærer $x$-aksen i $x = -3$. 
* Grafen til $h$ har et bruddpunkt i $x = 2$. 

Bestem et mulig uttrykk for $h(x)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) = \dfrac{4x + 12}{x - 2}
$$
::::

:::::::::::::
::::::::::::::

:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 6
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x - 2}{x + 3}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktet og asymptotene til $f$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
* Nullpunkt: $x = 2$.
* Horisontal asymptote: $y = 1$.
* Vertikal asymptote: $x = -3$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten $f(x) \geq 0$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \mathbb{R} \setminus [-3, 2\rangle. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningen $f(x) = 2$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -8. 
$$
::::

:::::::::::::

:::::::::::::{tab-item} d
Løs ulikheten $f(x) \leq 2$.  


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \mathbb{R} \setminus \langle -8, -3].
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7

En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{-2x + 4}{x + 1}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem hvor grafen til $f$ skjærer $x$-aksen. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 2. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem asymptotene til $f$.

::::{admonition} Fasit
---
class: answer, dropdown
---
* Horisontal asymptote: $y = -2$.
* Vertikal asymptote: $x = -1$.
::::

:::::::::::::


:::::::::::::{tab-item} c
Lag en skisse av grafen til $f$.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_7/c.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::


:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten $f(x) \geq 0$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -1, 2]
$$

:::::::::::::

::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 8

:::{figure} ./figurer/oppgaver/oppgave_8/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


Figuren ovenfor vises grafen til en rasjonal funksjon $f(x) = \dfrac{1}{x}$ og tangenten til grafen til $f$ i punktet $(s, f(s))$. 

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



Bestem likningen for tangenten.


:::::::::::::



:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::


Tangenten skjærer koordinataksene i punktene $A$ og $B$.

Bestem koordinatene til $A$ og $B$ uttrykt ved $s$.
:::::::::::::



:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


Bestem arealet av $\triangle OAB$ 



:::::::::::::



::::::::::::::

:::::::::::::::



---








