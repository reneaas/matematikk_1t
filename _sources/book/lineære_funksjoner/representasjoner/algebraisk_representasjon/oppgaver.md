# Oppgaver: <br> Algebraisk representasjon av lineære funksjoner

:::::{problem} Oppgave 1
---
level: 1
---
Fyll ut tabellen under.

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = 2x - 3$ |  |  |
| $g$ | $g(x) = -3x + 4$ |  |  |
| $h$ | $h(x) = 4x + 1$ |  |  |
| $r$ | $r(x) = 3$ |  |  |
| $s$ | $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ |  |  |

::::{answer}

| Funksjonsnavn | Funksjonsuttrykk | Stigningstall | Konstantledd |
| :---: | :---: | :---: | :---: |
| $f$ | $f(x) = 2x - 3$ | $2$ | $-3$ |
| $g$ | $g(x) = -3x + 4$ | $-3$ | $4$ |
| $h$ | $h(x) = 4x + 1$ | $4$ | $1$ |
| $r$ | $r(x) = 3$ | $0$ | $3$ |
| $s$ | $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ | $-\dfrac{1}{3}$ | $\dfrac{3}{2}$ |

::::

:::::


---

:::::{problem} Oppgave 2
---
level: 1
---

Regn ut funksjonsverdiene i tabellen under.

| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = 2x - 3$ | $1$ |  |
| $g(x) = -3x + 4$ | $2$ |  |
| $h(x) = 4x + 1$ | $0$ |  |
| $r(x) = 3$ | $-1$ |  |
| $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ | $3$ |  |

::::{answer}

| Funksjonsuttrykk | $\quad x \quad$ | Funksjonsverdi $f(x)$ |
| :--- | :---: | :--- |
| $f(x) = 2x - 3$ | $1$ | $-1$ |    
| $g(x) = -3x + 4$ | $2$ | $-2$ |
| $h(x) = 4x + 1$ | $0$ | $1$ |
| $r(x) = 3$ | $-1$ | $3$ |
| $s(x) = -\dfrac{1}{3}x + \dfrac{3}{2}$ | $3$ | $\dfrac{1}{2}$ |

::::

:::::

---

:::::{problem} Oppgave 3
---
level: 1
---

Under vises et program i tilfeldig rekkefølge som regner ut funksjonsverdien til en lineær funksjon $f$.

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} a
Pusle sammen programmet i riktig rekkefølge for å få det fullstendige programmet. <br> Hva forventer du at programmet skriver ut? Kjør programmet og sjekk svaret!
````

````{tab-item} b
Hva er funksjonsuttrykket til $f$ i programmet? <br> Hvilken funksjonsverdi er det programmet regner ut?

::::{answer}
* Funksjon: $f(x)= -\dfrac{1}{2}x + 3$
* Funksjonsverdi: $y = f(-4)$
::::
````

````{tab-item} c
Endre programmet slik at det regner ut $f(2)$. <br> Hva forventer du at svaret blir? Kjør programmmet og sjekk.

::::{answer}
$$
f(2) = 2
$$
::::
````

````{tab-item} d
Endre programmet slik at det regner ut $f(2)$ når $f(x) = 2x + 1$. <br> Kjør programmet og sjekk at svaret blir riktig.


::::{answer}
Vi kan bare overskrive definisjonen av `f(x)`{l=python}. <br> Endret program:
```{code-block} python
---
linenos:
emphasize-lines: 2
---
def f(x):
    return 2 * x + 1

y = f(2)
print(y)
```

Funksjonsverdi:

$$
f(2) = 5
$$
::::
````
`````

<br>

:::{parsons-puzzle}
def f(x):
    return -x/2 + 3

y = f(-4)
print(y)

:::


:::::

