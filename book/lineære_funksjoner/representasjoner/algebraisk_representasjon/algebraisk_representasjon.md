# Algebraisk representasjon av lineære funksjoner


```{admonition} Læringsmål: representasjoner av lineære funksjoner
:class: tip
Målet med denne seksjonen er at du skal kunne:
* Ha en grunnleggende forståelse av funksjonsbegrepet.
* Kjenne til den algebraiske representasjonen av lineære funksjoner.
* Kunne regne ut funksjonsverdier for en lineær funksjon.
```
---

En representasjon er en måte å uttrykke noe på. Når vi jobber med rette linjer, er de to vanligste måtene å representere linjer på, algebraisk og grafisk. Med algebraisk representasjon, mener vi en formel som beskriver linja. Med grafisk representasjon, mener vi en tegning av linja i et koordinatsystem.

---

## Algebraisk representasjon av lineære funksjoner
En lineær funksjon er en spesiell rett linje der $y$-verdien er bestemt av $x$-verdien. Vi skal komme mer presist tilbake til funksjonsbegrepet senere, men først tar vi en litt kortfattet og enkelt definisjon av en lineær funksjon:

````{admonition} Definisjon: lineær funksjon
:class: theory
En **lineær funksjon** $f$ er en formel som kan skrives som en likning på formen 

$$
f(x) = ax + b.
$$ (eq:linear_funksjon)



Merknad 1
: Sammenhengen mellom $y = ax + b$ og uttrykket over, er at vi tydeliggjør at $y$ er bestemt av $x$ ved å bytte ut $y = f(x)$. Vi sier at $f$ er funksjonen, mens $f(x)$ er *funksjonsverdien* eller *funksjonsuttrykket*.

Merknad 2
: Konstantene $a$ og $b$ kalles for **koeffisientene** til den lineære funksjonen. Koeffisienten $a$ kalles ofte for **stigningstallet** og konstanten $b$ kalles **konstantleddet** eller **skjæringen med $y$-aksen**. 

Merknad 3
: Det er *ingenting* spesielt med at vi bruker $f$ for *funksjon* annet enn at dette en vanlig. Vi kommer til å møte på funksjoner som heter $g$ og har funksjonsverdier $g(x)$, funksjoner som heter $h$ og har funksjonsverdier $h(x)$, og så videre. 
````

Vi tar noen eksempler på lineære funksjoner med skrivemåten over:

```{admonition} Eksempel 1: algebraisk representasjon av lineære funksjoner
:class: example

Under vises funksjonsuttrykket til tre lineære funksjoner. Vi skal bestemme stigningstallet og konstantleddet til hver av funksjonene. 

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = 3x - 1$ | $3$ | $-1$ |
| $g$ | $g(x) = -2x + 4$ | $-2$ | $4$ |
| $h$ | $h(x) = -x + 2$ | $-1$ | $2$ |
| $r$ | $r(x) = 3$ | $0$ | $3$ |
| $s$ | $s(x) = \frac{1}{2}x$ | $\frac{1}{2}$ | $0$ |

```

Og så er det **din tur**!

````{admonition} Underveisoppgave 1: algebraisk representasjon av lineære funksjoner
:class: check

Fyll ut tabellen under: 

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = -3x + 2$ |  |  |
|  | $t(x) = ax + 3$ | $2$ | |
| $p$ | | $-1$ | $1$ |
| $q$ | $q(x) = 4$ |  |  |
| $r$ |  | $-2$ | $0$ |

```{admonition} Løsning
:class: solution, dropdown

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = -3x + 2$ | $-3$ | $2$ |
| $t$ | $t(x) = 2x + 3$ | $2$ | $3$ |
| $p$ | $p(x) = -x + 1$ | $-1$ | $1$ |
| $q$ | $q(x) = 4$ | $0$ | $4$ |
| $r$ | $r(x) = -2x$  | $-2$ | $0$ |
```
````

## Funksjonsverdier
Når vi introduserte $f(x)$ som notasjon, så sa vi $f(x) = y$ var funksjonsverdien til $f$ for en bestemt $x$-verdi. Her skal vi ta en titt på skrivemåten og hvordan man regner ut funksjonsverdier med en funksjonsuttrykket til $f$. Vi sier for eksempel at $f(2)$ er funksjonsverdien til $f$ i $x = 2$. Mer generelt er $f(a)$ funksjonsverdien til $f$ i $x = a$. 

```{admonition} Eksempel 2: funksjonsverdier
:class: example

Under vises eksempler på utregning av funksjonsverdier. Vi erstatter rett og slett verdien til $x$ alle steder den opptrer i funksjonsuttrykket (formelen/likningen) til funksjonen og regner ut:

| Funksjon | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = 3x - 1$ | $2$ | $f(2) = 3\cdot 2 - 1 = 6 - 1 = 5$ |
| $g(x) = -2x + 4$ | $3$ | $g(3) = -2\cdot 3 + 4 = -6 + 4 = -2$ |
| $h(x) = -x + 2$ | $0$ | $h(0) = -0 + 2 = 2$ |
| $r(x) = 3$ | $1$ | $r(1) = 3$ |
| $s(x) = \frac{1}{2}x$ | $4$ | $s(4) = \frac{1}{2}\cdot 4 = 2$ |

```

Og så er det **din tur**!


````{admonition} Underveisoppgave 2: funksjonsverdier
:class: check

Regn ut funksjonsverdiene i tabellen under:

| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = -3x + 2$ | $1$ |  |
| $t(x) = 2x + 3$ | $0$ |  |
| $p(x) = -x + 1$ | $3$ |  |
| $q(x) = 4$ | $2$ |  |
| $r(x) = -2x$ | $5$ |  |



```{admonition} Løsning
:class: solution, dropdown
| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = -3x + 2$ | $1$ | $f(1) = -3\cdot 1 + 2 = -3 + 2 = -1$  |
| $t(x) = 2x + 3$ | $0$ | $t(0) = 2\cdot 0 + 3 = 0 + 3 = 3$  |
| $p(x) = -x + 1$ | $3$ | $p(3) = -3 + 1 = -2$  |
| $q(x) = 4$ | $2$ | $q(2) = 4$  |
| $r(x) = -2x$ | $5$ | $r(5) = -2\cdot 5 = -10$  |
```
````

## Regne ut funksjonsverdier med Python
Vi kan bruke Python som en kalkulator for å regne ut funksjonsverdier. 

::::{admonition} Eksempel 3: funksjonsverdier i Python
---
class: example
---

La oss regne ut funksjonsverdien til 

$$
f(x) = 3x - 1,
$$

i x = 2. Da kan vi skrive følgende kode i Python:


```{code-block} python
---
linenos:
---
x = 2
y = 3*x - 1

print(f"{y = }")

```
som gir utskriften
```console
y = 5
```
::::

Men i eksemplet over bruker vi ikke notasjonen for funksjoner. Men i Python har vi faktisk støtte for akkurat dette. 


:::{admonition} Ordforklaring: syntaks
---
class: sidenote, margin
--- 
Ordet **syntaks** betyr "regler for å skrive kode". Tenk på det som grammatikk - men i motsetning til norsklæreren, så skjønner ikke Python hva du mener hvis du ikke skriver riktig.
:::

::::{admonition} Syntaks: Funksjoner i Python
---
class: theory
---
En funksjon i Python har følgende syntaks:


```{code-block} python
def f(x):
    return funksjonsuttrykk
```