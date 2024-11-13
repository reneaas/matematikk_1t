# Regresjon 

:::::{admonition} Læringsmål: regresjon
---
class: tip
---
Etter dette delkapitlet, er målet at du skal:
* Kunne bruke regresjon til å bestemme en lineær modell basert på et datasett.

:::::

I mange praktiske situasjoner, er det ikke helt opplagt hva sammenhengen mellom to størrelser er. En strategi for å prøve å finne en modell som beskriver sammenhengen mellom de to variablene er å samle inn data og lage en modell basert på dataene. 

Måten vi lager en modell basert på dataene kalles for **regresjon**.

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

Og i Geogebra kan du også velge mellom å bruke **regneark** eller **CAS**! 


```{tab} CAS
Hvis *jeg* er markert, vil du jobbe med regresjon i **CAS**.

```

```{tab} Regneark
Hvis *jeg* er markert, vil du jobbe med regresjon ved hjelp av **regneark**. 

```

````

````{tab} Python

Hvis *jeg* er markert, vil du jobbe med regresjon i **Python**.

````

---

:::::::::::::::{admonition} Utforsk 1
---
class: explore, full-width
---

Et datasett er gitt ved 

| $x$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: |
| $y$ | $-1$ | $1$ | $3$ | $5$ |


````{tab} Geogebra

```{tab} CAS
I CAS vinduet under vises det hvordan man kan bestemme en lineær modell ved hjelp av regresjon. Vi gjør dette i to steg:

1. Vi lager en liste med punktene $(x, y)$. 
2. Vi bruker `LinReg`-funksjonen som gir oss en lineær modell (Lin = lineær og Reg = regresjon). 

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/cas/utforsk_1.html
---
:::

```

```{tab} Regneark

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

```


````

````{tab} Python 

For å bestemme en modell med Python, kan vi bruke en funksjon fra biblioteket `scipy.optimize`{l=python} som heter `curve_fit`{l=python}. Vi må gå i fire "enkle" steg:

1. Importer `curve_fit`{l=python} fra `scipy.optimize`{l=python}.
2. Definer en funksjon skal tilpasses dataene.
3. Definer lister for dataene.
4. Finn de beste parameterne med `curve_fit`{l=python}. 

> Når vi skriver ut `parametere`{l=python} i programmet under, vil det skrives ut en liste med verdier som har samme rekkefølge som i `modell(x , a,  b)`{l=python}. 


:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/utforsk_1.html
---
:::

````

:::::::::::::::



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

1. Importer `curve_fit`{l=python} fra `scipy.optimize`{l=python}
2. Definer en funksjon som skal tilpasses dataene
3. Bruk `curve_fit`{l=python} til å finne parametrene i funksjonen


````

:::::::::::::::