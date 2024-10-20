# Regresjon 
Det er ikke alltid en opplagt sammenhengen mellom to størrelser. I slike tilfeller kan vi: 
* Gjøre målinger og samle inn et datasett.
* Bruke regresjon som en *metode* for å finne en funksjon som passer best til dataene.

Hvert datapunkt i et datasett består av en $x$-verdi og en tilhørende $y$-verdi. Men når man gjør målinger, vil det alltid være en viss usikkerhet knyttet til målingene. Antakelsen er da det finnes en funksjon $f$ slik at en måling $(x, y)$ henger sammen ved

$$
y = f(x) + \mathrm{støy}. 
$$

Målet vårt er å praksis å finne $f(x)$, men det klarer vi sjeldent å gjøre nøyaktig. En viktig ferdighet blir derfor å kunne både lage modeller, og vurdere påliteligheten til disse.

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
Vi kan merke oss at den grønne linja stiger for raskt og passer ikke spesielt godt til punktene. Både den rød og en blå linja følger punktene godt og ser ut til å ha samme stningstall. 
Men den rød linja har en tendens til å ligge på oversiden av punktene, mens den blå linja ligger på oversiden og undersiden av punktene i en jevn fordeling. Derfor vil vi si at den blå linja passer best til dataene.

:::
::::


## Regresjon
I eksempel 1 argumenterte vi for at én av modellene passet bedre enn de andre. En metode får å finne den beste modellen i lys av dataene, kalles for **regresjon**. Regresjon innebærer tre ingredisenser:
1. Samle inn et datasett med målinger $(x, y)$.
2. Velg en modellklasse som du tror kan forklare sammenhengen mellom $x$ og $y$. 
3. Bruk regresjon til å bestemme hvilken modell i modellklassen som passer best til dataene.

Regresjon kan gjøres både med Geogebra og Python – her får du selv velge hvilken læringssti du vil følge. Husk at du alltid kan bytte sti underveis.


````{tab} Geogebra
Hvis *jeg* er markert, vil du jobbe med regresjon i **Geogebra**.
````

````{tab} Python
Hvis *jeg* er markert, vil du jobbe med regresjon i **Python**.
````




:::::::::::::::{admonition} Utforsk 1
---
class: explore, full-width
---

I eksempelet under skal vi se på en lineær funksjon bestemt ved hjelp av regresjon til datasettet

| $x$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: |
| $y$ | $-1$ | $1$ | $3$ | $5$ |

````{tab} Geogebra

Du kan bestemme en regresjonsmodell ved å følge disse stegene i vinduet under:

1. Åpne regneark <img src="figurer/icons/menu_view_spreadsheet.svg" class="inline-image"/> og skriv inn tallene i to kolonner nedover. 
2. Trykk på rullemenyen med ikonet <img src="figurer/icons/mode_onevarstats.svg" class="inline-image"/> og bla ned og velg regresjonsanalyse <img src="figurer/icons/mode_twovarstats.svg" class="inline-image"/> 
3. Velg en regresjonsmodell
4. Trykk på <img src="figurer/icons/export.svg" class="inline-image"/> og velg "Kopier til grafikkfeltet"


:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/utforsk_1.html
---
:::

````

````{tab} Python

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/utforsk_1.html
---
:::

````

:::::::::::::::

---

:::::::::::::::{admonition} Oppsummering: oppskrift på regresjon
---
class: summary, dropdown
---


````{tab} Geogebra

1. Åpne regneark <img src="figurer/icons/menu_view_spreadsheet.svg" class="inline-image"/> og skriv inn tallene i to kolonner nedover. 
2. Trykk på rullemenyen med ikonet <img src="figurer/icons/mode_onevarstats.svg" class="inline-image"/> og bla ned og velg regresjonsanalyse <img src="figurer/icons/mode_twovarstats.svg" class="inline-image"/> 
3. Velg en regresjonsmodell
4. Trykk på <img src="figurer/icons/export.svg" class="inline-image"/> og velg "Kopier til grafikkfeltet"

````


````{tab} Python

sss

````

:::::::::::::::
<!-- 
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
:::: -->