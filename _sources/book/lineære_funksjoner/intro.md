# Lineære funksjoner

:::::{grid} 1 1 2 2
---
gutter: 3
---

::::{grid-item-card}
---
link: representasjoner/intro
link-type: doc
---
**Representasjoner**

^^^
$$
f(x) = ax + b
$$

---

:::{figure} representasjoner/figurer/f.svg
---
width: 100%
---
:::

---

```{code-block} python
def f(x):
    return a * x + b
```
::::

::::{grid-item-card}
---
link: likninger/intro
link-type: doc
---
**Likninger**

^^^
$$
f(x) = g(x)
$$

---

:::{figure} likninger/grafisk_løsning/figurer/teori/ax+b=cx+d.svg
---
width: 100%
---
:::

---

```{code-block} python
def f(x):
    return 2*x - 6

for x in range(-5, 6):
    if f(x) == 2:
        print(x)
```
::::

::::{grid-item-card}
---
link: likningssystemer/intro
link-type: doc
---
**Likningssystemer**

^^^

$$
2x + 3y = 7 \quad \land \quad -x + y = 2
$$

---

:::{figure} likningssystemer/figurer/intro.svg
---
width: 100%
---
:::

---

```{code-block} python
for x in range(-5, 6):
    for y in range(-5, 6):
        if x + y == 2 and x - y == 0:
            print(x, y)
```
::::

::::{grid-item-card}
---
link: ulikheter/intro
link-type: doc
---
**Ulikheter**

^^^

$$
2x - 6 > 2
$$

---

:::{figure} ulikheter/grafisk_løsning/figurer/teori/ulikhet_type_3.svg
---
width: 100%
---
:::


---

:::{figure} ulikheter/figurer/fortegnslinjer.svg
---
width: 100%
---
:::

---

::::





:::::







