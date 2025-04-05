:::::::::::::::{admonition} Oppgave 4
---
class: check
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 - 1}{x^2 - 2x + 1}
$$

Avgjør hvilken graf som tilhører $f$.

Husk å forklare hvordan du kommer fram til svaret ditt.


:::{figure} ./figurer/del_1/oppgave_4/merged_figure.svg
---
width: 100%
class: no-click
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

der vi bruke konjugatsetningen i tellerpolynomet og 2.kvadratsetning i nevnerpolynomet. Ettersom vi nå har forkortet bort alle felles faktorer, kan vi bestemme $f$ sine nullpunkter og asymptoter.

Fra tellerpolynomet i det fortkortede uttrykket får vi at 

$$
f(x) = 0 \liff x + 1 = 0 \liff x = -1
$$

som betyr at $f$ har et nullpunkt i $x = -1$. Fra nevnerpolynomet får vi at 

$$
x - 1 = 0  \liff x = 1
$$

som betyr at $f$ har en vertikal asymptote i $x = 1$. Siden ledene koeffisient for teller og nevnerpolynomet er $1$ og polynomeme er av samme grad, følger det at den horisontale asymptoten er $y = 1$.

Graf $B$ er den eneste grafen som samtidig har
* Har et nullpunkt for $x < 0$
* en vertikal asymptote når $x > 0$
* En horisontal asymptote der $y > 0$.

Dermed må graf B gære grafen til $f$. 

:::::

:::::::::::::::
