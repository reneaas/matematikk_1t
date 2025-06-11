# Regning med parenteser

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare dem distributive loven
* Kunne bruke den distributive loven til å utvide og faktorisere algebraiske uttrykk
:::::


## Den distributive lov
Den distributive loven lar oss både utvide og faktorisere algebraiske uttrykk. 

:::::{theory} Den distributive lov
---
class: theory
---
For alle tall $a$, $b$ og $c$ gjelder:

$$
a \cdot (b + c) = a \cdot b + a \cdot c
$$

Vi kan tolke dette som at når vi skal legge sammen $(b + c)$ eksemplarer av $a$, kan vi først legge sammen $b$ eksemplarer av $a$ og deretter $c$ eksemplarer av $a$.
:::::

Vi kan begrunne den distributive loven ved arealberegninger med utgangspunkt i figuren nedenfor.

:::{figure} ./figurer/teori/distributiv_lov.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser en figur bestående av to rektangler. Det blå fargelagte rektangelet har sidelengder $a$ og $b$, og det rød fargelagte rektangelet har sidelengder $a$ og $c$.
:::

Arealet av hele figuren kan skrives på to måter:
1. Arealet av hele figuren som er et rektangel med sidelengder $a$ og $(b + c)$
2. Summen av arealene til de to mindre rektanglene.

Da får vi

::::{grid}
:::{grid-item-card}
Hele figuren
^^^
$$
\mathrm{areal} = a \cdot (b + c)
$$
:::

:::{grid-item-card}
Summen av arealene
^^^
$$
\mathrm{areal} = a \cdot b + a \cdot c
$$
:::
::::

De to arealene må være like som betyr at 

$$
a \cdot (b + c) = a \cdot b + a \cdot c
$$


Dette er et eksempel på en **identitet**. En identitet er en likning som er sann for alle verdier av variablene i likningen. Uansett hvilke tall vi setter inn for $a$, $b$ og $c$, vil likningen alltid stemme.

Vi kan bruke den distributive loven til å både utvide og faktorisere algebraiske uttrykk.


#### Utvide uttrykk

:::::{example} Eksempel 2
Utvid uttrykket nedenfor

$$
3x(2x + 4y)
$$

::::{admonition} Løsning
---
class: solution
---
Vi bruker den distributive loven for å utvide uttrykket:

:::{sidebar}
**Distributiv lov**

$$
a\cdot(b + c) = a\cdot b + a\cdot c
$$
:::

$$
3x(2x + 4y) = 3x\cdot 2x + 3x\cdot 4y = 6x^2 + 12xy
$$
::::

:::::

---

:::::{exercise} Underveisoppgave 2
Utvid uttrykket nedenfor

$$
2y(3x + 5)
$$


::::{answer}
$$
6xy + 10y
$$
::::

::::{solution}
Vi bruker den distributive loven for å utvide uttrykket:

$$
2y(3x + 5) = 2y\cdot 3x + 2y\cdot 5 = 6xy + 10y
$$

::::
:::::


#### Faktorisering


:::{margin}

$$
a\cdot(b + c) = a\cdot b + a\cdot c
$$
:::

:::::{example} Eksempel 3
Faktoriser uttrykket nedenfor 

$$
6x^2 + 12xy
$$

::::{admonition} Løsning
---
class: solution
---

Vi kan se at begge ledd har en felles faktor $6x$. Vi kan bruke den distributive loven i motsatt retning for å faktorisere uttrykket:

$$
6x^2 + 12xy = 6x \cdot x + 6x \cdot 2y = 6x(x + 2y)
$$
::::

:::::

---

:::::{exercise} Underveisoppgave 3
Faktoriser uttrykket nedenfor

$$
4x^3 + 8xy
$$

::::{answer}
$$
4x(x^2 + 2y)
$$
::::

::::{solution}
Vi kan se at begge ledd har en felles faktor $4x$. Vi kan bruke den distributive loven i motsatt retning for å faktorisere uttrykket:

$$
4x^3 + 8xy = 4x \cdot x^2 + 4x \cdot 2y = 4x(x^2 + 2y)
$$
::::
:::::


## Den doble distributive loven
Den distributive loven kan også brukes når vi har to parenteser som skal ganges med hverandre. Vi kan kalle den for den **dobbelt distributive loven**.

:::::{theory} Den doble distributive loven
---
class: theory
---
For alle tall $a$, $b$, $c$ og $d$ gjelder:

$$
(a + b)(c + d) = a \cdot c + a \cdot d + b \cdot c + b \cdot d
$$
:::::

---

:::::{exercise} Underveisoppgave 4
I figuren nedenfor vises et stort rektangel med sidelengder $(a + b)$ og $(c + d)$. Figuren er bygget opp av fire mindre rektangler. Se figuren nedenfor.

:::{figure} ./figurer/teori/dobbel_distributiv_lov.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::


Bruk arealberegninger til å vise at den doble distributive loven stemmer.

::::{solution}
Det store rektangelet har sidelengder $(a + b)$ og $(c + d)$, så arealet av det store rektangelet er

$$
\mathrm{areal} = (a + b)\cdot (c + d)
$$

Arealet av de fire mindre rektanglene er 

$$
\mathrm{areal} = a \cdot c + a \cdot d + b \cdot c + b \cdot d
$$

Siden de to arealene er like, følger det at 

$$
(a + b)\cdot (c + d) =  a \cdot c + a \cdot d + b \cdot c + b \cdot d
$$

::::

:::::


---

:::::{example} Eksempel 4
Utvid uttrykket nedenfor

$$
(2x + 3)(x + 4)
$$

::::{admonition} Løsning
---
class: solution
---
\begin{align*}
(2x + 3)(x + 4) &= 2x \cdot x + 2x \cdot 4 + 3 \cdot x + 3 \cdot 4 \\
\\
&= 2x^2 + 8x + 3x + 12 \\
\\
&= 2x^2 + 11x + 12
\end{align*}
::::
:::::

---

:::::{exercise} Underveisoppgave 5
Utvid uttrykket nedenfor

$$
(3x + 2)(2x + 5)
$$

::::{answer}
$$
6x^2 + 19x + 10
$$
::::

::::{solution}
\begin{align*}
(3x + 2)(2x + 5) &= 3x \cdot 2x + 3x \cdot 5 + 2 \cdot 2x + 2 \cdot 5 \\
\\
&= 6x^2 + 15x + 4x + 10 \\
\\
&= 6x^2 + 19x + 10
\end{align*}
::::
:::::







