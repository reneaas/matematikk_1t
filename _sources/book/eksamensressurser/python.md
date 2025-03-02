# Python


:::::::::::::::{admonition} Oversikt over kommandoer
---
class: summary, dropdown
---
::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} `for`{l=python}-løkker

:::::::::::::


:::::::::::::{tab-item} `while`{l=python}-løkker

:::::::::::::


:::::::::::::{tab-item} CAS
Kommandoene nedenfor hører til Python pakken `casify`{l=python}. Ha med følgende kodelinje på toppen av programmet ditt:

:::{code-block} python
from casify import *
:::

| Tema | Kommando | Eksempel |
|------|----------|----------|
| Likninger | <ul><li>`løs(likning)`{l=python} (eksakt løsning)</li><li>`nløs(likning)`{l=python} (numerisk løsning)</li></ul> | <ul><li>`løs("x**2 - 3*x - 4 = 0")`{l=python} </li><li>`nløs("2 ** x = 10")`{l=python}</li></ul> |
| Ulikheter | `løs(ulikhet)`</li></ul> | <ul><li>`løs("x**2 - 3*x - 4 > 0")`{l=python} </li><li>`løs("x**3 - x + 2 <= 0")`{l=python}</li></ul> |

:::::::::::::

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

:::::::::::::


::::::::::::::

:::::::::::::::


:::{raw} html
---
file: ./python/kodevindu.html
---
:::