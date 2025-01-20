
## Utledning av den deriverte (*)

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




