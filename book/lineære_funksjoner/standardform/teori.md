# Standardform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en lineær funksjon på standardform og beskrive sammenhengen med den grafiske representasjonen.
* Kunne bytte fra en representasjon til en annen.
:::

En lineær funksjon er en rett linje som du kanskje har lært å beskrive med en likning

$$
y = ax + b 
$$


der vi setter inn en verdi for $x$ for å finne den **tilhørende** verdien for $y$. Gjør vi dette med mange ulike verdier for $x$, får vi en samling punkter $(x, y)$ – dette kaller vi for **grafen** til den lineære funksjonen. Vi gir gjerne funksjonen et navn, for eksempel $f$, og skriver funksjonsuttrykket som

$$
f(x) = ax + b
$$

som betyr at $y = f(x)$. Vi kaller $f(x)$ for **funksjonsverdien** når vi tenker på et bestemt tall $x$, og **funksjonsuttrykket** når vi ikke tenker på noe spesielt tall for $x$.


:::::::::::::::{admonition} Påminnelse: Koordinatsystemet
---
class: summary
---

Koordinatsystemet består av to tallinjer som vi kaller for **akser**. De to aksene er:
* $x$-aksen (den horisontale aksen - også kalt *førsteaksen*).
* $y$-aksen (den vertikale aksen - også kalt *andreaksen*).

Punktet der aksene møtes kaller vi for **origo**. Origo har koordinatene $(0, 0)$.

For å finne et punkt $(x, y)$ i koordinatsystemet, går vi $x$ plasser parallelt med $x$-aksen og $y$ plasser parallelt med $y$-aksen. Da står vi på punktet $(x, y)$. 
Vi kaller $x$-verdien til punktet for $x$-koordinaten og $y$-verdien for $y$-koordinaten.

I figuren nedenfor vises en konkret eksempel med punktet $(3, 2)$.


:::{plot}
point: (3, 2)
text: 3, 2, "$(3, 2)$", top-right
hline: 2, 0, 3
vline: 3, 0, 2
width: 80%
:::

:::::::::::::::


---




:::::::::::::::{example} Eksempel 1
I figuren nedenfor vises grafen til en lineær funksjon $f$ gitt ved 

$$
f(x) = 2x + 1.
$$


:::{plot}
function: 2 * x + 1, f
width: 70%
annotate: (3.5, 2), (2, 5), "$(2, f(2))$"
point: (2, 5)
xmin: -3
ymax: 8
vline: 2, 0, 5
hline: 5, 0, 2
:::



I figuren har vi markert et punkt $(2, f(2))$ på grafen til $f$. Vi ser at $x$-koordinaten til dette punktet er $2$ og $y$-koordinaten er $5$. Det betyr at 

$$
f(2) = 5
$$

Vi kan også sjekke at dette stemmer ved å regne ut verdien med funksjonsuttrykket til $f$:

$$
f(\textcolor{red}{2}) = 2 \cdot \textcolor{red}{2} + 1 = 4 + 1 = 5. 
$$


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 3x - 2
$$

Bestem $f(1)$ ved
1. Å regne ut med funksjonsuttrykket
2. Ved å lese av fra grafen til $f$ vist i figuren nedenfor.


:::{plot}
function: 3*x - 2, f
width: 70%
:::


::::{answer}
$$
f(1) = 1
$$
::::




:::::::::::::::


## Standardform: Algebraisk og grafisk representasjon


En **representasjon** er en måte å beskrive noe på. En lineær funksjon kan representeres på flere måter, for eksempel med en formel som vi gjerne kaller for en **algebraisk representasjon**. En lineær funksjon kan også representeres grafisk med en **graf**. Det finnes flere representasjoner, men disse er de to viktigste. 

En algebraisk representasjon kan gi oss umiddelbar informasjon om grafen til en funksjon. Å velge en representation som er hensiktmessig for å løse en oppgave er en viktig ferdighet i matematikk. Den første vi skal se på kaller vi for **standardform**. 


:::::::::::::::{summary} Standardform: Algebraisk representasjon

En lineær funksjon $f$ kan skrives på **standardform** som

:::{figure} ./figurer/teori/algebraisk/standardform.svg
---
width: 70%
class: no-click, adaptive-figure
:::

* Verdien til $a$ er hvor mye $f(x)$ endrer seg når vi øker $x$ med $1$. Vi kaller $a$ for **stigningstallet** til grafen til $f$.
* Verdien til $b$ er $y$-koordinaten til skjæringspunktet mellom grafen til $f$ og $y$-aksen. Vi kaller ofte $b$ for **konstantleddet** til $f(x)$.


:::{plot}
function: 2*x - 1, f 
width: 80%
hline: 1, 1, 2
vline: 2, 1, 3
grid: off
xmin: -2
xmax: 5
ymin: -2
ymax: 5
text: 1.5, 1, "$1$", bottom-center
text: 2, 2, "$a$", center-right
point: (0, -1)
annotate: (1, -1), (0, -1), "Skjæring med $y$-aksen $(0, b)$", -0.4
:::


:::::::::::::::

---


:::::::::::::::{example} Eksempel 2
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor. 

Bestem $f(x)$.


:::{plot}
function: -2*x + 1, f
width: 70%
:::



::::{solution}
---
dropdown: 0
---
En lineær funksjon på standardform er gitt ved

$$
f(x) = ax + b
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, 1)$ som betyr at $b = 1$. 

Hvis vi velger ut et punkt på grafen til $f$, for eksempel $(0, 1)$, så ser vi at når vi øker $x$ med $1$, så synker funksjonsverdien $f(x)$ med $-2$ (husk $y = f(x)$) som betyr at stigningstallet er $a = -2$. 

Da er $f(x)$ gitt ved

$$
f(x) = ax + b = -2 \cdot x + 1 = -2x + 1
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2 
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$. 


:::{plot}
function: 3*x - 4, f
width: 70%
:::


::::{answer}
$$
f(x) = 3x - 4
$$
::::

::::{solution}
En lineær funksjon på standardform er gitt ved 

$$
f(x) = ax + b
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -4)$ som betyr at $b = -4$. 

Hvis vi velger et punkt på grafen til $f$, for eksempel $(0, -4)$ og øker $x$ med $1$, så er vi at $f(x)$ øker med $3$ siden grafen går gjennom punktet $(1, -1)$. Det betyr at stigningstallet er $a = 3$. 

Da er 

$$
f(x) = 3 \cdot x - 4 = 3x - 4
$$
::::


:::::::::::::::



---


La oss se på et eksempel der vi går fra funksjonsuttrykk til graf. 

:::::::::::::::{example} Eksempel 3
En lineær funksjon $f$ er gitt ved 

$$
f(x) = -x + 2
$$

Lag en skisse av grafen til $f$. 


::::{solution}
---
dropdown: 0
---
Fra funksjonsuttrykket

$$
f(x) = -x + 2 = (-1) \cdot x + 2
$$

ser vi at stigningstallet til $f$ er $a = -1$ og konstantleddet er $b = 2$. Det betyr at grafen til $f$ skjærer $y$-aksen i $(0, 2)$. Da kan vi lage følgende skisse av grafen til $f$:


:::{plot}
function: -x + 2, f
width: 70%
grid: off
point: (0, 2)
text: 0, 2, "$(0, 2)$", center-right
hline: 4, -2, -1
vline: -1, 4, 3
xmin: -4
xmax: 4
ymax: 5
ymin: -3
text: -1.5, 4, "$1$", top-center
text: -1, 3.5, "$-1$", center-right


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
En lineær funksjon $f$ er gitt ved

$$
f(x) = -2x + 3
$$

Lag en skisse av grafen til $f$ der du markerer skjæringspunktet med $y$-aksen og stigningstallet.


::::{answer}
:::{plot}
function: -2*x + 3, f
width: 70%
grid: off
point: (0, 3)
text: 0, 3, "$(0, 3)$", center-left
ymin: -2
hline: 2, 0.5, 1.5
vline: 1.5, 0, 2
text: 1, 2, "$1$", top-center
text: 1.5, 1, "$-2$", center-right
:::
::::


::::{solution}
Vi har at 

$$
f(x) = (-2) \cdot x + 3
$$

som betyr at stigningstallet er $a = -2$ og konstantleddet er $b = 3$. Grafen til $f$ skjærer derfor $y$-aksen i $(0, 3)$. 

Ut ifra denne informasjonen kan vi tegne følgende skisse av grafen til $f$.


:::{plot}
function: -2*x + 3, f
width: 70%
grid: off
point: (0, 3)
text: 0, 3, "$(0, 3)$", center-left
ymin: -2
hline: 2, 0.5, 1.5
vline: 1.5, 0, 2
text: 1, 2, "$1$", top-center
text: 1.5, 1, "$-2$", center-right
:::
::::


:::::::::::::::



## Topunktsformelen

Vi vet allerede nå at vi kan bestemme stigningstallet $a$ til en lineær funksjon ved å sjekke hvor mye $f(x)$ endrer seg når vi øker $x$ med $1$. Men vi vet ikke alltid funksjonsverdier til $f$ i $x$-verdier som ligger en avstand $1$ fra hverandre. Da trenger vi en annen metode for å bestemme stigningstallet. 


:::::::::::::::{summary} Topunktsformelen
Hvis grafen til en lineær funksjon $f$ går gjennom punktene $(x_1, y_1)$ og $(x_2, y_2)$, så er stigningstallet $a$ gitt ved 

$$
a = \dfrac{\Delta y}{\Delta x} = \dfrac{y_2 - y_1}{x_2 - x_1}
$$


der vi har definert

$$
\Delta y = y_2 - y_1 \qog \Delta x = x_2 - x_1
$$

Vi leser symbolet $\Delta$ som "endring i" slik at $\Delta y$ betyr "endring i $y$-verdien" og $\Delta x$ betyr "endring i $x$-verdien". Stigningstallet er altså endringen i $y$-verdien delt på endringen i $x$-verdien.


:::{plot}
function: x + 1
width: 70%
grid: off
xmin: -1
xmax: 4.5
ymin: -1
point: (1, 2)
point: (4, 5)
text: 1, 2, "$(x_1, y_1)$", top-left
text: 4, 5, "$(x_2, y_2)$", top-left
hline: 2, 1, 4
vline: 4, 2, 5
text: 2.5, 2, "$\Delta x$", bottom-center
text: 4, 3.5, "$\Delta y$", center-right
:::




:::::::::::::::

---


:::::::::::::::{example} Eksempel 4
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$.

:::{plot}
function: 3*x - 5, f
width: 70%
grid: off
xmin: -2
xmax: 5
ymin: -7
ymax: 5
point: (0, -5)
point: (2, 1)
text: 0, -5, "$(0, -5)$", center-left
text: 2, 1, "$(2, 1)$", center-right
:::


::::{solution}
---
dropdown: 0
---
En lineær funksjon på standardform er gitt ved

$$
f(x) = ax + b.
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -5)$ som betyr at $b = -5$. 

Vi ser at grafen til $f$ også går gjennom punktet $(2, 1)$. Vi kan bruke topunktsformelen til å bestemme stigningstallet:

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{1 - (-5)}{2 - 0} = \dfrac{6}{2} = 3
$$

Dermed er 

$$
f(x) = 3x - 5
$$
::::

:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 4
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor. 

Bestem $f(x)$.



:::{plot}
function: -2*x + 4, f
width: 70%
grid: off
point: (0, 4)
text: 0, 4, "$(0, 4)$", center-left
point: (3, -2)
text: 3, -2, "$(3, -2)$", center-right
ymin: -5
ymax: 5
xmax: 5
xmin: -1
:::



::::{answer}
$$
f(x) = -2x + 4
$$
::::

::::{solution}
Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, 4)$ som betyr at $b = 4$. 

Vi ser grafen også går gjennom punktet $(3, -2)$. Vi bestemmer stigningstallet med topunktsformelen:

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{-2 - 4}{3 - 0} = \dfrac{-6}{3} = -2
$$

Dermed er 

$$
f(x) = -2x + 4
$$
::::


:::::::::::::::










