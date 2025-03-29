# Python


:::::::::::::::{admonition} Oversikt over Pythonkode
---
class: summary, dropdown
---
::::::::::::::{tab-set}

:::::::::::::{tab-item} Variabler og `print`{l=python}

:::{code-block} python
---
linenos:
---
a = 2
b = 3.0
melding = "hei"

print(a)
print(f"{b = }")
print(f"{melding = }")
:::

Utskrift:

:::{code-block} console
2
b = 3.0
melding = 'hei'
:::


:::::::::::::


:::::::::::::{tab-item} `for`{l=python}-løkker

**Grunnleggende `for`{l=python}-løkke**
```{code-block} python
---
linenos:
---
for i in range(5):
    print(i)
```

<br>

**En `for`{l=python}-løkke med summering**:

Regner ut summen $s = 1 + 2 + 3 + 4 + 5$:

```{code-block} python
---
linenos:
---
s = 0
for i in range(1, 6):
    s = s + i

print(s)
```

:::::::::::::


:::::::::::::{tab-item} `while`{l=python}-løkker

**Grunnleggende `while`{l=python}-løkke**:

:::{code-block} python
---
linenos:
---
i = 0
while i < 5:
    print(i)
    i = i + 1
:::

**`while`{l=python}-løkke med summering**:

Regner ut summen $s = 1 + 2 + 3 + 4 + 5$:

:::{code-block} python
---
linenos:
---
s = 0
i = 1
while i <= 5:
    s = s + i
    i = i + 1

print(s)
:::

:::::::::::::

:::::::::::::{tab-item} Funksjoner

:::{code-block} python
---
linenos:
---
def f(x):
    return x**2 - x - 6

x = 1
y = f(x)

print(y)
:::

Utskrift:

:::{code-block} console
-6
:::

:::::::::::::


::::::::::::::

:::::::::::::::


:::{raw} html
---
file: ./python/kodevindu.html
---
:::




<!-- :::::::::::::{tab-item} CAS
Kommandoene nedenfor hører til Python pakken `casify`{l=python}. Ha med følgende kodelinje på toppen av programmet ditt:

:::{code-block} python
from casify import *
:::

| Tema | Kommando | Eksempel |
|------|----------|----------|
| Likninger | <ul><li>`løs(likning)`{l=python} (eksakt løsning)</li><li>`nløs(likning)`{l=python} (numerisk løsning)</li></ul> | <ul><li>`løs("x**2 - 3*x - 4 = 0")`{l=python} </li><li>`nløs("2 ** x = 10")`{l=python}</li></ul> |
| Ulikheter | `løs(ulikhet)`</li></ul> | <ul><li>`løs("x**2 - 3*x - 4 > 0")`{l=python} </li><li>`løs("x**3 - x + 2 <= 0")`{l=python}</li></ul> |

::::::::::::: -->
<!-- 
:::::::::::::{tab-item} Regresjon

**Kodemal** som kan kopieres og fylles ut:

:::{code-block} python
---
linenos:
---
from casify import *

xdata = [] # FYLL INN x-verdier
ydata = [] # FYLL INN y-verdier
modell = # FYLL INN: regresjonsmodell, f.eks "a * x ** b"

# Utfører regresjon
f = reg(
    modell=modell,
    xdata=xdata,
    ydata=ydata,
)

# Lager graf
f.graf(
    definisjonsmengde=(0, 100),
    xstep=10,
    ystep=5,
)


# Regner ut en funksjonsverdi med modellen
verdi = f(5)
print(verdi)


# Løser en likning med regresjonsmodellen
løsning = løs("f(x) = 10")

:::

::::::::::::: -->