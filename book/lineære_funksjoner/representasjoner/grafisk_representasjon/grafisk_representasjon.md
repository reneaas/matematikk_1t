# Grafisk representasjon av lineære funksjoner

:::{admonition} Læringsmål: representasjoner av lineære funksjoner
---
class: tip
---

Målet med denne seksjonen er at du skal kunne:
* Lese av og tegne koordinater i et koordinatssystem.
* Kunne lage en verditabell og tegne grafen til en lineær funksjon i et koordinatssystem.
* Ved å lese av stigningstall og skjæring med $y$-aksen fra en graf.
:::
---

Når vi kjenner formelen til en lineær funksjon $f(x) = ax + b$ kan vi tegne **grafen** til funksjonen. I mange tilfeller, er det nyttig å bruke grafen til å få oversikt over egenskapene til en funksjon og for å løse problemer i praksis. 
Selv om du ofte vil bruke digitale hjelpemidler til å tegne grafen, er det å kunne skissere grafen raskt for hånd en uvurderlig ferdighet i matematikk, spesielt når man skal få rask oversikt over et problem man prøver å løse.

## Grafen til en lineær funksjon

::::{admonition} Oppskrift: Tegne grafen til en funksjon
---
class: theory
---

Vi følger stegene under for å tegne grafen til en lineær funksjon $f(x) = ax + b$:

Steg 1: Lage en verditabell av punkter $(x, y) = (x, f(x))$
: $\to$ Velg ut en liste med $x$-verdier.
: $\to$ Regn ut $f(x)$ for hver $x$-verdi. 

Steg 2: Tegne punktene i et koordinatsystem
: $\to$ Tegn opp en $x$-akse og en $y$-akse i et koordinatsystem.
: $\to$ Plasser punktene $(x, f(x))$ i koordinatsystemet.

Steg 3: Tegne rette linjer mellom nabopunkter i koordinatsystemet
: $\to$ Vi tegner rette linjer mellom nabopunktene for å få en grafisk representasjon av funksjonen. 
: $\to$ Dette blir **grafen** til funksjonen.

::::


::::{admonition} Påminnelse: koordinatssystem
---
class: dropdown, sidenote
---

Koordinatsystemet får vi ved å lage oss to tallinjer som står $90^\circ$ på hverandre, der null på hver tallinje ligger på samme sted. Vi kaller dette punktet for **origo**, og det har koordinatene $(0, 0)$.

* Den vannrette linja kaller vi oftest $x$-aksen. Et annet navn for aksen er *førsteaksen*.
* Den loddrette linja kaller vi $y$-aksen. Et annen navn for denne aksen er *andreaksen*. 

Hvis vi har et punkt $(x, y)$ i koordinatsystemet, betyr det at vi går $x$ enheter langs $x$-aksen og $y$ enheter langs $y$-aksen fra origo. For eksempel betyr $(3, 2)$ at vi først flytter oss 3 plasser langs $x$-aksen og deretter 2 plasser langs $y$-aksen. Da står vi på punktet $(3, 2)$. Se figuren under: 

:::{figure} ./figurer/teori/koordinatsystem.svg
---
name: koordinatsystem
width: 80%
---

Viser et eksempel på et koordinatsystem der punktet $(3, 2)$ er markert. For å lese av $x$-koordinaten, trekker vi en linje fra punktet normalt ned på $x$-aksen. For å lese av $y$-koordinaten, trekker vi en linje fra punktet normalt bort på $y$-aksen.
:::

::::

Vi tar et eksempel:

::::{admonition} Eksempel 1: Tegne grafen til en lineær funksjon
---
class: example
---

Vi skal tegne grafen til den lineære funksjonen

$$
f(x) = 2x - 4.
$$

Steg 1: Lage verditabell
: Vi lager en tabell bestående av punkter $(x, y) = (x, f(x))$ som grafen til funksjonen går gjennom. Da må vi regne ut funksjonsverdiene for hver $x$-verdi vi velger oss.

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | $-6$ | $-4$ | $-2$ | $0$ | $2$ |

<br>

Steg 2: Tegn koordinatene i et koordinatsystem
: Vi tegner inn punktene $(x, f(x))$ i et koordinatsystem, med $x$-verdiene på førsteaksen og $f(x)$-verdiene på andreaksen. Da får vi

:::{figure} ./figurer/eksempler/eksempel_1_koordinatsystem.svg
---
name: eksempel_1_koordinatsystem
width: 80%
---
:::

Steg 3: Tegn rette linjer mellom nabopunkter i koordinatsystemet
: Vi tegner rette linjer mellom punktene for å få en grafisk representasjon av funksjonen. Da får vi

:::{figure} ./figurer/eksempler/eksempel_1_graf.svg
---
name: eksempel_1_graf
width: 80%
---
:::

::::

Gjett hva... nå er det **din tur**!


:::::{admonition} Underveisoppgave 1
---
class: check
---
En lineær funksjon er gitt ved

$$
f(x) = -x + 2. 
$$


<br>

Deloppgave 1
: Fyll ut verditabellen under:

    | $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
    | :---: | :---: | :---: | :---: | :---: | :---: |
    | $f(x)$ |  |  |  |  |  |


:::{admonition} Fasit
---
class: answer, dropdown
---
| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | $3$ | $2$ | $1$ | $0$ | $-1$ |
:::

<br>

Deloppgave 2
: Tegn koordinatene i et koordinatsystem.

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1_med_punkter.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-1
width: 80%
---
Viser punktene fra verditabellen i deloppgave 1 i et koordinatsystem.
:::

::::

<br>

Deloppgave 3:
: Tegn grafen til $f$.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1_med_graf.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-underveisoppgave-1-graf
width: 80%
---
Viser grafen til funksjonen $f(x) = -x + 2$.
:::
::::

:::::





## Koeffisientene $a$ og $b$ i en lineær funksjon fra grafen

Når vi har grafen til en lineær funksjon, kan vi lære oss å lese av stigningstallet $a$ og konstantleddet $b$ direkte fra grafen.

```{admonition} Lese av koeffisientene fra grafen til en lineær funksjon
:class: theory
Gitt grafen til en lineær funksjon $f(x) = ax + b$ kan vi lese av koeffisientene som følger:

Stigningstallet $a$
: Stigningstallet $a$ er lik hvor mye $y$-verdien til grafen endrer seg når vi øker $x$ med én. 

Konstantleddet $b$
: Konstantleddet $b$ er lik $y$-verdien til grafen når $x = 0$. Med andre ord $y$-verdien der grafen skjærer $y$-aksen (andreaksen).
```

La oss se på et eksempel


:::::{admonition} Eksempel 2: lese av koeffisientene til en lineær funksjon fra graf
:class: example

Grafen til en funksjon $f$ er vist i {numref}`fig-lineære-funksjoner-grafisk-representasjon-eksempel-2`.

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-eksempel-2
width: 80%
---
Viser grafen til en lineær funksjon $f$.
:::

Bestem $f(x)$ fra grafen. 

::::{admonition} Løsning
---
class: solution
---
 
Vi kan lese av stigningstallet $a$ og konstantleddet $b$ direkte fra grafen slik som forklart over.

Stigningstallet
: Vi starter på en $x$-verdi og ser hvor mye $y$-verdien endrer seg når vi øker $x$ med én. Starter vi på $x = 0$, så er $y = f(0) = 6$. Øker vi $x$ med én, har vi at $x = 1$. Da er $y = f(1) = 4$. Dermed er endringen av $y$-verdien $a = -2$ som også er stigningstallet til grafen.

Konstantleddet
: Vi ser på $y$-verdien der grafen skjærer $y$-aksen. Når $x = 0$ er $y = f(0) = 6$. Dermed er konstantleddet $b = 6$. 


Altså er 

$$
f(x) = -2x + 6.
$$
::::

:::::


Og så var det **din tur**!

````{admonition} Underveisoppgave 2
:class: check

Under vises grafen til en lineær funksjon $g$. Bruk grafen til å bestemme $g(x)$. 

```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
:name: underveisoppgave_2
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown

Stigningstallet
: Når vi går fra $x = 0$ til $x = 1$, går $y$-verdien fra $g(0) = -2$ til $g(1) = 1$ som er en økning på $3$. Dermed er stigningstallet $a = 3$.

Konstantleddet
: Når $x = 0$ er $y = g(0) = -2$. Dermed er konstantleddet $b = -2$.

Altså er funksjonsuttrykket gitt ved 

$$
g(x) = 3x - 2.
$$
```
````


## Oppgaver

:::::{admonition} Oppgave 1
---
class: problem-level-1
---

Grafen til en lineær funksjon $f$ er vist i {numref}`fig-lineære-funksjoner-grafisk-representasjon-oppgave-1`.

:::{figure} ./figurer/oppgaver/oppgave_1.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-oppgave-1
width: 80%
---
Viser grafen til en lineær funksjon $f$.
:::


Deloppgave 1
: Bruk grafen til å bestemme $f(-1)$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(-1) = 0
$$
:::

<br>


Deloppgave 2
: Bruk grafen til å bestemme koordinatene til punktet $(2, f(2))$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
(2, f(2)) = (2, -3)
$$
:::

<br>


Deloppgave 3
: Bruk grafen til å bestemme stigningstallet og konstantleddet til $f$. 


:::{admonition} Fasit
---
class: answer, dropdown
---
Stigningstall
: $a = -1$

Konstantledd
: $b = -1$
:::

<br>

Deloppgave 4
: Bestem $f(x)$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -x - 1
$$
:::
:::::

:::::{admonition} Oppgave 2
---
class: problem-level-1
---

Funksjonsuttrykket til $f$ er gitt som 

$$ f(x) = 2x - 3 $$

Deloppgave 1
: Fyll ut verditabellen for $f$ under: 

| x | f(x) | y|
|:---:|:---:|:---:|
| $- 1$ | $f(-1) = 2\cdot (-1) - 3$ | $-5$ |
| $0 $ | | |
| $1 $ | | | 
| $2 $ | | |
| $3 $ | | |

:::{admonition} Fasit
---
class: answer, dropdown
---
| x | f(x) | y|
|:---:|:---:|:---:|
| $- 1$ | $f(-1) = 2\cdot (-1) - 3 = -5$ | $-5$ |
| $0 $ | $f(-1) = 2\cdot 0 - 3 = -3$  | $-3$ |
| $1 $ | $f(1) = 2\cdot (1) - 3 = -1$ | $-1$ | 
| $2 $ | $f(2) = 2\cdot (2) - 3 = 1$  | $1$ |
| $3 $ | $f(3) = 2\cdot (3) - 3 = 3$  | $3$ |
:::

<br>


Deloppgave 2
: Finn frem papir og blyant. Tegn opp et passende koordinatsystem for grafen til $f$. 

:::{admonition} Hint
---
class: hints, dropdown
---
Se på verdiene regnet ut i deloppgave 1. 
* Hva er den minste og den største verdien for x?
* Hva er den minste og den største verdien for y?
:::

<br>


Deloppgave 3
: Tegn grafen til $f$ i koordinatsystemet du akkurat laget. 


:::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_2.svg
---
name: fig-lineære-funksjoner-grafisk-representasjon-oppgave-2
width: 80%
---
Viser grafen til $f(x)= 2x - 3$.
:::

:::

<br>

Deloppgave 4
: Bruk grafen til å bestemme stigningstallet og konstantleddet til funksjonen. Sjekk svarene dine ved å studere funksjonsuttrykket. 

:::{admonition} Fasit
---
class: answer, dropdown
---
:$a = 2$
:$b = -3$
:::
:::::
