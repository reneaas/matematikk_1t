# Mengder

:::{admonition} Læringsmål: mengder
---
class: tip
---
Etter dette delkapittelet, er målet at du skal kunne:
* Kunne forklare hva en mengde er og bruke notasjon for å beskrive om et tall er en del av en mengde eller ikke.
* Forklare mengdene $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ og $\mathbb{R}$ og gi eksempler på tall som er inneholdt i hver mengde. 
:::


## De spesielle tallmengdene

En **mengde** er rett og slett en samling objekter. En **tallmengde** er derfor en samling med tall. Noen ganger er tall i en mengde gruppert sammen fordi de har like egenskaper, andre ganger fordi vi ønsker å beskrive en samling tall, for eksempel som løsningen til en likning. 
Vi starter med å introdusere fire *spesielle* tallmengder:

| Symbol | Navn | Eksempler | Forklaring | 
| :---: | --- | --- |--- |
| $\mathbb{N}$ | De **naturlige** tallene. | $1, 2, 3, 8 $| Alle de positive heltallene. |
| $\mathbb{Z}$ | **Heltallene** | $-3, -2, -1, 0, 1, 2$| Alle heltallene, inkludert 0. |
| $\mathbb{Q}$ | De **rasjonale** tallene | $-\dfrac{1}{2}, \dfrac{1}{3}, \dfrac{7}{4}, 2$| Alle tall som kan skrives som en brøk der teller og nevner er heltall. |
| $\mathbb{R}$ | De **reelle** tallene | $\pi, \sqrt{2}, \dfrac{10}{2}$ | Alle tallene på tallinja. | 

Kanskje la du merke til at alle de naturlige tallene er inkludert i heltallene. Og på samme måte er alle heltallene (og dermed også de naturlige tallene) inkludert i de rasjonale tallene. Og alle disse tallene er igjen inkludert i den reelle tallmengden. 
Vi kan derfor illustrere sammenhengen mellom tallmengdene som i {numref}`mengder_venndiagram` under. 

:::{figure} ./figurer/mengder_venndiagram.svg
---
name: mengder_venndiagram
width: 80%
---

viser hvordan de ulike tallmengdene henger sammen. Diagrammet illustrerer at $\mathbb{N}$ er inkludert i $\mathbb{Z}$, som igjen er inkludert i $\mathbb{Q}$, som igjen er inkludert i $\mathbb{R}$.
:::

---

Selv om vi kan si at $2$ tilhører $\mathbb{Z}$, så er ikke dette den "minste" mulige mengden vi kan bruke til å beskrive tallet. Vi Vi velger vanligvis den minste mulige mengden for å beskrive hvor tallet "hører hjemme". Derfor sier vi at $2$ tilhører de naturlige tallene $\mathbb{N}$. 

Men nå bør teste forståelsen din!

:::::{admonition} Underveisoppgave 1
---
class: check
---
Plasser tallene under i riktig tallmengde (husk: den *minste* mulige mengden):

| Tall | $-6$ | $4$ | $0$ | $120$ | $\dfrac{5}{2}$ | $\dfrac{15}{5}$ | $\sqrt{3}$ | $-8$ | $\sqrt{16}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| **Mengde** | | | | | | | | | | 



::::{admonition} Løsning
---
class: solution, dropdown
---
Merk først at noen av tallene er ikke skrevet så enkelt som mulig. Spesielt kan vi merke oss at:

$$
\frac{15}{5} = \frac{3 \cdot 5}{5} = 3  \quad \text{og} \quad \sqrt{16} = 4.
$$

Deretter kan vi fylle ut tabellen:

| Tall | $-6$ | $4$ | $0$ | $120$ | $\frac{5}{2}$ | $\frac{15}{5}$ | $\sqrt{3}$ | $-8$ | $\sqrt{16}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| **Mengde** | $\mathbb{Z}$ | $\mathbb{N}$ | $\mathbb{Z}$ | $\mathbb{N}$ | $\mathbb{Q}$ | $\mathbb{N}$ | $\mathbb{R}$ | $\mathbb{Z}$ | $\mathbb{N}$ |
::::

:::::

## En mer generell definisjon av en mengde
Vi gjentar: en mengde bare en *samling objekter*. I de fleste tilfeller vil objektene i mengden være tall, men de vil i blant også være punkter. Vi skal foreløpig bare fokusere på tallmengder.

```{admonition} Definisjon: Mengde
:class: theory

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
| $\frac{1}{2}$ | | $\mathbb{N}$ |
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
| $\frac{1}{2}$ | $\notin$ | $\mathbb{N}$ |
| $\sqrt{2}$ | $\in$ | $\mathbb{Q}$ |
| $\pi$ | $\notin$ | $\mathbb{Q}$ |
| $0$ | $\in$ | $\mathbb{R}$ |
| $-3$ | $\in$ | $\mathbb{R}$ |
| $\sqrt{3}$ | $\in$ | $\mathbb{R}$ |
```
````