# CAS-kurs: Del 2


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne løse likninger, ulikheter og likningssystemer med CAS.
* Kunne løse ikke-lineære likningssystemer med CAS. 
* Kunne utføre polynomdivisjon med CAS.
* Kunne finne nullpunktene og ekstremalpunktene til en funksjon med CAS.
* Kunne finne den deriverte til en funksjon med CAS.
* Kunne bruke regresjon med CAS til å lage modeller.
:::::


> Som vanlig kan du velge mellom CAS i Geogebra og CAS i Python. Du kan fritt bytte læringsløp underveis om du ønsker det!


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
Nedenfor vises et CAS-vindu der vi løser en likning. 



::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
1. Hvilken likning løses i CAS-vinduet?
2. Hva er løsningen av likningen, ifølge utskriften? 


::::{admonition} Fasit
---
class: answer, dropdown
---
1. $x^2 - x - 6 = 0$.
2. $x = -2 \or x = 3$.
::::


:::::::::::::


:::::::::::::{tab-item} b
Endre på likningen i CAS-vinduet og bruk det til å løse 


$$
x^2 - 2x - 3 = 0. 
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \or x = 3.
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Endre på likningen i CAS-vinduet og bruk det til å løse 

$$
x^2 - 5x + 6 = x + 2. 
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 3 - \sqrt{5} \or x = 3 + \sqrt{5}.
$$
::::

:::::::::::::


::::::::::::::







:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/utforsk_1_cmd.html
---
:::


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
Nedenfor vises et CAS-vindu som løser en ulikhet. 


::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
1. Avgjør hvilken ulikhet som løses i CAS-vinduet.
2. Bestem løsningen av ulikheten ut ifra utskriften.


:::::::::::::


:::::::::::::{tab-item} b
Endre på ulikheten i CAS-vinduet og bruk det til å løse

$$
x^2 - 4x - 5 \geq 0.
$$

> Hint: For å skrive $\geq$ i Geogebra, skriver du $>$ etterfulgt av $=$

:::::::::::::


:::::::::::::{tab-item} c
Endre på ulikheten i CAS-vinduet og bruk det til å løse

$$
(x + 1)^2 > 0. 
$$


:::::::::::::

::::::::::::::





:::{raw} html
---
file: ./ggb/utforsk/utforsk_2/utforsk_2_cmd.html
---
:::

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

Nedenfor vises et CAS-vindu som løser et likningssystem.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
1. Avgjør hvilket likningssystem som løses i CAS-vinduet.
2. Bestem løsningen av likningssystemet ut ifra utskriften.


:::::::::::::


:::::::::::::{tab-item} b

:::::::::::::


:::::::::::::{tab-item} c

:::::::::::::


:::::::::::::{tab-item} d

:::::::::::::

::::::::::::::


:::{raw} html
---
file: ./ggb/utforsk/utforsk_3/utforsk_3_cmd.html
---
:::

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

---


:::::::::::::::{admonition} Underveisoppgave 4
---
class: check
---
Et likningssystem er gitt ved 

$$
x^2 + y^2 = 25 \and x - y = 1. 
$$

I {numref}`fig-cas-kurs-del-2-likningssystem-underveisoppgave-4` vises en grafisk representasjon av de to likningene. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4/likningssystem_figur.svg
---
name: fig-cas-kurs-del-2-likningssystem-underveisoppgave-4
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
Bruk {numref}`fig-cas-kurs-del-2-likningssystem-underveisoppgave-4` til å bestemme løsningen av likningssystemet.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \, \land \, y = -4 \or x = 4 \, \land \, y = 3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk innsettingsmetoden til å bestemme løsningen av likningssystemet. 


:::::::::::::


:::::::::::::{tab-item} c


````{tab} Geogebra
Bruk CAS-vindu nedenfor til å løse likningssystemet. 


:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_4/c.html
---
:::

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


## Algebra 

* Faktorisere polynomer. 
* Faktorisere og forkorte rasjonale funksjoner. 
* Utvide polynomer. 


## Polynomdivisjon

* Utføre polynomdivisjon.
* Lese av kvotient og rest.
* Bestemme asymptoter til rasjonale funksjoner.

## Funksjoner


* Regne ut funksjonsverdier

* Løse likninger med $f(x)$

* Bestemme $f'(x)$ og løser bestemme ekstremalpunkter


## Regresjon 

* Bruke CAS til å lage egendefinerte regresjonsmodeller






