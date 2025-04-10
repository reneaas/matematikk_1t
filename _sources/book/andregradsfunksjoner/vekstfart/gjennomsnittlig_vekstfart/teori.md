# Gjennomsnittlig vekstfart

:::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare og regne ut gjennomsnittlig vekstfart.
* Kunne gi en praktisk tolkning av gjennomsnittlig vekstfart og knytte denne størrelsen til sekanter.
* Kunne bestemme likningen til en sekant. 
:::


Når vi jobbet med lineære funksjoner, hadde vi en tydelig måte å tolke hvor mye $f(x)$ endrer seg når vi endrer på $x$ – gjennom stigningstallet til en rett linje. 

::::{admonition} Repetisjon: stigningstallet til en lineær funksjon
---
class: reminder
---
Stigningstallet til en lineær funksjon $f$ som går gjennom to punkter $(x_1, y_1)$ og $(x_2, y_2)$ er gitt ved

$$
a = \dfrac{\Delta y}{\Delta x} = \dfrac{y_2 - y_1}{x_2 - x_1}
$$

Dette tallet forteller oss hvor mye $f(x)$ endrer seg når vi øker $x$ med 1.

:::{figure} ./figurer/teori/topunktsformelen.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

For en andregradsfunksjon har ikke koeffisientene en slik betydning, men funksjonsverdien til en andregradsfunksjon endrer seg jo opplagt når vi endrer på verdien til $x$. 

For å kunne sette tall på slike endringer, kan vi finne på en ny størrelse som gir oss informasjon om hvor mye funksjonsverdien endrer seg når vi endrer på $x$. Én slik størrelse er **gjennomsnittlig vekstfart**. Denne størrelsen tar (skamløst) direkte inspirasjon fra stigningstallet til en rett linje:


:::::::::::::::{admonition} Gjennomsnittlig vekstfart
---
class: summary
---
Den **gjennomsnittlige vekstfarten** til en funksjon $f$ i intervallet $[x_1, x_2]$ er definert som stigningstallet til en rett linje som går gjennom punktene $(x_1, f(x_1))$ og $(x_2, f(x_2))$ på grafen til $f$.

:::{figure} ./figurer/teori/formel2.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

Linjen som går gjennom de to punktene kaller vi for en **sekant**. Se {numref}`fig-teori-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-sekanter`.

:::{figure} ./koder/animasjoner/gjennomsnittig_vekstfart/media/videos/gjennomsnittlig_vekstfart/1440p60/gjennomsnittlig_vekstfart.gif
---
name: fig-teori-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-sekanter
width: 100%
class: no-click, manim-figure
---
viser grafen til en andregradsfunksjon (blå) og en sekant (rød) som går gjennom to punkter $(x_1, f(x_1))$ og $(x_2, f(x_2))$ og den tilsvarende formelen for gjennomsnittlig vekstfart i intervallet $[x_1, x_2]$.
:::

:::::::::::::::

---

:::::{admonition} Eksempel 1
---
class: example
---
I {numref}`fig-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-eksempel-1` vises grafen til en andregradsfunksjon $f$ og en sekant $s$ som går gjennom punktene $(-1, f(-1))$ og $(2, f(2))$ på grafen til $f$.

Bruk sekanten til å bestemme den gjennomsnittlige vekstfarten til $f$ i intervallet $[-1, 2]$.

:::{figure} ./figurer/eksempler/eksempel_1/graf.svg
---
name: fig-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-eksempel-1
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$ og en sekant $s$ som går gjennom to punkter på grafen til $f$. 
:::

::::{admonition} Løsning
---
class: solution
---

Den gjennomsnittlige vekstfarten til $f$ i intervallet $[-1, 2]$ svarer til stigningtallet til sekanten siden denne linja går gjennom punktene $(-1, f(-1))$ og $(2, f(2))$:

$$
\dfrac{\Delta f(x)}{\Delta x} = \dfrac{f(2) - f(-1)}{2 - (-1)} = \dfrac{3 - (-3)}{2 - (-1)} = \dfrac{6}{3} = 2.
$$
::::

:::::

---


:::::{admonition} Eksempel 2
---
class: example
---
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 2x + 1.
$$

Bestem den gjennomsnittlige vekstfarten i intervallet $[1, 3]$. 



::::{admonition} Løsning
---
class: solution
---
Intervallet er $[a, b] = [1, 3]$. Vi regner ut funksjonsverdiene i de to endepunktene på intervallet:

\begin{align*}
    f(1) &= 1^2 - 2\cdot 1 + 1 = 0, \\
    \\
    f(3) &= 3^2 - 2\cdot 3 + 1 = 4.
\end{align*}

Så bruker vi definisjonen av gjennomsnittlig vekstfart: 

$$
\dfrac{\Delta f(x)}{\Delta x} = \dfrac{f(3) - f(1)}{3 - 1} = \dfrac{4 - 0}{3 - 1} = \dfrac{4}{2} = 2.
$$
::::
:::::

---

:::::{admonition} Underveisoppgave 1
---
class: check
---
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = -x^2 + 3x - 4
$$

Bestem den gjennomsnittlige vekstfarten i intervallet $[-2, 3]$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\dfrac{\Delta f(x)}{\Delta x} = 2
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
Den gjennomsnittlige vekstfarten i intervallet $[-2, 3]$ er gitt ved 

$$
\dfrac{\Delta f(x)}{\Delta x} = \dfrac{f(3) - f(-2)}{3 - (-2)} = \dfrac{f(3) - f(-2)}{5}
$$

Vi regner ut funksjonsverdiene:

\begin{align*}
    f(3) &= -3^2 + 3\cdot 3 - 4 = -9 + 9 - 4 = -4, \\
    \\
    f(-2) &= -(-2)^2 + 3\cdot (-2) - 4 = -4 - 6 - 4 = -14.
\end{align*}

som gir 

$$
\dfrac{\Delta f(x)}{\Delta x} = \dfrac{f(3) - f(-2)}{5} = \dfrac{-4 - (-14)}{5} = \dfrac{10}{5} = 2.
$$
:::
:::::

---

## Likningen til en sekant

:::::{admonition} Repetisjon: ettpunktsformelen
---
class: reminder
---
En rett linje med stigningstall $a$ som går gjennom punktet $(x_1, y_1)$ har likningen

$$
y - y_1 = a(x - x_1)
$$
:::::

---

:::::{admonition} Eksempel 3
---
class: example
---
En rett linje går gjennom punktene $(1, f(1))$ og $(3, f(3))$ på en andregradsfunksjon gitt ved 

$$
f(x) = (x + 1)^2 - 2.
$$

Bestem likningen til linja. 

::::{admonition} Løsning
---
class: solution
---
Den rette linja har samme stigningstall som den gjennomsnittlige vekstfarten til $f$ i intervallet $[1, 3]$. 

Vi har at 

\begin{align*}
    f(1) &= (1 + 1)^2 - 2 = 2, \\
    \\
    f(3) &= (3 + 1)^2 - 2 = 14.
\end{align*}

Den gjennomsnittlige vekstfarten – som svarer til stigningdstallet til den rette linja – er gitt ved 

$$
a = \dfrac{\Delta f(x)}{\Delta x} = \dfrac{f(3) - f(1)}{3 - 1} = \dfrac{14 - 2}{3 - 1} = \dfrac{12}{2} = 6.
$$

Vi bruker ettpunktsformelen med punktet $(1, 2)$ for å finne likningen til linja:

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - 2 &= 6(x - 1) \\
    \\
    y &= 6x - 4.
\end{align*}
::::
:::::

---

:::::{admonition} Underveisoppgave 2
---
class: check
---
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = x^2 - 2x - 3.
$$

Bestem likningen for sekanten som går gjennom $(-1, f(-1))$ og $(2, f(2))$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -x - 1.
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
Sekanten går gjennom punktene $(-1, f(-1))$ og $(2, f(2))$ som gir stigningstallet 

$$
a = \dfrac{\Delta f(x)}{\Delta x} = \dfrac{f(2) - f(-1)}{2 - (-1)} = \dfrac{f(2) - f(-1)}{3}
$$

Vi regner ut funksjonsverdiene:

\begin{align*}
    f(2) &= 2^2 - 2\cdot 2 - 3 = -3, \\
    \\
    f(-1) &= (-1)^2 - 2\cdot (-1) - 3 = 0.
\end{align*}

Dermed har sekanten stigningstallet 

$$
a = \dfrac{f(2) - f(-1)}{3} = \dfrac{-3 - 0}{3} = -1.
$$

Vi bruker ettpunktsformelen for å bestemme likningen med punktet $(-1, f(-1)) = (-1, 0)$:

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - 0 &= -1(x - (-1)) \\
    \\
    y &= -(x + 1) \\
    \\
    y &= -x - 1.
\end{align*}


::::
:::::



