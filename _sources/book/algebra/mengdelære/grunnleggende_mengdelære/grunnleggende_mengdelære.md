# Mengder

:::{admonition} Læringsmål: mengder
---
class: tip
---
* Kunne forklare hva en mengde er og bruke matematisk notasjon for å uttrykke om et tall er et element i en mengde eller ikke.
* Kunne beskrive mengdene $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ og $\emptyset$, og gi eksempler på tall som er element i hver mengde. 
:::


## De spesielle tallmengdene

En **mengde** er rett og slett en samling objekter. En **tallmengde** er derfor en samling med tall. Noen ganger er tall i en mengde gruppert sammen fordi de har like egenskaper, andre ganger fordi vi ønsker å beskrive en samling tall, for eksempel som løsningen til en likning. 
Vi starter med å introdusere fire *spesielle* tallmengder.

::::{admonition} De spesielle tallmengdene
---
class: theory
---

| Symbol | Navn | Eksempler | Beskrivelse | 
| :---: | --- | --- |--- |
| $\mathbb{N}$ | De **naturlige** tallene. | $1, 2, 3, 8 $| Alle de positive heltallene. |
| $\mathbb{Z}$ | **Heltallene** | $-3, -2, -1, 0, 1, 2$| Alle hele tall - inkludert $0$ og alle negative hele tall. |
| $\mathbb{Q}$ | De **rasjonale** tallene | $-\dfrac{1}{2}, \dfrac{1}{3}, \dfrac{7}{4}, 2$| Alle tall som kan skrives som en brøk der teller og nevner er heltall. |
| $\mathbb{R}$ | De **reelle** tallene | $\pi, \sqrt{2}, \dfrac{10}{2}$ | Alle tallene på tallinja. | 
| $\emptyset$ | Den **tomme** mengden | - | Mengden uten noen elementer. |

::::

Fra tabellen over kan det hende du la merke til at alle de naturlige tallene også er hele tall, og dermed er alle naturlige tall inkludert i heltallsmengden. På tilsvarende måte vil alle heltall også være rasjonale tall der nevneren er $1$. Derfor er heltallene inkludert i mengden av rasjonale tall. Dette argumentet kan vi føre videre, fordi alle de rasjonale tallene må være reelle tall siden de ligger på tallinja.
Vi kan illustrere sammenhengen mellom tallmengdene som i {numref}`mengder_venndiagram`. 

:::{figure} ./figurer/mengder_venndiagram.svg
---
name: mengder_venndiagram
width: 80%
class: no-click, adaptive-figure
---

viser hvordan de ulike tallmengdene henger sammen. Diagrammet illustrerer at $\mathbb{N}$ er inkludert i $\mathbb{Z}$, som igjen er inkludert i $\mathbb{Q}$, som igjen er inkludert i $\mathbb{R}$.
:::

---

Vi kan altså si at $2$ tilhører både $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ og $\mathbb{R}$, mens $2/3$ kun tilhører $\mathbb{Q}$ og $\mathbb{R}$. 





:::::{admonition} Underveisoppgave 1
---
class: check
---
Fyll ut tabellen med alle mengdene tallene tilhører.

| Tall | $-6$ | $4$ | $0$ | $\dfrac{5}{2}$| $\sqrt{5}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Mengder** | | | |


::::{admonition} Fasit
---
class: answer, dropdown
---

| Tall | $-6$ | $4$ | $0$ | $\dfrac{5}{2}$| $\sqrt{5}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Mengder** | $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{R}$ |
::::

:::::

## En mer generell definisjon av en mengde
Vi gjentar: En mengde er bare en *samling objekter*. I de fleste tilfeller vil objektene i mengden være tall, men de vil iblant også være punkter. Vi skal foreløpig bare fokusere på tallmengder.

```{admonition} Definisjon: mengde
---
class: theory
---
En **mengde** $A$ er en samling tall. Dersom et tall $x$ er en del av mengden $A$, skriver vi $x \in A$. Vi leser dette som "$x$ er *et element i* $A$". 

Dersom et tall $y$ *ikke* er er en del av mengden $A$, skriver vi $y \notin A$. Vi leser dette som "$y$ er *ikke* et element i $A$". 
```


Her kan du få prøve å anvende definisjonen på noen eksempler:

````{admonition} Underveisoppgave 2
:class: check

Vi skriver $2 \in \mathbb{N}$ fordi $2$ er et element i den naturlige mengden. Samtidig kan vi skrive $\pi \notin \mathbb{Z}$ siden $\pi$ ikke er et element i heltallsmengden. 

Fyll ut tabellen under der du uttrykker om tallet er et element i mengden eller ikke:

|Tall| $\in$ eller $\notin$ | Mengde |
|:---:|:---:|:---:|
| $3$ | | $\mathbb{N}$ |
| $-2$ | | $\mathbb{Z}$ |
| $\dfrac{1}{2}$ | | $\mathbb{N}$ |
| $\sqrt{2}$ | | $\mathbb{Q}$ |
| $\pi$ | | $\mathbb{Q}$ |
| $0$ | | $\mathbb{R}$ |
| $-3$ | | $\mathbb{R}$ |
| $\sqrt{3}$ | | $\mathbb{R}$ |

```{admonition} Løsning
:class: solution, dropdown

|Tall| $\in$ eller $\notin$ | Mengde |
|:---:|:---:|:---:|
| $3$ | $\in$ | $\mathbb{N}$ |
| $-2$ | $\in$ | $\mathbb{Z}$ |
| $\dfrac{1}{2}$ | $\notin$ | $\mathbb{N}$ |
| $\sqrt{2}$ | $\notin$ | $\mathbb{Q}$ |
| $\pi$ | $\notin$ | $\mathbb{Q}$ |
| $0$ | $\in$ | $\mathbb{R}$ |
| $-3$ | $\in$ | $\mathbb{R}$ |
| $\sqrt{3}$ | $\in$ | $\mathbb{R}$ |
```
````