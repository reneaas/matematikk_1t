# Grafisk representasjon av lineære funksjoner

Når vi kjenner formelen til en lineær funksjon $f(x) = ax + b$ kan vi tegne **grafen** til funksjonen. I mange tilfeller, er det nyttig å bruke grafen til å få oversikt over egenskapene til en funksjon og for å løse problemer i praksis. 
Selv om du ofte vil bruke digitale hjelpemidler til å tegne grafen, er det å kunne skissere grafen raskt for hånd en uvurderlig ferdighet i matematikk, spesielt når man skal få rask oversikt over et problem man prøver å løse.

## Grafen til en lineær funksjon
For å komme fram til grafen til en funksjon, kan vi følge en enkel oppskrift:

Steg 1: Lage en verditabell
: Vi velger ut en liste med $x$-verdier som vi ønsker å bruke til å tegne grafen til $x$. Deretter regner vi ut funksjonsverdiene $f(x)$ for hver $x$-verdi vi har valgt. Dette gir oss en **verditabell** bestående av punkter $(x, y) = (x, f(x))$ som grafen til funksjonen går gjennom.

Steg 2: Tegne punktene i et koordinatsystem
: Vi tegner inn punktene $(x, f(x))$ i et koordinatsystem, med $x$-verdiene på førsteaksen og $f(x)$-verdiene på andreaksen.

Steg 3: Tegne rette linjer mellom nabopunkter i koordinatsystemet
: Vi tegner rette linjer mellom nabopunktene for å få en grafisk representasjon av funksjonen. Dette blir **grafen** til funksjonen.


Vi tar et eksempel:

````{admonition} Eksempel 1: Tegne grafen til en lineær funksjon
:class: example

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
```{figure} ./figurer/eksempler/eksempel_1_koordinatsystem.svg
:name: eksempel_1_koordinatsystem
:width: 80%
```

Steg 3: Tegn rette linjer mellom nabopunkter i koordinatsystemet
: Vi tegner rette linjer mellom punktene for å få en grafisk representasjon av funksjonen. Da får vi
```{figure} ./figurer/eksempler/eksempel_1_graf.svg
:name: eksempel_1_graf
:width: 80%
```
````

Gjett hva... nå er det **din tur**!


`````{admonition} Underveisoppgave 1
:class: check

Tegn grafen til en lineære funksjonen 

$$
f(x) = -x + 2. 
$$

Steg 1:
: Fyll ut verditabellen under:

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ |  |  |  |  |  |

<br>

Steg 2: 
: Tegn koordinatene i et koordinatsystem.

Steg 3:
: Tegn rette linjer mellom nabopunktene i koordinatsystemet (men *nabopunkter*, mener vi to punkter med naboverdier på $x$-aksen!)

````{admonition} Løsning
:class: solution, dropdown

Vi følger stegene for å tegne grafen til funksjonen:

Steg 1: Lage verditabell
: Vi lager en tabell bestående av punkter $(x, y) = (x, f(x))$ som grafen til funksjonen går gjennom. Da må vi regne ut funksjonsverdiene for hver $x$-verdi vi velger oss.

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | $3$ | $2$ | $1$ | $0$ | $-1$ |

<br>

Steg 2 og 3:
: Vi tegner inn punktene fra verditabellen og tegner inn rette linjer mellom dem i samme koordinatsystem. Da får vi

```{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
:name: underveisoppgave_1
:width: 80%
```
````
`````


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


````{admonition} Eksempel 2: lese av koeffisientene til en lineær funksjon fra graf
:class: example

Vi har grafen til en funksjon $f(x)$ som vist i figure under:

```{figure} ./figurer/eksempler/eksempel_2.svg
:name: eksempel_2
:width: 80%
```

Bestem $f(x)$ fra grafen. 


**Løsning**: 
Vi kan lese av stigningstallet $a$ og konstantleddet $b$ direkte fra grafen slik som forklart over.

Stigningstallet
: Vi starter på en $x$-verdi og ser hvor mye $y$-verdien endrer seg når vi øker $x$ med én. Starter vi på $x = 0$, så er $y = f(0) = 6$. Øker vi $x$ med én, har vi at $x = 1$. Da er $y = f(1) = 4$. Dermed er endringen av $y$-verdien $a = -2$ som også er stigningstallet til grafen.

Konstantleddet
: Vi ser på $y$-verdien der grafen skjærer $y$-aksen. Når $x = 0$ er $y = f(0) = 6$. Dermed er konstantleddet $b = 6$. 


Altså er 

$$
f(x) = -2x + 6.
$$
````


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


