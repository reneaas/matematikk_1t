# Lineære likninger


En **lineær likning** kan representeres på flere måter. For eksempel:
* Algebraisk: $f(x) = g(x)$ der $f$ og $g$ er lineære funksjoner.
* Grafisk: $x$-koordinaten til skjæringen mellom grafene til to lineære funksjoner.
* Programkode: Et program som søker etter en verdi for $x$ slik at $f(x) = g(x)$. 

::::::{admonition} Utforsk: lineære likninger
---
class: explore
---

Under vises noen eksempler på lineære likninger representert på tre forskjellige måter.

``````{tab-set} 
`````{tab-item} $ax + b = 0$

````{tab} Algebraisk
$$
x - 2 = 0
$$
````

````{tab} Grafisk
```{figure} ./figurer/ax+b=0.svg
---
name: fig-lineære-funksjoner-likninger-ax+b=0
width: 80%
---
```
````

````{tab} Programkode
```{code-block} python
---
linenos: true
---
def f(x):
    return x - 2

for x in range(-10, 11):
    if f(x) == 0:
        print(f"Løsning: {x = }")
```
````

`````

`````{tab-item} $ax + b = k$

````{tab} Algebraisk
$$
-2x + 4 = 2
$$
````

````{tab} Grafisk
```{figure} ./figurer/ax+b=k.svg
---
name: fig-lineære-funksjoner-likninger-ax+b=k
width: 80%
---
```
````

````{tab} Programkode
```{code-block} python
---
linenos: true
---
def f(x):
    return -2 * x + 4

def g(x):
    return 2


for x in range(-10, 11):
    if f(x) == g(x):
        print(f"Løsning: {x = }")
```
````

`````


`````{tab-item} $ax + b = cx + d$

````{tab} Algebraisk
$$
2x - 1 = x + 1
$$
````

````{tab} Grafisk
```{figure} ./figurer/ax+b=cx+d.svg
---
name: fig-lineære-funksjoner-likninger-ax+b=cx+d
width: 80%
---
```
````

````{tab} Programkode
```{code-block} python
---
linenos: true
---
def f(x):
    return 2 * x - 1

def g(x):
    return x + 1


for x in range(-10, 11):
    if f(x) == g(x):
        print(f"Løsning: {x = }")
```
````

`````

``````


::::::



Mer generelt, vil en lineær likning kunne skrives som

$$
f(x) = g(x)
$$

der $f$ og $g$ er lineære funksjoner. Løsningen til en lineær likning er i seg selv en likning som forteller oss hva verdien til $x$ må være for at de to funksjonsverdiene skal være like. 


:::{tableofcontents}
:::
