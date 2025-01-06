# Oppgaver: Gjennomsnittlig vekstfart


:::::::::::::::{admonition} Oppsummering
---
class: summary
---
::::::::::::::{tab-set}
:::::::::::::{tab-item} Gjennomsnittlig vekstfart
Den **gjennomsnittlige vekstfarten** til en funksjon $f$ i intervallet $[x_1, x_2]$ er definert som stigningstallet til en rett linje som går gjennom punktene $(x_1, f(x_1))$ og $(x_2, f(x_2))$ på grafen til $f$.

:::{figure} ./figurer/teori/formel2.svg
---
width: 60%
class: no-click
---
:::

Linjen som går gjennom de to punktene kaller vi for en **sekant**. Se {numref}`fig-teori-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-sekanter`.

:::{figure} ./koder/animasjoner/gjennomsnittig_vekstfart/media/videos/gjennomsnittlig_vekstfart/1440p60/gjennomsnittlig_vekstfart.gif
---
name: fig-teori-andregradsfunksjoner-vekstfart-gjennomsnittlig-vekstfart-sekanter
width: 100%
class: no-click
---
viser grafen til en andregradsfunksjon (blå) og en sekant (rød) som går gjennom to punkter $(x_1, f(x_1))$ og $(x_2, f(x_2))$ og den tilsvarende formelen for gjennomsnittlig vekstfart i intervallet $[x_1, x_2]$.
:::
:::::::::::::

:::::::::::::{tab-item} Ettpunktsformelen
En linje med stigningstall $a$ som går gjennom punktet $(x_1, y_1)$ kan skrives på formen

$$
y - y_1 = a(x - x_1).
$$

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem den gjennomsnittlige vekstfarten til $f$ i intervallet $[0, 3]$. 

:::{figure} ./figurer/oppgaver/oppgave_1/a.svg
---
width: 80%
class: no-click
---
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
\dfrac{f(3) - f(0)}{3 - 0} = 1
$$
:::

:::::::::::::

:::::::::::::{tab-item} b
Bestem den gjennomsnittlige vekstfarten til $g$ i intervallet $[-4, 0]$.

:::{figure} ./figurer/oppgaver/oppgave_1/b.svg
---
width: 80%
class: no-click
---
:::


:::{admonition} Fasit
---
class: dropdown, answer
---
$$
\dfrac{g(0) - g(-4)}{0 - (-4)} = 0
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
Bestem den gjennomsnittlige vekstfarten til $h$ i intervallet $[-3, 1]$.

:::{figure} ./figurer/oppgaver/oppgave_1/c.svg
---
width: 80%
class: no-click
---
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
\dfrac{h(1) - h(-3)}{1 - (-3)} = - \dfrac{3}{2}
$$
:::
:::::::::::::

:::::::::::::{tab-item} d
Bestem den gjennomsnittlige vekstfarten til $p$ i intervallet $[-1, 2]$. 

:::{figure} ./figurer/oppgaver/oppgave_1/d.svg
---
width: 80%
class: no-click
---
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
\dfrac{p(2) - p(-1)}{2 - (-1)} = 1
$$
:::
:::::::::::::
::::::::::::::
:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem den gjennomsnittlige vekstfarten til $f$ i intervallet $[1, 4]$.

$$
f(x) = x^2 + 3x - 2
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\dfrac{\Delta f(x)}{\Delta x} = 8
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
Bestem den gjennomsnittlige vekstfarten til $g$ i intervallet $[-1, 1]$.

$$
g(x) = -x^2 + 4
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\dfrac{\Delta g(x)}{\Delta x} = 0
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
Bestem den gjennomsnittlige vekstfarten til $h$ i intervallet $[-1, 1]$.

$$
h(x) = -(x + 1)(x + 2)
$$


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\dfrac{\Delta h(x)}{\Delta x} = -3
$$
:::

:::::::::::::


:::::::::::::{tab-item} d
Bestem den gjennomsnittlige vekstfarten til $p$ i intervallet $[-2, 0]$.

$$
p(x) = (x - 2)^2 - 3
$$


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\dfrac{\Delta p(x)}{\Delta x} = -6
$$
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
En andregradsfunksjon er gitt ved 

$$
f(x) = (x + 2)^2 - 1.
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem den gjennomsnittlige vekstfarten til $f$ i intervallet $[-2, 1]$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\dfrac{\Delta f(x)}{\Delta x} = 3
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
Bestem stigningstallet til sekanten som går gjennom punktene $(-2, f(-2))$ og $(1, f(1))$.

:::{admonition} Fasit
---
class: answer, dropdown
---
Stigningstallet til sekanten er det samme som den gjennomsnittlig vekstfarten til $f$ i intervallet $[-2, 1]$. Dermed er stigningstallet 

$$
a = 3
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
Bestem likningen for sekanten. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 3x + 5.
$$
:::
:::::::::::::


::::::::::::::


:::::::::::::::


:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-2
---


::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::{tab-item} a
Bestem likningen for sekanten gjennom punktene $(1, f(1))$ og $(3, f(3))$ på grafen til

$$
f(x) = x^2 - 2x + 1.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 2x - 2
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi regner ut stigningstallet til sekanten: 

$$
a = \dfrac{f(3) - f(1)}{3 - 1} 
$$

der funksjonsverdiene er 

\begin{align*}
    f(1) &= 1^2 - 2 \cdot 1 + 1 = 0 \\
    \\
    f(3) &= 3^2 - 2 \cdot 3 + 1 = 4
\end{align*}

Dermed er stigningstallet

$$
a = \dfrac{f(3) - f(1)}{2} = \dfrac{4 - 0}{2} = 2.
$$

Så bruker vi ettpunktsformelen med ett av punktene. Vi velger $(1, f(1)) = (1, 0)$ som gir

\begin{align*}
y - y_1 &= a(x - x_1) \\
\\
y - 0 &= 2(x - 1) \\
\\
y &= 2x - 2.
\end{align*}
::::
:::::::::::::

::::::::::::{tab-item} b
Bestem likningen for sekanten gjennom punktene $(-2, g(-2))$ og $(1, g(1))$ på grafen til

$$
g(x) = (x - 1)(x + 3)
$$


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = x - 1
$$
:::
:::::::::::::


::::::::::::{tab-item} c
Bestem likningen for sekanten gjennom punktene $(0, h(0))$ og $(2, h(2))$ på grafen til

$$
h(x) = -(x + 2)^2 + 3
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -6x - 1
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Stigningstallet til sekanten er gitt ved:

$$
a = \dfrac{h(2) - h(0)}{2 - 0}
$$

Vi regner ut funksjonsverdiene først:

\begin{align*}
    h(2) &= -(2 + 2)^2 + 3 = -4^2 + 3 = -16 + 3 = -13 \\
    \\
    h(0) &= -(0 + 2)^2 + 3 = -2^2 + 3 = -4 + 3 = -1
\end{align*}

Stigningstallet til sekanten blir derfor

\begin{align*}
    a = \dfrac{h(2) - h(0)}{2} = \dfrac{-13 + 1}{2} = \dfrac{-12}{2} = -6.
\end{align*}

Så bruker vi ettpunktsformelen med et av punktene. Velger $(0, h(0)) = (0, -1)$ som gir

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - (-1) &= -6(x - 0) \\
    \\
    y + 1 &= -6x \\
    \\
    y &= -6x - 1.
\end{align*}
::::
:::::::::::::

::::::::::::{tab-item} d
Bestem likningen for sekanten gjennom punktene $(-2, p(-2))$ og $(0, p(0))$ på grafen til

$$
p(x) = -x^2 + 16
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 2x + 16.
$$
:::
:::::::::::::

::::::::::::::

:::::::::::::::


:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
En andregradsfunksjon $f$ har følgende egenskaper:
* Nullpunkter i $x = 1$ og $x = 3$.
* Gjennomsnittlig vekstfart i intervallet $[-1, 1]$ er $-4$.

Bestem $f(x)$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = -(x - 1)(x - 3)
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi vet at nullpunktene til $f$ er $x = 1 \, \lor \, x = 3$ som betyr at vi kan skrive $f(x)$ på nullpunktsform:

$$
f(x) = a(x - 1)(x - 3).
$$

At den gjennomsnittlige vekstfarten i intervallet $[-1, 1]$ er $-4$ betyr at 

$$
\dfrac{f(1) - f(-1)}{1 - (-1)} = -4
$$

Vi setter inn $f(x)$ og regner ut:

\begin{align*}
    f(1) &= a(1 - 1)(1 - 3) = 0 \\
    \\
    f(-1) &= a(-1 - 1)(-1 - 3) = a\cdot (-2)\cdot (-4) = 8a
\end{align*}

Dermed vet vi at 

$$
\dfrac{8a}{2} = -4  \quad \iff \quad a = -1.
$$

Dermed er 

$$
f(x) = -(x - 1)(x - 3).
$$
::::
:::::::::::::

:::::::::::::{tab-item} b
En andregradsfunksjon $g$ har følgende egenskaper:
* Et bunnpunkt i $(2, 3)$. 
* Gjennomsnittlig vekstfart i intervallet $[1, 4]$ er $2$.

Bestem $g(x)$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
g(x) = 2(x - 2)^2 + 3
$$
:::
:::::::::::::


:::::::::::::{tab-item} c
En andregradsfunksjon $h$ har følgende egenskaper:
* Et nullpunkt i $x = -1$.
* Gjennomsnittlig vekstfart i intervallet $[-2, 6]$ er $0$.
* $h(x) \in [-6, \to\rangle$.

Bestem $h(x)$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
h(x) = \dfrac{2}{3}(x - 2)^2 - 6
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
At den gjennomsnittlige vekstfarten i intervallet $[-2, 6]$ er $0$ betyr at symmetrilinja til $h$ er midtpunktet i intervallet som gir 

$$
x_0 = \dfrac{-2 + 6}{2} = \dfrac{4}{2} = 2.
$$

At verdimengden til $h$ er $V_h = [-6, \to\rangle$ betyr at den *minste* verdien til $h(x)$ er $-6$. Dette må skje i ekstremalpunktet som betyr at 

$$
h(x) = a(x - 2)^2 - 6.
$$

Vi kan bruke at $x = -1$ er et nullpunkt for å bestemme $a$, som gir oss 

\begin{align*}
    h(-1) &= a(-1 - 2)^2 - 6 = 0 \\
    \\
    0 &= a\cdot (-3)^2 - 6 \\
    \\
    0 &= 9a - 6 \\
    \\
    6 &= 9a \\
    \\
    \dfrac{6}{9} &= a \\
    \\
    \dfrac{2}{3} &= a
\end{align*}


Altså er 

$$
h(x) = \dfrac{2}{3}(x - 2)^2 - 6.
$$
::::
:::::::::::::

:::::::::::::{tab-item} d
En andregradsfunksjon $p$ har følgende egenskaper:
* Symmetrilinje i $x = -1$.
* Gjennomsnittlig vekstfart i intervallet $[0, 2]$ er $-2$.
* Et nullpunkt i $x = 2$.

Bestem $p(x)$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
p(x) = -\dfrac{1}{2}(x + 1)^2 + \dfrac{9}{2}
$$
:::
:::::::::::::
::::::::::::::


:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-3
---
Lova syns ikke $abc$-formelen var så grei å bruke for å finne nullpunkter, så hun har lest seg opp på en annen strategi der hun kan bruke sekanter for å finne nullpunktene til en andregradsfunksjon.

Hun har laget en animasjon for å illustrere strategien sin. 

::::{video} ./koder/animasjoner/media/videos/sekantmetoden/1440p60/sekantmetoden.mp4
---
width: 95%
---
::::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Se på animasjonen og forklar strategien til Lova.
Hva vil skje hvis hun gjentar strategien mange ganger? 


::::{admonition} Fasit
---
class: answer, dropdown
---
Lova starter med to punkter $x_1$ og $x_2$. Deretter regner hun ut en sekant gjennom $(x_1, f(x_1))$ og $(x_2, f(x_2))$. 
Hun finner nullpunktet til sekanten som hun kaller for $x_3$. Deretter lager hun en ny sekant ved å bruke $x_2$ og $x_3$. Så finner hun nullpunktet til denne sekanten som hun kaller for $x_4$. Dette gjentar hun flere ganger. 

Hvis hun gjentar dette mange ganger, vil hun få en $x_n$ for et stort tall $n$ som vil være *veldig* nærme et av nullpunktene til andregradsfunksjonen.


::::

:::::::::::::

:::::::::::::{tab-item} b
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 4
$$

Bruk strategien til Lova i to steg til å regne ut $x_3$ og $x_4$. Start med $x_1 = 1$ og $x_2 = 5$.

Kommer du nærme ett av nullpunktene til $f$?

::::{admonition} Fasit
---
class: answer, dropdown
---
\begin{align*}
    x_3 &= \dfrac{3}{2} = 1.5 \\
    \\
    x_4 &= \dfrac{23}{13} \approx 1.77
\end{align*}
::::
:::::::::::::

:::::::::::::{tab-item} c
Lova ønsker seg en generell algoritme for å finne nullpunktene med strategien og har funnet at man trenger en formel for nullpunktet til en sekant som er skrevet med ettpunktsformelen 

$$
y - y_1 = a(x - x_1)
$$

der $a$ er stigningstallet til sekanten som går gjennom et punkt $(x_1, y_1)$.


Finn en formel for nullpunktet til sekanten. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x_\text{nullpunkt} = x_1 - \dfrac{y_1}{a}
$$
::::

:::::::::::::

:::::::::::::{tab-item} d
Under vises et interaktivt kodevindu som må fylles ut.

Fyll ut koden slik at det bruker strategien til Lova for å finne et av nullpunktene til $f(x) = x^2 - 4$. 


:::{raw} html
---
file: ./python/oppgaver/oppgave_6.html
---
:::


::::{admonition} Fasit
---
class: dropdown, answer
---

:::{code-block} python
---
linenos: true
---
def f(x):
    return x**2 - 4

x1 = 1
x2 = 5

antall_ganger = 10   # Hvor mange sekanter du skal lage sekanter
for n in range(antall_ganger):
    y1 = f(x1)
    y2 = f(x2)

    if x2 - x1 != 0: # Sjekk at vi ikke deler på null
        a = (y2 - y1) / (x2 - x1)
    else:
        break # Hvis x2 - x1 = 0, så stopper vi så vi ikke deler på null

    x_nullpunkt = x1 - y1 / a


    x1, x2 = x2, x_nullpunkt # Setter x1 = x2 og x2 = x_nullpunkt

print(x_nullpunkt) # Skriver ut nullpunktet til slutt
:::

::::
:::::::::::::
::::::::::::::


:::::::::::::::