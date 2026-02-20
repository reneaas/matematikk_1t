# Optimering

:::{goals} Læringsmål
* Kunne sette opp en matematisk modell for en praktisk situasjon
* Kunne bruke teori om funksjoner til å analysere en matematisk modell for en praktisk situasjon
* Kunne bruke digitale verktøy til å analysere en matematisk modell, og fremstille resultater ved hjelp av grafiske framstillinger, tabeller og regneark.
* Bruke en matematisk modell til å løse optimeringsproblemer i praktiske situasjoner
:::

**Optimering** handler om å gjøre noe størst eller minst mulig. I slike problemer har vi en teoretisk modell vi har satt opp som kan beskrive noe praktisk. 


Vi kan løse optimeringsproblemer ved hjelp av fire ulike strategier:
1. Lage en **verditabell** og bruke denne til å finne den optimale verdien.
2. Lage en **grafisk framstilling** av modellen og bruke denne til å finne den optimale verdien ved hjelp av ekstremalpunktene til grafen.
3. Bruke **CAS** til å finne den optimale verdien ved hjelp av den deriverte.
4. Bruke **programmering** til å finne en optimale verdien. 


### Verditabell
Én strategi for å løse et optimeringsproblem med en teoridrevet modell er å lage en systematisk oversikt ved hjelp av en **verditabell**. Dette betyr at vi regner ut en rekke verdier for en modell og lager en systematisk oversikt over disse verdiene i en tabell. For å lage dette, skal vi benytte oss av **regneark**. Vi kan så bruke denne tabellen til å finne den verdien som gir det optimale resultatet.

:::::::::::::::{example} Eksempel 1
Et område skal gjerdes inn og skal ha form som et rektangel. Vi har 64 m med gjerde til rådighet som vi skal bruke til å gjerde inn området. Målet er å få størst mulig areal. 

Se figuren nedenfor.



:::{plot}
width: 60%
axis: off
polygon: (0, 0), (44, 0), (44, 20), (0, 20)
xmin: -5
xmax: 45
ymax: 22
ymin: -2
text: 22, 0, "$x$", bottom-center
text: 44, 10, "$y$", center-right
figsize: (4, 2)
:::

Lag en oversikt over arealet for ulike lengder av sidekantene og bestem omtrent hvilken lengde på sidekantene som gir størst mulig areal.


::::{solution}
---
dropdown: 0
---
Siden vi har $64$ m med gjerde til rådighet som skal fordeles rundt to sidekanter med lengde $x$ og to sidekanter med lengde $y$, kan vi sette opp følgende likning for omkretsen:

$$
2x + 2y = 64
$$

som kan forenkles til 

$$
x + y = 32.
$$

Her er det nyttig å løse likningen for $y$ slik at vi kan velge verdien til $x$ og dermed automatisk bestemme hvilken verdi $y$ må ha slik at omkretsen fortsatt er $64$ m. Vi får da

$$
y = 32 - x.
$$

Vi må også vite arealet av rektangelet, som er gitt ved 

$$
A = x \cdot y.
$$

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::


Så lager vi en verditabell med et regneark der vi har en kolonne for $x$, en kolonne for $y$ og en kolonne for arealet $A$. Vi velger verdier for $x$ og bruker formelen for $y$ til å regne ut verdiene for $y$. Se gif-en nedenfor. Bruk Geogebra-vinduet til høyre for å følge eksempelet!


:::{figure} ./videoer/eksempler/eksempel_1/regneark.webp
---
class: no-click, adaptive-figure
width: 100%
---
:::


Fra gif-en ovenfor ser vi at når $x = y = 16 \, \mathrm{m}$, så får vi det største mulige arealet som er da er $256 \, \mathrm{m^2}$.
::::

:::::::::::::::

En svakhet med strategien i Eksempel 1 er at vi ikke får et eksakt svar på oppgaven – i stedet har vi regnet ut arealet for ulike verdier og velger ut verdiene til $x$ og $y$ ut ifra som det som gir størst areal ut ifra verdiene vi har regnet ut. For å få et mer eksakt svar, må vi enten regne ut flere verdier, eller bruke en helt annen strategi. 

### Grafisk framstilling
Å fremstille modellen grafisk er en annen strategi. Dette innebærer at vi må sette opp et funksjonsuttrykk for modellen som beskriver det vi ønsker å gjøre størst eller minst mulig. Deretter tegner grafen og
1. Finner toppunktene hvis vi ønsker å gjøre noe størst mulig.
2. Finner bunnpunktene hvis vi ønsker å gjøre noe minst mulig.

Vi tar utgangspunkt i samme situasjon som i Eksempel 1 i eksemplet nedenfor.

:::::::::::::::{example} Eksempel 2
Et område skal gjerdes inn og skal ha form som et rektangel. Vi har 64 m med gjerde til rådighet som vi skal bruke til å gjerde inn området. Målet er å få størst mulig areal. 

Se figuren nedenfor.



:::{plot}
width: 60%
axis: off
polygon: (0, 0), (44, 0), (44, 20), (0, 20)
xmin: -5
xmax: 45
ymax: 22
ymin: -2
text: 22, 0, "$x$", bottom-center
text: 44, 10, "$y$", center-right
figsize: (4, 2)
:::

Lag en grafisk framstilling og bestem lengden på sidekantene som gir størst mulig areal.


::::{solution}
---
dropdown: 0
---
Fra Eksempel 1 har vi så langt funnet ut at

$$
y = 32 - x  \qog A = x \cdot y.
$$

Hvis vi setter inn verdien for $y$ i uttrykket for arealet $A$, så får vi et funksjonsuttrykk $A(x)$ for arealet som kun er avhengig av $x$:

$$
A(x) = x \cdot (32 - x).
$$

:::{ggb-popup}
---
layout: sidebar
---
:::


Bruk Geogebra-vinduet til høyre for å følge eksempelet!

Vi lager en grafisk framstilling av funksjonen $A(x)$ og finner ekstremalpunktet til funksjonen ved å bruke {ggb-icon}`mode_extremum` i Geogebra. Se gif-en nedenfor.



:::{figure} ./videoer/eksempler/eksempel_2/grafisk.webp
---
class: no-click, adaptive-figure
width: 100%
---
:::

Fra gif-en ovenfor er vi at ekstremalpunktet til grafen er $(16, 256)$. Dette er et toppunkt som betyr at når $x = 16 \, \mathrm{m}$, så får vi det største mulige arealet som er da er $256 \, \mathrm{m^2}$. Dette stemmer overens med det vi fant i Eksempel 1, men her kan vi være sikre på at svaret er riktig fordi den grafiske framstillingen tegner grafen med langt flere punkter enn vi kan lage i en verditabell.


::::

:::::::::::::::

Å løse optimeringsproblemer ved hjelp av grafisk framstilling er en god og robust strategi som gir oss god oversikt over situasjonen ved hjelp av grafen og hjelper oss å bestemme verdier for $x$ som gjør en størrelse størst eller minst mulig. En svakhet med denne strategien er at den egentlig ikke gir oss **eksakte** verdier. I Eksempel 1 og 2, så er den riktige verdien et heltall som vi derfor får eksakt. Men i noen tilfeller vil det riktig svaret være et desimaltall eller et irrasjonalt tall og da vil denne strategien bare gi oss en tilnærmet verdi for svaret.


### CAS
Den tredje strategien vi skal se på er å bruke CAS til å finne den optimale verdien ved hjelp av den deriverte. Vi tar utgangspunkt i samme situasjon som i Eksempel 1 og 2 i eksemplet nedenfor.

:::::::::::::::{example} Eksempel 3
Et område skal gjerdes inn og skal ha form som et rektangel. Vi har 64 m med gjerde til rådighet som vi skal bruke til å gjerde inn området. Målet er å få størst mulig areal. 

Se figuren nedenfor.



:::{plot}
width: 60%
axis: off
polygon: (0, 0), (44, 0), (44, 20), (0, 20)
xmin: -5
xmax: 45
ymax: 22
ymin: -2
text: 22, 0, "$x$", bottom-center
text: 44, 10, "$y$", center-right
figsize: (4, 2)
:::

Bestem lengden på sidekantene som gir størst mulig areal.


::::{solution}
---
dropdown: 0
---
Fra Eksempel 1 og 2 så fant vi at en modell for arealet $A$ er gitt ved 

$$
A(x) = x \cdot (32 - x)
$$

der $x$ er en av lengdene til sidekantene til rektangelet, og den andre lengden er gitt ved $y = 32 - x$.


:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS-vinduet til å følge resten av eksemplet! 

For å bruke CAS til å bestemme hvilken verdi av $x$ som gir størst areal, husker vi på at eventuelle toppunkter til en funksjon $A$ er gitt ved der den deriverte $A'(x) = 0$. Dette kan vi løse med CAS:


:::{figure} ./videoer/eksempler/eksempel_3/cas.webp
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra gif-en ovenfor ser vi at når vi løser $A'(x) = 0$, så får vi $x = 16$. Hvis vi ønsker å vite hva arealet er når $x = 16$, så regner vi bare ut $A(16)$ slik som er vist i gif-en. 


::::


:::::::::::::::


### Programmering


En annen vanlig strategi er å bruke programmering til å løse optimeringsproblemer. Her skal vi se hvordan vi kan bruke programmering til å finne topp- og bunnpunkter på grafen til en funksjon.

#### Toppunkter
Vi tenker oss at vi starter i et valgt punkt $x = a$. Hvis et toppunkt ligger på oversiden av $x = a$, så betyr det at grafen til $f$ stiger. Da kan vi bruke følgende strategi:


:::::::::::::::{summary} Toppunkter med programmering
For en funksjon $f$, kan vi lete etter nullpunkter med følgende algoritme:

::::::::::::::{theory} Algoritme
1. Velg et punkt $x = a$ som startpunkt.
2. Så lenge $f(a) < f(a + 1)$:
    * Sett $a = a + 1$ (øk verdien med til $a$ med $1$).

::::::::::::::

Programmet stopper når $f(a) < f(a + 1)$ er usant, som betyr at neste verdi $f(a + 1)$ er lavere enn $f(a)$. Den siste verdien for $a$ vil da gi en tilnærming til et toppunkt $(a, f(a))$ på grafen til $f$. Figuren nedenfor viser grafisk hvordan algoritmen fungerer.

:::{interactive-graph} 
width: 60%
interactive-var: a, 0, 5, 6
interactive-var-start: 1
let: h = 1
function: -x * (x - 6), (0, 6)
def: f(x) = -x * (x - 6)
point: (a, f(a))
point: (a + h, f(a + h))
text: 6, 10, "$f({a}) < f({a} + {h:.0f})$:  {f(a) < f(a + h)}", bbox
ymin: -1
ymax: 12
xmin: -1
xmax: 8
text: a, 0, "${a:.0f}$", bottom-center
text: a + h, 0, "${a} + {h:.0f}$", bottom-right
ticks: off
vline: a, 0, f(a), dashed, gray
vline: a + h, 0, f(a + h), dashed, gray
hline: f(a), 0, a, dashed, gray
hline: f(a + h), 0, a + h, dashed, gray
hline: f(a + h), a + h, 6, dashed, gray
text: 6, f(a + h), "$f({a} + {h:.0f})$", center-right
text: 0, f(a), "$f({a})$", center-left
:::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 4

:::{plot}
align: right
width: 100%
function: x * (32 - x), (0, 32), A, blue
xmin: -2
xmax: 34
ymin: -1
ymax: 260
ticks: off
fontsize: 26
lw: 3
:::



Arealfunksjonen fra eksempel 1 er gitt ved

$$
A(x) = x(32 - x)
$$

Denne grafen har et toppunkt, som gjør at vi kan bruke algoritmen vi diskuterte ovenfor.

Vi kan velge $a = 0$, og deretter øker vi $a$ med $1$ så lenge $A(a) < A(a + 1)$ er sant.


:::{clear}
:::

:::{interactive-code}
def A(x):
    return x * (32 - x)

a = 0
while A(a) < A(a + 1):
    a = a + 1

print("Toppunkt:")
print((a, A(a)))
:::


:::::::::::::::



---


#### Bunnpunkter
Når vi skal lete etter et bunnpunkt, så starter vi i et punkt $x = a$ og sjekker om $f(a) > f(a + 1)$ er sant. Hvis det er sant, så betyr det at grafen til $f$ synker og da kan vi bruke følgende strategi:


:::::::::::::::{summary} Bunnpunkter med programmering
For en funksjon $f$, kan vi lete etter nullpunkter med følgende algoritme

::::::::::::::{theory} Algoritme
1. Velg et punkt $x = a$ som startpunkt.
2. Så lenge $f(a) > f(a + 1)$:
    * Sett $a = a + 1$ (øk verdien med til $a$ med $1$).

::::::::::::::

Programmet stopper når $f(a) > f(a + 1)$ er usant, som betyr at $f(a + 1)$ vil ligge høyere enn $f(a)$. Den siste verdien for $a$ vil da gi en tilnærming til et bunnpunkt $(a, f(a))$ på grafen til $f$. Figuren nedenfor viser grafisk hvordan algoritmen fungerer.


:::{interactive-graph} 
width: 60%
interactive-var: a, 0, 5, 6
interactive-var-start: 0
let: h = 1
function: (x - 3)**2 + 1
def: f(x) = (x - 3)**2 + 1
point: (a, f(a))
point: (a + h, f(a + h))
text: 5, 10, "$f({a}) > f({a} + {h:.0f})$:  {f(a) > f(a + h)}", bbox
ymin: -1
ymax: 12
xmin: -1
xmax: 8
text: a, 0, "${a:.0f}$", bottom-center
text: a + h, 0, "${a} + {h:.0f}$", bottom-right
ticks: off
vline: a, 0, f(a), dashed, gray
vline: a + h, 0, f(a + h), dashed, gray
hline: f(a), 0, a, dashed, gray
hline: f(a + h), 0, a + h, dashed, gray
hline: f(a + h), a + h, 6, dashed, gray
text: 6, f(a + h), "$f({a} + {h:.0f})$", center-right
text: 0, f(a), "$f({a})$", center-left
:::

:::::::::::::::



---



:::::::::::::::{example} Eksempel 5

:::{plot}
align: right
width: 100%
function: (x - 3)^2 + 1, f
xmin: -1
ymin: -1
ticks: off
fontsize: 26
lw: 3
:::



En andregradsfunksjon $f$ er gitt ved

$$
f(x) = (x - 3)^2 + 1
$$

Grafen har et bunnpunkt, så da kan vi bruke algoritmen ovenfor til å finne koordinatene til bunnpunktet med følgende program:


:::{clear}
:::


:::{interactive-code}
def f(x):
    return (x - 3)**2 + 1

a = 0
while f(a) > f(a + 1):
    a = a + 1

print("Bunnpunkt:")
print((a, f(a)))
:::

:::::::::::::::


En svakhet med algoritmene vi har sett på for å finne topp- og bunnpunkter er at de ikke nødvendigvis gir oss eksakte verdier for topp- og bunnpunktene. I Eksempel 4 og 5 så er det slik at topp- og bunnpunktene ligger på heltall, så da får vi eksakte verdier for topp- og bunnpunktene. I oppgavene skal du jobbe med oppgaver der du i stedet bruker mindre steg enn $1$ for å få en bedre tilnærming til topp- og bunnpunktene.





## Klassiske problemstillinger
De vanligste problemstillingene som kommer til å dukke opp er å bestemme modeller som beskriver areal, lengder eller volum. Etter vi har satt opp modellene, kan vi velge en av de tre strategiene vi har sett på for å løse optimeringsproblemet. I eksemplene nedenfor vil vi fokusere på det å sette opp modeller og løse optimeringsproblemene som betyr at eksemplene i seg selv her ikke representerer noen praktisk situasjon. Jobben din i oppgavene er å gjenkjenne typen matematisk problemstilling som er beskrevet i den praktiske situasjonen og oversette dette til en matematisk modell!

### Areal

Vi tar et eksempel der vi må sette opp en modell for et areal og bestemme det største mulige arealet.


:::::::::::::::{example} Eksempel 4
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = -x^2 + 9 \qder x \in [0, 3].
$$

Et rektangel har hjørnene $(0, 0)$, $(a, 0)$, $(a, f(a))$ og $(0, f(a))$. Se figuren nedenfor.

:::{plot}
width: 70%
function: -x**2 + 9, (0, 3), f, blue
xmin: -1
xmax: 4
ymin: -1
ymax: 10
ticks: off
polygon: (0, 0), (2, 0), (2, 5), (0, 5)
point: (0, 0)
point: (2, 0)
point: (2, 5)
point: (0, 5)
text: 2, 0, "$(a, 0)$", bottom-center
text: 2, 5, "$(a, f(a))$", top-right
text: 0, 5, "$(0, f(a))$", top-left
text: 0, 0, "$(0, 0)$", bottom-left
:::


Bestem $a$ slik at arealet av rektangelet er størst mulig.

::::{solution}
---
dropdown: 0
---
Vi setter opp en modell $A$ for arealet for en verdi av $a \in [0, 3]$. Grunnlinjen til rektangelet er $a$ og høyden er $f(a)$, som gir oss arealet $A$ gitt ved 

$$
A(a) = a \cdot f(a)
$$


:::{cas-popup}
---
layout: sidebar
---
:::


For å bestemme verdien av $a$ som gir størst mulig areal, kan vi bruke en av de tre strategiene vi har sett på. Her bruker vi CAS:

:::{clear}
:::

:::{figure} ./figurer/eksempler/eksempel_4/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi vet at $a \in [0, 3]$, så vi må passe på at vi kun får svar innenfor dette intervallet. Fra løsningen med CAS får vi at 

$$
a = \pm \sqrt{3}
$$

Men det er bare $a = \sqrt{3}$ som ligger i intervallet $[0, 3]$. Dermed får vi det største mulige arealet når $a = \sqrt{3}$.


::::




:::::::::::::::



### Lengde

En vanlig problemstilling er å bestemme en modell for en lengde for å så bestemme den korteste mulige lengden. Vi tar et eksempel nedenfor.

:::::::::::::::{example} Eksempel 5
Figuren nedenfor viser to punkter $A$, $B$ og et punkt $M$.

Bestem den korteste mulige lengden $AM + MB$ kan være.

:::{plot}
width: 70%
xmin: -2
xmax: 14
ymax: 2
ymin: -14
axis: off
figsize: (5, 4)
hline: 0, -1.5, 12.5, solid, gray
point: (0, -10)
point: (12, -12)
text: 0, -10, "$A$", bottom-left
text: 12, -12, "$B$", bottom-right
line-segment: (0, 0), (0, -10), dashed, gray
line-segment: (12, 0), (12, -12), dashed, gray
point: (8, 0)
text: 8, 0, "$M$", top-center
line-segment: (0, -10), (8, 0), solid, black
line-segment: (12, -12), (8, 0), solid, black
bar: (0, 2), 12, h 
text: 6, 2, "$12$", top-center
bar: (-1, 0), -10, v
text: -1, -5, "$10$", center-left
bar: (13, 0), -12, v
text: 13, -6, "$12$", center-right
:::


::::{solution}
---
dropdown: 0
---

La $M$ ha koordinatene $(x, 0)$ slik at avstanden fra "skyggen" til $A$ er $x$ og avstanden fra "skyggen" til $B$ er $12 - x$. Vi kan bruke Pytagoras' setning til å sette opp en modell for lengden $L$ av $AM + MB$. Først bestemmer vi $AM$:

$$
AM = \sqrt{x^2 + 10^2} = \sqrt{x^2 + 100}
$$

Så bestemmer vi $MB$:

$$
MB = \sqrt{(12 - x)^2 + 12^2} = \sqrt{(12 - x)^2 + 144}
$$

Modellen vår for lengden er derfor 

$$
L(x) = AM + MB = \sqrt{x^2 + 100} + \sqrt{(12 - x)^2 + 144}
$$

:::{ggb-popup}
---
layout: sidebar
---
:::


Denne gangen bruker vi en grafisk framstilling til å bestemme den korteste mulige lengden (bruk Geogebra-vinduet til høyre for å følge eksempelet!):


:::{figure} ./figurer/eksempler/eksempel_5/sol.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Fra figuren ovenfor ser vi at bunnpunktet til grafen er omtrent i $(5.45, 25.06)$ som betyr at den korteste mulige lengden er omtrent $25.06$ som vi får når $x \approx 5.45$.

::::




:::::::::::::::



