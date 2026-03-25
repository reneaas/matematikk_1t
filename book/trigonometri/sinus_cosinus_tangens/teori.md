# Sinus, cosinus og tangens

:::::{admonition} Læringsmål 
---
class: tip
---
* Kunne bestemme $\sin v$, $\cos v$ og $\tan v$ for en vinkel $v$ i en rettvinklet trekant.
* Kjenne til sammenhengen mellom $\tan v$, og $\sin v$ og $\cos v$.
:::::

**Trigonometri** er en del av geometrien som handler om trekanter. Her skal vi se på tre trigonometriske størrelser som er sentrale i trigonometri: **sinus**, **cosinus** og **tangens**. Disse størrelsene er forholdstall som er avhengig av en bestemt vinkel $v$ i en rettvinklet trekant.

## Motstående og hosliggende kateter

Når vi jobber med rettvinklede trekanter, kommer vi til å få bruk for å kategorisere sidene i trekanten. 

:::::::::::::::{admonition} Motstående og hosliggende kateter
---
class: summary
---

I en rettvinklet trekant, vil katetene i trekanten ha to navn:
* Den **motstående** kateten er kateten som står på motsatt side av vinkelen.
* Den **hosliggende** kateten er kateten som spenner ut vinkelen.

Om en katet er motstående eller hosliggende er altså avhengig av hvilken vinkel vi ser på.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
axis: off
axis: equal
width: 100%
let: s = 6
let: Ax = 0
let: Ay = 0
let: v = 30 * pi / 180
let: Bx = s * cos(v)
let: By = 0
let: Cx = s * cos(v)
let: Cy = s * sin(v)
triangle: points=((Ax, Ay), (Bx, By), (Cx, Cy)), angles=(A, B), angle-radius=30
nocache:
fontsize: 26
text: 0.5 * (Ax + Bx), 0, "Hosliggende katet", bottom-center
text: Bx, 0.5 * (By + Cy), "Motstående\\ \,katet", center-right
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "Hypotenus", top-left
:::


:::{plot}
axis: off
axis: equal
width: 100%
let: s = 6
let: Ax = 0
let: Ay = 0
let: v = 30 * pi / 180
let: Bx = s * cos(v)
let: By = 0
let: Cx = s * cos(v)
let: Cy = s * sin(v)
triangle: points=((Ax, Ay), (Bx, By), (Cx, Cy)), angles=(B, C), angle-radius=30
nocache:
fontsize: 30
fontsize: 26
text: 0.5 * (Ax + Bx), 0, "Motstående katet", bottom-center
text: Bx, 0.5 * (By + Cy), "Hosliggende\\ \,katet", center-right
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "Hypotenus", top-left
:::

::::

:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 1
:::{plot}
width: 100%
align: right
triangle: sss=(3, 4, 5), angles=(A, B, C), angle-radius=30, side-labels=(AB=exact, BC=exact, CA=exact)
axis: off
axis: equal
fontsize: 30
:::


En trekant $\triangle ABC$ er vist til høyre.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

* Hvilken sidelengde er motstående katet til vinkel $A$?
* Hvilken sidelengde er hosliggende katet til vinkel $A$?

::::{answer}
* $BC$ er motstående katet til vinkel $A$.
* $AB$ er hosliggende katet til vinkel $A$. 
::::
:::::::::::::

:::::::::::::{tab-item} b
* Hvilken sidelengde er motstående katet til vinkel $A$?
* Hvilken sidelengde er hosliggende katet til vinkel $A$?

::::{answer}
* $AB$ er motstående katet til vinkel $C$.
* $BC$ er hosliggende katet til vinkel $C$.
::::

:::::::::::::

::::::::::::::


:::::::::::::::


## $\sin v$ og $\cos v$

Vi skal nå se på de to mest grunnleggende trigonometriske størrelsene. Den ene er **sinus** til en vinkel $v$ og skrives som $\sin v$. Den andre er **cosinus** til en vinkel $v$ og skrives som $\cos v$. 


:::::::::::::::{summary} Definisjon: Sinus og Cosinus
:::{plot}
axis: off
axis: equal
align: right
width: 380px
let: s = 6
let: Ax = 0
let: Ay = 0
let: v = 30 * pi / 180
let: Bx = s * cos(v)
let: By = 0
let: Cx = s * cos(v)
let: Cy = s * sin(v)
triangle: points=((Ax, Ay), (Bx, By), (Cx, Cy)), angles=(A, B), angle-radius=45, angle-text=(A="$v$")
nocache:
fontsize: 26
let: ds = 0.3
text: 0.5 * (Ax + Bx), -ds, "Hosliggende katet", bottom-center
text: Bx + ds, 0.5 * (By + Cy), "Motstående\\ \,katet", center-right
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "Hypotenus", top-left
:::

Sinus og cosinus til en vinkel $v$ i en rettvinklet trekant er definert som **forholdstallene**:

$$
\sin v = \frac{\text{motstående katet}}{\text{hypotenus}}
$$

$$
\cos v = \frac{\text{hosliggende katet}}{\text{hypotenus}}
$$


:::{clear}
:::

> Vi skriver ofte $\sin A$ og $\cos A$ når vi snakker om vinkelen i et hjørne $A$ i en trekant, og tilsvarende for vinklene $B$ og $C$.

:::::::::::::::


---


:::::::::::::::{example} Eksempel 1

:::{plot}
width: 100%
align: right
triangle: sss=(3, 4, 5), angles=(A, B, C), angle-radius=30, side-labels=(AB=exact, BC=exact, CA=exact)
axis: off
axis: equal
fontsize: 30
:::

En trekant $\triangle ABC$ er vist til høyre.


1. Bestem $\sin A$ og $\cos A$.
2. Bestem $\sin C$ og $\cos C$.


:::{clear}
:::


::::{solution}
---
dropdown: 0
---
For vinkel $A$, vil $AB = 3$ være hosliggende katet og $BC = 4$ være motstående katet, og $AC = 5$ er hypotenusen. Det betyr at 

$$
\sin A = \dfrac{BC}{AB} = \dfrac{4}{5} \qog \cos A = \dfrac{AB}{AC} = \dfrac{3}{5}
$$


For vinkel $C$ vil $BC = 4$ være hosliggende katet og $AB = 3$ være motstående katet, og $AC = 5$ er hypotenusen. Det betyr at

$$
\sin C = \dfrac{AB}{AC} = \dfrac{3}{5} \qog \cos C = \dfrac{BC}{AC} = \dfrac{4}{5}
$$

::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
:::{plot}
width: 100%
align: right
triangle: sss=(sqrt(3), 1, 2), angles=(A, B, C), angle-radius=50, angle-labels=(A=numeric, C=numeric), side-labels=(AB=exact, BC=exact, CA=exact)
axis: off
axis: equal
fontsize: 30
:::


En trekant $\triangle ABC$ er vist til høyre.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\sin A$.


::::{answer}
$$
\sin A = \dfrac{1}{2}.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\cos A$.


::::{answer}
$$
\cos A = \dfrac{\sqrt{3}}{2}.
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
Bestem $\sin C$.

::::{answer}
$$
\sin C = \dfrac{\sqrt{3}}{2}.
$$
::::
:::::::::::::


:::::::::::::{tab-item} d
Bestem $\cos C$.

::::{answer}
$$
\cos C = \dfrac{1}{2}.
$$
::::
:::::::::::::


::::::::::::::


:::::::::::::::




---



## $\tan v$
En annen trigonometrisk størrelse som er spesielt nyttig å måle avstander er **tangens** til en vinkel $v$ som vi skriver som $\tan v$. Eksempel på anvendelser er:
* Måle høyden til bygninger eller trær
* Måle avstanden til stjerner eller galakser
* Måle høyden til fjell


:::::::::::::::{summary} Definisjon: Tangens
:::{plot}
axis: off
axis: equal
align: right
width: 380px
let: s = 6
let: Ax = 0
let: Ay = 0
let: v = 30 * pi / 180
let: Bx = s * cos(v)
let: By = 0
let: Cx = s * cos(v)
let: Cy = s * sin(v)
triangle: points=((Ax, Ay), (Bx, By), (Cx, Cy)), angles=(A, B), angle-radius=45, angle-text=(A="$v$")
fontsize: 26
let: ds = 0.3
text: 0.5 * (Ax + Bx), -ds, "Hosliggende katet", bottom-center
text: Bx + ds, 0.5 * (By + Cy), "Motstående\\ \,katet", center-right
text: 0.5 * (Ax + Cx), 0.5 * (Ay + Cy), "Hypotenus", top-left
:::

Tangens til en vinkel $v$ i en rettvinklet trekant er definert som **forholdstallet**:

$$
\tan v = \frac{\text{motstående katet}}{\text{hosliggende katet}}
$$

Denne definisjonen er ekvivalent med at 

$$
\tan v = \frac{\sin v}{\cos v}
$$

:::::::::::::::


---


:::::::::::::::{example} Eksempel 2

:::{plot}
width: 100%
align: right
triangle: sss=(sqrt(3), 1, 2), angles=(A, B, C), angle-radius=50, angle-labels=(A=numeric, C=numeric), side-labels=(AB=exact, BC=exact, CA=exact)
axis: off
axis: equal
fontsize: 30
:::

En trekant $\triangle ABC$ er vist til høyre.

Bestem $\tan 30 \degree$.


:::{clear}
:::

::::{solution}
---
dropdown: 0
---
Vi kan bruke definisjonen av tangens til å finne at

$$
\tan 30 \degree = \dfrac{BC}{AB} = \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}.
$$

::::



:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
:::{plot}
width: 100%
align: right
triangle: sss=(sqrt(3), 1, 2), angles=(A, B, C), angle-radius=50, angle-labels=(A=numeric, C=numeric), side-labels=(AB=exact, BC=exact, CA=exact)
axis: off
axis: equal
fontsize: 30
:::

En trekant $\triangle ABC$ er vist til høyre.

Bestem $\tan 60 \degree$.


:::{clear}
:::


::::{answer}
$$
\tan 60 \degree = \dfrac{AB}{BC} = \dfrac{\sqrt{3}}{1} = \sqrt{3}.
$$
::::

:::::::::::::::



---


## Kjente vinkler for $\sin v$ og $\cos v$
For en bestemt vinkel $v$, vil $\sin v$, $\cos v$ og $\tan v$ ha samme verdi uansett hvor stor eller liten en trekant er. Verdiene er bare avhengig av forholdstallet mellom katetene, og hypotenusen. Derfor er det naturlig å tenke på de tre trigonometriske størrelsene som funksjoner av vinkelen $v$. 

Vi skal her se på noen eksakte verdier for $\sin v$ og $\cos v$ for noen utvalgte vinkler som vil bli nyttig i mange problemstillinger. 



:::::::::::::::{example} Eksempel 3
:::{plot}
width: 100%
align: right
triangle: sss=(sqrt(3), 1, 2), angles=(A, B, C), angle-radius=50, angle-labels=(A=numeric, C=numeric), side-labels=(AB=exact, BC=exact, CA=exact)
axis: off
axis: equal
fontsize: 30
nocache:
:::

En trekant $\triangle ABC$ er vist til høyre.


Bestem eksakte verdier for $\sin 30 \degree$ og $\cos 30 \degree$.



:::{clear}
:::


::::{answer}
$$
\sin 30 \degree = \dfrac{1}{2} \qog \cos 30 \degree = \dfrac{\sqrt{3}}{2}.
$$
::::



:::::::::::::::




