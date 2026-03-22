# Arealsetningen

:::::::::::::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke arealsetningen til arealberegninger for trekanter. 
* Kunne begrunne arealsetningen.
:::::::::::::::



## Repetisjon: Arealet av en trekant

Fra geometri har du tidligere lært en måte å regne ut arealet av en trekant. Arealet $T$ av en trekant med grunnlinje $g$ og høyde $h$ er 

$$
T = \dfrac{1}{2} \cdot g \cdot h.
$$

Høyden $h$ vil være den korteste avstanden fra linja som går gjennom linjestykke til grunnlinja $g$ og hjørnet som ikke ligger på grunnlinja.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
width: 100%
axis: off
axis: equal
triangle: svs=(4, 30, 2), color=blue, angle-color=red, angles=none
nocache:
let: Ax = 0
let: Ay = 0
let: Bx = 4
let: By = 0
let: Cx = 2 * cos(pi/6)
let: Cy = 2 * sin(pi/6)
vline: Cx, 0, Cy, dashed, gray
text: Cx, 0.5*Cy, "$h$", center-right
let: ds = 0.2
line-segment: (Cx - ds, 0), (Cx - ds, ds), solid, gray
line-segment: (Cx - ds, ds), (Cx, ds), solid, gray
text: 0.5 * (Ax + Bx), 0, "$g$", bottom-center
:::

:::{plot}
width: 100%
axis: off
axis: equal
triangle: svs=(3, 120, 2), color=blue, angle-color=red, angles=none
nocache:
let: Ax = 0
let: Ay = 0
let: Bx = 3
let: By = 0
let: Cx = 2 * cos(2 * pi / 3)
let: Cy = 2 * sin(2 * pi / 3)
vline: Cx, 0, Cy, dashed, gray
hline: 0, Ax, Cx, dashed, gray
text: Cx, 0.5*Cy, "$h$", center-right
let: ds = 0.2
line-segment: (Cx + ds, 0), (Cx + ds, ds), solid, gray
line-segment: (Cx + ds, ds), (Cx, ds), solid, gray
text: 0.5 * (Ax + Bx), 0, "$g$", bottom-center
:::
::::



---



:::::::::::::::{admonition} Underveisoppgave 1
---
class: check 
---
En trekant $\triangle ABC$ er vist i figuren nedenfor. $AB = 4$. 

Bestem arealet av trekanten.


:::{figure} ./figurer/underveisoppgaver/oppgave_1/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T = 2. 
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Fra figuren, kan vi se at grunnlinja er $g = AB = 4$ og høyden er $h = 1$. Dermed blir arealet av trekanten 

$$
T = \dfrac{g \cdot h}{2} = \dfrac{4 \cdot 1}{2} = 2. 
$$
::::



:::::::::::::::


## Arealsetningen

Arealsetningen lar oss regne ut arealet så lenge vi kjenner til to sidelenger og vinkelen som disse sidene spenner ut. 

:::::::::::::::{summary} Arealsetningen

:::{plot}
width: 100%
ticks: off
axis: off
axis: equal 
align: right
triangle: svs=(3, 30, 6), angles=(A), color=blue, angle-color=red, angle-radius=40, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3
fontsize: 30
:::


Gitt en trekant $\triangle ABC$, så er arealet $T$ av trekanten gitt ved


$$
T = \dfrac{1}{2} \cdot AB \cdot AC \cdot \sin A
$$



:::{clear}
:::

::::::::::::::{admonition} Forklaring av formelen
---
class: theory, dropdown
--- 
:::{plot}
width: 100%
ticks: off
axis: off
axis: equal 
align: right
let: Ax = 0
let: Ay = 0
let: Bx = 3
let: By = 0
let: Cx = 6 * cos(pi/6)
let: Cy = 6 * sin(pi/6)
triangle: svs=(3, 30, 6), angles=(A), color=blue, angle-color=red, angle-radius=40, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3
vline: Cx, 0, Cy, dashed, gray
hline: 0, Bx, Cx, dashed, gray
text: Cx, 0.5*Cy, "$h$", center-right
text: Cx, 0, "$D$", bottom-right
let: ds = 0.3
line-segment: (Cx - ds, 0), (Cx - ds, ds), solid, gray
line-segment: (Cx - ds, ds), (Cx, ds), solid, gray 
fontsize: 30
:::

Vi lager oss en hjelpefigur som vist til høyre for en trekant $\triangle ABC$. Med de stiplede linjene får vi rettvinklet trekant $\triangle ADC$

Grunnlinja i trekanten er $AB$, og høyden er $h$. Arealet av trekanten er derfor 

$$
T = \dfrac{1}{2} \cdot AB \cdot h.
$$

Fra definisjonen av $\sin A$, har vi at 

$$
\sin A = \dfrac{h}{AC} \liff h = AC \cdot \sin A.
$$

Setter vi dette inn i formelen for arealet, får vi

$$
T = \dfrac{1}{2} \cdot AB \cdot AC \cdot \sin A.
$$


::::::::::::::



:::::::::::::::


---


:::::::::::::::{example} Eksempel 2

:::{plot}
figsize: (6, 6)
width: 100%
align: right
axis: off
axis: equal
triangle: svs=(3, 30, 4), angles=A, color=blue, angle-color=red, angle-radius=30, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric)
fontsize: 30
nocache:
:::


Figuren til høyre viser en trekant $\triangle ABC$. 

Bestem arealet av trekanten.


:::{clear}
:::


::::{solution}
---
dropdown: 0
---
Arealet til trekanten er gitt ved 

$$
T = \dfrac{1}{2} \cdot AB \cdot AC \cdot \sin A.
$$

Vi har at $\sin A = \sin 30\degree = \dfrac{1}{2}$. Siden $AB = 3$ og $AC = 4$, så får vi at arealet av trekanten er

$$
T = \dfrac{1}{2} \cdot 3 \cdot 4 \cdot \dfrac{1}{2} = 3.
$$
::::
:::::::::::::::




---




:::::::::::::::{exercise} Underveisoppgave 2

:::{plot}
align: right
width: 100%
axis: off
axis: equal
triangle: svs=(5, 60, 2), angles=A, color=blue, angle-color=red, angle-radius=25, side-labels=(AB=exact, CA=exact), angle-labels=(A=numeric)
fontsize: 30
:::


En trekant $\triangle ABC$ er vist i figuren til høyre.

Bestem arealet av trekanten.


:::{clear}
:::


::::{answer}
$$
T = \dfrac{5\sqrt{3}}{4}.
$$
::::


::::{solution}
Arealet av trekanten er

$$
T = \dfrac{1}{2} \cdot AB \cdot AC \cdot \sin A.
$$

Vi har at $\sin A = \sin 60\degree = \dfrac{\sqrt{3}}{2}$. Siden $AB = 5$ og $AC = 2$, så får vi at arealet av trekanten er

$$
T = \dfrac{1}{2} \cdot 5 \cdot 2 \cdot \dfrac{\sqrt{3}}{2} = \dfrac{5\sqrt{3}}{4}.
$$
::::

:::::::::::::::



---


Hittil har vi fokusert på arealsetningen ut ifra hjørne $A$ i en trekant, men den fungerer like godt ut ifra hjørnene $B$ og $C$.


:::::::::::::::{summary} Arealsetningen: Generelt
:::{plot}
width: 100%
ticks: off
axis: off
axis: equal 
align: right
triangle: svs=(3, 45, 4), angles=all, color=blue, angle-color=red, angle-radius=20, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-text=(AB="$c$", CA="$b$", BC="$a$")
fontsize: 30
:::


Gitt en trekant $\triangle ABC$, så er arealet $T$ av trekanten gitt ved

$$
\begin{align*}
T &= \dfrac{1}{2} \cdot b \cdot c \cdot \sin A && (\mathrm{hjørne \, A})\\
\\
T &= \dfrac{1}{2} \cdot a \cdot c \cdot \sin B && (\mathrm{hjørne \, B})\\
\\
T &= \dfrac{1}{2} \cdot a \cdot b \cdot \sin C && (\mathrm{hjørne \, C})
\end{align*}
$$



Det er enklest å huske formelen for arealsetningen ved å tenke seg følgende oppskrift:
1. Velg et hjørne i trekanten.
2. Ta produktet av de to sidene som spenner ut vinkelen i hjørnet.
3. Gang med sinus til vinkelen i hjørnet.
4. Del med 2.

:::::::::::::::



---




:::::::::::::::{example} Eksempel 3
:::{plot}
width: 100%
align: right
triangle: points=((0, 0), (4, 0), (4 - 2 * cos(pi/3), 2 * sin(pi/3))), color=blue, angle-color=red, angles=(B), angle-radius=20, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-labels=(AB=exact, BC=exact), angle-labels=(B=numeric)
fontsize: 30
axis: off
axis: equal
:::


Figuren til høyre viser en trekant $\triangle ABC$.

Bestem arealet til trekanten.


:::{clear}
:::


::::{solution}
---
dropdown: 0
---
Vi tar produktet av de to sidene som spenner ut vinkelen i hjørnet $B$. Siden $AB = 4$ og $BC = 2$, så får vi at arealet av trekanten er

$$
T = \dfrac{1}{2} \cdot 4 \cdot 2 \cdot \sin 60\degree = \dfrac{1}{2} \cdot 4 \cdot 2 \cdot \dfrac{\sqrt{3}}{2} = 2\sqrt{3}
$$

der vi har brukt at $\sin 60\degree = \dfrac{\sqrt{3}}{2}$.

::::


:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 3

:::{plot}
width: 100%
align: right
triangle: points=((0, 0), (3, 0), (3 - 5 * cos(pi/6), 5 * sin(pi/6))), color=blue, angle-color=red, angles=(B), angle-radius=30, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-labels=(AB=exact, BC=exact), angle-labels=(B=numeric)
axis: equal
axis: off
fontsize: 30
:::



I figuren til høyre vises en trekant $\triangle ABC$.

Bestem arealet av trekanten.



:::{clear}
:::

::::{answer}
$$
T = \dfrac{15}{4}
$$
::::


::::{solution}
Arealet av trekanten er

$$
T = \dfrac{1}{2} \cdot 3 \cdot 5 \cdot \sin 30\degree = \dfrac{1}{2} \cdot 3 \cdot 5 \cdot \dfrac{1}{2} = \dfrac{15}{4}.
$$
::::

:::::::::::::::




