# Ettpunktsform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en lineær funksjon på ettpunktsform og beskrive sammenhengen med den grafiske representasjonen.
* Kunne bytte fra en representasjon til en annen.
:::

Hittil har vi sett på to måter å representere en lineær funksjon på, nemlig {popup}`standardform<$f(x) = ax + b$>` og {popup}`nullpunktsform<$f(x) = a(x - x_0)$>`. Standardform fortalte oss stigningen til grafen og hvor grafen skjærer gjennom $y$-aksen, mens nullpunktsform fortalte oss stigningen og hvor grafen skjærer gjennom $x$-aksen. 

Her skal vi se på en tredje måte å representere en lineær funksjon som vi skal kalle for **ettpunktsform**. Denne måten å uttrykke en lineær funksjon forteller oss stigningen til grafen og ett punkt som grafen går gjennom. Vi kan se på denne måten å uttrykke funksjonen på som at vi *bygger opp* linja ved å starte fra ett punkt og så forteller stigningstallet oss hvilken retning vi skal tegne grafen i.


:::::::::::::::{theory} Ettpunktsform
En lineær funksjon $f$ kan skrives på ettpunktsform som følger: 

:::{figure} ./figurer/teori/algebraisk_representasjon/ettpunktsform.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::


:::{plot}
width: 60%
function: -x + 5, f
hline: 4, 1, 2
vline: 2, 4, 3
xmin: -1
xmax: 6
ymin: -1
ymax: 7
text: 1.5, 4, $1$, top-center
text: 2, 3.5, $a$, center-right
point: (3, 2)
text: 3, 2, "$(x_0, y_0)$", top-right
ticks: off
:::



:::::::::::::::


---


:::::::::::::::{explore} Utforsk 1
Nedenfor vises grafen til en lineær funksjon $f$ i et interaktivt vindu der $f(x)$ er skrevet på ettpunktsform 

$$
f(x) = a\cdot (x - x_0) + y_0
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $x_0$. 

Gi en beskrivelse av hva som skjer med grafen.

:::::::::::::


:::::::::::::{tab-item} b
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $y_0$. 

Gi en beskrivelse av hva som skjer med grafen.

:::::::::::::


:::::::::::::{tab-item} c
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $a$.

Er det noen forskjell fra standardform og nullpunktsform? Kan du fortsatt lese av verdien til $a$ på samme måte som før?

:::::::::::::

::::::::::::::


:::{ggb} 720 600
---
material_id: u8hkthry
---
:::


:::::::::::::::





---




:::::::::::::::{underveisoppgave} Underveisoppgave 1
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2\cdot (x - 1) + 3
$$

Hvilken av grafene nedenfor viser grafen til $f$?



:::{multi-plot}
width: 100%
functions: -2*x + 5, 2*x + 1, 2*x + 5, x + 2
function-names: A, B, C, D
rows: 2
cols: 2
:::



::::{answer}
Graf B
::::

::::{solution}
Fra ettpunktsformen til $f(x)$ kan vi lese av at grafen må gå gjennom punktet $(1, 3)$. Dette passer med graf A, B og C. Stigningstallet til $f$ er $a = 2$ som eliminerer graf A siden den har negativ stigning. Sjekker vi stigningstallet til graf B er stigningstallet $a = 2$, mens stigningstallet til graf C er $a = 1$. 

Dermed er graf B grafen til $f$.
::::


:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 2
:::{plot}
width: 380
function: -3*(x - 1) - 2, f
align: right
fontsize: 26
lw: 3.5
:::

Til høyre vises grafen til en lineær funksjon $f$.


Hvilken av uttrykkene nedenfor viser $f(x)$?


:::{clear}
:::

:::::{grid} 1 2 2 2
::::{grid-item-card} A
$$
f(x) = -3 \cdot (x - 1) - 2
$$
::::

::::{grid-item-card} B
$$
f(x) = 3 \cdot (x - 1) - 2
$$
::::

::::{grid-item-card} C
$$
f(x) = -3 \cdot (x + 1) - 2
$$
::::

::::{grid-item-card} D
$$
f(x) = -3 \cdot (x - 1) + 2
$$
::::


:::::


::::{answer}
A
::::

::::{solution}
Vi ser fra grafen til $f$ at når vi øker $x$ med $1$, så synker $f(x)$ med $-3$. Dermed er stigningstallet $a = -3$. Vi kan også se at grafen går gjennom punktet $(1, -2)$ som betyr at 

$$
f(x) = a(x - x_0) + y_0 = -3 \cdot (x - 1) - 2
$$

som passer med svaralternativ A.
::::


:::::::::::::::



