# Programmering av likningssystemer

:::{admonition} Læringsmål
---
class: tip
---
Målet etter dette delkapittelet er at du skal:
* Kunne lese, tolke og endre på programkode som løser lineære likningssystemer. 
* Kunne lese, tolke og lage nøstede `for`{l=python}-løkker for å lage punkter i et rutenett og bruke dette til å løse likningssystemer.
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
I mange tilfeller kan vi skrive om et likningssystem fra dens generelle form til en form som svarer til to lineære funksjoner. Da kan vi tolke likningssystemet som at vi skal bestemme koordinatene til skjæringspunktet $(x, y)$ mellom grafene til de to funksjonene. 

::::{admonition} Eksempel
---
class: example
---

$$
5x + y = 2 \quad \land \quad 3x - y = 2
$$

kan skrives om ved å løse begge likninger for $y$ til:

$$
y = \underbrace{-5x + 2}_{\displaystyle f(x)} \quad \land \quad y = \underbrace{3x - 2}_{\displaystyle g(x)}
$$

Løsningen av likningssystemet er da bare koordinatene til skjæringspunktet mellom grafene til $f$ og $g$.
::::

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
class: no-click, adaptive-figure
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





:::::::::::::::{admonition} Utforsk 2
---
class: explore, full-width
---
> Her skal du utforske en strategi som vi kaller for **gridsøk**. 

I prinsippet kan vi løse et hvert likningssystem ved å lage et rutenett med punkter $(x, y)$ i $xy$-planet og sjekke hvilke punkter som oppfyller likningssystemet. For å gjøre dette må vi lage **nøstede** `for`{l=python}-løkker. Dette er `for`{l=python}-løkker som ligger inne i hverandre. Den første `for`{l=python}-løkken lager punktene $x$, og den andre `for`{l=python}-løkken lager punktene $y$.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises et program og en animasjon som henger sammen. Undersøk på hvilken måte.

::::::::::::{grid}
:::::::::::{grid-item-card}
---
columns: 6
---
Programkode
^^^

:::{interactive-code}
for x in range(0, 4):
    for y in range(0, 3):
        print(x, y)


:::

:::::::::::

:::::::::::{grid-item-card}
Animasjon
^^^

:::{figure} ./figurer/utforsk/utforsk_2/a/animasjon.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::
:::::::::::

::::::::::::


:::::::::::::



:::::::::::::{tab-item} b
Nedenfor vises et program og en animasjon som henger sammen. Undersøk på hvilken måte.

::::::::::::{grid}
:::::::::::{grid-item-card}
---
columns: 6
---
Programkode
^^^

:::{interactive-code}
for x in range(-3, 2):
    for y in range(-1, 3):
        print(x, y)

:::

:::::::::::

:::::::::::{grid-item-card}
Animasjon
^^^

:::{figure} ./figurer/utforsk/utforsk_2/b/animasjon.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::
:::::::::::

::::::::::::


:::::::::::::

::::::::::::::


:::::::::::::::




---

::::{admonition} Underveisoppgave 1
---
class: check
---
Ta quizen! 

:::{raw} html
---
file: ./quiz/quiz_3/quiz_3.html
---
:::
::::


---


::::::::{admonition} Utforsk 3: strategi 2
---
class: explore, full-width
---
Her skal vi se hvordan vi kan bruke gridsøk til å finne løsningen av likningssystemer.

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a
Vi trenger en måte å sjekke om et likningssystem er oppfylt for et punkt $(x, y)$. Med andre ord, vi må kunne sjekke om to likninger er sanne *samtidig*.

Under vises det tre eksemplekoder der man sjekker om et likningssystem er oppfylt for et bestemt punkt $(x, y)$. For hvert kodeeksempel: 

* Les kodeeksempelet og løs likningssystemet (med valgfri metode) programmet sjekker.
* Forutsi om programmet skriver ut `True`{l=python} eller `False`{l=python}. 
* Skriv inn forutsigelsen din og sjekk svaret ditt! 

:::::{tab-set}
::::{tab-item} Eksempel 1

> ⚠️ Merk at nøkkelordet `and`{l=python} = $\land$ (*og samtidig*)

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_3/a/eksempel_1.html
---
:::

::::

::::{tab-item} Eksempel 2

> ⚠️ Merk at nøkkelordet `and`{l=python} = $\land$ (*og samtidig*)

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_3/a/eksempel_2.html
---
:::

::::

::::{tab-item} Eksempel 3

> ⚠️ Merk at nøkkelordet `and`{l=python} = $\land$ (*og samtidig*)

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_3/a/eksempel_3.html
---
:::

::::
:::::


::::::

::::::{tab-item} b
For å få programmet til å si ifra for oss når det finner en løsning, kan vi bruke en `if`{l=python}-setning som sjekker om begge likningene er sanne, og deretter skriver ut svaret! 

* Les eksemplene under og kjør programmene. 
* Kan du forklare sammenhengen mellom utskriften og animasjonen? 


`````{tab-set}
````{tab-item} Eksempel 1

:::::{grid}

::::{grid-item} **Programkode**

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/b/eksempel_1.html
---
:::

::::

::::{grid-item} **Animasjon**


:::{figure} ./figurer/utforsk/utforsk_3/b/animasjon_1.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::

:::::

````

````{tab-item} Eksempel 2

:::::{grid}

::::{grid-item} **Programkode**

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/b/eksempel_2.html
---
:::

::::

::::{grid-item} **Animasjon**


:::{figure} ./figurer/utforsk/utforsk_3/b/animasjon_2.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::

:::::

````

`````

::::::

::::::{tab-item} c
I oppgavene under må du fylle inn programmet med riktig likningssystem i `if`{l=python}-setningen for å bestemme løsningen.

:::::{tab-set}
::::{tab-item} Oppgave 1
Bruk programmet til å bestemme løsningen av likningssystemet 

$$
3x + 2y = 7 \quad \land \quad x - y = 4
$$

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_3/c/oppgave_1.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
Programkode: 
    
```{code-block} python
---
linenos: true
emphasize-lines: 3
---
for x in range(-5, 6):
    for y in range(-5, 6):
        if 3*x + 2*y == 7 and x - y == 4:
            print(f"{x = } \t {y = }")
```

som gir utskriften

```console
x = 3 	 y = -1
```

som betyr at 

$$
3x + 2y = 7 \quad \land \quad x - y = 4 \quad \iff \quad x = 3 \quad \land \quad y = -1
$$

:::

::::

::::{tab-item} Oppgave 2
Bruk programmet til å bestemme løsningen av likningssystemet 

$$
x + 2y = 4 \quad \land \quad -2x + y = -3
$$

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_3/c/oppgave_2.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
Programkode: 
    
```{code-block} python
---
linenos: true
emphasize-lines: 3
---
for x in range(-5, 6):
    for y in range(-5, 6):
        if x + 2*y == 4 and -2*x + y == -3:
            print(f"{x = } \t {y = }")
```

som gir utskriften

```console
x = 2 	 y = 1
```

som betyr at 

$$
x + 2y = 4 \quad \land \quad -2x + y = -3 \quad \iff \quad x = 2 \quad \land \quad y = 1
$$

:::

::::

::::{tab-item} Oppgave 3
Bruk programmet til å bestemme løsningen av likningssystemet 

$$
3x + 4y = -10 \quad \land \quad \dfrac{1}{2}x + y = -2
$$

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_3/c/oppgave_3.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
Programkode: 
    
```{code-block} python
---
linenos: true
emphasize-lines: 3
---
for x in range(-5, 6):
    for y in range(-5, 6):
        if 3*x + 4*y == -10 and x/2 + y == -2:
            print(f"{x = } \t {y = }")
```

som gir utskriften

```console
x = -2 	 y = -1
```

som betyr at 

$$
3x + 4y = -10 \quad \land \quad \dfrac{1}{2}x + y = -2 \quad \iff \quad x = -2 \quad \land \quad y = -1
$$

:::


::::

:::::


::::::

::::::{tab-item} d
I programmene under må du:
* Fylle inn likningssystemene i `if`{l=python}-setningen.
* Bestemme riktig `range`{l=python} i `for`{l=python}-løkkene slik at programmet lager de samme punktene $(x, y)$ som vises i tilhørende animasjonene.


``````{tab-set}
````{tab-item} Oppgave 1
Bruk programmet under til å bestemme løsningen av likningssystemet

$$
x + 3y = 5 \quad \land \quad 2x - y = 3
$$

---

:::::{grid}

::::{grid-item} **Programkode**

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/d/oppgave_1.html
---
:::

::::

::::{grid-item} **Animasjon**

:::{figure} ./figurer/utforsk/utforsk_3/d/oppgave_1_animasjon.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::
:::::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
```{code-block} python
---
linenos: true
---
for x in range(0, 4):
    for y in range(-2, 3):
        if x + 3*y == 5 and 2*x - y == 3:
            print(f"{x = } \t {y = }")
```
:::

````

````{tab-item} Oppgave 2
Bruk programmet under til å bestemme løsningen av likningssystemet

$$
x + y = -1 \quad \land \quad x + \dfrac{1}{2}y = \dfrac{1}{2}
$$

---

:::::{grid}

::::{grid-item} **Programkode**

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/d/oppgave_2.html
---
:::

::::

::::{grid-item} **Animasjon**

:::{figure} ./figurer/utforsk/utforsk_3/d/oppgave_2_animasjon.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::
:::::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
```{code-block} python
---
linenos: true
---
for x in range(0, 5):
    for y in range(-4, 1):
        if x + y == -1 and x + y/2 == 1/2:     
            print(f"{x = } \t {y = }")
```
:::

````

````{tab-item} Oppgave 3
Bruk programmet under til å bestemme løsningen av likningssystemet

$$
2x - y = -5 \quad \land \quad x + 3y = 1
$$

---

:::::{grid}

::::{grid-item} **Programkode**

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/d/oppgave_3.html
---
:::

::::

::::{grid-item} **Animasjon**

:::{figure} ./figurer/utforsk/utforsk_3/d/oppgave_3_animasjon.gif
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::
:::::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
```{code-block} python
---
linenos: true
---
for x in range(-3, 4): 
    for y in range(0, 4):
        if 2*x - y == -5 and x + 3*y == 1:
            print(f"{x = } \t {y = }")
```
:::

````

``````



::::::
:::::::


:::::::: 

---

::::::::{admonition} Utforsk 4: anvendelse
---
class: explore
---
Her skal vi se hvordan vi kan anvende gridsøk til å bestemme funksjonsuttrykket til lineære funksjoner. I dette tilfellet er det ikke lenger $x$ og $y$ som er variablene i likningssystemet, men koeffisientene $a$ og $b$ til den lineære funksjonen.

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a
I eksemplene under viser vi hvordan vi kan bruke gridsøk til å bestemme koeffisientene $a$ og $b$ til en lineær funksjon $f(x) = ax + b$ som går gjennom to gitte punkter.

* Les programmene og sjekk at du kan forklare sammenhengen mellom innholdet i programmet og likningene den lineære funksjonen må oppfylle.
* Bruk utskriften av programmet til å bestemme funksjonsuttrykket til funksjonen.

`````{tab-set}
````{tab-item} Eksempel 1
Et lineær funksjon $f(x) = ax + b$ går gjennom punktene $(-1, -5)$ og $(1, 1)$. Dette gir likningssystemet

$$
f(-1) = -5 \quad \land \quad f(1) = 1
$$

$$
-a + b = -5 \quad \land \quad a + b = 1
$$

Programkode: 
:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_4/a/eksempel_1.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 3x - 2
$$
:::

````

````{tab-item} Eksempel 2
En lineær funksjon $g(x) = ax + b$ går gjennom punktene $(-3, 5)$ og $(-2, 4)$. Dette gir likningssystemet

$$
g(-3) = 5 \quad \land \quad g(-2) = 4
$$

$$
-3a + b = 5 \quad \land \quad -2a + b = 4
$$

Programkode:
:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_4/a/eksempel_2.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(x) = -x + 2
$$
:::

````

````{tab-item} Eksempel 3
En lineær funksjon $h(x) = ax + b$ går gjennom punktene $(-2, -5)$ og $(3, 10)$. Dette gir likningssystemet

$$
h(-2) = -5 \quad \land \quad h(3) = 10
$$

$$
-2a + b = -5 \quad \land \quad 3a + b = 10
$$

Programkode:
:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_4/a/eksempel_3.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
h(x) = 3x + 1
$$
:::

````

::::::

::::::{tab-item} b
I oppgavene under skal du sette opp likningssystemet for koeffisientene til de lineære funksjonene og fylle inn i programmet for å bestemme funksjonsuttrykket. 

`````{tab-set}
````{tab-item} Oppgave 1
En lineær funksjon $f(x) = ax + b$ går gjennom punktene $(-1, -6)$ og $(3, 10)$. 

1. Sett opp et likningssystem for koeffisientene til $f$. 
2. Fyll ut programmet under og bruk det til å bestemme $f(x)$. 

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_4/b/oppgave_1.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Likningssystem
$$
-a + b = -6 \quad \land \quad 3a + b = 10
$$
:::

:::{tab-item} Programkode
```{code-block} python
---
linenos: true
---
for a in range(-5, 6):
    for b in range(-5, 6):
        if -a + b == -6 and 3*a + b == 10:
            print(f"{a = } \t {b = }")
```
Utskrift: 

```console
a = 4 	 b = -2
```
:::

:::{tab-item} Funksjonsuttrykk
$$
f(x) = 4x - 2
$$
:::
::::
:::::

````

````{tab-item} Oppgave 2
En lineær funksjon $g(x) = ax + b$ går gjennom punktene $(1, 1)$ og $(4, -5)$. 

1. Sett opp et likningssystem for koeffisientene til $g$. 
2. Fyll ut programmet under og bruk det til å bestemme $g(x)$. 

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_4/b/oppgave_2.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Likningssystem
$$
a + b = 1 \quad \land \quad 4a + b = -5
$$
:::

:::{tab-item} Programkode
```{code-block} python
---
linenos: true
---
for a in range(-5, 6):
    for b in range(-5, 6):
        if a + b == 1 and 4*a + b == -5:
            print(f"{a = } \t {b = }")
```
Utskrift: 

```console
a = -2 	 b = 3
```
:::

:::{tab-item} Funksjonsuttrykk
$$
g(x) = -2x + 3
$$
:::
::::
:::::

````

````{tab-item} Oppgave 3
En lineær funksjon $h(x) = ax + b$ går gjennom punktene $(-3, 13)$ og $(7, -17)$. 

1. Sett opp et likningssystem for koeffisientene til $h$. 
2. Fyll ut programmet under og bruk det til å bestemme $h(x)$. 

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_4/b/oppgave_3.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Likningssystem
$$
-3a + b = 13 \quad \land \quad 7a + b = -17
$$
:::

:::{tab-item} Programkode
```{code-block} python
---
linenos: true
---
for a in range(-5, 6):
    for b in range(-5, 6):
        if -3*a + b == 13 and 7*a + b == -17:
            print(f"{a = } \t {b = }")
```
Utskrift: 

```console
a = -3 	 b = 4
```
:::

:::{tab-item} Funksjonsuttrykk
$$
h(x) = -3x + 4
$$
:::
::::
:::::

````

`````

::::::

:::::::

::::::::