# Enhetssirkelen


::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive hvordan $\cos v$ og $\sin v$ henger sammen med koordinatene til et punkt $P$ på enhetssirkelen.
* Kunne bruke enhetssirkelen til å bestemme $\cos v$ og $\sin v$ for vinkler $v \in [0, 360\degree\rangle$.
::::

Når vi jobbet med arealsetningen, så vi at når vi møtte på stumpe vinkler $v \in \langle 90\degree, 180\degree\rangle$ så kunne vi ikke lenger direkte bruke trekanten til å bestemme $\sin v$. Men vi fant at dersom vi brukte en rettvinklet trekant på *utsiden* av trekanten, så ville supplementvinkelen $180\degree - v$ gi en vinkel mellom $0\degree$ og $90\degree$ som ga oss høyden i trekanten. Da definerte vi at $\sin v = \sin(180\degree - v)$ når $v \in \langle 90\degree, 180\degree\rangle$.

Her skal vi ta denne definisjonen på alvor og generalisere til hva dette betyr for $\cos v$ og $\sin v$ for alle vinkler $v$. Vi skal se at vi kan bruke **enhetssirkelen** til å bestemme $\cos v$ og $\sin v$ for alle vinkler $v \in [0, 360\degree\rangle$ på følgende måte:

:::::::::::::::{admonition} Enhetssirkelen
---
class: summary
---
Enhetssirkelen er en sirkel med radius $1$ og sentrum i origo. Et punkt $P$ på enhetssirkelen vil da være 

$$
P = (\cos v, \sin v)
$$

der $v$ er vinkelen mellom $OP$ og $x$-aksen i positiv omløpsretning. Dette betyr at vi trekker en vinkelbue fra $x$-aksen **mot klokka** til vi treffer linja $OP$. Se figurene nedenfor.


:::::{figure} ./figurer/teori/enhetssirkelen/merged_figure.svg
---
width: 100%
class: no-click
---
:::

:::::::::::::::


---

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Nedenfor vises en enhetssirkelen med et punkt $P(x, y)$ tegnet inn på sirkelen. En trekant er tegnet inn der hypotenusen går fra origo opp til punktet $P$.

:::{figure} ./figurer/utforsk/utforsk_1/enhetssirkelen.svg
---
width: 80%
class: no-click
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\cos v$ for trekanten.

::::{admonition} Løsning
---
class: solution, dropdown
---
Ut ifra trekanten er hypotenusen $1$ og den hosliggende kateten er $x$. Dermed får vi 

$$
\cos v = \frac{x}{1} = x
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\sin v$ for trekanten.


::::{admonition} Løsning
---
class: solution, dropdown
---
Ut ifra trekanten er hypotenusen $1$ og den motstående kateten $y$. Dermed får vi 

$$
\sin v = \frac{y}{1} = y
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
Forklar at svarene dine i **a** og **b** betyr at 

$$
P = (x, y) = (\cos v, \sin v)
$$

::::{admonition} Løsning
---
class: solution, dropdown
---
Siden $x = \cos v$ og $y = \sin v$ og koordinatene til punktet $P$ er $P(x, y)$, så har vi at 

$$
P = (x, y) = (\cos v, \sin v)
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises enhetssirkelen med en linje fra origo ut til en punkt $P$ som har vinkelen $v = 37\degree$ med $x$-aksen.

:::{figure} ./figurer/underveisoppgaver/oppgave_1/a.svg
---
width: 80%
class: no-click
---
:::

Bruk figuren til å bestemme

$$
\cos 37\degree \quad \text{og} \quad \sin 37\degree
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\cos 37\degree = 0.80 \quad \text{og} \quad \sin 37\degree = 0.60
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
$x$-koordinaten til punktet $P$ er $\cos 37\degree = 0.80$ og $y$-koordinaten til punktet $P$ er $\sin 37\degree = 0.60$. Dermed har vi at 

$$
\cos 37\degree = 0.80 \quad \text{og} \quad \sin 37\degree = 0.60
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

Nedenfor vises enhetssirkelen med en linje fra origo ut til en punkt $P$ som har vinkelen $v = 133\degree$ med $x$-aksen.

:::{figure} ./figurer/underveisoppgaver/oppgave_1/b.svg
---
width: 80%
class: no-click
---
:::

Bruk figuren til å bestemme

$$
\cos 133\degree \quad \text{og} \quad \sin 133\degree
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\cos 133\degree = -0.68 \quad \text{og} \quad \sin 133\degree = 0.73
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
$x$-koordinaten til punktet $P$ er $\cos 133\degree = -0.68$ og $y$-koordinaten til punktet $P$ er $\sin 133\degree = 0.73$. Dermed har vi at

$$
\cos 133\degree = -0.68 \quad \text{og} \quad \sin 133\degree = 0.73
$$
::::

:::::::::::::


::::::::::::::




:::::::::::::::




