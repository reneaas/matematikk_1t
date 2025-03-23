# Sinussetningen


:::::::::::::::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare sinussetningen og bruke den til å finne ukjente sider og vinkler i en trekant.
* Kunne begrunne sinussetningen ut ifra arealsetningen.

:::::::::::::::


**Sinussetningen** gir oss en sammenheng mellom vinklene og sidelengdene i en trekant. Vi skal se at setningen er en uungåelig konsekvens av arealsetningen. Men først skal vi bli kjent med nøyaktig hva setningen forteller oss.



:::::::::::::::{admonition} Sinussetningen
---
class: summary
---
For en trekant $\triangle ABC$ med sidelengder $a$, $b$ og $c$ og motstående vinkler $A$, $B$ og $C$, gjelder følgende sammenheng:

$$
\dfrac{\sin \angle A}{a} = \dfrac{\sin \angle B}{b} = \dfrac{\sin \angle C}{c}
$$


:::{figure} ./figurer/teori/sinussetningen.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::::

---


:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Nedenfor vises en trekant $\triangle ABC$. 

Bestem de sidelengdene $x$ og $y$. 

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
width: 80%
class: no-click
---
:::


::::::::::::::{admonition} Løsning
---
class: solution
---
Sidelengden $y$ er motstående side til $\angle A = 40\degree$. Den motstående sidelengden til $\angle B = 35.52\degree$ er $3$. Ut ifra sinussetningen kan vi da sette opp likningen

$$
\dfrac{\sin (40\degree)}{y} = \dfrac{\sin (35.52\degree)}{3}
$$

Sidelengden $x$ er motstående side til $\angle C = 104.48\degree$. Da kan vi også sette opp likningen

$$
\dfrac{\sin(104.48\degree)}{x} = \dfrac{\sin(35.52\degree)}{3}
$$

Vi løser de to likningene med CAS:

:::{raw} html
---
file: ./ggb/eksempler/eksempel_1/solution.html
---
:::

<br>

Dermed er de ukjente lengdene $x = 5$ og $y \approx 3.32$. 

::::::::::::::




:::::::::::::::




