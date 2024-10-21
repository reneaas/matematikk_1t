# Oppgaver: Regresjon

::::::::::::{admonition} Oppgave 1
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


:::::::::::{tab-set}
---
class: tabs-parts
---

::::::::::{tab-item} a
Lag en modell for iskremsalget ved hjelp av regresjon som gir oss $f(x)$ iskrem solgt når temperaturen er $x$ grader Celsius.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 7.52 x - 61.34
$$
:::
::::::::::

::::::::::{tab-item} b
Gi en praktisk tolkning av stigningstallet og konstantleddet til modellen din. Gir de praktisk mening? 


:::{admonition} Fasit
---
class: answer, dropdown
---
* $a = 7.52$ forteller oss hvor mange flere iskrem som blir solgt når vi øker temperaturen med én grad Celsius. Dette kan gi praktisk mening.
* $b = -61.34$ forteller oss hvor mange iskrem som blir solgt når det er 0 grader ute. Dette tallet gir ikke praktisk mening, men er et kunstig biprodukt av at vi har bestemt $f(x)$ ved regresjon. 
:::

::::::::::

::::::::::{tab-item} c
Hvor mange iskrem blir solgt hvis temperaturen er $23 \, ^\circ \mathrm{C}$, ifølge modellen?
:::{admonition} Fasit
---
class: answer, dropdown
---
Ifølge modellen vil det selges 112 iskrem dersom temperaturen er $23 \, ^\circ \mathrm{C}$. 
:::
::::::::::

:::::::::::

::::::::::::

---


::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---

Sirisser (en slags gresshoppe) lager lyd ved å gni vingene mot hverandre – vi sier at de *kvitrer*. 

Sirisser ble observert ved ulike anledninger og målinger av antall ganger sirissene kvitret per 10 sekunder ble målt ved ulike temperaturer. 

| Antall kvitringer per 10 sekunder | Temperatur (°C) |
|:------------------------------------|-----------------|
| 14                                  | 14.4              |   
| 15                                  | 16.7              |
| 16                                  | 19.4              |
| 17                                  | 19.4              |
| 18                                  | 18.3              |
| 20                                  | 22.2              |


:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Bruk regresjon til å lage en funksjon $T$ som gir oss temperaturen $T(x)$ i grader Celsius når sirissene kvitrer $x$ ganger per 10 sekunder.

::::::::::

::::::::::{tab-item} b
Gi en praktisk tolkning av stigningstallet og konstantleddet til modellen din. 
::::::::::

::::::::::{tab-item} c
Bruk modellen din til å bestemme hva temperaturen er når sirissene kvitrer 5 ganger per 10 sekunder.
::::::::::

::::::::::{tab-item} d
Hvor mange ganger kvitrer sirissene per 10 sekunder når temperaturen er 30 grader Celsius, ifølge modellen din?
::::::::::

:::::::::::
::::::::::::

::::::::::::{admonition} Oppgave 2
---
class: problem-level-2
---
Gunnar og Einar sår et tomatfrø. De følger nøye med og måler planten hver dag den første uka etter at planten begynner å spire. 

|Antall dager | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Høyde i cm | 0,8 | 1,2 | 1,5 | 1,7 | 1,9 | 2,3 | 2,5 |

---

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Bestem en lineær funksjon $f$ som gir oss høyden $h(x)$ i cm etter $x$ dager.

:::{admonition} Fasit
---
class: answer, dropdown
---
Vi bruker regresjon og får den lineære modellen 

$$
h(x) = 0.275 x + 0.875
$$
:::
::::::::::

::::::::::{tab-item} b
Bruk modellen til å forutsi høyden etter 10 dager.

:::{admonition} Fasit
---
class: answer, dropdown
---
Etter 10 dager vil planten være 

$$
T(10) = 3.6 \mathrm{cm},
$$ 

ifølge modellen.

:::
::::::::::

::::::::::{tab-item} c
Gunnar og Einar har tenkt å plante ut planten etter hvert. Kan modellen brukes til å anslå hvor høy planten er etter to måneder?

:::{admonition} Fasit
---
class: answer, dropdown
---
Nei, det er ikke så sannsynlig, for planten vil ikke ha lineær vekst hele tiden. 
:::


::::::::::
:::::::::::
::::::::::::


---

::::::::::::{admonition} Oppgave 3
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


:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Bruk lineær regresjon for å modellere sammenhengen mellom år og folketall i bygda.
::::::::::

::::::::::{tab-item} b
Dersom vi bruker årstallene slik de er, vil konstantleddet i modellen være folketallet i år 0. For å unngå det, vil vi ofte la den uavhengige variabelen være antall år *etter* året der vi startet å registrere folketallet. Lag en ny modell der uavhengig variabel er **antall år etter 2000**. 
::::::::::

::::::::::{tab-item} c
Studer modellene du laget i deloppgave 1 og deloppgave 2. Hvilke forskjeller finner du mellom modellene? Har de noe til felles?
::::::::::

::::::::::{tab-item} d
Bruk regresjonsmodellen din til å forutsi folketallet i 2012. 
::::::::::

:::::::::::

::::::::::::