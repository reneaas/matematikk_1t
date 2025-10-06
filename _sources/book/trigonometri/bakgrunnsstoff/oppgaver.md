# Oppgaver: Pytagoras' setning, formlikhet og vinkler




:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{plot}
width: 100%
lw: 1
line-segment: (0, 0), (1, 0), solid, black
line-segment: (0, 0), (0, sqrt(3)), solid, black
line-segment: (1, 0), (0, sqrt(3)), solid, black
angle-arc: (1, 0), 0.3, 180, 120
axis: off
axis: equal
figsize: (3, 3)
align: right
text: 0, 0, "$A$", bottom-left
text: 1, 0, "$B$", bottom-right
text: 0, sqrt(3), "$C$", top-center
text: 1 - 0.3*cos(pi/6), 0.3*sin(pi/6), "$60^\circ$", top-left
polygon: (0, 0), (0.2, 0), (0.2, 0.2), (0, 0.2), solid, black
:::

En trekant $\triangle ABC$ er vist i figuren til høyre. 

Bestem $\angle C$.

:::{clear}
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\angle C = 30 \degree.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

:::{plot}
width: 100%
axis: off
axis: equal
align: right
figsize: (3, 3)
lw: 1
line-segment: (0, 0), (1, 0), solid, black
line-segment: (0, 0), (0, 1), solid, black
line-segment: (1, 0), (0, 1), solid, black
angle-arc: (0, 1), 0.2, 270, 315
text: 0, 0, "$A$", bottom-left
text: 1, 0, "$B$", bottom-right
text: 0, 1, "$C$", top-left
text: 0.3*cos(pi/4), 1 - 0.3*sin(pi/4), "$45^\circ$", bottom-left
polygon: (0, 0), (0.15, 0), (0.15, 0.15), (0, 0.15), solid, black
:::


Figuren til høyre vises en trekant $\triangle ABC$. 

Bestem $\angle B$. 


:::{clear}
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\angle B = 45 \degree.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

:::{plot}
width: 400
align: right
lw: 1
axis: off
axis: equal
figsize: (5, 3)
line-segment: (0, 0), (4, 0), solid, black
line-segment: (4, 0), (4 - 4 * cos(pi/9)/cos(2*pi/9) * cos(20*pi/180), 4 * cos(pi/9)/cos(2*pi/9) * sin(20*pi/180)), solid, black
line-segment: (0, 0), (4 - 4 * cos(pi/9)/cos(2*pi/9) * cos(20*pi/180), 4 * cos(pi/9)/cos(2*pi/9) * sin(20*pi/180)), solid, black
angle-arc: (4, 0), 0.8, 180, 160
angle-arc: (0, 0), 0.3, 0, 110
text: 0, 0, "$A$", bottom-left
text: 4, 0, "$B$", bottom-right
text: 4 - 4 * cos(pi/9)/cos(2*pi/9) * cos(20*pi/180), 4 * cos(pi/9)/cos(2*pi/9) * sin(20*pi/180), "$C$", top-left
text: 4 - 1, 0.15, "$20^\circ$", center-center
text: 0.2, 0.2, "$110^\circ$", top-right
:::

En trekant $\triangle ABC$ er vist i figuren til høyre. 

Bestem $\angle C$.

:::{clear}
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\angle C = 50 \degree.
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


Nedenfor vises en rettvinklet trekant.

Bestem $x$. 


:::{figure} ./figurer/oppgaver/oppgave_2/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
viser en rettvinklet trekant.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \sqrt{3}. 
$$
::::


:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 3
---
level: 1
---

Nedenfor vises en rettvinklet trekant.

Bestem $x$. 


:::{figure} ./figurer/oppgaver/oppgave_3/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 5 \sqrt{3}.
$$
::::

:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 4
---
level: 1
---
Nedenfor vises en trekant. 

Bestem høyden $h$ i trekanten. 


:::{figure} ./figurer/oppgaver/oppgave_4/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
viser en trekant.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
h = 2\sqrt{3}.
$$
::::


:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 5
---
level: 1
---
Nedenfor vises en rettvinklet trekant.

Bestem $x$.

:::{figure} ./figurer/oppgaver/oppgave_5/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 6.
$$
::::


:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
Nedenfor vises to rettvinklete trekanter.


:::{figure} ./figurer/oppgaver/oppgave_6/merged_figure.svg
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
Forklar at $\triangle ABC \sim \triangle DEF$.

::::{admonition} Fasit
---
class: answer, dropdown
---
Vi kjenner til alle sidelengdene i $\triangle ABC$ og $\triangle DEF$, så vi kan sjekke SSS-kriteriet:

$$
\dfrac{DE}{AB} = \dfrac{8}{4} = 2 \and \dfrac{DF}{AC} = \dfrac{6}{3} = 2 \and \dfrac{EF}{BC} = \dfrac{10}{5} = 2.
$$

Siden alle forholdstallene er like, må $\triangle ABC \sim \triangle DEF$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\angle F$ og $\angle E$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\angle F = \angle C = 53.13 \degree \and \angle E = \angle B = 36.87 \degree.
$$
::::

:::::::::::::


::::::::::::::



:::::::::::::::




---

:::::::::::::::{exercise} Oppgave 7
---
level: 2
---
Nedenfor vises to rettvinklete trekanter.

:::{figure} ./figurer/oppgaver/oppgave_7/merged_figure.svg
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
Forklar at $\triangle ABC \sim \triangle EDF$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
I $\triangle ABC$ har vi at 


$$
\angle C = 90 \degree - \angle B = 90 \degree - 30 \degree = 60 \degree.
$$

For $\triangle EDF$ har vi samtidig at:

$$
\angle D = 90 \degree - \angle F = 90 \degree - 60 \degree = 30 \degree.
$$

Dermed er

$$
\angle B = \angle D \and \angle C = \angle F \and \angle A = \angle E,
$$

som etter VVV-kriteriet betyr at $\triangle ABC \sim \triangle EDF$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $x$, $y$ og $z$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 6 \and y = \sqrt{3} \and z = 2 \sqrt{3}.
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
Nedenfor vises to trekanter.

:::{figure} ./figurer/oppgaver/oppgave_8/merged_figure.svg
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
Forklar at $\triangle ABC \sim \triangle EDF$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
Vi kan bestemme alle vinklene i de to trekantene som gjør det hensiktsmessig å sjekke VVV-kriteriet.

For $\triangle ABC$ har vi at

$$
\angle A = 120 \degree \and \angle C = 30 \degree \and \angle B = 180 \degree - \angle A - \angle C = 30 \degree.
$$

og for $\triangle EDF$ har vi at

$$
\angle D = 30 \degree \and \angle F = 30 \degree \and \angle E = 180 \degree - \angle D - \angle F = 120 \degree.
$$

Ut ifra VVV-kriteriet er derfor $\triangle ABC \sim \triangle EDF$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $AC$.

::::{admonition} Fasit
---
class: answer, dropdown
---
Trekant $\triangle ABC$ er likebeint så $AB = AC = 3$. 
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $DE$ og $EF$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
DE = EF = 6.
$$
::::

:::::::::::::

::::::::::::::



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 9
---
level: 2
---
Nedenfor vises to trekanter $\triangle ABC$ og $\triangle ADE$ der 

$$
BC = 2\sqrt{3} \quad\quad\quad AB = 4 \quad\quad\quad AE = 1. 
$$

:::{figure} ./figurer/oppgaver/oppgave_9/figur.svg
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
Forklar at $\triangle ABC \sim \triangle ADE$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$\angle A$ er en felles vinkel i $\triangle ABC$ og $\triangle ADE$. Vi har også at $\angle E = \angle C = 90 \degree$. Siden to av vinklene er like, blir den siste også lik i hver av trekantene som betyr at trekantene oppfyller VVV-kriteriet og derfor er 

$$
\triangle ABC \sim \triangle ADE.
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem $DE$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
DE = \sqrt{3}. 
$$
::::

:::::::::::::

::::::::::::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
---
level: 3
---
Figuren nedenfor viser en trekant.

Bestem $x$, $y$ og $z$.

:::{figure} ./figurer/oppgaver/oppgave_10/figur.svg
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
x = 5 \and y = 5 \sqrt{3} \and z = \dfrac{5\sqrt{3}}{2}
$$
::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 11
---
level: 3
---
Bestem $CM$ i figuren nedenfor.


:::{figure} ./figurer/oppgaver/oppgave_11/figur.svg
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
CM = 2\sqrt{3}
$$
::::


:::::::::::::::











