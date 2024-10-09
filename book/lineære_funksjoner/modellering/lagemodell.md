# Lag en matematisk modell

Ettersom det finnes mange ulike matematiske modeller, finnes det også flere ulike metoder for å komme frem til matematiske modeller. Noen ganger er det nok å identifisere variablene, andre ganger må vi bruke data for å lage en modell.

## Identifisere variablene og sette opp funksjon
I noen tilfeller holder det å identifisere hva som er uavhengig og avhengig variabel, og sette opp en funksjon. 

````{admonition} Underveisoppgave
Sparkesykkelfirmaet *Lemon* har en prismodell der du betaler 10 kr for å låse opp en sparkesykkel, og deretter 2 kr per minutt du bruker sparkesykkelen. 

1. Sett opp en matematisk modell som beskriver sammenhengen mellom prisen, $P$ og antall minutter du har kjørt sparkesykkelen $t$.
2. Bruk modellen din til å finne ut hva det koster dersom du har kjørt sparkesykkelen i 8 minutter. 

**Prøv selv før du ser på løsningsforslaget. Det kan hende du bør lese gjennom forklaringene over et par ganger for å forstå den godt.**

```{dropdown} Løsningsforslag
1. I dette tilfellet er $t$ en uavhengig variabel, mens $P$ er en avhengig variabel som avhenger av $t$. Vi setter da opp funksjonsuttrykket

    $$
    P(t) = 10 + 2\cdot t
    $$

2. For å bestemme prisen dersom vi kjører sparkesykkelen i 8 minutter, setter vi inn $t=8$ i uttrykket for $P(t)$. Vi får da 

    $$
    P(t) = 10 + 2\cdot 8 = 10 + 16 = 26
    $$

    Dermed koster det 26 kr å kjøre sparkesykkelen i 10 minutter. 
```
````

## Definisjonsmengde og verdimengde

## Modeller basert på data
Ofte ønsker vi å lage modeller basert på data. For eksempel kan vi lage en modell for antall kilometer vi har kjørt som funksjon av tiden vi har brukt, som vist i eksempelet under:

| Tid | Kilometer |
| --- | --- |
| 15 | 18 |
| 30 | 35 | 
| 45 | 55 |
| 60 | 78 | 
| 75 | 90 |
| 90 | 120 |

Basert på dataene over kan vi lage en figur og forsøke å finne den linja som passer best. Hvilken av linjene mener du passer best til dataene? 

```{figure} ./figurer/datamodellering.svg
:name: datamod
:width: 100%

Datamodellering 
```

## Regresjon
I modellen over så vi at en av linjene passet bedre enn de andre. Vi kan finne linja som passer best ved å bruke regresjon. Til regresjon bruker vi alltid et digitalt verktøy, enten python eller GeoGebra. Dersom vi velger GeoGebra, ser det ut som på figuren under. 

```{figure} ./figurer/regresjon.svg
:name: regresjon
:width: 100%

Eksempel på regresjon i GeoGebra, dette gjør vi om til faner. 
```
GeoGebra har mange ulike modeller vi kan velge i tillegg til lineære modeller. Vi skal bruke flere av de andre modellene senere i 1T. 

## Gyldighetsområdet til en modell

## Oppgaver

````{admonition} Oppgave 1
---
class: problem-level-1
---
I [denne](https://www.tek.no/nyheter/guide/i/XgPoLm/leie-sparkesykkel-dette-selskapet-er-best-og-billigst) saken fra tek.no finner du priser for ulike sparkesykkelselskap. 

Deloppgave 1
: Ta utgangspunkt i oppstartsprisen og prisen per minutt, og lag en modell som viser prisen per selskap. 

Deloppgave 2
: Bruk modellen til å bestemme hvilket selskap som er billigst dersom du bruker sparkesykkelen i 8 minutter. 

Deloppgave 3
: I tabellen finner du også pris per 10 minutter. Vurder hvor godt dette tilbudet er i hvert tilfelle.
````
---

````{admonition} Oppgave 2
---
class: problem-level-1
---
I 1987 kostet en kroneis 6 kr. I 2022 hadde prisen steget til 27 kroner. Vi antar at prisutviklingen har vært tilnærmet lineær i perioden fra 1987 til 2022. 

Sett opp en lineær modell som beskriver prissstigningen. 

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

````{admonition} Oppgave 5
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

````{admonition} Oppgave 4
---
class: problem-level-1
---
Du har registrert salg av iskrem på ulike temperaturer i grader Celsius over en uke. Her er datapunktene:

| Temperatur (°C) | Salg (is) |
|------------------|-----------|
| 15               | 50        |
| 18               | 70        |
| 20               | 90        |
| 22               | 110       |
| 25               | 130       |
| 30               | 160       |

Deloppgave 1
: Hva er uavhengig og avhengig variabel i denne situasjonen?

:::{admonition} Fasit
---
class: answer, dropdown
---
Her er temperaturen den uavhengige variabelen og iskremsalget den avhengige variabelen
:::

Deloppgave 2
: Lag en modell for iskremsalget som funksjon av temperatur. 

:::{admonition} Fasit
---
class: answer, dropdown
---
Ved hjelp av lineær regresjon får vi modellen $I(T)= 7.52 x - 61.34 $. 
:::

Deloppgave 3
: Bruk modellen din til å forutsi hvor mye iskrem som vil selges ved 23 $^\circ$ C. 
:::{admonition} Fasit
---
class: answer, dropdown
---
Ifølge modellen vil det selges 112 iskrem dersom temperaturen er 23 $^\circ C$. 
:::
````

````{admonition} Oppgave 5
---
class: problem-level-2
---
Gunnar og Einar sår et tomatfrø. De følger nøye med og måler planten hver dag den første uka etter at planten begynner å spire. 

|Antall dager | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Høyde i cm | 0,8 | 1,2 | 1,5 | 1,7 | 1,9 | 2,3 | 2,5 |

Deloppgave 1
: Bestem en lineær modell for tomatplanten. 

:::{admonition} Fasit
---
class: answer, dropdown
---
Vi bruker regresjon og får den lineære modellen $ T(x) = 0.275 x + 0.875$
:::

Deloppgave 2
: Bruk modellen til å forutsi høyden etter 10 dager.

:::{admonition} Fasit
---
class: answer, dropdown
---
Etter 10 dager vil planten være $ T(10) = 2,75 + 0,875 = 3,6 \mathrm{cm}$ ifølge modellen

:::

Deloppgave 3
: Gunnar og Einar har tenkt å plante ut planten etter hvert. Kan modellen brukes til å anslå hvor høy planten er etter to måneder?

:::{admonition} Fasit
---
class: answer, dropdown
---
Nei, det er ikke så sannsynlig, for planten vil ikke ha lineær vekst hele tiden. 

:::
````



::::{admonition} Oppgave 6
---
class: problem-level-3
---
Du har registrert folketallet i Utbygd over flere år. Dataene er som følger:

| År      | Folketall |
|---------|-----------|
| 2000    | 1500      |
| 2001    | 1540      |
| 2002    | 1600      |
| 2003    | 1620      |
| 2004    | 1650      |
| 2005    | 1705      |
| 2006    | 1725      |
| 2007    | 1780      |
| 2008    | 1800      |
| 2009    | 1810      |

<br>

Deloppgave 1
: Bruk lineær regresjon for å modellere sammenhengen mellom år og folketall i bygda.

Deloppgave 2
: Dersom vi bruker årstallene slik de er, vil konstantleddet i modellen være folketallet i år 0. For å unngå det, vil vi ofte la den uavhengige variabelen være antall år *etter* året der vi startet å registrere folketallet. Lag en ny modell der uavhengig variabel er **antall år etter 2000**. 

Deloppgave 3
: Studer modellene du laget i deloppgave 1 og deloppgave 2. Hvilke forskjeller finner du mellom modellene? Har de noe til felles?

Deloppgave 4
: Bruk regresjonsmodellen din til å forutsi folketallet i 2012. 

Deloppgave 5
: Hvilken antakelse har du gjort når du bruker modellen til å forutsi folketallet i 2012? Hva kan påvirke nøyaktigheten av forutsigelsen din?

::::