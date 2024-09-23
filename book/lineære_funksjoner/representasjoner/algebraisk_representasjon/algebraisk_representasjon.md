# Algebraisk representasjon


:::{admonition} Læringsmål: representasjoner av lineære funksjoner
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Kunne representere en lineær funksjon algebraisk, og kunne lese av stigningstall og konstantledd.
* Kunne regne ut funksjonsverdier med funksjonsuttrykket til en lineær funksjon.
* Kunne bruke Python til å regne ut funksjonsverdier til en lineær funksjon.
:::
---

En representasjon er en måte å uttrykke noe på. Når vi jobber med rette linjer, er de to vanligste måtene å representere linjer på, algebraisk og grafisk. Med algebraisk representasjon mener vi en formel som beskriver linja. Med grafisk representasjon mener vi en tegning av linja i et koordinatsystem.

---


## Algebraisk representasjon av lineære funksjoner
En lineær funksjon er en rett linje der $y$-verdien er bestemt av $x$-verdien. 

::::{admonition} Stigningstall og skjæring med $y$-aksen
---
class: sidenote, margin
---
Vi skal se nærmere på betydningen av stigningstall og skjæring med $y$-aksen når vi ser på grafisk representasjon av lineære funksjoner i neste delkapittel.
::::


::::{admonition} Definisjon: lineær funksjon
---
class: theory
---
En **lineær funksjon** $f$ er en formel som kan skrives som en likning på formen 

$$
f(x) = ax + b.
$$ (eq:linear_funksjon)


* $a$ og $b$ konstanter som vi kaller for **koeffisientene** til den lineære funksjonen.
* $a$ er **stigningstallet** til linja.
* $b$ er **konstantleddet** til linja. Også kalt for **skjæringen med $y$-aksen**.
* $f$ er **navnet** til funksjonen.
* $y = f(x)$ er **funksjonsverdien** for en bestemt $x$-verdi.
::::

Vi tar noen eksempler på lineære funksjoner med skrivemåten over:

:::{admonition} Eksempel 1: algebraisk representasjon av lineære funksjoner
---
class: example
name: lineære-funksjoner-algebraisk-representasjon-eksempel-1
---

Under vises eksempler på lineære funksjoner. 

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = 3x - 1$ | $3$ | $-1$ |
| $g$ | $g(x) = -2x + 4$ | $-2$ | $4$ |
| $h$ | $h(x) = -x + 2$ | $-1$ | $2$ |
| $r$ | $r(x) = 3$ | $0$ | $3$ |
| $s$ | $s(x) = \dfrac{1}{2}x$ | $\dfrac{1}{2}$ | $0$ |

:::

Og så er det **din tur**!


::::{admonition} Underveisoppgave 1
---
class: check
---
Under vises noen funksjonsuttrykk og koeffisienter som parvis hører sammen. <br> Pusle sammen riktig funksjonsuttrykk med riktige koeffisienter.

:::{raw} html
---
file: ./pair_puzzles/underveisoppgaver/underveisoppgave_1.html
---
:::

::::


<!-- ::::{admonition} Underveisoppgave 1
---
class: check
name: lineære-funksjoner-algebraisk-representasjon-underveisoppgave-1
---

Fyll ut tabellen under: 

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = -3x + 2$ |  |  |
|  | $t(x) = ax + 3$ | $2$ | |
| $p$ | | $-1$ | $1$ |
|  | $q(x) = 4$ |  |  |
| $r$ |  | $-2$ | $0$ |

:::{admonition} Løsning: 
---
class: solution, dropdown
---

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = -3x + 2$ | $-3$ | $2$ |
| $t$ | $t(x) = 2x + 3$ | $2$ | $3$ |
| $p$ | $p(x) = -x + 1$ | $-1$ | $1$ |
| $q$ | $q(x) = 4$ | $0$ | $4$ |
| $r$ | $r(x) = -2x$  | $-2$ | $0$ |
:::
:::: -->

## Funksjonsverdier
Som nevnt er $f(x)$ funksjonsverdien til $f$ for en bestemt $x$-verdi. Når vi lar $x$ variere, tenker vi på $f(x)$ som *funksjonsuttrykket* til $f$. Når vi har en bestemt $x$-verdi, tenker vi på det som en *funksjonsverdi*.
Her skal vi bli bedre kjent med skrivemåten og betydningen.



:::{admonition} Funksjonsverdier
---
class: theory
---

$f(c)$ er **funksjonsverdien** til $f$ i $x = c$ og regnes ut ved å sette $x = c$ i funksjonsuttrykket til $f$.
:::

:::{admonition} Eksempel 2: funksjonsverdier
---
class: example
name: lineære-funksjoner-algebraisk-representasjon-eksempel-2
---

Under vises eksempler på utregning av funksjonsverdier. Vi bytter ut $x$-verdien i formelen og regner ut.

| Funksjon | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = 3x - 1$ | $2$ | $f(\textcolor{red}{2}) = 3\cdot \textcolor{red}{2} - 1 = 6 - 1 = 5$ |
| $g(x) = -2x + 4$ | $3$ | $g(\textcolor{red}{3}) = -2\cdot \textcolor{red}{3} + 4 = -6 + 4 = -2$ |
| $h(x) = -x + 2$ | $0$ | $h(\textcolor{red}{0}) = -\textcolor{red}{0} + 2 = 2$ |
| $r(x) = 3$ | $1$ | $r(\textcolor{red}{1}) = 3$ |
| $s(x) = \dfrac{1}{2}x$ | $4$ | $s(\textcolor{red}{4}) = \dfrac{1}{2}\cdot \textcolor{red}{4} = 2$ |

:::

Og så er det **din tur**!

::::{admonition} Underveisoppgave 2
---
class: check
---

I tabellen under vises noen funksjonsuttrykk.
| Funksjonsuttrykk |
| :--- |
| $f(x) = -3x + 2$ |
| $g(x) = 2x + 3$ |
| $h(x) = x + 8$ |
| $p(x) = -x + 1$ |
| $q(x) = 4$ |
| $r(x) = -5x$ |

<br>

Under vises noen funksjonsverdier og tall som parvis hører sammen. <br> Pusle sammen riktig funksjonsverdi med riktig tall. 

:::{raw} html
---
file: ./pair_puzzles/underveisoppgaver/underveisoppgave_2.html
---
:::
::::

<!-- ::::{admonition} Underveisoppgave 2: funksjonsverdier
---
class: check
name: lineære-funksjoner-algebraisk-representasjon-underveisoppgave-2
---

Regn ut funksjonsverdiene i tabellen under:

| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = -3x + 2$ | $1$ |  |
| $t(x) = 2x + 3$ | $0$ |  |
| $p(x) = -x + 1$ | $3$ |  |
| $q(x) = 4$ | $2$ |  |
| $r(x) = -2x$ | $5$ |  |



:::{admonition} Løsning
---
class: solution, dropdown
---
| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = -3x + 2$ | $1$ | $f(1) = -3\cdot 1 + 2 = -3 + 2 = -1$  |
| $t(x) = 2x + 3$ | $0$ | $t(0) = 2\cdot 0 + 3 = 0 + 3 = 3$  |
| $p(x) = -x + 1$ | $3$ | $p(3) = -3 + 1 = -2$  |
| $q(x) = 4$ | $2$ | $q(2) = 4$  |
| $r(x) = -2x$ | $5$ | $r(5) = -2\cdot 5 = -10$  |
:::

:::: -->

## Funksjonsverdier i Python
Vi kan bruke Python som en kalkulator for å regne ut funksjonsverdier. 


:::::{admonition} Utforsk 1: funksjonsverdier i Python
---
class: explore
name: lineære-funksjoner-algebraisk-representasjon-utforsk-1
---
Programmet under regner ut funksjonsverdien $f(2)$ for funksjonen

$$
f(x) = 3x - 1.
$$


````{tab-set}
```{tab-item} a
Les programmet og forutsi hvilken verdi programmet skriver ut. Skriv det inn under for å sjekke! 
```

```{tab-item} b
Endre på programmet slik at det i stedet regner ut $f(-1)$. <br>

Kjør programmet for å sjekke svaret ditt.

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
def f(x):
    return 3 * x - 1

y = f(-1)
print(y)
:::
::::
```

```{tab-item} c
Prøv å endre funksjonsuttrykket i `f(x)`{l=python} slik at programmet ut $f(-1)$ for 

$$
f(x) = 4x + 2.
$$ 

Kjør koden og sjekk at svaret blir riktig.

::::{admonition} Fasit
---
class: answer, dropdown
---

:::{code-block} python
---
linenos: true
emphasize-lines: 2
---
def f(x):
    return 4 * x + 2

y = f(-1)
print(y)
:::
::::
```

````

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html
---
:::

:::::

---


:::{admonition} Ordforklaring: syntaks
---
class: sidenote, margin
--- 
Ordet **syntaks** betyr "regler for å skrive kode". Tenk på det som grammatikk - men i motsetning til norsklæreren, så skjønner ikke Python hva du mener hvis du ikke skriver riktig.
:::


Nå skal vi se litt mer grundig på skrivemåten for funksjoner i Python.

::::{admonition} Syntaks: Funksjoner i Python
---
class: theory
---
En funksjon i Python har følgende syntaks:


```{code-block} python
def funksjonsnavn(x):
    return funksjonsuttrykk
```

* `def`{l=python} er et nøkkelord som forteller Python at vi skal lage en funksjon.
* `return`{l=python} er et nøkkelord som gir tilbake verdien av funksjonsuttrykket når vi bruker funksjonen. Uten dette nøkkelordet, skjer ingenting når vi bruker funksjonen. 

Vi sier forresten at det "å bruke" funksjonen er "å kalle på" funksjonen. Vi kaller dette for et "funksjonskall".
::::


Nå skal du prøve å lage et program som regner ut en funksjonsverdi i Python.


:::::{admonition} Underveisoppgave 3: funksjoner i Python
---
class: check
name: lineære-funksjoner-algebraisk-representasjon-underveisoppgave-3
---
Under vises et program i tilfeldig rekkefølge som regner ut funksjonsverdien til en funksjon $g$.


Deloppgave 1
: Pusle sammen programmet i riktig rekkefølge for å få det fullstendige programmet. <br> Hva forventer du at programmet skriver ut? Kjør programmet og sjekk svaret!


<br>

:::{raw} html
---
file: interaktiv_kode/underveisoppgaver/underveisoppgave_3.html
---
:::


:::{admonition} Fasit
---
class: dropdown, answer
---
Programmet skriver ut funksjonsverdien

$$
g(1) = -2\cdot 1 + 3 = -2 + 3 = 1.
$$
:::

<br>

Deloppgave 2
: Fiks programmet slik at det regner ut $g(-2)$. Sjekk at programmet gir riktig svar ved å regne for hånd.


:::{admonition} Løsning
---
class: solution, dropdown
---
Programmet skal gi funksjonsverdien

$$
g(\textcolor{red}{-2}) = -2\cdot (\textcolor{red}{-2}) + 3 = 4 + 3 = 7.
$$

Vi må legge inn følgende i programmet:
* Funksjonsuttrykket `-2*x + 3`{l=python} i funksjonen.
* `y = g(-2)`{l=python} så vi regner ut $g(-2)$. 

Programmet vil da se slik ut:

```{code-block} python
---
linenos:
emphasize-lines: 2, 4
---
def g(x):
    return -2 * x + 3

y = g(-2)

print(y)
```
Kjører vi programmet, får vi utskriften
```console
7
```

Så programmet funker som det skal.
:::


<br>

Deloppgave 3
: Bruk programmet til å regne ut $g(3)$. 


<br>

:::{admonition} Løsning
---
class: solution, dropdown
---
Dersom vi endrer linje 4 i programmet til `y = g(3)`{l=python}, vil programmet regne ut $g(3)$. 

```{code-block} python
---
linenos: true
emphasize-lines: 4
---
def g(x):
    return -2 * x + 3

y = g(3)
print(y)
```

Da forventer vi å få følgende verdi i utskriften:

$$
g(3) = -2\cdot 3 + 3 = -6 + 3 = -3.
$$
:::


:::::

