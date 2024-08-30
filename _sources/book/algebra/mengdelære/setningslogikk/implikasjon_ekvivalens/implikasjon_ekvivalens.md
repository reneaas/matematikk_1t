## Implikasjon og Ekvivalens

Ofte er det en sammenheng mellom to påstander. Noen ganger vil en sann påstand medføre at en annen påstand er sann, andre ganger vil de begge medføre at den andre er sann samtidig. Vi har to måter å uttrykke slike sammenhenger på: 


### Implikasjon

:::{admonition} Vanlige symboler for påstander
---
class: sidenote, margin
---
Det er vanlig å bruke symbolene $P$ og $Q$ for påstander. 
:::

:::{admonition} Implikasjon
---
class: theory
---
La $P$ og $Q$ være to påstander. Hvis det er slik at når $P$ er sann, så er automatisk $Q$ sann, sier vi at $P$ **impliserer** $Q$. 

Vi skriver

$$
P \Rightarrow Q
$$

Hvis $P$ *ikke* impliserer $Q$, skriver vi $P \not \Rightarrow Q$.
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

Hvis $P$ er sann, så er også $Q$ sann. Derfor kan vi skrive $P \Rightarrow Q$, eller mer eksplisitt:

$$
\text{Kari bor i Oslo} \quad \Rightarrow \quad \text{Kari bor i Norge}.
$$


Det motsatte er ikke tilfellet, for hvis Kari bor i Norge, kan hun bo mange andre steder enn Oslo. Dermed har vi at 

$$
\text{Kari bor i Oslo} \quad \not \Leftarrow \quad \text{Kari bor i Norge}.
$$


Her kan vi merke oss at vi kan skrive implikasjonspilen mot venstre også. Når det *ikke* er en implikasjon, skriver vi en strek gjennom pilen. Pilen leses da som "impliserer ikke".
:::

Vi tar et eksempel som er mer matematisk orientert:

:::{admonition} Eksempel 3: implikasjon
---
class: example
---
Vi tenker oss to påstander:

| Påstand $P$ | Påstand $Q$ |
|:-----------:|:-----------:|
| $x = 4$ | $x^2 = 16$ |

<br>

Hvis $P$ er sann, så er også $Q$ sann siden $4^2 = 16$. Derfor kan vi skrive at 

$$
x = 4 \quad \Rightarrow \quad x^2 = 16.
$$

Men hvis $x^2 = 16$, kan også $x = -4$ være tilfellet. Derfor er det ikke sånn at hvis $x^2 = 16$ er sant, så er også $x = 4$ sant. Dermed kan vi også skrive at 

$$
x^2 = 16 \quad \not \Rightarrow \quad x = 4.
$$
:::


::::{admonition} Underveisoppgave 1
---
class: check
---
Skriv av og fyll ut tabellen: 

| Påstand $P$ |  $\Leftarrow$ eller $\Rightarrow$| Påstand $Q$ |
|:-----------:|:----------------------------------:|:-----------:|
| $x = 3$ |  | $x^2 = 9$ |
| $y \in \langle -3, 5 \rangle$ |  | $y \in \langle -4, 6\rangle$ |
|$y \in \langle -4, 6\rangle$|  |$y \in [-4, 6 ]$|
| $z = 2$ |  | $z \in \mathbb{N}$ |
| $r \in \mathbb{Z}$ |  | $r \in \mathbb{Q}$ |
| $s \in \mathbb{R}$ |  | $s \in \mathbb{Q}$ |
| $t \in \mathbb{N}$ |  | $t \in \mathbb{Z}$ |

:::{admonition} Fasit
---
class: answer, dropdown
---
| Påstand $P$ |  $\Leftarrow$ eller $\Rightarrow$| Påstand $Q$ |
|:-----------:|:----------------------------------:|:-----------:|
| $x = 3$ |  $\Rightarrow$ | $x^2 = 9$ |
| $y \in \langle -3, 5 \rangle$ | $\Leftarrow$ | $y \in \langle -4, 6\rangle$ |
|$y \in \langle -4, 6\rangle$| $\Leftarrow$ |$y \in [-4, 6]$|
| $z = 2$ |  $\Rightarrow$ | $z \in \mathbb{N}$ |
| $r \in \mathbb{Z}$ | $\Rightarrow$ | $r \in \mathbb{Q}$ |
| $s \in \mathbb{R}$ | $\Leftarrow$ | $s \in \mathbb{Q}$ |
| $t \in \mathbb{N}$ | $\Rightarrow$ | $t \in \mathbb{Z}$ |
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
P \Leftrightarrow Q
$$

Vi leser dette som "$P$ er sann hvis og bare hvis $Q$ er sann".
::::


Vi tar et eksempel:

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
Vi har to påstander $P$ og $Q$ som følger:

| Påstand $P$ | Påstand $Q$ |
|:-----------:|:-----------:|
| $\|x\| = 4$ | $x^2 = 16$ |

<br>

Vi kan merke oss at $|x| = 4$ er sann hvis og bare hvis $x = 4$ eller $x = -4$. Men det samme er sant for $x^2 = 16$. Derfor har vi at påstand $P$ er kun sann hvis $Q$ er sann, og motsatt. Men da betyr dette at de to påstandene er ekvivalente. Derfor kan vi skrive at 

$$
|x| = 4 \quad \Leftrightarrow \quad x^2 = 16.
$$

::::

Så er det **din tur**!

::::{admonition} Underveisoppgave 2
---
class: check
---
Fyll ut tabellen under med $\Leftrightarrow$, $\Leftarrow$ eller $\Rightarrow$ slik at hver rad blir en sann påstand.

| Påstand $P$ |  $\Leftrightarrow$, $\Leftarrow$ eller $\Rightarrow$ | Påstand $Q$ |
|:-----------:|:-------------------------------------------------------:|:-----------:|
| $x = 3$ |  | $x^2 = 9$ |
| $x = -2$ eller $x = 2$ |  | $x^2 = 4$ |
| $x^2 = 25$ |  | $x = -5$ |
| $\|x\| = 3$ |  | $x = 3$ eller $x = -3$ |
| $-2 < x < 3$ | | $x \in \langle -2, 3 \rangle$ |
| $x = -5$ |  | $\|x\| = 5$ |

:::{admonition} Fasit
---
class: answer, dropdown
---
| Påstand $P$ |  $\Leftrightarrow$, $\Leftarrow$ eller $\Rightarrow$ | Påstand $Q$ |
|:-----------:|:-------------------------------------------------------:|:-----------:|
| $x = 3$ |  \Rightarrow | $x^2 = 9$ |
| $y \in \langle -3, 5 \rangle$ | \Leftrightarrow | $y \in \langle -4, 6\rangle$ |
|$y \in \langle -4, 6\rangle$| \Leftarrow |$y [-4, 6]$|
| $z = 2$ |  \Rightarrow | $z \in \mathbb{N}$ |
| $r \in \mathbb{Z}$ | \Leftrightarrow | $r \in \mathbb{Q}$ |
| $s \in \mathbb{R}$ | \Leftrightarrow | $s \in \mathbb{Q}$ |
| $t \in \mathbb{N}$ | \Rightarrow | $t \in \mathbb{Z}$ |
:::
::::



