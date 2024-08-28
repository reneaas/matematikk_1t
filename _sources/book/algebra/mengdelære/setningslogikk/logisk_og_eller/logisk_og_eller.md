## Logisk *og* - og logisk *eller*

Ofte ønsker vi å sette sammen påstander for å lage nye mer sammensatte påstander. Dette kan vi gjøre ved hjelp av såkalt logisk *og* - og logisk *eller*.

### Logisk *eller*

Logisk *eller* brukes når en av to påstander er sanne, eller begge.

:::{admonition} Definisjon: logisk *eller*
---
class: theory
---
La $p$ og $q$ være to påstander. Da kan vi lage oss en ny påstand ved å skrive 

$$
p \lor q
$$

som betyr at enten så er $p$ sann, eller så er $q$ sann, eller så begge er sanne.
:::

Vi tar et eksempel som vi kommer til å se gjentatte ganger senere:

::::{admonition} Eksempel 5: logisk *eller*
---
class: example
---
En spesiell type andregradslikning som dukker opp i blant kan vi løse ved å "gjette" på svare. Vi ser på likningen

$$
(x - 1)\cdot(x + 2) = 0.
$$

Hvis vi prøver å sette inn $x = 1$ så får vi 

$$
(1 - 1) \cdot (1 + 2) = 0 \cdot 3 = 0,
$$

så vi ser at $x = 1$ er en løsning. Hvis vi prøver å sette inn $x = -2$ så får vi

$$
(-2 - 1) \cdot (-2 + 2) = -3 \cdot 0 = 0,
$$

så vi ser at $x = -2$ er en løsning også. 

Formelt sett kan vi da uttrykke at påstanden 

$$
(x - 1)\cdot (x + 2) = 0
$$

er sann *hvis og bare hvis* $x = 1$ eller $x = -2$. Matematisk skriver vi dette som

$$
x = 1 \, \lor \, x = -2.
$$
::::


### Logisk *og*

Logisk *og* bruker vi når vi skal kombinere to påstander sammen, der begge to må være sanne samtidig. 

:::{admonition} Logisk *og*
---
class: theory
---
La $p$ og $q$ være to påstander. Da kan vi lage oss en ny påstand ved å skrive

$$
p \land q
$$

som uttrykker at $p$ og $q$ må være sanne *samtidig*. Vi leser gjerne $p \land q$ som $p$ er sann *og samtidig* er $q$ sann.
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

Når vi løser et likningssystem, så er vi ute etter å bestemme $x$ og $y$ slik at begge likningene er oppfylt samtidig - altså at begge likninger er sanne påstander. Bruker vi logisk *og* for å uttrykke dette, kan vi skrive:

$$
x + y = 1 \, \land \, x - y = 3.
$$

Løsningen viser seg å være $x = 2$ og $y = -1$ (du kan sjekke ved å plugge inn verdiene i begge likninger). Dermed kan vi uttrykke løsningen som

$$
x = 2 \, \land \, y = -1.
$$

Vi bruker er logisk *og* - ikke logisk *eller* - fordi 
::::