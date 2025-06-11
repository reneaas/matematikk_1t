# Algebraisk representasjon


:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en lineær funksjon algebraisk, og kunne lese av stigningstall og konstantledd.
* Kunne regne ut funksjonsverdier med funksjonsuttrykket til en lineær funksjon.
* Kunne bruke Python til å regne ut funksjonsverdier til en lineær funksjon.
:::
---

En **representasjon** er en måte å uttrykke noe på. Når vi jobber med rette linjer, er de to vanligste måtene å representere linjer på, algebraisk og grafisk. Med algebraisk representasjon mener vi en formel som beskriver linja. Med grafisk representasjon mener vi en tegning av linja i et koordinatsystem.

---


## Algebraisk representasjon av lineære funksjoner
En lineær funksjon er en rett linje der $y$-verdien er bestemt av $x$-verdien. 

::::{admonition} Definisjon: lineær funksjon
---
class: theory
---
En lineær funksjon $f$ er en funksjon på formen

:::{figure} ./figurer/teori/algebraisk_uttrykk.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::



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



## Funksjonsverdier i Python
Vi kan bruke Python som en kalkulator for å regne ut funksjonsverdier. 


:::::{admonition} Utforsk 1: funksjonsverdier i Python
---
class: explore
---
Programmet under regner ut funksjonsverdien $f(2)$ for funksjonen

$$
f(x) = 3x - 1.
$$


````{tab-set}
---
class: tabs-parts
---
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


:::::::::::::::{underveisoppgave} Underveisoppgave 3

Nedenfor vises et program i tilfeldig rekkefølge.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Pusle sammen programmet i riktig rekkefølge for å få det fullstendige programmet. 

Hva forventer du at programmet skriver ut? Kjør programmet og sjekk svaret!

::::{solution}
Programmet skriver ut 

$$
f(2) = 2\cdot 2 - 3 = 1.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Endre programmet slik at det regner ut $f(-1)$. 

Sjekk at programmet gir riktig svar ved å regne for hånd.

::::{solution}
:::{code-block} python
---
linenos:
emphasize-lines: 5
---
def f(x):
    return 2 * x - 3


y = f(-1)
print(y)
:::

som gir utskriften

:::{code-block}
-5
:::


::::

:::::::::::::


::::::::::::::


:::{parsons-puzzle}
def f(x):
    return 2 * x - 3


y = f(2)
print(y)

:::





:::::::::::::::

