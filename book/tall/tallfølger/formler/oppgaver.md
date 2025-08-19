# Oppgaver: Formler


:::{margin} Tips: Oppgave 1c
Når det står "Bestem $S_n$" så mener vi at du skal finne en formel for $S_n$ som gjelder for alle naturlige tall $n$.
:::

:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Nedenfor vises noen figurer som følger et bestemt mønster. Vi tenker oss at figurene fortsetter etter samme mønster. 

La $S_n$ være antall sirkler i figur $n$. 

:::{figure} ./figurer/oppgaver/oppgave_1/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts 
---
:::::::::::::{tab-item} a
Bestem verdien til $S_1$, $S_2$ og $S_3$ fra figurene. 

::::{answer}
$$
S_1 = 4 \qog S_2 = 8 \qog S_3 = 12
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $S_4$. 

::::{answer}
$$
S_4 = 16
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $S_n$. 

::::{answer}
$$
S_n = 4n \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Hvilken figur har $120$ sirkler? 

::::{answer}
Figur $30$ har $120$ sirkler siden $S_{30} = 4 \cdot 30 = 120$.
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Nedenfor vises noen figurer som følger et bestemt mønster. Vi tenker oss at figurene fortsetter etter samme mønster. 

La $S_n$ være antall fargelagte kvadrater i figur $n$.


:::{figure} ./figurer/oppgaver/oppgave_2/figur_4n_plus_2.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem verdien til $S_1$, $S_2$, $S_3$ og $S_4$ fra figurene.

::::{answer}
$$
S_1 = 6 \qog S_2 = 10 \qog S_3 = 14 \qog S_4 = 18
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $S_n$. 

::::{answer}
$$
S_n = 4n + 2 \qder n \in \mathbb{N}
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
Hvilken figur har $82$ sirkler?


::::{answer}
Figur $20$ har $82$ sirkler siden $S_{20} = 4 \cdot 20 + 2 = 82$.
::::

:::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
---
level: 2
---
Nedenfor vises noen figurer som følger et bestemt mønster. Vi tenker oss at figurene fortsetter etter samme mønster. 

La $R_n$ være antall prikker i figur $n$.


:::{figure} ./figurer/oppgaver/oppgave_3/figur_rektangulære.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem verdien til $R_5$. 

::::{answer}
$$
R_5 = 30
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem et uttrykk for $R_n$. 


::::{answer}
$$
R_n = n(n + 1) \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
La $T_n$ være antall prikker i figur $n$ som er blå. 

Bestem en formel for $T_n$. 

::::{answer}
$$
T_n = \dfrac{R_n}{2} = \dfrac{n(n + 1)}{2} \qder n \in \mathbb{N}
$$
::::
:::::::::::::

::::::::::::::
:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 4
Nedenfor vises de tre første figurene i en figurfølge. Figurene tenker oss at figurene følger dette mønsteret videre.

La $K_n$ være antall kvadrater i figur $n$.


:::{figure} ./figurer/oppgaver/oppgave_4/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $K_1$, $K_2$ og $K_3$. 




::::{answer}
$$
K_1 = 2 \and K_2 = 6 \and K_3 = 12
$$
::::



:::::::::::::



:::::::::::::{tab-item} b
Bestem $K_4$. 


::::{answer}
$$
K_4 = 20
$$
::::

::::{solution}
$$
K_4 = 5 \cdot 4 = 20
$$
::::

:::::::::::::



:::::::::::::{tab-item} c
Bestem $K_n$.


::::{answer}
$$
K_n = n(n + 1) \qder n \in \mathbb{N}
$$
::::

::::{solution}
Vi kan se et mønster i figurene som at

$$
K_1 = 2 \cdot 1 \and K_2 = 3 \cdot 2 \and K_3 = 4 \cdot 3
$$

Vi kan se at det er $n$ rader og $(n + 1)$ kolonner i figur $n$ ut ifra mønsteret, som betyr at formelen for $K_n$ er

$$
K_n = (n + 1) \cdot n = n(n + 1) \qder n \in \mathbb{N}
$$
::::


:::::::::::::



::::::::::::::


:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 5
Nedenfor vises noen figurer som følger et bestemt mønster. Vi tenker oss at figurene fortsetter etter samme mønster. 

La $F_n$ være antall fargelagte firkanter i figur $n$.


:::{figure} ./figurer/oppgaver/oppgave_5/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $F_1$, $F_2$ og $F_3$ fra figurene.


::::{answer}
$$
F_1 = 2 \and F_2 = 12 \and F_3 = 30
$$
::::


::::{solution}
$$
F_1 = 1 \cdot 2 = 2 \and F_2 = 3 \cdot 4 = 12 \and F_3 = 5 \cdot 6 = 30
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $F_4$.


::::{answer}
$$
F_4 = 56
$$
::::

::::{solution}
$$
F_4 = 7 \cdot 8 = 56
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Lag en formel $F_n$ for antall fargelagte firkanter i figur $n$.


::::{answer}
$$
F_n = 2n\cdot (2n - 1) \qder n \in \mathbb{N}
$$
::::


::::{solution}
Vi kan systematisere mønsteret i antall rader og kolonner: 


| Figur $n$ | Antall rader | Antall kolonner |
|:-----------:|:---------------:|:-----------------:|
| $1$ | $2$ | $1$ |
| $2$ | $4$ | $3$ |
| $3$ | $6$ | $5$ |
| $4$ | $8$ | $7$ |


Vi kan se at antall rader passer med partall $2n$ og antall kolonner passer med oddetallne $2n - 1$.

Dermed får vi formelen for $F_n$:

$$
F_n = 2n\cdot (2n - 1) \qder n \in \mathbb{N}
$$


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6
Nedenfor vises de tre første figurene i en figurfølge. Figurene tenker oss at figurene følger dette mønsteret videre.

La $K_n$ være antall kvadrater i figur $n$.


:::{figure} ./figurer/oppgaver/oppgave_6/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem verdiene til $K_1$, $K_2$ og $K_3$ fra figurene.


::::{answer}
$$
K_1 = 12 \and K_2 = 32 \and K_3 = 60
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $K_4$.


::::{answer}
$$
K_4 = 96
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem en formel for $K_n$. 


::::{answer}
$$
K_n = 4(n + 1)^2 - 4
$$
::::


:::::::::::::


::::::::::::::


:::::::::::::::





---



:::::::::::::::{exercise} Oppgave 7
Nedenfor vises noen figurer som følger et bestemt mønster. Vi tenker oss at figurene fortsetter etter samme mønster.

Vi lar $K_n$ være antall fargelagte kvadrater i figur $n$.

:::{figure} ./figurer/oppgaver/oppgave_7/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem verdien til $K_1$, $K_2$ og $K_3$ fra figurene.


::::{answer}
$$
K_1 = 4 \and K_2 = 9 \and K_3 = 16
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Bestem $K_4$.

::::{answer}
$$
K_4 = 25
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem en formel for $K_n$. 


::::{answer}
$$
K_n = n^2 + 2n + 1 = (n + 1)^2 \qder n \in \mathbb{N}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 8
Nedenfor vises de tre første figurene i en figurfølge. Figurene tenker oss at figurene følger dette mønsteret videre.

La $F_n$ være antall firkanter i figur $n$.


:::{figure} ./figurer/oppgaver/oppgave_8/figur_katt.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $F_1$, $F_2$ og $F_3$ fra figurene.


::::{answer}
$$
F_1 = 5 \and F_2 = 13 \and F_3 = 25
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
Bestem $F_4$.


::::{answer}
$$
F_4 = 41
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $F_n$. 



::::{answer}
$$
F_n = 2n^2 + 2n + 1 \qfor n \in \mathbb{N}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 9
Nedenfor vises noen figurer som følger et bestemt mønster. Vi tenker oss at figurene fortsetter i samme mønster. 

La $S_n$ være antall sirkler i figur $n$.

:::{figure} ./figurer/oppgaver/oppgave_9/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Bestem $S_1$, $S_2$ og $S_3$ fra figurene.


::::{answer}
$$
S_1 = 4 \and S_2 = 13 \and S_3 = 28
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Bestem $S_4$. 


::::{answer}
$$
S_4 = 49
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $S_n$. 



::::{answer}
$$
S_n = 3n^2 + 1 \qfor n \in \mathbb{N}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
---
level: 2
---
En tallfølge $a_n$ er gitt ved 

$$
4, 7, 10, 13, \ldots
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem det neste leddet i tallfølgen.


::::{answer}
Neste ledd i tallfølgen er $16$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem en formel for $a_n$. 

::::{answer}
$$
a_n = 3n + 1 \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Hvilket ledd i tallfølgen har verdien $100$? 

::::{answer}
Leddet $n = 33$ har verdien $100$ siden $a_{33} = 3 \cdot 33 + 1 = 100$.
::::

:::::::::::::
::::::::::::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 11
---
level: 2
---
I denne oppgave skal du bestemme formlene til tallfølger.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En tallfølge $a_n$ er gitt ved 

$$
-1, 1, 3, 5, \ldots
$$

Bestem en formel for $a_n$. 

::::{answer}
$$
a_n = 2n - 3 \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
En tallfølge $b_n$ er gitt ved 

$$
6, 11, 16, 21, \ldots
$$

Bestem en formel for $b_n$. 


::::{answer}
$$
b_n = 5n + 1 \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En tallfølge $c_n$ er gitt ved 

$$
0, 3, 8, 15, \ldots
$$

Bestem en formel for $c_n$. 

::::{answer}
$$
c_n = n^2 - 1 \qder n \in \mathbb{N}
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::{margin} Tips til oppgave 12
$1 = (-1)^2 = (-1)^4 = (-1)^6 = \ldots$

og 

$-1 = (-1)^3 = (-1)^5 = (-1)^7 = \ldots$
:::


:::::::::::::::{exercise} Oppgave 12
---
level: 3
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En tallfølge $a_n$ er gitt ved 

$$
1, -2, 4, -6, 8, -10, \ldots
$$

Bestem en formel for $a_n$. 

::::{answer}
$$
a_n = (-1)^{n+1} \cdot 2n \qder n \in \mathbb{N}
$$
::::


:::::::::::::

:::::::::::::{tab-item} b
En tallfølge $b_n$ er gitt ved 

$$
-1, 4, -9, 16, -25, \ldots
$$

Bestem en formel for $b_n$. 


::::{answer}
$$
b_n = (-1)^n \cdot n^2 \qder n \in \mathbb{N}
$$
::::


:::::::::::::

:::::::::::::{tab-item} c
En tallfølge $c_n$ er gitt ved 

$$
1, -3, 5, -7, 9, -11, \ldots
$$

Bestem en formel for $c_n$. 


::::{answer}
$$
c_n = (-1)^{n+1} \cdot (2n - 1) \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
En tallfølge $d_n$ er gitt ved

$$
1, -\dfrac{1}{2}, \dfrac{1}{4}, -\dfrac{1}{8}, \dfrac{1}{16}, \ldots
$$

Bestem en formel for $d_n$. 


::::{answer}
$$
d_n = \dfrac{(-1)^{n+1}}{2^{n-1}} \qder n \in \mathbb{N}
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::

