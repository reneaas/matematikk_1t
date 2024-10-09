# Programmering av likningssystemer

:::{admonition} Læringsmål
---
class: tip
---
Målet etter dette delkapittelet er at du skal:
* Kunne lese, tolke og endre på programkode som løser lineære likningssystemer. 
:::

---

## Numerisk løsning av likningssystemer

Akkurat som at det finnes likninger som ikke har noen analytisk løsning, finnes det også likningssystemer der dette er tilfellet. I andre tilfeller vil vi ha likningssystemer med så mange likninger og variabler at å løse dem uten datamaskin er en håpløs oppgave.

Her skal vi se på hvordan vi kan bruke programmering til å finne løsninger til lineære likningssystemer.


### Repetisjon
Først bør vi starte med å få repetert det viktigste vi trenger for å løse likningssystemer med programmering. 

::::::{admonition} Repetisjon 1:
---
class: reminder
---
Her kommer en quiz om `for`{l=python}-løkker, funksjoner i Python og løsning av likninger med programmering. 


:::::{tab-set} 
::::{tab-item} Level 1 🔥
Ta quizen!

:::{raw} html
---
file: quiz/quiz_1/quiz_1.html
---
:::

::::

:::::{tab-item} Level 2 🔥🔥
Svar på så mange spørsmål du kan før tiden er ute! ⏳

:::{raw} html
---
file: quiz/quiz_2/quiz_2.html
---
:::

::::

::::::

---

### Løsning av likningssystemer med programmering

::::::::::{admonition} Utforsk 1: strategi 1
---
class: explore
---
I mange tilfeller kan vi skrive om et likningssystem fra den generelle formen 

$$
Ax + By = C \, \land \, Dx + Ey = F
$$

til 

$$
y = ax + b \quad \land \quad y = cx + d
$$

Ved å løse hver av likningene for $y$. Da kan vi tolke problemet som at vi skal finne skjæringspunktet mellom grafene til de to lineære funksjonene 

$$
y = f(x) \quad \land \quad y = g(x)
$$


::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Et likningssystem er gitt ved

$$
x + 2y = 5 \quad \land \quad 4x + y = 6
$$

Skriv om likningssystemet til formen

$$
y = ax + b \quad \land \quad y = cx + d
$$

Hvilke to lineære funksjoner inngår i likningssystemet?

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -\dfrac{1}{2}x + \dfrac{5}{2} \quad \land \quad y = -4x + 6
$$
:::: 
:::::

:::::{tab-item} b
Under vises et uferdig program som skal løse likningssystemet fra deloppgave a.

Fyll inn koden som mangler og kjør programmet for å bestemme løsningen av likningssystemet.

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html
---

:::

::::{admonition} Sjekk svaret ved å sammenligne med figuren her når du er klar!
---
class: check, dropdown
---
:::{figure} ./figurer/utforsk/utforsk_1.svg
---
width: 100%
---
viser linjene i likningssystemet $x + 2y = 5 \, \land \, 4x + y = 6$
:::
::::

---

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
---
def f(x):
    return -x / 2 + 5 / 2

def g(x):
    return -4 * x + 6

for x in range(-5, 6):
    if f(x) == g(x):
        print(x, f(x))
:::

Utskriften blir

:::{code-block} console
1 2.0
:::

som betyr at løsningen av likningssystemet er 

$$
x = 1 \, \land \, y = 2
$$
::::
::::

:::::

::::::

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html
---
:::

<br>

::::::::::

---

::::::::::{admonition} Utforsk 2: nøstede `for`{l=python}-løkker
---
class: explore, full-width
---
I utforsk 3 skal vi anvende en strategi som kalles for *gridsøk*. Dette er en metode hvor vi systematisk løper gjennom punkter $(x, y)$ i et rutenett og sjekker om likningene i likningssystemet er oppfylt samtidig. For å gjøre dette trenger vi å se på **nøstede** `for`{l=python}-løkker. Dette er `for`{l=python}-løkker som er plassert inni en annen `for`{l=python}-løkke.


::::::::{tab-set}
---
class: tabs-parts
---
:::::::{tab-item} a

Under vises to eksempler på hvordan nøstede `for`{l=python}-løkker kan brukes til å lage punkter $(x, y)$ i et rutenett. Til hver kode er det en animasjon som viser hvordan punktene genereres i rutenettet. 

* Kjør programmet for hver eksempelkode og sammenlign utskriften med animasjonen. <br> (*Tips:* Prøv å trykke på kjør *akkurat* når animasjonen starter på nytt!)
* Bruk det du observerer til å forklare betydningen av *rekkefølgen* på de to `for`{l=python}-løkkene i programmet.

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} Eksempel 1
> ⚠️ Merk deg rekkefølgen på `for`{l=python}-løkken til `x`{l=python} og `y`{l=python} i programmet. 

:::::{grid}

::::{grid-item} **Programkode**


:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/eksempel_1.html 
---
:::

::::

::::{grid-item} **Animasjon**
:::{figure} ./figurer/utforsk/utforsk_2/a/eksempel_1.gif
---
width: 100%
---
viser hvordan punktene $(x, y)$ i rutenettet løpes gjennom av programmet til venstre.
::: 
::::
:::::

````

````{tab-item} Eksempel 2
> ⚠️ Merk deg rekkefølgen på `for`{l=python}-løkken til `x`{l=python} og `y`{l=python} i programmet. 
:::::{grid}

::::{grid-item} **Programkode**


:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/eksempel_2.html 
---
:::

::::

::::{grid-item} **Animasjon**
:::{figure} ./figurer/utforsk/utforsk_2/a/eksempel_2.gif
---
width: 100%
---
viser hvordan punktene $(x, y)$ i rutenettet løpes gjennom av programmet til venstre.
::: 
::::
:::::

````

`````


:::::::

:::::::{tab-item} b
Under vises tre programkoder og tre animasjoner som parvis hører sammen. 

* Les programmene og bestem hvilket program som hører til hvilken animasjon. 
* Skriv inn hypotesen din og kjør programmet for å sjekke svarene dine! 


::::::{grid}
:::::{grid-item} **Programkoder**
`````{tab-set}
````{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b/program_1.html 
---
:::

````

````{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b/program_2.html 
---
:::

````

````{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b/program_3.html 
---
:::

````
`````
:::::

:::::{grid-item} **Animasjoner**
`````{tab-set}
````{tab-item} Animasjon A

:::{figure} ./figurer/utforsk/utforsk_2/b/animasjon_A.gif
---
width: 100%
---
:::

````

````{tab-item} Animasjon B

:::{figure} ./figurer/utforsk/utforsk_2/b/animasjon_B.gif
---
width: 100%
---
:::

````

````{tab-item} Animasjon C

:::{figure} ./figurer/utforsk/utforsk_2/b/animasjon_C.gif
---
width: 100%
---
:::


````
`````
:::::
::::::


:::::::

::::::::

::::::::::

---


::::{admonition} Utforsk 3: strategi 2
---
class: explore
---
Gridsøk over mulige løsninger av likningssystemer kommer her...


:::: 

---

::::{admonition} Utforsk 4: anvendelse
---
class: explore
---
Gridsøk for å bestemme koeffisientene til en lineær funksjon som passer til to gitte punkter kommer her.
::::