:::::::::::::::{admonition} Oppgave 6
---
class: check
---
En elev jobber med en funksjon $f$. Grafen til $f$ er vist i figuren nedenfor. 

:::{figure} ./figurer/del_1/oppgave_6/figur.svg
---
width: 60%
class: no-click
---
:::

Eleven har skrevet programmet nedenfor.

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
class: no-click
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

