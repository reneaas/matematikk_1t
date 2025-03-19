# Enhetssirkelen


::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive hvordan $\cos v$ og $\sin v$ henger sammen med koordinatene til et punkt $P$ på enhetssirkelen.
* Kunne bruke enhetssirkelen til å bestemme $\cos v$ og $\sin v$ for vinkler $v \in [0, 360\degree\rangle$.
::::

Så langt har vi brukt rettvinklede trekanter for å beskrive sinus og cosinus som forholdstallet mellom to sider. Når vi jobbet med arealsetningen, fant vi at vi også kunne gi en meningsfull definisjon av $\sin v$ selv om $v$ var en stump vinkel. Måten vi gjorde det på, var å bruke en rettvinklet trekant på utsiden av trekanten for å finne høyden i trekanten slik at vi kunne bruke definisjonen av sinus. 

Men $\sin v$ og $\cos v$ forteller oss indirekte hvor stor en vinkelbue $v$ er. I Utforsk 1 nedenfor skal vi se hvordan vi kan uttrykke $\sin v$ og $\cos v$ dersom vi jobber med en rettvinklet trekant der hypotenusen er $1$.



:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Nedenfor vises en rettvinklet trekant der hypotenusen er $1$. Den ene kateten har lengde $x$ og den andre kateten har lengde $y$.


:::{figure} ./figurer/utforsk/utforsk_1/figur.svg
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

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\sin v$ for trekanten.

:::::::::::::


:::::::::::::{tab-item} c
Forklar at 

$$
(\cos v)^2 + (\sin v)^2 = 1
$$

Hvorfor tror du dette kalles for **Pytagoras' identitet**?

:::::::::::::

::::::::::::::

:::::::::::::::

---

Vi har nå sett at $\sin v$ og $\cos v$ får en spesielt enkel form dersom vi jobber med en rettvinklet trekant der hypotenusen er $1$. Men rettvinklede trekanter begrenser oss til å beskrive vinkelbuer som ligger mellom $0\degree$ og $90\degree$. For å kunne beskrive vinkelbuer som er større enn $90\degree$, kan vi utvide definisjonen vår ved å ta utgangspunkt i en sirkel som har radius $1$. Denne sirkelen kalles for **enhetssirkelen**. Denne definisjonen vil fortsatt gi akkurat de samme verdiene når vinkelen er mellom $0\degree$ og $90\degree$, men lar oss også definere $\sin v$ og $\cos v$ for vinkler $v \in [0\degree, 360\degree\rangle$.


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

:::::::::::::::{admonition} Utforsk 2
---
class: explore
---
Nedenfor vises enhetssirkelen med et punkt $P(x, y)$ tegnet inn på sirkelen. En trekant er tegnet inn der hypotenusen går fra origo opp til punktet $P$.

:::{figure} ./figurer/utforsk/utforsk_2/enhetssirkelen.svg
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




