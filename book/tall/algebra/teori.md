# Algebra


:::{goals} Læringsmål
* Kunne forenkle algebraiske uttrykk.
* Kunne forklare hva et algebraisk uttrykk er. 
* Kunne begrunne og bruke kvadratsetningene til å utvide og faktorisere algebraiske uttrykk.
* Kunne begrunne og bruke de distributive lovene for å utvide og faktorisere algebraiske uttrykk.
:::

## Algebraiske uttrykk

Et algebraisk uttrykk består av variabler, koeffisienter, faktorer og ledd. Nedenfor ser du to eksempler på algebraiske uttrykk der vi har markert hvilke deler som hører til de ulike begrepene.


:::::::::::::::{example} Eksempel 1
:::::{grid}
::::{grid-item}
:::{figure} ./figurer/teori/algebraisk_uttrykk_1.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

::::{grid-item}
:::{figure} ./figurer/teori/algebraisk_uttrykk_2.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::
:::::
:::::::::::::::


---

:::::{exercise} Underveisoppgave 1
Bestem hvilke deler av uttrykket nedenfor som er **ledd**, **variabler**, **faktorer** og **koeffisienter**. 


$$
3x^2 + 4xy
$$


::::{solution}
Ledd
: $3x^2$ og $4xy$

Variabler
: $x$ og $y$

Faktorer
: $3$ og $x^2$ i leddet $3x^2$, og $4$, $x$ og $y$ i leddet $4xy$

Koeffisienter
: $3$ i leddet $3x^2$ og $4$ i leddet $4xy$
::::

:::::


---



## Legge sammen algebraiske uttrykk
Ofte må vi legge sammen eller trekke algebraiske uttrykk fra hverandre. Da legger vi sammen koeffisientene til like variabler. La oss se på et eksempel:

:::::{example} Eksempel 2
Skriv uttrykket nedenfor så enkelt som mulig

$$
3x + 4y - 5x + y
$$

::::{admonition} Løsning
---
class: solution
---
Vi legger sammen ledd som inneholder samme variabel:

$$
3x + 4y - 5x + y = (3x - 5x) + (4y + y) = -2x + 5y
$$
::::

:::::

---

:::::{exercise} Underveisoppgave 2
Skriv uttrykket nedenfor så enkelt som mulig

$$
6x - 3y + 2x + 5y 
$$

::::{answer}
$$
8x + 2y
$$
::::

::::{solution}
Vi legger sammen ledd som inneholder samme variabel:

$$
6x - 3y + 2x + 5y = (6x + 2x) + (-3y + 5y) = 8x + 2y
$$
::::
:::::


---

Når vi åpner opp en parentes, gjelder følgende regneregler:

:::::::::::::::{summary} Åpne parentser
\begin{align*}
a + (b + c) &= a + b + c \\
\\
a - (b - c) &= a - b + c \\
\end{align*}
:::::::::::::::


:::::::::::::::{example} Eksempel 3
Trekk sammen uttrykket nedenfor.

$$
x + (2x - 3) - (4 - x)
$$

::::{solution}
---
dropdown: 0
---
\begin{align*}
x + (2x - 3) - (4 - x) &= x + 2x - 3 - 4 + x \\
\\
&= (x + 2x + x) + (-3 - 4) \
\\
&= 4x - 7
\end{align*}
::::

:::::::::::::::

## 1.Distributiv lov
Den 1.distributive loven lar oss utvide og faktorisere algebraiske uttrykk med en felles faktor. 


:::::::::::::::{summary} 1.Distributiv lov
For tall $a$, $b$ og $c$ gjelder

$$
a(b + c) = ab + ac
$$

:::::::::::::::


---

:::::::::::::::{theory} Begrunnelse for 1.distributiv lov

Nedenfor vises et rektangel.

:::{figure} ./figurer/bevis/bevis_1/figur_annotert.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

Rektangelet har sidelengder $a$ og $(b + c)$ Arealet av hele rektangelet kan derfor bestemmes direkte ved å gange sidelengdene: 

$$
\text{Areal} = a \cdot (b + c)
$$

Hele rektangelet er bygget opp av to mindre rektangler. Det ene rektangelet har sidelengder $a$ og $b$ og dermed et areal $ab$. Det andre rektangelet har sidelengder $a$ og $c$ og dermed et areal $ac$. Arealet av hele rektangelet kan derfor også bestemmes ved å legge sammen arealene til de to mindre rektanglene:

$$
\text{Areal} = ab + ac
$$

De to arealene må være like, og da får vi 1.distributiv lov:

$$
a(b + c) = ab + ac
$$

:::::::::::::::

---

Vi kan bruke 1.distributiv lov både til å utvide og faktorisere algebraiske uttrykk. La oss se på et eksempel der vi bruker den til å utvide et uttrykk:

:::::::::::::::{example} Eksempel 4

Utvid uttrykket nedenfor:

$$
2x(3x + 4)
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 1.distributiv lov:

$$
2x(3x + 4) = 2x\cdot 3x + 2x\cdot 4 = 6x^2 + 8x
$$
::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 4

Utvid uttrykket nedenfor. 

$$
3x(2x - 5)
$$

::::{answer}
$$
6x^2 - 15x
$$
::::


::::{solution}
Vi bruker 1.distributiv lov:

$$
3x(2x - 5) = 3x\cdot 2x - 3x\cdot 5 = 6x^2 - 15x
$$
::::

:::::::::::::::


---

La oss se på et eksempel der vi bruker 1.distributiv lov til å faktorisere et uttrykk:


:::::::::::::::{example} Eksempel 5
Faktoriser uttrykket nedenfor.

$$
3x^2 + 6x
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 1.distributiv lov baklengs:

$$
3x^2 + 6x = \textcolor{red}{3x}\cdot \textcolor{RoyalBlue}{x} + \textcolor{red}{3x}\cdot \textcolor{RoyalBlue}{2} = \textcolor{red}{3x}(\textcolor{RoyalBlue}{x} + \textcolor{RoyalBlue}{2})
$$
::::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 5

Faktoriser uttrykket nedenfor.

$$
4x^2 - 8x
$$


::::{answer}
$$
4x(x - 2)
$$
::::

::::{solution}
Vi bruker 1.distributiv lov baklengs:

$$
4x^2 - 8x = \textcolor{red}{4x}\cdot \textcolor{RoyalBlue}{x} - \textcolor{red}{4x}\cdot \textcolor{RoyalBlue}{2} = \textcolor{red}{4x}(\textcolor{RoyalBlue}{x} - \textcolor{RoyalBlue}{2})
$$
::::

:::::::::::::::



## Kvadratsetningene


:::{margin} Begrep: Identitet
En identitet er en likning som er sann uansett hvilke verdier vi setter inn for variablene. 
:::


Kvadratsetningene er tre viktige **identiteter** som lar oss gange sammen og faktorisere to spesielle algebraiske uttrykk som dukker opp når vi senere skal jobbe med andregradsfunksjoner. 

### 1.Kvadratsetning

:::::::::::::::{summary} 1.Kvadratsetning
For to tall $a$ og $b$ gjelder

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

:::::::::::::::


---

::::::::::::::{theory} Begrunnelse for 1.kvadratsetning
Nedenfor vises en figur av et kvadrat. Kvadratet er delt opp i mindre rektangler. 

:::{figure} ./figurer/bevis/bevis_2/figur_annotert.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

Sidelengdene av hele kvadratet er $a + b$. Det betyr at arealet av hele kvadratet er 

$$
\text{Areal} = (a + b) \cdot (a + b) = (a + b)^2
$$

Vi kan også regne ut arealet av figuren ved å legge sammen arealene av de mindre rektanglene. Da får vi: 

$$
\text{Areal} = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2
$$

Siden de to arealene må være like, så får vi 

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

som er 1.kvadratsetning.

::::::::::::::

---

Vi kan bruke 1.kvadratsetning både til å utvide og faktorisere algebraiske uttrykk. La oss se på et eksempel der vi utvider et uttrykk med 1.kvadratsetning:

:::::::::::::::{example} Eksempel 6

Utvid uttrykket nedenfor med 1.kvadratsetning

$$
(2x + 3)^2
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 1.kvadratsetning:

$$
(\textcolor{red}{2x} + \textcolor{RoyalBlue}{3})^2 = (\textcolor{red}{2x})^2 + 2\cdot \textcolor{red}{2x}\cdot \textcolor{RoyalBlue}{3} + \textcolor{RoyalBlue}{3}^2 = 4x^2 + 12x + 9
$$

::::



:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 6

Bruk 1.kvadratsetning til å utvide uttrykket 
nedenfor.

$$
(3x + 1)^2
$$


::::{answer}
$$
9x^2 + 6x + 1
$$
::::

::::{solution}
Vi bruker 1.kvadratsetning:

$$
(3x + 1)^2 = (3x)^2 + 2\cdot (3x)\cdot 1 + 1^2 = 9x^2 + 6x + 1
$$
::::


:::::::::::::::


---

La oss se på et eksempel der vi bruker 1.kvadratsetning til å faktorisere et uttrykk:

:::::::::::::::{example} Eksempel 7
Bruk 1.kvadratsetning til å faktorisere uttrykket nedenfor

$$
x^2 + 6x + 9
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 1.kvadratsetning baklengs:

$$
x^2 + 6x + 9 = \textcolor{red}{x}^2 + 2 \cdot \textcolor{red}{x} \cdot \textcolor{RoyalBlue}{3} + \textcolor{RoyalBlue}{3}^2 = (\textcolor{red}{x} + \textcolor{RoyalBlue}{3})^2
$$

::::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 7
Bruk 1.kvadratsetning til å faktorisere uttrykket nedenfor.

$$
x^2 + 4x + 4
$$


::::{answer}
$$
(x + 2)^2
$$
::::


::::{solution}
Vi bruker 1.kvadratsetning baklengs:

$$
x^2 + 4x + 4 = \textcolor{red}{x}^2 + 2 \cdot \textcolor{red}{x} \cdot \textcolor{RoyalBlue}{2} + \textcolor{RoyalBlue}{2}^2 = (\textcolor{red}{x} + \textcolor{RoyalBlue}{2})^2
$$
::::

:::::::::::::::


### 2.Kvadratsetning

:::::::::::::::{summary} 2.Kvadratsetning
For to tall $a$ og $b$ gjelder

$$
(a - b)^2 = a^2 - 2ab + b^2
$$
:::::::::::::::

---


:::::::::::::::{theory} Begrunnelse for 2.kvadratsetning
I figuren nedenfor vises et kvadrat. Kvadratet er delt opp i mindre rektangler. 


:::{figure} ./figurer/bevis/bevis_3/figur_annotert.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


Vi ser at det blå fargelagte området er et kvadrat med sidelengder $(a - b)$. Arealet av det blå fargelagte området er derfor

$$
\text{Areal} = (a - b) \cdot (a - b) = (a - b)^2
$$

Vi kan også uttrykket arealet av det blå fargelagte området ved å ta arealet av hele figuren og trekke fra arealene til de grå rektanglene. Da får vi: 

\begin{align*}
\text{Areal} &= a^2 - b(a - b) - b(a - b) - b^2 \\
\\
&= a^2 - ab + b^2 - ab + b^2 - b^2 \\
\\
&= a^2 - 2ab + b^2
\end{align*}

De to arealene må være like, og da får vi 2.kvadratsetning:

$$
(a - b)^2 = a^2 - 2ab + b^2
$$


:::::::::::::::


---

Vi kan bruke 2.kvadratsetning både til å utvide og faktorisere algebraiske uttrykk. La oss se på et eksempel der vi utvider et uttrykk med 2.kvadratsetning:

:::::::::::::::{example} Eksempel 8

Utvid uttrykket nedenfor med 2.kvadratsetning

$$
(2x - 4)^2 
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 2.kvadratsetning:

$$
(\textcolor{red}{2x} - \textcolor{RoyalBlue}{4})^2 = (\textcolor{red}{2x})^2 - 2\cdot \textcolor{red}{2x}\cdot \textcolor{RoyalBlue}{4} + \textcolor{RoyalBlue}{4}^2 = 4x^2 - 16x + 16
$$

::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 8
Bruk 2.kvadratsetning til å utvide uttrykket nedenfor.

$$
(4x - 3)^2
$$

::::{answer}
$$
16x^2 - 24x + 9
$$
::::

::::{solution}
Vi bruker 2.kvadratsetning:

$$
(\textcolor{red}{4x} - \textcolor{RoyalBlue}{3})^2 = (\textcolor{red}{4x})^2 - 2\cdot \textcolor{red}{4x}\cdot \textcolor{RoyalBlue}{3} + \textcolor{RoyalBlue}{3}^2 = 16x^2 - 24x + 9
$$
::::



:::::::::::::::


---

La oss nå se på et eksempel der vi bruker 2.kvadratsetning til å faktorisere et uttrykk:

:::::::::::::::{example} Eksempel 9
Faktoriser uttrykket nedenfor med 2.kvadratsetning

$$
x^2 - 10x + 25
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 2.kvadratsetning baklengs:

$$
x^2 - 10x + 25 = \textcolor{red}{x}^2 - 2 \cdot \textcolor{red}{x} \cdot \textcolor{RoyalBlue}{5} + \textcolor{RoyalBlue}{5}^2 = (\textcolor{red}{x} - \textcolor{RoyalBlue}{5})^2
$$
::::
:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 9
Bruk 2.kvadratsetning til å faktorisere uttrykket nedenfor.

$$
x^2 - 8x + 16
$$

::::{answer}
$$
(x - 4)^2
$$
::::

::::{solution}
Vi bruker 2.kvadratsetning baklengs:

$$
x^2 - 8x + 16 = \textcolor{red}{x}^2 - 2 \cdot \textcolor{red}{x} \cdot \textcolor{RoyalBlue}{4} + \textcolor{RoyalBlue}{4}^2 = (\textcolor{red}{x} - \textcolor{RoyalBlue}{4})^2
$$

::::


:::::::::::::::




### Konjugatsetningen
Den siste kvadratsetningen uttrykker ikke arealet av et kvadrat, men heller arealet av ett kvadrat minus arealet av et annet kvadrat. Vi kaller den for **konjugatsetningen**.

:::::::::::::::{summary} Konjugatsetningen
For to tall $a$ og $b$ gjelder

$$
a^2 - b^2 = (a + b)(a - b)
$$

:::::::::::::::


---

:::::::::::::::{theory} Begrunnelse for konjugatsetningen
I figuren nedenfor vises et kvadrat. Kvadratet er delt opp i mindre rektangler.


:::{figure} ./figurer/bevis/bevis_4/figur_annotert.svg
---
class: no-click, adaptive-figure
width: 
---
:::


Arealet av det fargelagte området kan bestemmes direkte ved å ta arealet av de blå rektanglene:

\begin{align*}
\text{Areal} &= (a - b)^2 + b(a - b) + b(a - b) \\
\\
&= (a - b)^2 + 2b(a - b) \\
\\
&= (a - b)\left((a - b) + 2b\right) \\
\\
&= (a - b)(a + b)
\end{align*}


Arealet av det blå fargelagte området kan også bestemme ved å ta arealet av hele figuren og trekke fra arealet av det blå området: 

$$
\text{Areal} = a^2 - b^2
$$

De to arealene må være like, og da får vi konjugatsetningen:

$$
a^2 - b^2 = (a + b)(a - b)
$$


:::::::::::::::


---


Vi kan bruke konjugatsetningen både til å utvide og faktorisere algebraiske uttrykk. La oss se på et eksempel der vi utvider et uttrykk:


:::::::::::::::{example} Eksempel 10
Bruk konjugatsetningen til å utvide uttrykket nedenfor.

$$
(x + 2)(x - 2)
$$


::::{solution}
---
dropdown: 0
---
$$
(\textcolor{red}{x} + \textcolor{RoyalBlue}{2})(\textcolor{red}{x} - \textcolor{RoyalBlue}{2}) = \textcolor{red}{x}^2 - \textcolor{RoyalBlue}{2}^2 = x^2 - 4
$$
::::
:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 10
Bruk konjugatsetningen til å utvide uttrykket nedenfor.

$$
(x + 5)(x - 5)
$$

::::{answer}
$$
x^2 - 25
$$
::::

::::{solution}
$$
(\textcolor{red}{x} + \textcolor{RoyalBlue}{5})(\textcolor{red}{x} - \textcolor{RoyalBlue}{5}) = \textcolor{red}{x}^2 - \textcolor{RoyalBlue}{5}^2 = x^2 - 25
$$
::::



:::::::::::::::


---

Så kan vi bruke konjugatsetningen til å faktorisere et uttrykk:

:::::::::::::::{example} Eksempel 11
Bruk konjugatsetningen til å faktorisere uttrykket nedenfor.

$$
x^2 - 9
$$

::::{solution}
---
dropdown: 0
---
$$
x^2 - 9 = \textcolor{red}{x}^2 - \textcolor{RoyalBlue}{3}^2 = (\textcolor{red}{x} + \textcolor{RoyalBlue}{3})(\textcolor{red}{x} - \textcolor{RoyalBlue}{3})
$$
::::
:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 11
Bruk konjugatsetningen til å faktorisere uttrykket nedenfor.

$$
x^2 - 1
$$

::::{answer}
$$
(x + 1)(x - 1)
$$
::::

::::{solution}
$$
x^2 - 1 = \textcolor{red}{x}^2 - \textcolor{RoyalBlue}{1}^2 = (\textcolor{red}{x} + \textcolor{RoyalBlue}{1})(\textcolor{red}{x} - \textcolor{RoyalBlue}{1})
$$
::::
:::::::::::::::


## 2.Distributiv lov

Den 2.distributive loven er ikke så enkel å bruke til å faktorisere, men den lar oss utvide algebraiske uttrykk der vi ganger sammen to parenteser. 

:::::::::::::::{summary} 2.Distributiv lov
For tall $a$, $b$, $c$ og $d$ gjelder

$$
(a + b)(c + d) = ac + ad + bc + bd
$$
:::::::::::::::


---

:::::::::::::::{theory} Begrunnelse for 2.distributiv lov
Nedenfor vises et rektangel. Rektangelet er delt opp i mindre rektangler.

Bruk arealberegninger til å bestemme arealet av figuren på to forskjellige måter og vis at 2.distributiv lov stemmer.

:::{figure} ./figurer/bevis/bevis_5/figur_annotert.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

Vi ser at hele rektangelet har sidelengder $(a + b)$ og $(c + d)$. Arealet av hele rektangelet kan derfor bestemmes direkte ved å gange sidelengdene:

$$
\text{Areal} = (a + b)(c + d)
$$

Hele rektangelet er bygget opp av fire mindre rektangeler:
* Et rektangel med sidelengder $a$ og $c$ som har areal $ac$.
* Et rektangel med sidelengder $a$ og $d$ som har areal $ad$.
* Et rektangel med sidelengder $b$ og $c$ som har areal $bc$.
* Et rektangel med sidelengder $b$ og $d$ som har areal $bd$.


Arealet av hele rektangelet kan derfor også bestemmes ved å legge sammen arealene til de fire mindre rektanglene:

$$
\text{Areal} = ac + ad + bc + bd
$$

De to arealene må være like, og da får vi 2.distributiv lov:

$$
(a + b)(c + d) = ac + ad + bc + bd
$$

:::::::::::::::


---

La oss se på et eksempel der vi bruker 2.distributiv lov til å utvide et uttrykk:

:::::::::::::::{example} Eksempel 12
Utvid uttrykket nedenfor med 2.distributiv lov

$$
(2x + 3)(x - 4)
$$

::::{solution}
---
dropdown: 0
---
Vi bruker 2.distributiv lov:

\begin{align*}
(2x + 3)(x - 4) &= 2x\cdot x + 2x\cdot (-4) + 3\cdot x + 3\cdot (-4) \\
\\
&= 2x^2 - 8x + 3x - 12\\
\\
& = 2x^2 - 5x - 12
\end{align*}
::::
:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 12
Utvid uttrykket nedenfor.

$$
(3x + 2)(x + 5)
$$


::::{answer}
$$
3x^2 + 17x + 10
$$
::::


::::{solution}
\begin{align*}
(3x + 2)(x + 5) &= 3x\cdot x + 3x\cdot 5 + 2\cdot x + 2\cdot 5 \\
\\
&= 3x^2 + 15x + 2x + 10\\
\\
& = 3x^2 + 17x + 10
\end{align*}
::::

:::::::::::::::







