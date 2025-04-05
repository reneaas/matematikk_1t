:::::::::::::::{admonition} Oppgave 7
---
class: check
---
Nedenfor vises noen påstander. 

Avgjør om påstandenen er sanne eller usanne. <br> Husk å forklare hvordan du kommer fram til svarene dine.


Påstand 1
: Hvis $f$ er en polynomfunksjon og $f(-1) = f(3)$, så er $f'(1) = 0$.

<br>

Påstand 2
: Hvis $f(x)$ er et polynom av grad $5$, så må $f(x) = 0$ for *minst* én verdi av $x$.

<br>

Påstand 3
: Funksjon $f$ gitt ved 

    $$
    f(x) = \dfrac{(x - 3)^m}{x^2 - 6x + 9} \quad \text{der} \quad m \in \mathbb{N}
    $$

: har en vertikal asymptote *kun* når $m = 1$.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for hver påstand som er vurdert riktig.

Riktig svar uten argumentasjon gir ingen uttelling.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
::::{tab-set}
:::{tab-item} Påstand 1
Påstanden er **usann**. Påstanden er bare sann for andregradsfunksjoner, men generelt så vil det bare *finnes* et tall $c \in \langle -1, 3\rangle$ hvor $f'(c) = 0$, men dette punktet må ikke nødvendigvis være midt i intervallet.

Vi kan vise dette med et *moteksempel* ved å se på en tredjegradsfunksjon der $f(-1) = f(3)$. Én slik tredjegradsfunksjon er:

$$
f(x) = (x + 1)(x - 3)^2
$$ 

siden her er $f(-1) = f(3) = 0$. Så kan vi bestemme i hvilke punkter $x$ vi får $f'(x) = 0$ og undersøke hvor i intervallet $[-1, 3]$ et av disse punktene ligger.

```{figure} ./figurer/del_2/oppgave_7/påstand_1/sol.png
---
width: 80%
class: no-click
---
```

Her finner vi at $x = \dfrac{1}{3}$ er det eneste punktet som ligger i intervallet $\langle -1, 3 \rangle$. Men dette punktet er ikke $x = 1$ (midt i intervallet), så vi har motbevist påstanden.

:::


:::{tab-item} Påstand 2
Påstanden er **sann** fordi alle oddegradspolynomer må minst ha ett nullpunkt fordi et polynom $f(x)$ alltid kan faktoriseres i et produkt av lineære faktorer og andregradsfaktorer. For at vi skal få en oddetallspotens som høyeste potens må det alltid være minst én lineær faktor $(x - r)$ i $f(x)$ som sikrer at $f(x) = 0$ for minst én verdi av $x = r$.
:::


:::{tab-item} Påstand 3
Påstanden er **sann** som vi kan se ved å faktorisere nevneren:

$$
f(x) = \dfrac{(x - 3)^m}{(x - 3)^2}
$$

Bare når $m = 1$ vil vi ha færre faktorer av $(x - 3)$ i telleren enn i nevneren som dermed gir en vertikal asymptote i $x = 3$. For alle andre naturlig tall $m$ vil vi enten ha like mange faktorer eller flere i telleren som bare gir et bruddpunkt i $x = 3$.
:::


::::
:::::


:::::::::::::::