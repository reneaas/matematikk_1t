# Regnerekkefølgen

:::{admonition} Læringsmål
---
class: tip
---
Etter å ha gått gjennom dette kapittelet, er målet at du skal:
* Kunne bruke regnerekkefølgen til å regne ut uttrykk med parenteser, potenser, multiplikasjon, divisjon, addisjon og subtraksjon.
:::



## Regnerekkefølgen

Regnerekkefølgen er en tommelregel som gir oss en måte å regne ut matematiske uttrykk på. 

::::{admonition} Regnerekkefølgen
---
class: theory
---
Regnerekkefølgen sier at vi skal regne ut et matematisk uttrykk i følgende rekkefølge:
1. Parenteser
2. Potenser
3. Multiplikasjon og divisjon
4. Addisjon og subtraksjon
::::

Vi går løs på et eksempel:

::::{admonition} Eksempel 1: Regnerekkefølgen
---
class: example
---
Regn ut uttrykket

$$
6 + 3\cdot \dfrac{3\cdot(2^3 - 4)^2}{2}
$$


:::{admonition} Løsning
---
class: answer
---
Vi følger regnerekkefølgen:

\begin{flalign*}
6 + 5\cdot \dfrac{3\cdot\textcolor{red}{(2^3 - 6)^2}}{2} &= 6 + 5\cdot \dfrac{3\cdot\textcolor{red}{(8 - 6)^2}}{2} && \text{1. Parenteser + 2. Potenser}\\
\\
&= 6 + 5\cdot \dfrac{3\cdot \textcolor{red}{2^2}}{2} && \text{2. Potenser}\\
\\
&= 6 + 5\cdot \dfrac{\textcolor{red}{3 \cdot 4}}{2} && \text{3. Multiplikasjon}\\
\\
&= 6 + 5\cdot \textcolor{red}{\dfrac{12}{2}} && \text{3. Divisjon}\\
\\
&= 6 + \textcolor{red}{5\cdot 6} && \text{3. Multiplikasjon}\\
\\
& = \textcolor{red}{6 + 30} && \text{4. Addisjon}\\
\\
&= 36
\\
\end{flalign*}
:::
::::

Så er det **din tur**!

::::{admonition} Underveisoppgave 1
---
class: check
---
Regn ut 

$$
7 + \dfrac{5\cdot 2^2 + 1}{6 - 3} - 4
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$10$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker regnerekkefølgen:

\begin{flalign*}
7 + \dfrac{5\cdot 2^2 + 1}{\textcolor{red}{(6 - 3)}} - 4 &= 7 + \dfrac{5\cdot 2^2 + 1}{3} - 4 && \text{1. Parentes}\\
\\
&= 7 + \dfrac{5\cdot \textcolor{red}{2^2} + 1}{3} - 4 && \text{2. Potenser}\\
\\
&= 7 + \dfrac{\textcolor{red}{5\cdot 4} + 1}{3} - 4 && \text{3. Multiplikasjon}\\
\\
&= 7 + \dfrac{\textcolor{red}{(20 + 1)}}{3} - 4 && \text{1. Parenteser}\\
\\
&= 7 + \textcolor{red}{\dfrac{21}{3}} - 4 && \text{3. Divisjon}\\
\\
&= \textcolor{red}{7 + 7} - 4 && \text{4. Addisjon}\\
\\
&= \textcolor{red}{14 - 4} && \text{4. Subtraksjon}\\
\\
&= 10
\end{flalign*}
:::

::::