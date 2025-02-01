# Oppgaver: Derivasjon og optimering



:::::::::::::::{admonition} Oppgave X
---
class: problem-level-2
---
{numref}`fig-oppgave-x` viser grafen til en rasjonal funksjon $f$ som er gitt ved 

$$
f(x) = \dfrac{8}{x^2 + 4} \,, \quad D_f = [0, \to \rangle.
$$

Et rektangel har hjørnene $(0, 0)$, $(3, 0)$, $(3, f(3))$ og $(0, f(3))$.

:::{figure} ./figurer/oppgaver/oppgave_x/graf.svg
---
name: fig-oppgave-x
width: 80%
class: no-click
---
viser grafen til $f$ og et rektangel med hjørner $(0, 0)$, $(3, 0)$, $(3, f(3))$ og $(0, f(3))$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet til rektangelet.


:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet under og bruk det til å lage en systematisk oversikt over arealene til rektanglene med hjørner $(0, 0)$, $(n, 0)$, $(n, f(n))$ og $(0, f(n))$ for $n \in \{0, 1, 2, \ldots, 10\}$. 



:::::::::::::


:::::::::::::{tab-item} c
En strategi for å bestemme det største mulige arealet er forklart under.

::::::::::::{admonition} Strategi: Maksimere en funksjon $f$
---
class: theory
---
Gitt en funksjon $f$, kan vi bestemme $x$ slik at $f(x)$ er størst mulig ved:
1. Start med den laveste verdien $x \in D_f$. 
2. Sjekk om $f(x) < f(x + 1)$. 
3. Øk verdien til $x$ med $1$ og gjenta punkt 2 frem til $f(x) \geq f(x + 1)$. 

Verdien til $x$ vil da svare til $x$-verdien som gjør $f(x)$ størst mulig. 
::::::::::::



:::::::::::::

::::::::::::::


:::::::::::::::
