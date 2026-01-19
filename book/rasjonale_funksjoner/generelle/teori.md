# Generelle rasjonale funksjoner


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne bestemme horisontale eller skrå asymptoter til en rasjonal funksjon. 
* Kunne bestemme nullpunktene til en rasjonal funksjon. 
* Kunne bestemme vertikale asymptoter til en rasjonal funksjon.
* Kunne lage fortegnslinjer og skissere grafen til en rasjonal funksjon, å bruke dette til å løse rasjonale ulikheter.
:::::



Når vi jobbet med lineære-over-lineære rasjonale funksjoner fant vi at funksjonen alltid hadde en horisontal asymptote, en vertikal asymptote og et nullpunkt. Men for rasjonale funksjoner generelt sett, vil antall nullpunkter og vertikale asymptoter variere, og det finnes også rasjonale funksjoner som ikke har noen av delene. Men disse tre egenskapene er likevel de mest sentrale egenskapene for rasjonale funksjoner.


:::::::::::::::{summary} Sentrale egenskaper ved rasjonale funksjoner
For rasjonale funksjoner, er de mest sentrale egenskapene:
* **Nullpunkter**
* **Horisontale og skrå asymptoter**
* **Vertikale asymptoter**

:::::::::::::::


Målet vårt er å utvikle verktøy for å avgjøre hvilke egenskaper en rasjonal funksjon har. Men først tar vi et eksempel som illustrerer hvor variert antallet av disse egenskapene kan være – for de må slett ikke ha vertikale asymptoter, nullpunkter eller horisontale asymptoter i det hele tatt. Mangfoldet av egenskaper er for mange til å vise *alle* tilfeller, men dette vil gi oss en idé om variasjonen vi kan møte på. Deretter skal vi se på hvordan vi kan avgjøre hvilke egenskaper en rasjonal funksjon har.

:::::::::::::::{example} Eksempel 1
Nedenfor vises fire eksempler på rasjonale funksjoner med ulike egenskaper. 

Det *ikke* meningen at du skal forstå *hvorfor* grafene ser ut som de gjør enda, men få et inntrykk av hvor stort mangfold rasjonale funksjoner kan ha.

::::::::::::::{grid} 1 1 2 2
---
gutter: 2
---
:::::::::::::{grid-item-card}
$$f(x) = \dfrac{(x - 2)(x + 3)}{x^2 - 1}$$
^^^

:::{plot}
function: (x - 2) * (x + 3) / (x**2 - 1)
vline: 1
vline: -1
hline: 1
point: (-3, 0)
point: (2, 0) 
xmin: -10
xmax: 10
ticks: off
fontsize: 25

Her har $f$ en horisontal asymptote $y = 1$, to vertikale asymptoter med likningene $x = \pm 1$, og to nullpunkter $x = -3$ og $x = 2$.
:::

:::::::::::::


:::::::::::::{grid-item-card}
$$f(x) = \dfrac{x^2 - 4}{x - 1}$$
^^^


:::{plot}
function: (x**2 - 4) / (x - 1)
vline: 1
line: 1, 1
point: (-2, 0)
point: (2, 0)
xmin: -8
xmax: 8
ymax: 10
ymin: -10
ticks: off
fontsize: 25

Grafen har to nullpunkter $x = \pm 2$, en vertikal asymptote i $x = 1$ og en **skrå** asymptote $y = x + 1$. Grafen til $f$ nærmer seg altså en lineær funksjon når $|x|$ blir stor.
:::

:::::::::::::


:::::::::::::{grid-item-card}
$$f(x) = \dfrac{1}{x - 2}$$
^^^


:::{plot}
function: 1 / (x - 2)
vline: 2
hline: 0
xmin: -8
xmax: 8
ymax: 10
ymin: -10 
ticks: off
fontsize: 25

Grafen har en vertikal asymptote i $x = 2$, men ingen nullpunkter. Grafen til $f$ har en horisontal asymptote $y = 0$.
:::



:::::::::::::


:::::::::::::{grid-item-card} 
$$f(x) = \dfrac{x - 1}{x^2 + 1}$$
^^^


:::{plot}
function: (x - 1) / (x**2 + 1)
hline: 0
xmin: -8
xmax: 8
ymax: 3
ymin: -3
ticks: off
fontsize: 25
point: (1, 0) 

Grafen har et nullpunkt i $x = 1$ og en horisontal asymptote $y = 0$. Grafen har ingen vertikale asymptoter.
:::


:::::::::::::


::::::::::::::



:::::::::::::::



---



## Skrå– og horisontale asymptoter

For å bestemme likningene til eventuelle horisontale eller skrå asymptoter til en rasjonal funksjon, utfører vi polynomdivisjon og leser av **kvotienten**. Dette vil være likningen til den horisontale eller skrå asymptoten.

:::::::::::::::{summary} Skrå– og horisontale asymptoter
La $f$ være en rasjonal funksjon $f(x) = \dfrac{P(x)}{Q(x)}$, der $P(x)$ og $Q(x)$ er polynomer. Likningen til den skrå– eller horisontale asymptoten til $f$ er gitt ved kvotienten $y = K(x)$ når vi utfører polynomdivisjonen $P(x) : Q(x)$.


Da får vi følgende mulige utfall:
* Hvis tellergraden er én større enn nevnergraden, vil $K(x)$ være et førstgradspolynom og vi får en **skrå asymptote**.
* Hvis tellergraden er lik nevnergradenm vil $K(x)$ være en konstant og vi får en **horisontal asymptote**.
* Hvis tellergraden er mindre enn nevnergraden, vil kvotienten være $0$ og vi har en horisontal asymptote gitt ved likningen $y = 0$.
:::::::::::::::



---

La oss først se på et eksempel der funksjonen har en horisontal asymptote:

:::::::::::::::{example} Eksempel 2
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{2x^2 + 3}{x^2 - 4}
$$

Bestem likningen til en eventuell skrå– eller horisontal asymptote til $f$.

::::{solution}
---
dropdown: 0
---
Vi utfører polynomdivisjon for å bestemme kvotienten til brøken:

:::{polydiv}
---
p: 2x^2 + 3
q: x^2 - 4
width: 70%
---
:::

Vi kan se at kvoitenten er $K(x) = 2$, som betyr at likningen til den horisontale asymptoten til $f$ er

$$
y = 2
$$


::::
:::::::::::::::


---


Men hva skjer dersom nevnergraden til funksjonen er større enn tellergraden? Da vil vi ikke kunne dele noe mer siden telleren har lavere grad enn nevneren. Da betyr det at kvotienten er $0$ allerede, og dette blir likningen til den horisontale asymptoten. La oss se på et eksempel på dette:

:::::::::::::::{example} Eksempel 3
En rasjonal funksjon $f$ er gitt ved

$$
f(x) = \dfrac{x + 1}{x^2 + 2}
$$

Bestem likningen til en eventuell skrå– eller horisontal asymptote til $f$.

::::{solution}
---
dropdown: 0
---
Vi har at nevnergraden er større enn tellergraden, som betyr at 

$$
\dfrac{x + 1}{x^2 + 2} = 0 + \dfrac{x + 1}{x^2 + 2}
$$

der $x + 1$ er resten i polynomdivisjon allerede. Dermed er kvotienten $K(x) = 0$, som betyr at likningen til den horisontale asymptoten til $f$ er

$$
y = 0
$$

::::

:::::::::::::::


---


Så tar vi det siste tilfellet hvor tellergraden er én større enn nevnergraden slik at grafen til $f$ har en skrå asymptote.


---



:::::::::::::::{example} Eksempel 4
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 - 4}{x + 1}
$$

Bestem likningen til en eventuell skrå– eller horisontal asymptote til $f$.

::::{solution}
---
dropdown: 0
---
Vi utfører polynomdivisjon for å bestemme kvotienten til brøken:


:::{polydiv}
---
p: x^2 - 4
q: x + 1
width: 70%
---
:::

Vi ser at kvotienten er $K(x) = x - 1$. Dermed er likningen til den skrå asymptoten

$$
y = x - 1.
$$


::::
:::::::::::::::

