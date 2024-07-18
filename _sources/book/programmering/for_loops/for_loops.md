# `for`{l=python}-løkker

:::{admonition} Læringsmål: `for`{l=python}-løkker
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Lese og forstå `for`{l=python}-løkker som brukes `range`{l=python}-funksjonen.
* Kunne skrive grunnleggende `for`{l=python}-løkker som bruker `range`{l=python}-funksjonen til å løse matematiske problemer.

:::

:::{admonition} Gjør dette først!
---
class: warning, margin
---
Du bør ha lest {ref}`kapittelet om while-løkker <while-loops>` før du leser dette kapittelet, eller være godt kjent med bruken av `while`{l=python}-løkker.
:::


En `for`{l=python}-løkke kan tenkes på som en *spesiell* type `while`{l=python}-løkke som automatiserer tellingen for deg. Det finnes mange typer `for`{l=python}-løkker, men vi skal konsentrere oss om en som er mest nyttig i matematikk.


::::{admonition} Syntaks: `for`{l=python}-løkker med `range`{l=python}-funksjonen
---
class: theory
---

En `for`{l=python}-løkke med `range`{l=python}-funksjonen skrives på følgende måte:

```{code-block} python
for i in range(start, stop, step):
    # Gjøre noe for hvert tall i rekken
```

* `start`{l=python} er startverdien til `i`. Denne er frivillig og er satt til `start = 0`{l=python} som standard.
* `stop`{l=python} er stoppverdien til `i`. Denne må skrives.
* `step`{l=python} er steglengden til `i` (avstanden mellom hver verdi). Denne er frivillig og er satt til `step = 1`{l=python} som standard.
::::


Vi tar et eksempel for å vise hvordan en `for`{l=python}-løkke fungerer ved å sammenligne med fra {ref}`eksempel 1 fra while-løkker <while-loops-example-1>`.

::::{admonition} Grenser i `range`{l=python}-funksjonen
---
class: sidenote, margin
---
`range`{l=python}-funksjonen stopper *før* stoppverdien. I {ref}`eksempel 1 <for-loops-example-1>` ga `range(1, 6, 1)`{l=python}
tallene 1, 2, 3, 4 og 5, men ikke 6. 

::::


:::::{admonition} Eksempel 1: `for`{l=python}-løkke vs `while`{l=python}-løkke
---
class: example
name: for-loops-example-1
---
Følgende koder gir akkurat samme resultat.
::::{grid}
:gutter: 1

:::{grid-item-card} `for`{l=python}-løkke
```{code-block} python
---
linenos:
---
for i in range(1, 6, 1):
    print(f"{i = }")
```
:::

:::{grid-item-card} `while`{l=python}-løkke
```{code-block} python
---
linenos:
---
i = 1
while i <= 5:
    print(f"{i = }")
    i = i + 1
```
:::
::::

Vi kan merke oss at mens man med `while`{l=python}-løkka lager variabelen og oppdaterer `i`{l=python} selv, gjør `for`{l=python}-løkka dette for deg automatisk. `for`{l=python}-løkker er derfor en slags `while`{l=python}-løkke i bunnen. 


Utskriften vi får fra begge programmer er (kopier kodene og prøv selv!)

```console
i = 1
i = 2
i = 3
i = 4
i = 5
```


:::::

**Din tur**!


:::::{admonition} Underveisoppgave 1
---
class: check
--- 

Kopier `for`{l=python}-løkke koden fra {ref}`eksempel 1 <for-loops-example-1>`.

Deloppgave 1
: Juster programmet slik at det skriver ut tallene $i = 1, 2, \ldots, 10$.

::::{admonition} Løsning: deloppgave 1
---
class: solution, dropdown
---
Vi setter `start`{l=python} til `1`{l=python} og `stop`{l=python} til `11`{l=python} for å få tallene fra 1 til og med 10. Dette er fordi `range`{l=python}-funksjonen stopper én plass før `stop`{l=python}. I koden under har vi skrevet `stop`{l=python}-verdien som `10 + 1`{l=python} for å gjøre det tydeligere.
```{code-block} python
---
linenos:
---
for i in range(1, 10 + 1, 1):
    print(f"{i = }")
```
---

::::

Deloppgave 2
: Juster programmet slik at det skriver ut alle partallene $i \in \{2, 4, \ldots, 10\}$

::::{admonition} Løsning: deloppgave 2
---
class: solution, dropdown
---
For få partallene $i \in \{2, 4, \ldots, 10\}$, må vi gjøre følgende endringer:
1. Vi må sette startverdien til `start`{l=python} til `2`{l=python}. 
2. Vi må sette `step`{l=python} til `2`{l=python} så vi for hvert andre tall.
3. Vi må sette `stop`{l=python} til `10 + 1`{l=python} så vi får med oss $10$ som siste tall siden `range`{l=python}-funksjonen stopper før én plass før `stop`. 

```{code-block} python
---
linenos:
---
for in range(2, 10 + 1, 2):
    print(f"{i = }")
```
::::


Deloppgave 3
: Juster programmet slik at det skriver ut alle $i \in \{10, 20, 30, 40, \ldots, 100\}$.

::::{admonition} Løsning: deloppgave 3
---
class: solution, dropdown
---
Vi må gjøre følgende endringer for å få alle $i \in \{10, 20, 30, 40, \ldots, 100\}$:
1. Vi må endre `start`{l=python} til `10`{l=python}.
2. Vi må endre `step`{l=python} til `10`{l=python} slik at vi får hvert tiende tall.
3. Vi må sette `stop`{l=python} til `100 + 1`{l=python} for å få med oss $100$ som siste tall.

```{code-block} python
---
linenos:
---
for i in range(10, 100 + 1, 10):
    print(f"{i = }")
```

::::

:::::

Vi tar med en sammenlikning av {ref}`eksempel 2 fra while-løkker <while-loops-example-2>` for å vise hvordan vi kan skrive `for`{l=python}-løkker for å løse samme problem.

:::::{admonition} Eksempel 2: `for`{l=python}-løkke vs `while`{l=python}-løkke
---
class: example
name: for-loops-example-2
---
Vi skal regne ut summen av de 100 første naturlige tallene $n \in \{1, 2, 3, \ldots, 100\}$. Under to koder som løser problemet der den ene bruken `for`{l=python}-løkke og den andre en `while`{l=python}-løkke. 

::::{grid}
:gutter: 1

:::{grid-item-card} `for`{l=python}-løkke
```{code-block} python
---
linenos:
---
summen = 0
for n in range(1, 100 + 1, 1):
    summen = summen + n

print(f"{summen = }")
```
:::

:::{grid-item-card} `while`{l=python}-løkke
```{code-block} python
---
linenos:
---
summen = 0
n = 1

while heltall <= 100:
    summen = summen + n
    n = n + 1

print(f"{summen = }")
```
:::

::::
:::::


**Din tur**!

:::::{admonition} Underveisoppgave 2
---
class: check
---

Under vises et program som regner ut noe.

```{code-block} python
---
linenos:
---
p = 1
n = 1
while n <= 5:
    p = p * n
    n = n + 1

print(f"{p = }")
```

Deloppgave 1
: Kan du forklare hva programmet gjør (spesielt betydningen av linje 4)? 
: Kan du bestemme verdien programmet skriver ut *uten* å kjøre programmet først?

::::{admonition} Løsning: deloppgave 1
---
class: solution, dropdown
---
På linje 4 finner vi koden `p = p * n`{l=python}, som betyr at vi ganger den gamle verdien til `p`{l=python} med `n`{l=python} og lagrer resultatet i `p`{l=python}. Vi gjentar dette for $n \in \{1, 2, 3, \ldots, 4, 5\}$.
Vi kan lage en tabell for å spore endringene i `p`{l=python} og `n`{l=python}, der vi husker på at `p * n`{l=python} blir verdien til `p`{l=python} i neste iterasjon.

| `n`{l=python} | `p`{l=python} | `p * n`{l=python} |
| :---: | :---: | :---: |
| `1`{l=python} | `1`{l=python} | `1`{l=python} |
| `2`{l=python} | `1`{l=python} | `2`{l=python} |
| `3`{l=python} | `2`{l=python} | `6`{l=python} |
| `4`{l=python} | `6`{l=python} | `24`{l=python} |
| `5`{l=python} | `24`{l=python} | `120`{l=python} |

Den siste verdien til `p`{l=python} er `120`{l=python}, så da skriver programmet ut

```console
p = 120
```
:::: 


Deloppgave 2
: Skriv om programmet slik at det bruker en `for`{l=python}-løkke i stedet for en `while`{l=python}-løkke.

::::{admonition} Løsning: deloppgave 2
---
class: solution, dropdown
---
Vi må gjøre følgende endringer:

1. Vi kan bytte ut `while`{l=python}-løkka med en `for`{l=python}-løkke ved å bruke `range(1, 5 + 1, 1)`{l=python} for å få tallene $n \in \{1, 2, 3, 4, 5\}$. 
2. Vi må passe på at vi ikke øker verdien til `n`{l=python} ved å ta bort linja `n = n + 1`{l=python}.

Da får vi koden 

```{code-block} python
---
linenos:
---
p = 1
for n in range(1, 5 + 1, 1):
    p = p * n

print(f"{p = }")
```
::::


:::::