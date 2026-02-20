# Datadrevet modellering


:::{goals} Læringsmål
* Kunne bestemme en matematisk modell for å modellere en praktisk situasjon med digitale verktøy.
* Kunne bruke en modell til å belyse en praktisk situasjon med digitale verktøy
:::

## Oversikt over funksjonsklasser

Vi har til nå sett mange eksempler på matematiske funksjoner. Ulike situasjoner vil være egnet til å beskrives av ulike funksjoner.


:::::::::::::::{summary} Funksjonsklasser

::::{grid} 1 1 2 3
---
gutter: 2
---
:::{grid-item-card}
Lineære funksjoner
^^^
:::{plot}
width: 100%
function: 2*x + 1
ticks: off
fontsize: 26
lw: 3
:::

:::

:::{grid-item-card}
Andregradsfunksjoner
^^^
:::{plot}
width: 100%
function: (x - 1)**2 - 4
ticks: off
fontsize: 26
lw: 3
:::

:::

:::{grid-item-card}
Polynomfunksjoner
^^^
:::{plot}
function: 0.25 * (x + 1)**2 * (x - 2) 
ticks: off
fontsize: 26
lw: 3
:::

:::

:::{grid-item-card}
Rasjonale funksjoner
^^^
:::{plot}
function: (2*x - 4) / (x - 1)
vline: 1, dashed, red
hline: 2, dashed, red
point: (2, 0)
ticks: off
fontsize: 26 
lw: 3
ymax: 10
:::

:::


:::{grid-item-card}
Eksponentialfunksjoner
^^^
:::{plot}
function: 6 * 0.6**x, blue
function: 6 * 1.2**x, red
ticks: off
fontsize: 26  
lw: 3
ymax: 12
ymin: -1
xmax: 10
xmin: -10
:::

:::


:::{grid-item-card}
Potensfunksjoner
^^^
:::{plot}
function: x**1.5, blue
function: x**0.5, red
function: 1/x**2, orange
ticks: off
fontsize: 26 
lw: 3
xmin: -0.5
ymin: -0.5
xmax: 3
ymax: 3
:::

:::
::::


:::::::::::::::


## Definisjonsmengde og verdimengde
I praktiske situasjoner, så avgrenser vi ofte hvor funksjonen kan brukes. Selv om funsjonsuttrykk $f(x)$ kan gi mening for alle verdier av $x$, kan det hende det ikke mening å bruke alle mulige verdier for $x$ en praktisk situasjon. 

:::::::::::::::{example} Eksempel 1
Når man bruker en el-sparkesykkel fra Voi, så koster det 10 kr å låse opp sparkesykkelen. Deretter koster det 3 kr per minutt. Et funksjonsuttrykk som beskriver hvor mange kr $f(x)$ vi må betale for å bruke sparkesykkelen i $x$ minutter, er da 

$$
f(x) = 3x + 10
$$

Vi kan ikke kjøre sparkesykkelen i negative minutter, så derfor må $x \geq 0$. Men samtidig så setter de en grense på hvor lenge du kan leie sparkesykkelen, som gjerne er 45 minutter. Derfor må også $x \leq 45$. 

Men da er $f(x)$ bare gyldig når $x \in [0, 45]$. 


:::::::::::::::


De verdiene for $x$ som en funksjon er gyldig for kaller vi for **definisjonsmengden** til funksjonen. De verdiene som $f(x)$ da får, kaller vi for **verdimengden** til funksjonen.



:::::::::::::::{summary} Definisjonsmengde og verdimengde
For en funksjon $f$ kaller vi 

* **Definisjonsmengden** til $f$ for $D_f$ og den består av alle $x$-verdier der $f(x)$ er gyldig.
* **Verdimengden** til $f$ for $V_f$ og den består av alle $f(x)$-verdier der $x$ er i definisjonsmengden til $f$.



:::{plot}
xmin: -2
ymin: -2
ymax: 4
width: 70%
function: 0.125 * (x - 1) * (x - 3)**2 + 1, [1, 5], f, blue
function-endpoints: true
ticks: off
hline: 0, 1, 5, solid, red
vline: 0, 1, 3, solid, red
vline: 1, 0, f(1), dashed, gray
vline: 5, 0, f(5), dashed, gray
hline: f(1), 0, 1, dashed, gray
hline: f(5), 0, 5, dashed, gray
bar: (1, -0.5), 5 - 1, h
text: 0.5 * (5 + 1), -0.5, "$D_f$", bottom-center
bar: (-0.5, 1), f(5) - f(1), v
text: -0.5, 0.5 * (f(5) + f(1)), "$V_f$", center-left
:::

Vi markerer endepunktene til grafen til $f$ med klammeparenteser $[,]$ hvis endepunktet er med i definisjonsmengden. Vi bruker vinkelparenteser $\langle, \rangle$ hvis endepunktet ikke er med i definisjonsmengden.



:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen!

::::::::{quiz-2}
:::::::{quiz-question}
Grafen til en funksjon $f$ er vist i figuren nedenfor.


:::{plot}
width: 60%
function: (x - 1)**2 - 4, [-2, 4], f, blue
function-endpoints: true
:::


Hvilket alternativ viser riktig definisjonsmengde?

::::::{quiz-answer}
---
correct: true
---
$$
D_f = [-2, 4]
$$
::::::


::::::{quiz-answer}
$$
D_f = \langle -2, 4\rangle
$$
::::::


::::::{quiz-answer}
$$
D_f = [-4, 5]
$$
::::::

::::::{quiz-answer}
$$
D_f = \langle -4, 5\rangle
$$
::::::

:::::::



:::::::{quiz-question}
Grafen til en funksjon $g$ er vist i figuren nedenfor.


:::{plot}
width: 60%
function: 4 * 2**-x, [-1, 2), g, blue
function-endpoints: true
xmin: -3
xmax: 3
ymin: -1
ymax: 9
:::

Hvilket alternativ viser riktig definisjonsmengde?

::::::{quiz-answer}
---
correct: true
---
$$
D_g = [-1, 2\rangle
$$
::::::



::::::{quiz-answer}
$$
D_g = \langle-1, 2]
$$
::::::


::::::{quiz-answer}
$$
D_g = \langle 1, 8]
$$
::::::


::::::{quiz-answer}
$$
D_g = [1, 8\rangle
$$
::::::


:::::::


:::::::{quiz-question}
Grafen til en funksjon $h$ er vist i figuren nedenfor.


:::{plot}
width: 60%
function: -0.5 * (x - 1)**2 + 3, [-3, 3), h, blue
function-endpoints: true
:::

Hvilket alternativ viser riktig verdimengde?


::::::{quiz-answer}
---
correct: true
---
$$
V_h = [-5, 3]
$$
::::::


::::::{quiz-answer}
$$
V_h = [-5, 1\rangle
$$
::::::


::::::{quiz-answer}
$$
V_h = [-3, 3\rangle
$$
::::::


::::::{quiz-answer}
$$
V_h = [-5, -1]
$$
::::::




:::::::


:::::::{quiz-question}
Grafen til en funksjon $p$ er vist i figuren nedenfor.

:::{plot}
xmin: -2
ymin: -2
width: 70%
function: 0.125 * (x - 1) * (x - 3)**2 + 1, [1, 5], f, blue
function-endpoints: true
:::

Hvilket alternativ viser riktig verdimengde?



::::::{quiz-answer}
---
correct: true
---
$$
V_p = [1, 3]
$$
::::::


::::::{quiz-answer}
$$
V_p = [1, 5]
$$
::::::


::::::{quiz-answer}
$$
V_p = \langle 1, 3 \rangle
$$
::::::


::::::{quiz-answer}
$$
V_p = \langle 1, 5\rangle
$$
::::::


:::::::



::::::::

:::::::::::::::





## Regresjon
Regresjon er en metode for å finne en funksjon som passer godt til et gitt datamateriale. Ideen bak regresjon er å bestemme parameterne til modellen slik at avstanden fra grafen til $f$ og punktene i datamaterialet så liten som mulig i gjennomsnitt. 


Vi tar et praktisk eksempel.


:::::::::::::::{example} Eksempel 2

:::::::::::::::








## Gyldighetsområde
Når vi har funnet en modell, så vil det være viktig å vurdere hvor modellen er gyldig slik at vi vet hvor den gir pålitelige svar. **Gyldighetsområdet** er sterkt tilknyttet til definisjonsmengden til en funksjon, men har et mer praktisk fokus på hvor funksjonen gir pålitelige svar, ikke bare hvor funksjonsuttrykket er gyldig.




## Praktisk tolkning av gjennomsnittlig vekstfart


## Praktisk tolkning av momentan vekstfart

Momentan vekstfart skal på én måte måle stigningen *akkurat* i et punkt. Det er en meningsfull tolkning av dette. Tenk deg at vi har en skibakke
