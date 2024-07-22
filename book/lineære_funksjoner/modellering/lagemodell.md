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

## Oppgaver


### Oppgave 1
I [denne](https://www.tek.no/nyheter/guide/i/XgPoLm/leie-sparkesykkel-dette-selskapet-er-best-og-billigst) saken fra tek.no finner du priser for ulike sparkesykkelselskap. 

1) Ta utgangspunkt i oppstartsprisen og prisen per minutt, og lag en modell som viser prisen per selskap. 
2) Bruk modellen til å bestemme hvilket selskap som er billigst dersom du bruker sparkesykkelen i 8 minutter. 
3) I tabellen finner du også pris per 10 minutter. Vurder hvor godt dette tilbudet er i hvert tilfelle.

---

### Oppgave 2
I 1987 kostet en kroneis 6 kr. I 2022 hadde prisen steget til 27 kroner. Vi antar at prisutviklingen har vært tilnærmet lineær i perioden fra 1987 til 2022. 

Sett opp en lineær modell som beskriver prissstigningen. 

```{dropdown} Løsningsforslag
Vi lar $x$ være antall år etter 1987. Ettersom konstantleddet er prisen i startåret, setter vi $b = 6$. 

Fra 1987 til 2022 er det 35 år. På de 35 årene har prisen steget med 21 kroner. Vi finner da årlig prisstigning

$$ a = \frac{\Delta y}{\Delta x} = \frac{21}{35} = \frac{3}{5}$$

Vi kan da sette opp den lineære modellen $y = \frac{3}{5} + 6$. 
```
---
### Oppgave 3
Gunnar og Einar sår et tomatfrø. De følger nøye med og måler planten hver dag den første uka etter at planten begynner å spire. 

|Antall dager | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Høyde i cm | 0,8 | 1,2 | 1,5 | 1,7 | 1,9 | 2,3 | 2,5 |

1) Bestem en lineær modell for tomatplanten. 
2) Bruk modellen til å forutsi høyden etter 10 dager. 
3) Gunnar og Einar har tenkt å plante ut planten etter hvert. Kan modellen brukes til å anslå hvor høy planten er etter to måneder?

```{dropdown} Løsningsforslag
1) Vi bruker regresjon og får den lineære modellen $ T(x) = 0.275 x + 0.875
2) Etter 10 dager vil planten være $ T(10) = 2,75 + 0,875 = 3,6 cm ifølge modellen
3) Nei, det er ikke så sannsynlig, for planten vil ikke ha lineær vekst hele tiden. 

```

---


````{admonition} Oppgave 3
:class: problem-level-2
Det er tre selskaper som tilbyr leie av elsparkesykler i Oslo (per juli 2024). I tabellen under vises oppstartspris og pris per minutt for de ulike selskapene. Selskapene har litt forskjellige tilbud til kundene sine. 

| Selskap | Oppstartspris [kr] | Pris per minutt [kr/min] | Pris per km [kr/km] |
| :---: | :---: | :---: | :---: |
| Voi | 10 | 3 | - |
| Bolt | 5 | - | 11.88 |
| Ryde | 10 | 2.5 | - |

<br>

{style=lower-alpha}
1. Lag en modell $g$ som gir $f(x)$ kroner for $x$ minutter med kjøretid med en sparkesykkel fra Voi. Hvor mye koster det å kjøre sparkesykkelen i 8 minutter?
2. Lag en modell $g$ som gir $g(x)$ kroner for å kjøre $x$ minutter med en sparkesykkel fra Bolt.  Hvor mye koster det å kjøre sparkesykkelen i 8 minutter?
3. Hvilket tilbud er mest gunstig dersom du skal kjøre $2 \ \mathrm{km}$? 

<br>

Oppgave 3a
: Lag en modell $g$ som gir $f(x)$ kroner for $x$ minutter med kjøretid med en sparkesykkel fra Voi. Hvor mye koster det å kjøre sparkesykkelen i 8 minutter?

<br>

Vi antar at gjennomsnittsfarten under en kjøretur er $15 \ \mathrm{km/t}$.

Oppgave 3b
: Lag en modell $g$ som gir $g(x)$ kroner for å kjøre $x$ minutter med en sparkesykkel fra Bolt.  Hvor mye koster det å kjøre sparkesykkelen i 8 minutter?

Oppgave 3c
: Hvilket tilbud er mest gunstig dersom du skal kjøre $2 \ \mathrm{km}$? 

````
