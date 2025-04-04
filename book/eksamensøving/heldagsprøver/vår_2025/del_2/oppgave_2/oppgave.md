:::::::::::::::{admonition} Oppgave 2
---
class: check
---
En regulær 6-kant er en 6-kant der alle sidene er like lange. 

En sirkel med radius $1$ er innskrevet i en regulær 6-kant. En trekant har et hjørne i sentrum av sirkelen. Se figuren nedenfor.


:::{figure} ./figurer/del_2/oppgave_2/figur.svg
---
width: 80%
class: no-click
---
:::


Bruk trigonometri til å bestemme arealet av 6-kanten.

:::::{admonition} Fasit
---
class: answer, dropdown
---
Arealet av 6-kanten er $2\sqrt{3}$.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
6-kanten består av 6 like store trekanter. Vi trenger derfor å bestemme arealet av én slik trekant først. La trekanten som er tegnet inn være $\triangle ABC$ der $A$ er hjørnet i sentrum av sirkelen. Vi kan først merke oss at sentralvinkelen $\angle A = u$ vil være 

$$
\angle A = \frac{360\degree}{6} = 60\degree.
$$

siden det er $360\degree$ i en hel sirkel og det er 6 like store toppvinkler i de 6 trekantene vi har plass til med toppunkt i sentrum av sirkelen.

Trekant $\triangle ABC$ er *minimum* en likebeint trekant siden $AB = AC$. Videre er $\angle A = 60\degree$ som betyr at $\angle B = \angle C = 60\degree$ og trekanten er derfor også *likesidet*. Vi kan derfor lage følgende hjelpefigur der vi trekker en **midtnormal** fra hjørne $A$ ned på $BC$ som deler $\angle A$ nøyaktig i to like store vinkler, og tilsvarende deler $BC$ i to like lange linjestykker. Siden radien i sirkelen er $1$, følger det at lengden på midtnormalen er $1$. Vi lar sidelengdene i trekanten være $\ell$. Se figuren nedenfor.

:::{figure} ./figurer/del_2/oppgave_2/hjelpefigur.svg
---
width: 80%
class: no-click
---
:::

> I utregningen nedenfor bruker vi at $\sin 60 \degree = \cos 30 \degree = \dfrac{\sqrt{3}}{2}$.

Fra definisjonen av cosinus, kan vi da skrive 

$$
\cos 30 \degree = \dfrac{1}{\ell} \liff \ell = \dfrac{1}{\cos 30 \degree} = \dfrac{1}{\sqrt{3}/2} = \dfrac{2}{\sqrt{3}}.
$$

Deretter bruker vi arealsetningen for å bestemme arealet av trekant $\triangle ABC$:

$$
T_{\triangle ABC} = \dfrac{1}{2} \cdot \ell^2 \cdot \sin 60\degree = \dfrac{1}{2} \cdot \left(\dfrac{2}{\sqrt{3}}\right)^2 \cdot \dfrac{\sqrt{3}}{2} = \dfrac{1}{2} \cdot \dfrac{4}{3} \cdot \dfrac{\sqrt{3}}{2} = \dfrac{\sqrt{3}}{3}.
$$


6-kanten består av 6 slike trekanter, så det samlede arealet blir da 

$$
T_{6-\mathrm{kant}} = 6 \cdot T_{\triangle ABC} = 6 \cdot \dfrac{\sqrt{3}}{3} = 2\sqrt{3}.
$$

:::::
:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 3
---
class: check
---


:::::::::::::::

