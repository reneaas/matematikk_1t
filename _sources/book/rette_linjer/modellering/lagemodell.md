# Lag en matematisk modell

Ettersom det finnes mange ulike matematiske modeller, finnes det også flere ulike metoder for å komme frem til matematiske modeller. Noen ganger er det nok å identifisere variablene, andre ganger må vi bruke data for å lage en modell.

## Identifisere variablene og sette opp funksjon
I noen tilfeller holder det å identifisere hva som er uavhengig og avhengig variabel, og sette opp en funksjon. 

````{admonition} Underveisoppgave
Sparkesykkelfirmaet *Lemon* har en prismodell der du betaler 10 kr for å låse opp en sparkesykkel, og deretter 2 kr per minutt du bruker sparkesykkelen. 

1. Sett opp en matematisk modell som beskriver sammenhengen mellom prisen, $P$ og antall minutter du har kjørt sparkesykkelen $t$.
2. Bruk modellen din til å finne ut hva det koster dersom du har kjørt sparkesykkelen i 8 minutter. 

**Prøv godt selv før du ser på løsningsforslaget. Det kan hende du bør lese gjennom forklaringene over et par ganger for å forstå den godt.**

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

Datamodellering - stygg figur som må fikses slik at den viser flere ulike linjer. 
```

## Regresjon
I modellen over så vi at en av linjene passet bedre enn de andre. Vi kan finne linja som passer best ved å bruke regresjon. Til regresjon bruker vi alltid et digitalt verktøy, enten python eller GeoGebra. Dersom vi velger GeoGebra, ser det ut som på figuren under. 

```{figure} ./figurer/regresjon.svg
:name: regresjon
:width: 100%

Eksempel på regresjon i GeoGebra
```
GeoGebra har mange ulike modeller vi kan velge i tillegg til lineære modeller. Vi skal bruke flere av de andre modellene senere i 1T. 

## Oppgaver


