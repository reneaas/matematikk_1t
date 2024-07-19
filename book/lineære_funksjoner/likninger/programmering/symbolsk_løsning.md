# Symbolsk programmering (CAS)

:::{admonition} Læringsmål: symbolsk programmering
---
class: tip
--- 
Etter å ha gått gjennom denne delen, er målet at du skal kunne:
* Løse lineære likninger symbolsk med programmering i Python.
:::


## Symbolsk programmering av likninger

Vi starter med et eksempel. 

::::{admonition} Eksempel 1
---
class: example
name: lineære-likninger-symbolsk-eksempel-1
---
Vi ønsker å løse den lineære likningen

$$
3x + 4 = 2x - 1.
$$

Vi kan løse denne likningen symbolsk ved å bruke Python ved hjelp av biblioteket `sympy`{l=python}. Følgende kode løser likningen:

```{code-block} python
---
linenos:
---
from sympy import *                     # Henter alle innebygde sympy-funksjoner
from sympy.abc import x                 # Henter ut et symbol for `x`

venstre_side = 3*x + 4                  # Definerer venstre side
høyre_side = 2*x - 1                    # Definerer høyre side
likning = Eq(venstre_side, høyre_side)  # Lager en symbolsk likning
løsning = solve(likning)                # Løser likningen symbolsk

print(løsning)                          # Skriver ut løsningen
```
som gir utskriften
```console
[-5]
```
som betyr at løsningsmengden er $x \in \{-5\}$. 
::::

Så er det **din tur**!

::::{admonition} Underveisoppgave 1
---
class: check
---
Kopier koden fra {ref}`eksempel 1 <lineære-likninger-symbolsk-eksempel-1>` og juster den slik at den løser likningen

$$
4x - 2 = x + 5.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---

```{code-block} python
from sympy import *
from sympy.abc import x

venstre_side = 4*x - 4
høyre_side = x + 5
likning = Eq(venstre_side, høyre_side)
løsning = solve(likning)

print(løsning)
```
som gir utskriften
```console
[3]
```
som betyr at løsningen av likningen er $x = 3$. 
:::
::::