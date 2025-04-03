# Modellering (Del 2)

> Her kan du bruke digitale hjelpemidler som **CAS**, **graftegner** (Geogebra), **Python** og **regneark** til å løse oppgaver. 


:::::::::::::::{admonition} Oppgave 1 (Vår 2024)
---
class: check 
---
Tabellen nedenfor viser hvor mange bagetter en kantine har solgt hver av de siste sju ukene, og hvor stort overskudd salget har gitt.


| Solgte bagetter | 100 | 130 | 160 | 175 | 190 | 220 | 235 |
|------|---|---|---|---|---|---|---|
| Overskudd (kroner) | 1450 | 2300 | 3050 | 3365 | 3720 | 4140 | 4175 |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene ovenfor til å vise at funksjonen $O$ gitt ved 

$$
O(x) = -0.09x^2 + 51.04x - 2776.98
$$

er en god modell for hvor stort overskuddet en uke blir når kantinen produserer og selger $x$ bagetter i løpet av uken.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Først fyller vi inn datapunktene i et regneark:

:::{figure} ./oppgave_1/a/regneark.png
---
width: 30%
class: no-click
---
:::

Velger vi regresjonsanalyse og et polynom av grad $2$, får vi

:::{figure} ./oppgave_1/a/regresjonsmodell.png
---
width: 100%
class: no-click
---
:::

Vi kan altså se at 

$$
O(x) = -0.09x^2 + 51.04x - 2776.98
$$

er en god modell ut ifra regresjonsanalysen og datapunktene vi har brukt.

:::::

:::::::::::::

:::::::::::::{tab-item} b
Hvor mange bagetter må kantinen produsere og selge i løpet av en uke, ifølge modellen $O$, for at overskuddet skal bli størst mulig? 

Hvor stort blir dette overskuddet?

:::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $O$ vil ha et toppunkt siden $O$ er en andregradsfunksjon og ledende koeffisient er negativ. Da vil overskuddet blir størst mulig når $O'(x) = 0$. Vi løser likningen med CAS:

:::{figure} ./oppgave_1/b/sol.png
---
width: 100%
class: no-click
---
:::

som betyr at $O'(x) = 0$ når $x \approx 283.56$. Kantina må derfor produsere og selges ca. 284 bagetter for at overskuddet skal bli størst mulig.



:::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem stigningstallet til den rette linjen som går gjennom punktene $(100, O(100))$ og $(200, O(200))$. Gi en praktisk tolkning av svaret du får.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bestemmer stigningstallet til linja gjennom punktene $(100, O(100))$ og $(200, O(200))$ ved å regne ut den gjennomsnittlige vekstfarten til $O$ i intervallet $[100, 200]$. Dette gjør vi direkte med CAS:

:::{figure} ./oppgave_1/c/sol.png
---
width: 100%
class: no-click
---
:::

som gir oss ca. 24 kr per bagett. Den praktiske tolkning av tallet er at dersom kantina øker antall bagetter de produserer og selger fra $100$ til $200$, så vil overskuddet øke med ca $24$ kr per bagett i gjennomsnitt. 

:::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem den momentane vekstfarten når $x = 235$. Gi en praktisk tolkning av svaret du får.


::::{admonition} Løsning
---
class: solution, dropdown
---
Den momentane vekstfarten til $O$ i $x = 235$ er $O'(235)$. Vi regner ut dette med CAS:

:::{figure} ./oppgave_1/d/sol.png
---
width: 100%
class: no-click
---
:::

som gir at $O'(235) \approx 8.74$ kr per bagett. Den praktiske tolkningen av dette tallet er at dersom kantina øker antall bagetter de produserer og selger fra $235$ til $236$, så vil overskuddet øke med ca $8.74$ kr.
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 2 (Vår 2022)
---
class: check 
---
En fabrikk har en vanntank. Vannet i tanken skal tappes ut.

Anta at funksjonen $V$ gitt ved 

$$
V(x) = 2000 - 2000\cdot \left(1 - \dfrac{x}{40}\right)^2 \, , \quad 0 \leq x \leq 40
$$

kan brukes som en modell for hvor mange liter vann $V(x)$ som er tappet ut av tanken $x$ minutter etter tappingen startet.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $V(0)$. Gi en praktisk tolkning av svaret.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bestemmer $V(0)$ ved å bruke CAS:

:::{figure} ./oppgave_2/a/sol.png
---
width: 80%
class: no-click
---
:::

Altså er $V(0) = 0$ som forteller oss at når vi setter i gang å tappe ut vann, så har vi tappet ut $0$ liter med vann.
:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem verdimengden til $V$.


:::::{admonition} Fasit
---
class: solution, dropdown
---
$$
V(x) \in [0, 2000]
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra den praktiske situasjonen, vil det være naturlig at verdimengden er $V(x) \in [0, V_\mathrm{maks}]$ for et maksimalt volum $V_\mathrm{maks}$. For å bestemme dette kan vi regne ut verdien til $V(x)$ i endepunktene $x\in \{0, 40\}$. Vi regner ut for det sistenevnte punktet med CAS og finner:

:::{figure} ./oppgave_2/b/sol.png
---
width: 100%
class: no-click
---
:::

som betyr at $V(0) = 0$ og $V(40) = 2000$. Dermed vil verdimengden kunne beskrives som

$$
V(x) \in [0, 2000]
$$

som forteller oss ta vi til sammen har 2000 liter med vann i tanken. 

:::::

:::::::::::::


:::::::::::::{tab-item} c
Hvor lang tid vil det ta før halvparten av vannet er tappet ut av tanken?


:::::{admonition} Fasit
---
class: answer, dropdown
---
$11.72$ minutter.
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
For å avgjøre hvor lang tid det tar før halvparten av vannet er tappet ut, løser vi likningen

$$
V(x) = \dfrac{2000}{2} = 1000
$$

siden vi fant at det til sammen var 2000 liter med vann i tanken i oppgave **b**. Vi løser likningen med CAS:

:::{figure} ./oppgave_2/c/sol.png
---
width: 100%
class: no-click
---
:::

Her får vi to løsninger, men det er bare løsningen $x \in [0, 40]$ som er meningsfull, som betyr at det tar $11.72$ minutter før halvparten av vannet er tappet ut av tanken.
:::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem stigningstallet til den rette linjen som går gjennom punktene $(0, V(0))$ og $(30, V(30))$. Gi en praktisk tolkning av svaret du får. 


:::::{admonition} Fasit
---
class: answer, dropdown
---
$62.5$ liter per minutt tappes ut i gjennomsnitt de første 30 minuttene av tappingen.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Stigningstallet til den rette linjen gjennom $(0, V(0))$ og $(30, V(30))$ svarer til den gjennomsnittlige vekstfarten til $V(x)$ i intervallet $[0, 30]$. Vi regner ut dette med CAS:

:::{figure} ./oppgave_2/d/sol.png
---
width: 100%
class: no-click
---
:::

som betyr at stigningstallet til linja er $62.5$ liter per minutt. Den praktiske tolkningen av svaret er at det tappes ut $62.5$ liter per minutt i gjennomsnitt de første 30 minuttene av tappingen.

:::::

:::::::::::::


:::::::::::::{tab-item} e
Undersøk om det noen gang vil tappes ut mer enn 105 liter vann i løpet av ett minutt.


:::::{admonition} Løsning
---
class: answer, dropdown
---
Den praktiske tolkningen av den momentane vekstfarten $V'(x)$ er at den forteller oss omtrent hvor mye volumet med vann endrer dersom vi øker verdien av $x$ med $1$. Med andre ord

$$
V'(x) \approx V(x + 1) - V(x)
$$

som betyr at det er tilnærmet verdi for hvor mye vann som tappes ut i løpet av ett minutt. Siden spørsmålet handler om det tappes ut mer enn $105$ liter, betyr det at vi lurer på om 

$$
V'(x) < -105
$$

for noen $x \in [0, 40]$. Vi løser ulikheten med CAS:

:::{figure} ./oppgave_2/e/sol.png
---
width: 100%
class: no-click
---
:::

$$
V'(x) < -105 \liff x > 82
$$

som ikke ligger innenfor definisjonsmengden. Med andre ord finner vi at det *aldri* tappes ut mer enn $105$ liter vann i løpet av ett minutt.


:::::

:::::::::::::

::::::::::::::

:::::::::::::::





---


:::::::::::::::{admonition} Oppgave 3 (Vår 2024)
---
class: check
---
Lufttrykk måles ofte i hektopascal (hPa). Jo høyere over havet vi befinner oss, jo lavere er lufttrykket. Lufttrykket ved havets overflate er ca. 1000 hPa.


Når lufttrykket er lavere enn 1000 hPa, vil kokepunktet for vann være lavere enn $100 \degree \mathrm{C}$. Se tabellen nedenfor.

| Lufttrykk $\left(\mathrm{hPa}\right)$ | Kokepunkt for vann $\left(\degree \mathrm{C}\right)$ |
|------|---|
| $1000$ | $100$ |
| $500$ | $81.4$ |
| $200$ | $60.1$ |
| $80$ | $41.5$ |
| $40$ | $29$ |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en modell $K$ på formen 

$$
K(x) = a \cdot x^b
$$

som tilnærmet viser sammenhengen mellom lufttrykket $x$ hPa og kokepunktet $K(x) \, \degree \mathrm{C}$. 


::::{admonition} Løsning
---
class: solution, dropdown
---
Først fyller vi inn datapunktene i et regneark:

:::{figure} ./oppgave_3/a/regneark.png
---
width: 30%
class: no-click
---
:::

deretter bruker vi regresjonsanalyse og velger **potens** som modellklasse:

:::{figure} ./oppgave_3/a/regresjonsmodell.png
---
width: 100%
class: no-click
---
:::

Modellen vår $K$ er derfor gitt ved 

$$
K(x) = 7.56 \cdot x^{0.38}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Nedenfor vises en samtale mellom to elever:

Ari 
: Betyr dette at det ikke går an å få egg hardkokte oppe på et høyt fjell? 
: Et egg blir ikke hardkokt dersom temperaturen i vannet er lavere enn $85 \, \degree \mathrm{C}$.

Lisa
: Det kommer vel an på hvor høyt fjellet er?

Ari
: Jeg vil lage en modell som viser hvor høyt lufttrykket er $x$ kilometer over havets overflate. Jeg har lært at lufttrykket minker med ca. $12 \, \%$ per km. 

Lisa
: Jeg har lært at lufttrykket halveres for hver $5.5$ km. Jeg vil ta utgangspunkt i dette og lage en modell på samme form som den du lager, Ari.

---

**Lag modellene for Ari og Lisa.**

::::{admonition} Løsning
---
class: solution, dropdown
---
Modellen til Ari er en eksponentiell modell der vekstfaktoren er $0.88$ siden det er $12 \%$ nedgang per kilometer. Vi kaller modellen for $A$. Da har vi at 

$$
A(x) = 1000 \cdot 0.88^x
$$

siden $x$ er antall kilometer over havet og lufttrykket er $1000 hPa$ ved havnivå.


Modellen til Lisa er også en eksponentiell modell der vi vet at lufttrykket halveres for hver $5.5$ km. Vi lar $L$ være modellen til Lisa. Da har vi at 

$$
L(x) = 1000 \cdot b^x
$$

Siden lufttrykket halveres for hver $5.5$ km, betyr det at 

$$
L(5.5) = 500. 
$$

Vi må bestemme $b$ slik at dette stemmer. Vi gjør det med CAS:

:::{figure} ./oppgave_3/b/sol_lisa.png
---
width: 100%
class: no-click
---
:::

Vi ser at $b \approx 0.88$ akkurat som i Ari sin modell. Det er altså ingen nevneverdig forskjell mellom de to modellene, de er bare beskrevet på forskjellig måte.
::::

:::::::::::::


:::::::::::::{tab-item} c
Omtrent hvor høyt over havet er det mulig å få egg hardkokte?


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi finner først ut hvilket lufttrykk $x$ som gir $K(x) = 85$. Vi løser likningen med CAS:

:::{figure} ./oppgave_3/c/sol_del1.png
---
width: 100%
class: no-click
---
:::

som betyr at vi må ha et lufttrykk på omtrent $574.76$ hPa. Vi kan så bestemme ved hvilken høyde over havet dette lufttrykket er ved å bruke Ari sin modell i CAS:


:::{figure} ./oppgave_3/c/sol_del2.png
---
width: 100%
class: no-click
---
:::

som forteller oss at kokepunktet er på $85 \degree \mathrm{C}$ når vi er omtrent $4.3$ km over havet. Dermed er dette den størst høyden vi kan være på for å kunne lage hardkokte egg.

:::::



:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 4 (Høst 2024)
---
class: check
---
Funksjonen $P$ gitt ved 

$$
P(x) = 3600 \cdot 0.85^x + 600
$$


er en modell som viser hvor mange personer som abonnerte på papirutgaven av en avis $x$ år etter 2010. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis hvordan du på to ulike måter kan finne ut hvor mange person som abonnerte på papirutgaven av avisen i 2010. 


:::::{admonition} Løsning
---
class: solution, dropdown
---
1) **Metode 1: Regne ut $P(0)$** <br> 
Vi kan bruke funksjonsuttrykket og regne ut $P(0)$ siden $x = 0$ tilsvarer å 2010. Vi bruker CAS til å utføre dette:

:::{figure} ./oppgave_4/a/metode_1.png
---
width: 100%
class: no-click
---
:::

2) **Metode 2: Finne skjæringen med $y$-aksen** <br>
Vi bruker den grafiske representasjonen til $P$ og bestemmer skjæringen med $y$-aksen med en graftegner. Se figuren nedenfor.

:::{figure} ./oppgave_4/a/metode_2.png
---
width: 100%
class: no-click
---
:::

I utgangspunktet bruker vi bare kommandoen:

:::{figure} ./oppgave_4/a/skjæringspunkt.png
---
width: 60%
class: no-click
---
:::

som forteller oss at punktet $(0, 4200)$ ligger på grafen til $P$. Dermed er det 4200 personer som abonnerte på papirutgaven når $x = 0$ som tilsvarer i år 2010.

:::::



:::::::::::::


:::::::::::::{tab-item} b
Bestem stigningstallet til den rette linjen som går gjennom punktene $(4, P(4))$ og $(14, P(14))$. Gi en praktisk tolkning av svaret du får.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Stigningstallet til den rette linjen som går gjennom $(4, P(4))$ og $(14, P(14))$ er den gjennomsnittlige vekstfarten til $P$ i intervallet $[4, 14]$. Vi regner ut dette med CAS:

:::{figure} ./oppgave_4/b/sol.png
---
width: 100%
class: no-click
---
:::

Altså er stigningstallet til linja ca. $-151$. Den praktiske tolkningen er at antall abonnenter papirutgaven av avisen synker med 151 abonnenter per år i gjennomsnitt, i perioden fra 2014 til 2024.

:::::

:::::::::::::

:::::::::::::{tab-item} c
Bestem den momentane vekstfarten når $x = 10$. Gi en praktisk tolkning av svaret du får.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Den momentane vekstfarten til $P$ når $x = 10$, er gitt ved $P'(10)$. Vi regner ut dette med CAS:

:::{figure} ./oppgave_4/c/sol.png
---
width: 100%
class: no-click
---
:::

som betyr at 

$$
P'(10) \approx -116
$$

Den praktiske tolkningen av dette tallet er at det er det blir ca. 116 færre abonnenter fra år $x = 10$ til $x = 11$ som betyr at i løpet av år 2020, så vil det være ca. 116 person som kansellerer abonnementet sitt på papirutgaven av avisen. 

:::::

:::::::::::::


:::::::::::::{tab-item} d
I 2019 abonnerte 1000 personer på den digitale utgaven av avisen. Antallet personer som abonnerte på den digitale utgaven, økte med $5.5 \%$ hvert år fra 2019 til 2024.


I hvilket år var det for første gang flere personer som abonnerte på den digitale utgaven av avisen enn på papirutgaven?


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan sette opp en modell $D$ som gir antall abonnenter $D(t)$ på den digitale utgaven $t$ år etter 2019 slik at $t = 0$ svarer til år 2019. Siden det er prosentvis økning på $5.5 \%$ per år fra en startverdi på $1000$ abonnenter i 2019, vil modellen være en eksponentiell modell på formen

$$
D(t) = \underbrace{1000}_{\text{startverdi}} \cdot \underbrace{1.055^t}_{\mathrm{vekstfaktor}}
$$

For å kunne sammenligne $D(t)$ med $P(x)$, er det hjelpsomt å bytte variabel i én av modellene så vi kan sammenligne funksjonsverdiene direkte. Her kan vi for eksempel bytte variabel i $D(t)$ til $x$ slik at vi får en modell $D(x)$ som gir antall abonnenter på den digitale utgaven av avisen $x$ år etter 2010. Men samtidig må vi huske på at denne modellen kun er gyldig fra og med år 2019, altså når $x \geq 9$. Det betyr at vi kan skrive sammenhengen mellom $t$ og $x$ som 

$$
t = x - 9
$$

så lenge $x \geq 9$ siden $x = 9$ vil gi $t = 0$, $x = 10$ vil gi $t = 1$ osv. 

Da kan vi skrive om $D(t)$ til $D(x)$ ved å bytte variabelen slik vi har definert over:

$$
D(x) = 1000 \cdot 1.055^{x - 9}
$$

der modellen kun gir mening for $x \geq 9$ siden dette er fra og med år 2019. Med denne modellen, kan vi nå undersøke når antall papirabonnenter $P(x)$ er mindre enn antall digitale abonnenter $D(x)$ ved å løse ulikheten 

$$
P(x) < D(x)
$$

som vi gjør med CAS:

:::{figure} ./oppgave_4/d/sol.png
---
width: 100%
class: no-click
---
:::

Altså vil antall papirabonnenter bli lavere enn antall digitale abonnenter når $x > 11.58$ som betyr at det i løpet av år 2021 blir flere digitale abonnenter enn papirabonnenter.

:::::

:::::::::::::

::::::::::::::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 5 (Høst 2023)
---
class: check
---
En gruppe statistikere har sett på hvordan folketallet i et område har endret seg siden 1960, og laget en modell $F$ gitt ved 

$$
F(x) = \dfrac{1}{1000}\cdot \left(0.027 x^3 - 5.8 x^2 + 220x + 7900\right), \quad x \in [0, 80]
$$

for folketallet $F(x)$ tusen innbyggere i området $x$ år etter 1960.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis hvordan du på to ulike måter kan bestemme når folketallet var høyest ifølge modellen.


:::::{admonition} Løsning
---
class: solution, dropdown
---
**Metode 1: Løse $F'(x) = 0$** <br>
Siden løsningene av $F'(x) = 0$ gir ekstremalpunktene som vil være punkter når folketallet enten er lavest eller høyest, kan vi løse denne likningen for å avgjøre når folketallet var høyest. Vi gjør dette med CAS:

:::{figure} ./oppgave_5/a/metode_1.png
---
width: 100%
class: no-click
---
:::
Her får vi to kandidater 

$$
x \approx 22.5 \or x \approx 120.71.
$$

Men kun den første kandidaten ligger innenfor definisjonsmengden $D_F = [0, 80]$. Vi kan undersøke om det er toppunkt ved å regne ut $F(x)$ i to "nabopunkter" til $x = 22.5$ og sjekker om $F(22.5)$ er større enn begge. Vi gjør utregningen med CAS:

:::{figure} ./oppgave_5/a/metode_1_check.png
---
width: 100%
class: no-click
---
:::

som forteller oss at 

$$
F(22.5) > F(20) \and F(22.5) > F(25)
$$

så $x = 22.5$ svarer til et toppunkt. Dermed er det høyeste folketallet i området $x = 22.5$ år etter 1960 som tilsvarer i år 1982.


**Metode 2: Finne toppunktet grafisk** <br>
Vi kan også bruke den grafiske representasjonen til $F$ og bestemme toppunktet med en graftegner. Se figuren nedenfor.

:::{figure} ./oppgave_5/a/metode_2.png
---
width: 100%
class: no-click
---
viser grafen til $F$ der $y$-aksen viser folketallet i tusen innbyggere og $x$-aksen viser antall år etter 1960.
:::

Her har vi brukt følgende kommando i Geogebra for å bestemme koordinatene til toppunktet:

:::{figure} ./oppgave_5/a/metode_2_kommando.png
---
width: 60%
class: no-click
---
:::

som forteller oss at koordinatene til toppunktet er $(22.5, 10.22)$ som betyr at folketallet var høyest når $x = 22.5$ år etter 1960 som tilsvarer i år 1982.


:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem stigningstallet til den rette linjen som går gjennom punktene $(30, F(30))$ og $(70, F(70))$. Gi en praktisk tolkning av dette stigningstallet.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Stigningstallet til den rette linjen som går gjennom $(30, F(30))$ og $(70, F(70))$ er den gjennomsnittlige vekstfarten til $F$ i intervallet $[30, 70]$. Vi regner ut dette med CAS:

:::{figure} ./oppgave_5/b/sol.png
---
width: 80%
class: no-click
---
:::

Vi ser at stigningstallet til linja er ca. $-0.15$ som betyr at folketallet synker med ca. $150$ innbyggere per år i gjennomsnitt i perioden fra 1990 til 2030, iføle modellen.

:::::

:::::::::::::


:::::::::::::{tab-item} c
Når vil folketallet avta raskest ifølge modellen? 


:::::{admonition} Løsning
---
class: solution, dropdown
---
Folketallet vil avta raskest når den momentane vekstfarten $F'(x)$ er minst mulig *og* negativ. Vi må altså lete etter bunnpunktet til $F'(x)$. Vi kan gjøre dette ved å løse likningen $F''(x) = 0$. Det vil si, vi deriverer den deriverte $F'$ for å finne ut hvor mye $F'$ endrer seg, og så finner vi bunnpunktet til $F'$ for å bestemme når $F''(x) = 0$. Vi gjør dette med CAS:

:::{figure} ./oppgave_5/c/sol.png
---
width: 80%
class: no-click
---
:::

som betyr at når $x \approx 71.6$, altså i år 2031, vil folketallet avta raskest ifølge modellen. Vi kan være sikre på at dette er punktet hvor $F'(x)$ er minst mulig *og* negativ fordi grafen til $F$ synker mest her ved å referere tilbake til grafen til $F$ fra oppgave **a**. Grafen til $F$ synker etter at $x = 22.5$ frem til $x = 80$ og $F'(x)$ er negativ i hele dette intervallet. Tangenten til grafen til $F$ vil være "brattest" i $x = 71.6$, og siden stigningstallet er negativt, vil det svare til når folketallet avtar raskest ifølge modellen.

:::::

:::::::::::::

::::::::::::::

:::::::::::::::


<!-- 
:::::::::::::::{admonition} Oppgave 5 (Høst 2023)
---
class: check
---
Tabellen nedenfor viser antall personer i Norge som hadde fiske som hovedyrke noen år i perioden 1952 - 2022.

| År | 1952 | 1982 | 1992 | 2002 | 2012 | 2022 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Antall fiskere** | 65 956 |25 289 | 19 780 | 13 841 | 9 825 | 9 591 |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
La $x$ være antall år etter 1950 og bruk opplysningene i tabellen til å bestemme en modell $F$ som du mener kan brukes til å si noe om antall personer som har hatt fiske som hovedyrke i perioden 1952 - 2022.

:::::::::::::

:::::::::::::{tab-item} b
Hvor mange personer i Norge vil i 2050 ha fiske som hovedyrke ifølge modellen fra oppgave **a**? Vurder modellens gyldighetsområde.

:::::::::::::

::::::::::::::

:::::::::::::::

















 -->
