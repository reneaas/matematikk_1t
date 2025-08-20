# Tallmengder

:::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive de ulike spesielle tallmengdene.
* Kunne bruke matematisk notasjon for å beskrive elementer i ulike tallmengder.
* Kunne beskrive delmengder av de reelle tallene med intervaller og ulikheter.
:::


En tallmengde er en samling av tall. Noen ganger er de samlet basert på felles egenskaper som skiller dem fra andre tall. Andre ganger er de samlet fordi de alle sammen løser en bestemt likning. 


## Spesielle tallmengder


:::{figure} ./figurer/teori/mengder_venndiagram.svg
---
width: 100%
class: clickable-figure, adaptive-figure
figclass: margin
---

viser hvordan de ulike tallmengdene henger sammen. Diagrammet illustrerer at $\mathbb{N}$ er inkludert i $\mathbb{Z}$, som igjen er inkludert i $\mathbb{Q}$, som igjen er inkludert i $\mathbb{R}$.
:::

::::{summary} De spesielle tallmengdene

| Symbol | Navn | Eksempler | Beskrivelse | 
| :---: | --- | --- |--- |
| $\mathbb{N}$ | De **naturlige** tallene. | $1, 2, 3, 8 $| Alle de positive heltallene. |
| $\mathbb{Z}$ | **Heltallene** | $-3, -2, -1, 0, 1, 2$| Alle hele tall - inkludert $0$ og alle negative hele tall. |
| $\mathbb{Q}$ | De **rasjonale** tallene | $-\dfrac{1}{2}, \dfrac{1}{3}, \dfrac{7}{4}, 2$| Alle tall som kan skrives som en brøk der teller og nevner er heltall. |
| $\mathbb{R}$ | De **reelle** tallene | $\pi, \sqrt{2}, \dfrac{10}{2}$ | Alle tallene på tallinja. | 
| $\emptyset$ | Den **tomme** mengden | - | Mengden uten noen elementer. |


::::

Fra tabellen over kan det hende du la merke til at alle de naturlige tallene også er hele tall, og dermed er alle naturlige tall inkludert i heltallsmengden. På tilsvarende måte vil alle heltall også være rasjonale tall der nevneren er $1$. Derfor er heltallene inkludert i mengden av rasjonale tall. Dette argumentet kan vi føre videre, fordi alle de rasjonale tallene må være reelle tall siden de ligger på tallinja. Tallene som er reelle, men ikke rasjonale kaller vi for **irrasjonale** tall. Eksempler på irrasjonale tall er $\pi$ og $\sqrt{2}$. 

## Mengdenotasjon


:::{margin}
Mengder trenger ikke bare å være tall. Hvis $A$ er en mengde av alle elever i en klasse. Da ville $x \in A$ bety at $x$ er en elev i klassen, mens $x \notin A$ ville bety at $x$ ikke er en elev i klassen.
:::

Vi skal ofte beskrive tallmengder og da trenger vi matematisk notasjon for å gjøre det. Når et tall tilhører en mengde, sier vi at tallet er et **element** i mengden. Når et tall $x$ er et element i en mengde $A$, skriver vi $x \in A$. Hvis $x$ *ikke* er et element i mengden skriver vi $x \notin A$. For eksempel er $2 \in \natural$ og $-3 \notin \natural$.


### Listenotasjon
Noen ganger vil vi beskrive en mengde bestående av noen bestemte elementer. Dette får vi bruk for når vi skal jobbe med likninger som har mer enn én løsning.
Da kan vi bruke **listenotasjon**. Vi kan beskrive alle tallene i $\natural$ og $\integer$ ved å bruke listenotasjon:

$$
\natural = \{1, 2, 3, 4, 5, \ldots\} \qog \integer = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}
$$

Men vi kan også beskrive mengder som bare består av noen få elementer. For eksempel vil mengden som bare inneholder tallene $-3$, $0$ og $2$ skrives som $\{-3, 0, 2\}$. 

### Ulikheter

Når vi jobber med ulikheter, vil løsningen av ulikheten ofte være en **delmengde** av de reelle tallene. For eksempel beskriver $-3 < x < 2$ alle reelle tall som er større enn $-3$ og mindre enn $2$. Slik mengder er begrenset både nedenfra og ovenfra. 
 
:::::{summary} Begrensende mengder som ulikheter
Vi kan skrive en begrenset mengde av reelle tall på følgende måter:

| Ulikhet | Beskrivelse |
|:---:|---|
| $a \leq x \leq b$ | Alle reelle tall $x$ større enn eller lik $a$ og mindre enn eller lik $b$. |
| $a < x < b$ | Alle reelle tall $x$ større enn $a$ og mindre enn $b$. |
| $a \leq x < b$ | Alle reelle tall $x$ større enn eller lik $a$ og mindre enn $b$. |
| $a < x \leq b$ | Alle reellle tall $x$ større enn $a$ og mindre enn eller lik $b$. |

<br>

Se figuren nedenfor.

::::{figure} ./figurer/teori/teori_1.svg
---
width: 100%
class: no-click, adaptive-figure
---
::::
:::::

---


:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen! 

:::::{quiz}
Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $-1$ og mindre enn eller lik $1$?
+ $-1 \leq x \leq 1$
- $-1 < x < 1$
- $-1 \leq x < 1$
- $-1 < x \leq 1$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn $0$ og mindre enn $3$?
+ $0 < x < 3$
- $0 \leq x < 3$
- $0 < x \leq 3$
- $0 \leq x \leq 3$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $2$ og mindre enn $5$?
+ $2 \leq x < 5$
- $2 < x < 5$
- $2 \leq x \leq 5$
- $2 < x \leq 5$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn $-4$ og mindre enn eller lik $1$?
+ $-4 < x \leq 1$
- $-4 \leq x < 1$
- $-4 < x < 1$
- $-4 \leq x \leq 1$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $-3$ og mindre enn eller lik $2$?
+ $-3 \leq x \leq 2$
- $-3 < x < 2$
- $-3 \leq x < 2$
- $-3 < x \leq 2$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn $1$ og mindre enn eller lik $4$?
+ $1 < x \leq 4$
- $1 \leq x < 4$
- $1 < x < 4$
- $1 \leq x \leq 4$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $-2$ og mindre enn $3$?
+ $-2 \leq x < 3$
- $-2 < x < 3$
- $-2 \leq x \leq 3$
- $-2 < x \leq 3$

Q: Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn $-5$ og mindre enn eller lik $0$?
+ $-5 < x \leq 0$
- $-5 \leq x < 0$
- $-5 < x < 0$
- $-5 \leq x \leq 0$
:::::
:::::::::::::::

---

Vi kan også ha ulikheter der løsningen kun er begrenset på den ene siden. For eksempel beskriver $x \geq 2$ alle reelle tall som er større enn eller lik $2$. Slik mengder er ikke begrenset ovenfra, men er begrenset nedenfra.

:::::{summary} Ubegrensede mengder som ulikheter
Vi kan skrive en ubegrenset mengde av reelle tall på følgende måter:
| Ulikhet | Beskrivelse |
|:---:|---|
| $x \geq a$ | Alle reelle tall $x$ større enn eller lik $a$. |
| $x > a$ | Alle reelle tall $x$ større enn $a$. |
| $x \leq b$ | Alle reelle tall $x$ mindre enn eller lik $b$. |
| $x < b$ | Alle reelle tall $x$ mindre enn $b$. |

<br>

Se figuren nedenfor.

::::{figure} ./figurer/teori/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
viser to typer ubegrensende mengder. Figuren øverst viser en mengde som er begrenset nedenfra, men ikke ovenfra. Figuren nederst viser en mengde som er begrenset ovenfra, men ikke nedenfra.
::::
:::::

---



:::::::::::::::{exercise} Underveisoppgave 2
Ta quizen!


:::::{quiz}
Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $-2$?
+ $x \geq -2$
- $x > -2$
- $x \leq -2$
- $x < -2$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er mindre enn $4$?
+ $x < 4$
- $x \leq 4$
- $x > 4$
- $x \geq 4$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er mindre enn eller lik $-1$?
+ $x \leq -1$
- $x < -1$
- $x \geq -1$
- $x > -1$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn $3$?
+ $x > 3$
- $x \geq 3$
- $x < 3$
- $x \leq 3$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $-5$?
+ $x \geq -5$
- $x > -5$
- $x \leq -5$
- $x < -5$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er mindre enn eller lik $2$?
+ $x \leq 2$
- $x < 2$
- $x \geq 2$
- $x > 2$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er større enn eller lik $0$?
+ $x \geq 0$
- $x > 0$
- $x \leq 0$
- $x < 0$

Q: Hvilken ulikhet passer med beskrivelsen: <br> Alle reelle tall $x$ som er mindre enn $-3$?
+ $x < -3$
- $x \leq -3$
- $x \geq -3$
- $x > -3$

:::::
:::::::::::::::



### Intervaller
Etter hvert som løsningene av ulikheter blir mer kompliserte å beskrive, blir notasjonen med ulikheter ganske tungvint. Derfor har vi noe om vi kaller for **intervaller** som gjør det en del enklere å lese hvilke reelle tall som er med i mengden. 


### Begrensede intervaller
Akkurat som med ulikheter, kan vi beskrive en begrenset mengde av reelle tall ved hjelp av intervaller. 


:::{margin}
Vi leser "$\mid$" som "slik at". Det betyr at når vi skriver $\{x \in \mathbb{R} \mid a \leq x \leq b\}$, leser vi dette som "alle reelle tall $x$ slik at $a \leq x \leq b$".
:::

:::::{summary} Begrensende Intervaller
Intervaller kan skrives på følgende måter:
| Intervall | Beskrivelse |
|:---:|---|
| $[a, b]$ | $\{x \in \mathbb{R} \mid a \leq x \leq b\}$ |
| $\langle a, b \rangle$ | $\{x \in \mathbb{R} \mid a < x < b\}$ |
| $[a, b \rangle$ | $\{x \in \mathbb{R} \mid a \leq x < b\}$ |
| $\langle a, b]$ | $\{x \in \mathbb{R} \mid a < x \leq b\}$ |

:::::


---


:::::::::::::::{exercise} Underveisoppgave 3
Ta quizen! 

:::::{quiz}
Q: Hvilket intervall passer med $-1 \leq x \leq 2$?
+ $[-1, 2]$
- $\langle -1, 2 \rangle$
- $[-1, 2 \rangle$
- $\langle -1, 2]$

Q: Hvilket intervall passer med $0 < x < 3$?
+ $\langle 0, 3 \rangle$
- $[0, 3]$
- $[0, 3 \rangle$
- $\langle 0, 3]$

Q: Hvilket intervall passer med $-2 \leq x < 1$?
+ $[-2, 1 \rangle$
- $\langle -2, 1 \rangle$
- $[-2, 1]$
- $\langle -2, 1]$

Q: Hvilket intervall passer med $-3 < x \leq 4$?
+ $\langle -3, 4]$
- $[-3, 4]$
- $[-3, 4 \rangle$
- $\langle -3, 4 \rangle$

Q: Hvilket intervall passer med $1 \leq x \leq 5$?
+ $[1, 5]$
- $\langle 1, 5 \rangle$
- $[1, 5 \rangle$
- $\langle 1, 5]$

Q: Hvilket intervall passer med $-4 < x < 2$?
+ $\langle -4, 2 \rangle$
- $[-4, 2]$
- $[-4, 2 \rangle$
- $\langle -4, 2]$

Q: Hvilket intervall passer med $-1 \leq x < 3$?
+ $[-1, 3 \rangle$
- $\langle -1, 3 \rangle$
- $[-1, 3]$
- $\langle -1, 3]$

Q: Hvilket intervall passer med $0 < x \leq 4$?
+ $\langle 0, 4]$
- $[0, 4]$
- $[0, 4 \rangle$
- $\langle 0, 4 \rangle$


:::::

:::::::::::::::



### Ubegrensede intervaller
Vi kan også beskrive ubegrensede mengder av reelle tall ved hjelp av intervaller. Disse intervallene strekker seg i det uendelige i minst én retning.

:::::{summary} Ubegrensede intervaller
Ubegrensede intervaller kan skrives på følgende måter:
| Intervall | Beskrivelse |
|:---:|---|
| $[a, \to\rangle$ | $\{x \in \mathbb{R} \mid x \geq a\}$ |
| $\langle a, \to\rangle$ | $\{x \in \mathbb{R} \mid x > a\}$ |
| $\langle\gets, b]$ | $\{x \in \mathbb{R} \mid x \leq b\}$ |
| $\langle\gets, b \rangle$ | $\{x \in \mathbb{R} \mid x < b\}$ |
:::::

---


:::::::::::::::{exercise} Underveisoppgave 4
Ta quizen!


:::::{quiz}
Q: Hvilket intervall passer med $x \geq -2$?
+ $[-2, \to\rangle$
- $\langle -2, \to\rangle$
- $\langle -2, \gets]$
- $\langle -2, \gets \rangle$

Q: Hvilket intervall passer med $x > 3$?
+ $\langle 3, \to\rangle$
- $[3, \to\rangle$
- $[3, \gets]$
- $\langle 3, \gets \rangle$

Q: Hvilket intervall passer med $x \leq 1$?
+ $\langle\gets, 1]$
- $\langle\gets, 1 \rangle$
- $[1, \gets]$
- $[1, \gets \rangle$

Q: Hvilket intervall passer med $x < -4$?
+ $\langle\gets, -4 \rangle$
- $\langle\gets, -4]$
- $[-4, \gets]$
- $[-4, \gets \rangle$

Q: Hvilket intervall passer med $x \geq 0$?
+ $[0, \to\rangle$
- $\langle 0, \to\rangle$
- $\langle 0, \gets]$
- $\langle 0, \gets \rangle$

Q: Hvilket intervall passer med $x < 2$?
+ $\langle\gets, 2 \rangle$
- $\langle\gets, 2]$
- $[2, \gets]$
- $[2, \gets \rangle$

Q: Hvilket intervall passer med $x \leq -1$?
+ $\langle\gets, -1]$
- $\langle\gets, -1 \rangle$
- $[-1, \gets]$
- $[-1, \gets \rangle$

Q: Hvilket intervall passer med $x > 5$?
+ $\langle 5, \to\rangle$
- $[5, \to\rangle$
- $[5, \gets]$
- $\langle 5, \gets \rangle$

:::::

:::::::::::::::
