# Vekstfart


:::{goals} Læringsmål
* Kunne bestemme gjennomsnittlig vekstfart til en funksjon.
* Kunne bestemme den momentane vekstfarten til en funksjon.
* Kunne bestemme den deriverte til en andregradsfunksjon og bruke den til å finne egenskaper ved funksjonen.
:::

Når vi jobbet med lineære funksjoner, så var en sentral egenskap at de har et stigningstall. Stigningstallet forteller oss hvor mye funksjonsverdier endrer seg når vi endrer $x$-verdien med én enhet. Mer generelt kaller vi dette for en funksjon sin **vekstfart**. Målet vårt her er å definere meningsfulle måter å måle hvor mye funksjonsverdien til en andregradsfunksjon endrer seg når vi endrer på $x$-verdien.


## Gjennomsnittlig vekstfart
**Gjennomsnittlig vekstfart** er et mål på hvor mye funksjonsverdien endrer seg i *gjennomsnitt* i et intervall dersom vi øker $x$ med én enhet. Vi kan tolke dette som stigningstallet til en rett linje som går gjennom to punkter på grafen til funksjonen. 


:::{margin} Husk: Stigningstall
Formelen for gjennomsnittlig vekstfart er akkurat den samme som for stigningstallet til en lineær funksjon:

$$
a = \dfrac{\Delta y}{\Delta x} = \dfrac{y_2 - y_1}{x_2 - x_1}
$$

Vi bare bruker litt annen notasjon for å uttrykke at det er en egenskap ved en funksjon $f$.

:::

:::::::::::::::{summary} Gjennomsnittlig vekstfart
Den **gjennomsnittlige vekstfarten** til en andregradsfunksjon $f$ i intervallet $[a, b]$ er gitt ved 

$$
\dfrac{\Delta f}{\Delta x} = \dfrac{f(b) - f(a)}{b - a}
$$

Se figuren nedenfor. Linja som går gjennom de to punktene kaller vi for en **sekant**. Den gjennomsnittlige vekstfarten er altså stigningstallet til sekanten.


:::{plot}
width: 80%
function: 2 * (x - 2) ** 2 + 1, f
line: (f(4) - f(1)) / 3, (1, f(1)), solid
point: (1, f(1))
point: (4, f(4))
ymin: -2
xmin: -1
ymax: 11
xmax: 5
text: 1, f(1), "$(a, f(a))$", center-right
text: 4, f(4), "$(b, f(b))$", center-right
vline: 2, f(4) - 2*(f(4) - f(1))/3, f(4), dashed, gray
hline: f(4), 2, 4, dashed, gray
annotate: (0.3, f(4)), (2, f(4) - (f(4) - f(1))/3), "$\displaystyle \frac{f(b) - f(a)}{b - a}$", 0.3
text: 3, f(4), "$1$", top-center
ticks: off
nocache:
:::





:::::::::::::::


La oss se på et eksempel: 

:::::::::::::::{example} Eksempel 1
Nedenfor vises grafen til en andregradsfunksjon $f$. 

Bestem den gjennomsnittlige vekstfarten til $f$ i intervallet $[1, 3]$. 

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{solution}
---
dropdown: 0
---
Fra grafen til $f$ ser vi at $f(1) = -4$ og $f(3) = 0$. Den gjennomsnittlige vekstfarten i intervallet $[1, 3]$ er da gitt ved

$$
\dfrac{f(3) - f(1)}{3 - 1} = \dfrac{0 - (-4)}{3 - 1} = \dfrac{4}{2} = 2
$$

Altså øker funksjonsverdien til $f$ i gjennomsnitt med $2$ når vi øker $x$ med $1$ i intervallet $[1, 3]$.
::::


:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 1
En andregradsfunksjon $f$ er vist i figuren nedenfor.

Bestem den gjennomsnittlige vekstfarten til $f$ i intervallet $[-2, 1]$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
\dfrac{f(1) - f(-2)}{1 - (-2)} = -1
$$
::::


::::{solution}
Vi ser fra grafen til $f$ at $f(-2) = 3$ og $f(1) = 0$. Den gjennomsnittlige vekstfarten i intervallet $[-2, 1]$ er da gitt ved

$$
\dfrac{f(1) - f(-2)}{1 - (-2)} = \dfrac{0 - 3}{1 + 2} = \dfrac{-3}{3} = -1
$$


::::


:::::::::::::::



## Momentan vekstfart
**Momentan vekstfart** er et mål på hvor mye funksjonsverdien endrer seg når vi øker $x$ med en veldig liten verdi. Vi kan tolke det som et mål på hvor bratt grafen er i et punkt. Vi skal se på momentan vekstfart som stigningstallet til en lineær funksjon som vi kaller for en **tangent**. 


:::::::::::::::{summary} Momentan vekstfart
Den **momentane vekstfarten** til en andregradsfunksjon $f$ i $x = a$, er gitt ved stigningstallet til en linje som berører grafen til $f$ i punktet $(a, f(a))$. Denne linjen kaller vi for en **tangent**. 

Vi definerer en ny skrivemåte for den momentane vekstfarten:

$$
f'(a) = \text{Momentan vekstfart til $f$ i punktet $(a, f(a))$}
$$

Se figuren nedenfor. 


:::{plot}
width: 70%
function: (x - 1)**2 + 1, f
point: (2, f(2))
text: 2, f(2), "$(a, f(a))$", top-left
ymin: -2
xmin: -2
tangent: 2, f, solid
vline: 3, 2, 4, dashed, gray
hline: 2, 2, 3, dashed, gray
text: 2.5, 2, "$1$", bottom-center
annotate: (4.5, 1.5), (3, 3), "$\displaystyle f'(a)$", 0.3
ticks: off
:::


:::::::::::::::


Det er ikke opplagt hvordan vi kan finne stigningstallet til en tangent, siden det er en linje der vi bare vet om ett punkt på linja. Vi skal snart se hvordan vi kan gjøre dette med regning, men det er hensiktsmessig å først se hvordan vi kan gjøre det med digitale verktøy. La oss se på et eksempel:


:::::::::::::::{example} Eksempel 2
I gif-en nedenfor viser vi hvordan vi kan bestemme likningen til en tangent til grafen til en andregradsfunksjon $f$ i punktet $(3, f(3))$. Andregradsfunksjonen er gitt ved 

$$
f(x) = x^2 - 4x + 5.
$$


:::{figure} ./videoer/finne_tangenter_ggb.gif
---
class: no-click, adaptive-figure
width: 100%
---
:::

Likningen til tangenten i $(3, f(3))$ er 

$$
y = 2x - 4
$$

Stigningstallet til tangenten er $2$. Den momentane vekstfarten til $f$ i punktet $(3, f(3))$ er dette stigningstallet. Vi skriver dette som

$$
f'(3) = 2
$$




:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2

:::{ggb-popup}
---
layout: sidebar
---
:::



En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = -x^2 + 4x + 1
$$

Bruk Geogebra-vinduet til å bestemme den momentane vekstfarten til $f$ i punktet $(1, f(1))$. 

::::{answer}
$$
f'(1) = 2
$$
::::

::::{solution}
Vi skriver inn funksjonsuttrykket, lager punktet og bruker `Tangent(punkt, funksjon)` for å finne likningen til tangenten. Se figuren nedenfor:

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/sol.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at likningen til tangenten er 

$$
y = 2x + 2
$$

Stigningstallet til tangenten er $2$. Den er den momentane vekstfarten til $f$ i punktet $(1, f(1))$ er dette stigningstallet. Vi skriver dette som:

$$
f'(1) = 2
$$


::::

:::::::::::::::




## Den deriverte
Siden vi kan bestemme stigningstallet til tangenter overalt på grafen til en andregradsfunksjon, er det naturlig å lure på om det finnes en funksjon som gir oss stigningstallet i alle punkter på grafen. Det gjør det, og denne funksjonen kaller vi for **den deriverte** til $f$. Vi skriver denne funksjonen som $f'$ og leser det som "$f$-derivert".




:::::::::::::::{summary} Den deriverte
**Den deriverte** til en andregradsfunksjon $f(x) = ax^2 + bx + c$ er en lineær funksjon gitt ved 

$$
f'(x) = 2ax + b
$$


::::{multi-plot2}
---
rows: 1
cols: 2
---

:::{plot}
function: (x - 1)**2 + 1, f 
ticks: off
fontsize: 26
xmin: -2
ymin: -1
ymax: 4
xmax: 4
lw: 3
point: (1, f(1))
hline: f(1), 1, 2, dashed, gray
vline: 2, f(1), f(2), dashed, gray
text: (1 + 2)/2, f(1), "$1$", bottom-center
text: 2, (f(1) + f(2))/2, "$a$", center-right
:::

:::{plot}
function: 2*(x - 1), f' 
fontsize: 26
xmin: -2
ymax: 4
ymin: -2
ticks: off
lw: 3
point: (1, 0)
hline: 2*(1.5 - 1), 1.5, 2.5, dashed, gray
vline: 2.5, 2*(1.5 - 1), 2*(2.5 - 1), dashed, gray
text: (1.5 + 2.5) / 2, 2*(1.5 - 1), "$1$", bottom-center
text: 2.5, (2*(1.5 - 1) + 2*(2.5 - 1)) / 2, "$2a$", center-right
annotate: (2.5, -1), (1, 0), "Symmetrilinja til $f$", -0.3
:::



::::


:::{plot}
function: 2*(x - 1), f' 
fontsize: 26
xmin: -2
ymax: 4
ymin: -4
ticks: off
lw: 3
point: (1, 0)
hline: 2*(1.5 - 1), 1.5, 2.5, dashed, gray
vline: 2.5, 2*(1.5 - 1), 2*(2.5 - 1), dashed, gray
text: (1.5 + 2.5) / 2, 2*(1.5 - 1), "$1$", bottom-center
text: 2.5, (2*(1.5 - 1) + 2*(2.5 - 1)) / 2, "$2a$", center-right
annotate: (3.5, -1), (1, 0), "$x = -\frac{b}{2a}$", -0.3
nocache:
:::




::::::::::::::{admonition} Bevis
---
class: dropdown, theory
---
La $f$ være en andregradsfunksjon og la $T$ være en tangent til grafen til $f$ i et vilkårlig punkt $(x_0, f(x_0))$. Vi kan uttrykke de to funksjonene som

$$
f(x) = ax^2 + bx + c \qog T(x) = Ax + B
$$

der $A$ er stigningstallet til tangenten. Siden stigningstallet til tangenten er lik den momentane vekstfarten til $f$ i punktet $(x_0, f(x_0))$, er målet vårt å bestemme et uttrykk for $A$. Først kan vi observere at siden tangenten bare skjærer grafen til $f$ i ett punkt, vil likningen 

$$
f(x) = T(x)
$$

bare ha én løsning. Hvis vi trekker $T(x)$ over på venstre side, får vi en andregradsfunksjon $f - T$ som bare skjærer $x$-aksen i $x = x_0$. Dette derfor også symmetrilinja til $f - T$. Se figuren nedenfor: 

::::{multi-plot2}
---
rows: 1
cols: 2
---

:::{plot}
function: 0.5*(x + 1)**2 - 4, f
tangent: 1, f
point: (1, f(1))
fontsize: 26
ticks: off
text: 1, f(1), "$(x_0, f(x_0))$", center-right
:::


:::{plot}
function: 0.5 * (x + 1)**2 - 4 - (2*x - 4), f-T
point: (1, 0)
vline: 1, dashed, gray
fontsize: 26
ticks: off
text: 1, 0, "$(x_0, 0)$", bottom-right
annotate: (-6, 4), (1, 4), "Symmetrilinje $x = x_0$"
:::


::::




La oss utføre denne regningen:

$$
f(x) - T(x) = ax^2 + bx + c - (Ax + B) = ax^2 + (b - A)x + (c - B)
$$

Siden denne funksjonen har $x = x_0$ som symmetrilinje, kan vi bruke formelen for symmetrilinja til en andregradsfunksjon:

$$
x_0 = -\frac{b - A}{2a} \liff -2ax_0 = b - A \liff A = 2ax_0 + b
$$

Siden $A$ er stigningstallet til tangenten, er det også den momentane vekstfarten til $f$ i punktet $(x_0, f(x_0))$. Vi skriver dette som

$$
f'(x_0) = 2ax_0 + b
$$

Punktet $x_0$ var vilkårlig, så dette vil stemme for alle punkter på grafen til $f$. Derfor kan vi konkludere at funksjonen for den momentane vekstfarten – den deriverte – er 

$$
f'(x) = 2ax + b
$$

::::::::::::::

:::::::::::::::

---


La oss se på et eksempel hvor vi bruker formelen: 

:::::::::::::::{example} Eksempel 3
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = 3x^2 - 6x + 2
$$

Bestem $f'(x)$. 


::::{solution}
---
dropdown: 0
---
Den deriverte er gitt ved 

$$
f'(x) = 2ax + b
$$

Vi har at $a = 3$ og $b = -6$, så 

$$
f'(x) = 2 \cdot 3 \cdot x - 6 = 6x - 6
$$
::::

:::::::::::::::


---


Vi kan også se på en konkret sammenheng mellom $f$ og $f'$ dersom $f(x)$ er skrevet på ekstremalpunktsform 
ved å merke oss at nullpunktet til $f'$ ligger i symmetrilinja til $f$. Dette stemmer fordi

$$
f'(x) = 0 \liff 2ax + b = 0 \liff 2ax = -b \liff x = -\frac{b}{2a}
$$

Derfor må det være mulig å skrive $f'(x)$ på nullpunktsform som

$$
f'(x) = 2a(x - x_0) \qder x_0 = -\frac{b}{2a}
$$


:::::::::::::::{summary} Den deriverte på nullpunktsform
Den deriverte til en andregradsfunksjon $f(x) = a(x - x_0)^2 + y_0$ er gitt ved

$$
f'(x) = 2a(x - x_0)
$$

:::::::::::::::



### Grafisk sammenheng mellom $f$ og $f'$ 

I animasjonen nedenfor vises sammenhengen mellom grafen til $f$ og grafen til $f'$. Grafen til en andregradsfunksjon $f$ er vist til venstre og grafen til den deriverte $f'$ er vist til høyre.

:::{video} ./videoer/den_deriverte.mp4
---
width: 95%
class: manim-video
---
:::

Vi kan oppsummere noen viktige observasjoner fra animasjonen: 

:::::::::::::::{summary} Grafisk sammenheng mellom $f$ og $f'$
* Grafen til $f$ stiger når $f'(x) > 0$. 
* Grafen til $f$ synker når $f'(x) < 0$.
* Grafen til $f$ har et ekstremalpunkt når $f'(x) = 0$. Symmetrilinja til $f$ svarer til nullpunktet til den deriverte $f'$. 
:::::::::::::::

La oss se på et konkret eksempel som illustrerer dette:


:::::::::::::::{example} Eksempel 4
I figuren nedenfor vises grafen til en andregradsfunksjon $f$ til venstre og grafen til den deriverte $f'$ til høyre. 

:::{figure} ./figurer/eksempler/eksempel_4/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
grafen til $f$ vises til venstre og grafen til $f'$ vises til høyre.
:::

Vi kan legge merke til følgende:
* Symmetrilinja til $f$ er $x = -2$. Vi kan også se at da skjærer grafen til $f'$ gjennom $x$-aksen. Med andre ord er $f'(x) = 0$ ved ekstremalpunktet til $f$.
* Til venstre for ekstremalpunktet til $f$, så stiger grafen. Vi kan se at på det tilsvarende område, så ligger grafen til $f'$ over $x$-aksen. Altså er $f'(x) > 0$ og da stiger grafen til $f$.
* Til høyre for ekstremalpunktet til $f$, så synker grafen. Vi kan se at på det tilsvarende område, så ligger grafen til $f'$ under $x$-aksen. Altså er $f'(x) < 0$ og da synker grafen til $f$.

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 4

:::{plot}
align: right
width: 350
function: (x - 2)**2 - 4, f
fontsize: 26
lw: 4
:::


Grafen til en andregradsfunksjon $f$ er vist i figuren til høyre. 

Nedenfor vises det fire grafer der én viser grafen til den deriverte $f'$. 

Hvilken graf viser grafen til $f'$?


:::{multi-plot}
width: 100%
functions: 2*x - 4, -2*x + 4, 2*x, -2*(x - 4)
function-names: A, B, C, D
rows: 2
cols: 2
:::



::::{answer}
Graf A.
::::

::::{solution}
Grafen til $f$ har symmetrilinje i $x = 2$. Det betyr at $f'$ må skjære $x$-aksen i $x = 2$ som både bare graf A og B gjør. Dermed kan vi utelukke graf C og D. Til venstre for symmetrilinja synker grafen til $f$ så her må 

$$
f'(x) < 0 \liff \text{grafen til $f'$ må ligge under $x$-aksen.}
$$

Til høyre for symmetrilinja stiger grafen til $f$ så her må

$$
f'(x) > 0 \liff \text{grafen til $f'$ må ligge over $x$-aksen.}
$$

Dette stemmer for graf A, men ikke for graf B. Dermed er det graf A som viser grafen til $f'$.
::::


:::::::::::::::


## Anvendelser av den deriverte
Den deriverte gir oss et nytt verktøy for å finne egenskapene til en andregradsfunksjon. Vi kan bruke den til å finne symmetrilinja til grafen, likningen til tangenter, og vi kan bruke den til å bestemme $f(x)$ og $f'(x)$ når vi har informasjon om grafen.


### Bestemme ekstremalpunkt
Vi har sett at grafen til den deriverte $f'$ skjærer $x$-aksen i samme punkt som grafen til $f$ har ekstremalpunkt. Eller sagt med andre ord, samme $x$-verdi som grafen til $f$ har symmetrilinje. Vi kan se at dette stemmer ved å sette $f'(x) = 0$ og løse likningen for $x$:

$$
f'(x) = 0 \liff 2ax + b = 0 \liff 2ax = -b \liff x = -\frac{b}{2a}
$$

:::{margin}
Å løse $f'(x) = 0$ for å finne ekstremalpunkter kommer til å bli et viktig verktøy når vi senere skal jobbe med andre funksjoner.
:::

Her har vi gode gamle formelen for symmetrilinja til en andregradsfunksjon! Det betyr at vi nå har et nytt verktøy for å finne symmetrilinja – eller $x$-koordinaten til ekstremalpunktet til grafen til $f$. La oss se på et eksempel:


:::::::::::::::{example} Eksempel 5
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 8x + 5
$$

Bestem symmetrilinja til grafen til $f$.


::::{solution}
---
dropdown: 0
---
Vi bestemmer $f'(x)$ først. Vi ser at $a = 1$ og $b = -8$, så vi får

$$
f'(x) = 2 \cdot 1 \cdot x - 8 = 2x - 8
$$

Deretter løser vi likningen 

$$
f'(x) = 0 \liff 2x - 8 = 0 \liff x = 4
$$

Altså er symmetrilinja til grafen til $f$ gitt ved 

$$
x = 4.
$$

Vi sjekker at dette stemmer overens med formelen for symmetrilinja til en andregradsfunksjon:

$$
x_0 = -\frac{b}{2a} = -\frac{-8}{2 \cdot 1} = 4
$$

Det stemmer! 

::::

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 5
Bruk den deriverte til å finne $x$-verdien til ekstremalpunktet til 

$$
f(x) = -2x^2 + 4x + 1.
$$

Sjekk at svaret ditt stemmer overens ved å bruke formelen for symmetrilinja til en andregradsfunksjon.

::::{answer}
$$
x = 1
$$
::::

::::{solution}
Vi har at $a = -2$ og $b = 4$, så vi får

$$
f'(x) = 2 \cdot (-2) \cdot x + 4 = -4x + 4.
$$

Deretter løser vi likningen 

$$
f'(x) = 0 \liff -4x + 4 = 0 \liff -4x = -4 \liff x = 1.
$$

Vi sjekker at dette stemmer overens med formelen for symmetrilinja til en andregradsfunksjon:

$$
x_0 = -\frac{b}{2a} = -\frac{4}{2 \cdot -2} = 1.
$$

Det stemmer!
::::


:::::::::::::::


### Likningen til en tangent
Når vi introduserte begrepet momentan vekstfart, så vi hvordan vi kan bestemme likningen til en tangent med digitale verktøy. Nå skal vi se hvordan vi kan gjøre det ved regning. Først minner vi oss på at likningen til en lineær funksjon med stigningstall $a$ som går gjennom ett punkt $(x_0, y_0)$ er gitt ved ettpunktsformelen 

$$
y = a(x - x_0) + y_0
$$

Når linja er en tangent, så er stigningstallet $a$ lik den momentane vekstfarten til $f$ i punktet $(x_0, f(x_0))$. Det vil si at $a = f'(x_0)$ og $y_0 = f(x_0)$.  


:::::::::::::::{summary} Likningen til en tangent
Likningen til en tangent til grafen til en andregradsfunksjon $f$ i punktet $(x_0, f(x_0))$ er gitt ved

$$
y = f'(x_0)(x - x_0) + f(x_0)
$$


:::::::::::::::


La oss se på et eksempel: 


:::::::::::::::{example} Eksempel 6
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 3x + 1.
$$

Bestem likningen til tangenten til grafen til $f$ i punktet $(2, f(2))$.


::::{solution}
---
dropdown: 0
---
Likningen til tangenten er gitt ved 

$$
y = a(x - x_0) + y_0
$$

Vi har at $x_0 = 2$. For å bestemme $y$-koordinaten til punktet, regner vi ut $f(2)$:

$$
y_0 = f(2) = 2^2 - 3 \cdot 2 + 1 = 4 - 6 + 1 = -1.
$$

For å bestemme stigningstallet $a = f'(2)$, regner vi først ut den deriverte. 

$$
f'(x) = 2\cdot 1\cdot x - 3.
$$

Deretter setter vi inn $x = 2$:

$$
f'(2) = 2 \cdot 2 - 3 = 4 - 3 = 1.
$$

Altså er stigningstallet til tangenten $a = 1$. Da får vi at likningen til tangenten er gitt ved 

$$
y = 1\cdot(x - 2) - 1 = x - 2 - 1 = x - 3.
$$

::::

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 6
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -2x^2 + 5x + 1
$$

Bestem likningen til tangenten til grafen til $f$ i punktet $(1, f(1))$.


::::{answer}
$$
y = x + 3
$$
::::

::::{solution}
Likningen til tangenten er gitt ved

$$
y = a(x - x_0) + y_0
$$

Vi har at $x_0 = 1$. For å bestemme $y$-koordinaten til punktet, regner vi ut $f(1)$:

$$
y_0 = f(1) = -2\cdot 1^2 + 5\cdot 1 + 1 = -2 + 5 + 1 = 4.
$$

For å bestemme stigningstallet $a = f'(1)$, regner vi først ut den deriverte.

$$
f'(x) = 2\cdot (-2)\cdot x + 5
$$

Deretter setter vi inn $x = 1$:

$$
f'(1) = 2\cdot (-2)\cdot 1 + 5 = -4 + 5 = 1.
$$

Da får vi at likningen til tangenten er gitt ved

$$
y = 1\cdot(x - 1) + 4 = x - 1 + 4 = x + 3.
$$
::::

:::::::::::::::




### Bestemme $f(x)$ og $f'(x)$ 
Vi kan bruke opplysninger om grafen til $f$ og grafen til $f'$ til å bestemme funksjonsuttrykkene $f(x)$ og $f'(x)$. La oss se på et eksempel: 

:::::::::::::::{example} Eksempel 7
I figuren nedenfor vises grafen til en andregradsfunksjon $f$. Grafen har en tangent i punktet $(3, f(3))$ med likningen $y = -4x + 13$.

Bestem $f(x)$ og $f'(x)$.


:::{plot}
width: 70%
function: -x**2 + 2*x + 4, f
point: (0, f(0))
text: 0, f(0), "$(0, 4)$", center-left
point: (3, f(3))
text: 3, f(3), "$(3, f(3))$", top-right
tangent: 3, f
ticks: off
xmin: -3
:::



::::{solution}
---
dropdown: 0
---

:::{cas-popup}
---
layout: sidebar
---
:::

Her bruker vi CAS til å sette opp et likningssystem for å bestemme $f(x)$ og $f'(x)$. Bruk CAS-vinduet til å utføre utregningene som vises nedenfor! 

Vi skriver $f(x)$ på standardform:

$$
f(x) = ax^2 + bx + c.
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, 4)$ som betyr at $f(0) = 4$. 

Likningen til tangenten er gitt ved $y = -4x + 13$. Siden tangenten går gjennom punktet $(3, f(3))$, kan vi bestemme $f(3)$ ved å sette inn $x = 3$ i likningen til tangenten:

$$
f(3) = -4 \cdot 3 + 13 = -12 + 13 = 1.
$$

Stigningstallet til tangenten er $-4$, som betyr at $f'(3) = -4$ siden stigningstallet til tangenten er lik den momentane vekstfarten til $f$ i punktet $(3, f(3))$. Da har vi tre likninger:

\begin{align*}
f(0) &= 4 && \text{Skjæring med $y$-aksen} \\
\\
f(3) &= 1 && \text{Punktet tangenten treffer} \\
\\
f'(3) &= -4 && \text{Stigningstallet til tangenten}
\end{align*}

Vi løser likningsssystemet med CAS for å bestemme $a$, $b$ og $c$:


:::{figure} ./figurer/eksempler/eksempel_7/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

> Vi skriver `f'(x)` for å få den deriverte til $f$ i CAS-vinduet.

Fra utskriften ser vi at 

$$
a = 1 \and b = -2 \and c = 4.
$$

Det betyr at 

$$
f(x) = ax^2 + bx + c = x^2 - 2x + 4.
$$

og

$$
f'(x) = 2ax + b = 2\cdot 1\cdot x - 2 = 2x - 2.
$$



::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 7


:::{cas-popup}
---
layout: sidebar
---
:::


I figuren nedenfor vises grafen til en andregradsfunksjon $f$. 

Grafen har en tangent i punktet $(-2, f(-2))$ med stigningstall $2$ og en tangent som går gjennom ett av nullpunktene til $f$ med likningen $y = -4x + 4$. 

Bestem $f(x)$ og $f'(x)$.


:::{plot}
width: 70%
function: -x**2 - 2*x + 3, f
point: (-2, f(-2))
text: -2, f(-2), "$(-2, f(-2))$", top-left
tangent: -2, f
point: (1, f(1))
tangent: 1, f
ymin: -2
xmax: 3
ticks: off 
ymax: 8
:::


::::{answer}
$$
f(x) = -x^2 - 2x + 3 \qog f'(x) = -2x - 2.
$$
::::

::::{solution}
Vi starter med tangenten som går gjennom punktet $(-2, f(-2))$. Siden stigningstallet er $2$, så betyr det at den deriverte er lik denne verdien i $x = -2$. Altså er $f'(-2) = 2$.

Den andre tangenten går gjennom den ene nullpunktet til $f$. Vi kan bestemme nullpunktet ved å sette likningen til tangenten lik null: 

$$
0 = -4x + 4 \liff 4x = 4 \liff x = 1.
$$

Da vet vi at ett av nullpunktene til $f$ er $x = 1$ og da må $f(1) = 0$. 

Stigningstallet til den samme tangenten er $-4$ så da må $f'(1) = -4$. Da har vi tre likninger:


\begin{align*}
f'(-2) = 2 && \text{Stigningstallet til tangenten i $(-2, f(-2))$} \\
\\
f(1) = 0 && \text{Nullpunktet til $f$} \\
\\
f'(1) = -4 && \text{Stigningstallet til tangenten i nullpunktet}
\end{align*}

Da kan vi bruke CAS til å løse likningssystemet: 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_7/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at 

$$
a = -1 \and b = -2 \and c = 3. 
$$

Det betyr at

$$
f(x) = -x^2 - 2x + 3 \qog f'(x) = -2x - 2.
$$


::::



:::::::::::::::








