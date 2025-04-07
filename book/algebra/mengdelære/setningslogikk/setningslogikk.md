# Setningslogikk

:::{admonition} Læringsmål: setningslogikk
---
class: tip
---
* Kunne forklare hva en påstand er i matematikken.
* Kunne forklare begrepene *implikasjon* og *ekvivalens*, og bruke disse for å uttrykke sammenhenger mellom påstander.
* Kunne forklare begrepene *logisk og*, og *logisk eller*, og bruke disse for å uttrykke sammensatte påstander.
* Kunne bruke matematisk notasjon for implikasjon, ekvivalens, logisk *og* - og logisk *eller*.
:::

Setningslogikk handler om å uttrykke påstander på en presis måte. Vi skal introdusere et par nyttige begreper og skrivemåter som vi kommer til å bruke mye.

## Påstander

En **påstand** i matematikken kan ofte beskrives som en likning eller en ulikhet. En påstand kan være usann, men vi skal alltid anta at en påstand er sann og utvikle teori der vi beskriver sanne påstander.

:::{admonition} Eksempel 1: påstander i matematikken
---
class: example
---
La oss se på noen eksempler på påstander i matematikken:

| Påstand | Beskrivelse |
| :---: | :--- |
| $2x + 1 = 3$ | $2x + 1$ er lik $3$. |
| $x > 4$ |  $x$ er større enn 4. |
| $x \in [1, 2]$ | $x$ er et tall i intervallet $[1, 2]$. |
| $x \in \mathbb{N}$ | $x$ er et naturlig tall. |
| $x \in \mathbb{R}$ | $x$ er et reelt tall. |
:::


---

## Implikasjon og ekvivalens

Noen ganger er det en logisk sammenheng mellom to påstander. Hvis en påstand er sann og dette gjør at en annen påstand også må være sann, kaller vi det for en **implikasjon**. Hvis det derimot er slik at begge påstandene må være sanne for at den ene skal være sann, snakker vi om **ekvivalens**.


### Implikasjon

:::{admonition} Hva med motsatt?
---
class: sidenote, margin
---

Hvis $P$ impliseres *av* $Q$, kan vi skrive pilen motsatt vei:

$$
P \impliedby Q
$$

eller bare skrive

$$
Q \implies P
$$
:::

:::{admonition} Implikasjon
---
class: theory
---
La oss si $P$ og $Q$ er to påstander. Hvis det er slik at når $P$ er sann, så betyr dette automatisk også at $Q$ er sann, sier vi at $P$ **impliserer** $Q$. 

Da skriver vi:

$$
P \implies Q
$$

som vi leser som "hvis $P$ er sann, så er $Q$ sann" - eller bare "hvis $P$, så $Q$". 
:::

Vi går løs på et eksempel:

:::{admonition} Eksempel 2: implikasjon
---
class: example
---
To har to påstander som følger:

Vi har to påstander $P$ og $Q$ som følger:

$$
P = \text{Kari bor i Oslo} \quad \text{og} \quad Q = \text{Kari bor i Norge}.
$$

Vi kan være enig om at hvis Kari bor i Oslo, så bor hun også i Norge. Derfor må det være slik at hvis $P$ er sann, så er $Q$ også sann. Derfor kan vi skrive

$$
\text{Kari bor i Oslo} \implies \text{Kari bor i Norge}.
$$


Det motsatte er ikke tilfellet. Hvis Kari bor i Norge, kan hun bo mange andre steder enn Oslo. Derfor er *ikke* slik at hvis $Q$ er sann, så er også nødvendigvis $P$ sann. Vi skriver dette som

$$
\text{Kari bor i Norge} \quad \not\!\!\!\!\implies \quad \text{Kari bor i Oslo}
$$

Vi slenger altså en skråstrek gjennom pilen hvis vi vil uttrykke at implikasjonen ikke gjelder.
:::

Vi tar noen eksempler som er litt mer matematiske:

:::{admonition} Eksempel 3: implikasjon
---
class: example
---
Under vises noen påstander $P$ og $Q$. Her vises vi noen eksempler hvor $P \implies Q$, og noen hvor $P \impliedby Q$.

| Påstand $P$ |  | Påstand $Q$ |  Forklaring |
|:---:|:---:|:---:|:---|
| $x = 2$ | $\implies$ | $x \in \{1, 2, 5\}$ | Hvis $x = 2$, så er $x$ også et element i mengden $\{1, 2, 5\}$. |
| $n \in \mathbb{N}$ | $\implies$ | $n \in \mathbb{Z}$ | Hvis $n$ er et naturlig tall, er det også et heltall. |
| $x > 3$ | $\impliedby$ | $x > 6$ | Hvis $x$ er større enn $6$, må også $x$ være større enn $3$ siden $6 > 3$. |
| $x \in \langle -10, 10 \rangle$ | $\impliedby$ | $x \in \langle -5, 5 \rangle$ | Hvis $x$ ligger mellom $-5$ og $5$, ligger $x$ også mellom $-10$ og $10$. |


<br>

Legg merke til at implikasjonene i tabellen over ikke går motsatt vei. For eksempel er det ikke slik at hvis $x \in \{1, 2, 5\}$, så må ikke $x = 2$ siden $x$ kan også være en av de to andre tallene i mengden.

:::

Så er det **din tur**!

::::{admonition} Underveisoppgave 1
---
class: check
---
Fyll ut tabellen under med $\impliedby$ eller $\implies$ for å uttrykke den logiske sammenhengen mellom påstandene. 

| Påstand $P$ |  $\impliedby$ eller $\implies$| Påstand $Q$ |
|:-----------:|:----------------------------------:|:-----------:|
| $m = -2$ | | $m \in \mathbb{Z}$ |
| $n \in \mathbb{R}$ | | $n \in \mathbb{Q}$ |
| $x < -2$ | | $x < 0$ |
| $x \in \langle -4, 6 \rangle$ | | $x \in \langle -3, 5 \rangle$|
| $-1 \leq x \leq 1$  |  | $-3 < x < 3$ |

:::{admonition} Fasit
---
class: answer, dropdown
---

| Påstand $P$ |  $\impliedby$ eller $\implies$| Påstand $Q$ |
|:-----------:|:----------------------------------:|:-----------:|
| $m = -2$ | $\implies$ | $m \in \mathbb{Z}$ |
| $n \in \mathbb{R}$ | $\impliedby$ | $n \in \mathbb{Q}$ |
| $x < -2$ | $\implies$ | $x < 0$ |
| $x \in \langle -4, 6 \rangle$ | $\impliedby$ | $x \in \langle -3, 5 \rangle$|
| $-1 \leq x \leq 1$  | $\implies$ | $-3 < x < 3$ |
:::
::::

### Ekvivalens

::::{admonition} Ekvivalens
---
class: theory
---
La $P$ og $Q$ være to påstander. Hvis det er slik at $P$ er sann bare hvis $Q$ er sann, og $Q$ er sann bare hvis $P$ er sann, så sier vi at $P$ og $Q$ er **ekvivalente** påstander.
Vi skriver

$$
P \iff Q
$$

Vi leser dette som "$P$ er sann hvis og bare hvis $Q$ er sann". Sammenhengen med implikasjon er at både

$$
P \implies Q \quad \text{og} \quad P \impliedby Q
$$
::::


Vi tar et eksempel der noen påstander er ekvivalente, mens andre kun impliserer den éne veien.

:::{admonition} Absoluttverdien
---
class: sidenote, margin
---
En mye brukt størrelse i matematikken kalles for **absoluttverdien** av et tall $x$ og skrives som $|x|$. Absoluttverdien av et tall er avstanden fra $0$ til tallet på tallinjen. Vi kan se det som at vi bare "tar bort" fortegnet. For eksempel er $|-4| = 4$ og $|4| = 4$.
:::

::::{admonition} Eksempel 4: ekvivalens
---
class: example
---
Under vises noen påstander $P$ og $Q$. I noen tilfeller er påstandene ekvivalente, i andre tilfeller er det bare implikasjon én vei.

| Påstand $P$ |  | Påstand $Q$ |  Forklaring |
|:---:|:---:|:---:|:---|
| $x \in \{-2, 2\}$ | $\iff$ | $x^2 = 4$ | Hvis $x$ er enten $-2$ eller $2$, så er $x^2 = 4$. Og motsatt, hvis $x^2 = 4$, så må $x$ være enten $-2$ eller $2$. |
| $x = 3$ | $\implies$ | $x^2 = 9$ | $x = -3$ kan også være tilfellet når $x^2 = 9$. Derfor er ikke påstandene ekvivalente. |
| $-2 < x < 2$ | $\iff$ | $x \in \langle -2, 2 \rangle$ | To måter å skrive akkurat det samme på. | 
| $x^2 > 0 $ | $\impliedby$ | $x > 0$ | $x^2 > 0$ når $x < 0$ også. Derfor er ikke påstandene ekvivalente. |

::::

Så er det **din tur**!

::::{admonition} Underveisoppgave 2
---
class: check
---
Fyll ut tabellen under med $\iff$, $\impliedby$ eller $\implies$ slik at sammenhengene mellom påstandene stemmer.

| Påstand $P$ |  $\iff$, $\impliedby$ eller $\implies$ | Påstand $Q$ |
|:-----------:|:-------------------------------------------------------:|:-----------:|
| $x = 5$ |  | $x^2 = 25$ |
| $x \in \{-3, 3\}$ |  | $\|x\| = 3$ |
| $x^2 = 25$ |  | $x = -5$ |
| $x^3 > 0$ | | $x > 0$ | 
| $-2 < x < 3$ | | $x \in \langle -2, 3 \rangle$ |
| $x > 2$ |  | $x\in [2, \to \rangle$ |

:::{admonition} Fasit
---
class: answer, dropdown
---
| Påstand $P$ |  $\iff$, $\impliedby$ eller $\implies$ | Påstand $Q$ |
|:-----------:|:-------------------------------------------------------:|:-----------:|
| $x = 5$ | $\implies$ | $x^2 = 25$ |
| $x \in \{-3, 3\}$ | $\iff$ | $\|x\| = 3$ |
| $x^2 = 25$ | $\impliedby$ | $x = -5$ |
| $x^3 > 0$ | $\iff$ | $x > 0$ | 
| $-2 < x < 3$ | $\iff$ | $x \in \langle -2, 3 \rangle$ |
| $x > 2$ | $\implies$ | $x \in [2, \to \rangle$ |
:::
::::





---

## Logisk *og* – logisk *eller*

Ofte ønsker vi å sette sammen påstander for å lage nye mer sammensatte påstander. Dette kan vi gjøre ved hjelp av såkalt logisk *og* - og logisk *eller*.

### Logisk *eller*

Logisk *eller* brukes når en av to påstander er sanne, eller begge.

:::{admonition} Definisjon: logisk *eller*
---
class: theory
---
La $P$ og $Q$ være to påstander. Da kan vi lage oss en ny påstand ved å skrive 

$$
P \lor Q
$$

som betyr at enten så er $P$ sann, eller så er $Q$ sann, eller så er begge sanne. 

Vi leser $P \lor Q$ som "$P$ er sann *eller* $Q$ er sann".
:::

Vi tar et eksempel som vi kommer til å se gjentatte ganger senere:

::::{admonition} Eksempel 5: logisk *eller*
---
class: example
---
En spesiell type andregradslikning som dukker opp i blant kan vi løse ved å "gjette" på svaret. Vi ser på likningen

$$
(x - 1)\cdot(x + 2) = 0.
$$

Hvis vi prøver å sette inn $x = 1$ får vi 

$$
(1 - 1) \cdot (1 + 2) = 0 \cdot 3 = 0,
$$

så vi ser at $x = 1$ er en løsning. Hvis vi prøver å sette inn $x = -2$ får vi

$$
(-2 - 1) \cdot (-2 + 2) = -3 \cdot 0 = 0,
$$

så vi ser at $x = -2$ er en løsning også. 

Formelt sett kan vi da uttrykke at påstanden 

$$
(x - 1)\cdot (x + 2) = 0,
$$

er sann *hvis og bare hvis* 

$$
x = 1 \quad \text{eller} \quad x = -2.
$$

Matematisk skriver vi dette som

$$
x = 1 \quad \lor \quad x = -2.
$$

Vi kan derfor tenke på symbolet som

$$
\lor = \text{"eller"}.
$$
::::


### Logisk *og*

Logisk *og* bruker vi når vi skal kombinere to påstander sammen, der begge to må være sanne samtidig. 

:::{admonition} Logisk *og*
---
class: theory
---
La $P$ og $Q$ være to påstander. Da kan vi lage oss en ny påstand ved å skrive

$$
P \land Q
$$

som uttrykker at $P$ og $Q$ må være sanne *samtidig*. 

Vi leser $P \land Q$ som "$P$ er sann *og samtidig* er $Q$ sann".
:::

Vi tar et eksempel på en typisk tilfelle der vi får bruk for dette:

::::{admonition} Eksempel 6: logisk *og*
---
class: example
---

Et likningssystem er gitt ved 

\begin{align*}
    x + y &= 1 \\
    x - y &= 3
\end{align*}

Når vi løser et likningssystem, så er vi ute etter å bestemme $x$ og $y$ slik at begge likningene er oppfylt samtidig - altså at begge likninger er sanne påstander. Altså mener vi egentlig at vi er ute etter å bestemme $x$ og $y$ slik at

$$
x + y = 1 \quad \text{og samtidig} \quad x - y = 3.
$$

Løsningen viser seg å være

$$
x = 2 \quad \text{og samtidig} \quad y = -1.
$$

Matematisk skriver vi:

$$
x = 2 \quad \land \quad y = -1.
$$

Vi tenker derfor på symbolet for logisk *og* som

$$
\land = \text{"og samtidig"}.
$$
::::