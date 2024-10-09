# Oppgaver: Regresjon
````{admonition} Oppgave 1
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

````{admonition} Oppgave 2
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

::::{admonition} Oppgave 3
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