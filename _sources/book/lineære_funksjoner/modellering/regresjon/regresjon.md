# Modeller basert på data
Ofte ønsker vi å lage modeller av situasjoner fra virkeligheten gjennom å bruke flere datapunkter. Hvert datapunkt består av en $x-verdi$ og en $y-verdi$. En viktig del av modellering er å lage slike modeller og deretter vurdere hvor gode modellene er. 

::::{admonition} Eksempel 1: Modeller basert på data
---
class: example
---

Vi har data for antall kilometer vi har kjørt som funksjon av tiden vi har brukt:

| Tid | Kilometer |
| --- | --- |
| 15 | 18 |
| 30 | 35 | 
| 45 | 55 |
| 60 | 78 | 
| 75 | 90 |
| 90 | 120 |

Basert på dataene over kan vi lage en figur og forsøke å finne den linja som passer best. Hvilken av linjene passer best til dataene? 

```{figure} ../figurer/datamodellering.svg
:name: datamod
:width: 80%

Datamodellering 
```

:::{admonition} Løsning
---
class: solution
---
I eksempelet ser vi at den grønne linja og den rød linja stiger raskere enn alle punktene, mens den blå linja har omtrent halvparten av punktene over og halvparten av punktene under linja. Den blå linja vil dermed være den beste modellen. 

:::
::::


## Regresjon
I modellen over så vi at en av linjene passet bedre enn de andre. Vi kan finne linja som passer best ved å bruke regresjon. Til regresjon bruker vi alltid et digitalt verktøy, enten python eller GeoGebra. Dersom vi velger GeoGebra, ser det ut som på figuren under. 

```{figure} ../figurer/regresjon.svg
:name: regresjon
:width: 100%

Eksempel på regresjon i GeoGebra, dette gjør vi om til faner. 
```
GeoGebra har mange ulike modeller vi kan velge i tillegg til lineære modeller. Vi skal bruke flere av de andre modellene senere i 1T. 

[Her bør vi ha et eksempel]

## Hvor god er modellen?
En viktig del av matematisk modellering handler om å vurdere hvor god modellen er. For å gjøre det, må vi vurdere modellen vår opp mot situasjonen vi forsøkte å modellere. Vi kan for eksempel vurdere: 
* Kan den matematiske funksjonen vi har valgt (lineær funksjon) virkelig beskrive situasjonen?
* For hvilken definisjonsmengde er modellen vår en god modell?
* Når har vi grunn til å anta at modellen vår ikke er gyldig?

::::{admonition} Eksempel 2: Gyldighetsområdet til en modell
---
class: example
---
Modellen under beskriver folketallet i bygda Oppvik. Vurder gyldighetsområdet til modellen. 

[Trenger hjelp til å lage en figur med datapunkter og en lineær funksjon, og der modellen strekker seg langt utover punktene i både positiv og negativ retning. La gjerne datapunktene øke eksponensielt, slik at de siste punktene passer dårligere]

:::{admonition} Løsning
---
class: solution
---
Vi ser fra modellen at ser ut til å være en nokså god beskrivelse av utviklingen av folketallet. Men modellen kan neppe brukes til å beskrive folketallet før datatellingen starter. Når det har gått lang tid, er det også grunn til å ikke stole på modellen. 

Vi ser også at de siste punktene passer dårligere med modellen enn de første. Ser vi nøye på modellen, kan det se ut til at økningen ikke er lineær, men øker raskere og raskere. Vi skal se nærmere på slike modeller senere i matematikk 1T. 

:::
::::