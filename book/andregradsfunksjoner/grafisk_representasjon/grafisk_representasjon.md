# Hva er en andregradsfunksjon?

Først skal vi ta litt tid på å utforske hvordan en andregradsfunksjon ser ut grafisk, og hvordan koeffisientene til funksjonen påvirker hvordan funksjonen ser ut. <br>

```{admonition} Læringsmål: andregradsfunksjoner
:class: tip
Etter å ha gått gjennom denne seksjonen, er målet at du skal kunne:
* Forklare hva en andregradsfunksjon er, og kjenne til den algebraiske og grafiske representasjonen av andregradsfunksjoner.
* Forstå hvordan koeffisientene til andregradsfunksjonen bestemmer formen på grafen til funksjonen.
```

## Algebraisk representasjon

Vi skal ta en kort titt på den algebraiske definisjonen av en andregradsfunksjon. 

```{admonition} Definisjon (algebraisk): Andregradsfunksjon
:class: theory
En andregradsfunksjon $f(x)$ er en funksjon på formen

$$
f(x) = ax^2 + bx + c,
$$

der $a, b, c \in \mathbb{R}$ er koeffisientene til andregradsfunksjonen. 

Merknad 1
: Merk **spesielt** at $a$ kalles for den **ledende koeffisienten** til andregradsfunksjonen. En *ledende koeffisient* er koeffisienten til den høyeste potensen av $x$ i et algebraisk uttrykk. 

Merknad 2
: La oss understreke at $a$ **ikke** er stigningstall. Dette er **kun** tilfelle for lineære funksjoner $g(x) = ax + b$.
```

````{admonition} Eksempel 1: Andregradsfunksjoner
:class: example
I tabellen under vises en rekke andregradsfunksjoner og deres koeffisienter.

| Funksjon | $a$ | $b$ | $c$ |
|:----------|:-----:|:-----:|:-----:|
| $f(x) = 2x^2 + 3x + 1$ | $2$ | $3$ | $1$ |
| $g(x) = -x^2 + 4x - 2$ | $-1$ | $4$ | $-2$ |
| $h(x) = 3x^2 - 2x + 5$ | $3$ | $-2$ | $5$ |
| $p(x) = 2x^2$ | $2$ | $0$ | $0$ |
| $q(x) = x^2 - 3x$ | $1$ | $-3$ | $0$ |
| $r(x) = -x^2 + 4$ | $-1$ | $0$ | $4$ |
````

Så er det din tur:

````{admonition} Underveisoppgave 1
:class: check
Fyll ut tabellen med koeffisientene eller funksjonsuttrykket til andregradsfunksjonene:

| Funksjon | $a$ | $b$ | $c$ |
|:----------|:-----:|:-----:|:-----:|
| $f(x) = 3x^2 + 2x + 1$ | | | |
| $g(x) = -2x^2 + 5x - 3$ | | | |
| $h(x) = $ | $-1$ | $6$ | $0$ |
| $p(x) = 3x^2$ | | | |
| $q(x) = x^2 - 2x$ | | | |
| $r(x) = $ | $-2$ | $0$ | $-5$ |

```{admonition} Løsning
:class: solution, dropdown

| Funksjon | $a$ | $b$ | $c$ |
|:----------|:-----:|:-----:|:-----:|
| $f(x) = 3x^2 + 2x + 1$ | $3$ | $2$ | $1$ |
| $g(x) = -2x^2 + 5x - 3$ | $-2$ | $5$ | $-3$ |
| $h(x) = -x^2 + 6x$ | $-1$ | $6$ | $0$ |
| $p(x) = 3x^2$ | $3$ | $0$ | $0$ |
| $q(x) = x^2 - 2x$ | $1$ | $-2$ | $0$ |
| $r(x) = -2x^2 - 5$ | $-2$ | $0$ | $-5$ |
```
````



## Grafisk representasjon


Under vises grafen til tre forskjellige andregradsfunksjoner tegnet i samme koordinatsystem. 


```{figure} ./figurer/teori/intro_tre_andregradsfunksjoner.svg
:name: teori_tre_andregradsfunksjoner
:width: 80%

Grafen til tre forskjellige andregradsfunksjoner med ulike koeffisienter. 
```

Nå skal du utforske litt og se om du kan komme fram til hvordan koeffisientene $a$, $b$ og $c$ påvirker grafen til en andregradsfunksjon. 

````{admonition} Underveisoppgave 2
:class: check

Bruk den interaktive grafen under til å se om du kan lage tre grafer tilsvarende de i {numref}`teori_tre_andregradsfunksjoner`. <br>

* Hvordan påvirker verdien til $a$ grafen?
* Hvordan påvirker verdien til $b$ grafen?
* Hvordan pårvirker verdien til $c$ grafen?
* Legger du merke til noe spesielt med nullpunkter for andregradsfunksjoner?

Hint: Prøv å endre én og én koeffisient av gangen for å se hvordan de påvirker hvordan grafen ser ut.

```{raw} html
:file: ./figurer/underveisoppgaver/interaktive_plot/underveisoppgave_1.html
```

````