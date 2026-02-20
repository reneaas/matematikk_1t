# Oppgaver: Optimering



:::::::::::::::{exercise} Oppgave 1
Anna og Bjørn har materiale nok til å lage et gjerde som er 64 m langt.

De skal gjerde inn et område som skal ha form som et rektangel, og de ønsker at området skal få størst mulig areal. Se figuren nedenfor.

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





::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::


Anna mener at arealet blir størst mulig dersom alle sidekantene er like lange.

Lag en oversikt over arealet for ulike lengder på sidekantene og vurder om Anna sin påstand er riktig.


:::{clear}
:::


::::{hints}
Sett først opp et uttrykk for omkretsen uttrykt med $x$ og $y$. Deretter kan du løse likningen for $y$ og la $x$ bestemme verdiene til $y$.
::::




:::::::::::::



:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



Bjørn vil sette opp et funksjonsuttrykk for å bestemme hvilken lengde på sidekantene som gir størst mulig areal.


Lag modellen for Bjørn og bruk den til å bestemme hvilken lengde på sidekantene som gir størst mulig areal.
:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 2
Alma og Synne skal slå opp telt ved en elvebredde. De skal sette opp et tau rundt teltet for å holde dyr unna. 

De har 80 m med tau og fire pinner. Området de skal gjerde inn skal ha form som et rektangel og de tenker å bruke elvebredden som en av sidene i rektangelet slik at de kan gjerde inn et større område. Målet deres er å få et størst mulig areal innenfor gjerdet. Se figuren nedenfor.


:::{plot}
width: 70%
axis: off
figsize: (5, 3)
hline: 0, -10, 10, solid, blue
line-segment: (0, 0), (8, 0), black, solid
line-segment: (-4, 0), (-4, 5), black, solid
line-segment: (-4, 5), (4, 5), black, solid
line-segment: (4, 5), (4, 0), black, solid
text: 0, 0, "Elvebredde", bottom-center
annotate: (5, 5), (0, 5), "Gjerde", 0.5
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::

Lag en oversikt over arealet for ulike lengder på sidekantene og avgjør omtrent hvilken lengde på sidekantene som gir størst mulig areal.




:::::::::::::



:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::


Synne vil lage en grafisk framstilling som viser arealet av området for ulike lengder på sidekantene.

Lag en grafisk framstilling for Synne og bruk den til å bestemme hvilken lengde på sidekantene som gir størst mulig areal.


::::{answer}
:::{plot}
width: 80%
function: x * (80 - 2*x), (0, 40), A
xmin: -5
xmax: 45
xstep: 5
ymin: -200
ymax: 1000
ystep: 200
point: (20, 800)
text: 20, 800, "$(20, 800)$", top-center
xlabel: $x / \mathrm{m}$
ylabel: $A(x) / \mathrm{m^2}$, -40
:::

::::


:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


Alma vil løse oppgaven helt eksakt. 

Bruk CAS til å bestemme den eksakte verdien for lengden på sidekantene som gir størst mulig areal.
:::::::::::::



::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 9 \qder x \in [0, 3].
$$

En trekant har hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$. Se figuren nedenfor.


:::{plot}
width: 70%
function: -x**2 + 9, (0, 3), f
xmin: -1
xmax: 4
ymax: 10
ymin: -1
ticks: off
polygon: (0, 0), (2, 0), (2, 5), blue, 0.2
point: (0, 0)
point: (2, 0)
point: (2, 5)
text: 0, 0, "$(0, 0)$", bottom-left
text: 2, 0, "$(k, 0)$", bottom-center
text: 2, 5, "$(k, f(k))$", top-right
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::


Lag en systematisk oversikt over arealet av trekanten for ulike verdier av $k \in [0, 3]$ og finn et estimat på hvilken verdi av $k$ som gir størst mulig areal.


:::::::::::::


:::::::::::::{tab-item} b
:::{ggb-popup}
---
layout: sidebar
---
:::


Lag en grafisk framstilling som viser sammenhengen mellom arealet $A(k)$ av trekanten og $k$. 

Bestem det største mulige arealet trekanten kan ha.
:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem en eksakt verdi for det største arealet trekanten kan ha.


:::::::::::::


::::::::::::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
En tredjegradsfunksjon $f$ er gitt ved

$$
f(x) = -x^3 + 4x^2 \qder x \in [0, 4].
$$

En trekant har hjørner i punktene $(1, 0)$, $(4, 0)$ og $(1, f(1))$. Se figuren nedenfor.


:::{plot}
width: 70%
function: -x**3 + 4*x**2, (0, 4), f
xmin: -1
xmax: 5
ymax: 10
ymin: -1
yticks: off
grid: off
polygon: (1, 0), (4, 0), (1, 3), blue, 0.2
point: (1, 0)
point: (4, 0)
point: (1, 3)
text: 1, 3, "$(1, f(1))$", top-left
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet av trekanten.

:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::



En trekant har hjørner i $(k, 0)$, $(4, 0)$, og $(k, f(k))$ der $k \in [0, 4]$. 

Lag en systematisk oversikt over arealet av trekanten for ulike verdier av $k$ og finn et estimat på hvilken verdi av $k$ som gir størst mulig areal.
:::::::::::::


:::::::::::::{tab-item} c

:::{ggb-popup}
---
layout: sidebar
---
:::


En trekant har hjørner i $(k, 0)$, $(4, 0)$, og $(k, f(k))$ der $k \in [0, 4]$. 

Lag en grafisk fremstilling som viser arealet $A(k)$ til trekanten for $k \in [0, 4]$. Bestem det største mulige arealet trekanten kan ha.
:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::

En trekant har hjørner i $(k, 0)$, $(4, 0)$, og $(k, f(k))$ der $k \in [0, 4]$. 

Bestem en eksakt verdi for $k$ som gir det største arealet for trekanten. 

:::::::::::::


::::::::::::::



:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5
Nedenfor ser du grafen til en funksjon $f$ gitt ved

$$
f(x) = \dfrac{8}{x^2 + 20} \qder D_f = [0, \to \rangle
$$

Et rektangel har hjørnene $(0, 0)$, $(r, 0)$, $(r, f(r))$ og $(0, f(r))$. Se figuren nedenfor.

:::{plot}
width: 70%
function: 8/(x**2 + 20), (0, 20), f
xmin: -1
xmax: 15
ymin: -0.1
ymax: 0.5
ystep: 0.1
point: (5, f(5))
point: (0, 0)
point: (0, f(5))
point: (5, 0)
polygon: (0, 0), (5, 0), (5, f(5)), (0, f(5)), blue, 0.2
text: 0, 0, "$(0, 0)$", bottom-left
text: 5, 0, "$(r, 0)$", bottom-center
text: 5, f(5), "$(r, f(r))$", top-right
text: 0, f(5), "$(0, f(r))$", top-left
ticks: off
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::



Lag en systematisk oversikt over arealet for verdier av $r \in \{0, 1, 2, \ldots, 10\}$.

Bruk oversikten til å anslå hvilken verdi av $r$ som gir størst mulig areal.

:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::



Lag en grafisk framstilling som viser sammenhengen mellom arealet $A(r)$ og $r$.

Bruk den grafiske framstillingen til å bestemme hvilken verdi av $r$ som gir størst mulig areal.
:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem en eksakt verdi for det største arealet rektangelet kan ha.

:::::::::::::



::::::::::::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6

:::{cas-popup}
---
layout: sidebar
---
:::


En båt skal reise fra en øy $A$ til en øy $C$. <br>
Båten skal kjøre innom land på en kystlinje på et punkt $B$ for å hente ferskvann. Punktet kan være hvor som helst langs kystlinjen. Båten skal reise en så kort som mulig avstand for å spare drivstoff.

Kystlinjen er $9$ km lang. Øy $A$ ligger $2$ km fra land og øy $C$ ligger $4$ km fra land. En strandkiosk $S$ er plassert på starten av kystlinja.

Se figuren nedenfor.


:::{plot}
width: 70%
axis: off
xmin: -1
xmax: 10
ymax: 5
ymin: -2
hline: 0, -1, 10, solid
vline: 0, 0, 2, dashed, gray
vline: 9, 0, 4, dashed, gray
point: (0, 2)
point: (4, 0)
point: (9, 4)
line-segment: (0, 2), (4, 0), black, solid
line-segment: (4, 0), (9, 4), black, solid
vline: 0.65, 0, 0.4, solid, black
hline: 0.4, 0, 0.65, solid, black
vline: 8.35, 0, 0.4, solid, black
hline: 0.4, 9, 8.35, solid, black
text: 4, 0, "$B$", top-center
text: 0, 2, "$A$", top-left
text: 9, 4, "$C$", top-right
lw: 1.5
point: (0, 0)
text: 0, -0.2, "$S$", bottom-left
bar: (0, -0.3), 4, horizontal
text: 2, -0.3, "$x$ km", bottom-center
bar: (0, -0.8), 9, horizontal
text: 4.5, -0.8, "9 km", bottom-center
bar: (-0.5, 0), 2, vertical
text: -0.5, 1, "2 km", center-left
bar: (9.5, 0), 4, vertical
text: 9.5, 2, "4 km", center-right
:::






::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem lengden båten må kjøre fra $A$ til $C$ dersom den går i land $1$ km fra strandkiosken. 




:::::::::::::


:::::::::::::{tab-item} b
Lag en modell $L$ som gir lengden $L(x)$ som båten må kjøre dersom den går i land en avstand $x$ fra strandkiosken.



:::::::::::::



:::::::::::::{tab-item} c
Bestem hvor langt unna strandkiosken båten må gå i land for å få kortest mulig reisevei fra $A$ til $C$.



:::::::::::::


::::::::::::::


:::::::::::::::



---



::::::::::::::::{exercise} Oppgave 7
---
level: 3
---

Anna skal reise fra en holme som ligger $8$ km fra strandkanten. $12$ km fra det punktet på stranden som ligger nærmest holmen, ligger det en hytte. 
Anna kan ro med en fart på $2$ km/t og gå med en fart på $6$ km/t. Anna kan gå i land i hvilket som helst punkt $\ell$ på veien.

Se figuren nedenfor. 

:::{plot}
width: 70%
axis: off
xmin: -1
xmax: 13
ymax: 10
ymin: -2
point: (0, 8)
point: (4, 0)
point: (12, 0)
line-segment: (0, 8), (4, 0), blue, solid
hline: 0, -1, 13, solid, gray
vline: 0, 0, 8, dashed, gray
hline: 0, 4, 12, solid, red
text: 0, 8, "Holme", top-center
text: 12, 0, "Hytte", top-center
text: 4, 0, "$\ell$", top-right
bar: (-0.5, 0), 8, vertical
text: -0.5, 4, "8 km", center-left
bar: (0, -0.5), 4, horizontal
text: 2, -0.5, "$x$ km", bottom-center
bar: (0, -1.4), 12, horizontal
text: 6, -1.4, "12 km", bottom-center
text: 2, 4, "I vann", top-right
text: 8, -0.2, "På land", bottom-center
:::


:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem hvor lang tid Anna bruker til hytta dersom hun ror i land $6$ km fra det punktet på stranden som ligger nærmest holmen.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T = 6 \, \mathrm{t}
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker Pytagoras' setning til å regne ut hvor langt Anna må ro for å komme i land $6$ km fra det punktet på stranden som ligger nærmest holmen. Da får vi at:

$$
L_\mathrm{robåt} = \sqrt{6^2 + 8^2} \, \mathrm{km} = \sqrt{100} \, \mathrm{km} = 10 \, \mathrm{km}.
$$

Siden Anna ror med en fart på $2$ km/t, bruker hun tiden

$$
T_\mathrm{robåt} = \frac{L_\mathrm{robåt}}{2 \, \mathrm{km/t}} = \frac{10 \, \mathrm{km}}{2 \, \mathrm{km/t}} = 5 \, \mathrm{t}
$$

til å ro til stranden. Hun må deretter gå $12 - 6 = 6$ km til hytta. Siden hun går med en fart på $6$ km/t, bruker hun tiden

$$
T_\mathrm{gåtur} = \frac{6 \, \mathrm{km}}{6 \, \mathrm{km/t}} = 1 \, \mathrm{t}
$$

til å gå til hytta. Den totale tiden hun bruker til hytta blir derfor

$$
T = T_\mathrm{robåt} + T_\mathrm{gåtur} = 5 \, \mathrm{t} + 1 \, \mathrm{t} = 6 \, \mathrm{t}.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} b
Lag en modell $T$ som viser mange timer $T(x)$ Anna bruker på å reise til hytta dersom hun ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen. 

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T(x) = \dfrac{\sqrt{x^2 + 8^2}}{2} + \dfrac{12 - x}{6}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Hvis Anna ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen, må hun ro en avstand på

$$
L_\mathrm{robåt}(x) = \sqrt{x^2 + 8^2}
$$

Anna ror med en fart på $2$ km/t, så tiden hun bruker til å ro blir

$$
T_\mathrm{robåt}(x) = \frac{L_\mathrm{robåt}(x)}{2} = \frac{\sqrt{x^2 + 8^2}}{2}.
$$

Siden avstanden er 12 km fra punktet på strandlinja nærmest holmen bort til hytta, så må hun gå

$$
L_\mathrm{gåtur}(x) = 12 - x
$$

kilometer til hytta. Anna går med en fart på $6$ km/t, så tiden hun bruker til å gå blir

$$
T_\mathrm{gåtur}(x) = \frac{L_\mathrm{gåtur}(x)}{6} = \frac{12 - x}{6}.
$$

Dermed vil en modell for tiden Anna bruker til hytta når hun ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen være gitt ved

$$
T(x) = T_\mathrm{robåt}(x) + T_\mathrm{gåtur}(x) = \frac{\sqrt{x^2 + 8^2}}{2} + \frac{12 - x}{6}.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} c
Bestem hvor Anna må gå i land for at hun skal bruke minst mulig tid på å reise til hytta. <br>
Hva er den kortest tiden Anna kan bruke?


:::::{admonition} Fasit
---
class: answer, dropdown
---
* Anna må gå i land ved $x \approx 2.83 \, \mathrm{km}$ for å få kortest mulig reisetid.
* Anna bruker da $T \approx 5.77 \, \mathrm{t}$ på reisen.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å finne ut hvor Anna må gå i land for at hun skal bruke minst mulig tid på å reise til hytta, løser vi likningen $T'(x) = 0$ med CAS for å finne $x$-koordinaten til et eventuelt bunnpunkt for $T$:


:::{figure} ./figurer/oppgave_9/c.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed vil Anna bruke minst mulig tid dersom hun går i land ved

$$
x = 2 \sqrt{2} \, \mathrm{km} \approx 2.83 \, \mathrm{km}.
$$

Da bruker hun ca. $5.77$ timer på reisen. 

Vi bør dobbeltsjekke at dette svarer til et bunnpunkt ved å regne ut $T(x)$ i endepunktene og sjekke at verdiene vi får er høyere:

:::{figure} ./figurer/oppgave_9/exercise.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

* Hvis Anna ror båten direkte til nærmeste punkt på stranden, bruker hun $T(0) = 6$ timer. 
* Hvis Anna ror båten hele veien til hytta, bruker hun $T(12) \approx 7.21$ timer.


**Konklusjon**:
* Anna må gå i land ved $x \approx 2.83 \, \mathrm{km}$ for å få kortest mulig reisetid.
* Anna bruker da $T \approx 5.77 \, \mathrm{t}$ på reisen.

:::::

::::::::::::::

:::::::::::::::


::::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
En halvsirkel er gitt ved

$$
x^2 + y^2 = 4 \qder y \geq 0.
$$

Et rektangel har hjørnene $(-a, 0)$, $(a, 0)$, $(a, f(a))$ og $(-a, f(-a))$ der $f$ er funksjonen som beskriver halvsirkelen. 

Se figuren nedenfor.


:::{plot}
width: 70%
ticks: off 
xmin: -2.5
xmax: 2.5
ymin: -0.1
ymax: 2.5
function: sqrt(4 - x**2), (-2, 2), f
polygon: (-1.5, 0), (1.5, 0), (1.5, f(1.5)), (-1.5, f(-1.5)), blue, 0.2
point: (-1.5, 0)
point: (1.5, 0)
point: (1.5, f(1.5))
point: (-1.5, f(-1.5))
axis: equal
text: -1.5, 0, "$(-a, 0)$", bottom-center
text: 1.5, 0, "$(a, 0)$", bottom-center
text: 1.5, f(1.5), "$(a, f(a))$", top-right
text: -1.5, f(-1.5), "$(-a, f(-a))$", top-left
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::

Lag en systematisk oversikt over arealet av rektangelet for ulike verdier av $a \in [0, 2]$ og finn et estimat på hvilken verdi av $a$ som gir størst mulig areal.

:::::::::::::


:::::::::::::{tab-item} b
:::{ggb-popup}
---
layout: sidebar
---
:::

Lag en grafisk framstilling som viser sammenhengen mellom arealet $A(a)$ av rektangelet og $a$.

Bestem det største mulige arealet rektangelet kan ha.

:::::::::::::



:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Bestem en eksakt verdi for det største arealet rektangelet kan ha.
:::::::::::::


::::::::::::::





:::::::::::::::



---





:::::::::::::::{exercise} Oppgave 9

:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved 

$$
f(x) = ax^3 + bx^2, \quad x \in [0, 8]
$$

En trekant $\triangle ABC$ er dannet ved at $A$ er i origo, $B$ er er punkt på $x$-aksen og $C$ er et punkt på grafen til $f$ med samme $x$-koordinat som $B$.

:::{plot}
width: 60%
function: -2 * x**3 + 16 * x**2, (0, 8), f
xmin: -1
xmax: 9
ymin: -10
ymax: 160
polygon: (0, 0), (4, 0), (4, f(4)), blue, 0.2
ticks: off
point: (0, 0)
point: (4, 0)
point: (4, f(4))
text: 0, 0, "$A$", bottom-left
text: 4, 0, "$B$", bottom-right
text: 4, f(4), "$C$", top-left
fontsize: 26
:::

Om trekanten får du vite at:

* Arealet av trekanten er $7$ når koordinatene til $B$ er $(1, 0)$.
* Arealet av trekanten er størst når koordinatene til $B$ er $(6, 0)$.

Bestem $a$ og $b$. 


::::{answer}
$$
a = -2 \and b = 16
$$
::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 10
En lysstråle ble først observert i et punkt $A(1000, 0)$ i luften og deretter i et punkt $B(10000, -1000)$ i vann. Alle avstander er målt i meter. 

Lyset reiser med en fart på $300 \, \mathrm{m/ \mu s}$ i luft og $225 \, \mathrm{m/ \mu s}$ i vann. Her står $1 \, \mu s$ for 1 mikrosekund og er det samme som én milliondel av ett sekund. Lyset vil velge den veien mellom punktene $A$ og $B$ som gir kortest mulig reisetid.

Se figuren nedenfor.



Bestem hvor lang tid lysstrålen brukte fra $A$ til $B$.



:::{plot}
width: 70%
xmin: -1000
xmax: 11000
ymax: 1100
ymin: -1200
ticks: off
axis: off
point: (0, 1000)
point: (10000, -1000)
point: (7000, 0)
text: 0, 1000, "$A$", top-left
text: 10000, -1000, "$B$", bottom-right
text: 7000, 0, "$M$", top-right
vector: 0, 1000, 7000, -1000, red
vector: 7000, 0, 3000, -1000, red
vline: 0, 0, 1000, dashed, gray
vline: 10000, 0, -1000, dashed, gray
hline: 0, -5000, 15000, solid, gray
bar: (-500, 0), 1000, v
bar: (10500, 0), -1000, v
text: -500, 500, "1000 m", center-left
text: 10500, -500, "1000 m", center-right
text: 8000, 800, "Luft", center-left
text: -800, -800, "Vann", center-left
bar: (0, -1100), 10000, h
text: 5000, -1100, "10000 m", bottom-center
figsize: (6, 4)
:::


:::{cas-popup}
:::

:::{ggb-popup}
:::


:::::::::::::::



---



::::::::::::::::{exercise} Oppgave 11

:::{cas-popup}
---
layout: sidebar
---
:::



En takrenne skal lages i form av et åpent trapes ved å brette to sidekanter fra et flatt rektangel slik at alle sidelengder i takrenna er $10$ cm og takrennen har en høyde på $x$ cm. Se figuren nedenfor.


:::{plot}
width: 70%
axis: off
xmin: -8.5
xmax: 18.5
ymin: -2
ymax: 8
line-segment: (0, 0), (10, 0), black, solid
line-segment: (0, 0), (-8, 6), black, solid
line-segment: (10, 0), (18, 6), black, solid
text: 5, 0, "10 cm", bottom-center
text: -4, 3, "10 cm", center-left
text: 14.2, 3, "10 cm", center-right
hline: 6, -8, 18, dashed, gray
vline: 0, 0, 6, dashed, gray
vline: 10, 0, 6, dashed, gray
text: 0, 3, "$x$ cm", center-right
lw: 1.5
figsize: (6, 4)
:::



:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem tverrsnittsarealet $T$ av takrenna dersom høyden av takrenna er $6$ cm.



::::{answer}
$$
T = 60 \, \mathrm{cm^2}. 
$$
::::



::::::::::::::


::::::::::::::{tab-item} b
Lag en modell $T$ som gir tverrsnittsarealet $T(x)$ i $\mathrm{cm}^2$ når takrenna er $x$ cm høy.



::::{answer}
$$
T(x) = 10x + x\sqrt{100 - x^2}
$$
::::

::::::::::::::


::::::::::::::{tab-item} c
Bestem hvilken høyde som lar mest mulig vann strømme gjennom takrenna til enhver tid.

::::{answer}
$$
x = 5\sqrt{3} \, \mathrm{cm} \approx 8.66 \, \mathrm{cm}
$$
::::
::::::::::::::

:::::::::::::::


::::::::::::::::



---






::::::::::::::::{exercise} Oppgave 12
---
level: 3
---


:::{plot}
width: 80%
axis: off, equal
xmin: -0.5
xmax: 10.5
ymax: 3
ymin: -1
lw: 1.5
hline: 0, 0, 10, solid, black
vline: 3, 0, 3, solid, black
vline: 7, 0, 3, solid, black
line-segment: (0, 0), (3, 3), black, solid
line-segment: (7, 3), (10, 0), black, solid
line-segment: (3, 3), (7, 3), black, solid
text: 1.5, 0, "$x$", bottom-center
text: 5, 0, "$y$", bottom-center
text: 8.5, 0, "$x$", bottom-center
text: 3, 1.5, "$x$", center-right
text: 7, 1.5, "$x$", center-left
text: 5, 3, "$y$", top-center
vline: 2.6, 0, 0.4, solid, black
hline: 0.4, 2.6, 3, solid, black
hline: 0.4, 7, 7.4, solid, black
vline: 7.4, 0, 0.4, solid, black
figsize: (7, 3)
:::



Else skal gjerde inn tre områder for å lage en grønnsakshage. Det største området skal ha form som et rektangel og de to minste som likebeinte rettvinklede trekanter. Se figuren ovenfor.

Else skal sette opp gjerde langs alle linjestykkene vist i figuren ovenfor. <br>
Hun har til sammen 100 m gjerde som hun vil bruke.

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Hvor stor blir arealet av grønnsakhagen dersom hun velger at katetene i trekantene skal være $8$ meter?


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A = 245.5 \, \mathrm{m}^2
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Først må vi bestemme hvor lange linjestykkene $y$ i figuren er. Vi vet at $x = 8$ meter. Til sammen summerer linjestykkene til $L = 100$ meter. Vi kan skrive den samlede lengden av linjestykkene som

$$
L = \underbrace{2x}_{\mathrm{kateter}} + \underbrace{2x + 2y}_{\mathrm{rektangel}} + \underbrace{2\sqrt{2}x}_{\mathrm{hypotenuser}} = 100
$$

der vi har brukt Pytagoras' setning til å finne at begge hypotenusene i de rettvinklede trekantene må være 

$$
h^2 = x^2 + x^2 \limplies h = \sqrt{2}x.
$$

Vi kan først løse likningen for $y$ slik at vi kan regne ut $y$ for en hver verdi av $x$:

$$
4x + 2y + 2\sqrt{2}x = 100 \liff 2x + y + \sqrt{2}x = 50
$$

som gir 

$$
y = 50 - (2 + \sqrt{2})x.
$$

Det samlede arealet til grønnsakhagen blir

\begin{align*}
    A &= A_{\mathrm{rektangel}} + 2A_{\mathrm{trekant}} \\
    \\
    &= xy + 2 \cdot \frac{1}{2}x^2 \\
    \\
    &= x\left(50 - (2 + \sqrt{2})x\right) + x^2 \\
    \\
    &= 50x - (2 + \sqrt{2})x^2 + x^2 \\
    \\
    &= 50x - (1 + \sqrt{2})x^2
\end{align*}


Vi kan definere en funksjon $A(x)$ i CAS og regne ut arealet for $x = 8$:

:::{figure} ./figurer/oppgave_7/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at arealet av grønnsakhagen er omtrent $A = 245.5 \, \mathrm{m}^2$ dersom katetene i trekantene er $8$ meter lange.


:::::

::::::::::::::

::::::::::::::{tab-item} b
Lag en oversikt som viser hvordan arealet av grønnsakhagen endrer seg dersom hun velger andre lengder på katetene. Av oversikten skal Else kunne se omtrent hvor lange katetene må være for at arealet av grønnsakhagen skal bli størst mulig.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker en grafisk framstilling av arealet $A(x)$ for å se hvordan arealet endrer seg med lengden på katetene. Vi kan bruke Geogebra-vinduet til å lage grafen til $A$ siden vi allerede har definert $A(x)$ i CAS.

:::{figure} ./figurer/oppgave_7/b.png
---
width: 100%
class: no-click, adaptive-figure
---
viser en grafisk fremstilling av arealet $A(x) \, \mathrm{m}^2$ på $y$-aksen når katetene i trekanten er $x$ meter lange. 
:::

Fra den grafiske framstillingen kan vi se at arealet er størst når katetene i trekanten er omtrent $x = 10$ meter lange fordi dette svarer til et toppunkt på grafen til $A$.
:::::


::::::::::::::


::::::::::::::{tab-item} c
Lag en modell $A$ som Else kan bruke for å regne ut arealet $A(x)$ av grønnsakhagen for ulike verdier av $x$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(x) = 50x - (1 + \sqrt{2})x^2.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi har allerede laget denne modellen i oppgave **a** som er gitt ved 

$$
A(x) = 50x - (1 + \sqrt{2})x^2.
$$
:::::

::::::::::::::


::::::::::::::{tab-item} d
Bruk modellen til å finne den lengden av katetene som vil gi det største arealet.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = (25\sqrt{2} - 25) \, \mathrm{m} \approx 10.36 \, \mathrm{m}.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme den kateten som gir størst mulig areal, bruker vi CAS og løser $A'(x) = 0$ for å bestemme $x$-koordinaten til toppunktet til $A$:

:::{figure} ./figurer/oppgave_7/d.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at arealet er størst når katetene i trekantene er 

$$
x = (25\sqrt{2} - 25) \, \mathrm{m} \approx 10.36 \, \mathrm{m}.
$$

Men *vet* vi at dette er et toppunkt? Ja, for den ledende koeffisienten til $A(x)$ er negativ, så vi *legger'n død* – og vi hadde strengt tatt grafen som viste det i oppgave **b** også.

:::::

::::::::::::::


::::::::::::::{tab-item} e
Bestem modellens gyldighetsområde.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
0 < x < \dfrac{50}{\sqrt{2} + 2}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Modellen er gyldig så lenge $A(x) > 0$ og $y > 0$. Vi løser den første ulikheten i CAS:


:::{figure} ./figurer/oppgave_7/e.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er $A(x) > 0$ når

$$
x \in \left\langle 0, 50 \sqrt{2} - 50 \right\rangle.
$$

Men vi må også sjekke at $y > 0$. Fra **a** vet vi at 

$$
y = 50 - (2 + \sqrt{2})x
$$

så vi løser ulikheten $y > 0$ i CAS:

:::{figure} ./figurer/oppgave_7/e2.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Kombinerer vi de to løsningene, ser vi at modellen er gyldig så lenge

$$
0 < x < \dfrac{50}{\sqrt{2} + 2}
$$

:::::


::::::::::::::

:::::::::::::::

::::::::::::::::




---






:::::::::::::::{exercise} Oppgave 13
---
level: 3
---

Isabel er industridesigner. Hun arbeider med et design på bokser med form som sylindre.


:::{plot}
width: 80%
ellipse: (0, 5), 3, 0.5, black, solid
ellipse: (0, 0), 3, 0.5, black, solid
line-segment: (-3, 0), (-3, 5), black, solid
line-segment: (3, 0), (3, 5), black, solid
figsize: (3, 4)
ymin: -1
axis: off
align: right
bar: (3.8, 0), 5, v
text: 3.8, 2.5, "$h$", center-right
bar: (0, 6), 3, h
text: 1.5, 6, "$r$", top-center
hline: 5, 0, 3, dashed, gray
:::

Formel for å regne ut volumet av en boks med radius $r$ og høyde $h$ er

$$
V = \pi r^2 h
$$

Formel for å regne ut arealet av overflaten av boksen er 

$$
\mathcal{O} = \pi  r^2 + 2\pi r  h
$$

Isabel lurer på hvor stor radius hun bør velge og hvor høye boksene må være, når hver boks skal ha 
* et volum $V$ på $450 \, \mathrm{cm}^3$
* minst mulige overflate $\mathcal{O}$

Isabel ser at når hun har gitt volum og radius, kan hun regne ut høyden ved å bruke formelen $V = \pi \cdot r^2 \cdot h$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
perspective: S
---
:::


Lag en oversikt som vist nedenfor. Gjør beregninger og fyll inn verdiene som mangler.

:::{clear}
:::

| Radius, $r$ (cm) | Høyde, $h$ (cm) | Overflate, $\mathcal{O}$ (cm$^2$) | Volum, $V$ (cm$^3$) |
|:---:|:---:|:---:|:---:|
| 2 | 35.8  | 462.6 | 450 |
| 4 |  |   | 450 |
| 6 |  |   | 450 |
| 8 |  |   | 450 |

:::::{solution}
Vi kan skrive om formelen for volum slik at vi kan bestemme høyden $h$ gitt et volum $V$ og en radius $r$ som:

$$
V = \pi \cdot r^2 \cdot h \liff h = \dfrac{V}{\pi \cdot r^2}
$$

Deretter lager vi et regneark der vi fyller ut tabellen:

:::{figure} ./figurer/oppgaver/oppgave_12/a_regneark.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

Nedenfor vises en oversikt over formlene som er brukt i regnearket:

:::{figure} ./figurer/oppgaver/oppgave_12/a_regneark_med_formler.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

:::::

:::::::::::::


:::::::::::::{tab-item} b

:::{ggb-popup}
---
layout: sidebar
---
:::



Sett opp et funksjonsuttrykk Isabel kan bruke, og lag en grafisk framstilling som viser sammenhengen mellom radius og overflate.


:::{clear}
:::

:::::{solution}
Vi kan lage et funksjonsuttrykk $O(r)$ for overflaten $O$ av boksen for en gitt høyde $r$. Volumet $V = 450$, så vi kan sette opp et likningssystem for å bestemme $O(r)$. Vi løser likningssystemet med CAS:

:::{figure} ./figurer/oppgaver/oppgave_12/b_formel.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

som betyr at vi kan skrive 

$$
O(r) = \dfrac{\pi r^3 + 900}{r} \and h = \dfrac{450}{\pi r^2}.
$$

Deretter kan vi lage en grafisk framstilling av funksjonen $O(r)$: 

:::{plot}
width: 100%
function: (pi * x**3 + 900) / x, (0.0001, 100), blue
xmin: -2
xmax: 22
ymin: -1000
ymax: 5000
xstep: 2
ystep: 1000
xlabel: $r / \mathrm{cm}$
ylabel: $O(r) / \mathrm{cm}^2$, -50
:::





:::::

:::::::::::::


:::::::::::::{tab-item} c


:::{cas-popup}
:::


:::{ggb-popup}
:::



Hvor står må radius i boksene være for at overflaten skal bli minst mulig? <br>
Hvor stor blir overflaten da?

:::::{solution}
For å bestemme hvilken radius som gir minst mulig overflate, så kan vi løse likningen

$$
O'(r) = 0
$$

Deretter kan vi regne ut $O(r)$ i dette punktet. Vi gjør dette med CAS:

:::{figure} ./figurer/oppgaver/oppgave_12/c.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

Ut ifra den grafiske framstillingen fra **b** kan vi være sikre på at løsningen her gir et bunnpunkt og dermed den minste overflaten. Vi har da at boksen har minst overflate dersom 

$$
r \approx 5.23 \, \mathrm{cm}
$$

som gir en overflate på ca. $258 \, \mathrm{cm}^2$.



:::::

:::::::::::::

::::::::::::::




:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 14

:::{plot}
align: right
width: 100%
ellipse: (0, 4), 2, 0.7, solid, black
line-segment: (0, 0), (2, 4), solid, black
line-segment: (0, 0), (-2, 4), solid, black
nocache:
vline: 0, 0, 4, dashed, gray
hline: 4, 0, 2, dashed, gray
text: 0, 2, "$h$", center-right
text: 1, 4, "$r$", top-center
text: 1, 2, "$\ell$", bottom-right
figsize: (4, 4)
xmin: -3
xmax: 3
ymin: -1
ymax: 5
ticks: off
axis: off
line-segment: (0.3, 4), (0.3, 3.7), solid, gray
line-segment: (0, 3.7), (0.3, 3.7), solid, gray
:::


En kjegle har radius $r$, høyde $h$ og sidelengde $\ell$.

Formlene for overflatearealet $A$ og volumet $V$ til kjeglen er gitt ved

$$
A = \pi r^2 + \pi r \ell \qog V = \frac{1}{3} \pi r^2 h.
$$

Sidelengden $\ell$ er gitt ved 

$$
\ell = \sqrt{r^2 + h^2}.
$$


En kjegle skal ha volumet $12\pi \, \mathrm{cm}^3$ og minst mulig overflate.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en oversikt som vist nedenfor. Gjør beregninger og fyll inn verdiene som mangler.

| Radius $r$ (cm)| Høyde $h$ (cm) | Overflate $A$ (cm$^2$) | Volum $V$ (cm$^3$) |
|:---:|:---:|:---:|:---:|
| 1 | |  | 12$\pi$ |
| 2 | |  | 12$\pi$ |
| 3 | |  | 12$\pi$ |
| 4 | |  | 12$\pi$ |
| 5 | |  | 12$\pi$ |

:::::::::::::


:::::::::::::{tab-item} b
Sett opp et funksjonsuttrykk som viser sammenhengen mellom overflatearealet og radius.

Lag en grafisk framstilling av funksjonen.

:::::::::::::


:::::::::::::{tab-item} c
Hva må radius være for at overflaten skal bli minst mulig?

Hvor stort er overflatearealet da?
:::::::::::::


::::::::::::::



:::::::::::::::



---





:::::::::::::::{exercise} Oppgave 15


:::{cas-popup}
---
layout: sidebar
---
:::



En kurve er gitt ved grafen til funksjonen $f(x) = x^2$. I samme figur er et punkt $P(6, 3)$. 
Et linjestykke $\ell$ går fra punktet $P$ til et punkt på grafen.

Bestem koordinatene til punktet på grafen som gjør at $\ell$ blir kortest mulig. Bestem et eksakt uttrykk for lengden av $\ell$ i dette tilfellet.

:::{plot}
width: 70%
function: x**2, f
point: (5, 3)
text: 5, 3, "$P(6, 3)$", top-right
ymin: -1 
ymax: 8
xmin: -3
hline: 3, 2.5, 5, dashed, gray
vline: 2.5, 3, f(2.5), dashed, gray
point: (2.5, f(2.5))
text: 2.5, f(2.5), "$(x, f(x))$", top-right
line-segment: (5, 3), (2.5, f(2.5)), red, solid
text: 3.7, 4.5, "$\ell$", top-right
ticks: off
polygon: (2.5, 3), (2.8, 3), (2.8, 3.4), (2.5, 3.4)
:::

::::{answer}
* Koordinatene til punktet på grafen er $(2, 4)$
* Lengden til linjestykket er da $\sqrt{17}$
::::


::::{solution}
Avstanden fra punktet $P(6, 3)$ til et punkt på grafen $(x, f(x))$ kan vi uttrykke ved hjelp av Pytagoras' setning:

$$
d(x) = \sqrt{(x - 6)^2 + (f(x) - 3)^2} = \sqrt{(x - 6)^2 + (x^2 - 3)^2}
$$


For å bestemme ekstremalpunktene til $d$, må vi løse $d'(x) = 0$ og sjekke at $d''(x) > 0 i punktet for å sikre at det er et bunnpunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_9/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $d'(x) = 0$ når $x = 2$. Vi ser også at $d''(2) > 0$ som betyr at $d$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $x = 2$ et bunnpunkt. Derfor vil linjestykket $\ell$ bli kortest mulig når det går fra $P(6, 3)$ til punktet $(2, f(2)) = (2, 4)$ på grafen. Vi ser også at $d(2) = \sqrt{17}$ som er lengden av linjestykket i dette tilfellet.

::::


:::::::::::::::




---





:::::::::::::::{exercise} Oppgave 16
:::{cas-popup}
---
layout: sidebar
---
:::


En likebeint trekant skal innskrives i en sirkel med radius $1$. 

Bestem en eksakt verdi for det største arealet en slik trekant kan ha.


:::{plot}
width: 50%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
fontsize: 30
:::


::::{hints} Vanskelig å komme i gang? Her er en hjelpefigur!
Nedenfor vises en mindre rettvinklet trekant som er tegnet inn som du kan bruke for å hjelpe deg å finne et uttrykk for arealet av den store trekanten.

:::{plot}
width: 55%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
line-segment: (0, 0), (0, sin(-pi/4)), black, dashed
line-segment: (0, 0), (cos(pi + pi/4), sin(pi + pi/4)), black, dashed
text: 0.5 * (cos(pi + pi/4)), 0.5 * (sin(pi + pi/4)) + 0.15, "$1$", center-center
text: 0 + 0.1, 0.5 * sin(-pi/4), "$x$", center-center
text: 0.5 * cos(pi + pi/4), sin(pi + pi/4) - 0.1, "$\ell$", center-center
fontsize: 30
polygon: (0, sin(-pi/4)), (-0.15, sin(-pi/4)), (-0.15, sin(-pi/4) + 0.15), (0, sin(-pi/4) + 0.15)
:::
::::


::::{answer}
$$
\dfrac{3\sqrt{3}}{4}
$$
::::


::::{solution}
:::{plot}
align: right
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
line-segment: (0, 0), (0, sin(-pi/4)), black, dashed
line-segment: (0, 0), (cos(pi + pi/4), sin(pi + pi/4)), black, dashed
text: 0.5 * (cos(pi + pi/4)), 0.5 * (sin(pi + pi/4)) + 0.15, "$1$", center-center
text: 0 + 0.1, 0.5 * sin(-pi/4), "$x$", center-center
text: 0.5 * cos(pi + pi/4), sin(pi + pi/4) - 0.1, "$\ell$", center-center
fontsize: 30
polygon: (0, sin(-pi/4)), (-0.15, sin(-pi/4)), (-0.15, sin(-pi/4) + 0.15), (0, sin(-pi/4) + 0.15)
:::
Vi lager en hjelpefigur der vi lager en mindre rettvinklet som vi kan bruke til å finne et uttrykk for arealet av den store trekanten som vist til høyre.

Vi trenger å et uttrykk for grunnlinja og høyden til trekanten for å kunne finne et uttrykk for arealet.

Fra Pytagoras' setning har vi at 

$$
\ell^2 + x^2 = 1^2
$$

Vi kan løse denne likningen for $\ell$:

$$
\ell = \sqrt{1 - x^2}
$$

:::{clear}
:::

Grunnlinjen $g$ til den store trekanten er da $g = 2\ell$. 

Høyden til trekanten vil være $h = x + 1$. 

Arealet $A$ av trekanten kan da skrives som:

$$
A = \dfrac{g \cdot h}{2} = \dfrac{2\ell \cdot h}{2} = \ell \cdot h
$$

Setter vi inn uttrykket for $\ell$ og $h$, får vi funksjonen

$$
A(x) = \ell \cdot h = \sqrt{1 - x^2} \cdot (x + 1) = (x + 1)\sqrt{1 - x^2}
$$


For å bestemme det største arealet $A$ vi kan få, så løser vi $A'(x) = 0$ og sjekker at $A''(x) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:


:::{figure} ./figurer/oppgave_12/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $x = \dfrac{1}{2}$ er et ekstremalpunkt og vi ser at $A''\left(\dfrac{1}{2}\right) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $x = \dfrac{1}{2}$ et toppunkt. Derfor vil arealet $A$ bli størst mulig når $x = \dfrac{1}{2}$. Fra utskriften kan vi da også konkludere at det eksakte største arealet er

$$
A\left(\dfrac{1}{2}\right) = \dfrac{3\sqrt{3}}{4}
$$

::::


:::::::::::::::




---





:::::::::::::::{exercise} Oppgave 17



:::{cas-popup}
---
layout: sidebar
---
:::


En kjegle med sirkulær grunnflate med radius $r$ og høyde $h$ er innskrevet i en kule med radius $1$. 

Volumet $V$ av en slik kjegle er gitt ved 

$$
V = \dfrac{\pi r^2 h}{3}
$$


Se figurene nedenfor.

::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
line-segment: (0, 1), (cos(-pi/6), sin(-pi/6))
line-segment: (0, 1), (cos(pi + pi/6), sin(pi + pi/6))
ellipse: (0, 0), 1, 0.2, gray, dashed
ellipse: (0, sin(-pi/6)), cos(-pi/6), 0.2, red, dashed
line-segment: (0, sin(-pi/6)), (cos(-pi/6), sin(-pi/6)), black, solid
text: 0.5 * cos(-pi/6), sin(-pi/6) - 0.1, "$r$", center-center
bar: (1.1, -0.5), 1.5, vertical
text: 1.05, 0.25, "$h$", center-right
fontsize: 30
lw: 3
:::

:::{plot}
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
line-segment: (0, 1), (cos(-pi/6), sin(-pi/6))
line-segment: (0, 1), (cos(pi + pi/6), sin(pi + pi/6))
line-segment: (0, sin(-pi/6)), (cos(-pi/6), sin(-pi/6)), black, solid
line-segment: (0, sin(-pi/6)), (-cos(-pi/6), sin(-pi/6)), black, dotted
line-segment: (0, 0), (cos(-pi/6), sin(-pi/6)), solid, black
line-segment: (0, 0), (0, sin(-pi/6)), solid, black
text: 0.5 * cos(-pi/6), sin(-pi/6) - 0.1, "$s$", center-center
bar: (1.1, -0.5), 1.5, vertical
text: 1.05, 0.25, "$h$", center-right
fontsize: 30
lw: 3
text: 0 - 0.1, 0.5 * sin(-pi/6), "$\ell$", center-center
text: 0.5 * cos(-pi/6), 0 - 0.1, "$r$", center-center
polygon: (0, sin(-pi/6)), (0.1, sin(-pi/6)), (0.1, sin(-pi/6) + 0.1), (0, sin(-pi/6) + 0.1)
line-segment: (0, 0), (0, 1), dotted, black
text: 0 + 0.1, 0.4, "$r$", center-left
:::
::::


Bestem det største volumet en slik kjegle kan ha. 


::::{answer}
$$
V_\text{størst} = \dfrac{32}{81}\pi
$$
::::

::::{solution}

Volumet av en kjegle er gitt ved 

$$
V = \dfrac{Gh}{3}
$$

der $G$ er arealet av grunnflaten og $h$ er høyden. Arealet av grunnflaten er gitt ved

$$
G = \pi r^2
$$

Høyden $h$ er gitt ved 

$$
h = 1 + \ell
$$

Fra figuren kan vi bruke Pytagoras' setning på den rettvinkla trekanten til å skrive opp sammenhengen:

$$
r^2 + \ell^2 = 1^2
$$

Fra dette finner vi at 

$$
\ell = \sqrt{1 - r^2}
$$

Det betyr at høyden er 

$$
h = 1 + \sqrt{1 - r^2}
$$

Dermed vil volumet av kjeglen kunne uttrykkes som en funksjon av $r$:

$$
V(r) = \dfrac{\pi r^2 \left(1 + \sqrt{1 - r^2}\right)}{3}
$$

Vi bruker CAS til å bestemme ekstremalpunktene til $V$ og avgjør hvilke av punktene som er toppunkter ved å sjekke at $V''(r) < 0$ i punktet:

:::{figure} ./figurer/oppgave_13/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Fra utskriften ser vi at $V'(r) = 0$ når 

$$
r = 0 \or r = \pm \dfrac{2\sqrt{2}}{3}
$$

Når $r = 0$ så er $V(r) = 0$ så dette er opplagt ikke det største volumet. Den eneste løsningen som gir mening er derfor $r = \dfrac{2\sqrt{2}}{3}$. Vi ser også at $V''\left(\dfrac{2\sqrt{2}}{3}\right) < 0$ som betyr at $V$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $r = \dfrac{2\sqrt{2}}{3}$ et toppunkt. Derfor vil volumet $V$ bli størst mulig når $r = \dfrac{2\sqrt{2}}{3}$. Fra utskriften kan vi da også konkludere at det eksakte største volumet er

$$
V_\text{størst} = \dfrac{32}{81}\pi
$$




::::
:::::::::::::::

