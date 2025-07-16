# Oppgaver: Regning med Python 


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---


Ta quizen!

:::{quiz}
Q: Hva skrives ut av programmet? <pre><code class="python">print(2 * 3 + 5)</code></pre>
+ $11$
- $16$
- $10$
- $30$

Q: Hva skrives ut av programmet? <pre><code class="python">x = 2 \ny = 3 * x + 6 \n\nprint(y)</code></pre>
+ $12$
- $24$
- $6$
- $15$

Q: Hva skrives ut av programmet? <pre><code class="python">a = 2 \nb = 3 \nc = a ** b \n\nprint(c)</code></pre>
+ $8$
- $6$
- $9$
- $5$


Q: Hva skrives ut av programmet? <pre><code class="python">x = 10 \ny = x / 2 + 3 \n\nprint(y)</code></pre>
+ $8.0$
- $7$
- $10$
- $6.5$

Q: Hva skrives ut av programmet? <pre><code class="python">x = 4 \ny = (x + 3) * 2 \n\nprint(y)</code></pre>
+ $14$
- $10$
- $7$
- $18$

Q: Hva skrives ut av programmet? <pre><code class="python">x = 2 \ny = 8 / (x + 2) * 2 \n\nprint(y)</code></pre>
+ $4$
- $1$
- $8$
- $2$

Q: Hvilket av programmene skriver ut et partall?
+ <pre><code class="python">n = 3 \ny = 2 * n \n\nprint(y)</code></pre>
- <pre><code class="python">n = 2 \ny = 3 ** n \n\nprint(y)</code></pre>
- <pre><code class="python">n = 3 \ny = 2 * n - 1 \n\nprint(y)</code></pre>
- <pre><code class="python">n = 1 \ny = 2 * n + 3 \n\nprint(y)</code></pre>


:::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Når et program ble kjørt, ga det utskriften

```console
6
-11
0
3
2.0
```

Programmet er vist i tilfeldig rekkefølge nedenfor. Sett sammen programmet i riktig rekkefølge.

:::{parsons-puzzle}
print(2 * 3)
print(-3 * 5 + 4)
print(-1 ** 2 + 1)
print((-1) ** 2 + 2)
print((3 + 1) / 2)
:::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3 
---
level: 1
---
Lag et program som regner ut og skriver ut tallene nedenfor.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
3 + 5 - 8
$$

:::{interactive-code}
# Din kode her



:::

:::::::::::::


:::::::::::::{tab-item} b
$$
3 \cdot 4 + 2 \cdot 5
$$

:::{interactive-code}
# Din kode her



:::

:::::::::::::



:::::::::::::{tab-item} c
$$
2^3 + 4^2 \cdot (3 - 8)
$$

:::{interactive-code}
# Din kode her



:::

:::::::::::::


:::::::::::::{tab-item} d
$$
3 \cdot\dfrac{(5 + 2)^3}{7} - 2
$$

:::{interactive-code}
# Din kode her



:::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
---
level: 2
---

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Lag et program som regner ut og skriver ut verdien til

$$
y = 2 \cdot x + 3
$$

for $x = 2$.

:::{interactive-code}
# Din kode her 


:::

::::{answer}
:::{code-block} python
---
linenos:
---
x = 2
y = 2*x + 3

print(y)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut og skriver ut verdien til

$$
y = -2(x + 3)
$$

for $x = 5$.

:::{interactive-code}
# Din kode her 


:::


::::{answer}
:::{code-block} python
---
linenos:
---
x = 5
y = -2 * (x + 3)

print(y)
:::
::::


:::::::::::::


:::::::::::::{tab-item} c
Lag et program som regner ut og skriver ut verdien til

$$
y = x^2 + 3x - 4
$$

for $x = -2$.

:::{interactive-code}
# Din kode her 


:::


::::{answer}
:::{code-block} python
---
linenos:
---
x = -2 
y = x**2 + 3*x - 4

print(y)
:::
::::


:::::::::::::


:::::::::::::{tab-item} d
Lag et program som regner ut og skriver ut verdien til

$$
y = 5x^3 - 3x^2 + 1
$$

for $x = 3$.

:::{interactive-code}
# Din kode her 


:::

::::{answer}
:::{code-block} python
---
linenos:
---
x = 3
y = 5 * x**3 - 3 * x**2 + 1

print(y)
:::
::::


:::::::::::::

::::::::::::::


:::::::::::::::





