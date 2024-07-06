# Mengdelære

Har du tenkt på at det finnes ulike typer tall? Tallene $1$, $5$ og $8$ skiller seg fra tallene $13/5$ og $\pi$, men hva er forskjellen? I dette kapittelet skal vi se på noen vanlige tallmengder og hvilke tall som hører til i de ulike mengdene. 

```{admonition} Læringsmål: mengdelære
:class: tip

* Du skal kunne forklare mengdene $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ og $\mathbb{R}$ og gi eksempler på tall som er inneholdt i hver mengde. 
* Du skal kunne skrive tallmengder både som intervaller og som mengder.

```

## Tallmengder
En **mengde** er rett og slett en samling objekter. En **tallmengde** er derfor en samling med tall. Noen ganger er tall i en mengde gruppert sammen fordi de har like egenskaper, andre ganger fordi vi ønsker å beskrive en samling tall, for eksempel som løsningen til en likning. 
Vi starter med å introdusere fire *spesielle* tallmengder:

| Symbol | Navn | Eksempel | Kommentar | 
| :---: | --- | --- |--- |
| $\mathbb{N}$ | De **naturlige** tallene. | $1, 2, 3, 8 $| Alle de positive heltallene. |
| $\mathbb{Z}$ | **Heltallene** | $-3, -2, -1, 0, 1, 2$| Alle heltallene, inkludert 0. |
| $\mathbb{Q}$ | De **rasjonale** tallene | $-\frac{1}{2}, \frac{1}{2}, \frac{10}{5}, 2$| Alle tall som kan skrives som en brøk der teller og nevner er heltall. |
| $\mathbb{R}$ | De **reelle** tallene | $\pi, \sqrt{2}, \frac{10}{2}$ | Alle tallene på tallinja. | 

La du merke til noe ved tabellen over? Alle de naturlige tallene er inkludert i heltallene. På samme måte er alle heltallene (og dermed også de naturlige tallene) inkludert i de rasjonale tallene. Og alle disse tallene er igjen inkludert i den reelle tallmengden. 
Vi kan derfor illustrere sammenhengen mellom tallmengdene som i {numref}`mengder_venndiagram` under. 

```{figure} ./figurer/mengder_venndiagram.svg
:name: mengder_venndiagram
:width: 80%

Figuren viser hvordan de ulike tallmengdene henger sammen. Diagrammet illustrerer at $\mathbb{N}$ er inkludert i $\mathbb{Z}$, som igjen er inkludert i $\mathbb{Q}$, som igjen er inkludert i $\mathbb{R}$.
```
---

Legg merke til at vi sier at $2$ tilhører $\mathbb{N}$. Det betyr selvsagt at $2$ også tilhører alle de andre tallmengdene. Vi velger altså alltid den **minste** mulige tallmengden et tall kan tilhøre. 

`````{admonition} Underveisoppgave 1
:class: check
Plasser tallene under i riktig tallmengde (husk: den *minste* mulige mengden):

| Tall | $-6$ | $4$ | $0$ | $120$ | $\frac{5}{2}$ | $\frac{15}{5}$ | $\sqrt{3}$ | $-8$ | $\sqrt{16}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| **Mengde** | | | | | | | | | | 



````{admonition} Løsning
:class: solution, dropdown
Merk først at noen av tallene er ikke skrevet så enkelt som mulig. Spesielt kan vi merke oss at:

$$
\frac{15}{5} = \frac{3 \cdot 5}{5} = 3  \quad \text{og} \quad \sqrt{16} = 4.
$$

Deretter kan vi fylle ut tabellen:

| Tall | $-6$ | $4$ | $0$ | $120$ | $\frac{5}{2}$ | $\frac{15}{5}$ | $\sqrt{3}$ | $-8$ | $\sqrt{16}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| **Mengde** | $\mathbb{Z}$ | $\mathbb{N}$ | $\mathbb{Z}$ | $\mathbb{N}$ | $\mathbb{Q}$ | $\mathbb{N}$ | $\mathbb{R}$ | $\mathbb{Z}$ | $\mathbb{N}$ |
````

`````

## En mer generell definisjon av en mengde
Som vi nevnte i innledningen, er en mengde bare en samling objekter. I de fleste tilfeller vil objektene i mengden være tall, men de vil i blant være punkter. Men foreløpig skal vi formulere en generell nok definisjon av mengde som består av tall:

```{admonition} Definisjon: Mengde
:class: theory

En **mengde** $A$ er en samling tall. Dersom et tall $x$ er en del av mengden $A$, skriver vi $x \in A$. Vi leser dette som "$x$ er *et element i* mengden $A$". 

Dersom et tall $y$ *ikke* er er en del av mengden $A$, skriver vi $y \notin A$. Vi leser dette som "$y$ er *ikke* et element i mengden $A$". 
```


Her kan du få prøve å anvende definisjonen på noen eksempler:

````{admonition} Underveisoppgave 2
:class: check

Vi skriver $2 \in \mathbb{N}$ fordi $2$ er et element i den naturlige mengden. Samtidig kan vi skrive $\pi \notin \mathbb{Z}$ siden $\pi$ ikke er et element i heltallsmengden. 
Fyll ut tabellen under der du uttrykket om tallet er et element i mengden eller ikke:

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