# Tallfølger


:::::{grid} 1 1 2 2
---
gutter: 3
---

::::{grid-item-card}
---
link: formler/teori
link-type: doc
---
**Formler**
^^^

$$
P_n = 2n 
$$


$$
O_n = 2n - 1
$$

::::


::::{grid-item-card}
---
link: programmering/teori
link-type: doc
---
**Programmering av tallfølger**
^^^
:::{code-block} python
---
linenos:
---
for n in range(1, 11):
    partall = 2 * n
    oddetall = 2 * n - 1
    
    print(partall, oddetall)
:::
::::



:::::