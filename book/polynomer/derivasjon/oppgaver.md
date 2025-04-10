# Oppgaver: Den deriverte

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Deriver polynomfunksjonene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = x^2 - 3x + 2
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f'(x) = 2x - 3
$$
:::
:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = -x^3 + 4x + 1
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
g'(x) = -3x^2 + 4
$$
:::

:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = 2x^4 - 3x^2 + 1
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
h'(x) = 8x^3 - 6x
$$
:::

:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = 3x^5 - 2x^3 + 4x
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
p'(x) = 15x^4 - 6x^2 + 4
$$
:::

:::::::::::::
::::::::::::::

:::::::::::::::


::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
> I denne oppgaven skal du finne likningene til tangentene ved å bruke den deriverte og ettpunktsformelen.

::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::{tab-item} a
En polynomfunksjon er gitt ved 

$$
f(x) = -x^2 + 3x + 1
$$

Bestem likningen til tangenten i $(2, f(2))$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
y = -x + 5
$$
:::

:::::::::::


:::::::::::{tab-item} b
En polynomfunksjon er gitt ved 

$$
g(x) = 2x^3 - 3x^2 - 5x + 6
$$

Bestem likningen til tangenten i $(1, g(1))$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -5x + 5
$$
::::

:::::::::::

:::::::::::{tab-item} c
En polynomfunksjon er gitt ved 

$$
h(x) = 3x^4 - 2x^2 + 1
$$

Bestem likningen til tangenten i $(0, h(0))$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 1
$$
::::

:::::::::::


:::::::::::{tab-item} d
En polynomfunksjon er gitt ved 

$$
p(x) = 4x^5 - 3x^3 + 2x
$$

Bestem likningen til tangenten i $(-1, p(-1))$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 13x + 10.
$$
::::
:::::::::::


::::::::::::


:::::::::::::



::::::::::::::

:::::::::::::::

:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
> I denne oppgaven skal du bruke polynomdivisjon til å finne likningen til tangentene. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En polynomfunksjon er gitt ved 


$$
f(x) = -x^2 + 3x + 1
$$

Bruk polynomdivisjon til å bestemme likningen til tangenten i $(2, f(2))$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
y = -x + 5
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjonen $f(x) : (x - 2)^2$ og leser av resten siden dette gir likningen til tangenten i $(2, f(2))$. 
Vi bruker 2.kvadratsetning for å regne ut divisoren:

$$
(x - 2)^2 = x^2 - 4x + 4.
$$

Polynomdivisjonen blir da:

:::{figure} ./koder/oppgaver/oppgave_3/a.svg
---
width: 85%
class: no-click, adaptive-figure
---
:::

Vi kan se at resten er $-x + 5$ som gir likningen til tangenten:

$$
y = -x + 5.
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
En polynomfunksjon er gitt ved 

$$
g(x) = 2x^3 - 3x^2 - 5x + 6.
$$

Bruk polynomdivisjon til å bestemme likningen til tangenten i $(1, g(1))$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
y = -5x + 5
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjonen $g(x) : (x - 1)^2$ for å finne resten som gir likningen til tangenten i $(1, g(1))$.

Fra 2.kvadratsetning får vi divisoren som:

$$
(x - 1)^2 = x^2 - 2x + 1.
$$

Dermed blir polynomdivisjonen:

:::{figure} ./koder/oppgaver/oppgave_3/b.svg
---
width: 85%
class: no-click, adaptive-figure
---
:::

Vi kan lese av at resten er $-5x + 5$ som gir likningen til tangenten:

$$
y = -5x + 5.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En polynomfunksjon er gitt ved 

$$
h(x) = 3x^4 - 2x^2 + 1.
$$

Bruk polynomdivisjon til å bestemme likningen til tangenten i $(0, h(0))$.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
y = 1
$$
:::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjonen $h(x) : (x - 0)^2$ for å finne resten som gir likningen til tangenten i $(0, h(0))$.

Siden $(x - 0)^2 = x^2$, kan vi utføre polynomdivisjonen direkte:

:::{figure} ./koder/oppgaver/oppgave_3/c.svg
---
width: 85%
class: no-click, adaptive-figure
---
:::

Vi kan lese av at resten er $1$ som betyr at likningen til tangenten er 

$$
y = 1.
$$

::::
:::::::::::::

:::::::::::::{tab-item} d
En polynomfunksjon er gitt ved 

$$
p(x) = 4x^5 - 3x^3 + 2x.
$$

Bruk polynomdivisjon til å bestemme likningen til tangenten i $(-1, p(-1))$.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
y = 13x + 10.
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjonen $p(x) : (x + 1)^2$ for å finne resten som gir likningen til tangenten i $(-1, p(-1))$.

Vi bruker 1.kvadratsetning til å regne ut divisoren:

$$
(x + 1)^2 = x^2 + 2x + 1.
$$

Så utfører vi polynomdivisjonen:

:::{figure} ./koder/oppgaver/oppgave_3/d.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi leser av at resten er $13x + 10$ som gir likningen til tangenten:

$$
y = 13x + 10.
$$
::::
:::::::::::::


::::::::::::::
:::::::::::::::


---

:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-4-a` viser grafen til en andregradsfunksjon $f$.

Bruk grafen til å tegne fortegnslinja til $f'(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_4/a.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_4/a_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-a-løsning
width: 100%
class: no-click, adaptive-figure
---
viser fortegnslinja til $f'(x)$.
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-4-b` viser grafen til en tredjegradsfunksjon $g$.

Bruk grafen til å tegne fortegnslinja til $g'(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_4/b.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $g$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_4/b_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-b-løsning
width: 100%
class: no-click, adaptive-figure
---
viser fortegnslinja til $g'(x)$.
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-4-c` viser grafen til en tredjegradsfunksjon $h$.

Bruk grafen til å tegne fortegnslinja til $h'(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_4/c.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $h$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_4/c_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-c-løsning
width: 100%
class: no-click, adaptive-figure
---
viser fortegnslinja til $h'(x)$.
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-4-d` viser grafen til en fjerdegradsfunksjon $p$.

Bruk grafen til å tegne fortegnslinja til $p'(x)$. 

:::{figure} ./figurer/oppgaver/oppgave_4/d.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-d
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en fjerdegradsfunksjon $p$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_4/d_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-4-d-løsning
width: 100%
class: no-click, adaptive-figure
---
viser fortegnslinja til $p'(x)$.
:::
::::

:::::::::::::


::::::::::::::
:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-5-a` viser grafen til en andregradsfunksjon $f$.

Lag en skisse av grafen til $f'$.


:::{figure} ./figurer/oppgaver/oppgave_5/a.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_5/a_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-a-løsning
width: 80%
class: no-click, adaptive-figure
---
viser grafen til den deriverte $f'$. 
:::
::::



:::::::::::::


:::::::::::::{tab-item} b
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-5-b` viser grafen til en tredjegradsfunksjon $g$.

Lag en skisse av grafen til $g'$.


:::{figure} ./figurer/oppgaver/oppgave_5/b.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $g$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_5/b_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-b-løsning
width: 80%
class: no-click, adaptive-figure
---
viser grafen til den deriverte $g'$. 
:::
::::

:::::::::::::


:::::::::::::{tab-item} c

{numref}`fig-polynomfunksjoner-derivasjon-oppgave-5-c` viser grafen til en tredjegradsfunksjon $h$.

Lag en skisse av grafen til $h'$.


:::{figure} ./figurer/oppgaver/oppgave_5/c.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $h$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_5/c_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-c-løsning
width: 80%
class: no-click, adaptive-figure
---
viser grafen til den deriverte $h'$. 
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-5-d` viser grafen til en fjerdegradsfunksjon $p$.

Lag en skisse av grafen til $p'$.


:::{figure} ./figurer/oppgaver/oppgave_5/d.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-d
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en fjerdegradsfunksjon $p$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_5/d_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-5-d-løsning
width: 80%
class: no-click, adaptive-figure
---
viser grafen til den deriverte $p'$. 
:::
::::

:::::::::::::


::::::::::::::


:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-6-a` viser grafen til en lineær funksjon $f'$.

Lag en skisse av grafen til $f$. 

:::{figure} ./figurer/oppgaver/oppgave_6/a.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-a
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f'$.
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_6/a_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-a-løsning
width: 80%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $f$.
:::

::::



:::::::::::::

:::::::::::::{tab-item} b
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-6-b` viser grafen til en andregradsfunksjon $g'$. 

Lag en skisse av grafen til $g$. 

:::{figure} ./figurer/oppgaver/oppgave_6/b.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-b
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $g'$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_6/b_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-b-løsning
width: 80%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $g$.
:::

::::

:::::::::::::


:::::::::::::{tab-item} c
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-6-c` viser grafen til en andregradsfunksjon $h'$. 

Lag en skisse av grafen til $h$. 

:::{figure} ./figurer/oppgaver/oppgave_6/c.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-c
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $h'$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_6/c_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-c-løsning
width: 80%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $h$.
:::

::::



:::::::::::::


:::::::::::::{tab-item} d
{numref}`fig-polynomfunksjoner-derivasjon-oppgave-6-d` viser grafen til en tredjegradsfunksjon $p'$. 

Lag en skisse av grafen til $p$. 

:::{figure} ./figurer/oppgaver/oppgave_6/d.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-d
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $p'$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgaver/oppgave_6/d_løsning.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-6-d-løsning
width: 80%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $p$.
:::

::::

:::::::::::::

::::::::::::::

:::::::::::::::




:::::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---

{numref}`fig-polynomfunksjoner-derivasjon-oppgave-7` viser grafen til en andregradsfunksjon $f$ og to tangenter. Om tangentene får du vite at:
* Tangentene går gjennom nullpunktene til $f$.
* Den ene tangenten har likningen $y = 4x + 4$.
* Den andre tangenten skjærer $y$-aksen i $(0, 12)$.
* Grafen til $f$ skjærer $y$-aksen i $(0, 3)$. 


Bestem $f(x)$ og $f'(x)$.

:::{figure} ./figurer/oppgaver/oppgave_7/graf.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-7
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$ og to tangenter. Den ene tangenten har likningen $y = 4x + 4$ og den andre tangenten skjærer $y$-aksen i $(0, 12)$. 
:::


:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = -x^2 + 2x + 3 \quad \text{og} \quad f'(x) = -2x + 2.
$$
:::



:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 8
---
class: problem-level-2
---

{numref}`fig-polynomfunksjoner-derivasjon-oppgave-8` viser grafen til en andregradsfunksjon $f'$.


:::{figure} ./figurer/oppgaver/oppgave_8/graf.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-8
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f'$.  
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f'(x)$. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f'(x) = (x + 1)^2 - 4
$$
:::
:::::::::::::


:::::::::::::{tab-item} b
Grafen til $f$ har et nullpunkt i $x = 1$. 

Bestem $f(x)$. 


:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = \dfrac{1}{3}x^3 + x^2 - 3x + \dfrac{5}{3}
$$
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 9
---
class: problem-level-3
---

{numref}`fig-polynomfunksjoner-derivasjon-oppgave-9` viser grafen til en andregradsfunksjon $f'$. Tangenten gjennom toppunktet til $f'$ har likningen $y = 4$. 

:::{figure} ./figurer/oppgaver/oppgave_9/graf.svg
---
name: fig-polynomfunksjoner-derivasjon-oppgave-9
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f'$. 
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f'(x)$.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f'(x) = -\dfrac{4}{9}(x + 2)(x - 4)
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
En tangent som går gjennom $(0, f(0))$ har likningen $y = 3x - 2$.

Bestem $f(x)$. 


:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = -\dfrac{1}{3}x^3 + x^2 + 3x - 2.
$$
:::

:::::::::::::

::::::::::::::


:::::::::::::::



