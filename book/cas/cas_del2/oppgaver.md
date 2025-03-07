# CAS-kurs: Del 2


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne løse likninger, ulikheter og likningssystemer med CAS.
* Kunne jobbe med funksjoner i CAS til å finne funksjonsverdier, løse likninger, ulikheter, likningssystemer, bestemme den deriverte og anvende disse til å løse oppgaver.
:::::



````{tab} Geogebra
Hvis *jeg* er markert, jobber du med CAS i Geogebra.

````


````{tab} Python
Hvis *jeg* er markert, jobber du med CAS i Python.

````


## Likninger

Nedenfor vises et eksempel på hvordan man løser likninger med CAS. 

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---

````{tab} Geogebra
Nedenfor vises et CAS-vindu som løser likningen 

$$
x^2 - x - 6 = 0. 
$$


Vi gjør følgende:
1. Skriver inn likningen i **celle 1**.
2. Bruker `Løs`-kommandoen til å løse likningen i **celle 2**. Vi skriver `Løs($1)` der `$1` fyller inn likningen fra celle 1 for oss.

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/eksempel_1.html
---
:::

<br>

Fra utskriften i **celle 2** kan vi lese av at løsningen er 

$$
x = -2 \or x = 3.
$$


````


````{tab} Python 
Nedenfor vises et program som løser en likning. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør hvilken likning programmet løser.

Kjør programmet og bruk utskriften til å bestemme løsningen av likningen.

::::{admonition} Fasit
---
class: answer, dropdown
---
* Likning: $x^2 - x - 6 = 0$.
* Løsning: $x = -2 \or x = 3$. 
::::

:::::::::::::

:::::::::::::{tab-item} b
Endre på programmet og bruk det til å løse likningen 

$$
x^2 - 2x - 3 = 0.
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

:::{code-block} python
---
linenos: true
emphasize-lines: 3
---
from casify import *

løsning = løs("x**2 -2*x - 3 = 0")

print(løsning)
:::

**Utskrift**:

:::{code-block} console
x = -1 ∨ x = 3
:::

**Løsning**:

$$
x = -1 \or x = 3.
$$

::::


:::::::::::::

:::::::::::::{tab-item} c
Endre på programmet og bruk det til bestemme løsningen av likningen

$$
x^2 - 5x + 6 = x + 2.
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

:::{code-block} python
---
linenos: true
emphasize-lines: 3
---
from casify import *

løsning = løs("x**2 - 5*x + 6 = x + 2")

print(løsning)
:::

**Utskrift**:

:::{code-block} console
x = 3 - √5 ∨ x = √5 + 3
:::

**Løsning**:

$$
x = 3 - \sqrt{5} \or x = 3 + \sqrt{5}.
$$

::::

:::::::::::::

::::::::::::::

:::{raw} html
---
file: ./python/utforsk/utforsk_1/eksempel.html
---
:::

````


:::::::::::::::


---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---


````{tab} Geogebra
Bruk CAS-vinduet nedenfor til å løse likningene. 

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
x^2 - 3x - 4 = 0.
$$

:::{raw} html 
---
file: ./ggb/underveisoppgaver/underveisoppgave_1/a.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_1/a.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
x = -1 \or x = 4.
$$

::::


:::::::::::::


:::::::::::::{tab-item} b


$$
-x^2 + 9 = 0.
$$

:::{raw} html 
---
file: ./ggb/underveisoppgaver/underveisoppgave_1/b.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_1/b.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
x = -3 \or x = 3.
$$

::::

:::::::::::::


:::::::::::::{tab-item} c


$$
x^3 + 6x^2 - x - 30 = 0.
$$


:::{raw} html 
---
file: ./ggb/underveisoppgaver/underveisoppgave_1/c.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_1/c.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
x = -5 \or x = -3 \or x = 2.
$$

::::

:::::::::::::


:::::::::::::{tab-item} d

$$
x^3 + x^2 - 5x + 1 = -x + 5.
$$

:::{raw} html 
---
file: ./ggb/underveisoppgaver/underveisoppgave_1/d.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_1/d.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
x = -2 \or x = -1 \or x = 2.
$$

::::

:::::::::::::

::::::::::::::

````

````{tab} Python 

Skriv ferdig programmene nedenfor og bruk dem til å løse likningene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

$$
x^2 - 3x - 4 = 0.
$$

:::{raw} html 
---
file: ./python/underveisoppgaver/underveisoppgave_1/a.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**: 

:::{code-block} python
---
linenos: true
---
from casify import *

løsning = løs("x**2 - 3*x - 4 = 0")

print(løsning)
:::

**Utskrift**:

:::{code-block} console
x = -1 ∨ x = 4
:::

:::::

:::::::::::::

:::::::::::::{tab-item} b

$$
-x^2 + 9 = 0.
$$

:::{raw} html 
---
file: ./python/underveisoppgaver/underveisoppgave_1/b.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**: 

:::{code-block} python
---
linenos: true
---
from casify import *

løsning = løs("-x**2 + 9 = 0")

print(løsning)

:::

**Utskrift**:

:::{code-block} console
x = -3 ∨ x = 3
:::

:::::

:::::::::::::

:::::::::::::{tab-item} c

$$
x^3 + 6x^2 - x - 30 = 0.
$$


:::{raw} html 
---
file: ./python/underveisoppgaver/underveisoppgave_1/c.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**: 

:::{code-block} python
---
linenos: true
---
from casify import *

løsning = løs("x**3 + 6*x**2 - x - 30 = 0")

print(løsning)

:::

**Utskrift**:

:::{code-block} console
x = -5 ∨ x = -3 ∨ x = 2
:::

:::::

:::::::::::::


:::::::::::::{tab-item} d

$$
x^3 + x^2 - 5x + 1 = -x + 5.
$$

:::{raw} html 
---
file: ./python/underveisoppgaver/underveisoppgave_1/d.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**: 

:::{code-block} python
---
linenos: true
---
from casify import *

løsning = løs("x**3 + x**2 - 5*x + 1 = -x + 5")

print(løsning)

:::

**Utskrift**:

:::{code-block} console
x = -2 ∨ x = -1 ∨ x = 2
:::

:::::

:::::::::::::

::::::::::::::

````

:::::::::::::::



## Ulikheter

:::::::::::::::{admonition} Utforsk 2
---
class: explore
---


````{tab} Geogebra
Nedenfor vises et CAS-vindu som løser ulikheten

$$
x^3 - 2x^2 - 7x - 4 < 0.
$$


Vi gjør følgende:
1. Skriver inn ulikheten i **celle 1**. 
2. Bruker `Løs`-kommandoen til å løse ulikheten i **celle 2**. Vi skriver `Løs($1)` der `$1` fyller inn ulikheten fra celle 1 for oss.


:::{raw} html
---
file: ./ggb/utforsk/utforsk_2/eksempel_2.html
---
:::

<br>

Fra utskriften kan vi lese av at løsningen er 

$$
x < -1 \or -1 < x < 4.
$$

````


````{tab} Python

Nedenfor vises et program som løser en ulikhet.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Les programmet og avgjør hvilken ulikhet det løser. 

Bruk programmet til å bestemme løsningen av ulikheten. 
:::::::::::::

:::::::::::::{tab-item} b
Endre på programmet og bruk det til å løse ulikheten 

$$
x^2 - 4x - 5 \geq 0.
$$

> Hint: For å skrive $\geq$ i Python brukes `>=`{l=python}.

:::::::::::::

:::::::::::::{tab-item} c
Endre på programmet og bruk det til å løse ulikheten

$$
(x + 1)^2 > 0
$$

:::::::::::::

::::::::::::::

:::{raw} html
---
file: ./python/utforsk/utforsk_2/eksempel.html
---
:::


````
:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---

````{tab} Geogebra

Bruk CAS-vinduene nedenfor til å løse ulikhetene.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
(x - 1)(x + 4) \leq 0. 
$$

:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_2/a.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_2/a.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
-4 \leq x \leq 1. 
$$

::::

:::::::::::::


:::::::::::::{tab-item} b

$$
(x - 1)^2(x + 3) > 0. 
$$


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_2/b.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_2/b.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
-3 < x < 1 \or x > 1.
$$

::::

:::::::::::::


:::::::::::::{tab-item} c

$$
x^2 - 3x - 4 \geq 0.
$$


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_2/c.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_2/c.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
x \leq -1 \or x \geq 4
$$

::::

:::::::::::::


:::::::::::::{tab-item} d

$$
x^3 + x^2 - 4x - 4 \geq 0.
$$


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_2/d.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_2/d.png
---
width: 100%
class: no-click
---
:::

**Svar:**

$$
-2 \leq x \leq -1 \or x \geq 2
$$

::::

:::::::::::::

::::::::::::::




````


````{tab} Python

Fyll ut programmene nedenfor og bruk dem til å løse ulikhetene.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
(x - 1)(x + 4) \leq 0. 
$$

:::{raw} html
---
file: ./python/underveisoppgaver/underveisoppgave_2/a.html
---
:::

:::::::::::::


:::::::::::::{tab-item} b

$$
(x - 1)^2(x + 3) > 0. 
$$


:::{raw} html
---
file: ./python/underveisoppgaver/underveisoppgave_2/b.html
---
:::

:::::::::::::


:::::::::::::{tab-item} c

$$
x^2 - 3x - 4 \geq 0.
$$


:::{raw} html
---
file: ./python/underveisoppgaver/underveisoppgave_2/c.html
---
:::

:::::::::::::


:::::::::::::{tab-item} d

$$
x^3 + x^2 - 4x - 4 \geq 0.
$$


:::{raw} html
---
file: ./python/underveisoppgaver/underveisoppgave_2/d.html
---
:::

:::::::::::::

::::::::::::::


````

:::::::::::::::



## Likningssystemer


:::::::::::::::{admonition} Utforsk 3
---
class: explore
---


````{tab} Geogebra

Nedenfor vises et CAS-vindu som løser likningssystemet

\begin{align*}
    2x - y &= 1 \\
    -x^2 + 3x + y &= 3
\end{align*}


Vi gjør følgende:
1. Vi skriver inn likningene i **celle 1** og **celle 2**. 
2. Vi bruker `Løs`-kommandoen til å løse likningssystemet i **celle 3**. Vi skriver `Løs({$1, $2})` der `$1` og `$2` fyller inn likningene fra celle 1 og celle 2 for oss i en liste. **Merk** at vi lager en liste med `{}`-parenteser. 

:::{raw} html
---
file: ./ggb/utforsk/utforsk_3/eksempel_3.html
---
:::

<br>

Fra utskriften i **celle 3**, kan vi lese av at løsningen av likningssystemet er 

$$
x = 4 \lland y = 7 \or x = 1 \lland y = 1. 
$$

````


````{tab} Python 

Nedenfor vises et program som løser et likningssystem. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
1. Avgjør hvilket likningssystem som løses i programmet.
2. Bestem løsningen av likningssystemet ut ifra utskriften (*kjør programmet*).

:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet og bruk det til å løse likningssystemet

$$

$$

:::::::::::::


:::::::::::::{tab-item} c

:::::::::::::


:::::::::::::{tab-item} d

:::::::::::::

::::::::::::::


:::{raw} html
---
file: ./python/utforsk/utforsk_3/eksempel.html
---
:::


````


:::::::::::::::




---


:::::::::::::::{admonition} Underveisoppgave 3
---
class: check
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningssystemet

\begin{align*}
    3x + y &= 3 \\
    3x^2 - y^2 &= -9
\end{align*}



:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_3/a.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_3/a.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = 0 \lland y = 3 \or x = 3 \lland y = -6. 
$$


:::::


:::::::::::::


:::::::::::::{tab-item} b
Løs likningssystemet

\begin{align*}
    -2x^2 - 3x + y &= 2 \\
    x^2 + 4x - y &= -4
\end{align*}


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_3/b.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_3/b.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = 2 \lland y = 16 \or x = -1 \lland y = 1. 
$$


:::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningssystemet

\begin{align*}
    x - y &= 1 \\
    -x^2 + 4x + y &= 3
\end{align*}


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_3/c.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_3/c.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = 1 \lland y = 0 \or x = 4 \lland y = 3.
$$


:::::

:::::::::::::



:::::::::::::{tab-item} d
Løs likningssystemet

\begin{align*}
    2x - y &= 4 \\
    x^2 - 3x - 2y &= -4
\end{align*}


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_3/d.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_3/d.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = 4 \lland y = 4 \or x = 3 \lland y = 2.
$$


:::::

:::::::::::::

::::::::::::::

:::::::::::::::



## Funksjoner

:::::::::::::::{admonition} Utforsk 4
---
class: explore
---
Her skal vi se på hvordan vi kan jobbe med funksjoner i CAS.


::::::::::::::{tab-set}

:::::::::::::{tab-item} Funksjonsverdier
I CAS-vinduet nedenfor vises et eksempel på hvordan vi definerer en funksjon $f(x)$ og regner ut funksjonsverdier. 

* Vi definerer en funksjon ved å skrive `f(x) := x^2 - 2x - 3` i **celle 1**. Legg merke til at vi bruker `:=` når vi **definerer** en funksjon!
* I celle 2 - 4 regner vi ut funksjonsverdier med tall.
* I celle 5 regner vi ut funksjonsverdien med en variabel.

:::{raw} html
---
file: ./ggb/utforsk/utforsk_4/funksjonsverdier.html
---
:::


:::::::::::::


:::::::::::::{tab-item} Likninger og ulikheter
I CAS-vinduet nedenfor viser vi hvordan vi kan løse likninger og ulikheter med $f(x)$. 

* I **celle 2** løser vi $f(x) = 0$.
* I **celle 3** løser vi $f(x) \geq 0$.
* I **celle 4** løser vi $f(x) < 5$. 


:::{raw} html
---
file: ./ggb/utforsk/utforsk_4/likninger_ulikheter.html
---
:::

:::::::::::::


::::::::::::::


:::::::::::::::


:::::::::::::::{admonition} Underveisoppgave 4
---
class: check
---
En funksjon $f$ er gitt ved 

$$
f(x) = x^3 - 2x^2 - 7x - 4. 
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Definer en funksjon $f$ og regn ut funksjonsverdiene $f(0)$, $f(1)$, $f(-2)$ og $f(k)$.


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_4/a.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_4/a.png
---
width: 100%
class: no-click
---
:::

::::

:::::::::::::

:::::::::::::{tab-item} b
Løs likningen 

$$
f(x) = 0.
$$


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_4/b.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_4/b.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = -1 \or x = 4.
$$

::::




:::::::::::::

:::::::::::::{tab-item} c
Løs ulikheten 

$$
f(x) \geq 0. 
$$

:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_4/c.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_4/c.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = -1 \or x \geq 4.
$$

::::

:::::::::::::

::::::::::::::




:::::::::::::::


---


:::::::::::::::{admonition} Utforsk 5
---
class: explore
---
> Her skal vi se på hvordan vi kan bestemme $f(x)$ fra opplysninger om en funksjon $f$. 

En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = ax^3 + bx^2 + cx + d
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Grafen til $f$ går gjennom punktet $(2, -4)$. 

Sett opp én eller flere likninger som passer med opplysningen.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(2) = -4. 
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Punktet $(-1, -4)$ er et bunnpunkt på grafen til $f$. 

Sett opp én eller flere likninger som passer med opplysningen.

::::{admonition} Fasit
---
class: answer, dropdown
---
* $f(-1) = -4$ (fordi punktet ligger på grafen til $f$). 
* $f'(-1) = 0$ (fordi det er et bunnpunkt på grafen til $f$). 
::::

:::::::::::::


:::::::::::::{tab-item} c
Tangenten til grafen til $f$ i punktet $(0, f(0))$ har stigningstall $3$. 

Sett opp én eller flere likninger som passer med opplysningen.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f'(0) = 3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
I CAS-vinduet nedenfor er tredjegradsfunksjon $f$ definert og to av likningene er skrevet inn.

Fyll ut CAS-vinduet og bestem $a$, $b$, $c$ og $d$ ved å løse likningssystemet.



:::{admonition} Hva var likningene igjen?
---
class: hints, dropdown
---
* $f(2) = -4$
* $f(-1) = -4$
* $f'(-1) = 0$
* $f'(0) = 3$
:::

:::{raw} html
---
file: ./ggb/utforsk/utforsk_5/d.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./ggb/utforsk/utforsk_5/d.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
a = -1 \lland b = 0 \lland c = 3 \lland d = -2. 
$$

::::


:::::::::::::



:::::::::::::::


---


:::::::::::::::{admonition} Underveisoppgave 5
---
class: check
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = ax^3 + bx^2 + cx + d.
$$

Om $f$ får du vite at 
* Grafen til $f$ skjærer $x$-aksen i $x = 2$.
* Punktet $(-3, 0)$ er et toppunkt på grafen til $f$. 
* Tangenten til grafen til $f$ i punktet $(1, f(1))$ har stigningstall $8$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Sett opp likninger som passer med opplysningene om $f$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
Likningene blir

1. $f(2) = 0$.
2. $f(-3) = 0$.
3. $f'(-3) = 0$.
4. $f'(1) = 8$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$, $b$, $c$ og $d$. 


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_5/b.html
---
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_5/b.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = 1 \lland b = 4 \lland c = -3 \lland d = -18
$$

:::::

:::::::::::::

::::::::::::::



:::::::::::::::


---


:::::::::::::::{admonition} Utforsk 6
---
class: explore
---
> Her skal vi se på et eksempel der vi skal bruke CAS til å løse en optimeringsoppgave.

I {numref}`fig-cas-del-2-utforsk-6` vises grafen til en andregradsfunksjon $f$ som er gitt ved

$$
f(x) = -x^2 + 9,
$$

der $D_f = [0, 3]$, og en trekant som har hjørner i punktene $(0, 0)$, $(k, 0)$ og $(k, f(k))$.


:::{figure} ./figurer/utforsk/utforsk_6/figur.svg
---
name: fig-cas-del-2-utforsk-6
width: 80%
class: no-click
---
viser grafen til $f(x) = -x^2 + 9$ for $x \in [0, 3]$ og en trekant med hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet $A(k)$ til uttrykt ved $f(k)$ og $k$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(k) = \dfrac{k\cdot f(k)}{2}
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
Sett opp en likning som kan brukes til å bestemme den verdien av $k$ som gir størst mulig areal for trekanten.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
A'(k) = 0. 
$$
:::
:::::::::::::


:::::::::::::{tab-item} c
I CAS-vinduet nedenfor har vi definert $f(x)$ og $A(k)$. 

Fyll ut CAS-vinduet og bruk det til å bestemme den verdien av $k$ som gir størst mulig areal for trekanten.

:::{raw} html
---
file: ./ggb/utforsk/utforsk_6/c.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/utforsk/utforsk_6/c.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
k = \sqrt{3}
$$

::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Underveisoppgave 6
---
class: check
---
En fjerdegradsfunksjon $f$ er gitt ved 

$$
f(x) = -x(x - 3)^3, \quad D_f = [0, 3]. 
$$

En trekant har hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$. Se {numref}`fig-cas-del-2-underveisoppgave-6`.

Bestem den verdien av $k$ som gir størst mulig areal for trekanten.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_6/figur.svg
---
name: fig-cas-del-2-underveisoppgave-6
width: 80%
class: no-click
---
viser grafen til $f(x) = -x(x - 3)^3$ for $x \in [0, 3]$ og en trekant med hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$.
:::



:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_6/cas.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_6/solution.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
k = \dfrac{6}{5}
$$
:::::


:::::::::::::::




<!-- ## Algebra 

* Faktorisere polynomer. 
* Faktorisere og forkorte rasjonale funksjoner. 
* Utvide polynomer. 


## Polynomdivisjon

* Utføre polynomdivisjon.
* Lese av kvotient og rest.
* Bestemme asymptoter til rasjonale funksjoner. -->


## Oppgaver


:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = (x - 1)^2 - 9. 
$$

Løs oppgavene nedenfor med CAS.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Regn ut $f(-4)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_1/a.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
f(-4) = 16.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Finn nullpunktene til $f$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_1/b.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = -2 \or x = 4.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem ekstremalpunktet til $f$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_1/c.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = 1.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Løs ulikheten $f(x) > 0$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_1/d.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x < 2 \or x > 4.
$$
::::

:::::::::::::

::::::::::::::

<br>

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_1/cas.html
---
:::




:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 - 19x + 30. 
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_2/a.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = -5 \or x = 2 \or x = 3.
$$


::::

:::::::::::::


:::::::::::::{tab-item} b
Faktoriser $f(x)$. 

> Hint: Du kan bruke en funksjon i CAS som heter `Faktoriser(f)` til å faktorisere $f(x)$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_2/b.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
f(x) = (x - 2)(x - 3)(x + 5).
$$


::::

:::::::::::::


:::::::::::::{tab-item} c
Løs ulikheten $f(x) \leq 0$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_2/c.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x \leq -5 \or 2 \leq x \leq 3.
$$


::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem ekstremalpunktene til $f$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_2/d.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = -\dfrac{\sqrt{57}}{3} \or x = \dfrac{\sqrt{57}}{3}
$$


::::

:::::::::::::

::::::::::::::

<br>

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_2/cas.html
---
:::



:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-2
---
Et likningssystem er gitt ved 

$$
x^2 + y^2 = 25 \and x - y = 1. 
$$

I {numref}`fig-cas-kurs-del-2-likningssystem-oppgave-3` vises en grafisk representasjon av de to likningene. 

:::{figure} ./figurer/oppgaver/oppgave_3/likningssystem_figur.svg
---
name: fig-cas-kurs-del-2-likningssystem-oppgave-3
width: 80%
class: no-click
---
viser en grafisk representasjon av likningene $x^2 + y^2 = 25$ og $x - y = 1$.
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Bruk {numref}`fig-cas-kurs-del-2-likningssystem-oppgave-3` til å bestemme løsningen av likningssystemet.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \lland y = -4 \or x = 4 \lland y = 3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk innsettingsmetoden til å bestemme løsningen av likningssystemet. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \lland y = -4 \or x = 4 \lland y = 3.
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Likning 2 gir oss 

$$
x - y = 1 \liff y = x - 1.
$$

Vi setter inn dette uttrykket for $y$ i likning 1:

\begin{align*}
    x^2 + y^2 &= 25 \\
    \\
    x^2 + (x - 1)^2 &= 25 \\
    \\
    x^2 + x^2 - 2x + 1 &= 25 \\
    \\
    2x^2 - 2x - 24 &= 0 \\
    \\
    x^2 - x - 12 &= 0
\end{align*}

som gir 

$$
x = \dfrac{1 \pm \sqrt{1 + 4 \cdot 12}}{2} = \dfrac{1 \pm 7}{2}
$$

som betyr at 

$$
x = -3 \or x = 4.
$$


Kombinerer vi disse løsningene med $y = x - 1$, får vi:

$$
x = -3 \implies y = -3 - 1 = -4
$$

og 

$$
x = 4 \implies y = 4 - 1 = 3.
$$

Dermed er løsningene av likningssystemet gitt ved 

$$
x = -3 \lland y = -4 \or x = 4 \lland y = 3.
$$

::::


:::::::::::::


:::::::::::::{tab-item} c


````{tab} Geogebra
Bruk CAS-vindu nedenfor til å løse likningssystemet. 


:::{raw} html
---
file: ./ggb/oppgaver/oppgave_3/c.html
---
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_3/c.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
x = -3 \lland y = -4 \or x = 4 \lland y = 3.
$$

:::::



````


````{tab} Python

Bruk programmet under til å løse likningssystemet.

:::{raw} html
---
file: ./python/underveisoppgaver/underveisoppgave_4/c.html
---
:::

````

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-2
---
Om en tredjegradsfunksjon $f$ gitt ved 

$$
f(x) = ax^3 + bx^2 + cx + d
$$

får du vite at

* Grafen til $f$ går gjennom punktet $(2, 6)$. 
* Punktet $(-2, 8)$ er et toppunkt på grafen til $f$.
* Tangenten til grafen til $f$ i punktet $(3, f(3))$ har stigningstall $4$. 



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Sett opp et likningssystem som passer med opplysningene om $f$.

::::{admonition} Fasit
---
class: answer, dropdown
---
* $f(2) = 6$.
* $f(-2) = 8$.
* $f'(-2) = 0$.
* $f'(3) = 4$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk likningssystemet fra oppgave **a** til å bestemme koeffisientene $a$, $b$, $c$ og $d$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/oppgaver/oppgave_4/b.png
---
width: 100%
class: no-click
---
:::

**Svar**:

$$
a = \dfrac{3}{20} \lland b = \dfrac{7}{40} \lland c = -\dfrac{11}{10} \lland d = \dfrac{63}{10}
$$
::::

:::::::::::::

::::::::::::::

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_4/cas.html
---
:::


:::::::::::::::


