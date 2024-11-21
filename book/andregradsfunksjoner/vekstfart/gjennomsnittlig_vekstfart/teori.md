# Gjennomsnittlig vekstfart

:::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare og regne ut gjennomsnittlig vekstfart.
* Kunne gi en praktisk tolkning av gjennomsnittlig vekstfart og knytte denne størrelsen til sekanter.
* Kunne bestemme likningen til en sekant. 
:::


Når vi jobbet med lineære funksjoner, hadde vi en veldefinert tolkning av stigningene til funksjonen – gjennom stigningstallet til en rett linje. Stigningstallet til en lineær funksjon $f$ forteller oss hvor mye 
funksjonsverdien $f(x)$ endrer seg når vi øker $x$ med én enhet. Dette er funksjonens **vekstfart**. 

::::{admonition} Repetisjon: stigningstallet til en lineær funksjon
---
class: reminder
---
Stigningstallet til en lineær funksjon som går gjennom to punkter $(x_1, y_1)$ og $(x_2, y_2)$ er gitt ved

$$
a = \dfrac{\Delta y}{\Delta x} = \dfrac{y_2 - y_1}{x_2 - x_1}
$$

:::{figure} ./figurer/teori/topunktsformelen.svg
---
width: 80%
class: no-click
---
:::

::::

For en andregradsfunksjon har ikke koeffisientene en slik betydning, men vi har likevel behov for å kunne beskrive hvor raskt funksjonsverdien endrer seg når vi endrer $x$. Én slik beskrivelse er **gjennomsnittlig vekstfart**. Gjennomsnittlig vekstfart er tett knyttet til stigningstallet til en lineær funksjon. 

:::::::::::::::{admonition} Gjennomsnittlig vekstfart
---
class: summary
---
Den **gjennomsnittlige vekstfarten** til en funksjon $f$ i intervallet $[a, b]$ er definert som

:::{figure} ./figurer/teori/formel.svg
---
width: 60%
class: no-click
---
:::
:::::::::::::::

---

:::::{admonition} Eksempel 1
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
\bar{v} = \dfrac{f(3) - f(1)}{3 - 1} = \dfrac{4 - 0}{3 - 1} = \dfrac{4}{2} = 2.
$$
::::
:::::

---

## Tolkning av gjennomsnittlig vekstfart

Gjennomsnittlig vekstfart gir oss hvor mye funksjonsverdien $f(x)$ endrer seg i **gjennomsnitt** når vi øker $x$ med én enhet i et intervall $[a, b]$. Vi kan knytte denne størrelsen til stigningstallet til en spesiell rett linje som vi kaller for en **sekant**. 

:::::{admonition} Gjennomsnittlig vekstfart og sekanter
---
class: summary
---
Den gjennomsnittlige vekstfarten til en funksjon $f$ i et intervall $[a, b]$ svarer til stigningstallet til en rett linje som går gjennom punktene $(a, f(a))$ og $(b, f(b))$ på grafen til $f$. 

Denne linjen kaller vi for en **sekant**. Se {numref}`fig-teori-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-sekanter`.

:::{figure} ./figurer/teori/gjennomsnittlig_vekstfart.svg
---
name: fig-teori-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-sekanter
class: no-click
width: 80%
---
viser grafen til en andregradsfunksjon $f$ og en sekant som går gjennom punktene $(a, f(a))$ og $(b, f(b))$. Den gjennomsnittlige vekstfarten til $f$ i intervallet $[a, b]$ er stigningstallet til sekanten.
:::


:::::

---

:::::{admonition} Eksempel 2
---
class: example
---
I {numref}`fig-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-eksempel-1` vises grafen til en andregradsfunksjon $f$ og en sekant $s$ som går gjennom to punkter på grafen til $f$.

1. Bestem hvilket intervall du kan bruke for å bestemme den gjennomsnittlige vekstfarten til $f$ ved hjelp av sekanten.
2. Finn den gjennomsnittlige vekstfarten til $f$ i intervallet.

:::{figure} ./figurer/eksempler/eksempel_1/graf.svg
---
name: fig-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-eksempel-1
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$ og en sekant $s$ som går gjennom to punkter på grafen til $f$. 
:::

::::{admonition} Løsning
---
class: solution
---
1. Sekanten $s$ går gjennom punktene $(-1, -3)$ og $(2, 3)$ på grafen til $f$. Vi kan derfor bruke sekanten til å bestemme den gjennomsnittlige vekstfarten til $f$ i intervallet $[-1, 2]$.

2. Den gjennomsnittlige vekstfarten svarer til stigningtallet til tangenten som gir

$$
\bar{v} = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{3 - (-3)}{2 - (-1)} = \dfrac{6}{3} = 2.
$$
::::

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
a = \dfrac{f(3) - f(1)}{3 - 1} = \dfrac{14 - 2}{3 - 1} = \dfrac{12}{2} = 6.
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



