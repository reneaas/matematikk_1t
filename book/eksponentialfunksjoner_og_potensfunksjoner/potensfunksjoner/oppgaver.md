# Oppgaver: Potensfunksjoner



:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk potensreglene til å skrive svaret som en potens med grunntall $2$.

$$
2^3 \cdot 2^4
$$

:::::::::::::

:::::::::::::{tab-item} b
Bruk potensreglene til å skrive svaret som en potens av grunntall $2$. 

$$
\dfrac{2^2}{2^{-2}}
$$


:::::::::::::


:::::::::::::{tab-item} c
Bruk potensreglene til å skrive svaret som en potens med grunntall $2$.

$$
(2^3)^4 \cdot 2^{-2}
$$

:::::::::::::


:::::::::::::{tab-item} d
Bruk potensreglene til å skrive svaret som en potens med grunntall $3$. 

$$
\dfrac{3^2 \cdot 3^{-4} }{9^{-2}}
$$

:::::::::::::


::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Ta quizen! 

:::{raw} html 
---
file: quiz/oppgaver/quiz_1/quiz_1.html
---
:::

:::::::::::::::


---

<!-- 
:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
Skriv om potensene til røtter.

::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
$$
x^{1/5}
$$

:::::::::::::


:::::::::::::{tab-item} b
$$
x^{-1/2}
$$

:::::::::::::


:::::::::::::{tab-item} c
$$
x^{2/3}
$$

:::::::::::::


:::::::::::::{tab-item} d
$$
x^{-3/4}
$$

:::::::::::::


::::::::::::::
::::::::::::::: -->


:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I {numref}`fig-potensfunksjoner-oppgave-3-a` vises grafene til funksjoner gitt ved

$$
f(x) = x^2 \quad\quad g(x) = \sqrt{x} \quad\quad h(x) = \dfrac{1}{x}
$$

Koble sammen riktig funksjon med riktig graf.

:::{figure} ./figurer/oppgaver/oppgave_3/a.svg
---
name: fig-potensfunksjoner-oppgave-3-a
width: 100%
class: no-click
---
viser grafene til tre funksjoner.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
* Graf A tilhører $f$.
* Graf B tilhører $h$.
* Graf C tilhører $g$.
::::


:::::::::::::


:::::::::::::{tab-item} b
I {numref}`fig-potensfunksjoner-oppgave-3-b` vises grafene til tre funksjoner gitt ved

$$
f(x) = x^{-1} \quad\quad g(x) = \dfrac{2}{x} \quad\quad h(x) = \dfrac{4}{x^2}
$$

Koble sammen riktig funksjon med riktig graf.

:::{figure} ./figurer/oppgaver/oppgave_3/b.svg
---
name: fig-potensfunksjoner-oppgave-3-b
width: 100%
class: no-click
---
viser grafene til tre funksjoner.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
* Graf A tilhører $h$.
* Graf B tilhører $f$.
* Graf C tilhører $g$.
::::

:::::::::::::


:::::::::::::{tab-item} c
I {numref}`fig-potensfunksjoner-oppgave-3-c` vises grafene til tre funksjoner gitt ved

$$
f(x) = x^{1/3} \quad\quad g(x) = 2 x^{1/2} \quad\quad h(x) = 2 x^{2/3}
$$

Koble sammen riktig funksjon med riktig graf.

:::{figure} ./figurer/oppgaver/oppgave_3/c.svg
---
name: fig-potensfunksjoner-oppgave-3-c
width: 100%
class: no-click
---
viser grafene til tre funksjoner.
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
* Graf A tilhører $f$.
* Graf B tilhører $h$.
* Graf C tilhører $g$.
::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-2
---
Adam har arvet $100 \, 000$ kr. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvis Adam setter pengene i banken og får en rente på $3 \%$ per år, hvor mye penger har han etter $10$ år?


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
100 \, 000 \cdot 1.03^{10} \approx 134 \, 392 \text{ kr}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Adam tenker å investere pengene i 10 år og vil undersøke hvor penger han kan få avhengig av renten. 

Lag en modell $f$ som viser sammenhengen mellom $f(x)$ kr som Adam vil ha om 10 år og vekstfaktoren $x$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 100 \, 000 \cdot x^{10}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Hvor mye penger vil Adam ha etter $10$ år dersom renten er $5 \%$ per år?


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(1.05) = 100 \, 000 \cdot 1.05^{10} \approx 162 \, 889 \text{ kr}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Hva må renta være for at Adam skal ha $200 000$ kr etter $10$ år?


> Du kan bruke Geogebra eller Python nedenfor som hjelpemiddel.

````{tab} Geogebra

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_4/cas_vindu.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---

Vi kan løse likningen 

$$
f(x) = 200 \, 000
$$

eller vi kan gå direkte på å bestemme renten $r$ ved å løse likningen 

$$
100 \, 000 \cdot (1 + r)^{10} = 200 \, 000
$$

Vi bruker den siste strategien med CAS som vi kan få til med:

:::{figure} ./ggb/oppgaver/oppgave_4/d_sol.png
---
width: 100%
class: no-click
---
:::

som betyr at renten må være omtrent $r = 0.07 = 7 \%$ for at Adam skal ha $200 \, 000$ kr etter $10$ år.

::::

````


````{tab} Python 

:::{raw} html
---
file: ./python/oppgaver/oppgave_4/kode.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
Vi kan løse likningen 

$$
f(x) = 200 \, 000
$$

eller vi kan gå direkte på å bestemme renten $r$ ved å løse likningen 

$$
100 \, 000 \cdot (1 + r)^{10} = 200 \, 000
$$

Vi bruker den siste strategien med CAS som vi kan få til med koden:

:::{code-block} python
---
linenos:
---
from casify import *

likning = nløs("100_000 * (1 + rente)**10 = 200_000")

print(likning)
:::

som gir utskriften

:::{code-block} console
rente = -2.072 ∨ rente = 0.072
:::

Vi finner altså at renten må være $r = 0.072 = 7.2 \%$ for at Adam skal ha $200 \, 000$ kr etter $10$ år.

:::::

````

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
Perioden til en planet er tiden det tar for en planet å gjennomføre et fullt omløp i banen sin rundt solen. 

:::{figure} ./figurer/eksempler/eksempel_3/planetbane.svg
---
width: 50%
class: no-click
---
:::

Nedenfor vises en tabell over periodene til noen av planetene i solsystemet og deres avstand til solen. Avstandene er gitt i astronomiske enheter (AU) som er avstanden fra solen til jorden.

| Planet | Avstand (AU) | Periode (år) |
|--------|:--------------:|:--------------:|
| Merkur | 0.39         | 0.24         |
| Venus  | 0.72         | 0.62         |
| Mars   | 1.52         | 1.88         |
| Jupiter| 5.20         | 11.86        |
| Saturn | 9.58         | 29.46        |

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell $P$ som gir perioden til en planet i $P(x)$ år når avstanden til solen er $x$ AU på formen

$$
P(x) = a \cdot x^b.
$$


:::::{admonition} Fasit
---
class: answer, dropdown
---

$$
P(x) \approx 1 \cdot x^{1.5}
$$

````{tab} Geogebra 

Bruker `RegPot` for å lage en potensfunksjon med regresjon:

:::{figure} ./ggb/oppgaver/oppgave_5/a_sol.png
---
width: 100%
class: no-click
---
:::

````


````{tab} Python


:::{code-block} python
---
linenos:
---
from casify import *

xdata = [0.39, 0.72, 1.52, 5.2, 9.58]
ydata = [0.24, 0.62, 1.88, 11.86, 29.46]
modell = "a * x ** b"

# Utfører regresjon
P = reg(
    modell=modell,
    xdata=xdata,
    ydata=ydata,
)

print(P)
::: 

:::{code-block} console
       1.49
1.015*x  
::: 

som gir:

$$
P(x) = 1.015 \cdot x^{1.49}
$$


````

:::::

:::::::::::::


:::::::::::::{tab-item} b
Regn ut perioden til en planet som er $1$ AU fra solen.

Er svaret rimelig? 

:::::{admonition} Fasit
---
class: answer, dropdown
---

````{tab} Geogebra
Vi regner ut $P(1)$ med modellen vi bestemte i **a**:

:::{figure} ./ggb/oppgaver/oppgave_5/b_sol.png
---
width: 100%
class: no-click
---
:::

som gir en periode på $P(1) \approx 1$ år som stemmer godt overens med at dette er perioden til jorda.

````


````{tab} Python 
Vi utvider programmet fra **a** med følgende kodelinje:

:::{code-block} python
print(P(1)) # Periode til planet 1 AU unna sola (aka jorda)
:::

som gir utskriften 

:::{code-block} console
1.01500000000000
:::

Som betyr at $P(1) \approx 1.015$ år som stemmer godt overens med jordens periode er $1$ år. 

````

:::::

:::::::::::::

:::::::::::::{tab-item} c
Uranus har en periode på $84.01$ år. 


Bruk modellen din til å anslå avstanden til Uranus og sammenlign med den virkelige avstanden på $19.22$ AU.


:::::{admonition} Fasit
---
class: answer, dropdown
---
Vi må løse likningen $P(x) = 84.01$ for $x$ for å bestemme perioden til Uranus. 

````{tab} Geogebra
Vi utvider CAS-vinduet med å løse likningen

:::{figure} ./ggb/oppgaver/oppgave_5/c_sol.png
---
width: 100%
class: no-click
---
:::

Ut ifra modellen vår er avstanden til Uranus $x \approx 19.2$ AU. I virkeligheten er den $19.22$ AU, så modellen gir en god tilnærming.

````

````{tab} Python 
Vi utvider programmet fra **a** og **b** for å løse likningen $P(x) = 84.01$:

:::{code-block} python
avstand_uranus = nløs("P(x) = 84.01")
print(avstand_uranus)
:::

som gir utskriften

:::{code-block} console
x = 19.371
:::

som betyr at avstanden ifølge modellen vår er $x \approx 19.37$ AU som stemmer godt overens med den virkelige avstanden på $19.22$ AU.

````
:::::

:::::::::::::
::::::::::::::

> Du kan bruke Geogebra eller Python nedenfor for å løse oppgavene.

````{tab} Geogebra 

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_5/oppgave_5.html
---
:::

````

````{tab} Python 

:::{raw} html
---
file: ./python/oppgaver/oppgave_5/oppgave_5.html
---
:::

````


:::::::::::::::




:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-3
---
Kokepunktet til vann varierer med lufttrykket. Lufttrykket på sin side varierer med høyden over havet. I tabellen nedenfor vises kokepunktet til vann ved ulike høyder over havet.

| Lufttrykk (hPa) | Kokepunkt (°C) |
|-----------------|----------------|
| 1000            | 100            |
| 800             | 92.3           |
| 600             | 84.9           |
| 500             | 81.4           |
| 100             | 48.9           |



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

Bestem en modell $f$ på formen 

$$
f(x) = a \cdot x^b
$$

som gir kokepunktet til vann i $f(x)$ $^\circ \mathrm{C}$ ved et lufttrykk på $x$ hPa.

:::{raw} html
---
file: ./python/oppgaver/oppgave_6/a.html
---
:::

:::::::::::::


:::::::::::::{tab-item} b
Lufttrykket synker med ca. $12 \%$ per km i høyden. 

Bestem en modell $g$ som gir lufttrykket $g(x)$ hPa ved en høyde på $x$ km over havnivået.

:::::::::::::

:::::::::::::{tab-item} c
Bestem hvor langt over bakken lufttrykket er $300$ hPa.

:::::::::::::


:::::::::::::{tab-item} d
Bestem hvor langt over bakken kokepunktet til vann er $30 ^\circ \mathrm{C}$.

:::::::::::::


:::::::::::::{tab-item} e
Bruk modellen fra **a** og **b** og lag en modell $K$ som gir kokepunktet $K(x)$ $^\circ \mathrm{C}$ ved $x$ km over havnivået.

:::::::::::::


::::::::::::::




:::::::::::::::


