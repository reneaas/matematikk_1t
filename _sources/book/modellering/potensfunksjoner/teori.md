# Potensfunksjoner

:::{admonition} Læringsmål
---
class: tip
---
* Kan forklare begrepet proprosjonalitet og anvende begrepet proporsjonalitet.
* Kan beskrive egenskapene til potensfunksjoner.
* Kjenner til sammenhengen mellom potensfunksjoner og rotfunksjoner.
:::


Mange sammenhenger både i naturen og i samfunnet kan beskrives ved hjelp av **potensfunksjoner**. Potensfunksjoner er sterkt knyttet til begrepet **proporsjonalitet**. 



## Proporsjonalitet

**Proporsjonalitet** er et begrep som vi bruker til å beskrive at sammenhengen mellom to størrelser $x$ og $y$ kan uttrykkes som $y = a \cdot x$ der $a$ kalles for en **proprosjonalitetskonstant**.

:::::::::::::::{example} Eksempel 1
La oss si at hektoprisen for smågodt på butikken er $15$ kr/hg. Prisen $P$ vi må betale når vi kjøper $x$ hg smågodt er da

$$
P(x) = 15 \cdot x
$$

Dersom vi dobler mengden smågodt fra $x$ til $2x$, så får vi

$$
P(2x) = 15 \cdot (2x) = 2 \cdot (15 \cdot x) = 2 \cdot P(x)
$$

Det betyr at når vi dobler mengden smågodt, så dobles også prisen. Vi sier da at $P$ er proprosjonal med $x$ og skriver det $P \propto x$. Proprosjonalitetskonstanten er $15~\mathrm{kr/hg}$.
:::::::::::::::

---

Men at to størrelser er proprosjonale betyr ikke nødvendigvis at det er en lineær sammenheng. Vi kan mer generelt ha at $y$ er proprosjonal med $x^b$ for en konstant $b$. 


:::::::::::::::{example} Eksempel 2
Arealet $A$ av et rektangel med sidelengde $s$ er lik $A(s) = s^2$. Dersom vi dobler verdien til $s$, så får vi

$$
A(2s) = (2s)^2 = 2^2 s^2 = 4 \cdot s^2 = 4 \cdot A(s)
$$

Altså blir arealet $4$ ganger større når vi dobler sidelengden $s$. I dette tilfellet sier vi at arealet $A$ er proprosjonalt med $s^2$ og skriver det $A \propto s^2$.
:::::::::::::::

---

:::::::::::::::{summary} Proporsjonalitet
Dersom en størrelse $y$ er proporsjonal med $x^b$ for en konstant $b$, så betyr det at det finnes en **proporsjonalitetskonstant** $a$ slik at

$$
y = a \cdot x^b
$$

Vi sier da at $y$ og $x^b$ er **proprosjonale** størrelser og skriver det $y \propto x^b$.

:::::::::::::::



## Potensfunksjoner
Konseptet om proporsjonalitet som vi har beskrevet over kan generaliseres til en funksjonsklasse vi kaller for **potensfunksjoner**.

:::::::::::::::{summary} Potensfunksjoner
En potensfunksjon $f$ er en funksjon skrevet på formen

$$
f(x) = a \cdot x^b
$$


der $a$ og $b$ er konstanter. Tallet $a$ kaller vi for en **proporsjonalitetskonstant**.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
width: 100%
def: f(x) = x**1.5
function: x**1.5, (0, 10), blue
function: x**0.5, (0, 10), red
function: x**-2, (1e-4, 10), green
xmin: -0.5
xmax: 3
ymin: -0.5
ymax: 3
point: (1, f(1))
text: 0.9, f(1), "$(1, a)$", top-left
text: 0.95, 2.5, "$b < 0$", center-center
text: 2.5, 1.2, "$0 < b < 1$", center-center
text: 2.2, 2.5, "$b > 1$", center-center
ticks: off
fontsize: 28
:::

:::{interactive-graph} 
interactive-var: a, 0, 6, 25
interactive-var: b, -5, 5, 49
interactive-var-start: a=1, b=2
function: a * x**b, (0, 10), blue
point: (1, a)
text: 1, a, "$(1, a)$", center-right
xmin: -0.5
xmax: 6
ymin: -0.5
ymax: 6
fontsize: 28
:::
::::

:::::::::::::::



---


:::::::::::::::{example} Eksempel 1
Nedenfor vises noen eksempler på potensfunksjoner.


:::::{grid} 1 1 2 2
---
gutter: 2
---
::::{grid-item-card}
$$
f(x) = x^{3/2}
$$
^^^
:::{plot}
width: 100%
function: x**(3/2), (0, 6), f, blue
xmin: -0.5
ymin: -0.5
fontsize: 28
:::
::::


::::{grid-item-card}
$$
g(x) = x^{1/2}
$$
^^^
:::{plot}
width: 100%
function: x**(1/2), (0, 6), g, red
xmin: -0.5
ymin: -0.5
fontsize: 28
:::
::::

::::{grid-item-card}
$$
h(x) = x^{-2} = \frac{1}{x^2}
$$
^^^
:::{plot}
width: 100%
function: x**(-2), (0, 6), h, green
xmin: -0.5
ymin: -0.5
fontsize: 28
:::
::::


::::{grid-item-card}
$$
p(x) = x^{-1/2} = \frac{1}{x^{1/2}}
$$
^^^
:::{plot}
width: 100%
function: x**(-1/2), (0, 6), p, orange
xmin: -0.5
ymin: -0.5
fontsize: 28
:::
::::
:::::


:::::::::::::::



---


## Sammenheng mellom potensfunksjoner og røtter
Kvadratroten $\sqrt{x}$ av et tall $x$ er definert som det tallet som opphøyd i 2 gir $x$:

$$
\left(\sqrt{x}\right)^2 = x
$$

Samtidig vil 

$$
x^{1/2} \cdot x^{1/2} = x^{1/2 + 1/2} = x^1 = x
$$

Altså må 

$$
\sqrt{x} = x^{1/2}
$$

Mer generelt, kan vi definere $n$-te roten av $x$ som det tallet vi må opphøye i $n$ for å få $x$:

$$
\left(\sqrt[n]{x}\right)^n = x
$$

Av samme årsak får vi derfor at

$$
\underbrace{x^{1/n} \cdot x^{1/n} \cdot \ldots \cdot x^{1/n}}_{n\, \mathrm{ganger}} = x^{n \cdot 1/n} = x^1 = x
$$

Dermed må 

$$
x^{1/n} = \sqrt[n]{x}
$$


:::::::::::::::{summary} Sammenheng mellom potenser og $n$-røtter
$n$-te roten av $x$ kan skrives som en potens av $x$:

$$
\sqrt[n]{x} = x^{1/n}
$$

:::::::::::::::



<!-- 
## Modellering med potensfunksjoner
Det er mange praktiske situasjoner der det er naturlig å beskrive sammenhengen mellom to størrelser ved hjelp av en potensfunksjon. Her skal vi se på to strategier for å bestemme en potensmodell ut fra data.


### Bestemm potensmodell ved å bruke proporsjonalitet

### Bestemme potensmodell med regresjon -->

