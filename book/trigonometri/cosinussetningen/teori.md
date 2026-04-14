# Cosinussetningen


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke cosinussetningen til å regne ut ukjente sider, eller ukjente cosinusverdier
* Kunne kombinere cosinussetningen, sinussetningen og arealsetningen til å bestemme omkrets og areal av sammensatte figurer.
:::

Cosinussetningen er en **generalisert** versjon av Pytagoras' setning som gjelder **også** når ingen av vinklene i en trekant er $90\degree$. 



:::::::::::::::{summary} Cosinussetningen
:::{plot}
axis: off
axis: equal
width: 100%
align: right
triangle: svs=(3, 120, 4), angles=(A, B, C), color=blue, angle-color=red, angle-radius=50, corner-labels=(A="$A$", B="$B$", C="$C$"), side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24
fontsize: 35
:::

For en trekant $\triangle ABC$ der 
* $a$ er den motstående siden til vinkel $A$
* $b$ er den motstående siden til vinkel $B$
* $c$ er den motstående siden til vinkel $C$

så gjelder


$$
\begin{align*}
a^2 &= b^2 + c^2 - 2\cdot b \cdot c \cdot \cos A \\
\\
b^2 &= a^2 + c^2 - 2\cdot a \cdot c \cdot \cos B \\
\\
c^2 &= a^2 + b^2 - 2\cdot a \cdot b \cdot \cos C 
\end{align*}
$$



:::{clear}
:::

::::{admonition} Forklaring av formelen
---
class: theory, dropdown
---
:::{plot}
axis: off
axis: equal
width: 100%
align: right
triangle: svs=(3, 120, 4), angles=(A), color=blue, angle-color=red, angle-radius=50, corner-labels=(A="$A$", B="$B$", C="$C$"), side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24, angle-text=(A="$v$")
let: Cx = 4 * cos(120 * pi / 180)
let: Cy = 4 * sin(120 * pi / 180)
let: Dx = Cx
let: Dy = 0
let: Ax = 0
let: Ay = 0
line-segment: (Ax, Ay), (Dx, Dy), dashed, gray
line-segment: (Cx, Cy), (Dx, Dy), dashed, gray
let: ds = 0.4
line-segment: (Dx + ds, Dy), (Dx + ds, Dy + ds), solid, gray
line-segment: (Dx, Dy + ds), (Dx + ds, Dy + ds), solid, gray
text: Dx, Dy, "$D$", bottom-left
angle-arc: (Ax, Ay), 0.7, 120, 180, red
text: Ax + 0.7 * cos(150 * pi / 180), Ay + 0.7 * sin(150 * pi / 180), "$u$", top-left
text: 0.5 * (Ax + Dx), 0.5 * (Ay + Dy) - 0.1, "$x$", bottom-center
text: 0.5 * (Cx + Dx) - 0.1, 0.5 * (Cy + Dy), "$y$", center-left
fontsize: 35
nocache:
:::




Vi tenker oss en trekant $\triangle ABC$ med sider $a$, $b$ og $c$ og en vinkel $v$. I tillegg tegner vi oss en rettvinklet trekant $\triangle ACD$ på utsiden av trekanten som har en vinkel $u$. Vi kan tenke oss at de to trekantene til sammen lager en større rettvinklet trekant $\triangle DBC$. 

Bruker vi Pytagoras' setning på $\triangle DBC$ får vi at

$$
(x + c)^2 + y^2 = a^2
$$

Bruker vi Pytagoras' setning på $\triangle DAC$ får vi 

$$
x^2 + y^2 = b^2 \liff y^2 = b^2 - x^2
$$

Setter vi inn uttrykket for $y^2$ i det første uttrykket får vi at

$$
(x + c)^2 + (b^2 - x^2) = a^2
$$

Vi ganger ut parentesen og forenkler:

$$
x^2 + 2cx + c^2 + b^2 - x^2 = a^2
$$

$$
b^2 + c^2 + 2cx = a^2
$$

Vi må ha et uttrykk for $x$ som er relatert til størrelsene til den faktiske trekanten. Vi kan merke oss at

$$
\cos u = \dfrac{x}{b} \liff x = b \cos u
$$

Da kan vi skrive om likningen til

$$
b^2 + c^2 + 2\cdot b \cdot c \cdot \cos u = a^2
$$

Men vinkelen $u$ er ikke en del av trekanten $\triangle ABC$. Vi vet likevel at $u = 180\degree - v$. Da kan vi bruke at

$$
\cos u = \cos (180 \degree - v) = -\cos v
$$

Det betyr at vi kan skrive likningen om til

$$
b^2 + c^2 - 2\cdot b \cdot c \cdot \cos v = a^2
$$

Dette er cosinussetningen ut ifra vinkel $v = A$. Samme resonnement må nødvendigvis gjelde for de andre vinklene også. 
::::


:::::::::::::::



---


:::::::::::::::{example} Eksempel 1
:::{plot}
axis: off
axis: equal
width: 100%
align: right
triangle: svs=(5, 60, 4), angles=(A), color=blue, angle-color=red, angle-radius=50, corner-labels=(A="$A$", B="$B$", C="$C$"), side-labels=(AB=exact, CA=exact), label-offset=24, angle-labels=(A=numeric), angle-offset=24
fontsize: 35
:::

Trekanten $\triangle ABC$ er vist i figuren til høyre.

Bestem $BC$.


:::{clear}
:::

::::{solution}
---
dropdown: 0 
---
Vi lar $x = BC$. Cosinussetningen gir oss da at

$$
BC^2 = AB^2 + AC^2 - 2\cdot AB \cdot AC \cdot \cos A
$$

Vi setter inn de konkrete verdiene vi har som gir

$$
x^2 = 5^2 + 4^2 - 2\cdot 5 \cdot 4 \cdot \cos 60\degree
$$

Vi vet at $\cos 60\degree = \dfrac{1}{2}$, så da får vi at

$$
x^2 = 25 + 16 - 2 \cdot 5 \cdot 4 \cdot \dfrac{1}{2} = 25 + 16 - 20 = 21
$$

Dermed blir

$$
x = \sqrt{21}
$$

Vi kan ikke forenkle kvadratroten noe mer enn dette, så da er $BC = \sqrt{21}$.

::::

:::::::::::::::


---



:::::::::::::::{example} Eksempel 2
Nedenfor vises en firkant $\square ABCD$. 

:::{plot}
fontsize: 25
axis: off
axis: equal
width: 50%
let: Ax = 0
let: Ay = 0
let: Bx = 8
let: By = 0
let: Dx = 4 * cos(60 * pi/ 180)
let: Dy = 4 * sin(60 * pi/ 180)
let: Cx = Bx + 12 * cos(60 * pi / 180)
let: Cy = By + 12 * sin(60 * pi / 180)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Ax, Ay), (Dx, Dy), solid, blue
line-segment: (Dx, Dy), (Cx, Cy), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
angle-arc: (Ax, Ay), 1.4, 0, 60, red
text: Ax + 1.3 * cos(30 * pi / 180), Ay + 1.1 * sin(30 * pi / 180), "$60^\circ$", top-right
angle-arc: (Cx, Cy), 1.6, 60 + 180 - 30, 60 + 180, red
text: Cx + 1.5 * cos((60 + 180 - 15) * pi / 180), Cy + 1.7 * sin((60 + 180 - 15) * pi / 180), "$30^\circ$", bottom-left
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
text: 0.5 * (Ax + Bx), 0.5 * (Ay + By) - 0.1, "$8$", bottom-center
text: 0.5 * (Bx + Cx), 0.5 * (By + Cy) + 0.1, "$12$", bottom-right
text: 0.5 * (Cx + Dx), 0.5 * (Cy + Dy) + 0.1, "$8\sqrt{3}$", top-left
:::

Bestem $AD$.


::::{solution}
---
dropdown: 0
---

Vi tegner en hjelpelinje for linjestykket $BD$.


:::{plot}
fontsize: 25
axis: off
axis: equal
width: 50%
let: Ax = 0
let: Ay = 0
let: Bx = 8
let: By = 0
let: Dx = 4 * cos(60 * pi/ 180)
let: Dy = 4 * sin(60 * pi/ 180)
let: Cx = Bx + 12 * cos(60 * pi / 180)
let: Cy = By + 12 * sin(60 * pi / 180)
line-segment: (Ax, Ay), (Bx, By), solid, blue
line-segment: (Ax, Ay), (Dx, Dy), solid, blue
line-segment: (Dx, Dy), (Cx, Cy), solid, blue
line-segment: (Bx, By), (Cx, Cy), solid, blue
angle-arc: (Ax, Ay), 1.4, 0, 60, red
text: Ax + 1.3 * cos(30 * pi / 180), Ay + 1.1 * sin(30 * pi / 180), "$60^\circ$", top-right
angle-arc: (Cx, Cy), 1.6, 60 + 180 - 30, 60 + 180, red
text: Cx + 1.5 * cos((60 + 180 - 15) * pi / 180), Cy + 1.8 * sin((60 + 180 - 15) * pi / 180), "$30^\circ$", bottom-left
text: Ax, Ay, "$A$", bottom-left
text: Bx, By, "$B$", bottom-right
text: Cx, Cy, "$C$", top-right
text: Dx, Dy, "$D$", top-left
text: 0.5 * (Ax + Bx), 0.5 * (Ay + By) - 0.1, "$8$", bottom-center
text: 0.5 * (Bx + Cx), 0.5 * (By + Cy) + 0.1, "$12$", bottom-right
text: 0.5 * (Cx + Dx), 0.5 * (Cy + Dy) + 0.1, "$8\sqrt{3}$", top-left
line-segment: (Bx, By), (Dx, Dy), dashed, gray
:::

For å bestemme $AD$ kan vi følge disse stegene:
1. Bestemme $BD$ med cosinussetningen
2. Bestemme $AD$ med cosinussetningen

Vi lar $x = BD$. Fra cosinussetningen har vi da at

$$
BD^2 = BC^2 + CD^2 - 2 \cdot BC \cdot CD \cdot \cos C
$$

vi setter inn de konkrette konkrete verdiene vi har som gir:

$$
x^2 = \left(8 \sqrt{3}\right)^2 + 12^2 - 2 \cdot 8 \sqrt{3} \cdot 12 \cdot \cos 30\degree
$$

Vi vet også at 

$$
\cos 30\degree = \dfrac{\sqrt{3}}{2}
$$

Vi setter inn og forenkler likningen så mye som mulig:

$$
x^2 = 8^2 \cdot 3 + 144 - 16 \sqrt{3} \cdot 12 \cdot \dfrac{\sqrt{3}}{2}
$$

$$
x^2 = 64 \cdot 3 + 144 - 16 \cdot 12 \cdot \dfrac{3}{2}
$$

$$
x^2 = 192 + 144 - 16 \cdot 12 \cdot \dfrac{3}{2}
$$

$$
x^2 = 192 + 144 - 16 \cdot 6 \cdot 3
$$

$$
x^2 = 192 + 144 - 288 = 48
$$

$$
x = \sqrt{48} = \sqrt{16 \cdot 3} = 4 \sqrt{3}
$$

Altså er $BD = 4 \sqrt{3}$.

Nå kan vi gå videre til å bestemme $AD$. Vi lar nå $x = AD$. Vi bruker cosinussetningen igjen som gir

$$
BD^2 = AB^2 + AD^2 - 2 \cdot AB \cdot AD \cdot \cos 60\degree
$$

Vi setter inn de konkrete verdiene vi har og forenkler så mye som mulig:

$$
(4 \sqrt{3})^2 = 8^2 + x^2 - 2 \cdot 8 \cdot x \cdot \dfrac{1}{2}
$$

$$
48 = 64 + x^2 - 8x
$$

$$
x^2 - 8x + 16 = 0 \liff (x - 4)^2 = 0
$$

Altså må $x = 4$ som betyr at

$$
AD = 4.
$$
::::


:::::::::::::::