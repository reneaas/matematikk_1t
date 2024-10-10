# Oppgaver: Lage en matematisk modell
::::{admonition} Oppgave 1
---
class: problem-level-1
---
Lise handler på en perlebutikk der man kan velge perler i løsvekt. For å lage et smykke trenger man et kjede, det koster 15 kroner. I tillegg velger man selv hvor mange perler man vil ha på kjedet. Hver perle koster 2 kroner. 

Deloppgave 1
: Sett opp en funksjon som beskriver prisen per ferdige smykke som funksjon av antall perler du kjøper. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$P(p) = 15 + 2p$
:::

Deloppgave 2
: Det er maksimalt plass til 60 perler på et smykke. Sett opp en definisjonsmengde og en verdimengde for funksjon fra deloppgave 1. 

:::{admonition} Fasit
---
class: answer, dropdown
---
D_P = [0, 60]
V_P = [15, 135] 
:::

````{admonition} Oppgave 2
---
class: problem-level-1
---
I 1987 kostet en kroneis 6 kr. I 2022 hadde prisen steget til 27 kroner. Vi antar at prisutviklingen har vært tilnærmet lineær i perioden fra 1987 til 2022. 

Deloppgave 1
: Sett opp en lineær modell som beskriver prissstigningen. 

:::{admonition} Løsningsforslag
---
class: solution, dropdown
---
Vi lar $x$ være antall år etter 1987. Ettersom konstantleddet er prisen i startåret, setter vi $b = 6$. 

Fra 1987 til 2022 er det 35 år. På de 35 årene har prisen steget med 21 kroner. Vi finner da årlig prisstigning

$$ a = \frac{\Delta y}{\Delta x} = \frac{21}{35} = \frac{3}{5}$$

Vi kan da sette opp den lineære modellen $y = \frac{3}{5} + 6$. 
:::
````
Deloppgave 2
: Bestem definisjonsmengden og verdimengden til modellen. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$D_f = [0, \to \rangle $ 

$V_f = [6, \to \rangle $

:::


````{admonition} Oppgave 3
---
class: problem-level-2
---
Det er tre selskaper som tilbyr leie av elsparkesykler i Oslo (per juli 2024). I tabellen under vises oppstartspris og pris per minutt for de ulike selskapene. Selskapene har litt forskjellige tilbud til kundene sine. 

| Selskap | Oppstartspris [kr] | Pris per minutt [kr/min] | Pris per km [kr/km] |
| :---: | :---: | :---: | :---: |
| Voi | 10 | 3 | - |
| Bolt | 5 | - | 11.88 |
| Ryde | 10 | 2.5 | - |

<br>

Deloppgave 1
: Lag en modell $V$ som gir $V(t)$ kroner for $t$ minutter med kjøretid med en sparkesykkel fra Voi. Hvor mye koster det å kjøre sparkesykkelen i 8 minutter?

:::{admonition} Fasit
---
class: answer, dropdown
---
$V(t)= 3t + 10$

$V(8)=3\cdot 8 + 10 = 34$. Det koster 34 kr å kjøre sparkesykkelen i 8 minutter. 
:::

<br>

Vi antar at gjennomsnittsfarten under en kjøretur er $15 \ \mathrm{km/t}$.

Deloppgave 2
: Lag en modell $B$ som gir $B(t)$ kroner for å kjøre $t$ minutter med en sparkesykkel fra Bolt.  Hvor mye koster det å kjøre sparkesykkelen i 8 minutter?

:::{admonition} Fasit
---
class: answer, dropdown
---
15 km/h tilsvarer 0,25 km/min. 
Prisen per minutt med Bolt blir da 
$11.88 \mathrm{kr/km} \cdot \mathrm{0,25 km/min} = 2.97 \mathrm{kr/min} $

Vi får da at 
$B(t)= 2.97t + 5$

$B(8)=2.97\cdot 8 + 5 = 28.76$ kroner. Det koster 29 kr å kjøre sparkesykkelen i 8 minutter. 
:::


Deloppgave 3
: Hvilket tilbud er mest gunstig dersom du skal kjøre $3 \ \mathrm{km}$? 

:::{admonition} Fasit
---
class: answer, dropdown
---
For 2 km vil Bolt koste $5 + 3\cdot 11.88 = 40.64$ kroner

Gitt en gjennomsnittsfart på 0.25 km/min, så vil Voi koste $\dfrac{3 \mathrm{kr/min}}{0,25 \mathrm{km/min}} = 12 \mathrm{kr/km}$

Da koster en tur på 3 km: $10 + 3\cdot 12 = 46$ kroner.

Ryde vil koste 
$\dfrac{2,5 \mathrm{kr/min}}{0,25 \mathrm{km/min}} = 10 \mathrm{kr/km}$

Da koster en tur på 3 km: $10 + 3\cdot 10 = 40$ kroner.

Det billigste tilbudet for 3 km er altså Ryde. 
:::

````