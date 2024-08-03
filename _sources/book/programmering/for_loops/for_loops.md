# `for`{l=python}-løkker

:::{admonition} Gjør dette først!
---
class: warning, margin
---
Du bør ha lest om [while-løkker](../while_loops/while_loops.md) før du leser dette kapittelet, eller være godt kjent med bruken av `while`{l=python}-løkker.
:::

:::{admonition} Læringsmål: `for`{l=python}-løkker
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Lese og forstå `for`{l=python}-løkker som brukes `range`{l=python}-funksjonen.
* Kunne skrive grunnleggende `for`{l=python}-løkker som bruker `range`{l=python}-funksjonen til å løse matematiske problemer.

:::


En `for`{l=python}-løkke kan tenkes på som en *spesiell* type `while`{l=python}-løkke som automatiserer tellingen for deg. Det finnes mange typer `for`{l=python}-løkker, men vi skal konsentrere oss om en som er mest nyttig i matematikk. 

Vi starter med en sammenlikning av `for`{l=python}-løkker og `while`{l=python}-løkker:



```{code-block}
---
linenos: true
class: margin
---
i = 1
while i <= 5:
    print(f"{i = }")
    i = i + 1
```

::::{admonition} Utforsk 1: `while`{l=python}-løkke
---
class: sidenote, margin
---
::::

:::::{admonition} Utforsk 1: `for`{l=python}-løkker vs `while`{l=python}-løkker
---
class: explore,
---
Under vises to interaktive kodevinduer. Begge kodene skriver ut de 5 første naturlige tallene, men bruker forskjellige type løkke. 


::::{grid}
---

gutter: 1
---

:::{grid-item-card} 
`for`{l=python}-løkke
```{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1_for_loop.html
---
```
:::

:::{grid-item-card} 
`while`{l=python}-løkke
```{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1_while_loop.html
---
```
:::
::::




Deloppgave 1
: Undersøk hva de tre tallene i `range(1, 6, 1)`{l=python} gjør for noe ved å prøve ut forskjellige kombinasjoner av tall. Kan du forklare rollen til de tre tallene?
: *Tips*: Prøv ut ett tall av gangen! Du kan også bruke negative tall.


<br>

Deloppgave 2
: Undersøk om du kan få `for`{l=python}-løkka til å skrive ut de 10 første naturlige tallene.
: Endre `while`{l=python}-løkka til å gjøre det samme. 


<br>

Deloppgave 3
: Undersøk om du kan få `for`{l=python}-løkka til å skrive ut alle partall fra 2 til 10. 
: Kan du gjøre det samme, men bare med oddetallene?


<br>

Deloppgave 4
: Kan du få `for`{l=python}-løkka til å skrive ut tallene fra 10 til 1 i synkende rekkefølge?
: Kan du gjøre det samme med `while`{l=python}-løkka?


:::::


Nå har du fått litt oversikt over hvordan en enkel `for`{l=python}-løkke fungerer. Nå skal du se på hvordan du kan få en `for`{l=python}-løkke til å løse tilsvarende problemer som du løste når du så på `while`{l=python}-løkker.


:::::{admonition} Utforsk 2: `for`{l=python}-løkker - *the better* løkke??
---
class: explore
---
Under vises to interaktive kodevinduer. Begge kodene summerer de 5 første naturlige tallene.


::::{grid}
---

gutter: 1
---

:::{grid-item-card} 
`for`{l=python}-løkke
```{raw} html
---
file: interaktiv_kode/utforsk/utforsk_2_for_loop.html
---
```
:::

:::{grid-item-card} 
`while`{l=python}-løkke
```{raw} html
---
file: interaktiv_kode/utforsk/utforsk_2_while_loop.html
---
```
:::
::::


:::::