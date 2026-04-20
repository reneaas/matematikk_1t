# Oppgaver: Cosinussetningen


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---

:::{cas-popup}
:::


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



:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 2
---
level: 1
---

:::{cas-popup}
:::


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


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3


En trekant $\triangle ABC$ er vist nedenfor.


:::{plot}
fontsize: 25
width: 60%
axis: equal
axis: off
let: l = 1
let: Ax = 0
let: Ay = 0
let: Bx = 5 * l
let: By = 0
let: Cx = 2 * l * cos(pi/3)
let: Cy = 2 * l * sin(pi/3)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
line-segment: (Cx, Cy), (Ax, Ay), solid, blue
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", center-right
text: Cx, Cy, "$C$", top-center
angle-arc: (Ax, Ay), 0.4, 0, 60, red
text: 0.4 * cos(pi/6), 0.4 * sin(pi/6), "$60^\circ$", top-right
text: 0.5 * (Ax + Bx), Ay - 0.1, "$5\ell$", bottom-center
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "$2\ell$", top-left
:::




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem et eksakt uttrykk for arealet av trekanten uttrykkt ved $\ell$.


::::{answer}
$$
T = \dfrac{5\sqrt{3}}{2} \cdot \ell^2
$$
::::


::::{solution}
Med arealsetningen får vi at

$$
T = \dfrac{1}{2} \cdot 2\ell \cdot 5\ell \cdot \sin 60\degree.
$$

Vi vet at $\sin 60\degree = \dfrac{\sqrt{3}}{2}$, som gir at

$$
T = \dfrac{1}{2} \cdot 2 \ell \cdot 5 \ell \cdot \dfrac{\sqrt{3}}{2} = \dfrac{5\sqrt{3}}{2} \cdot \ell^2.
$$
::::

:::::::::::::






:::::::::::::{tab-item} b
Bestem et eksakt uttrykk for lengden $BC$ uttrykt ved $\ell$.


::::{answer}
$$
BC = \sqrt{19} \cdot \ell
$$
::::


::::{solution}
Vi lar $x = BC$. Fra cosinussetningen får vi da at

$$
x^2 = (2 \ell)^2 + (5 \ell)^2 - 2 \cdot (2 \ell) \cdot (5 \ell) \cdot \cos 60\degree.
$$

Vi vet at $\cos 60\degree = \dfrac{1}{2}$, som gir at

$$
x^2 = 4 \ell^2 + 25 \ell^2 - 2 \cdot 2 \ell \cdot 5 \ell \cdot \dfrac{1}{2} = 19 \ell^2
$$

som betyr at

$$
x = \sqrt{19} \cdot \ell.
$$

Altså er $BC = \sqrt{19} \cdot \ell$.
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


En firkant $\square ABCD$ er vist nedenfor.


:::{plot}
fontsize: 25
axis: off
axis: equal
width: 50%
let: Ax = 0
let: Ay = 0
let: Bx = sqrt(3)
let: By = 0
let: Cx = Bx
let: Cy = By + 1
let: Dx = Cx + 3 * cos((90 + 180 - 120) * pi / 180)
let: Dy = Cy + 3 * sin((90 + 180 - 120) * pi / 180)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
line-segment: (Cx, Cy), (Dx, Dy), solid, blue
line-segment: (Dx, Dy), (Ax, Ay), solid, blue
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
let: ds = 0.2
line-segment: (Bx - ds, By), (Bx - ds, By + ds), solid, gray
line-segment: (Bx - ds, By + ds), (Bx, By + ds), solid, gray
angle-arc: (Cx, Cy), 0.2, 90 + 180 - 120, 90 + 180, red
text: 0.5 * (Ax + Bx), 0.5 * (Ay + By) - 0.1, "$\sqrt{3}$", bottom-center
text: 0.5 * (Ax + Dx), 0.5 * (Ay + Dy) - 0.1, "$\sqrt{7}$", bottom-left
text: 0.5 * (Bx + Cx) + 0.1, 0.5 * (By + Cy), "$1$", center-right
text: Cx - 0.18, Cy - 0.1, "$120^\circ$", bottom-left
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
Arealet av $\triangle ABC$ kan regnes ut direkte med grunnlinje $AB$ og høyde $BC$ (siden trekanten er rettvinklet):

$$
T_{\triangle ABC} = \dfrac{1}{2} \cdot AB \cdot BC = \dfrac{1}{2} \cdot \sqrt{3} \cdot 1 = \dfrac{\sqrt{3}}{2}.
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


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
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

:::{cas-popup}
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


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
aids: true
---


:::{cas-popup}
---
layout: sidebar
---
:::


En firkant $\square ABCD$ er vist nedenfor.


:::{plot}
fontsize: 25
width: 60%
axis: off
axis: equal
let: a = 1
let: Ax = 0
let: Ay = 0
let: Bx = a
let: By = 0
let: Cx = Bx + sqrt(2) * a * cos((180 - 75 - 30) * pi / 180)
let: Cy = By + sqrt(2) * a * sin((180 - 75 - 30) * pi / 180)
let: Dx = Ax + a * cos(120 * pi / 180)
let: Dy = Ay + a * sin(120 * pi / 180)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
line-segment: (Cx, Cy), (Dx, Dy), solid, blue
line-segment: (Dx, Dy), (Ax, Ay), solid, blue
line-segment: (Bx, By), (Dx, Dy), dashed, gray
angle-arc: (Ax, Ay), 0.15, 0, 120, red
angle-arc: (Bx, By), 0.2, 180 - 105, 180 - 105 + 75, red
angle-arc: (Dx, Dy), 0.3, 120 + 180, 120 + 180 + 30, red
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
text: Ax, Ay + 0.15, "$120^\circ$", top-right
text: Bx, By + 0.2, "$75^\circ$", top-left
text: Dx + 0.2, Dy - 0.22, "$30^\circ$", bottom-right 
text: 0.5 * (Ax + Bx), Ay, "$a$", bottom-center
text: 0.5 * (Bx + Cx), 0.5 * (By + Cy), "$\sqrt{2} \cdot a$", bottom-right
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


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 7
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


Nedenfor vises en regulær 5-kant med sidelengder $\ell$.



:::{plot}
axis: off
axis: equal
width: 50%
let: u = (180 - 108) * pi / 180
let: N = 5
let: l = 1
let: Ax = 0
let: Ay = 0
let: Bx = l
let: By = 0
let: Cx = Bx + l * cos(u)
let: Cy = By + l * sin(u)
let: Dx = Cx + l * cos(2 * u)
let: Dy = Cy + l * sin(2 * u)
let: Ex = Dx + l * cos(3 * u)
let: Ey = Dy + l * sin(3 * u)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
line-segment: (Cx, Cy), (Dx, Dy), solid, blue
line-segment: (Dx, Dy), (Ex, Ey), solid, blue
line-segment: (Ex, Ey), (Ax, Ay), solid, blue
line-segment: (Ax, Ay), (Cx, Cy), dashed, gray
line-segment: (Cx, Cy), (Ex, Ey), dashed, gray
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", center-right
text: Dx, Dy, "$D$", top-center
text: Ex, Ey, "$E$", center-left
angle-arc: (Bx, By), 0.15, 180 - 108, 180, red
text: Bx, By + 0.15, "$108^\circ$", top-left
fontsize: 25
text: 0.5 * (Ax + Bx), 0.5 * (Ay + By) - 0.1, "$\ell$", bottom-center
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


:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 8
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


:::::::::::::::{exercise} Oppgave 9
---
aids: true
---

:::{cas-popup}
---
layout: sidebar
---
:::


Nedenfor vises en regulær $7$-kant med sidelengder $2$. 

Bestem arealet av $7$-kanten.


:::{plot}
axis: off
axis: equal
width: 50%
let: N = 7
let: u = (180 - 128.57) * pi / 180
let: Ax = 0
let: Ay = 0
let: Bx = 2
let: By = 0
let: Cx = Bx + 2*cos(u)
let: Cy = By + 2*sin(u)
let: Dx = Cx + 2*cos(2*u)
let: Dy = Cy + 2*sin(2*u)
let: Ex = Dx + 2*cos(3*u)
let: Ey = Dy + 2*sin(3*u)
let: Fx = Ex + 2*cos(4*u)
let: Fy = Ey + 2*sin(4*u)
let: Gx = Fx + 2*cos(5*u)
let: Gy = Fy + 2*sin(5*u)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
line-segment: (Cx, Cy), (Dx, Dy), solid, blue
line-segment: (Dx, Dy), (Ex, Ey), solid, blue
line-segment: (Ex, Ey), (Fx, Fy), solid, blue
line-segment: (Fx, Fy), (Gx, Gy), solid, blue
line-segment: (Gx, Gy), (Ax, Ay), solid, blue
line-segment: (Ax, Ay), (Cx, Cy), dashed, gray
line-segment: (Ax, Ay), (Fx, Fy), dashed, gray
line-segment: (Cx, Cy), (Fx, Fy), dashed, gray
line-segment: (Cx, Cy), (Ex, Ey), dashed, gray
angle-arc: (Bx, By), 0.3, 180 - 128.57, 180, red
text: Bx, By + 0.25, "$128.57^\circ$", top-left
fontsize: 25
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", center-right
text: Dx, Dy, "$D$", top-right
text: Ex, Ey, "$E$", top-center
text: Fx, Fy, "$F$", top-left
text: Gx, Gy, "$G$", center-left
text: 0.5 * (Ax + Bx), 0.5 * (Ay + By), "$2$", bottom-center
:::



::::{answer}
$$
T_{\mathrm{7-kant}} \approx 14.5.
$$
::::


::::{solution}
Vi starter med å bestemme $AC$ ved hjelp av cosinussetningen. La $L = 2$ være sidelengdene i $7$-kanten slik at $L = AB = BC$. Da kan vi bestemme $AC$ som følger:

:::{figure} ./figurer/oppgaver/oppgave_9/AC.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

Altså er $AC \approx 3.6$.

Vi kan nå regne ut arealet til $\triangle ABC$, $\triangle CDE$ og $\triangle FGA$ siden alle disse trekantene er {popup}`kongruente.<To trekanter er kongruente hvis de er formlike og har nøyaktig samme størrelse.>` Men vi trenger å bestemme noen flere lengder og vinkler for å bestemme arealet av de resterende trekantene i figuren.

La oss lage en liste med mål:
1. Vi må bestemme lengden $CF$ og vinkelen $\angle FAC$ for å bestemme arealet av $\triangle ACF$
2. Vi må bestemme lengden vinkelen $\angle FCE$ for å bestemme arealet av $\triangle CEF$

Når vi har disse størrelsene kan vi bestemme arealet av de to resterende trekantene i figuren. Vi starter med å bestemme $CF$ og $\angle CAF$. I $\triangle ACF$ vet vi allerede at 

$$
AC = AF = 3.6
$$

Vi må for å kunne bruke cosinussetningen, må vi bestemme vinkelen $\angle FAC$ først. Først kan vi observere at $\angle CAB = \angle BCA$ og

$$
\angle CAB + \angle BCA + 128.57 \degree = 180 \degree \liff 2\cdot \angle CAB = 180 \degree - 128.57 \degree
$$

som betyr at 

$$
\angle CAB = 25.71 \degree.
$$

Videre kan vi observere at $\angle CAB = \angle GAF$ siden {popup}`$\triangle ABC \cong \triangle FGA$.<Trekantene er kongruente.>` Dermed følger det at 

\begin{align*}
    \angle CAB + \angle GAF + \angle FAC &= 128.57\degree \\
    \\
    2\cdot \angle CAB + \angle FAC &= 128.57\degree \\
    \\
    \angle FAC &= 128.57\degree - 2\cdot \angle CAB \\
    \\
    \angle FAC &= 128.57\degree - 2\cdot 25.71\degree \\
    \\
    \angle FAC &= 77.14\degree.
\end{align*}

Nå har vi opplysningene vi trenger for å bestemme sidelengden $CF$ med cosinussetningen:

:::{figure} ./figurer/oppgaver/oppgave_9/CF.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

Altså er $CF \approx 4.49$. Da har vi alle opplysninger vi trenger for å bestemme arealet av $\triangle ACF$.

Vi går nå videre til å bestemme $\angle CEF$ for å kunne bestemme arealet av $\triangle CEF$. Siden $\triangle ABC \cong \triangle CEF$, så følger det at 

$$
\angle DEF = \angle CAB = 25.71\degree.
$$

så vi har

$$
\angle DEF + \angle CEF = 128.57 \degree \liff \angle CEF = 128.57\degree - 25.71\degree
$$

som betyr at 

$$
\angle DEF = 102.86\degree.
$$

Nå har vi alle opplysninger vi trenger for å bestemme arealet av alle trekantene i figuren. Vi bruker arealsetningen til å bestemme arealet av hver trekant: 

\begin{align*}
    T_{\text{7-kant}} &= \underbrace{T_{\triangle ABC} + T_{\triangle CDE} + T_{\triangle FGA}}_{\displaystyle 3 \cdot T_{\triangle ABC}} + T_{\triangle ACF} + T_{\triangle CEF} \\
    \\
    &= 3\cdot T_{\triangle ABC} + T_{\triangle ACF} + T_{\triangle CEF}
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_9/areal.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

Altså er arealet av $7$-kanten 

$$
T_{\mathrm{7-kant}} \approx 14.5.
$$

::::


:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 10
En sirkel med radius $1$ er innskrevet i en regulær $6$-kant. 


:::{plot}
axis: off
axis: equal
width: 50%
let: r = 1
let: l = 2 * sqrt(3) / 3 * r
circle: (0, 0), r, solid, black
let: N = 6
repeat: n=0..N-1; line-segment: (l * cos(2 * pi / N * n), l * sin(2 * pi / N * n)), (l * cos(2 * pi / N * (n + 1)), l * sin(2 * pi / N * (n + 1))), solid, blue
repeat: n=0..N-1; line-segment: (0, 0), (l * cos(2 * pi / N * n), l * sin(2 * pi / N * n)), dashed, gray
line-segment: (0, 0), (r * cos(pi / 6), r * sin(pi / 6)), dashed, red
text: r * cos(pi / 6) / 2 + 0.1, r * sin(pi / 6) / 2 + 0.2, "$1$", center-center
fontsize: 25
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en eksakt verdi for omkretsen $\mathcal{O}$ av $6$-kanten.

::::{answer}
$$
\mathcal{O} = 4 \sqrt{3}
$$
::::


::::{solution}
Sirkelen er innskrevet i en regulær $6$-kant som betyr at **høyden** i trekanten er lik radius i sirkelen. Dermed er høyden $1$. 

Sentralvinkelen $v$ i hver trekant i $6$-kanten vil være

$$
v = \dfrac{360\degree}{6} = 60\degree.
$$

Deler vi opp hver av de $6$ trekantene i to like store mindre, rettvinklede trekanter, så vil vi få en rettvinkla trekant der den lengste kateten er lik høyden $1$, og trekanten blir er $30\degree$-$60\degree$-$90\degree$ trekant. Da følger det at den korteste kateten $x$ er halvparten av hypotenusen $2x$. Vi bruker Pytagoras' setning for å finne $x$:

$$
(2x)^2 = x^2 + 1^2 \liff 3x^2 = 1
$$

$$
x^2 = \dfrac{1}{3} \liff x = \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}.
$$

Vi har at $6$-kanten må bestå av $12$ slike deler som betyr at omkretsen til $6$-kanten er

$$
\mathcal{O} = 12x = 12 \cdot \dfrac{\sqrt{3}}{3} = 4 \sqrt{3}.
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
En eksakt verdi for arealet $T$ av $6$-kanten.


::::{answer}
$$
T = 2 \sqrt{3}
$$
::::


::::{solution}
Sidelengdene til de $6$ trekantene som bygger opp $6$-kanten har sidelengder $$\ell = 2x$ der $x = \dfrac{\sqrt{3}}{3}$ som vi fant i oppgave **a**. Altså blir sidelengdene som spenner ut hver trekant i $6$-kanten lik

$$
\ell = 2x = 2 \cdot \dfrac{\sqrt{3}}{3} = \dfrac{2\sqrt{3}}{3}.
$$



Da kan vi bruke arealsetningen for å finne arealet av hver trekant:

$$
\begin{align*}
T_{\triangle} &= \dfrac{1}{2} \cdot \ell^2 \cdot \sin(60\degree) \\
\\
&= \dfrac{1}{2} \cdot \left(\dfrac{2\sqrt{3}}{3}\right)^2 \cdot \dfrac{\sqrt{3}}{2} \\
\\
&= \dfrac{1}{2} \cdot \dfrac{12}{9} \cdot \dfrac{\sqrt{3}}{2} \\
\\
&= \dfrac{1}{2} \cdot \dfrac{4}{3} \cdot \dfrac{\sqrt{3}}{2} \\
\\
&= \dfrac{2\sqrt{3}}{6} \\
\\
&= \dfrac{\sqrt{3}}{3}.
\end{align*}
$$


Siden det er $6$ slike trekanter i $6$-kanten, så blir arealet av $6$-kanten:

$$
T = 6 \cdot T_{\triangle} = 6 \cdot \dfrac{\sqrt{3}}{3} = 2 \sqrt{3}.
$$

::::

:::::::::::::

::::::::::::::

:::::::::::::::














