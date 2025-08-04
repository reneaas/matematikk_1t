# Kvadratsetningene

:::{goals}
* Kunne bruke kvadratsetningene til å skrive om andregradsuttrykk
* Kunne forklare hva en matematisk identitet er, avgjøre om en sammenheng er en identitet, og gi konkrete eksempler på identiteter. 
:::


:::{margin} 
I oppgavene skal du få begrunne kvadratsetningene geometrisk. 
:::


Det finnes til sammen tre kvadratsetninger:

:::{summary} Kvadratsetningene
Gitt to vilkårlige tall $a, b \in \mathbb{R}$, så gjelder følgende tre setninger:

1.Kvadratsetning
: $(a + b)^2 = a^2 + 2ab + b^2$

2.Kvadratsetning
: $(a - b)^2 = a^2 - 2ab + b^2$

Konjugatsetningen
: $(a + b)(a - b) = a^2 - b^2$
:::

---

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Vi har møtt på andregradsuttrykk som passer rett inn i disse tre setningene. Her viser vi ett eksempel på hver av dem. 

::::::::::::::{tab-set}
:::::::::::::{tab-item} 1.kvadratsetning
$$
(x + 3)^2 = x^2 + 2\cdot x\cdot 3 + 3^2 = x^2 + 6x + 9
$$
:::::::::::::

:::::::::::::{tab-item} 2.kvadratsetning
$$
(x - 4)^2 = x^2 - 2\cdot x\cdot 4 + 4^2 = x^2 - 8x + 16
$$
:::::::::::::

:::::::::::::{tab-item} Konjugatsetningen
$$
(x + 2)(x - 2) = x^2 - 2^2 = x^2 - 4
$$
:::::::::::::
::::::::::::::


:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bruk kvadratsetningene til å utvide uttrykkene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
(x + 5)^2
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x^2 + 10x + 25
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
$$
(x - 2)^2 
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x^2 - 4x + 4
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
$$
(x + 4)(x - 4)
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x^2 - 16
$$
:::
:::::::::::::

::::::::::::::
:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
Bruk kvadratsetningene til å skrive om andregradsuttrykkene til nullpunktsform.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
$$
x^2 - 2x + 1
$$
:::::::::::::

:::::::::::::{tab-item} b
$$
x^2 + 12x + 36
$$
:::::::::::::

:::::::::::::{tab-item} c
$$
x^2 - 49
$$
:::::::::::::
::::::::::::::

:::::::::::::::


## Matematiske identiteter
Kvadratsetningene er eksempler på det vi kaller for en **identitet**. For eksempel vil 

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

være sann *uansett* hvilke tall $a$ og $b$ er. Da sier vi at sammenhengen er en identitet fordi den er sann uansett hvilke verdier variablene har.

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Bestem $s$ slik at sammenhengen nedenfor blir en identitet:

$$
9x^2 - 30x + 25 = (3x - s)^2.
$$

::::{admonition} Løsning
---
class: solution
---
Vi kan bruke 2.kvadratsetningen til å utvide uttrykket på høyre side:

$$
(3x - s)^2 = (3x)^2 - 2\cdot 3x\cdot s + s^2 = 9x^2 - 6sx + s^2.
$$

For at sammenhengen skal bli en identitet, må vi bestemme $s$ slik at vi får likhet for disse to uttrykkene:

$$
9x^2 - 30x + 25 = 9x^2 - 6sx + s^2
$$

Ved sammenlikning, kan vi se at dette må bety at 

$$
-30 = -6s \quad \land \quad 25 = s^2
$$

Fra den første likningen, får vi 

$$
-30 = -6s \quad \iff \quad s = 5.
$$

Fra den andre likningen får vi at

$$
s^2 = 25 \quad \iff \quad s = \pm 5.
$$

Men bare den positive løsningen gir oss en identitet, som betyr at vi må ha $s = 5$.

::::
:::::::::::::::

