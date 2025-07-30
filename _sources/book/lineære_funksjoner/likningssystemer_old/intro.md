# Lineære likningssystemer

:::::{grid} 1 1 2 2
---
gutter: 3
---

::::{grid-item-card}
---
link: ./grafisk_løsning/grafisk_løsning
link-type: doc
---
**Grafisk løsning** 📈

^^^
:::{figure} ./grafisk_løsning/figurer/teori/grafisk_løsning.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::
::::

::::{grid-item-card}
---
link: algebraisk_løsning/algebraisk_løsning
link-type: doc
---
**Algebraisk løsning** ✍🏼

^^^
\begin{align*}
    x + y &= 2 && (\mathrm{I}) \\
    x - y &= 0 && (\mathrm{II}) \\
    \\
    x + y &= 2 && (\mathrm{I}) \\
    x &= y && (\mathrm{II})
    \\
    \vdots &&& \vdots
\end{align*}

::::

::::{grid-item-card}
---
link: ./programmering/programmering
link-type: doc
---
**Løsning med programmering** 💻

^^^
:::{code-block} python
for x in range(-5, 6):
    for y in range(-5, 6):
        if x + y == 2 and x - y == 0:
            print(x, y)
:::
::::

:::::