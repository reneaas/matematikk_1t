# Algebraisk representasjon av lineære funksjoner


:::{admonition} Læringsmål: representasjoner av lineære funksjoner
---
class: tip
---
Målet med denne seksjonen er at du skal kunne:
* Ha en grunnleggende forståelse av funksjonsbegrepet.
* Kjenne til den algebraiske representasjonen av lineære funksjoner.
* Kunne regne ut funksjonsverdier for en lineær funksjon.
* Kunne bruke Python til å regne ut funksjonsverdier for en lineær funksjon.
:::
---

En representasjon er en måte å uttrykke noe på. Når vi jobber med rette linjer, er de to vanligste måtene å representere linjer på, algebraisk og grafisk. Med algebraisk representasjon, mener vi en formel som beskriver linja. Med grafisk representasjon, mener vi en tegning av linja i et koordinatsystem.

---

## Algebraisk representasjon av lineære funksjoner
En lineær funksjon er en spesiell rett linje der $y$-verdien er bestemt av $x$-verdien. Vi skal komme mer presist tilbake til funksjonsbegrepet senere, men først tar vi en litt kortfattet og enkelt definisjon av en lineær funksjon:

::::{admonition} Begrep: *Koeffisienter*
---
class: sidenote, margin
---
Konstantene $a$ og $b$ kalles for **koeffisientene** til den lineære funksjonen.
::::


::::{admonition} Definisjon: lineær funksjon
---
class: theory
---
En **lineær funksjon** $f$ er en formel som kan skrives som en likning på formen 

$$
f(x) = ax + b.
$$ (eq:linear_funksjon)


* $a$ er **stigningstallet** til linja.
* $b$ er **konstantleddet** til linja. Også kalt for **skjæringen med $y$-aksen**.
* $f$ er **navnet** til funksjonen.
* $y = f(x)$ er **funksjonsverdien** til en gitt $x$-verdi.
::::

Vi tar noen eksempler på lineære funksjoner med skrivemåten over:

:::{admonition} Eksempel 1: algebraisk representasjon av lineære funksjoner
:class: example

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

::::{admonition} Underveisoppgave 1: algebraisk representasjon av lineære funksjoner
---
class: check
---

Fyll ut tabellen under: 

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = -3x + 2$ |  |  |
|  | $t(x) = ax + 3$ | $2$ | |
| $p$ | | $-1$ | $1$ |
| $q$ | $q(x) = 4$ |  |  |
| $r$ |  | $-2$ | $0$ |

:::{admonition} Løsning
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
::::

## Funksjonsverdier
Vi har sagt at $f(x)$ er funksjonsverdien til $f$ for en bestemt $x$-verdi. Her skal vi bli bedre kjent med skrivemåten og betydningen.

:::{admonition} Funksjonsverdier
---
class: theory
---

$f(a)$ er **funksjonsverdien** til $f$ i $x = a$ og regnes ut ved å sette $x = a$ i funksjonsuttrykket til $f$.
:::

:::{admonition} Eksempel 2: funksjonsverdier
---
class: example
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


::::{admonition} Underveisoppgave 2: funksjonsverdier
---
class: check
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

::::

## Funksjonsverdier i Python
Vi kan bruke Python som en kalkulator for å regne ut funksjonsverdier. 

::::{admonition} Eksempel 3: funksjonsverdier i Python
---
class: example
name: algebraisk-representasjon-example-3
---

La oss regne ut funksjonsverdien til 

$$
f(x) = 3x - 1,
$$

i $x = 2$. Da kan vi skrive følgende kode i Python:


```{code-block} python
---
linenos:
---
x = 2
y = 3*x - 1

print(y)

```

som gir utskriften

```console
5
```

Med andre ord er $f(2) = 5$.

::::

Og så er det **din tur**!

::::{admonition} Underveisoppgave 3: funksjonsverdier i Python
---
class: check
---
Under vises et interaktivt vindu med koden fra {ref}`eksempel 3 <algebraisk-representasjon-example-3>`. 

Deloppgave 1
: Endre koden til å bestemme $f(-1)$.

<br>

Deloppgave 2
: Endre koden til å bestemme $g(-1)$ for $g(x) = 4x + 2$. Hva blir verdien? 💻

<br>

:::{raw} html
---
file: interaktiv_kode/underveisoppgave_3.html
---
:::

:::{admonition} Løsning: deloppgave 1
---
class: solution, dropdown
---

```{code-block} python
---
linenos: true
emphasize-lines: 1
---
x = -1
y = 3*x - 1

print(y)
```
som gir utskriften
```console
-4
```
Altså er $f(-1) = -4$. 
:::

:::{admonition} Løsning: deloppgave 2
---
class: solution, dropdown
---

```{code-block} python
---
linenos: true
emphasize-lines: 2
---
x = -1
y = 4*x + 2

print(y)
```
som gir utskriften
```console
-2
```
Altså er $g(-1) = -2$. 
:::
::::

---

I {ref}`eksempel 3 <algebraisk-representasjon-example-3>` brukte vi ikke notasjonen for funksjoner. Men i Python har vi faktisk støtte for akkurat dette. 


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
def funksjonsnavn(x):
    return funksjonsuttrykk
```
::::

::::{admonition} Eksempel 4: funksjoner i Python
---
class: example
name: algebraisk-representasjon-example-4
---

La oss skrive om {ref}`eksempel 3 <algebraisk-representasjon-example-3>` ved å bruke funksjonsnotasjon i Python. Vi husker på at vi har funksjonen $f(x) = 3x - 1$ og at vi skal regne ut $f(2)$. 
Følgende Pythonkode oppnår dette:

```{code-block} python
---
linenos:
---
# Definerer funksjonen f(x) = 3x - 1
def f(x):
    return 3*x - 1

y = f(2)    # Regner ut f(2)
print(y) # skriver ut resultatet
```
som gir utskriften

```console
5
```
som betyr at $f(2) = 5$.
::::


Og så er det **din tur**!

:::::{admonition} Underveisoppgave 4: funksjoner i Python
---
class: check
---

Lag et program som bruker en funksjon for $g(x) = 2x + 3$ og regn ut $g(-2)$ med programmet.

:::{raw} html
---
file: interaktiv_kode/underveisoppgave_4.html
---
:::

Deloppgave 1
: Endre programmet slk at det regner ut $f(-4)$. 


<br>

Deloppgave 2
: Endre programmet slik at det regner ut $g(-2)$ når $g(x) = 2x + 3$.



:::{admonition} Løsning
---
class: solution, dropdown
---

```{code-block} python
---
linenos:
---
def g(x):
    return 2*x + 3

y = g(-2)
print(y)
```
som gir utskriften
```console
-1
```
Altså er $g(-2) = -1$.
:::
:::::

## Oppgaver

:::::{admonition} Oppgave 1
---
class: problem-level-1
---
Fyll ut tabellen under.

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = 2x - 3$ |  |  |
| $g$ | $g(x) = -3x + 4$ |  |  |
| $h$ | $h(x) = 4x + 1$ |  |  |
| $r$ | $r(x) = 3$ |  |  |
| $s$ | $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ |  |  |

::::{admonition} Fasit
---
class: answer, dropdown
---

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = 2x - 3$ | $2$ | $-3$ |
| $g$ | $g(x) = -3x + 4$ | $-3$ | $4$ |
| $h$ | $h(x) = 4x + 1$ | $4$ | $1$ |
| $r$ | $r(x) = 3$ | $0$ | $3$ |
| $s$ | $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ | $-\dfrac{1}{3}$ | $\dfrac{3}{2}$ |

::::

:::::


:::::{admonition} Oppgave 2
---
class: problem-level-1
---

Regn ut funksjonsverdiene i tabellen under.

| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = 2x - 3$ | $1$ |  |
| $g(x) = -3x + 4$ | $2$ |  |
| $h(x) = 4x + 1$ | $0$ |  |
| $r(x) = 3$ | $-1$ |  |
| $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ | $3$ |  |

::::{admonition} Fasit
---
class: answer, dropdown
---

| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = 2x - 3$ | $1$ | $-1$ |    
| $g(x) = -3x + 4$ | $2$ | $-2$ |
| $h(x) = 4x + 1$ | $0$ | $1$ |
| $r(x) = 3$ | $-1$ | $3$ |
| $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ | $3$ | $\dfrac{5}{2}$ |
::::

:::::


:::::{admonition} Oppgave 3
---
class: problem-level-1
---

En elev har skrevet et program for å regne ut en funksjonsverdi.

```{code-block} python
---
linenos:
---
def f(x):
    return -x/2 + 3

print(f(2))
```

<br>

Deloppgave 1
: Hvilken funksjon er det elevens program regner ut funksjonsverdien til?

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -\dfrac{x}{2} + 3 = -\dfrac{1}{2}x + 3
$$
::::

<br>

Deloppgave 2
: Hva blir verdien programmet skriver ut? 📝 $\color{red}\xcancel{💻}$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(2) = 2
$$
::::


<br>

Deloppgave 3
: Under vises programmet i et interaktivt vindu. Endre programmet slik at det regner ut $f(-2)$ og bruk programmet til å bestemme verdien. 💻


:::{raw} html
---
file: interaktiv_kode/oppgave_3.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
Endret program:
```{code-block} python
---
linenos:
emphasize-lines: 4
---
def f(x):
    return -x/2 + 3

y = f(-2)
print(y)
```

Funksjonsverdi:

$$
f(-2) = 4
$$
::::
:::::