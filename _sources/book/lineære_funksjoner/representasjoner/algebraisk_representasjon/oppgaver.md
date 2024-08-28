# Oppgaver

:::::{admonition} Oppgave 1
---
class: problem-level-1
name: lineære-funksjoner-algebraisk-representasjon-oppgave-1
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
name: lineære-funksjoner-algebraisk-representasjon-oppgave-2
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
name: lineære-funksjoner-algebraisk-representasjon-oppgave-3
---

Under vises et program i tilfeldig rekkefølge som regner ut funksjonsverdien til en lineær funksjon $f$.

Deloppgave 1
: Pusle sammen programmet i riktig rekkefølge for å få det fullstendige programmet. <br> Hva forventer du at programmet skriver ut? Kjør programmet og sjekk svaret!



<br>

:::{raw} html
---
file: interaktiv_kode/oppgaver/oppgave_3.html
---
:::

<br>

Deloppgave 2
: Hva er funksjonsuttrykket til $f$ i programmet? <br> Hvilken funksjonsverdi er det programmet regner ut?
::::{admonition} Fasit
---
class: answer, dropdown
---
* Funksjon: $f(x)= -\dfrac{1}{2}x + 3$
* Funksjonsverdi: $y = f(-4)$
::::

<br>

Deloppgave 3
: Endre programmet slik at det regner ut $f(2)$. <br> Hva forventer du at svaret blir? Kjør programmmet og sjekk.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(2) = 2
$$
::::


<br>

Deloppgave 4
: Endre programmet slik at det regner ut $g(2)$ når $g(x) = 2x + 1$. <br> Kjør programmet og sjekk at svaret blir riktig.


::::{admonition} Fasit
---
class: answer, dropdown
---
Vi kan bare overskrive definisjonen av `f(x)`{l=python}. <br> Endret program:
```{code-block} python
---
linenos:
emphasize-lines: 2
---
def f(x):
    return 2*x + 1

y = f(2)
print(y)
```

Funksjonsverdi:

$$
g(2) = 5
$$
::::
:::::


