# Oppgaver: Eksponentialfunksjoner

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Ta quizen! Flere svaralternativer kan være riktig.


:::{raw} html
---
file: ./quiz/oppgaver/quiz_1/quiz_1.html
---
:::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Ta quizen!


:::{raw} html
---
file: ./quiz/oppgaver/quiz_2/quiz_2.html
---
:::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem vekstfaktoren til en økning på $40 \%$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
V = 1.4
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem vekstfaktoren til en nedgang på $15 \%$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
V = 0.85
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem vekstfaktoren til en økning på $18 \%$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
V = 1.18
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem vekstfaktoren til en nedgang på $12 \%$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
V = 0.88
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
Bestem den prosentvise endringen for hver vekstfaktor. 
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
V = 1.22
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
p = 22 \%
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
V = 0.93
$$ 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
p = -7 \%
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
V = 0.4
$$ 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
p = -60 \%
$$
::::

:::::::::::::


:::::::::::::{tab-item} d

$$
V = 1.45
$$ 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
p = 45 \%
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-1
---
En eksponentialfunksjon $f$ er gitt ved 

$$
f(x) = 2 \cdot 3^x. 
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f(0)$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(0) = 2.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $f(4)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(4) = 162.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bruk CAS til å løse likningen 

$$
f(x) = 1000.
$$

````{tab} Geogebra

Nedenfor vises et CAS-vindu som løser likningen $f(x) = 50$. Gjør nødvendige endringer og løs likningen din. 

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_5/c.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**CAS-vindu med løsning**:

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_5/c_solution.html
---
:::

<br>

**Løsning**:

$$
f(x) = 1000 \liff x \approx 5.66. 
$$

::::

````


````{tab} Python 

Nedenfor vises et eksempel på løsningen til likningen $f(x) = 50$ i Python. Endre på programmet slik at det løser riktig likning.

:::{raw} html
---
file: ./python/oppgaver/oppgave_5/c.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode:**

:::{code-block} python
---
linenos: 
---
from casify import *

f = funksjon("2 * 3 ** x")

løsning = nløs("f(x) = 1000")

print(løsning)
:::

**Utskrift**:

:::{code-block} console
x = 5.657
:::

**Løsning**:

Løsningen er $x \approx 5.657$.

::::

````

:::::::::::::



::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
Anna kjøper en bil og anslår at verdien til bilen de neste årene kan beskrives av funksjonen

$$
f(x) = 200000 \cdot 0.85^x.
$$

der $f(x)$ kr er verdien til bilen $x$ år etter hun kjøpte den.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor mye er bilen til Anna verdt nå? 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(0) = 200000.
$$

Bilen til Anna er verdt $200000$ kr nå.
::::

:::::::::::::


:::::::::::::{tab-item} b
Hvor mye anslår Anna at bilens verdi vil synke med per år? 

::::{admonition} Fasit
---
class: answer, dropdown
---
Bilens verdi vil synke med $15 \%$ per år.
::::


:::::::::::::


:::::::::::::{tab-item} c
Regn ut verdien til bilen etter $5$ år.


````{tab} Geogebra

<br>

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_6/c.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
**CAS-vindu med løsning**:

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_6/c_solution.html
---
:::

<br>

**Svar**:

Bilen koster ca. $88741$ kr etter $5$ år.
::::

````


````{tab} Python

<br>

:::{raw} html
---
file: ./python/oppgaver/oppgave_6/c.html
---
:::

<br>

::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

:::{code-block} python
---
linenos:
---
from casify import *

f = funksjon("200_000 * 0.85 ** x")

verdi = f(5)
print(verdi)
:::

**Utskrift**:
:::{code-block} console
88741.0625000000
:::

**Svar:**

Bilen koster ca. $88741$ kr etter $5$ år.
::::

````

:::::::::::::


:::::::::::::{tab-item} d
Bestem hvor mange år det tar før verdien til bilen er halvert.


````{tab} Geogebra

<br>

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_6/d.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**CAS-vindu med løsning**:

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_6/d_solution.html
---
:::

<br>

**Svar**:

Det tar litt over $4$ år før verdien til bilen er halvert.
::::

````


````{tab} Python

<br>

:::{raw} html
---
file: ./python/oppgaver/oppgave_6/d.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

:::{code-block} python
---
linenos:
---
from casify import *

f = funksjon("200_000 * 0.85 ** x")

løsning = nløs("f(x) = 100_000")

print(løsning)
:::

**Utskrift**:
:::{code-block} console
x = 4.265
:::

**Svar**:

Det tar litt over $4$ år før verdien til bilen er halvert.
::::

````


:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---
Du setter inn $1000 \, \text{kr}$ på en bankkonto som gir en rente på $3 \%$ per år.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell $f$ for sparebeløpet $f(x)$ kr etter $x$ år.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 1000 \cdot 1.03^x. 
$$
::::


:::::::::::::

:::::::::::::{tab-item} b
Bestem hvor lang tid det tar før sparebeløpet er dobbelt så stort som det opprinnelige beløpet.


````{tab} Geogebra

<br>

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_7/b.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
**CAS-vindu med løsning**

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_7/b_solution.html
---
:::

<br>

Det tar ca. 24 år før sparebeløpet er dobbelt så stort som det opprinnelige beløpet.
::::


````


````{tab} Python 

<br>

:::{raw} html
---
file: ./python/oppgaver/oppgave_7/b.html
---
:::

<br>

::::{admonition} Fasit
---
class: answer, dropdown
---

**Programkode**:

:::{code-block} python
---
linenos:
---
from casify import *

f = funksjon("1000 * 1.03 ** x")

løsning = nløs("f(x) = 2000")

print(løsning)
:::

**Utskrift**:
:::{code-block} console
x = 23.45
:::

Det tar ca. 24 år før sparebeløpet er dobbelt så stort som det opprinnelige beløpet.
::::

````

:::::::::::::

:::::::::::::{tab-item} c
Nedenfor vises et program som skal regne ut sparebeløpet etter $10$ år ved å bruke følgende algoritme: 

1. Sett `sparebeløp = 1000`{l=python}.
2. Øk `sparebeløp`{l=python} med renten hvert år så lenge antall år er mindre enn $10$. 


Skriv ferdig programmet og bruk det til å regne ut sparebeløpet etter $10$ år.

:::{raw} html
---
file: ./python/oppgaver/oppgave_7/c.html
---
:::

:::::::::::::

:::::::::::::{tab-item} d
Nå skal du sette inn $1000 \, \mathrm{kr}$ hvert år på kontoen. For å regne ut sparebeløpet ditt hvert år, kan du bruke følgende strategi:

1. Legg til renten først,
2. Legg til innskuddet. 

Gjenta dette hvert år.

Fullfør programmet nedenfor og bruk det til å bestemme hvor mange år det tar å spare opp $100 000 \, \mathrm{kr}$.

:::{raw} html
---
file: ./python/oppgaver/oppgave_7/d.html
---
:::

:::::::::::::

::::::::::::::


:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 8 
---
class: problem-level-2
---
Kristin jobber som biolog og studerer veksten av en bakteriekultur i et laboratorium. Hun har målt antall bakterier ved forskjellige tidspunkter og mener antallet bakterier følger en eksponentiell vekst. Hun har samlet inn dataen i tabellen nedenfor.

| Tid (timer) | Antall bakterier |
|-------------|------------------|
| 0           | 100              |
| 1           | 150              |
| 2           | 225              |
| 3           | 337              |
| 4           | 506              |


<br>

:::::::::::::{tab-set}
---
class: tabs-parts
---

::::::::::::{tab-item} a
Bruk opplysningene i tabellen ovenfor til å lage en eksponentiell modell $f$ som gir $f(x)$ bakterier etter $x$ timer.


::::{admonition} Fasit
---
class: answer, dropdown
---


````{tab} Geogebra

**Svar**:

$$
f(x) = 100.01 \cdot 1.5^x
$$


**CAS-vindu med løsning**:

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_8/a_solution.html
---
:::

> Du kan fint bare bruke `Reg`-kommandoen, men da er det ikke like lett å få lest av hva vekstfaktoren er. Du kan jo prøve å se hva som skjer!

````

````{tab} Python 

**Svar**:

$$
f(x) = 99.965 \cdot 1.5^x
$$

**Programkode**:

:::{code-block} python
---
linenos:
---
from casify import *

xdata = [0, 1, 2, 3, 4]
ydata = [100, 150, 225, 337, 506] 
modell = "a * b ** x" 

f = reg(
    modell=modell,
    xdata=xdata,
    ydata=ydata,
)

print(f) # Skriv ut funksjonsuttrykket
:::

**Utskrift**:
:::{code-block} console
          x
99.965*1.5 
:::

````
::::

::::::::::::


::::::::::::{tab-item} b
Bruk modellen til å anslå hvor mange bakterier det er etter $24$ timer.

:::::{admonition} Fasit
---
class: answer, dropdown
---

````{tab} Geogebra

**Svar**:
1 673 625 bakterier.


**CAS-vindu med løsning**:

:::{raw} html
---
file: ./ggb/oppgaver/oppgave_8/b_solution.html
---
:::


````

````{tab} Python 
**Svar**: 

1 682 822 bakterier.

**Programkode**:
Vi må utvide programmet fra oppgave **a** med følgende linje:

:::{code-block} python
print(f(24)) # antall bakterier etter 24 timer
::: 

**Utskrift**:

:::{code-block} console
1682822.02567596
:::

````
:::::


::::::::::::

::::::::::::{tab-item} c
Bruk modellen til å anslå hvor lang tid det tar før det er 10 millioner bakterier i kulturen.

:::::{admonition} Fasit
---
class: answer, dropdown
---

````{tab} Geogebra

**Svar**:

Litt over 28 timer. 


**CAS-vindu med løsning**:
:::{raw} html
---
file: ./ggb/oppgaver/oppgave_8/c_solution.html
---
:::

````

````{tab} Python 

**Svar**:

Litt over 28 timer.

**Programkode**:
Vi utvider det forrige programmet fra **a** og **b** med disse kodelinjene:

:::{code-block} python
løsning = nløs("f(x) = 10_000_000")

print(løsning)
:::

**Utskrift**:

:::{code-block} console
x = 28.395
:::


````

:::::


::::::::::::





:::::::::::::

> I denne oppgaven trenger du digitale hjelpemidler for å løse oppgaven. Velg mellom Geogebra eller Python.

````{tab} Geogebra

<br>

:::{raw} html 
---
file: ./ggb/oppgaver/oppgave_8/oppgave_8.html
---
:::

````


````{tab} Python 

<br>

:::{raw} html 
---
file: ./python/oppgaver/oppgave_8/oppgave_8.html
---
:::

````



:::::::::::::::










