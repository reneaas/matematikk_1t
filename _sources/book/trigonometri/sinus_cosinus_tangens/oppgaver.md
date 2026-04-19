# Oppgaver: Sinus, cosinus og tangens

:::::::::::::::{exercise} Oppgave 1
:::{plot}
width: 100%
align: right
triangle: sss=(8, 10, 6), angles=(A, B, C), angle-radius=50, side-labels=(AB=exact, BC=exact, ,CA=exact), side-offset=20
axis: off
axis: equal
fontsize: 34
nocache:
:::


I figuren til høyre vises en trekant $\triangle ABC$.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts 
---
:::::::::::::{tab-item} a
Bestem $\sin B$ og $\cos B$. 


:::{answer}
$$
\sin B = \dfrac{6}{10} = \dfrac{3}{5} \quad \quad \quad \cos B = \dfrac{8}{10} = \dfrac{4}{5}
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\tan B$. 

:::{answer}
$$
\tan B = \dfrac{6}{8} = \dfrac{3}{4}
$$
:::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $\sin C$ og $\cos C$.


:::{answer}
$$
\sin C = \dfrac{8}{10} = \dfrac{4}{5} \quad \quad \quad \cos C = \dfrac{6}{10} = \dfrac{3}{5}
$$
:::


:::::::::::::


:::::::::::::{tab-item} d
Bestem $\tan C$.

:::{answer}
$$
\tan C = \dfrac{8}{6} = \dfrac{4}{3}
$$
:::

:::::::::::::

::::::::::::::


:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 2
:::{plot}
width: 100%
align: right
triangle: sss=(3, sqrt(3), 2 * sqrt(3)), angles=(A, B, C), angle-radius=20, side-labels=(AB=exact, CA=exact), side-offset=25
axis: off
axis: equal
fontsize: 34
nocache:
:::

I figuren til høyre vises en trekant $\triangle ABC$.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $BC$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
BC = \sqrt{3}. 
$$
:::

:::::::::::::

:::::::::::::{tab-item} b
Bestem $\sin A$ og $\cos A$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\sin A = \dfrac{1}{2} \quad \quad \quad \cos A = \dfrac{\sqrt{3}}{2}
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
Bestem $\tan A$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\tan A = \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}
$$
:::

:::::::::::::


:::::::::::::{tab-item} d
Bestem $\sin C$ og $\cos C$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\sin C = \dfrac{\sqrt{3}}{2} \quad \quad \quad \cos C = \dfrac{1}{2}
$$
:::

:::::::::::::

:::::::::::::{tab-item} e
Bestem $\tan C$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\tan C = \sqrt{3}
$$
:::

:::::::::::::
::::::::::::::




:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 3

::::{hints} Hvordan regne ut sinus og cosinus med CAS
> I gif-en nedenfor viser vi hvordan man bruker CAS til å bestemme $\sin v$, $\cos v$ og $\tan v$ for en vinkel $v = 30\degree$ i en rettvinklet trekant. For å få gradertegn $\degree$ må du:
> 1. Trykke på "option + o" på tastaturet på **macOS**.
> 2. Trykke på "Alt + o" på tasteturet på **Windows**.

:::{figure} ./gifer/tutorial_1.webp
---
class: no-click, adaptive-figure
width: 80%
---
:::

::::



:::{plot}
width: 100%
align: right
triangle: sss=(8 * cos(pi/5), 8 * sin(pi/5), 8), angles=(A, B, C), angle-radius=60, side-labels=(AB=exact), side-offset=25, angle-labels=(A=numeric), angle-offset=24
axis: off
axis: equal
fontsize: 34
nocache:
:::

En trekant $\triangle ABC$ er vist til høyre.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::


Regn ut $\sin A$ og $\cos A$ med CAS.


:::{clear}
:::


::::{answer}
$$
\sin A = \dfrac{1}{4}\sqrt{2\left(5 - \sqrt{5}\right)} \and \cos B = \dfrac{1}{4} \left(\sqrt{5} + 1\right)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



Bruk trigonometri til å bestemme $AC$.

:::{clear}
:::

::::{answer}
$$
AC = 8
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bruk trigonometri til å bestemme $BC$.

:::{clear}
:::

::::{answer}
$$
BC = 2\sqrt{2(-\sqrt{5} + 5)}
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 4

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS til å regne ut $\sin 45^\circ$, $\cos 45^\circ$ og $\tan 45^\circ$.

:::{clear}
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_4/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er 

$$
\sin 45^\circ = \frac{\sqrt{2}}{2} \quad \quad \quad \cos 45^\circ = \frac{\sqrt{2}}{2} \quad \quad \quad \tan 45^\circ = 1
$$
::::

:::::::::::::

:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS til å regne ut $\sin 60^\circ$, $\cos 60^\circ$ og $\tan 60^\circ$.


:::{clear}
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_4/b.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er 

$$
\sin 60^\circ = \frac{\sqrt{3}}{2} \quad \quad \quad \cos 60^\circ = \frac{1}{2} \quad \quad \quad \tan 60^\circ = \sqrt{3}
$$
::::

:::::::::::::
::::::::::::::


:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 5
---
level: 1
---
> I denne oppgaven skal du bruke trigonometri og CAS til å bestemme ukjente sidelenger i rettvinklede trekanter.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::


I figuren nedenfor vises en rettvinklet trekant.

Bruk CAS til å bestemme $x$. 

:::{figure} ./figurer/oppgaver/oppgave_5/a.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::




::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_5/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed er $x = 10$. 

::::

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


I figuren nedenfor vises en rettvinklet trekant.

Bruk CAS til å bestemme $x$. 

:::{figure} ./figurer/oppgaver/oppgave_5/b.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::




::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_5/b.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed er $x = 2$. 

::::

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


I figuren nedenfor vises en rettvinklet trekant.

Bruk CAS til å bestemme $x$. 

:::{figure} ./figurer/oppgaver/oppgave_5/c.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_5/c.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed er $x = 4\sqrt{2}$. 

::::

:::::::::::::

:::::::::::::{tab-item} d

:::{cas-popup}
---
layout: sidebar
---
:::



I figuren nedenfor vises en rettvinklet trekant.

Bruk CAS til å bestemme $x$.

:::{figure} ./figurer/oppgaver/oppgave_5/d.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::




::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_5/d.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er $x = 4$.
::::

:::::::::::::


:::::::::::::{tab-item} e


:::{cas-popup}
---
layout: sidebar
---
:::



I figuren nedenfor vises en rettvinklet trekant.

Bruk CAS til å bestemme $x$.

:::{figure} ./figurer/oppgaver/oppgave_5/e.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_5/e.png
---
width: 100%
class: no-click, adaptive-figure
---
:::
Altså er $x = 1.25$.
::::

:::::::::::::


:::::::::::::{tab-item} f

:::{cas-popup}
---
layout: sidebar
---
:::



I figuren nedenfor vises en rettvinklet trekant.

Bruk CAS til å bestemme $x$.


:::{figure} ./figurer/oppgaver/oppgave_5/f.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::



::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_5/f.png
---
width: 100%
class: no-click, adaptive-figure
---
:::
Altså er $x = 3.22$.
::::

:::::::::::::

::::::::::::::


:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 6
> I denne oppgaven skal du lære å utlede eksakte verdier for sinus og cosinus når vinklene er $30^\circ$ og $60^\circ$. Disse verdiene er viktige å **huske** utenat, men det er enklere å huske dem dersom du vet hvor de kommer fra. 

:::{plot}
width: 100%
align: right
axis: equal
axis: off
triangle: sss=(2, 2, 2), angles=(A, B, C), side-labels=(AB=exact, BC=exact, CA=exact), angle-radius=30
fontsize: 32
:::



En likesidet trekant $\triangle ABC$ er vist i figuren til høyre. 


:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem høyden $h$ i trekanten. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h = \sqrt{3}. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk trekanten til å bestemme en eksakt verdi for $\sin 60^\circ$ og $\cos 60^\circ$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\sin 60^\circ = \frac{\sqrt{3}}{2} \quad \quad \quad \cos 60^\circ = \frac{1}{2}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bruk trekanten til å bestemme en eksakt verdi for $\sin 30^\circ$ og $\cos 30^\circ$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\sin 30^\circ = \frac{1}{2} \quad \quad \quad \cos 30^\circ = \frac{\sqrt{3}}{2}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Vis at 

$$
(\cos v)^2 + (\sin v)^2 = 1
$$

for $v = 30^\circ$ og $v = 60^\circ$.

:::::::::::::

::::::::::::::



:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 7
> I denne oppgaven skal du lære hvordan man kommer fram til sinus og cosinus når vinkelen er $45^\circ$. Det er også viktig å kunne disse verdiene utenat. Igjen – det er enklest å huske dersom man vet hvordan man kommer fram til dem.

:::{plot}
width: 100%
align: right
triangle: sss=(1, 1, sqrt(2)), angles=(A, B, C), side-labels=(CA=exact), angle-radius=30, angle-labels=(A=numeric, C=numeric)
fontsize: 32
axis: off
axis: equal
:::



:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem sidelengdene $AB$ og $BC$. 


::::{answer}
$$
AB = BC = 1
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk trigonometri til å bestemme de eksakte verdiene for $\sin 45\degree$ og $\cos 45\degree$.


::::{answer}
$$
\sin 45^\circ = \frac{\sqrt{2}}{2} \quad \quad \quad \cos 45^\circ = \frac{\sqrt{2}}{2}
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
I en matematikkbok står det følgende:

::::::::::::::{admonition} Setning
---
class: summary
---
For en vinkel $v$, gjelder

$$
2 \sin (v) \cdot \cos (v) = \sin (2\cdot v)
$$

::::::::::::::

Vis at formelen stemmer for trekanten nedenfor med $v = 30^\circ$.


:::{figure} ./figurer/oppgaver/oppgave_8/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::



::::::::::::::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9
---
level: 2
---
**Snells** lov forteller oss at når lys går fra luft til vann, vil lyset brytes slik at lysstrålen sin retning i luft og vann oppfyller

$$
\sin u = 1.33 \cdot \sin v
$$


:::{cas-popup} 350 500
:::

:::{figure} ./figurer/oppgaver/oppgave_9/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor stor vinkel $u$ må lyset ha for at vinkelen etter brytning i vannet skal være $v = 30^\circ$?



::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_9/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

$u \approx 41.68 \degree$.
::::


:::::::::::::


:::::::::::::{tab-item} b
Hva blir retningen til lysstrålen i vannet når $u$ nærmer seg $0^\circ$. Gi en praktisk tolkning av svaret.

::::{admonition} Fasit
---
class: answer, dropdown
---
Når $u \approx 0^\circ$, vil $\sin u \approx 0$ og dermed $\sin v \approx 0$. Dermed vil lysstrålen gå parallelt med innfallsloddet og vannstrålen endrer ikke retning når den går gjennom vannoverflaten. Det skjer altså ingen brytning.
::::

:::::::::::::

::::::::::::::



:::::::::::::::




---

:::::::::::::::{exercise} Oppgave 10 
---
level: 3
---
En lysstråle har beveget seg fra et punkt $A(0, 1)$ i luft til et punkt $B(10, -1)$ i vann. Lyset traff vannoverflaten i et punkt $M(x, 0)$. Alle avstander er i kilometer.

I figuren nedenfor vises en mulig bane for lysstrålen.

:::{figure} ./figurer/oppgaver/oppgave_10/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::{cas-popup} 350 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
Lag en modell $L_\text{luft}$ som beskriver hvor mange kilometer $L_\text{luft}(x)$ lysstrålen har beveget seg i luft før den traff vannoverflaten i punktet $M(x, 0)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
L_\text{luft}(x) = \sqrt{x^2 + 1}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag en modell $L_\text{vann}$ som beskriver hvor mange kilometer $L_\text{vann}(x)$ lysstrålen har beveget seg i vann etter at den traff vannoverflaten i punktet $M(x, 0)$ og endte opp i $B(10, -1)$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
L_\text{vann}(x) = \sqrt{(10 - x)^2 + 1}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Lys beveger seg med en fart på ca. 300 000 km/s i luft og ca. 225 000 km/s i vann. 

Lag en modell $T$ som beskriver hvor mange sekunder $T(x)$ det tar for lysstrålen å bevege seg fra $A$ til $B$ via punktet $M(x, 0)$.

::::{admonition} Hint: Vei-fart-tid
---
class: dropdown, hints
---
For en strekning $L$, en fart $v$ og en tid $t$, gjelder

$$
L = v \cdot t.
$$
::::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T(x) = \dfrac{L_\text{luft}(x)}{300000} + \dfrac{L_\text{vann}(x)}{225000}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem i hvilket punkt $M(x, 0)$ lysstrålen må ha truffet dersom lysstrålen skal bruke kortest mulig tid mellom $A$ og $B$. 



::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_10/d.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså gikk vannstrålen gjennom $M(8.88, 0)$ hvis den skulle bruke kortest mulig tid fra $A$ til $B$.
::::


:::::::::::::


:::::::::::::{tab-item} e
Bruk svaret ditt fra **d** til å vise at 

$$
\dfrac{\sin u}{\sin v} = 1.33
$$

:::{figure} ./figurer/oppgaver/oppgave_9/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::



::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_10/e.png
---
width: 100%
class: no-click, adaptive-figure
---
:::
::::


:::::::::::::



::::::::::::::





:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 11
---
level: 2
---

<br>

:::{cas-popup} 350 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Månen har en radius på ca. 1737 km og er ca. 384 400 km unna jorden.

Bestem hvor stor vinkel $v$ månen dekker på himmelen sett fra jorden.



::::{admonition} Fasit
---
class: answer, dropdown
---
$$
v = 0.5 \degree
$$  
::::


:::::::::::::


:::::::::::::{tab-item} b 
Andromedagalaksen er vår nærmeste nabogalakse. Den er er ca. 200 000 lysår i diameter og 2.5 millioner lysår unna oss.

Bestem hvor stor vinkel $v$ Andromeda dekker på himmelen sett fra jorden.

Dekker månen eller Andromedagalaksen størst vinkel på himmelen?





::::{admonition} Fasit
---
class: answer, dropdown
---
$$
v = 4.58 \degree.
$$  
::::

:::::::::::::

::::::::::::::



:::::::::::::::


---






:::::::::::::::{exercise} Oppgave 12
---
level: 3
---
Nedenfor vises en rettvinklet trekant med vinkler $u$ og $v$. 

:::{figure} ./figurer/oppgaver/oppgave_12/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


Avgjør om påstandene nedenfor stemmer eller ikke.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
For en rettvinklet trekant, gjelder alltid 

$$
\sin v = \cos u
$$ 

::::{admonition} Fasit
---
class: answer, dropdown
---
Påstanden stemmer.
::::


:::::::::::::

:::::::::::::{tab-item} b
For en rettvinklet trekant, gjelder alltid 

$$
\tan u \cdot \tan v = 1
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
Påstanden stemmer.
::::

:::::::::::::


:::::::::::::{tab-item} c
For en rettvinklet trekant, gjelder alltid 

$$
(\cos v)^2 + (\sin v)^2 = 1
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
Påstanden stemmer.
::::


:::::::::::::


::::::::::::::


:::::::::::::::



























