# Oppgaver: <br> Programmering av lineære likninger


::::{admonition} Oppgave 1
---
class: problem-level-1
---
Ta quizen!

:::{raw} html
---
file: quiz/quiz_1/quiz_1.html
---
:::

::::

---

:::::{admonition} Oppgave 2
---
class: problem-level-1
---

````{tab-set} 
---
class: tabs-parts
---
```{tab-item} a
Les programmet og forutsi hva det printer ut. 

Skriv inn hypotesen din og sjekk svaret ditt!
```

```{tab-item} b
Juster programmet og bruk det til å finne nullpunktet til

$$
g(x) = x + 5
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
emphasize-lines: 2
---
def g(x):
    return x + 5

for x in range(-10, 11):
    if g(x) == 0:
        print(x)

:::
::::
```

```{tab-item} c
Juster programmet og bruk det til å finne løsningen av likningen

$$
g(x) = 2
$$

:::{admonition} Hint
---
class: dropdown, hints
---
Siden man bruker `f(x) == 0`{l=python} for å sjekke om `f(x)`{l=python} er lik $0$, kan du kanskje tenke deg til hva du må endre på for å sjekke om $g(x) = 2$? 
::: 

::::{admonition} Fasit
---
class: answer, dropdown
---

**Programkode**:
:::{code-block} python
---
linenos: true
emphasize-lines: 5
---
def g(x):
    return x + 5

for x in range(-10, 11):
    if g(x) == 2:           # <-- er g(x) lik 2?
        print(x)
:::

**Utskrift**:
:::{code-block} console
-3
:::

**Tolkning**: <br>
Løsningen av likningen $g(x) = 2$ er $x = -3$.
::::
```

```{tab-item} d
Juster programmet og bruke det til å finne skjæringspunktet mellom grafen til $g$ og linja $y = -1$.


::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**: 

:::{code-block} python
---
linenos: true
emphasize-lines: 5, 6
---
def g(x):
    return x + 5

for x in range(-10, 11):
    if g(x) == -1:          # <-- sjekker om g(x) er -1
        print(x, g(x))      # <-- skriver ut x og g(x)
:::

**Utskrift**:
:::{code-block} console
-6 -1
:::

**Tolkning**: <br>
Grafen til $g$ skjærer linja $y = -1$ i punktet $(-6, -1)$.
::::
```
````

:::{raw} html
---
file: ./interaktiv_kode/oppgave_2.html
---
:::
:::::

---


:::::{admonition} Oppgave 3
---
class: problem-level-2
---
Under vises to programkoder som bruker funksjonene

$$
f(x) = 2x + 3 \quad \text{og} \quad g(x) = -3x + 8
$$




`````{tab-set}
````{tab-item} a
Les de to programmene nøye og forutsi hva de kommer til å skrive ut.

Skriv inn forutsigelsene dine under og sjekk! 
````

````{tab-item} b
1. Hvilke problemer kan du løse ved å bruke program 1? 
2. Hvilke problemer kan du løse ved å bruke program 2?
3. Kan du svare på de samme spørsmålene med både program 1 og program 2?
````

`````

`````{tab-set}
````{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/oppgave_3/program_1.html
---
:::

````

````{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/oppgave_3/program_2.html
---
:::
````

`````
:::::

---

:::::::{admonition} Oppgave 4
---
class: problem-level-2
---
Vi har fokusert på å løse likninger numerisk så langt, men det er også mulig å skrive programmer som løser likningene analytisk. Da bruker vi en form for CAS (*Computer Algebra System*). <br> I Python er det et bibliotek som heter `sympy`{l=python} som lar oss gjøre akkurat dette! 

Her skal du få en kort introduksjon til hvordan man gjøre dette!


::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Her følger tre programkoder som bruker `sympy`{l=python} til å løse likninger. For hvert av de tre programmene:

1. Les programmet prøv å finne ut hvilken likning programmet løser.
2. Forutsi hva programmet skriver ut.
3. Skriv inn hypotesen din og sjekket svaret ditt!


````{tab-set}
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/a/program_1.html
---
:::

```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/a/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/a/program_3.html
---
:::

```
````

---

::::{admonition} Fasit
---
class: answer, dropdown
---
````{tab-set}
```{tab-item} Program 1
Likning
: $2x - 4 = 0$

Løsning
: $x = 2$
```

```{tab-item} Program 2
Likning
: $2x - 3 = 5$

Løsning
: $x = 4$

```

```{tab-item} Program 3
Likning
: $3x - 6 = -2x + 1$

Løsning
: $x = \dfrac{7}{5}$

```
````
::::

:::::

:::::{tab-item} b
Fyll inn programmet for hver likning og bruk programmet til å løse likningen.

````{tab-set}
```{tab-item} Likning 1
$-3x + 12 = 0$

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/b/likning_1.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(-3 * x + 12, 0)
løsning = solve(likning)            

print(løsning)

:::
::::
```

```{tab-item} Likning 2
$2x + 5 = 0$

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/b/likning_2.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(2 * x + 5, 0)
løsning = solve(likning)            

print(løsning)

:::
::::
```

```{tab-item} Likning 3
$3x + 2 = 6$

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/b/likning_3.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(3 * x + 2, 6)
løsning = solve(likning)            

print(løsning)

:::
::::
```

```{tab-item} Likning 4
$-4x + 8 = 2x - 1$

:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/b/likning_4.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(-4 * x + 8, 2 * x - 1)
løsning = solve(likning)            

print(løsning)

:::
::::
```
````


:::{raw} html
---
file: ./interaktiv_kode/oppgave_4/b/program.html
---
:::

:::::
::::::



:::::::