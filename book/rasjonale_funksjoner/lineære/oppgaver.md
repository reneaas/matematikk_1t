# Oppgaver: <br> Lineære-over-lineære

:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Ta quizen!

:::{quiz}
Q: Hvilket funksjonsuttrykk hører til grafen? ![{width: 60%}](./figurer/quiz/quiz_1/spm_1/graf.svg)
+ $$f(x) = \dfrac{-(x - 1)}{x - 2}$$
- $$f(x) = \dfrac{(x - 1)}{x - 2}$$
- $$f(x) = \dfrac{(x + 1)}{x - 2}$$
- $$f(x) = \dfrac{(x - 1)}{x + 2}$$

Q: Hvilket funksjonsuttrykk hører til grafen? ![{width: 60%}](./figurer/quiz/quiz_1/spm_2/graf.svg)
+ $$f(x) = \dfrac{2(x + 2)}{x + 3}$$
- $$f(x) = \dfrac{2(x - 2)}{x - 3}$$
- $$f(x) = \dfrac{-3(x + 2)}{x - 2}$$
- $$f(x) = \dfrac{-3(x - 2)}{x + 2}$$
:::
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
Bestem definisjonsmengden $D_f$ og verdimengden $V_f$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
D_f = \mathbb{R} \setminus \{-1\} \quad \text{og} \quad V_f = \mathbb{R} \setminus \{2\}.
$$
:::

:::::::::::::


:::::::::::::{tab-item} d
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


:::::::::::::{tab-item} e
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
* Definisjonsmengden til $g$ er $D_g = \mathbb{R} \setminus \{-2\}$. 
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
* Verdimengden til $h$ er $V_h = \mathbb{R} \setminus \{4\}$. 
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








