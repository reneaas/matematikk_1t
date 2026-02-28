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
I praktiske situasjoner, så avgrenser vi ofte hvor funksjonen kan brukes. Selv om et funksjonsuttrykk $f(x)$ kan gi mening for alle verdier av $x$, kan det hende det ikke mening å bruke alle mulige verdier for $x$ i en praktisk situasjon. 

:::::::::::::::{example} Eksempel 1
Når man bruker en el-sparkesykkel fra Voi, så koster det 10 kr å låse opp sparkesykkelen. Deretter koster det 3 kr per minutt. Et funksjonsuttrykk som beskriver hvor mange kr $f(x)$ vi må betale for å bruke sparkesykkelen i $x$ minutter, er da 

$$
f(x) = 3x + 10
$$

Vi kan ikke kjøre sparkesykkelen i negative minutter, så derfor må $x \geq 0$. Men samtidig så setter de en grense på hvor lenge du kan leie sparkesykkelen, som gjerne er 45 minutter. Derfor må også $x \leq 45$. 

Men da er $f(x)$ bare **definert** når $x \in [0, 45]$. 


:::::::::::::::


De verdiene for $x$ som en funksjon er **definert** for kaller vi for **definisjonsmengden** til funksjonen. De verdiene som $f(x)$ da får, kaller vi for **verdimengden** til funksjonen.



:::::::::::::::{summary} Definisjonsmengde og verdimengde
For en funksjon $f$ kaller vi 

* **Definisjonsmengden** til $f$ for $D_f$ og den består av alle $x$-verdier der $f(x)$ er definert.
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
:::{cas-popup}
---
layout: sidebar
---
:::


:::{plot}
nocache: 
figsize: (3, 3)
align: left
axis: off
axis: equal
width: 70%
let: v = pi / 6
let: u = -pi / 6
let: l = 3
let: dr = 0.5
let: L = 3
line-segment: (-L, 0), (L, 0), solid, gray
line-segment: (0, 0), (l * sin(v), -l * cos(v)), solid, blue
circle: ((l + dr) * sin(v), -(l + dr) * cos(v)), dr, solid, red, fill
line-segment: (0, 0), (l * sin(u), -l * cos(u)), dashed, blue
circle: ((l + dr) * sin(u), -(l + dr) * cos(u)), dr, dashed, red, fill
angle-arc: (0, 0), l + dr, 270 + 30, 270 - 30, dashed, gray 
text: 0.5 * l, -0.5 * l, "$\ell$", top-right
point: (0, 0)
:::


:::{clear}
:::

Tiden det tar for en pendel å svinge frem og tilbake én gang kalles for perioden til pendelen.


I tabellen nedenfor vises perioden til en pendel for ulike snorlengder $\ell$. 


:::{table}
---
transpose:
---
labels: Snorlengde (meter), Periode (sekunder)
0.1, 0.69
0.3, 1.17
0.5, 1.44
0.8, 1.82
1.0, 2.08
1.3, 2.27
1.6, 2.53
2.0, 2.80
:::

<br>

Lag en modell $T$ på formen

$$
T(x) = a \cdot x^b
$$

som viser sammenhengen mellom snorlengden $x$ i meter og perioden $T(x)$ i sekunder.


::::{solution}
---
dropdown: 0
---

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::

Vi bruker regresjon til å bestemme parameterne $a$ og $b$ i modellen. 

1. Først skriver vi inn alle datapunktene i to kolonner i et **regneark**.
2. Deretter markerer vi datapunktene og trykker på {ggb-icon}`mode_regression` i verktøylinjen.

:::{figure} ./videoer/eksempler/2/regresjon_del_1.webp
---
class: no-click, adaptive-figure
width: 60%
---
:::

Da åpnes regresjonsvinduet, og vi velger modellen **potens** for å få en potensmodell på formen $T(x) = a \cdot x^b$.


:::{figure} ./videoer/eksempler/2/regresjon_del_2.webp
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra gif-en ovenfor, ser vi at modellen da blir

$$
T(x) = 2.03 \cdot x^{0.47}
$$



::::

:::::::::::::::








## Gyldighetsområde
Når vi har funnet en modell, så vil det være viktig å vurdere hvor modellen er gyldig slik at vi vet hvor den gir pålitelige svar. **Gyldighetsområdet** er sterkt tilknyttet til definisjonsmengden til en funksjon, men har et mer praktisk fokus på hvor funksjonen gir pålitelige svar, ikke bare hvor funksjonsuttrykket er gyldig.


:::::::::::::::{example} Eksempel 3
Funksjonen $T$ er gitt ved 

$$
T(x) = -0.0025x^3 + 0.089x^2 - 0.67x^2 + 6.12
$$

beskriver temperaturen $T(x)$ i grader Celsius $x$ timer etter midnatt i et døgn i Lindesnes i januar.

Anslå et gyldighetsområdet for modellen.

::::{solution}
---
dropdown: 0
---
Hvis vi tegner grafen til funksjonen, så vil vi se at grafen til $T$ vil synke mot $-\infty$ når $x$ blir stor og vokse mot $+\infty$ når $x$ blir stor og negativ. 

:::{plot}
width: 70%
function: -0.0025*x**3 + 0.089 * x**2 - 0.67 * x + 6.12, (-8, 32), T
xlabel: timer etter midnatt
ylabel: $T(x)/^\circ\mathrm{C}$, -20
xstep: 4
ystep: 4
xmin: -8
xmax: 32
ymin: -12
ymax: 20
:::

Altså vil modellen forutsi at det var urealistisk varmt dagen før, og at det vil bli urealistisk kaldt dagen etter.

Fordi temperaturen dagen før og dagen etter sannsynligvis ikke vil være veldig forskjellig fra temperaturen i døgnet modellen er basert på, så vil et rimelig gyldighetsområde være

$$
x \in [0, 24]
$$

Altså vil modellen med gyldighetsområdet se slik ut:

:::{plot}
width: 70%
function: -0.0025*x**3 + 0.089 * x**2 - 0.67 * x + 6.12, [0, 24], T, blue
function-endpoints: true
xlabel: timer etter midnatt
ylabel: $T(x)/^\circ\mathrm{C}$, -20
xstep: 4
ystep: 4
xmin: -8
xmax: 32
ymin: -12
ymax: 20
:::



::::



:::::::::::::::





## Praktisk tolkning av gjennomsnittlig vekstfart


:::{plot}
fontsize: 28
ticks: off
align: right
width: 100%
function: 0.5 * (x - 2)**3 + (x - 2)**2 - 2 * (x - 2) + 1, f, blue
xmin: -2
ymin: -1
ymax: 8
let: a = -1
let: b = 4
point: (a, f(a))
point: (b, f(b))
line: (a, f(a)), (b, f(b)), solid, red
text: a, f(a), "$(a, f(a))$", top-left
text: b, f(b), "$(b, f(b))$", bottom-right
:::


For en funksjon $f$, var det sånn at den gjennomsnittlige vekstfarten til funksjonen på intervallet $[a, b]$ var gitt ved 

$$
\dfrac{\Delta f}{\Delta x} = \dfrac{f(b) - f(a)}{b - a}
$$

Dette tilsvarte stigningstallet til den rette linjen som går gjennom punktene $(a, f(a))$ og $(b, f(b))$ på grafen til $f$. Vi kalte denne linja for en **sekant**.


:::::::::::::::{example} Eksempel 4
En kopp med kaffe har i utgangspunktet en temperatur på $100^\circ\mathrm{C}$. Kaffekoppen plasseres i et rom med temperatur $20^\circ\mathrm{C}$, og temperaturen til kaffen synker etter hvert. Etter 5 minutter er temperaturen til kaffen $80^\circ\mathrm{C}$, og etter 10 minutter er temperaturen $65^\circ\mathrm{C}$.

En modell for temperaturen $T(x)$ til kaffen i grader Celsius etter $x$ minutter er gitt ved 

$$
T(x) = 79.84 \cdot 0.93^x + 20
$$

Hvor mye endret temperaturen seg i gjennomsnitt de første 10 minuttene?


::::{solution}
---
dropdown: 0
---
Vi regner ut den gjennomsnittlige vekstfarten til temperaturen $T$ på intervallet $[0, 10]$ ved å bruke formelen for gjennomsnittlig vekstfart:

$$
\dfrac{\Delta T}{\Delta x} = \dfrac{T(10) - T(0)}{10 - 0}
$$

Vi gjør dette med CAS:


:::{figure} ./figurer/eksempler/4/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså var den gjennomsnittlige vekstfarten $-4.12$ grader Celsius per minutt. Det betyr at temperaturen i *gjennomsnitt* sank med $4.12$ grader Celsius per minutt de første 10 minuttene.


::::


:::::::::::::::


## Praktisk tolkning av momentan vekstfart

Momentan vekstfart skal på én måte måle stigningen *akkurat* i et punkt. Den gjennomsnittlige vekstfarten på et veldig lite intervall rundt punktet vil omtrent være lik den momentane vekstfarten. 
Det vil si at stigningstallet til en tangent i et punkt er nesten lik stigningstallet til en sekant som går gjennom to punkter som ligger i nærheten.


:::{plot}
width: 50%
function: 1 / x, (0, 10), f, blue
xmin: -0.5
xmax: 6
ymin: -0.2
ymax: 2
let: a = 2
let: b = 3
point: (a, f(a))
point: (b, f(b))
line: (a, f(a)), (b, f(b)), dashed, red
text: a, f(a), "$(a, f(a))$", top-right
text: b, f(b), "$(b, f(b))$", top-right
tangent: a, f, solid, teal
ticks: off
nocache:
fontsize: 24
:::


Så lenge en funksjon ikke endrer seg veldig raskt i nærheten av punktet, 
så er det rimelig å forvente at den momentane vekstfarten i et punkt $x$ er omtrent lik den gjennomsnittlige vekstfarten
på intervallet $[x, x + 1]$, som betyr at

$$
f'(x) \approx \dfrac{f(x + 1) - f(x)}{1} = f(x + 1) - f(x)
$$

Det betyr at den momentane vekstfarten forteller oss omtrent hvor mye $f(x)$ vil endre seg dersom vi øker $x$ med $1$. 
Dette stemmer jo ganske godt overens med hvordan vi tolker stigningstallet til en lineær funksjon. 


:::::::::::::::{example} Eksempel 5
Temperaturen $T$ til en kopp med kaffe i grader Celsius etter $x$ minutter er gitt ved

$$
T(x) = 79.84 \cdot 0.93^x + 20
$$

Bestem den momentane vekstfarten til temperaturen etter 10 minutter. Gi en praktisk tolkning av svaret.

::::{solution}
---
dropdown: 0
---
Vi regner ut $T'(10)$ med CAS, og så sammenligner vi det med $T(11) - T(10)$ for å se om det gir omtrent samme svar.

:::{figure} ./figurer/eksempler/5/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $T'(10) \approx -2.8$ grader Celsius per minutt som betyr at temperaturen vil synke med omtrent $2.8$ grader Celsius per minutt etter 10 minutter. 
Det vil si at temperaturen vil være ca. $2.8$ grader lavere 1 minutt senere. 

Vi ser at $T(11) - T(10) \approx -2.7$ grader Celsius, så dette stemmer ganske bra. 



::::
:::::::::::::::
