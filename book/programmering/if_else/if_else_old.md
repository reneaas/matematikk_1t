# `if`{l=python}-`else`{l=python}-setninger

:::{admonition} Læringsmål: `if`{l=python}-`else`{l=python}-setninger
---
class: tip
--- 
Etter å ha lest dette delkapittelet, er målet at du skal kunne:
* Forklare hva en **betingelse** er, og sette opp betingelser i Python.
* Forstå hva en **boolsk** variabel er, og kunne sette opp en sannhetstabell for ulike betingelser.
* Kunne bruke `if`{l=python}-`else`{l=python}-setninger i Python.
:::

I mange tilfeller ønsker vi å skrive et program som skal gjøre forskjellige ting avhengig av ulike såkalte **betingelser**. Hvis noe er sant, så ønsker vi kanskje at programmet skal gjøre en ting, mens hvis det ikke er sant så ønsker vi at programmet skal gjøre noe annet. Det er dette `if`{l=python}-`else`{l=python}-setninger er til for.


## Betingelser
For å forstå hvordan en `if`{l=python}-`else`{l=python}-setning fungerer, må vi først snakke om betingelser.

````{admonition} Definisjon: betingelse
---
class: theory
---
En **betingelse** er en påstand som kan være sann eller usann. I Python er en betingelse en boolsk variabel (`bool`{l=python}), som kan ha verdiene `True` eller `False`. 

````


For å uttrykke betingelser, må vi bruke **sammenligningsoperatorer**. Disse sammenlikner to ting og gir tilbake `True`{l=python} eller `False`{l=python} avhengig av om betingelsen er sann eller usann. 



````{admonition} Sammenlikningsoperatorer
---
class: theory
---

Vi har følgende boolske operatorer i Python:

| Operator | Eksempel | Forklaring |
|:--------:|:-----------:|:---------|
| `==`{l=python} | `a == b`{l=python} | Er `a`{l=python} lik `b`{l=python}? |
| `!=`{l=python} | `a != b`{l=python} | Er `a`{l=python} ulik `b`{l=python}? |
| `>`{l=python} | `a > b`{l=python} | Er `a`{l=python} større enn `b`{l=python}? |
| `<`{l=python} | `a < b`{l=python} | Er `a`{l=python} mindre enn `b`{l=python}? |
| `>=`{l=python} | `a >= b`{l=python} | Er `a`{l=python} større enn eller lik `b`{l=python}? |
| `<=`{l=python} | `a <= b`{l=python} | Er `a`{l=python} mindre enn eller lik `b`{l=python}? |
````

Nå er vi klare for et eksempel.


````{admonition} Eksempel 1: betingelser
---
class: example
---

Vi lar `a = 2`{l=python} og `b = -1`{l=python} være to variabler. Da kan vi sette opp følgende betingelser med deres sannhetsverdi:

| Betingelse | Verdi |
|:------------:|:-------:|
| `a > 0`{l=python} | `True`{l=python} |
| `b > 0`{l=python} | `False`{l=python} |
| `a == 2`{l=python} | `True`{l=python} |
| `a != b`{l=python} | `True`{l=python} |
| `a <= b`{l=python} | `False`{l=python} |
| `a >= b`{l=python} | `True`{l=python} |

````

Så er det **din tur**!

````{admonition} Underveisoppgave 1
---
class: check
---

Vi lar `r = 3`{l=python} og `s = 5`{l=python} være to variabler.
Fyll ut tabellen under med `True`{l=python} eller `False`{l=python} avhengig av om betingelsen er sann eller usann.

| Betingelse | Verdi |
|:------------:|:-------:|
| `r > 0`{l=python} |  |
| `s > 0`{l=python} |  |
| `r == 2`{l=python} |  |
| `r != s`{l=python} |  |
| `r <= s`{l=python} |  |
| `r >= s`{l=python} |  |
| `r == s - 2`{l=python} |  |


```{admonition} Løsning
---
class: solution, dropdown
---

| Betingelse | Verdi |
|:------------:|:-------:|
| `r > 0`{l=python} | `True`{l=python} |
| `s > 0`{l=python} | `True`{l=python} |
| `r == 2`{l=python} | `False`{l=python} |
| `r != s`{l=python} | `True`{l=python} |
| `r <= s`{l=python} | `True`{l=python} |
| `r >= s`{l=python} | `False`{l=python} |
| `r == s - 2`{l=python} | `True`{l=python} |

```
````




## `if`{l=python}-`else`{l=python} i praksis

Når vi har en betingelse, kan vi bruke en `if`{l=python}-`else`{l=python}-setning for å bestemme hva programmet skal gjøre avhengig av om betingelsen er sann eller usann. 

```{admonition} Ordforklaring: syntaks
---
class: sidenote, margin
--- 
Ordet **syntaks** betyr "regler for å skrive kode".
```


::::{admonition} Syntaks: `if`{l=python}-`else`{l=python}-setninger
---
class: theory
---

Syntaksen for en `if`{l=python}-`else`{l=python}-setning i Python er som følger:

```{code-block}
if betingelse:
    # Hvis betingelsen er sann, utfør handling 1
    # Dette er if-blokken
else:
    # Hvis ikke, utfør handling 2.
    # Dette er else-blokken
```

Vi kaller koden under `if`{l=python} for **`if`{l=python}-blokken**, og koden under `else`{l=python} for **`else`{l=python}-blokken**. Under vises et flytdiagram for en `if`{l=python}-`else`{l=python}-setning:

```{include} figurer/if_else_flytdiagram.md
```

::::


Vi går løs på et eksempel

:::::{admonition} Eksempel 2: `if`{l=python}-`else`{l=python}-setninger
---
class: example
---
Vi tar utgangspunkt i følgende kode:

```{code-block} python
---
linenos: 
emphasize-lines: 4
---

x = 5

if x > 0:
    print("x er større enn 0")
else:
    print("x er ikke større enn 0")
```

Siden `x = 5`{l=python}, vil betingelsen `x > 0`{l=python} være `True`{l=python}. Dermed vil programmet skrive kjøre linje 4 og ikke linje 6. Utskriften blir dermed:

```console
x er større enn 0
```
:::::


**Din tur!**

:::::{admonition} Underveisoppgave 2
---
class: check
---

Under vises et program. Hva blir utskriften?

```{code-block} python
---
linenos:
---

y = 1

if 2*y != 2:
    x = 4
else:
    x = 2

print(f"{x = }")
```

::::{admonition} Løsning
---
class: solution, dropdown
--- 

Siden `y = 1`{l=python}, vil `2*y`{l=python} være `2`{l=python}. Dermed vil betingelsen `2*y != 2`{l=python} være `False`{l=python}, og programmet vil gå til `else`{l=python}-blokken. Dermed vil `x = 2`{l=python}, og programmet vil skrive ut:

```console
x = 2
```
::::
:::::

**En til!**

::::{admonition} Underveisoppgave 3
---
class: check
---

Under vises et uferdig program. Sett inn en passende betingelse på linje 4 slik at programmet skriver ut verdien til `y`{l=python}.


```{code-block} python
---
linenos:
---
x = 2
y = 2*x + 3

if betingelse: # FIKSMEG!
    print(f"{y = }")
```

:::{admonition} Løsning
---
class: solution, dropdown
---
Først kan vi jo regne oss fram til hva verdien til `y`{l=python} er ved å bruke formelen på linje 2, og verdien til `x`{l=python} fra linje 1. Da har vi

$$
y = 2\cdot 2 + 3 = 7.
$$

En mulig betingelse vi kan sette opp slik at verdien til `y`{l=python} skrives ut er derfor `y == 7`{l=python}. Programmet blir da:

```{code-block} python
---
linenos:
emphasize-lines: 4
---
x = 2
y = 2*x + 3

if y == 7:
    print(f"{y = }")
```

:::
::::


## `if`{l=python}-`elif`{l=python}-`else`{l=python}-setninger

Noen ganger har vi flere *grener* enn to. Da kan vi legge inn en `elif`{l=python}-blokk. 


::::{admonition} Syntaks: `if`{l=python}-`elif`{l=python}-`else`{l=python}-setninger
---
class: theory
---

En `if`{l=python}-`elif`{l=python}-`else`{l=python}-setning i Python har følgende syntaks:

```{code-block} python

if betingelse1:
    # Hvis betingelse1 er sann, utfør handling 1
    # Dette er if-blokken
elif betingelse2:
    # Hvis betingelse2 er sann, utfør handling 2
    # Dette er elif-blokken
else:
    # Hvis ingen av betingelse1 eller betingelse2 er sanne, utfør handling 3
    # Dette er else-blokken
```

Under vises et flytdiagram for en `if`{l=python}-`elif`{l=python}-`else`{l=python}-setning:

```{include} figurer/if_elif_else_flytdiagram.md
```

::::

Vi tar et konkret eksempel.


::::{admonition} `input`{l=python}-funksjonen
---
class: note, margin
---

`input`{l=python}-funksjonen lar oss kjøre et program og skrive inn en ny verdi hver gang vi kjører programmet. På den måten kan vi prøve ut programmet med forskjellige verdier uten å endre på selve programmet.

::::

::::{admonition} Eksempel 3: `if`{l=python}-`elif`{l=python}-`else`{l=python}-setninger
---
class: example
name: if_else_setninger-eksempel-3
--- 

Merverdiavgiften (forkortelse: mva) på varer i Norge er avhengig av hvilken type vare det er. 

| Type vare | Merverdiavgift |
|:-----------:|:----------------:|
| Mat og drikke | 15 % |
| Reise | 12 % |
| Andre tjenester | 25 % |

<br>

Vi tenker oss at vi vil skrive et program som avhengig av varen gir oss riktig merverdiavgift i prosent. Da kan vi skrive slik:

```{code-block} python
---
linenos:
--- 
vare = input("Skriv inn varetype. Enten `mat`, `reise` eller `annet`: ")

if vare == "mat":
    merverdiavgift = 15
elif vare == "reise":
    merverdiavgift = 12
else:
    merverdiavgift = 25

print(f"{merverdiavgift = }%")
```

Vi kan forstå programmet ved hjelp av flytdiagrammet under:

```{include} figurer/if_elif_else_flytdiagram_eksempel_3.md
```

<br>

Hvis vi kjører programmet og skriver inn "reise", så vil vi få utskriften

```console
merverdiavgift = 12%
```
:::: 

**Din tur!**


::::{admonition} Underveisoppgave 4
---
class: check
---
Utvid programmet fra {ref}`eksempel 3 <if_else_setninger-eksempel-3>` slik at programmet:

* Tar inn prisen på en vare *før* merverdiavgift er lagt til.
* Regner ut prisen på varen *etter* merverdiavgift er lagt til.
* Skriver ut prisen på varen i stedet for merverdiavgiften. 


:::{admonition} Hint: nyttig formel
---
class: hints, dropdown
name: if_else_setninger-underveisoppgave-4-hint-1
---
Hvis $p_\text{før}$ er prisen på en vare før merverdiavgiften er lagt til, og $m$ er merverdiavgiften i prosent, så er prisen på varen etter merverdiavgiften er lagt til gitt ved:

$$
p_\text{etter} = p_\text{før}\cdot \left(1 + \dfrac{m}{100}\right)
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
Vi legger til de tre linjene som mangler i programmet fra {ref}`eksempel 3 <if_else_setninger-eksempel-3>`:

* På linje 2 har vi lagt at brukeren kan oppgi prisen på varen før merverdiavgift og lagrer verdien i `pris_før`{l=python}.
* På linje 11 regner vi ut prisen på verdien etter merverdiavgift ved å bruke formelen i fra {ref}`hintet <if_else_setninger-underveisoppgave-4-hint-1>`. Vi lagrer resultatet i `pris_etter`{l=python}. 
* På linje 13 har vi byttet ut `print`{l=python}-utsagnet slik at det skriver ut verdien til `pris_etter`{l=python} i stedet for `merverdiavgift`{l=python}. 
```{code-block} python
---
linenos:
emphasize-lines: 2, 11, 13
---
vare = input("Skriv inn varetype. Enten `mat`, `reise` eller `annet`: ")
pris_før = float(input("Skriv inn pris før merverdiavgift: "))

if vare == "mat":
    merverdiavgift = 15
elif vare == "reise":
    merverdiavgift = 12
else:
    merverdiavgift = 25

pris_etter = pris_før*(1 + merverdiavgift/100)

print(f"{pris_etter = } kr.")
```

Kjører vi programmet med `reise`{l=python} som varetype og `100`{l=python} som pris før merverdiavgift, vil vi få utskriften

```console
pris_etter = 112.0 kr.
```
::::


## Oppgaver

::::{admonition} Oppgave 1
---
class: problem-level-1
---

Under vises et program. Hva blir utskriften? 

```{code-block} python 
---
linenos:
---
x = 2.5

if x < 0:
    y = 1
elif x < 3:
    y = 2
else:
    y = 3

print(f"{y = }")
```
:::{admonition} Løsning
---
class: solution, dropdown
---
Siden $2.5 < 3$ er en sann påstand, vil `elif`{l=python}-blokken kjøres som betyr at `y = 2`{l=python}. Programmet vil dermed skrive ut

```console
y = 2
```

:::
::::

::::{admonition} Oppgave 2
---
class: problem-level-1
---
Under vises et uferdig program som skal sjekke om et trekant med sidelengder $a$, $b$ og $c$ er rettvinklet eller ikke. 

* Dersom trekanten er rettvinklet, skal programmet skrive ut "Trekanten er rettvinklet".
* Hvis trekanten ikke er rettvinklet, skal programmet skrive ut "Trekanten er ikke rettvinklet".

```{code-block} python
---
linenos:
---
a = float(input("Skriv inn sidelengde a: "))
b = float(input("Skriv inn sidelengde b: "))
c = float(input("Skriv inn sidelengde c: "))

# TODO: bytt ut betingelse1 og betingelse2
if a**2 + b**2 == c**2: 
    print("Trekanten er rettvinklet")
elif betingelse1: # FIKSMEG
    print("Trekanten er rettvinklet")
elif betingelse2: # FIKSMEG
    print("Trekanten er rettvinklet")
else:
    print("Trekanten er ikke rettvinklet")
```



:::{admonition} Hint 1: Hvordan kan du sjekke at en trekant er rettvinklet?
---
class: hints, dropdown
---

La $k_1$ og $k_2$ være kateter i en rettvinklet trekant, og $h$ være hypotenusen. Da vet vi at Pytagoras' setning sier at

$$
h^2 = k_1^2 + k_2^2 \,.
$$
:::

:::{admonition} Hint 2
---
class: hints, dropdown
---
Husk at du ikke vet hvilke sidelengder som er kateter og hvilken som er hypotenus. Du må derfor sjekke alle mulige kombinasjoner med Pytagoras' setning.
::: 

::::