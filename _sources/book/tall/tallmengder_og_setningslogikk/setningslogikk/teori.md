# Matematisk logikk og symboler


:::{goals} Læringsmål
* Kunne bruke symbolene for implikasjon og ekvivalens for å uttrykke logiske sammenhenger mellom påstander.
* Kunne bruke symbolene for *logisk-og* og *logisk-eller* for å uttrykke logiske sammenhenger mellom påstander.
:::

For å gjøre det enklere å skrive matematikk, er det nyttig å innføre noen symboler som beskriver logiske sammenhenger mellom påstander. En **påstand** i matematikk kan for eksempel være en likning eller en ulikhet. 


## Ekvivalens og implikasjon
Hvis en påstand sin sannhet automatisk betyr at en annen påstand også er sann, sier vi at den første påstanden **impliserer** den andre. 


:::::::::::::::{summary} Implikasjon
Hvis en påstand $P$ impliserer en annen påstand $Q$, skriver vi dette som $P \implies Q$. Vi leser dette som "hvis $P$ er sann, så er $Q$ sann". 
:::::::::::::::


Vi tar et litt konkret eksempel. 


:::{margin} Symbolet $\nimplies$
Symbolet leses som "impliserer ikke". Når vi vil uttrykke at noe *ikke* stemmer, slår vi en skråstrek over symbolet.
:::

:::::::::::::::{example} Eksempel 1
Hvis Anna bor i Oslo, så betyr det også at hun bor i Norge. Da kan vi skrive dette som:

$$
\text{Anna bor i Oslo} \limplies \text{Anna bor i Norge}
$$

Men det motsatte er ikke sant. Hvis Anna bor i Norge, betyr ikke det nødvendigvis at hun bor i Oslo. Hun kan for eksempel bo i Bergen. Da kan vi skrive 

$$
\text{Anna bor i Norge} \nimplies \text{Anna bor i Oslo}
$$
:::::::::::::::

---

Vi tar et eksempel som er litt mer matematisk. 

:::::::::::::::{example} Eksempel 2
Hvis $x = 2$, så er $x^2 = 4$. Da kan vi skrive 

$$
x = 2 \limplies x^2 = 4
$$

:::::::::::::::

---

Hvis to påstander må være sanne samtidig, sier vi at de er **ekvivalente**. Det betyr at hvis én av de er sanne, så må begge være sanne. I eksempel 1 så vi at det at Anna bodde i Norge ikke nødvendigvis ville betydd at hun bodde i Oslo. Disse påstandene er derfor ikke ekvivalente. 

:::{margin}
Vi kan også lese $P \iff Q$ som at $P$ er sann hvis og bare hvis $Q$ er sann.
:::

:::::::::::::::{summary} Ekvivalens
Hvis en påstand $P$ er sann betyr at en påstand $Q$ også må er sann og omvendt, skriver vi dette som $P \iff Q$. Vi leser dette som "$P$ er ekvivalent med $Q$". 
:::::::::::::::

Vi tar et eksempel.

:::{margin}
Vi kunne også skrevet 

$$
2x = 4 \limpliedby x = 2
$$

som vi leser som "$2x = 4$ er implisert av $x = 2$". 
:::

:::::::::::::::{example} Eksempel 3
Hvis $2x = 4$, så er $x = 2$. Det betyr at 

$$
2x = 4 \limplies x = 2
$$

Men hvis $x = 2$, så er også $2x = 4$. Det betyr at 

$$
x = 2 \limplies 2x = 4
$$

Siden påstandene impliserer begge veier, betyr dette at 

$$
2x = 4 \liff x = 2
$$
:::::::::::::::



## Logisk-og og logisk-eller

Noen ganger så vil vi uttrykke at én av flere påstander kan være sanne, men ikke nødvendigvis alle sammen samtidig. Da bruker vi **logisk-eller**. Hvis vi for eksempel sier at "Anna bor i Oslo eller Bergen", så betyr det at hun kan bo i Oslo, eller hun kan bo i Bergen, eller hun kan bo i begge byene. 

:::::::::::::::{summary} Logisk-eller
Hvis en påstand $P$ er sann eller en annen påstand $Q$ er sann, skriver vi dette som $P \lor Q$. Vi leser dette som "$P$ eller $Q$". 
:::::::::::::::


---

:::::::::::::::{example} Eksempel 4
Hvis Anna bor i Oslo eller Bergen, kan vi skrive dette som 

$$
\text{Anna bor i Oslo} \or \text{Anna bor i Bergen}
$$
:::::::::::::::

---

Vi tar et eksempel er mer matematisk.

:::::::::::::::{example} Eksempel 5
Hvis $x^2 = 4$, så kan det bety at $x = 2$ eller at $x = -2$ siden 

$$
2^2 = 4 \qog (-2)^2 = 4
$$

Da kan vi skrive at 

$$
x^2 = 4 \liff x = 2 \or x = -2
$$

:::::::::::::::


---


I tilfeller hvor to påstander må være sanne samtidig, bruker vi **logisk-og**. Den typiske situasjonen hvor dette er aktuelt, er når vi jobber med likningssystemer eller ulikheter. 


:::::::::::::::{summary} Logisk-og
Hvis en påstand $P$ er sann og en annen påstand $Q$ er sann, skriver vi dette som $P \land Q$. Vi leser dette som "$P$ og $Q$ *samtidig*". 
:::::::::::::::

:::::::::::::::{example} Eksempel 6
Et likningssystem er et eksempel på to påstander som må være sanne samtidig. Gitt likningssystemet som består av likningene

\begin{align*}
x + y &= 2 \\
x - y &= 0
\end{align*}

så mener vi egentlig at de skal være oppfylt samtidig. Da er det mer presist å skrive at 

$$
x + y = 2 \and x - y = 0
$$

Begge likninger er oppfylt hvis $x = 1$ og $y = 1$ **samtidig**. Derfor kan vi uttrykke løsningen som

$$
x = 1 \and y = 1
$$

:::::::::::::::



## Oppsummering

::::{summary} Oppsummering

| Skrivemåte | Betydning | Eksempel |
|---|---|:---:|
| $P \implies Q$ | $P$ impliserer $Q$ | $x = 2 \limplies x^2 = 4$ | 
| $P \iff Q$ | $P$ er ekvivalent med $Q$ | $2x = 4 \liff x = 2$ |
| $P \lor Q$ | $P$ eller $Q$ (eller begge) | $x = -2 \or x = 2$ |
| $P \land Q$ | $P$ og $Q$ (samtidig) | $x = 1 \and y = 1$ |
::::