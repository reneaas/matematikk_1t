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



Tester med et interaktivt popup vindu:

:::{popup-code}
def f(x):
    return x**2 - x - 6


y = f(2)
print(y)


::: 
