# Oppgaver: Cosinussetningen


:::::::::::::::{problem} Oppgave 1
---
level: 1
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $x$ i trekanten nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_1/a/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::



::::{answer}
$$
x \approx 4.14
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_1/a/sol.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

$$
x \approx 4.14
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $x$ i trekanten nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_1/b/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::{answer}
$$
x \approx 3.99
$$
::::

::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_1/b/sol.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

$$
x \approx 3.99
$$
::::



:::::::::::::


:::::::::::::{tab-item} c
Bestem $x$ i trekanten nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_1/c/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::{answer}
$$
x \approx 2.99
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_1/c/sol.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

$AB < AC = 5$ som betyr at $AB \approx 5.59$ ikke er en mulighet. Dermed har vi at

$$
x \approx 2.99
$$
::::



:::::::::::::

::::::::::::::

:::{cas-popup} 420 500
:::


:::::::::::::::




---


:::::::::::::::{problem} Oppgave 2
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $x$ i trekanten nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_2/a/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{answer}
$$
x \approx 117.28\degree
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_2/a/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::


$$
x \approx 117.28\degree
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $x$ i trekanten nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_2/b/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{answer}
$$
x \approx 104.48\degree
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_2/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::


$$
x \approx 104.48\degree
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $x$ i trekanten nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_2/c/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{answer}
$$
x \approx 58.81\degree
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_2/c/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::


$$
x \approx 58.81\degree
$$
::::


:::::::::::::

::::::::::::::

:::{cas-popup} 420 500
:::

:::::::::::::::



---



:::::::::::::::{problem} Oppgave 3
---
level: 2
---
En trekant $\triangle ABC$ er vist nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_3/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem et eksakt uttrykk for arealet av trekanten uttrykkt ved $\ell$.


::::{answer}
$$
T = \dfrac{5}{2}\sqrt{3} \cdot \ell^2
$$
::::


::::{solution}
Bruker arealsetningen og regner ut med CAS:

:::{figure} ./figurer/oppgaver/oppgave_3/a/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::
$$
T = \dfrac{5}{2}\sqrt{3} \cdot \ell^2
$$
::::

:::::::::::::






:::::::::::::{tab-item} b
Bestem et eksakt uttrykk for lengden $BC$ uttrykt ved $\ell$.


::::{answer}
$$
x = \sqrt{19} \cdot \ell
$$
::::


::::{solution}
La $x = BC$. Vi bruker cosinussetningen til å bestemme $x$ uttrykt ved $\ell$:

:::{figure} ./figurer/oppgaver/oppgave_3/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi antar at $\ell > 0$, som betyr at 

$$
x = \sqrt{19} \cdot \ell
$$
::::

:::::::::::::


::::::::::::::


:::{cas-popup} 420 500
:::

:::::::::::::::


---


:::::::::::::::{problem} Oppgave 4
---
level: 2
---
En firkant $\square ABCD$ er vist nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_4/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem omkretsen $\mathcal{O}$ av $\square ABCD$.


::::{answer}
$$
\mathcal{O} = 4 + \sqrt{3} + \sqrt{7}.
$$
::::

::::{solution}
Vi deler opp firkant $\square ABCD$ i to trekanter $\triangle ABC$ og $\triangle ACD$.

Først bestemmer vi lengden på diagonalen $AC$ som vi kan gjøre med Pytagoras' setning:

$$
AC^2 = 1^2 + (\sqrt{3})^2 = 1 + 3 = 4 \limplies AC = 2
$$

Vi kan merke oss at $\triangle ABC$ er en $30\degree$-$60\degree$-$90\degree$ trekant fordi den korteste kateten er halvparten av hypotenusen. Da følger det at 

$$
\angle BCA = 60\degree \limplies \angle ACD = 60\degree.
$$

Da kan vi bruke cosinussetningen til å bestemme lengden $x = CD$. Vi regner det ut med CAS:

:::{figure} ./figurer/oppgaver/oppgave_4/a/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er $CD = 3$. Dermed blir omkretsen til $\square ABCD$:

$$
\mathcal{O} = AB + BC + CD + DA = \sqrt{3} + 1 + 3 + \sqrt{7} = 4 + \sqrt{3} + \sqrt{7}.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem arealet $T$ av $\square ABCD$.


::::{answer}
$$
T = 2\sqrt{3}
$$
::::

::::{solution}
Arealet av $\triangle ABC$ kan regnes ut direkte:

$$
T_{\triangle ABC} = \dfrac{1}{2} \cdot AB \cdot AC = \dfrac{1}{2} \cdot \sqrt{3} \cdot 1 = \dfrac{\sqrt{3}}{2}.
$$

For $\triangle ACD$ kan vi bruke arealsetningen ut ifra vinkel $\angle ACD$. Vi regner det ut med CAS:


:::{figure} ./figurer/oppgaver/oppgave_4/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed følger det at arealet av $\square ABCD$ er

$$
T = T_{\triangle ABC} + T_{\triangle ACD} = \dfrac{\sqrt{3}}{2} + \dfrac{3\sqrt{3}}{2} = 2\sqrt{3}.
$$


::::

:::::::::::::


::::::::::::::


:::{cas-popup} 420 500
:::


:::::::::::::::


---


:::::::::::::::{problem} Oppgave 5
---
level: 2
---
Nedenfor vises en firkant $\square ABCD$. 

:::{figure} ./figurer/oppgaver/oppgave_5/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem omkretsen av $\square ABCD$.


::::{answer}
$$
\mathcal{O} \approx 9.33.
$$
::::

::::{solution}
Vi bruker cosinussetningen på $\triangle BCD$ for å bestemme lengden $BD$:

:::{figure} ./figurer/oppgaver/oppgave_5/a/sol_1.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som gir

$$
BD \approx 3.13.
$$

Deretter bruker vi cosinussetningen på $\triangle ABD$ for å bestemme lengden $AB$:

:::{figure} ./figurer/oppgaver/oppgave_5/a/sol_2.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som gir 

$$
AB \approx 1.33
$$

Omkretsen til $\square ABCD$ er derfor

$$
\mathcal{O} = AB + BC + CD + DA \approx 1.33 + 2 + 4 + 2 = 9.33.
$$


::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem arealet av $\square ABCD$.


::::{solution}
Fra oppgave **a** fant vi at 

$$
AB \approx 1.33 \quad \text{og} \quad BD \approx 3.13.
$$

Arealet av $\triangle ABD$ kan regnes ut med arealsetningen:

$$
T_{\triangle ABD} = \dfrac{1}{2} \cdot AB \cdot AD \cdot \sin \angle A
$$

og tilsvarende for $\triangle BCD$:

$$
T_{\triangle BCD} = \dfrac{1}{2} \cdot BC \cdot BD \cdot \sin \angle CBD
$$

som vi gjør med CAS:

:::{figure} ./figurer/oppgaver/oppgave_5/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::


Altså er 

$$
T_{\square ABCD} \approx 3.95. 
$$

::::

:::::::::::::

::::::::::::::

:::{cas-popup} 420 500
:::

:::::::::::::::


---


:::::::::::::::{problem} Oppgave 6
---
level: 2
---

En firkant $\square ABCD$ er vist nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_6/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem et eksakt uttrykk for $BD$ uttrykt ved $a$.



::::{answer}
$$
BD = \sqrt{3} \cdot a.
$$
::::


::::{solution}
La $x = BD$. Vi kan merke oss at siden $\angle ADB = 30 \degree$ og $\angle A = 120\degree$, så følger det at $\angle ABD = 30\degree$ som betyr at $\triangle ABD$ er en likebeint trekant. Dermed er $AB = AD = a$. Da kan bruke cosinussetningen til å bestemme $x$:

:::{figure} ./figurer/oppgaver/oppgave_6/a/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed er 

$$
x = BD = \sqrt{3} \cdot a.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem et eksakt uttrykk for omkretsen til $\square ABCD$.


::::{answer}
$$
\mathcal{O} = \dfrac{1}{2}\cdot a \cdot \left(3\sqrt{2} + \sqrt{6} + 4\right).
$$
::::

::::{solution}
Vi bestemmer lengden $CD$ ved å bruke cosinussetningen ut ifra vinkel $\angle DBC$ som gir

$$
CD^2 = BC^2 + BD^2 - 2 \cdot BC \cdot BD \cdot \cos(75\degree).
$$

Vi gjør utregningene med CAS:

:::{figure} ./figurer/oppgaver/oppgave_6/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Det er bare den positive løsningen som gir mening, så vi får at 

$$
CD = \dfrac{\sqrt{2} + \sqrt{6}}{2} \cdot a
$$

der $a = |a|$ siden $a$ er positiv. Nå kjenner vi alle sidelenger i $\square ABCD$ og kan regne ut omkretsen:


$$
\mathcal{O} = AB + BC + CD + DA
$$

vi gjør selve utregningen med CAS:

:::{figure} ./figurer/oppgaver/oppgave_6/b/sol_omkrets.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er omkretsen til $\square ABCD$:

$$
\mathcal{O} = \dfrac{1}{2}\cdot a \cdot \left(3\sqrt{2} + \sqrt{6} + 4\right).
$$



::::

:::::::::::::

:::::::::::::{tab-item} c
Bestem $a$ slik at arealet av firkanten er $\sqrt{3}$.


::::{answer}
$$
a = \sqrt{6} - \sqrt{2}
$$
::::

::::{solution}
Vi setter opp en likning der vi uttrykket arealet til $\square ABCD$ ved $a$ ved å bruke arealsetningen på $\triangle ABD$ og $\triangle BCD$, som vi løser med CAS:

:::{figure} ./figurer/oppgaver/oppgave_6/c/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::


Altså er arealet av $\square ABCD$ lik $\sqrt{3}$ dersom

$$
a = \sqrt{6} - \sqrt{2}
$$


::::

:::::::::::::

::::::::::::::


:::{cas-popup} 420 500
:::



:::::::::::::::


---



:::::::::::::::{problem} Oppgave 7
---
level: 2
---
Nedenfor vises en regulær 5-kant $ABCDE$. Alle sidelengdene er $\ell$ og vinklene i hvert hjørne er $108 \degree$.

:::{figure} ./figurer/oppgaver/oppgave_7/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem et eksakt uttrykk for $AC$ uttrykt ved $\ell$.


::::{answer}
$$
AC = \dfrac{1}{2}\left(\sqrt{5} + 1\right)\cdot \ell
$$
::::

::::{solution}
Vi bruker cosinussetningen med $AB = BC = \ell$ som gir:

:::{figure} ./figurer/oppgaver/oppgave_7/a/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::


$$
AC = \dfrac{1}{2}\left(\sqrt{5} + 1\right)\cdot \ell
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem et eksakt uttrykk for arealet av 5-kanten uttrykt ved $\ell$.


::::{answer}
$$
T_{ABCDE} = \dfrac{1}{4} \sqrt{5\left(2\sqrt{5} + 5\right)} \cdot \ell^2
$$
::::



::::{solution}
Fra figuren, kan vi merke oss at 5-kant $ABCDE$ er delt opp i tre trekanter $\triangle ABC$, $\triangle ACE$ og $\triangle CDE$. Vi kan også merke oss at $\triangle ABC$ og $\triangle CDE$ er **kongruente** (de er formlike *og* like store) fordi $\angle D = \angle B$ og $CD = DE = \ell$. Dermed kan vi uttrykke arealet av 5-kanten som 

$$
T_{ABCDE} = T_{\triangle ABC} + T_{\triangle ACE} + T_{\triangle CDE} = 2T_{\triangle ABC} + T_{\triangle ACE}.
$$

Arealet av $\triangle ABC$ kan regnes ut med arealsetningen:

$$
T_{\triangle ABC} = \dfrac{1}{2} \ell^2 \cdot \sin(108\degree).
$$

I $\triangle ACE$ kan vi konkludere at $AC = CE$ ettersom de er tilsvarende sider i $\triangle ABC$ og $\triangle CDE$. Vi trenger å kjenne til vinkelen som spenner ut av sidene $AC$ og $CE$. Vi bruker en hjelpefigur for å bestemme vinkelen:

:::{figure} ./figurer/oppgaver/oppgave_7/hjelpefigur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Her kan vi se at 

$$
\angle C = 108\degree = \gamma + 2\alpha. 
$$

Men vi vet også at 

$$
2\alpha + 108\degree = 180\degree \liff 2\alpha = 72\degree
$$

som betyr at 

$$
108\degree = \gamma + 2\alpha = \gamma + 72\degree \liff \gamma = 36\degree.
$$


Da følger det at arealet at $\triangle ACE$ er

$$
T_{\triangle ACE} = \dfrac{1}{2} AC^2 \cdot \sin(36\degree).
$$

Vi regner ut med CAS:

:::{figure} ./figurer/oppgaver/oppgave_7/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed finner vi at arealet av $5$-kanten er 

$$
T_{ABCDE} = \dfrac{1}{4} \sqrt{5\left(2\sqrt{5} + 5\right)} \cdot \ell^2
$$



::::



:::::::::::::

::::::::::::::


:::{cas-popup} 420 500
:::

:::::::::::::::


---

:::::::::::::::{problem} Oppgave 8
---
level: 2
---
Anna jobber med å finne en ukjent side $x$ i trekant. <br>
Hun har brukt cosinussetningen og har satt opp likningen

$$
14^2  = 16^2 + x^2 - 16x. 
$$


Hvilke opplysninger kan Anna ha fått om trekanten?

::::{solution}
Cosinussetningen kan skrives som 

$$
a^2 = b^2 + c^2 - 2\cdot b \cdot c \cdot \cos A. 
$$

Sammenlikner vi likningen ovenfor med likningen til Anna, kan vi se at det passer dersom 

$$
a = 14 \and b = 16 \and c = x \and \cos A = \dfrac{1}{2}
$$

Det betyr at 

$$
A = 60 \degree.
$$

Dette er en mulighet for opplysningene Anna kan ha fått.

::::


::::::::::::::

:::::::::::::::



---


:::::::::::::::{problem} Oppgave 9
---
level: 3
---
Nedenfor vises en regulær $7$-kant med sidelengder $2$. 

Bestem arealet av $7$-kanten.

:::{figure} ./figurer/oppgaver/oppgave_9/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::{answer}
$$
T_{\mathrm{7-kant}} \approx 14.55.
$$
::::



:::{cas-popup} 420 500
:::

:::::::::::::::














