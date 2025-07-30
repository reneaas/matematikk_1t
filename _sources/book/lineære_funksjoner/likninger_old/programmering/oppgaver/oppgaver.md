# Oppgaver: <br> Programmering av lineære likninger


::::{admonition} Oppgave 1
---
class: problem-level-1
---
Ta quizen!

:::{raw} html
---
file: quiz/quiz_1/quiz_1.html
---
:::

::::

---

:::::{admonition} Oppgave 2
---
class: problem-level-1
---

````{tab-set} 
---
class: tabs-parts
---
```{tab-item} a
Les programmet og forutsi hva det printer ut. 

Skriv inn hypotesen din og sjekk svaret ditt!
```

```{tab-item} b
Juster programmet og bruk det til å finne nullpunktet til

$$
g(x) = x + 5
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos: true
emphasize-lines: 2
---
def g(x):
    return x + 5

for x in range(-10, 11):
    if g(x) == 0:
        print(x)

:::
::::
```

```{tab-item} c
Juster programmet og bruk det til å finne løsningen av likningen

$$
g(x) = 2
$$

:::{admonition} Hint
---
class: dropdown, hints
---
Siden man bruker `f(x) == 0`{l=python} for å sjekke om `f(x)`{l=python} er lik $0$, kan du kanskje tenke deg til hva du må endre på for å sjekke om $g(x) = 2$? 
::: 

::::{admonition} Fasit
---
class: answer, dropdown
---

**Programkode**:
:::{code-block} python
---
linenos: true
emphasize-lines: 5
---
def g(x):
    return x + 5

for x in range(-10, 11):
    if g(x) == 2:           # <-- er g(x) lik 2?
        print(x)
:::

**Utskrift**:
:::{code-block} console
-3
:::

**Tolkning**: <br>
Løsningen av likningen $g(x) = 2$ er $x = -3$.
::::
```

```{tab-item} d
Juster programmet og bruke det til å finne skjæringspunktet mellom grafen til $g$ og linja $y = -1$.


::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**: 

:::{code-block} python
---
linenos: true
emphasize-lines: 5, 6
---
def g(x):
    return x + 5

for x in range(-10, 11):
    if g(x) == -1:          # <-- sjekker om g(x) er -1
        print(x, g(x))      # <-- skriver ut x og g(x)
:::

**Utskrift**:
:::{code-block} console
-6 -1
:::

**Tolkning**: <br>
Grafen til $g$ skjærer linja $y = -1$ i punktet $(-6, -1)$.
::::
```
````

:::{raw} html
---
file: ./interaktiv_kode/oppgave_2.html
---
:::
:::::

---


:::::{admonition} Oppgave 3
---
class: problem-level-2
---
Under vises to programkoder som bruker funksjonene

$$
f(x) = 2x + 3 \quad \text{og} \quad g(x) = -3x + 8
$$




`````{tab-set}
---
class: tabs-parts 
---
````{tab-item} a
Les de to programmene nøye og forutsi hva de kommer til å skrive ut.

Skriv inn forutsigelsene dine under og sjekk! 
````

````{tab-item} b
1. Hvilke problemer kan du løse ved å bruke program 1? 
2. Hvilke problemer kan du løse ved å bruke program 2?
3. Kan du svare på de samme spørsmålene med både program 1 og program 2?
````

`````

`````{tab-set}
````{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/oppgave_3/program_1.html
---
:::

````

````{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/oppgave_3/program_2.html
---
:::
````

`````
:::::
