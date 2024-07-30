# Topunktsformelen


## Hva må vi vite for å bestemme likningen til en linje? 
For å bestemme likningen til en linje, trenger vi å vite enten:
1. To punkter på linja.
2. Ett punkt på linja og stigningstallet til linja.

Med andre ord, vi trenger to biter med informasjon for å bestemme likningen til en linje. I dette kapittelet skal vi fokusere på hvordan vi kan bestemme stigningstallet i tilfelle 1. 


```{admonition} Læringsmål: topunktsformelen
:class: tip
Målet med denne seksjonen er at du skal kunne:
* Bestemme stigningstallet til en lineær funksjon ved å bruke topunktsformelen.
```

## Topunktsformelen: hva er det?

Vi går ut ifra at vi har to punkter $(x_1, y_1)$ og $(x_2, y_2)$ som grafen til en lineær funksjon $f$ går gjennom. For å bestemme funksjonsuttrykket $f(x)$, kan vi gjøre følgende:

Steg 1: bestemme stigningstallet $a$
: Vi regner ut stigningstallet $a$ ved å bruke *topunktsformelen*

Steg 2: bestemme konstantleddet $b$
: Vi bestemmer konstantleddet ved å sette opp en likning for $b$.


Men *hva* er topunktsformelen? 

````{admonition} Topunktsformelen
:class: theory
Hvis grafen til en lineær funksjon $f(x)$ går gjennom to punkter $(x_1, y_1)$ og $(x_2, y_2)$, så er stigningstallet $a$ gitt ved 

$$
a = \frac{\Delta y}{\Delta x},
$$ (eq:topunktsformelen)

der 

$$
\Delta x = x_2 - x_1 \quad \text{og} \quad \Delta y = y_2 - y_1,
$$

representerer endringene i $x$- og $y$-verdiene mellom de to punktene.

Grafen under viser to punkter $(x_1, y_1)$ og $(x_2, y_2)$ som grafen til en lineær funksjon går gjennom. I likhet med tolkningen vår før, vil stigningstallet være hvor mye $y$-verdien endrer seg dersom vi øker $x$-verdien med $1$. (Prøv å sette $\Delta x = 1$ i formelen over!)

```{figure} ./figurer/teori/topunktsformelen.svg
:name: topunktsformelen
:width: 80%
```
````


La oss ta et eksempel:

```{admonition} Eksempel 1: topunktsformelen til å finne stigningstallet
:class: example

Grafen til en lineær funksjon $f$ går gjennom punktene $(1, 2)$ og $(5, 6)$. 

Bestem stigningstallet til $f(x)$.

**Løsning**:<br>
Vi bruker topunktsformelen med $(x_1, y_1) = (1, 2)$ og $(x_2, y_2) = (7, 6)$. Vi regner først ut endringene i $x$- og $y$-verdiene:

$$
\Delta x = x_2 - x_1 = 7 - 1 = 6, \quad \text{og} \quad \Delta y = y_2 - y_1 = 6 - 2 = 4.
$$

Dermed blir stigningstallet

$$
a = \frac{\Delta y}{\Delta x} = \frac{4}{6} = \frac{2}{3}.
$$
```

Nå er det **din tur**:

`````{admonition} Underveisoppgave 1
:class: check

Under vises en tabell over noen lineære funksjoner der det er oppgitt to punkter som hver av grafene går gjennom. 

Bestem stigningstallet til hver av funksjonene.

| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $(1, 2)$  | $(3, 4)$  |  |  |  |
| $g(x)$ | $(2, 3)$  | $(4, 1)$  |  |  |  |         
| $h(x)$ | $(0, 1)$  | $(2, 5)$  |  |  |  |          
| $p(x)$ | $(-2, 4)$ | $(1, -5)$ |  |  |  |         
| $q(x)$ | $(-1, 4)$ | $(3, 4)$  |  |  |  |          

````{admonition} Løsning
:class: solution, dropdown

| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | $(1, 2)$  | $(3, 4)$  | $2$ | $2$ | $1$ |
| $g(x)$ | $(2, 3)$  | $(4, 1)$  | $2$ | $-2$ | $-1$ |         
| $h(x)$ | $(0, 1)$  | $(2, 5)$  | $2$  | $4$  | $2$ |          
| $p(x)$ | $(-2, 4)$ | $(1, -5)$ | $3$ | $-9$ | $-3$ |         
| $q(x)$ | $(-1, 4)$ | $(3, 4)$  | $4$  | $0$ | $0$ |   

````

`````


## Samme stigningstall uansett hvilke to punkter, altså??

En ting du kanskje stusset over i eksempelet over er at vi gikk ut ifra at vi bare kunne bruke tilfeldige punkter på grafen til en lineær funksjon for å bestemme stigningstallet til funksjonen. <br> Dette bør vi sette prøve på - eller **du bør**!

````{admonition} Underveisoppgave 2
---
class: check
name: lineære-funksjoner-topunktsformelen-underveisoppgave-2
---

I figuren under vises grafen til en lineær funksjon $f$. Det er tegnet inn en rekke punkter på grafen. 

Velg deg ut minst tre par med punkter og regn ut stigningstallet til funksjonen. 

```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-lineære-funksjoner-topunktsformelen-underveisoppgave-2
width: 80%
---
Viser grafen til $f$ med fem punkter tegnet inn på grafen.
```

```{admonition} Løsning
:class: solution, dropdown

Det er mange muligheter her, så her er tre eksempler på valg:

**Valg 1**: $(x_1, y_1) = (-1, 5)$ og $(x_2, y_2) = (1, 1)$. <br>
Dette valget gir

$$
\Delta x = 1 - (-1) = 2, \quad \text{og} \quad \Delta y = 1 - 5 = -4,
$$

slik at 

$$
a = \frac{-4}{2} = -2
$$

**Valg 2**: $(x_1, y_1) = (2, -1)$ og $(x_2, y_2) = (-1, 5)$. <br>
Dette valget gir

$$
\Delta x = -1 - 2 = -3, \quad \text{og} \quad \Delta y = 5 - (-1) = 6,
$$

slik at

$$
a = \frac{6}{-3} = -2
$$ 

(La du merke til at vi har byttet om slik at $x_1 > x_2$ - men hadde det noe å si da?)

**Valg 3**: $(x_1, y_1) = (0, 3)$ og $(x_2, y_2) = (3, -3)$. <br>
Dette valget gir

$$
\Delta x = 3 - 0 = 3, \quad \text{og} \quad \Delta y = -3 - 3 = -6,
$$

slik at

$$
a = \frac{-6}{3} = -2
$$

Altså kan vi observere at stigningstallet blir det samme uansett hvilke to par punkter vi velger oss. Fra valg 2 kan vi også se at det er ikke en gang noe viktig å passe på at $x_2$ er større enn $x_1$. Formelen funker uansett! Vi kommer tilbake til en tolkning av dette når vi skal diskutere begrepet *vekstfart*.
```
````


:::::{admonition} Underveisoppgave 3
---
class: check
---
Under vises en interaktivt kodevindu med en kode som regner ut stigningstallet til en lineær funksjon som går gjennom to punkter.

Endre programmet slik at det regner ut stigningstallet til funksjonen fra {ref}`underveisoppgave 2 <lineære-funksjoner-topunktsformelen-underveisoppgave-2>` ved å bruke to av punktene i som er vist i {numref}`fig-lineære-funksjoner-topunktsformelen-underveisoppgave-2`.

<!-- :::{raw} html
---
file: interaktiv_kode/underveisoppgave_3.html
---
::: -->




:::::

