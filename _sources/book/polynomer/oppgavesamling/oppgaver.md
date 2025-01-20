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
class: no-click
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
class: no-click
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
class: no-click
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
class: no-click
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
class: no-click
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

:::::::::::::


:::::::::::::{tab-item} b
Grafen til en andregradsfunksjon $g$ er vist i {numref}`fig-polynomer-oppgavesamling-oppgave-3-b`. 

Bestem $g(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_3/b.svg
---
name: fig-polynomer-oppgavesamling-oppgave-3-b
width: 80%
class: no-click
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

:::::::::::::


:::::::::::::{tab-item} c
Grafen til en andregradsfunksjon $h$ er vist i {numref}`fig-polynomer-oppgavesamling-oppgave-3-c`. 

Bestem $h(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_3/c.svg
---
name: fig-polynomer-oppgavesamling-oppgave-3-c
width: 80%
class: no-click
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

:::::::::::::


:::::::::::::{tab-item} d
En tredjegradsfunksjon $p$ er gitt ved 

$$
p(x) = x^3 + 4x^2 - 5x + 6
$$

Bestem likningen til tangenten i $(0, p(0))$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -5x + 6.
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


:::::::::::::


:::::::::::::{tab-item} d
Bestem $a$ og $b$ slik at likningen er en identitet.

$$
3x^3 + 6x^2 - 3x - 6 = (ax + b)(x^2 + 3x + 2). 
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = 3 \and b = -3.
$$
:::

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

:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten 

$$
x^3 - 5x^2 + 8x - 4 \geq 0.
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 2 \or x \leq 1. 
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 9
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
{numref}`fig-polynomer-oppgavesamling-oppgave-9-a` viser grafen til en andregradsfunksjon $f$. 

Lag en skisse av grafen til $f'$. 


:::{figure} ./figurer/oppgaver/oppgave_9/a.svg
---
name: fig-polynomer-oppgavesamling-oppgave-9-a
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_9/a_løsning.svg
---
width: 100%
class: no-click
---
viser en skisse av grafen til $f'$.
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
{numref}`fig-polynomer-oppgavesamling-oppgave-9-b` viser grafen til en tredjegradsfunksjon $g$. 

Lag en skisse av grafen til $g'$. 


:::{figure} ./figurer/oppgaver/oppgave_9/b.svg
---
name: fig-polynomer-oppgavesamling-oppgave-9-b
width: 80%
class: no-click
---
viser grafen til en tredjegradsfunksjon $g$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_9/b_løsning.svg
---
width: 100%
class: no-click
---
:::
viser en skisse av grafen til $g'$.
::::


:::::::::::::


:::::::::::::{tab-item} c
{numref}`fig-polynomer-oppgavesamling-oppgave-9-c` viser grafen til en tredjegradsfunksjon $h$. 

Lag en skisse av grafen til $h'$. 


:::{figure} ./figurer/oppgaver/oppgave_9/c.svg
---
name: fig-polynomer-oppgavesamling-oppgave-9-c
width: 80%
class: no-click
---
viser grafen til en tredjegradsfunksjon $h$.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_9/c_løsning.svg
---
width: 100%
class: no-click
---
:::
viser en skisse av grafen til $h'$.
::::


:::::::::::::

::::::::::::::


:::::::::::::::



:::::::::::::::{admonition} Oppgave 10
---
class: problem-level-2
---
En tredjegradsfunksjon er gitt ved 

$$
f(x) = x^3 - 32x, \quad x \in [0, 4 \sqrt{2} \, ]. 
$$

En trekant har hjørnene $(0, 0)$, $(2, 0)$ og $(2, f(2))$. Se {numref}`fig-polynomer-oppgavesamling-oppgave-10`.


:::{figure} ./figurer/oppgaver/oppgave_10/graf.svg
---
name: fig-polynomer-oppgavesamling-oppgave-10
width: 80%
class: no-click
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

:::::::::::::


:::::::::::::{tab-item} b
En tilsvarende trekant har hjørner i punktene $(0, 0)$, $(k, 0)$ og $(k, f(k))$. 

Bestem arealet $A(k)$ til trekanten.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(k) = -\dfrac{1}{2}k^4 + 16k^2.   
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


:::::::::::::::{admonition} Oppgave 11
---
class: problem-level-2
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
{numref}`fig-polynomer-oppgavesamling-oppgave-11-a` viser grafen til en lineær funksjon $f'$. 

Grafen til $f$ skjærer $x$-aksen i $x = 1$ og $x = 5$.  

Lag en skisse av grafen til $f$. 

:::{figure} ./figurer/oppgaver/oppgave_11/a.svg
---
name: fig-polynomer-oppgavesamling-oppgave-11-a
width: 80%
class: no-click
---
viser grafen til en lineær funksjon $f'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_11/a_løsning.svg
---
width: 100%
class: no-click
---
viser en skisse av grafen til $f$. 
:::

::::


:::::::::::::

:::::::::::::{tab-item} b
{numref}`fig-polynomer-oppgavesamling-oppgave-11-b` viser grafen til en andregradsfunksjon $g'$. 

Lag en skisse av grafen til $g$. 

:::{figure} ./figurer/oppgaver/oppgave_11/b.svg
---
name: fig-polynomer-oppgavesamling-oppgave-11-b
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $g'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_11/b_løsning.svg
---
width: 100%
class: no-click
---
viser en skisse av grafen til $g$. 
:::

::::


:::::::::::::

:::::::::::::{tab-item} c
{numref}`fig-polynomer-oppgavesamling-oppgave-11-c` viser grafen til en andregradsfunksjon $h'$. 

Funksjonen $h$ tilfredsstiller $h(-2) = h(1) = 0$. 

Lag en skisse av grafen til $h$. 

:::{figure} ./figurer/oppgaver/oppgave_11/c.svg
---
name: fig-polynomer-oppgavesamling-oppgave-11-c
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $h'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_11/c_løsning.svg
---
width: 100%
class: no-click
---
viser en skisse av grafen til $h$. 
:::

::::


:::::::::::::

:::::::::::::{tab-item} d
{numref}`fig-polynomer-oppgavesamling-oppgave-11-d` viser grafen til en tredjegradsfunksjon $p'$. Om $p$ får du vite at:
* $p(x)$ er et polynom med to negative røtter.
* Grafen til $p$ skjærer $y$-aksen i et punkt $(0, y)$ der $y > 0$. 

Lag en skisse av grafen til $p$. 

:::{figure} ./figurer/oppgaver/oppgave_11/d.svg
---
name: fig-polynomer-oppgavesamling-oppgave-11-d
width: 80%
class: no-click
---
viser grafen til en tredjegradsfunksjon $p'$. 
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_11/d_løsning.svg
---
width: 100%
class: no-click
---
viser en skisse av grafen til $p$. 
:::

::::


:::::::::::::


::::::::::::::


:::::::::::::::
