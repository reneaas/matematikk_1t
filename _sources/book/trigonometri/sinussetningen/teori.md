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
class: no-click, adaptive-figure
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
class: no-click, adaptive-figure
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


---


Nå skal vi se på hvorfor sinussetningen stemmer ved å ta utgangspunkt i arealsetningen. 



:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
I figuren nedenfor vises en trekant $\triangle ABC$.



:::{figure} ./figurer/teori/sinussetningen.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Skriv ned en formel for arealet til $\triangle ABC$ med utgangspunkt i vinkel $\angle A$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T = \dfrac{1}{2}bc \sin \angle A
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Skriv ned en formel for arealet til $\triangle ABC$ med utgangspunkt i vinkel $\angle B$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T = \dfrac{1}{2}ac \sin \angle B
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Skriv ned en formel for arealet til $\triangle ABC$ med utgangspunkt i vinkel $\angle C$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T = \dfrac{1}{2}ab \sin \angle C
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Forklar at 

$$
bc \sin \angle A = ac \sin \angle B = ab \sin \angle C
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
Vi har skrevet opp arealet $T$ på tre forskjellige måter ved å ta utgangspunkt i de tre vinklene. Dette arealet er likt uansett hvilken vinkel vi tar utgangspunkt i som betyr at 

$$
\dfrac{1}{2} bc \sin \angle A = \dfrac{1}{2} ac \sin \angle B = \dfrac{1}{2} ab \sin \angle C
$$

som derfor betyr at 

$$
bc \sin \angle A = ac \sin \angle B = ab \sin \angle C
$$
::::

:::::::::::::


:::::::::::::{tab-item} e
Bruk resultatet i **d** til å komme fram til sinussetningen.

$$
\dfrac{\sin \angle A}{a} = \dfrac{\sin \angle B}{b} = \dfrac{\sin \angle C}{c}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
Deler vi med $abc$ i alle uttrykkene i likningene fra **d** får vi:

$$
\dfrac{bc \sin \angle A}{abc} = \dfrac{ac \sin \angle B}{abc} = \dfrac{ab \sin \angle C}{abc}
$$

som gir

$$
\dfrac{\sin \angle A}{a} = \dfrac{\sin \angle B}{b} = \dfrac{\sin \angle C}{c}
$$
::::

:::::::::::::



::::::::::::::


:::::::::::::::



