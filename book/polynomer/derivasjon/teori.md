# Den deriverte

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke polynomdivisjon til å bestemme likningen for en tangent.
* Kunne derivere polynomfunksjoner algebraisk.
* Kunne bestemme ekstremalpunktene til en polynomfunksjon ved hjelp av den deriverte.
:::


## Polynomdivisjon og tangenter

Vi har allerede sett at resten i polynomdivisjon med $f(x) : (x - r)$ lar oss bestemme $f(r)$. Her skal vi gå et steg videre å se at resten i en bestem polynomdivisjon kan brukes til å bestemme likningen for en tangent til grafen til polynomfunksjonen.


:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 4x + 5.
$$



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem likningen for tangenten til grafen til $f$ i $(1, f(1))$ ved å bruke at $f'(x) = 2ax + b$ for en andregradsfunksjon.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -2x + 4
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
Regn ut

$$
f(x) : (x - 1)^2 
$$


Sammenlikn **resten** med likningen for tangenten du fant i **a**. 

> Husk å utvide $(x - 1)^2$ før du gjør polynomdivisjonen.

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./koder/utforsk/utforsk_1/b_annotert.svg
---
width: 80%
class: no-click
---
:::

::::

:::::::::::::



::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Setning: Resten i polynomdivisjon $f(x) : (x - r)^2$
---
class: summary
---
Gitt et polynom $f$, vil resten i polynomdivisjonen $f(x) : (x - r)^2$ være likningen til tangenten $T$ som går gjennom punktet $(r, f(r))$ på grafen til $f$.

:::::::::::::::


Før vi går videre, bør du prøve å anvende setningen.


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 - 4x + 12.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Regn ut

$$
f(x) : (x - 2)^2
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./koder/underveisoppgaver/underveisoppgave_1/a.svg
---
width: 100%
class: no-click
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk resultatet ditt fra **a** til å bestemme likningen for tangenten til grafen til $f$ i $(2, f(2))$.


:::{admonition} Fasit
---
class: answer, dropdown
---
Fra oppgave **a** har vi at resten er gitt ved 

$$
y = -4x + 8,
$$

som er tangenten til grafen til $f$ i $(2, f(2))$.
:::
:::::::::::::




::::::::::::::


:::::::::::::::

---

## Den deriverte til en polynomfunksjon

Polynomdivisjonen $f(x) : (x - r)^2$ lar oss finne tangenten til grafen til $f$ i punkt $(r, f(r))$ ved å lese av likningen til resten. Dette kan vi bruke til å generelt finne den deriverte til en polynomfunksjon siden stigningstallet til tangenten i $(r, f(r))$ er $f'(r)$. 



:::::::::::::::{admonition} Utforsk 2
---
class: explore
---
Et tredjegradspolynom er gitt ved 

$$
f(x) = ax^3
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Regn ut 

$$
f(x) : (x - r)^2
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./koder/utforsk/utforsk_2/a.svg
---
width: 100%
class: no-click
---
:::

::::



:::::::::::::


:::::::::::::{tab-item} b
Bruk resultatet ditt fra **a** til å bestemme $f'(r)$.

:::{admonition} Fasit
---
class: answer, dropdown
---
Resten fra polynomdivisjonen i **a** er 

$$
y = 3ar^2x - 2ar^3.
$$

Siden stigningstallet til tangenten i $(r, f(r))$ er $f'(r)$, har vi at

$$
f'(r) = 3ar^2.
$$
:::

:::::::::::::

:::::::::::::{tab-item} c
Forklar at resultatet ditt fra **b** gjelder for alle $r$ og at det derfor betyr at når $f(x) = ax^3$, så er 

$$
f'(x) = 3ax^2
$$

:::::::::::::

::::::::::::::

:::::::::::::::

---

Vi kan oppsummere derivasjonsreglene for polynomer som følger:


:::::::::::::::{admonition} Setning: Derivasjon av polynomfunksjoner
---
class: summary
---
Derivasjonsreglene for polynomer er som følger: 

1. $(x^n)' = n\cdot x^{n-1}$
2. $(ax^n)' = a \cdot (x^n)'$
3. $(a x^n + bx^m)' = a \cdot (x^n)' + b \cdot (x^m)'$
4. $C' = 0$ for $C \in \mathbb{R}$ (den deriverte til en konstant er $0$).
:::::::::::::::

---

::::{admonition} Definisjon: $x^0$
---
class: sidenote, margin
---
Vi definerer $x^0 = 1$ for alle $x \neq 0$. 
::::

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Bestem den deriverte til 

$$
f(x) = 2x^3 - 4x^2 + 6x - 2
$$

::::{admonition} Løsning
---
class: solution
---
\begin{align*}
    f'(x) &= (2x^3 - 4x^2 + 6x - 2)' \\
    \\
    &= 2\cdot (x^3)' - 4\cdot (x^2)' + 6\cdot x' - 2' \\
    \\
    &= 2 \cdot 3\cdot x^2 - 4\cdot 2 \cdot x^1 + 6 \cdot 1 \cdot x^0 - 0 \\
    \\
    &= 6x^2 - 8x + 6
\end{align*}
::::

:::::::::::::::




