# Vår 2026



## Del 1

> 3 timer uten hjelpemidler


:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = x^2 - x - 12.
$$

Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.

::::{answer}
$(-3, 0)$ og $(4, 0)$.
::::


::::{solution}
Grafen til $f$ skjærer $x$-aksen i de punktene der $f(x) = 0$. Vi løser denne likningen med $abc$-formelen:

$$
x = \dfrac{-(-1) \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot (-12)}}{2 \cdot 1} = \dfrac{1 \pm 7}{2}.
$$

som gir

$$
x = -3 \or x = 4. 
$$

Altså skjærer grafen til $f$ gjennom $x$-aksen i $(-3, 0)$ og $(4, 0)$.
::::

:::::::::::::


:::::::::::::{tab-item} b
En andregradsfunksjon $g$ er gitt ved

$$
g(x) = 3(x + 5)(x - 1).
$$

Bestem koordinatene til bunnpunktet til grafen til $g$.


::::{answer}
$(-2, -27)$.
::::

::::{solution}
Symmetrilinja (som gir $x$-koordinaten til bunnpunktet) vil ligge midt mellom nullpunktene. Vi kan lese av at nullpunktene er $x = -5$ og $x = 1$. Symmetrilinja er gitt ved gjennomsnittet av de to nullpunktene:

$$
x_0 = \dfrac{-5 + 1}{2} = -2.
$$

Vi finner $y$-koordinaten ved å regne ut $g(-2)$:

$$
g(-2) = 3(-2 + 5)(-2 - 1) = 3 \cdot 3 \cdot (-3) = -27.
$$

Altså er koordinatene til bunnpunktet $(-2, -27)$.
::::

:::::::::::::



:::::::::::::{tab-item} c
Bestem $a$, $b$ og $c$ slik at likningen nedenfor er en identitet.

$$
-2x^2 - 8x + 4 = a(x - b)^2 + c
$$




::::{answer}
$$
a = -2 \and b = -2 \and c = 12.
$$
::::

::::{solution}
Uttrykket på høyre side er gitt ved andregradsuttrykket på ekstremalpunktsform der $a$ er den ledende koeffisienten, $b$ er symmetrilinja og $c$ er $y$-koordinaten til ekstremalpunktet. 

Den ledende koeffisienten er $a = -2$ siden den ledende koeffisienten på venstre side er $-2$.

Symmetrilinja finner vi ved 

$$
x_0 = \dfrac{-(-8)}{2 \cdot (-2)} = -2.
$$

Altså må $b = -2$.

For å finne $c$ regner vi ut verdien til uttrykket på venstre side når $x = -2$:

$$
-2 \cdot (-2)^2 - 8 \cdot (-2) + 4 = -8 + 16 + 4 = 12.
$$

Altså har vi at 

$$
a = -2 \and b = -2 \and c = 12.
$$
::::

:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
I figuren nedenfor vises grafen til en andregradsfunksjon $f$.

Bestem $f(x)$.

Husk å forklare hvordan du har tenkt. 


:::{plot}
width: 70%
function: -2 * (x + 1)**2 + 8, f
xmin: -6
xmax: 4
ymin: -6
ymax: 10 
:::



::::{answer}
> Det er flere korrekte svar. Nedenfor vises de tre mulighetene.

Nullpunktsform:
: $f(x) = -2(x + 3)(x - 1)$.

Ekstremalpunktsform:
: $f(x) = -2(x + 1)^2 + 8$.

Standardform:
: $f(x) = -2x^2 - 4x + 6$.
::::


::::{solution}
> Vi trenger bare å finne $f(x)$ for én av de tre representasjonene vi har sett på for andregradsfunksjoner: Nullpunktsform, ekstremalpunktsform eller standardform. Nedenfor viser vi alle tre. 


**Nullpunktsform**

Vi kan bestemme $f(x)$ på nullpunktsform ved å ta utgangspunkt i nullpunktene til funksjonen. Vi kan se at grafen skjærer $x$-aksen i $x = -3$ og $x = 1$ som betyr at

$$
f(x) = a(x + 3)(x - 1).
$$

Flytter vi oss én enhet fra ekstremalpunktet langs $x$-aksen, endres $y$-verdien med $-2$. Det betyr at $a = -2$. Ergo får vi at

$$
f(x) = -2(x + 3)(x - 1).
$$


**Ekstremalpunktsform**
Vi har fortsatt at den ledenede koeffisienten er $a = -2$. Vi kan lese av at ekstremalpunktet er $(-1, 8)$ som betyr at

$$
f(x) = -2(x + 1)^2 + 8
$$


**Standardform**
På standardform vil $f(x)$ være gitt ved

$$
f(x) = ax^2 + bx + c.
$$

Symmetrilinja er $x = -1$ som betyr at

$$
x = -\dfrac{b}{2a} = -1 \implies b = 2a.
$$

Det betyr at 

$$
f(x) = ax^2 + 2ax + c.
$$

Grafen til $f$ skjærer $x$-aksen i $(0, 6)$ som betyr at $c = 6$. Dermed har vi at 

$$
f(x) = ax^2 + 2ax + 6.
$$

For å bestemme verdien til $a$ setter vi inn ett kjent punkt på grafen til $f$. Vi bruker $(1, 0)$ som gir

$$
f(1) = 0 \liff a + 2a + 6 = 0 \liff a = -2.
$$

Altså er 

$$
f(x) = -2x^2 - 4x + 6.
$$

::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
Funksjonen $f$ er gitt ved

$$
f(x) = x^3 + 5x^2 + 8x + 4
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktene til $f$.


::::{answer}
$$
x = -2 \qog x = -1.
$$
::::


::::{solution}
Alle mulige heltallige nullpunkter vil kunne dele kontantleddet til $f(x)$. Det betyr at kandidatene for heltallige nullpunkter er

$$
x \in \{\pm 1, \pm 2, \pm 4\}
$$

Siden alle leddene er positive, er det bare mulig å finne negative nullpunkter. Vi tester $x = -1$:

:::{horner}
---
p: x^3 + 5x^2 + 8x + 4
x: -1
width: 60%
---
:::

Her ble resten null som betyr at 

$$
x^3 + 5x^2 + 8x + 4 = (x + 1)(x^2 + 4x + 4) = (x + 1)(x + 2)^2.
$$

der vi i siste overgang har brukt 1. kvadratsetning. Det betyr at nullpunktene til $f$ er 

$$
x = -2 \qog x = -1.
$$


::::



:::::::::::::



:::::::::::::{tab-item} b
Løs ulikheten $f(x) < 0$.


::::{answer}
$$
x \in \langle \gets, -1 \rangle \setminus \{-2\}.
$$

> En alternativ måte å uttrykke løsningen på kan være $x \in \langle \gets, -2\rangle \cup \langle -2, -1 \rangle$.

::::

::::{solution}
For å løse ulikheten $f(x) < 0$ tegner vi et fortegnsskjema:

:::{signchart-2}
width: 80%
function: x**3 + 5 * x**2 + 8 * x + 4, f(x)
:::

Fra fortegnslinja til $f(x)$ ser vi at $f(x) < 0$ når 

$$
x \in \langle \gets, -1 \rangle \setminus \{-2\}.
$$

> En alternativ måte å uttrykke løsningen på kan være $x \in \langle \gets, -2\rangle \cup \langle -2, -1 \rangle$.


::::

:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
En rasjonal funksjon $f$ er gitt ved

$$
f(x) = \dfrac{4x + 8}{2x^2 - 8}
$$

Hvilke av påstandene nedenfor er riktige? 

Husk å begrunne svarene dine og vurdere hver påstand. 

Påstand 1
: Grafen til $f$ har to vertikale asymptoter.

Påstand 2
: Grafen til $f$ har en horisontal asymptote $y = 0$.

Påstand 3
: Grafen til $f$ har nøyaktig ett nullpunkt.



::::{answer}
Påstand 1
: Feil.

Påstand 2
: Riktig.

Påstand 3
: Feil.
::::


::::{solution}
For å vurdere de tre påstandene starter vi først med å nullpunktsfaktorisere telleren og nevneren, og deretter forkorte brøken så mye som mulig. 

For tellerpolynomet har vi at

$$
4x + 8 = 4(x + 2).
$$

For nevnerpolynomet har vi at

$$
2x^2 - 8 = 2(x^2 - 4) = 2(x + 2)(x - 2).
$$

Dermed kan vi forkorte brøken til

$$
f(x) = \dfrac{4(x + 2)}{2(x + 2)(x - 2)} = \dfrac{2}{x - 2}, \quad x \neq -2.
$$

Nå er vi klare til å vurdere påstandene.

Påstand 1
: Grafen til $f$ har bare én vertikal asymptote i $x = 2$ siden den forkortede brøken gir oss bare ett nullpunkt i nevneren som er $x = 2$. Det betyr at påstand 1 er feil.

Påstand 2
: Nevnerpolynomet er av en høyere grad enn tellerpolynomet som betyr at den horisontale asymptoten må være $y = 0$. Derfor er påstanden riktig.

Påstand 3
: Grafen til $f$ har ingen nullpunkter siden den forkortede brøken gir oss en konstant i telleren ikke kan være lik null. Dermed er påstand 3 feil.
::::




:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5
Anna har skrevet programmet nedenfor.


:::{code-block} python
---
linenos:
---
def f(x):
    return 2 * x**3 - 3 * x**2 - 12 * x - 4


x = -3
while f(x) < f(x + 1):
    x = x + 1

print((x, f(x)))
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hva er det Anna prøver å finne ut med programmet sitt?


::::{answer}
Programmet finner toppunktet til grafen til $f$.
::::

::::{solution}
Programmet starter med $x = -3$ og øker verdien til $x$ med $1$ så lenge $f(x) < f(x + 1)$. Det betyr at programmet stadig sjekker om den neste funksjonsverdien er større enn den forrige. Med én gang dette ikke er sant, så stopper `while`{l=python}-løkka og skriver ut $(x, f(x))$ for den siste verdien av $x$. Det betyr at programmet finner toppunktet til grafen til $f$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem verdiene som skrives ut av programmet når det kjøres.


::::{answer}
$$
(-1, 3)
$$
::::

::::{solution}
Siden programmet finner toppunktet til grafen til $f$, kan vi avgjøre verdiene programmet skriver ut ved å løse $f'(x) = 0$. 

Vi starter med å finne $f'(x)$:

$$
f'(x) = (2 x^3 - 3x^2 - 12x - 4)' = 6x^2 - 6x - 12.
$$

Deretter løser vi $f'(x) = 0$:

$$
f'(x) = 0 \liff 6x^2 - 6x - 12 = 0 \liff x^2 - x - 2 = 0.
$$

Vi bruker $abc$-formelen for å løse denne likningen:

$$
x = \dfrac{-(-1) \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot (-2)}}{2 \cdot 1} = \dfrac{1 \pm 3}{2}
$$

som gir

$$
x = -1 \or x = 2.
$$

Den første av de to vil gi oss toppunktet (hvis ikke ville programmet aldri kjørt i utgangspunktet). Vi finner $y$-koordinaten til punktet ved:

$$
f(-1) = 2 \cdot (-1)^3 - 3 \cdot (-1)^2 - 12 \cdot (-1) - 4 = -2 - 3 + 12 - 4 = 3.
$$

Ergo skriver programmet ut $(-1, 3)$.
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 6
Synne satte inn penger på en sparekonto med $3~\%$ rente per år for fem år siden. I dag har Synne $100~000$ kr på kontoen.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å regne ut hvor mye Synne satte inn på kontoen for fem år siden? 

:::::{grid} 1 2 3 3
---
gutter: 2
---
::::{grid-item-card}
**A**
^^^
$$
100~000 \cdot 0.97^5
$$
::::


::::{grid-item-card}
**B**
^^^
$$
\dfrac{100~000}{1.03^5}
$$
::::


::::{grid-item-card}
**C**
^^^
$$
100~000 \cdot 1.03^5
$$
::::

::::{grid-item-card}
**D**
^^^
$$
100~000 \cdot 0.97^{-5}
$$
::::


::::{grid-item-card}
**E**
^^^
$$
\dfrac{100~000}{0.97^5}
$$
::::

::::{grid-item-card}
**F**
^^^
$$
100~000 \cdot 1.03^{-5}
$$
::::
:::::


::::{answer}
Alternativ B og F.
::::


::::{solution}
Siden sparekontoen har en rente på $3~\%$ per år, betyr at vekstfaktoren $V$ til den prosentvise veksten er

$$
V = 100~\% + 3~\% = 103~\% = 1.03.
$$

Den opprinnelige verdien $x$ vil da være gitt ved

$$
100~000 = x \cdot V^5 = x \cdot 1.03^5 \liff x = \dfrac{100~000}{1.03^5} = 100~000 \cdot 1.03^{-5}.
$$

der vi har brukt at $\dfrac{1}{1.03^5} = 1.03^{-5}$ per definisjon.


Ergo er alternativ B og alternativ F riktige uttrykk for regnestykket.

::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
Grafen til den deriverte $f'$ til en funksjon $f$ er vist i figuren nedenfor.


:::{plot}
width: 50%
yticks: off
grid: off
ymax: 10
xmin: -5
xmax: 5
function: (x + 2) * (x - 1) * (x - 3), f'
fontsize: 26
:::


Hvilken figur nedenfor viser grafen til $f$?

Husk å begrunne svaret ditt.



::::{multi-plot2}
---
rows: 2
cols: 2
yticks: off
grid: off
---
:::{plot}
yticks: off
function: -(1/4 * x**4 - 2/3 * x**3 - 5/2 * x**2 + 6*x) - 5
ymin: -14
ymax: 14 
text: 4, 8, "A", bbox
fontsize: 26
:::


:::{plot}
yticks: off
function: 0.25 * (x + 2)**2 * (x - 1) * (x - 3)
ymin: -14
ymax: 14 
text: 4, 8, "B", bbox
fontsize: 26
:::



:::{plot}
yticks: off
function: (1/4 * x**4 - 2/3 * x**3 - 5/2 * x**2 + 6*x) + 5
ymin: -14
ymax: 14 
text: 4, 8, "C", bbox
fontsize: 26
:::


:::{plot}
yticks: off
function: -1/4 * ((1/4 * x**4 - 2/3 * x**3 - 5/2 * x**2 + 6*x))
text: 4, 4, "D", bbox
fontsize: 26
:::
::::


::::{answer}
Alternativ C.
::::


::::{solution}
Grafen til $f'$ skjærer $x$-aksen i 

$$
x = -2 \qog x = 1 \qog x = 3.
$$

Dette vil være $x$-koordinatene til ekstremalpunktene til grafen til $f$ som betyr at alternativ B kan utelukkes.

Fra grafen til $f'(x)$ kan vi se at $f'(x) < 0$ når $x < -2$ som betyr at grafen til $f$ synker når $x < -2$. Dette stemmer bare overens med graf C. 

Ergo er det riktige svaret alternativ C.
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 8
Grafen til en rasjonal funksjon $f$ er vist i figuren nedenfor.

:::{plot}
width: 70%
function: 2 * (x + 2) * (x - 2) / ((x + 1) * (x - 1)), f
vline: -1, dashed, red
vline: 1, dashed, red
hline: 2, dashed, red
ymin: -12
ymax: 12
ystep: 2
:::


Bestem et mulig uttrykk for $f(x)$.

Husk å forklare hvordan du har tenkt.



::::{answer}
$$
f(x) = \dfrac{2(x + 2)(x - 2)}{(x + 1)(x - 1)}.
$$
::::


::::{solution}
Vi kan skrive $f(x)$ som

$$
f(x) = \dfrac{P(x)}{Q(x)}
$$

der $P(x)$ og $Q(x)$ er polynomer. 

Grafen til $f$ har en horisontal asymptote $y = 2$ som betyr at både $P(x)$ og $Q(x)$ må ha samme grad.

* Nullpunktene til $f$ er gitt ved $x = -2$ og $x = 2$ som betyr at $P(x) = a(x + 2)(x - 2)$.
* De vertikale asymptotene til $f$ er gitt ved $x = -1$ og $x = 1$ som betyr at $Q(x) = (x + 1)(x - 1)$.

For å sikre at grafen til $f$ får riktig horisontal asymptote, må vi velge at $a = 2$. Dermed har vi at

$$
f(x) = \dfrac{2(x + 2)(x - 2)}{(x + 1)(x - 1)}.
$$
::::



:::::::::::::::



---



## Del 2

> 2 timer med hjelpemidler


:::::::::::::::{exercise} Oppgave 1
---
aids: 
---
En mynt blir sluppet fra ulike høyder. Farten mynten hadde rett før den traff bakken for ulike høyder er vist i tabellen nedenfor.


:::{table}
---
transpose:
---
labels: Høyde (meter), Fart (meter per sekund)
$0.5$, $3.1$
$1.0$, $4.4$
$1.5$, $5.4$
$2.0$, $6.2$
$3.0$, $7.7$
$4.0$, $8.9$
:::


<br>

Sammenhengen mellom farten og høyden kan beskrives av en modell $F$ på formen

$$
F(x) = a \cdot x^b
$$

der mynten blir sluppet $x$ meter over bakken og har farten $F(x)$ målt i meter per sekund rett før den treffer bakken.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene i tabellen ovenfor til å bestemme $a$ og $b$.



::::{answer}
$$
a = 4.3974 \and b = 0.507
$$
::::

::::{solution}
Vi legger inn opplysningene i et regneark som følger:


:::{figure} ./figurer/del_2/1/regneark.png
---
class: no-click, adaptive-figure
width: 30%
---
:::

Deretter bruker vi {ggb-icon}`mode_regression` og velger *potensfunksjon* for å bestemme verdiene til $a$ og $b$. Da finner vi som følger:

:::{figure} ./figurer/del_2/1/regresjonsmodell.png
---
class: no-click, adaptive-figure
width: 80%
---
:::


Ergo er

$$
a = 4.3974 \and b = 0.507
$$

::::


:::::::::::::



:::::::::::::{tab-item} b
Den største farten en mynt kan oppnå på grunn av luftmotstand er $20$ meter per sekund.

Gjør beregninger og anslå gyldighetsområdet til modellen.



::::{answer}
$$
x \in [0, 19.84]
$$
::::

::::{solution}
Vi bruker verdiene for $a$ og $b$ vi fant i forrige deloppgave og lager oss en potensfunksjon

$$
F(x) = a \cdot x^b = 4.3974 \cdot x^{0.507}.
$$

Deretter løser vi $F(x) < 20$ med CAS for å finne gyldighetsområdet til modellen:


:::{figure} ./figurer/del_2/1/gyldighetsområde.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Vi ser at farten til mynten holder seg nedenfor $F(x) = 20$ omtrentlig når

$$
x \in [0, 19.84]
$$

som er et anslag på gyldighetsområdet til modellen ut ifra opplysningen om den største mulige farten på grunn av luftmotstand.


::::
:::::::::::::


::::::::::::::



:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 2
---
aids: true
---
Funksjonen $f$ er gitt ved

$$
f(x) = -x^3 + 6x^2, \quad x \in [0, 6].
$$

Punktene $A$, $B$, $C$ og $D$ danner et rektangel. Punktet $A$ ligger i origo, punktet $B(k, 0)$ ligger på $x$-aksen, punktet $C$ ligger på grafen til $f$ og punktet $D$ ligger på $y$-aksen. 

Se figuren nedenfor.


:::{plot}
fontsize: 26
width: 60%
ticks: off
function: -x**3 + 6 * x**2, (0, 6), f
xmin: -0.5
xmax: 7
ymax: 40
let: k = 3
point: (0, 0)
point: (k, 0)
point: (k, f(k))
point: (0, f(k))
text: 0, 0, $A$, bottom-left
text: k, 0, "$B(k, 0)$", bottom-right
text: k, f(k), $C$, top-center
text: 0, f(k), $D$, top-left
polygon: (0, 0), (k, 0), (k, f(k)), (0, f(k)), blue, 0.2
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet dersom $k = 2$.


::::{answer}
$$
32
$$
::::

::::{solution}
Arealet av rektangelet er gitt ved 

$$
A = 2 \cdot f(2) = 2 \cdot (-2^3 + 6 \cdot 2^2) = 32.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem den verdien for $k$ som gir størst mulig areal av rektangelet.



::::{answer}
$$
k = \dfrac{9}{2}.
$$
::::

::::{solution}
Vi setter opp en funksjon for arealet av rektangelet:

$$
A(k) = k \cdot f(k).
$$

For å avgjøre hvilken verdi av $k$ som gir størst mulig arealet, løser vi $A'(k) = 0$ siden dette gir kandidater for ekstremalpunktene til $A(k)$. Vi gjør dette med CAS:


:::{figure} ./figurer/del_2/2/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Vi får at enten så er $k = 0$ eller så er $k = 9/2$. Siden $k = 0$ vil gi oss et areal på null vil den verdien av $k$ som gir størst mulig areal være

$$
k = \dfrac{9}{2}.
$$

::::

:::::::::::::

::::::::::::::




:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
---
aids: true
---

Nedenfor vises de fire første figurene i en figurfølge. Arealet av den første figuren er $1$.


::::{multi-plot2}
---
rows: 1
cols: 4
width: 100%
align: center
---

:::{plot}
axis: equal
axis: off
fontsize: 45
fill-polygon: (0, 0), (1, 0), (1/2, sqrt(3)/2), blue, 0.2
polygon: (0, 0), (1, 0), (1/2, sqrt(3)/2)
text: 1/2, -0.35, "Figur 1", top-center
:::

:::{plot}
axis: equal
axis: off
fontsize: 45
fill-polygon: (0, 0), (1/2, 0), (1/4, sqrt(3)/4), blue, 0.2
polygon: (0, 0), (1/2, 0), (1/4, sqrt(3)/4)
fill-polygon: (1/2, 0), (1, 0), (3/4, sqrt(3)/4), blue, 0.2
polygon: (1/2, 0), (1, 0), (3/4, sqrt(3)/4)
fill-polygon: (1/4, sqrt(3)/4), (3/4, sqrt(3)/4), (1/2, sqrt(3)/2), blue, 0.2
polygon: (1/4, sqrt(3)/4), (3/4, sqrt(3)/4), (1/2, sqrt(3)/2)
text: 1/2, -0.35, "Figur 2", top-center
:::

:::{plot}
axis: equal
axis: off
fontsize: 45

fill-polygon: (0, 0), (1/4, 0), (1/8, sqrt(3)/8), blue, 0.2
polygon: (0, 0), (1/4, 0), (1/8, sqrt(3)/8)
fill-polygon: (1/4, 0), (1/2, 0), (3/8, sqrt(3)/8), blue, 0.2
polygon: (1/4, 0), (1/2, 0), (3/8, sqrt(3)/8)
fill-polygon: (1/8, sqrt(3)/8), (3/8, sqrt(3)/8), (1/4, sqrt(3)/4), blue, 0.2
polygon: (1/8, sqrt(3)/8), (3/8, sqrt(3)/8), (1/4, sqrt(3)/4)

fill-polygon: (1/2, 0), (3/4, 0), (5/8, sqrt(3)/8), blue, 0.2
polygon: (1/2, 0), (3/4, 0), (5/8, sqrt(3)/8)
fill-polygon: (3/4, 0), (1, 0), (7/8, sqrt(3)/8), blue, 0.2
polygon: (3/4, 0), (1, 0), (7/8, sqrt(3)/8)
fill-polygon: (5/8, sqrt(3)/8), (7/8, sqrt(3)/8), (3/4, sqrt(3)/4), blue, 0.2
polygon: (5/8, sqrt(3)/8), (7/8, sqrt(3)/8), (3/4, sqrt(3)/4)

fill-polygon: (1/4, sqrt(3)/4), (1/2, sqrt(3)/4), (3/8, 3*sqrt(3)/8), blue, 0.2
polygon: (1/4, sqrt(3)/4), (1/2, sqrt(3)/4), (3/8, 3*sqrt(3)/8)
fill-polygon: (1/2, sqrt(3)/4), (3/4, sqrt(3)/4), (5/8, 3*sqrt(3)/8), blue, 0.2
polygon: (1/2, sqrt(3)/4), (3/4, sqrt(3)/4), (5/8, 3*sqrt(3)/8)
fill-polygon: (3/8, 3*sqrt(3)/8), (5/8, 3*sqrt(3)/8), (1/2, sqrt(3)/2), blue, 0.2
polygon: (3/8, 3*sqrt(3)/8), (5/8, 3*sqrt(3)/8), (1/2, sqrt(3)/2)

text: 1/2, -0.35, "Figur 3", top-center
:::

:::{plot}
axis: equal
axis: off
fontsize: 45

macro: tri(x, y, s)
    fill-polygon: (x, y), (x + s, y), (x + s/2, y + sqrt(3)/2*s), blue, 0.2
    polygon: (x, y), (x + s, y), (x + s/2, y + sqrt(3)/2*s)
endmacro

macro: sier3(x, y, s)
    use: tri(x, y, s/8)
    use: tri(x + s/8, y, s/8)
    use: tri(x + s/16, y + sqrt(3)/16*s, s/8)

    use: tri(x + s/4, y, s/8)
    use: tri(x + 3*s/8, y, s/8)
    use: tri(x + 5*s/16, y + sqrt(3)/16*s, s/8)

    use: tri(x + s/8, y + sqrt(3)/8*s, s/8)
    use: tri(x + s/4, y + sqrt(3)/8*s, s/8)
    use: tri(x + 3*s/16, y + 3*sqrt(3)/16*s, s/8)

    use: tri(x + s/2, y, s/8)
    use: tri(x + 5*s/8, y, s/8)
    use: tri(x + 9*s/16, y + sqrt(3)/16*s, s/8)

    use: tri(x + 3*s/4, y, s/8)
    use: tri(x + 7*s/8, y, s/8)
    use: tri(x + 13*s/16, y + sqrt(3)/16*s, s/8)

    use: tri(x + 5*s/8, y + sqrt(3)/8*s, s/8)
    use: tri(x + 3*s/4, y + sqrt(3)/8*s, s/8)
    use: tri(x + 11*s/16, y + 3*sqrt(3)/16*s, s/8)

    use: tri(x + s/4, y + sqrt(3)/4*s, s/8)
    use: tri(x + 3*s/8, y + sqrt(3)/4*s, s/8)
    use: tri(x + 5*s/16, y + 5*sqrt(3)/16*s, s/8)

    use: tri(x + s/2, y + sqrt(3)/4*s, s/8)
    use: tri(x + 5*s/8, y + sqrt(3)/4*s, s/8)
    use: tri(x + 9*s/16, y + 5*sqrt(3)/16*s, s/8)

    use: tri(x + 3*s/8, y + 3*sqrt(3)/8*s, s/8)
    use: tri(x + s/2, y + 3*sqrt(3)/8*s, s/8)
    use: tri(x + 7*s/16, y + 7*sqrt(3)/16*s, s/8)
endmacro

use: sier3(0, 0, 1)
text: 1/2, -0.35, "Figur 4", top-center
:::
::::


La $T_n$ være antall blå trekanter i figur $n$ og $A_n$ være arealet av én blå trekant i figuren.

Vi lar $F_n$ være arealet av alle de fargelagte trekantene i figur $n$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en oversikt som vist nedenfor. Fyll ut tabellen.


:::{table}
labels: $n$, $T_n$, $A_n$, $F_n$
$1$, $1$, $1$, $1 \cdot 1$
$2$, , , 
$3$, , ,
$4$, , ,
:::



::::{answer}
:::{table}
labels: $n$, $T_n$, $A_n$, $F_n$
$1$, $1$, $1$, $1 \cdot 1$
$2$, $3$, $\dfrac{1}{4}$, $3 \cdot \dfrac{1}{4}$
$3$, $3^2$, $\dfrac{1}{4^2}$, $3^2 \cdot \dfrac{1}{4^2}$
$4$, $3^3$, $\dfrac{1}{4^3}$, $3^3 \cdot \dfrac{1}{4^3}$
:::
::::


:::::::::::::



:::::::::::::{tab-item} b
Bestem et uttrykk for $F_n$.


::::{answer}
$$
T_n = 3^{n - 1} \cdot \dfrac{1}{4^{n - 1}} = \left(\dfrac{3}{4}\right)^{n - 1} \qfor n = 1, 2, 3, \dots
$$
::::


::::{solution}
Fra tabellen kan vi generalisere til at

$$
A_n = \dfrac{1}{4^{n - 1}} \and T_n = 3^{n - 1} \qfor n = 1, 2, 3, \dots
$$

Siden $F_n = T_n \cdot A_n$ for alle $n$, så har vi at

$$
T_n = 3^{n - 1} \cdot \dfrac{1}{4^{n - 1}} = \left(\dfrac{3}{4}\right)^{n - 1} \qfor n = 1, 2, 3, \dots
$$


::::

:::::::::::::



:::::::::::::{tab-item} c
Figurfølgen består av $100$ slike figurer som følger mønsteret ovenfor.

Lag et program som beregner det samlede arealet til alle de blå fargelagte trekantene.


:::{interactive-code}
# Din kode her


:::



::::{answer}
:::{code-block} python
---
linenos:
---
samlet_areal = 0
F = 1
for n in range(100):
    samlet_areal = samlet_areal + F
    F = F * 3/4

print(samlet_areal)
:::


som gir utskriften


:::{code-block} console
3.999999999998716
:::


::::


:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
---
aids: true
---

En skoleklasse skal på tur og overnatter på hotell.

Hotellet tilbyr rom med 2 senger eller 4 senger. Klassen får plass på 18 rom. Det er til sammen 48 senger. 

Hvor mange rom var det med $2$ senger og hvor mange rom var det med $4$ senger?


::::{answer}
$12$ rom med $2$ senger og $6$ rom med $4$ senger.
::::


::::{solution}
La $x$ være antall rom med $2$ senger og la $y$ være antall rom med $4$ senger. Da har vi at

\begin{align*}
x + y &= 18 && \mathrm{Antall \, rom}\\
2x + 4y &= 48 && \mathrm{Antall \, senger}
\end{align*}

Vi løser likningsystemet med CAS:


:::{figure} ./figurer/del_2/4/sol.png
---
class: no-click, adaptive-figure
width: 80%
---
:::


Altså er løsningen av likningsystemet

$$
x = 12 \and y = 6.
$$

Det betyr at det var $12$ rom med $2$ senger og $6$ rom med $4$ senger.



::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5
---
aids: true
---

:::{plot}
figsize: (6, 3)
width: 50%
axis: off
axis: equal
let: x = 4
let: y = 2
polygon: (0, 0), (x, 0), (x, x), (0, x), blue, 0.2
polygon: (x, x), (x + x, x), (x + x, x + y), (x, x + y), red, 0.2
polygon: (x, 0), (x + x, 0), (x + x, -y), (x, -y), red, 0.2
polygon: (0, 0), (-x, 0), (-x, -y), (0, -y), red, 0.2
polygon: (0, x), (-x, x), (-x, x + y), (0, x + y), red, 0.2
text: 0.5 * x, 0, "$x$", bottom-center
text: 0, 0.5 * x, "$x$", center-left
text: x + 0.5 * x, x, "$x$", bottom-center
text: x + x, x + 0.5 * y, "$y$", center-right
fontsize: 30
:::


Omkretsen av figuren ovenfor er $100$.


Bestem det største mulige arealet figuren kan ha.



::::{answer}
$$
A_\mathrm{størst} = 125
$$
::::


::::{solution}
Omkretsen til figuren tilfredsstiller likningen

$$
4x + 8x + 8y = 100 \liff 12x + 8y = 100.
$$

Arealet $A$ av figuren er gitt ved

$$
A = x^2 + 4xy.
$$

Vi løser den første likningen for $y$ slik at vi kan lage oss en funksjon $A(x)$ for arealet:

$$
12x + 8y = 100 \liff 8y = 100 - 12x \liff y(x) = \dfrac{100 - 12x}{8}
$$

Dermed har vi at

$$
A(x) = x^2 + 4x\cdot y(x) = x^2 + 4x \cdot \dfrac{100 - 12x}{8}
$$

For å bestemme det største mulige arealet av figuren, gjør vi som følger:
1. Løser $A'(x) = 0$ for å finne kandidater for ekstremalpunktene til $A(x)$.
2. Regner ut $A(x)$ for kandidatene for å finne det største arealet.

Dette gjør vi med CAS:


:::{figure} ./figurer/del_2/5/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Fra utregningene i CAS ser vi at det største mulige arealet av figuren er

$$
A_\mathrm{størst} = 125
$$


::::


:::::::::::::::