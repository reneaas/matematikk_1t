# Oppgavesamling: Polynomer

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---

::::::::::::::{admonition} Repetisjon: Andregradslikninger
---
class: summary, dropdown
---
Løsningene til en andregradslikning

$$
ax^2 + bx + c = 0
$$

er gitt ved $abc$-formelen

$$
x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Flere begreper er **ekvivalente** med løsningene til en andregradslikning. Å finne løsningene er det samme som:
* Å bestemme **nullpunktene** til andregradsfunksjonen $f(x) = ax^2 + bx + c$. 
* Å bestemme **røttene** til andregradspolynomet $ax^2 + bx + c$.
* Å finne punktene der grafen til $f$ **skjærer $x$-aksen**. 

::::::::::::::


::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - x - 2.
$$

Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen. 


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -1 \quad \text{og} \quad x = 2.
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
Grafen til $f$ skjærer $x$-aksen når $f(x) = 0$. Vi bruker $abc$-formelen for bestemme punktene:

$$
x = \dfrac{-(-1) \pm \sqrt{(-1)^2 - 4\cdot 1 \cdot (-2)}}{2\cdot 1} = \dfrac{1 \pm \sqrt{9}}{2} = \dfrac{1 \pm 3}{2}
$$

som gir løsningene 

$$
x = -1 \or x = 2.
$$

Grafen til $f$ skjærer derfor $x$-aksen i $x = -1$ og $x = 2$.
::::

:::::::::::::


:::::::::::::{tab-item} b
En andregradsfunksjon $g$ er gitt ved 

$$
g(x) = -x^2 + 2x + 3.
$$

Bestem nullpunktene til $g$.


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -1 \or x = 3
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
Nullpunktene til $g$ svarer til løsningene av likningen $g(x) = 0$. Vi bruker $abc$-formelen for å finne nullpunktene:

$$
x = \dfrac{-2 \pm \sqrt{2^2 - 4 \cdot (-1) \cdot 3}}{2 \cdot (-1)} = \dfrac{-2 \pm \sqrt{16}}{-2} = \dfrac{-2 \pm 4}{-2} = 1 \mp 2
$$

som gir

$$
x = -1 \or x = 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem røttene til polynomet 

$$
h(x) = x^2 - 5x + 6.
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 2 \or x = 3.
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
Røttene til polynomet $h(x)$ svarer til punktene hvor $h(x) = 0$. Vi bruker $abc$-formelen for å bestemme røttene:

$$
x = \dfrac{-(-5) \pm \sqrt{(-5)^2 - 4 \cdot 1 \cdot 6}}{2 \cdot 1} = \dfrac{5 \pm \sqrt{25 - 24}}{2} = \dfrac{5 \pm 1}{2}
$$

som gir røttene

$$
x = 2 \or x = 3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Løs likningen

$$
x^2 - 2x - 8 = 0
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -2 \or x = 4.
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
Vi bruker $abc$-formelen for å løse likningen:

$$
x = \dfrac{-(-2) \pm \sqrt{(-2)^2 - 4 \cdot 1 \cdot (-8)}}{2\cdot 1} = \dfrac{2 \pm \sqrt{36}}{2} = \dfrac{2 \pm 6}{2} = 1 \pm 3
$$

som gir løsningene

$$
x = -2 \or x = 4.
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Utfør polynomdivisjonen

$$
(x^3 - 5x^2 + 8x - 4) : (x - 1).
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x^3 - 5x^2 + 8x - 4) : (x - 1) = x^2 - 4x + 4.
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
:::{figure} ./koder/oppgaver/oppgave_2/a.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Utfør polynomdivisjonen

$$
(x^3 + 4x^2 + 5x + 2) : (x + 2). 
$$


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x^3 + 4x^2 + 5x + 2) : (x + 2) = x^2 + 2x + 1.
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
:::{figure} ./koder/oppgaver/oppgave_2/b.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Utfør polynomdivisjonen

$$
(x^3 - 2x^2 + 3x - 4) : (x - 2). 
$$


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x^3 - 2x^2 + 3x - 4) : (x - 2) = x^2 + 3 + \dfrac{2}{x - 2}
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
:::{figure} ./koder/oppgaver/oppgave_2/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
Utfør polynomdivisjonen

$$
(x^4 - x^2 + 1) : (x + 3).
$$


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
(x^3 - 2x^2 + 3x - 4) : (x - 2) = x^3 - 3x^2 + 8x - 24 + \dfrac{73}{x + 3}
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
:::{figure} ./koder/oppgaver/oppgave_2/d.svg
---
width: 90%
class: no-click, adaptive-figure
---
:::
::::

:::::::::::::



::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
::::::::::::::{admonition} Repetisjon: Andregradsfunksjoner
---
class: summary, dropdown
---
En andregradsfunksjon $f$ kan skrives på tre ulike måter:

:::::::::::::{tab-set}
::::::::::::{tab-item} Standardform
$$
f(x) = ax^2 + bx + c
$$

der $a$, $b$ og $c$ er koeffisientene og $a$ er ledende koeffisient.
::::::::::::

::::::::::::{tab-item} Ekstremalform
$$
f(x) = a(x - x_0)^2 + y_0
$$

der $a$ er ledende koeffisient, $x_0$ er ekstremalpunktet og $y_0$ er ekstremalverdien.

::::::::::::

::::::::::::{tab-item} Nullpunktsform
$$
f(x) = a(x - x_1)(x - x_2)
$$

der $a$ er ledende koeffisient, og $x_1$ og $x_2$ er nullpunktene.
::::::::::::
:::::::::::::

::::::::::::::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Grafen til en andregradsfunksjon $f$ er vist i {numref}`fig-polynomer-oppgavesamling-oppgave-3-a`. 

Bestem $f(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_3/a.svg
---
name: fig-polynomer-oppgavesamling-oppgave-3-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = (x - 1)^2 - 4. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $f$ har et bunnpunkt i $(1, -4)$ som betyr at vi kan bruke ekstremalform

$$
f(x) = a(x - 1)^2 - 4. 
$$

For å bestemme $a$ bruker vi ett annet punkt på grafen til $f$. Velger $(3, 0)$ som gir 

$$
f(3) = 0 \liff a(3 - 1)^2 - 4 = 0 \liff 4a - 4 = 0 \liff a = 1.
$$

Dermed er

$$
f(x) = (x - 1)^2 - 4. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Grafen til en andregradsfunksjon $g$ er vist i {numref}`fig-polynomer-oppgavesamling-oppgave-3-b`. 

Bestem $g(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_3/b.svg
---
name: fig-polynomer-oppgavesamling-oppgave-3-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $g$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(x) = -2(x + 2)^2 - 1. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan lese av at grafen til $g$ har et toppunkt i $(-2, -1)$ som betyr at vi kan skrive $g(x)$ på ekstremalform:

$$
g(x) = a(x + 2)^2 - 1. 
$$

Vi bestemmer $a$ ved å bruke ett punkt til på grafen til $g$. Velger $(-1, -3)$ som gir 

$$
g(-1) = -3 \liff a(-1 + 2)^2 - 1 = -3 \liff a - 1 = -3
$$

som gir $a = -2$. Dermed er 

$$
g(x) = -2(x + 2)^2 - 1. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Grafen til en andregradsfunksjon $h$ er vist i {numref}`fig-polynomer-oppgavesamling-oppgave-3-c`. 

Bestem $h(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_3/c.svg
---
name: fig-polynomer-oppgavesamling-oppgave-3-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $h$.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) = \dfrac{1}{2}(x + 2)(x - 1)
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan lese av at grafen til $h$ har nullpunktene $x = -2$ og $x = 1$ som betyr at vi kan skrive $h(x)$ på nullpunktsform:

$$
h(x) = a(x + 2)(x - 1).
$$

For å bestemme $a$, finner vi ett punkt til på grafen til $h$. Vi velger $(2, 2)$ som gir 

$$
h(2) = 2 \liff a(2 + 2)(2 - 1) = 2 \liff 4a = 2 \liff a = \dfrac{1}{2}.
$$

Dermed er

$$
h(x) = \dfrac{1}{2}(x + 2)(x - 1)
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---

::::::::::::::{admonition} Repetisjonsquiz om ulikheter og intervaller
---
class: summary, dropdown
---
Ta quizen for litt repetisjon! Flere svaralternativer kan være riktig.

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::

::::::::::::::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 4x + 4.
$$

Løs $f(x) > 0$. 


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x \in \mathbb{R} \setminus \{2\}.
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
Vi kan først bruke 2.kvadratsetning til å faktorisere $f(x)$ som gir 

$$
f(x) = (x - 2)^2.
$$

Videre skal vi løse ulikheten

$$
f(x) > 0 \liff (x - 2)^2 > 0.
$$

som betyr at $f(x) > 0$ så lenge $x \neq 2$. Dermed er løsningen

$$
x \in \mathbb{R} \setminus \{2\}.
$$
::::



:::::::::::::


:::::::::::::{tab-item} b
Løs 

$$
(x - 1)(x + 2) \leq 0. 
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in [-2, 1]. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å tegne et fortegnsskjema for $f(x) = (x - 1)(x + 2)$:

:::{figure} ./figurer/oppgaver/oppgave_4/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Fra fortegnslinja til $f(x)$, kan vi lese av at $f(x) \leq 0$ når

$$
x \in [-2, 1]. 
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem løsningen av 

$$
x^2 - x - 6 \geq 0. 
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \mathbb{R} \setminus \langle -2, 3 \rangle. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
For å løse ulikheten, må vi først faktorisere andregradspolynomet. For å oppnå dette, bestemmer vi først røttene med $abc$-formelen:

$$
x = \dfrac{-(-1) \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot (-6)}}{2 \cdot 1} = \dfrac{1 \pm \sqrt{25}}{2} = \dfrac{1 \pm 5}{2}
$$

som gir 

$$
x = -2 \or x = 3.
$$

Dermed kan vi skrive ulikheten som 

$$
x^2 - x - 6 \geq 0 \liff (x + 2)(x - 3) \geq 0.
$$

Vi tegner et fortegnsskjema for $f(x) = (x + 2)(x - 3)$ og leser av hvor $f(x) \geq 0$:

:::{figure} ./figurer/oppgaver/oppgave_4/c.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Fra fortegnslinja til $f(x)$ kan vi lese av at $f(x) \geq 0$ når


$$
x \in \mathbb{R} \setminus \langle -2, 3 \rangle. 
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
En andregradsfunksjon $g$ er gitt ved 

$$
g(x) = -x^2 + 2x + 3.
$$

Løs $g(x) < 0$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \mathbb{R} \setminus [-1, 3]. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å faktorisere $g(x)$ som vi gjør ved å først finne nullpunktene med $abc$-formelen:

$$
x = \dfrac{-2 \pm \sqrt{2^2 - 4 \cdot (-1) \cdot 3}}{2 \cdot(-1)} = \dfrac{2 \pm \sqrt{16}}{-2} = \dfrac{2 \pm 4}{-2} = 1 \mp 2
$$

som gir 

$$
x = -1 \or x = 3.
$$

Dermed kan vi skrive $g(x)$ som 

$$
g(x) = -(x + 1)(x - 3). 
$$

Så tegner vi et fortegnsskjema for $g(x)$ og leser av hvor $g(x) < 0$:

:::{figure} ./figurer/oppgaver/oppgave_4/d.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Fra fortegnslinja til $g(x)$ kan vi lese av at $g(x) < 0$ når

$$
x \in \mathbb{R} \setminus [-1, 3]. 
$$
::::

:::::::::::::




::::::::::::::


:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-1
---

::::::::::::::{admonition} Repetisjon: Derivasjonsregler for polynomer
---
class: summary, dropdown
---
For et polynom $f(x)$ av grad $n$, er den deriverte $f'(x)$ et polynom av grad $n - 1$.

Derivasjonsreglene for polynomer er som følger: 

Regel 1
: For ethvert ledd $a x^n$ i et polynom $f(x)$, vil den deriverte av leddet være

$$
(a x^n)' = n\cdot a x^{n-1}
$$

Regel 2
: Hvert ledd i et polynom deriveres hver for seg:

$$
(ax^n + bx^m)' = (ax^n)' + (bx^m)'
$$

Regel 3
: Den deriverte av en konstant er null:

$$
C' = 0
$$

Regel 4
: Den deriverte av et lineært ledd $ax$ er 

$$
(ax)' = a
$$

::::::::::::::


Bestem den deriverte til funksjonene. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = x^2 - 5x + 7
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f'(x) = 2x - 5
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
$$
f'(x) = (x^2 - 5x + 7)' = (x^2)' - (5x)' + (7)' = 2x - 5 + 0 = 2x - 5
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = x^3 + 4x^2 - 2
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
g'(x) = 3x^2 + 8x 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
$$
g'(x) = (x^3 + 4x^2 - 2)' = (x^3)' + (4x^2)' - (2)' = 3x^2 + 8x + 0 = 3x^2 + 8x
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = -3x^4 + 12x^2 
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h'(x) = -12x^3 + 24x
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
$$
h'(x) = (-3x^4 + 12x^2)' = (-3x^4)' + (12x^2)' = -12x^3 + 24x
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = 3x^5 - 2x^3 + 5x - 6
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
p'(x) = 15x^4 - 6x^2 + 5
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
    p'(x) &= (3x^5 - 2x^3 + 5x - 6)' \\
    \\
    &= (3x^5)' - (2x^3)' + (5x)' - (6)' \\
    \\
    &= 15x^4 - 6x^2 + 5 + 0 \\
    \\
    &= 15x^4 - 6x^2 + 5
\end{align*}
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---

::::::::::::::{admonition} Repetisjon: Likningen til en tangent
---
class: summary, dropdown
---
Likningen til en tangent i $(r, f(r))$ kan bestemmes på to måter:

1. **Strategi 1**: Den deriverte $f'(r)$ kombinert med ettpunktsformelen i $(r, f(r))$.
2. **Strategi 2**: Resten i polynomdivisjonen $f(x) : (x - r)^2$ gir likningen til tangenten.

Du velger selv hvilken strategi du ønsker å bruke. Men det kan være lurt å øve på begge.

::::::::::::::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = -x^2 + 4x + 5. 
$$

Bestem likningen til tangenten i $(1, f(1))$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 2x + 6.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Bruker ettpunktsformelen og den deriverte til $f$:

$$
f'(x) = (-x^2 + 4x + 5)' = (-2x + 4) = -2x + 4.
$$

Da blir stigningstallet til tangenten 

$$
a = f'(1) = -2 \cdot 1 + 4 = 2.
$$



Så trenger vi $y_1 = f(1)$:

$$
f(1) = -1^2 + 4 \cdot 1 + 5 = -1 + 4 + 5 = 8.
$$

Deretter bruker vi ettpunktsformelen for å bestemme likningen til tangenten: 

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - f(1) &= f'(1)(x - 1) \\
    \\
    y - 8 &= 2(x - 1) \\
    \\
    y - 8 &= 2x - 2 \\
    \\
    y &= 2x + 6.
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} b
En tredjegradsfunksjon $g$ er gitt ved 

$$
g(x) = x^3 + 4x^2 - 5x + 6
$$

Bestem likningen til tangenten i $(2, g(2))$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 23x - 26. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Bruker polynomdivisjon til å finne likningen til tangenten. Likningen er resten i polynomdivisjonen $g(x) : (x - 2)^2$

:::{figure} ./koder/oppgaver/oppgave_6/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi kan lese av fra polynomdivisjonen at resten er $23x - 26$. Dermed er likningen til tangenten

$$
y = 23x - 26. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En tredjegradsfunksjon $h$ er gitt ved 

$$
h(x) = x^3 - 5x^2 + 1
$$

Bestem likningen til tangenten i $(-1, h(-1))$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 13x + 8.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker ettpunktsformelen og den deriverte til å bestemme likningen til tangenten. Først finner vi den deriverte:

$$
h'(x) = (x^3 - 5x^2 + 1)' = 3x^2 - 10x. 
$$

Deretter regner vi ut stigningstallet til tangenten:

$$
a = h'(-1) = 3 \cdot (-1)^2 - 10 \cdot (-1) = 3 + 10 = 13.
$$

Deretter finner vi $y_1 = h(-1)$:

$$
h(-1) = (-1)^3 - 5 \cdot (-1)^2 + 1 = -1 - 5 + 1 = -5.
$$

Så setter vi alt dette inn i ettpunktsformelen og regner ut likningen til tangenten:

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - h(-1) &= h'(-1)(x - (-1)) \\
    \\
    y - (-5) &= 13(x + 1) \\
    \\
    y + 5 &= 13x + 13 \\
    \\
    y &= 13x + 8.
\end{align*}    

::::

:::::::::::::


:::::::::::::{tab-item} d
En tredjegradsfunksjon $p$ er gitt ved 

$$
p(x) = x^4 - 16x + 2. 
$$

Bestem likningen til tangenten i $(0, p(0))$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -16x + 2.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjonen $p(x) : (x - 0)^2$ for å finne likningen til tangenten. Resten i polynomdivisjonen gir likningen til tangenten:

:::{figure} ./koder/oppgaver/oppgave_6/d.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Resten i polynomdivisjonen er $-16x + 2$ som betyr at likningen til tangenten er

$$
y = -16x + 2.
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---

::::::::::::::{admonition} Repetisjon: Identiteter
---
class: summary, dropdown
---
En **identitet** er en likning som er sann for **alle** verdier av variabelen i likningen. For eksempel er 

$$
x^2 - x - 6 = (x - 3)(x + 2)
$$

en identitet siden venstre og høyre side er like for **alle** verdier av $x$. 

Strategier vi kan bruke i oppgaver av denne typen er:
* Prøve å bestemme røttene til polynomet direkte.
* Bruk polynomdivisjon til å finne kvotienten dersom det ikke er noen rest.
::::::::::::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ og $b$ slik at likningen er en identitet:

$$
x^2 - 3x - 10 = (x - a)(x - b).
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = -2 \and b = 5 \or a = 5 \and b = -2.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Likningen er en identitet dersom den er tilfredsstilt for alle verdier av $x$. I praksis trenger vi bare å nullpunktsfaktorisere andregradspolynomet 

$$
x^2 - 3x - 10,
$$ 

og lese av verdiene til $a$ og $b$. Vi bruker $abc$-formelen som gir

$$
x = \dfrac{-(-3) \pm \sqrt{(-3)^2 - 4 \cdot 1 \cdot (-10)}}{2 \cdot 1} = \dfrac{3 \pm \sqrt{49}}{2} = \dfrac{3 \pm 7}{2}
$$

som gir 

$$
x = -2 \or x = 5.
$$

Dette betyr at 

$$
x^3 - 3x - 10 = (x + 2)(x - 5).
$$

Sammenlikner vi med 

$$
x^3 - 3x - 10 = (x - a)(x - b).
$$

betyr dette at vi får to muligheter:

$$
a = -2 \and b = 5 \or a = 5 \and b = -2.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$, $b$ og $c$ slik at likningen er en identitet.

$$
x^3 - 2x^2 - 5x + 6 = (x - 1)(ax^2 + bx + c)
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = 1 \and b = -1 \and c = -6. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme $a$, $b$ og $c$ slik at likningen er tilfredsstilt for *alle* verdier av $x$, kan vi gå frem ved å faktorisere tredjegradspolynomet 

$$
x^3 - 2x^2 - 5x + 6 = (x - 1)(ax^2 + bx + c)
$$

der vi må lete etter et andregradspolynom slik at likningen er oppfylt. Dette kan vi gjøre ved å utføre polynomdivisjon av tredjegradspolynomet med $(x - 1)$:

:::{figure} ./koder/oppgaver/oppgave_7/b.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra polynomdivisjonen kan vi lese av at koeffisientene til andregradspolynomet er

$$
a = 1 \and b = -1 \and c = -6. 
$$

Med disse koeffisientene, må likningen være en identitet.
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $a$ og $b$ slik at likningen er en identitet. 

$$
x^3 + x^2 - 5x + 3 = (ax + b)(x^2 + 2x - 3). 
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = 1 \and b = -1. 
$$
::::



::::{admonition} Løsning
---
class: solution, dropdown
---
Vi vet at vi mangler en lineær faktor, som vi kan bestemme ved å utføre polynomdivisjonen

$$
(x^3 + x^2 - 5x + 3) : (x^2 + 2x - 3). 
$$

Vi fyrer løs:

:::{figure} ./koder/oppgaver/oppgave_7/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at 

$$
x^3 + x^2 - 5x + 3 = (x - 1)(x^2 + 2x - 3)
$$

Vi har dermed funnet at likningen er en identitet hvis

$$
a = 1 \and b = -1. 
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
En likning er gitt ved 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x + a)(x - b). 
$$

Bestem $a$ og $b$ slik at likningen blir en identitet.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = 2 \and b = 6 \or a = -6 \and b = -2.
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
Først merker vi oss at hvis vi utfører polynomdivisjonen 

$$
(x^3 - 5x^2 - 8x + 12) : (x - 1)
$$

så får vi et andregradspolynom som vi videre kan nullpunktsfaktorisere for å bestemme $a$ og $b$. Vi kjører på: 

:::{figure} ./koder/oppgaver/oppgave_7/d.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra polynomdivisjonen kan vi konkludere at 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x^2 - 4x - 12). 
$$

Nå må vi nullpunktsfaktorisere andregradspolynomet som vi kan oppnå ved å bestemme røttene med $abc$-formelen:

\begin{align*}
    x &= \dfrac{-(-4) \pm \sqrt{(-4)^2 - 4\cdot 1 \cdot (-12)}}{2 \cdot 1} = \dfrac{4 \pm \sqrt{16 + 48}}{2} \\
    \\
    &= \dfrac{4 \pm \sqrt{64}}{2} = \dfrac{4 \pm 8}{2} \\
    \\
    & = 2 \pm 4
\end{align*}

som gir 

$$
x = -2 \or x = 6.
$$

Dermed er 

$$
x^2 - 4x - 12 = (x + 2)(x - 6),
$$

og følgelig er

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x + 2)(x - 6).
$$

Ved å sammenlikne med 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x + a)(x - b),
$$

kan vi derfor konkludere at vi har to muligheter:

$$
a = 2 \and b = 6 \or a = -6 \and b = -2.
$$

::::

:::::::::::::

::::::::::::::

:::::::::::::::


---

:::::::::::::::{admonition} Oppgave 8
---
class: problem-level-2
---

::::::::::::::{admonition} Repetisjon: Nullpunktene til polynomer
---
class: summary, dropdown
---
* Alle heltallige røtter vil alltid være en faktor i konstantleddet til polynomet.
* Hvis $x = r$ er en rot til polynomet $f(x)$, vil $(x - r)$ dele $f(x)$ slik at polynomdivisjonen $f(x) : (x - r)$ har null i rest.

::::::::::::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen 

$$
x^3 - x^2 - 9x + 9 = 0.
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \or x = 1 \or x = 3.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
La 

$$
f(x) = x^3 - x^2 - 9x + 9.
$$

Heltallige løsninger til likningen må være en faktor i konstantleddet. Dette betyr at hvis det eksisterer heltallige løsninger $x$, så må disse være en del av mengden

$$
x \in \{\pm 1, \pm 3, \pm 9\}. 
$$

Vi prøver først ut $x = 1$: 

$$
f(1) = 1^3 - 1^2 - 9 \cdot 1 + 9 = 1 - 1 - 9 + 9 = 0.
$$

Dermed er $x = 1$ en løsning. Det betyr at $(x - 1)$ er en faktor i tredjegradspolynomet som betyr at $(x - 1) \, | \, f(x)$. Vi utfører derfor polynomdivisjonen $f(x) : (x - 1)$:


:::{figure} ./koder/oppgaver/oppgave_8/a.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Resultatet av polynomdivisjonen forteller oss at 

$$
f(x) = (x - 1)(x^2 - 9). 
$$

For å bestemme de resterende røttene til polynomet, løser vi likningen 

$$
x^2 - 9 = 0 \liff x = \pm 3.
$$

Dermed er løsningene til likningen:

$$
x = -3 \or x = 1 \or x = 3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 - 7x^2 + 14x - 8.
$$

Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 1 \or x= 2 \or x = 4.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å lete etter mulige heltallige røtter. Vi kan merke oss at konstantleddet er $-8$ og at alle heltallige røtter til tredjegradspolynomet må være en faktor i konstantleddet. Dette betyr at hvis en rot $x$ er et heltall, så må

$$
x \in \{\pm 1, \pm 2, \pm 4, \pm 8\}. 
$$


Vi prøver ut $x = 1$: 

$$
f(1) = 1^3 - 7 \cdot 1^2 + 14 \cdot 1 - 8 = 1 - 7 + 14 - 8 = 0.
$$

Dermed vet vi at $x = 1$ er en rot som betyr at $(x - 1)$ er en faktor i tredjegradspolynomet. Vi utfører derfor polynomdivisjonen $f(x) : (x - 1)$:

:::{figure} ./koder/oppgaver/oppgave_8/b.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra resultatet av polynomdivisjonen kan vi skrive at 

$$
f(x) = (x - 1)(x^2 - 6x + 8).
$$

For å bestemme de resterende røttene til polynomet, løser vi likningen

$$
x^2 - 6x + 8 = 0,
$$

som med $abc$-formelen gir 

$$
x = \dfrac{6 \pm \sqrt{36 - 32}}{2} = \dfrac{6 \pm 2}{2} = 3 \pm 1.
$$

Altså er løsningene 

$$
x = 2 \or x = 4.
$$

Det betyr at 

$$
f(x) = (x - 1)(x - 2)(x - 4).
$$

som til slutt gir oss at grafen til $f$ skjærer $x$-aksen i punktene

$$
x = 1 \or x = 2 \or x = 4.
$$

::::

:::::::::::::


:::::::::::::{tab-item} c
Et tredjegradspolynom er gitt ved 

$$
x^3 - x^2 - 5x - 3. 
$$

Bestem røttene til polynomet.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \or x = 3.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
La 

$$
f(x) = x^3 - x^2 - 5x - 3.
$$ 

Vi starter med å liste opp alle mulige heltallige røtter $x$ vi kan få, som er alle verdier av $x$ som kan dele konstantleddet $-3$. Dette kan bare være 

$$
x \in \{\pm 1, \pm 3\}.
$$

Vi sjekker som om noen av mulighetene medfører at $f(x) = 0$. 

$x = 1$: 
: $f(1) = 1^3 - 1^2 - 5\cdot 1 - 3 = 1 - 1 - 5 - 3 = -8$. 

$x = -1$:
: $f(-1) = (-1)^3 - (-1)^2 - 5\cdot (-1) - 3 = -1 - 1 + 5 - 3 = 0$. 

Dermed er $x = - 1$ en rot. Dette betyr at $f(x)$ er delelig med $(x + 1)$ som betyr at $f(x) : (x + 1)$ gir oss et andregradspolynom:

:::{figure} ./koder/oppgaver/oppgave_8/c.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Vi går videre med å finne røttene til andregradspolynomet, som vi kan oppnå med $abc$-formelen:

$$
x = \dfrac{-(-2) \pm \sqrt{(-2)^2 - 4 \cdot 1 \cdot (-3)}}{2 \cdot 1} = \dfrac{2 \pm \sqrt{4 + 12}}{2} = \dfrac{2 \pm 4}{2} = 1 \pm 2.
$$

som gir at røttene til andregradspolynomet er

$$
x = -1 \or x = 3.
$$

Siden $x = -1$ også var en rot for tredjegradspolynomet, betyr det at vi nå har funnet alle røttene til tredjegradspolynomet også.
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 9
---
class: problem-level-2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} b
Løs ulikheten 

$$
(x - 4)^2 (x + 2) > 0.
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -2, \to \rangle \setminus \{4\}.
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten 

$$
x^3 + 4x^2 + x - 6 > 0. 
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -3, -2 \rangle \cup \langle 1, \to \rangle.
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
En tredjegradsfunksjon er gitt ved 

$$
f(x) = -x^3 - 3x^2 + 4.
$$

Løs ulikheten $f(x) > 0$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle \gets, 1 \rangle \setminus \{-2\}. 
$$
::::

:::::::::::::



::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 10
---
class: problem-level-2
---

::::::::::::::{admonition} Repetisjon: Sammenheng mellom $f$ og $f'$
---
class: summary, dropdown
---
For en polynomfunksjon $f$ gjelder følgende:
* Hvis $f$ er en polynomfunksjon $f$ av grad $n$, er $f'$ en polynomfunksjon av grad $n - 1$.
* Ekstremalpunktene til $f$ er nullpunktene til $f'$.
* Grafen til $f'$ skjærer $x$-aksen der grafen til $f$ har topp- eller bunnpunkter.

::::::::::::::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
{numref}`fig-polynomer-oppgavesamling-oppgave-10-a` viser grafen til en andregradsfunksjon $f$. 

Lag en skisse av grafen til $f'$. 


:::{figure} ./figurer/oppgaver/oppgave_10/a.svg
---
name: fig-polynomer-oppgavesamling-oppgave-10-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_10/a_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $f'$.
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
{numref}`fig-polynomer-oppgavesamling-oppgave-10-b` viser grafen til en tredjegradsfunksjon $g$. 

Lag en skisse av grafen til $g'$. 


:::{figure} ./figurer/oppgaver/oppgave_10/b.svg
---
name: fig-polynomer-oppgavesamling-oppgave-10-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $g$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_10/b_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::
viser en skisse av grafen til $g'$.
::::


:::::::::::::


:::::::::::::{tab-item} c
{numref}`fig-polynomer-oppgavesamling-oppgave-10-c` viser grafen til en tredjegradsfunksjon $h$. 

Lag en skisse av grafen til $h'$. 


:::{figure} ./figurer/oppgaver/oppgave_10/c.svg
---
name: fig-polynomer-oppgavesamling-oppgave-10-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $h$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_10/c_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::
viser en skisse av grafen til $h'$.
::::


:::::::::::::

::::::::::::::


:::::::::::::::



:::::::::::::::{admonition} Oppgave 11
---
class: problem-level-2
---

::::::::::::::{admonition} Repetisjon: Optimering
---
class: summary, dropdown
---
Optimering handler om å finne maksimums- eller minimumsverdier til en funksjon.

Hvis en $f$ er en polynomfunksjon, vil maksimums- eller minimumsverdien til $f$ være i et ekstremalpunkt. Vi bør derfor lete etter punkter hvor $f'(x) = 0$ når vi ønsker å maksimere eller minimere en polynomfunksjon $f$.
::::::::::::::



En tredjegradsfunksjon er gitt ved 

$$
f(x) = x^3 - 32x, \quad x \in \left[0, 4 \sqrt{2} \, \right]. 
$$

En trekant har hjørnene $(0, 0)$, $(2, 0)$ og $(2, f(2))$. Se {numref}`fig-polynomer-oppgavesamling-oppgave-11`.


:::{figure} ./figurer/oppgaver/oppgave_11/graf.svg
---
name: fig-polynomer-oppgavesamling-oppgave-11
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $f$ og en trekant med hjørner i $(0, 0)$, $(2, 0)$ og $(2, f(2))$. 
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet $A$ til trekanten.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
A = 56. 
$$
:::



:::{admonition} Fasit
---
class: solution, dropdown
---
Siden $f(x) < 0$ for alle $x \in \left[0, 4\sqrt{2} \right]$, vil høyden i trekanten nødvendigvis være $|f(x)|$ for en gitt grunnlinje $x$. Dette betyr at arealet av trekanten er 

$$
A = \dfrac{1}{2} \cdot 2 \cdot |f(2)| = |f(2)|. 
$$

Da gjenstår det bare å regne ut $f(2)$ som gir:

$$
f(2) = 2^3 - 32 \cdot 2 = 8 - 64 = -56.
$$

Dermed er 

$$
A = |f(2)| = |-56| = 56.
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
En tilsvarende trekant har hjørner i punktene $(0, 0)$, $(k, 0)$ og $(k, f(k))$. 

Bestem arealet $A(k)$ til trekanten.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(k) = 16k^2 - \dfrac{1}{2}k^4. 
$$
:::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $k$ slik at arealet til trekanten er størst mulig. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
k = 4
$$
:::

:::::::::::::

::::::::::::::


:::::::::::::::


:::::::::::::::{admonition} Oppgave 12
---
class: problem-level-2
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
{numref}`fig-polynomer-oppgavesamling-oppgave-12-a` viser grafen til en lineær funksjon $f'$. 

Grafen til $f$ skjærer $x$-aksen i $x = 1$ og $x = 5$.  

Lag en skisse av grafen til $f$. 

:::{figure} ./figurer/oppgaver/oppgave_12/a.svg
---
name: fig-polynomer-oppgavesamling-oppgave-12-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en lineær funksjon $f'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_12/a_løsning.svg
---
width: 100%
class: no-click, 
---
viser en skisse av grafen til $f$. 
:::

::::


:::::::::::::

:::::::::::::{tab-item} b
{numref}`fig-polynomer-oppgavesamling-oppgave-12-b` viser grafen til en andregradsfunksjon $g'$. 

Lag en skisse av grafen til $g$. 

:::{figure} ./figurer/oppgaver/oppgave_12/b.svg
---
name: fig-polynomer-oppgavesamling-oppgave-12-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $g'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_12/b_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $g$. 
:::

::::


:::::::::::::

:::::::::::::{tab-item} c
{numref}`fig-polynomer-oppgavesamling-oppgave-12-c` viser grafen til en andregradsfunksjon $h'$. 

Funksjonen $h$ tilfredsstiller $h(-2) = h(1) = 0$. 

Lag en skisse av grafen til $h$. 

:::{figure} ./figurer/oppgaver/oppgave_12/c.svg
---
name: fig-polynomer-oppgavesamling-oppgave-12-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $h'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_12/c_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $h$. 
:::

::::


:::::::::::::

:::::::::::::{tab-item} d
{numref}`fig-polynomer-oppgavesamling-oppgave-12-d` viser grafen til en tredjegradsfunksjon $p'$. Om $p$ får du vite at:
* $p(x)$ er et polynom med to negative røtter.
* Grafen til $p$ skjærer $y$-aksen i et punkt $(0, y)$ der $y > 0$. 

Lag en skisse av grafen til $p$. 

:::{figure} ./figurer/oppgaver/oppgave_12/d.svg
---
name: fig-polynomer-oppgavesamling-oppgave-12-d
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $p'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_12/d_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $p$. 
:::

::::


:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 13
---
class: problem-level-3
---
En sylinder med radius $r$ og høyde $h$ er vist i {numref}`fig-polynomer-oppgavesamling-oppgave-13-sylinder`.

:::{figure} ./figurer/oppgaver/oppgave_13/figur.svg
---
name: fig-polynomer-oppgavesamling-oppgave-13-sylinder
width: 80%
class: no-click, adaptive-figure
---
viser en sylinder med radius $r$ og høyde $h$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en formel for overflatearealet $A$ til sylinderen. 


::::{admonition} Hint
---
class: dropdown, hints
---
For å bestemme overflatearealet, kan du dele det opp i tre deler:
1. Topp
2. Bunn
3. Sideflate

For å bestemme en formel for arealet av sideflaten, kan du tenke deg at du klipper opp sylinderen og bretter den ut. Hvilken form får du da? Kan du bestemme arealet av denne formen? 
::::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A = 2\pi r^2 + 2\pi rh.
$$
::::


::::{admonition} Løsning
---
class: answer, dropdown
---
Først kan vi merke oss at toppen og bunnen er begge to sirkler med radius $r$ som gir et areal på $\pi r^2$ hver. Tenker vi oss at vi tar av lokkene (toppen og bunnen), klipper opp sylinderen og bretter den ut, får vi et rektangel som har sidelengder $h$ og $2\pi r$ fordi dette er omkretsen til et tverrsnitt av sylinderen. Arealet av dette utbrettede rektangelet er $2 \pi r h$. Dermed er overflatearealet til sylinderen: 


$$
A = 2\pi r^2 + 2\pi rh.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Du skal lage en sylinder der du har materiale til å dekke et overflateareal på $24 \pi$.

Bestem en modell $V(r)$ for volumet av sylinderen.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
V(r) = -\pi r^3 + 12\pi r. 
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Først merker vi oss at arealet er 

$$
A = 2\pi r^2 + 2\pi rh \and A = 24\pi. 
$$

Dermed vil vi få at 

$$
24\pi = 2\pi r^2 + 2\pi rh \liff 12 = r^2 + rh \liff h = \dfrac{12 - r^2}{r}.
$$

I tillegg kan vi uttrykke volumet som 

$$
V = \pi r^2 h. 
$$

Setter vi inn uttrykket for $h$, får vi en funksjon som kun inneholder $r$ som variabel:

$$
V(r) = \pi r^2 \left( \dfrac{12 - r^2}{r} \right) = \pi r(12 - r^2) = -\pi r^3 + 12\pi r.
$$

Dermed er volumet $V(r)$ gitt ved 

$$
V(r) = -\pi r^3 + 12\pi r. 
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $r$ slik at volumet blir størst mulig. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
r = 2. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme $r$ slik at volumet blir størst mulig, løser vi likningen $V'(r) = 0$:

$$
V'(r) = (-\pi r^3 + 12\pi r)' = -3\pi r^2 + 12\pi = 0 \liff r^2 = 4 \limplies r = 2.
$$

der vi har forkastet $r = -2$ som en mulig løsning fordi radien $r > 0$. Dermed vil volumet bli størst mulig dersom

$$
r = 2. 
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 14
---
class: problem-level-3
---
En funksjon $f$ er en tredjegradsfunksjon. 

Under skal du vurdere ulike påstander og vurdere om de er sanne eller usanne.

::::::::::::::{tab-set}
---
class: tab-parts
---
:::::::::::::{tab-item} Påstand 1
$f'$ er en andregradsfunksjon.

::::{admonition} Fasit
---
class: answer, dropdown
---
Påstanden er sann.
::::

:::::::::::::



:::::::::::::{tab-item} Påstand 2
En linje $y = ax + b$ der $a, b \in \mathbb{R}$ vil alltid skjære grafen til $f$ i *minst* ett punkt.

::::{admonition} Fasit
---
class: answer, dropdown
---
Påstanden er sann.
::::

:::::::::::::


:::::::::::::{tab-item} Påstand 3
Grafen til $f'$ har et ekstremalpunkt i $x = 3$. Da er $f'(1) = f'(5)$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
Påstanden er sann.
::::

:::::::::::::

::::::::::::::


:::::::::::::::



