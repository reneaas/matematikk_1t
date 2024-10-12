# Lineære likninger


:::::{grid} 1 1 2 2
---
gutter: 3
---

::::{grid-item-card}
---
link: grafisk_løsning/grafisk_løsning
link-type: doc
---
**Grafisk løsning** 📈

^^^
:::{figure} grafisk_løsning/figurer/teori/ax+b=cx+d.svg
---
width: 100%
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
    2x + 6 &= 4 \\
    \\
    2x &= 4 - 6 \\
    \\
    2x &= -2 \\
    \\
    x &= -1
\end{align*}
::::

::::{grid-item-card}
---
link: programmering/programmering
link-type: doc
---
**Løsning med programmering** 💻

^^^

:::{code-block} python
def f(x):
    return 2*x + 6


for x in range(-5, 6):
    if f(x) == 0:
        print(x)
:::
:::::
