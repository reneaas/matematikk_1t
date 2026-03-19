# Trekantgeometri


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke egenskapene til likesidete, likebeinte og rettvinklete trekanter til å bestemme ukjente sider og vinkler. 
* Kunne bruke Pytagoras' setning til å finne ukjente sider i en rettvinklet trekant.
* Kunne bruke formlikhet til å beregne ukjente sidelengder i trekanter.
* Kunne undersøke om to trekanter er formlike.
:::

En trekant er en geometrisk figur som består av tre hjørner og tre sidekanter. Her skal vi repetere noen viktige egenskaper ved trekanter som vi kommer til å få bruk for når vi skal jobbe med trigonometri. Trigonometri er en del av matematikken som gir en ny måte å bruke sammenhenger mellom vinkler og sider i trekanter på. 


## Vinkler
En **vinkel** er et mål på hvor mange grader en sirkelbue spenner ut mellom to rette linjer. Vi deler inn vinkler i tre typer:


### Typer vinkler

:::::::::::::::{summary} Vinkler: Typer
En vinkel $v$ deles inn i tre typer:

::::{multi-plot2}
---
rows: 1
cols: 3
---
:::{plot}
figsize: (4, 4)
let: v = 60
let: v_rad = pi/3
let: r = 0.2
line-segment: (0, 0), (1, 0), blue
line-segment: (0, 0), (cos(v_rad), sin(v_rad)), blue
angle-arc: (0, 0), 0.2, 0, v
text: 1.25 * r * cos(v_rad/2), 1.25 * r * sin(v_rad/2), "$v$", center-center
text: 0.2, 0.8, "Spiss", bbox
ticks: off
axis: off
axis: equal
fontsize: 28
:::


:::{plot}
figsize: (4, 4)
let: v = 90
let: v_rad = pi/2
let: r = 0.2
line-segment: (0, 0), (1, 0), blue
line-segment: (0, 0), (0, 1), blue
let: ds = 0.15
line-segment: (ds, 0), (ds, ds), solid, black
line-segment: (ds, ds), (0, ds), solid, black
text: 1.4 * r * cos(v_rad/2), 1.4 * r * sin(v_rad/2), "$v$", center-center
text: 0.5, 0.8, "Rett", center-center, bbox
ticks: off
axis: off
axis: equal
fontsize: 28
:::


:::{plot}
figsize: (4, 4)
let: v = 2 * pi / 3 * 180 / pi
let: v_rad = 2 * pi / 3
let: r = 0.2
line-segment: (0, 0), (1, 0), blue
line-segment: (0, 0), (cos(v_rad), sin(v_rad)), blue
angle-arc: (0, 0), 0.2, 0, v
text: 1.35 * r * cos(v_rad/2), 1.35 * r * sin(v_rad/2), "$v$", center-center
text: 0.5, 0.8, "Stump", center-center, bbox
ticks: off
axis: off
axis: equal
fontsize: 28
:::
::::


:::{table}
width: 80%
labels: Type vinkel, $v$
Spiss vinkel, $\langle 0^\circ, 90^\circ \rangle$
Rett vinkel, $90^\circ$
Stump vinkel, $\langle 90^\circ, 180^\circ \rangle$
:::

:::::::::::::::


### Toppvinkler og samsvarende vinkler

Når vi jobber med geometriske figurer, så kan vi i blant si noe om ukjente vinkler ved å bruke at noe vinkler er like store ved å fokusere på hvor linjer skjærer hverandre. 


:::::::::::::::{summary} Toppvinkler og samsvarende vinkler
Toppvinkler
: Like vinkler på hver sin side av en linje som skjærer en annen linje

Samsvarende vinkler
: Like vinkler som ligger på samme side av en linje som skjærer to andre linjer.



:::{plot}
width: 70%
figsize: (4, 4)
line-segment: (0, 0), (1, 0), black, solid
line-segment: (0, 1), (1, 1), black, solid
line-segment: (0, 0.5), (1, 1), black, solid
axis: off
ymin: -3
ymax: 3
angle-arc: (1, 1), 1.5, 0, atan(0.5) * 180 / pi
:::



:::::::::::::::







## Likesidete trekanter


## Likebeinte trekanter


## Rettvinklete trekanter


## Formlikhet
