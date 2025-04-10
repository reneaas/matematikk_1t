# Oppgaver: Lineære likningssystemer

:::::{grid} 1 1 2 2
---
gutter: 3
---

::::{grid-item-card}
---
link: ./grafisk_løsning/oppgaver
link-type: doc
---
**Oppgaver: Grafisk løsning** 📈

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
link: algebraisk_løsning/oppgaver
link-type: doc
---
**Oppgaver: Algebraisk løsning** ✍🏼

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
link: programmering/oppgaver
link-type: doc
---
**Oppgaver: Løsning med programmering** 💻

^^^
:::{code-block} python
for x in range(-5, 6):
    for y in range(-5, 6):
        if x + y == 2 and x - y == 0:
            print(x, y)
:::
::::

:::::