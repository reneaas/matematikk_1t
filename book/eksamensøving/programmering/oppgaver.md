# Programmeringsoppgaver

:::::::::::::::{exercise} Oppgave 1

Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 2

Nedenfor vises en programkode. 

Forklar hva programmet regner ut og bestem verdien som skrives ut av programmet. Skriv inn svaret ditt i feltet nedenfor.


:::{interactive-code}
---
predict: 
---
def f(x):
    return x ** 2 - 3 * x + 7

a = 0
b = 5

v = (f(b) - f(a)) / (b - a)

print(v)


:::


::::{answer}

Programmet regner ut den gjennomsnittlige vekstfarten til $f(x) = x^2 - 3x + 7$ i intervallet $[0, 5]$. Programmet skriver ut at denne verdien er $2$. 
::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3

Nedenfor vises en programkode. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar hva programmet regner ut og avgjør hvilke verdier som skrives ut av programmet. 

Skriv inn svaret ditt i feltet nedenfor.


::::{admonition} Fasit
---
class: answer, dropdown
---
Programmet bestemmer nullpunktene til $f(x) = x^2 - 2x - 8$. Vi bestemmer disse med $abc$-formelen som gir 

$$
x = \dfrac{2 \pm \sqrt{4 + 4\cdot 8}}{2} = \dfrac{2 \pm 6}{2} = 1 \pm 3
$$

som betyr at programmet først skriver ut $x = -2$ og deretter $x = 4$.
::::

:::::::::::::

:::::::::::::{tab-item} b
Endre på programmet slik at det løser likningen 

$$
x^2 - x - 6 = 0
$$

Bestem løsningene med programmet ditt.


::::{admonition} Fasit
---
class: answer, dropdown
---
Vi endrer på $f(x)$ i programmet slik at vi i stedet bruker $f(x) = x^2 - x - 6$. 

:::{code-block} python
---
linenos:
emphasize-lines: 2
---
def f(x):
    return x**2 - x - 6

for x in range(-10, 11):
    if f(x) == 0:
        print(x)
:::

Programmet skriver da ut 

:::{code-block} console
-2
3
:::

som betyr at løsningene av $x^2 - x - 6 = 0$ er 

$$
x = -2 \or x = 3.
$$
::::


:::::::::::::

::::::::::::::



:::{interactive-code}
---
predict:
---
def f(x):
    return x**2 - 2*x - 8

for x in range(-10, 11):
    if f(x) == 0:
        print(x)


:::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4

En programkode er vist nedenfor. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar hva programmet regner ut og bestem hvilken verdi som skrives ut av programmet. 

Sjekk svaret ved å skrive inn i feltet nedenfor.


::::{admonition} Fasit
---
class: answer, dropdown
---
Programmet regner ut summen av de $4$ først naturlige tallene. Programmet skriver derfor ut verdi

$$
s = 1 + 2 + 3 + 4 = 10.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Da en matematiker som het Gauss gikk på skolen, fikk han i oppgave å summere de 100 første heltallene som straff for at han var urolig i timen. 

Endre på programmet og bruk det til å løse oppgaven til Gauss.


::::{admonition} Fasit
---
class: answer, dropdown
---
Vi må endre på programmet slik at det summerer opp tallene $1, 2, \ldots, 99, 100$, som vi kan oppnå ved å bruke `range(1, 101)` i stedet for `range(1, 5)`. Da får vi programmet:

:::{code-block} python
---
linenos: 
emphasize-lines: 3
---
s = 0

for n in range(1, 101):
    s = s + n

print(s)
:::

som gir utskriften

:::{code-block} console
5050
:::

Summen av de 100 første naturlige tallene er derfor $5050$. 
::::

:::::::::::::


::::::::::::::


:::{interactive-code}
---
predict:
---
s = 0

for n in range(1, 5):
    s = s + n

print(s)


:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5

I denne oppgaven skal du jobbe med summer av oddetall og partall. Vi lar $S_n$ være summen av de $n$ første oddetallene. Nedenfor vises noen av disse summene: 

\begin{align*}
    S_1 &= 1 \\
    S_2 &= 1 + 3 \\
    S_3 &= 1 + 3 + 5 \\
    S_4 &= 1 + 3 + 5 + 7 \\
    S_5 &= 1 + 3 + 5 + 7 + 9 \\
    S_6 &= 1 + 3 + 5 + 7 + 9 + 11 \\
    \vdots & \quad \quad \quad \vdots \quad \quad \quad \vdots \quad \quad \quad \vdots \\
\end{align*}


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som regner ut og skriver ut summene $S_1, S_2, S_3, \ldots, S_{20}$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
s = 0

for n in range(20):
    oddetall = 2 * n + 1
    s = s + oddetall
    print(s)
:::

som gir utskriften

:::{code-block} console
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør om summen av de 20 første partallene er større enn summen av de 20 første oddetallene.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
emphasize-lines: 3,4,5
---
s = 0

for n in range(1, 21):
    partall = 2 * n
    s = s + partall

print(s)
:::

som gir utskriften

:::{code-block} console
420
:::

Altså er summen av de 20 første partallene større enn summen av de 20 første oddetallene.


::::

:::::::::::::

::::::::::::::


:::{interactive-code}
# Skriv din kode her




:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6

Nedenfor vises en figur som er satt sammen av uendelig mange linjestykker.

Lengden til et linjestykke er alltid $90 \%$ av lengden til det forrige linjestykket. Det første linjestykket er $100$ cm langt.

:::{figure} ./figurer/oppgave_6/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som bestemmer summen av lengdene til de $10$ første linjestykkene.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
s = 0 # summen av lengdene
lengde = 100 # første linjestykke
n = 0 # antall linjestykker

while n < 10:
    s = s + lengde     # plusser på lengden
    n = n + 1        # øk antall linjestykker med 1
    lengde = 0.9 * lengde     # neste lengde = 90% av forrige lengde
    
print(s)
:::

gir utskriften

:::{code-block} console
651.3215599000001
:::

som betyr at summen av lengdene til de 10 første linjestykkene er ca. $651.32$ cm.
::::

:::::::::::::


:::::::::::::{tab-item} b
Hvor mange linjestykker må du legge sammen for at summen av lengdene skal bli minst 9 meter?



::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
emphasize-lines: 5,10
---
s = 0 # summen av lengdene
lengde = 100 # første linjestykke
n = 0 # antall linjestykker

while s < 900: # så lengde summen er mindre enn 9 m = 900 cm
    s = s + lengde     # plusser på lengden
    n = n + 1        # øk antall linjestykker med 1
    lengde = 0.9 * lengde     # neste lengde = 90% av forrige lengde
    
print(n)
:::

gir utskriften

:::{code-block} console
22
:::

som betyr at vi trenger 22 linjestykker før linjestykket blir lenger enn 9 meter (900 cm).
::::

:::::::::::::



:::::::::::::{tab-item} c
Hvilken lengde vil lengden av hele figuren nærme seg?

::::{admonition} Fasit
---
class: answer, dropdown
---
Kjører vi programmet med veldig mange linjestykker, vil summen av lengdene nærme seg $1000$ cm.
::::

:::::::::::::



::::::::::::::


:::{interactive-code}
# Skriv din kode her




:::




:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 7

I figuren nedenfor vises grafen til en rasjonal funksjon gitt ved

$$
f(x) = \dfrac{8}{x^2 + 4}
$$

Et rektangel har hjørner i punktene $(0,0)$, $(3, 0)$, $(3, f(3))$ og $(0, f(3))$.

:::{figure} ./figurer/oppgave_7/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som regner ut arealet til rektangelet.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 4)
    
def A(x):
    return x * f(x)
    

areal = A(3)

print(areal)
:::

som gir utskriften

:::{code-block} console
1.8461538461538463
:::

som betyr at arealet av rektangelet er omtrent $1.85$. 
::::

:::::::::::::


:::::::::::::{tab-item} b
Utvid programmet ditt slik at det skriver ut arealet av rektangelene med hjørner i punktet $(0, 0)$, $(k, 0)$, $(k, f(k))$ og $(0, f(k))$ for $k = \{1, 2, 3, \ldots, 9, 10\}$.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 4)
    
def A(x):
    return x * f(x)


for k in range(1, 11):
    print(k, A(k))
:::

som gir utskriften 

:::{code-block} console
1 1.6
2 2.0
3 1.8461538461538463
4 1.6
5 1.3793103448275863
6 1.2000000000000002
7 1.0566037735849056
8 0.9411764705882353
9 0.8470588235294118
10 0.7692307692307693
:::

Første kolonne er verdiene av $k$ og andre kolonne er arealene av rektanglene.

:::::::::::::


:::::::::::::{tab-item} c
Utvid programmet ditt og bestem hvilken verdi av $k \in \langle 0, \to\rangle$ som gir størst mulig areal.


::::{admonition} Fasit
---
class: answer, dropdown
---

Vi starter med den laveste mulige verdien av $k$, så øker vi $k$ med en liten verdi så lenge det neste arealet er større enn det nåværende. Når det neste arealet er mindre enn det nåværende, har vi funnet den verdien av $k$ som gir størst areal:

:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 4)
    
def A(x):
    return x * f(x)


k = 0
while A(k) < A(k + 0.01): # Så lenge neste areal er større 
    k = k + 0.01
    
print(k)
:::

som gir utskriften

:::{code-block} console
2.0000000000000013
:::

som betyr at $k \approx 2$ gir størst mulig areal.
::::

:::::::::::::

::::::::::::::

:::{interactive-code}
# Skriv din kode her




:::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8

I figuren nedenfor vises en følge av kvadrater der det første kvadratet har sidelengde $1$. Sidelengdene i det neste kvadratet er $90 \%$ av sidelengdene i det forrige kvadratet. Slik fortsetter følgen i det uendelige.

:::{figure} ./figurer/oppgave_8/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


Lag et program som regner ut summen av arealene til veldig mange kvadrater. 


:::{interactive-code}
# Skriv din kode her




:::




::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
sidelengde = 1
n_kvadrater = 1_000_000 # antall kvadrater

sum_arealer = 0    # lagrer summen av arealene
for i in range(n_kvadrater):
    areal = sidelengde ** 2 # arealet til kvadratet
    sum_arealer = sum_arealer + areal # legg til på summen
    
    sidelengde = 0.9 * sidelengde # neste sidelengde er 90% av forrige

print(sum_arealer)
:::

som gir utskriften

:::{code-block} console
5.263157894736843
:::

som betyr at arealet når vi bruker mange kvadrater er omtrent $5.26$. 
::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9

I denne oppgaven skal du bestemme arealet av det fargelagte området vist i figuren nedenfor. Funksjonen $f$ er gitt ved 

$$
f(x) = \dfrac{1}{9}(x + 1)(x - 6)^2
$$


:::{figure} ./figurer/oppgave_9/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

For å bestemme arealet av det fargelagte området, skal du summere arealene til rektangler som bruker $f(x)$ som høyde til rektangler for ulike verdier av $x$ i intervallet $[0, 6]$. Se figurene nedenfor:

:::{figure} ./figurer/oppgave_9/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem summen av arealene i rektanglene i figuren til venstre ovenfor (med 6 rektangler).

::::{admonition} Fasit
---
class: answer, dropdown
---
Arealet av rektanglene i figuren til venstre ovenfor (med 6 rektangler) er ca. $21.78$. 
::::


:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut arealet av det fargelagte området ved å bruke $6000$ rektangler.

Du kan ta utgangspunkt i programmet nedenfor.


:::{interactive-code}
def f(x):
    return 1/9 * (x + 1) * (x - 6) ** 2

x_min = 0
x_max = 6

n = 6000 # antall rektangler

bredde = # FYLL INN bredde til hvert rektangel


:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

:::{code-block} python
---
linenos:
---
def f(x):
    return 1/9 * (x + 1) * (x - 6) ** 2

x_min = 0
x_max = 6

n = 6000 # antall rektangler

bredde = (x_max - x_min) / n

areal = 0
for i in range(n):
    x = x_min + i * bredde
    høyde = f(x)
    
    areal = areal + bredde * høyde
    
print(areal)
:::

**Utskrift**:

:::{code-block} console
20.001999777777893
:::

Arealet under grafen til $f$ i intervallet $[0, 6]$ er derfor omtrent $20$.

::::


:::::::::::::
::::::::::::::




:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 10
I figuren til høyre vises en likesidet trekant med sidelengder $2$. 

:::{figure} ./figurer/oppgave_10/figur.svg
---
width: 100%
class: no-click, adaptive-figure
align: right
---
:::

Inni den ytre trekanten er det innskrevet en mindre likesidet trekant. Inni denne trekanten er det igjen innskrevet en enda mindre likesidet trekant. Slik fortsetter det i det uendelige.


Lag et program som regner ut summen av omkretsene til de 100 største trekantene.

:::{clear}
:::


:::{interactive-code}
# Skriv din kode her

:::

:::::{solution}
:::{code-block} python
---
linenos:
---
sidelengde = 2
samlet_omkrets = 0

for i in range(100):
    omkrets = 3 * sidelengde    # omkretsen til nåværende trekant
    samlet_omkrets = samlet_omkrets + omkrets    # legg til omkretsen
    sidelengde = sidelengde / 2 # neste trekant har halvparten av sidelengden
    
print(samlet_omkrets)
:::

som gir utskriften

:::{code-block} console
11.999999999999998
:::

som betyr at den samlede omkretsen til de 100 største trekantene er omtrent $12$.
:::::

:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 11
I figuren nedenfor til høyre vises en figur som er satt sammen av likesidede trekanter med sidelengder $2$. Figuren nedenfor til høyre viser en tilsvarende figur med mange flere slike likesidede trekanter.

:::{figure} ./figurer/oppgave_11/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som regner ut hvor mange trekanter det er i en figur dersom den ytre omkretsen til figuren er $600$. 


:::{interactive-code}
# Skriv din kode her 


:::

::::{solution}
Siden de mindre likesidede trekantene har sidelengder $2$ og den ytre omkretsen skal være $600$, så betyr at sidelengdene i den samlede figuren er $600 / 3 = 200$. Da følger det at det er $200 / 2 = 100$ rader med trekanter. Antall trekanter i hver rad er $1, 3, 5, \ldots, 2n + 1$ der $n = 0, 1, 2, \ldots, 99$. Vi kan summere opp antall trekanter i figuren med følgende program: 

:::{code-block} python
---
linenos:
---
n_trekanter = 0 # for å summere opp antall trekanter
for n in range(100): # summerer over 100 rader.
    n_trekanter = n_trekanter + (2 * n + 1) # legger til antall trekanter i rad n.
    
print(n_trekanter)
:::

som gir utskriften

:::{code-block} console
10000
:::

Altså er det 10000 trekanter i figuren.
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut hvor mange rader det er i en figur dersom arealet av hele figuren er $100 \cdot \sqrt{3}$.


:::{interactive-code}
# Skriv din kode her 


:::

:::::::::::::

::::::::::::::

:::::::::::::::



:::::::::::::::{exercise} Oppgave 12

En lysstråle ble først observert ved et punkt $A(1000, 0)$ i luften og deretter i et punkt $B(10000, -1000)$ i vann.

Alle avstander er målt i meter. Se figuren nedenfor.


:::{figure} ./figurer/oppgave_12/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Lyset reiser med en fart på $300 \, \mathrm{m/\mu s}$ (meter per mikrosekund) i luft og $225 \, \mathrm{m/\mu s}$ i vann. Her står $1 \, \mathrm{\mu s}$ for 1 mikrosekund som en milliondel av et sekund.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises et program som regner ut tiden det tar for lyset å reise fra $A$ til $M(3000, 0)$.

Pusle sammen programmet i riktig rekkefølge.


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{code-block} python
---
linenos:
---
from math import sqrt # jeg må være første kodelinje!

def tid_luft(x):
    fart_luft = 300 # meter per mikrosekund
    
    AM = sqrt(x**2 + 1000**2) # meter
    tid = AM / fart_luft # mikrosekunder

    return tid
    

x = 3000
reisetid = tid_luft(x)

print(f"{reisetid = :.2f} mikrosekunder")
:::

::::

:::::::::::::

:::::::::::::{tab-item} b
Forklar matematikken bak kodelinje 6 og 7 i programmet.

::::{admonition} Fasit
---
class: answer, dropdown
---
* **Kodelinje 6** bruker Pytagoras' setning til å regne ut avstanden $AM$ der den ene kateten er $x = 3000$ m og den andre kateten er $1000$ m. 
* **Kodelinje 7** bruker vei-fart-tid-formelen $s = v \cdot t$ til å regne ut tiden det tar å reise avstanden $AM$ i luft, der $s$ er avstanden, $v$ er farten og $t$ er tiden.
::::

:::::::::::::


:::::::::::::{tab-item} c
Utvid programmet slik at det regner ut tiden det tar for lyset å reise fra $M$ til $C$ i vann.

Bruk programmet til å regne ut tiden det tar for lyset å reise helt fra $A$ til $C$.


::::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
emphasize-lines: 11-17, 21
---
from math import sqrt

def tid_luft(x):
    fart_luft = 300 # meter per mikrosekund

    AM = sqrt(x**2 + 1000**2) # meter
    tid = AM / fart_luft # mikrosekunder

    return tid
    
def tid_vann(x):
    fart_vann = 225 # meter per mikrosekund
    
    MC = sqrt((x - 10_000)**2 + 1000**2)
    tid = MC / fart_vann
    
    return tid
    

x = 3000
reisetid = tid_luft(x) + tid_vann(x)

print(f"{reisetid = :.2f} mikrosekunder")
:::

som gir utskriften

:::{code-block} console
reisetid = 41.97 mikrosekunder
:::

som betyr at lyset bruker omtrent $41.97$ mikrosekunder fra $A$ til $C$.

::::::


:::::::::::::



:::::::::::::{tab-item} d
Utvid programmet ditt med en funksjon `T(x)`{l=python} som bruker funksjonen `tid_luft(x)`{l=python} og `tid_vann(x)`{l=python} til å regne ut den totale tiden lysstrålen bruker fra $A$ til $C$ når den treffer vannoverflaten i punktet $M(x, 0)$.


::::{admonition} Fasit
---
class: answer, dropdown
---
Funksjonen må plasseres nedenfor funksjonene `tid_luft(x)`{l=python} og `tid_vann(x)`{l=python} i programmet fra **a**. Da kan vi definere funksjonen som:

:::{code-block} python
---
linenos:
---
def T(x):
    return tid_luft(x) + tid_vann(x)
:::

::::

:::::::::::::


:::::::::::::{tab-item} e
Ifølge Snells lov, vil lysstrålen vil alltid "velge" den veien mellom $A$ og $C$ som gir kortest mulig reisetid. 

Utvid programmet ditt og bruk det til å bestemme i hvilket punkt lysstrålen må ha truffet vannoverflaten.

::::::::{admonition} Fasit
---
class: answer, dropdown
---
:::::::{tab-set}
::::::{tab-item} 1. Strategi
Vi må bestemme hvilken verdi av $x$ som gir minst mulig verdi for $T(x)$. Dette kan vi gjøre ved å starte med $x = 0$, og deretter øke $x$ med et lite tall så lenge reisetiden i $x$ er større enn reisetiden i $x + \mathrm{lite \, tall}$. Altså, så lenge

$$
T(x) > T(x + \mathrm{lite \, tall})
$$ 

Når $T(x) \leq T(x + \mathrm{lite \, tall})$, har vi funnet den verdien av $x$ som gir kortest mulig reisetid.
::::::

::::::{tab-item} 2. Utvidelse til programkode
Utvidelse av programkoden fra **b**:

:::{code-block} python
x = 0
while T(x) > T(x + 0.01):
    x = x + 0.01
    
print(x)
:::

::::::

::::::{tab-item} 3. Full programkode
Utvidelse av programkoden fra **b**:

:::{code-block} python
---
linenos:
---
from math import sqrt

def tid_luft(x):
    fart_luft = 300 # meter per mikrosekund

    AM = sqrt(x**2 + 1000**2) # meter
    tid = AM / fart_luft # mikrosekunder

    return tid
    
def tid_vann(x):
    fart_vann = 225 # meter per mikrosekund
    
    MC = sqrt((x - 10_000)**2 + 1000**2)
    tid = MC / fart_vann
    
    return tid

    
def T(x):
    return tid_luft(x) + tid_vann(x)    


x = 0
while T(x) > T(x + 0.01):
    x = x + 0.01

print(f"{x = :.2f} meter")

:::

som gir utskriften

:::{code-block} console
x = 8882.18 meter
:::

som betyr at lysstrålen traff vannet omtrentlig i punktet $M(8882, 0)$.

::::::

:::::::
::::::::

:::::::::::::


::::::::::::::




:::{parsons-puzzle}
from math import sqrt # jeg må være første kodelinje!

def tid_luft(x):
    fart_luft = 300 # meter per mikrosekund
    
    AM = sqrt(x**2 + 1000**2) # meter;    tid = AM / fart_luft # mikrosekunder

    return tid
    

x = 3000;reisetid = tid_luft(x)

print(f"{reisetid = :.2f} mikrosekunder")

:::


:::::::::::::::









