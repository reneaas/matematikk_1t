# `while`{l=python}-løkker

:::{admonition} Læringsmål: `while`{l=python}-løkker
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Kunne lese `while`{l=python}-løkker. 
* Kunne skrive `while`{l=python}-løkker som løser matematiske problemer.
:::

En `while`{l=python}-løkke er noe vi bruker når vi ønsker å gjenta en eller flere kodelinjer igjen og igjen så lenge en betingelse er oppfylt. 


:::{admonition} Syntaks: `while`{l=python}-løkker
---
class: theory
---
En `while`{l=python}-løkke skrives på følgende måte:

```{code-block} python
while betingelse:
    # Gjøre noe så lenge `betingelse` er sann!
```
:::

Vi tar et eksempel for å vise hvordan en `while`{l=python}-løkke fungerer. 

::::{admonition} Eksempel 1
---
class: example
name: while-loops-example-1
---
Programmet under printer ut heltall fra 1 til 5. Vi skal svare på følgende spørsmål.
1. Hva er betingelsen i programmet?
2. Hva betyr koden `i = i + 1`{l=python} på linje 4?

```{code-block} python
---
linenos:
---
i = 1
while i <= 5:
    print(f"{i = }")
    i = i + 1

```
som gir ut utskriften
```console
i = 1
i = 2
i = 3
i = 4
i = 5
```

La oss svare på de to spørsmålene:

Spørsmål 1: Hva er betingelsen?
: Betingelsen i programmet er `i <= 5`{l=python} som betyr at koden med innrykk i `while`{l=python}-løkken vil kjøre så lenge `i`{l=python} er mindre eller lik 5.

Spørsmål 2: Hva betyr `i = i + 1`{l=python}?
: Koden overskriver den gamle verdien til `i`{l=python} med en ny verdi `i + 1`{l=python}. Vi kan lese dette som at vi *øker* verdien til `i`{l=python} med 1.
:::: 

**Din tur**!

::::{admonition} Underveisoppgave 1
---
class: check
---
I det interaktive kodevinduet under finner du koden fra {ref}`eksempel 1 <while-loops-example-1>`. 


:::{raw} html
---
file: interaktiv_kode/underveisoppgave_1.html
---
:::


Deloppgave 1
: Endre programmet fra {ref}`eksempel 1 <while-loops-example-1>` slik at det skriver ut alle heltall $i \in \{1, 2, \ldots, 10\}$.

:::{admonition} Løsning: deloppgave 1
---
class: solution, dropdown
---

For å løse denne oppgaven, endrer vi betingelsen i `while`{l=python}-løkken til `i <= 10`{l=python}. Programmet blir da:
```{code-block} python
---
linenos:
emphasize-lines: 2
---
i = 1
while i <= 10:
    print(f"{i = }")
    i = i + 1

```
:::

<br>

Deloppgave 2
: Endre programmet fra {ref}`eksempel 1 <while-loops-example-1>` slik at det skriver ut alle heltall $i \in \{2, 4, 6, \ldots, 10\}$.

:::{admonition} Løsning: deloppgave 2
---
class: solution, dropdown
---

For å løse denne oppgaven, endrer startverdien til `i`{l=python} til `i = 2`{l=python} på linje 1, og vi endrer linje 4 til `i = i + 2`{l=python} for å øke `i`{l=python} med 2 i hver iterasjon. Da blir programmet:
```{code-block} python
---
linenos:
emphasize-lines: 1, 4
---
i = 2
while i <= 10:
    print(f"{i = }")
    i = i + 2
```
:::

::::

Vi tar et eksempel til for å vise hvordan vi kan bruke `while`{l=python}-løkker til å løse matematiske problemer.


:::{admonition} Hvorfor `summen`{l=python} og ikke `sum`{l=python}?
---
class: sidenote, margin
---

I Python er `sum`{l=python} en innebygd funksjon. Hvis vi bruker `sum`{l=python} som variabelnavn, overskriver vi funksjonen.
Selv om det ikke er farlig for et kort program her, så bør vi unngå å skrive over innebygde funksjoner så vi ikke får uventede feil. 

:::

::::{admonition} Eksempel 2: Legenden om Gauss
---
class: example
name: while-loops-example-2
--- 
En legende forteller om en kommende matematiker med navn Gauss som fikk i oppgave av læreren sin å summere de 100 første naturlige tallene for hånd. 
Han fant en lur løsning på dette, men vi kan løse det enda raskere enn Gauss ved å skrive et program som gjør det for oss. 

For å komme i gang, kan vi lage oss et flytdiagram som tar for seg stegene vi må gjøre i et program (tenk på det som om du skulle gjort dette for hånd!)

```{include} ./flytdiagrammer/eksempel_2.md
```

<br>

Vi kan oversette flytdiagrammet til kode som følger (les nøye og se på sammenhengen mellom flytdiagrammet og koden!):

```{code-block} python
---
linenos:
---
summen = 0      # Steg 1 i flytdiagrammet
heltall = 0     # Steg 2 i flytdiagrammet

while heltall <= 100:           # Steg 3 i flytdiagrammet
    summen = summen + heltall   # Steg 4 i flytdiagrammet
    heltall = heltall + 1       # Steg 5 i flytdiagrammet

print(f"{summen = }")   # Steg 6 i flytdiagrammet
```

Kjører vi programmet, vår vi utskriften

```console
summen = 5050
```

Altså er summen av de 100 første naturlige tallene lik 5050
::::

Så er det **din tur**!

::::{admonition} Underveisoppgave 2
---
class: check
---
Koden fra {ref}`eksempel 2 <while-loops-example-2>` er vist i det interaktive kodevinduet under:

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgave_2.html
---
:::

<br>

Deloppgave 1
: Endre programmet fra {ref}`eksempel 2 <while-loops-example-2>` slik at det regner ut summen av alle partall opp til og med 100.


:::{admonition} Løsning: deloppgave 1
---
class: solution, dropdown
---
Vi kopierer koden gjør to endringer:
1. Vi endrer startverdien til `heltall`{l=python} til `heltall = 2`{l=python} på linje 2.
2. Vi endrer linje 6 til `heltall = heltall + 2`{l=python} for å øke `heltall`{l=python} med 2 i hver iterasjon. 

```{code-block} python
---
linenos:
emphasize-lines: 2, 6
---
summen = 0      # Steg 1 i flytdiagrammet
heltall = 2     # Steg 2 i flytdiagrammet

while heltall <= 100:           # Steg 3 i flytdiagrammet
    summen = summen + heltall   # Steg 4 i flytdiagrammet
    heltall = heltall + 2       # Steg 5 i flytdiagrammet

print(f"{summen = }")   # Steg 6 i flytdiagrammet
```

Kjører vi programmet, får vi utskriften

```console
summen = 2550
```
:::

<br>

Deloppgave 2
: Juster programmet ditt fra deloppgave 1 slik at det regner ut summen av de hundre første partallene. 
:::{admonition} Hint: deloppgave 2
---
class: hints, dropdown
---

Her skal du summere opp partall frem til du har summert opp 100 tall. 
Kan du tenke deg en betingelse for dette? Kanskje du må lage deg en ny variabel også?
:::


:::{admonition} Løsning: deloppgave 2
---
class: solution, dropdown
---
For å løse dette problemet, må vi gjøre noen endringer i programmet:
1. Vi trenger en ny variabel som teller antall partall vi har summert opp. Vi kan kalle denne for `antall_partall`{l=python}. 
2. Vi må endre betingelsen fra `heltall <= 100`{l=python} til `antall_partall <= 100`{l=python} siden vi nå skal summere opp partall frem til vi har summert 100 av dem.
3. Vi må legge til en linje i `while`{l=python}-løkka som øker `antall_partall`{l=python} med 1 i hver iterasjon for å telle opp antall partall vi har summert.

Med endringene foreslått over, vil koden bli som følger:

```{code-block} python
---
linenos:
emphasize-lines: 3, 5, 8
---
summen = 0
heltall = 2
antall_partall = 0

while antall_partall <= 100:
    summen = summen + heltall
    heltall = heltall + 2
    antall_partall = antall_partall + 1

print(f"{summen = }")
```
:::

:::: 
