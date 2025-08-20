# Formler


:::{goals} Læringsmål
* Kunne bestemme formler for tallfølger og figurtall
* Kjenne til formlene for noen spesielle tallfølger
:::


## Partall og oddetall

Du vet sannsynligvis allerede hva et partall og et oddetall er. I noen situasjoner er det nyttig at vi kan beskrive partallene og oddetallene med formler. Partallene kan listes opp slik:

$$
\set{2, 4, 6, 8, \ldots}
$$

Vi kan se at dersom vi tar de naturlige tallene $\set{1, 2, 3, 4, \ldots}$ og ganger dem med $2$, så får vi alle partallene. Dette motiverer følgende resultat:

:::::::::::::::{summary} Partallene
Partallene $\set{2, 4, 6, 8, \ldots}$ er gitt ved formelen

$$
P_n = 2n \qder n \in \mathbb{N}
$$
:::::::::::::::


Hvis vi tar partallene $\set{2, 4, 6, 8, \ldots}$ og trekker fra $1$, så får vi alle oddetallene $\set{1, 3, 5, \ldots}$. Det gjør at vi kan skrive ned en generell formel for alle oddetallene:

:::::::::::::::{summary} Oddetallene
Oddetallene $\set{1, 3, 5, 7, \ldots}$ er gitt ved formelen

$$
O_n = 2n - 1 \qder n \in \mathbb{N}
$$
:::::::::::::::

Dersom vi ønsker å regne ut et en verdi med formelen, så erstatter vi $n$ med et bestemt tall. 

:::::::::::::::{example} Eksempel 1
Bestem verdien til det $5$-te partallet. 


::::{solution}
---
dropdown: 0
---
Vi setter inn $n = 5$ i formelen for partallene $P_n = 2n$: 

$$
P_\textcolor{red}{5} = 2 \cdot \textcolor{red}{5} = 10
$$
::::

:::::::::::::::



## Finne formler for tallfølger
En tallfølge $a_n$ er en følge av tall som følger et bestemt mønster. For eksempel er tallfølgen $a_n = 2n$ partallene, og tallfølgen $a_n = 2n - 1$ er oddetallene. For å oppdage mønstre i tallfølger, må vi ofte prøve oss frem og oppdage mønstre som vi **generaliserer** til en formel. Det er ikke alltid enkelt å finne en formel, men det blir ofte enklere når vi har gjort det en del ganger. 


Vi starter med å se på en bestemt tallfølge.

:::::::::::::::{example} Eksempel 1
Nedenfor vises noen figurer som følger et bestemt mønster.

:::{figure} ./figurer/eksempel/eksempel_1/figur_kvadrattall.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi lar $S_n$ være antall sirkler i figur $n$. Da har vi at 

$$
S_1 = 1 \qog S_2 = 4 \qog S_3 = 9
$$

Hvis vi tegner figur $4$, vil vi få $16$ sirkler. Men disse tallene følger et bestemt mønster fordi 

$$
1, 4, 9, 16,\ldots = 1^2, 2^2, 3^2, 4^2, \ldots
$$


Det betyr at vi kan skrive en formel for antall sirkler i den $n$-te figuren som

$$
S_n = n^2 \qder n \in \mathbb{N}
$$

Denne tallfølgen er en kjent tallfølge du kanskje har hørt om før og kalles for **kvadrattallene**.

:::::::::::::::
