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

### Definisjonsmengde
Funksjonene vi har arbeidet så langt med i 1T, har stort sett vært definert for alle mulige verdier av $x$. Vi kan skrive dette formelt som $D_f = \mathbb{R}$. Her refererer symbolet $D$ til definisjonsmengden, og $f$ til funksjonen vi ser på. Videre skal vi se på funksjoner som kun er definert for en bestemt definisjonsmengde. I noen tilfeller fordi vi bestemmer det, andre ganger fordi funksjonen beskriver en situasjon fra virkeligheten som setter noen begrensninger. 

### Verdimengde
Verdimengden er de mulige verdiene funksjonen kan få. Når vi arbeider med lineære funksjoner med definisjonsmengden $D_f = \mathbb{R}$, vil også verdimengden være alle de reelle tallene. Vi kan skrive dette formelt som $V_f = \mathbb{R}$. Her refererer symbolet $V$ til verdimengden, og $f$ til funksjonen vi ser på. Videre skal vi se på funksjoner som har en begrenset verdimengde, enten fordi definisjonsmengden er begrenset, eller fordi egenskapene til funksjonen i seg selv begrenser verdimengden. 

[SETT INN FIGUR SOM VISER BEGRENSET DEFINISJONSMENGDE OG VERDIMENGDE]

::::{admonition} Eksempel 1: Definisjonsmengde og verdimengde for en praktisk situasjon
---
class: example
---
Finn definisjonsmengden og verdimengden for funksjonen $P(t)=  10 + 2\cdot t$, som beskriver prisen vi må betale for sparkesykkelturen som funksjon av antall minutter vi bruker sparkesykkelen. 

:::{admonition} Løsning
---
class: solution
---
Vi kan ikke låne sparkesykkelen et negativt antakk minutter. Definisjonsmengden blir derfor $D_P = [0, \to \rangle$. 

Den laveste prisen vi kan betale for sparkesykkelturen er 10 kr. Verdimengden blir da $V_P = [10, \to \rangle$. 

:::

::::
