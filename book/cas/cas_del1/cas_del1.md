# CAS-kurs: del 1

:::{admonition} Læringsmål: CAS-kurs del 1
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Kunne løse lineære likninger med CAS.
* Kunne løse lineære likningssystemer med CAS.
* Kunne løse lineære ulikheter med CAS.

:::

---

CAS er en forkortelse for *Computer Algebra System*. CAS består av en samling funksjoner som er utviklet for å løse matematiske problemer symbolsk (algebraisk) på datamaskin på liknende vis som vi gjør når vi regner for hånd. Kan et problem løses for hånd, kan det også løses med CAS.

Det finnes mange utgaver av CAS i det store Univers, så her skal du få velge sti selv. Du kan velge mellom å:
* Lære CAS i Geogebra
* Lære CAS i Python

Klikk på en av fanene under for å velge sti (du kan alltids bytte underveis!). 

````{tab} Geogebra
Hvis *jeg* er markert, vil du jobbe med CAS i **Geogebra**.
````

````{tab} Python
Hvis *jeg* er markert, vil du jobbe med CAS i **Python**.
````

---

## Likninger med CAS

::::::::::::{admonition} Utforsk 1: likninger med CAS
---
class: explore
name: cas-del-1-utforsk-1
---
````{tab} Geogebra

Å løse likninger i CAS kan gjøres enten ved å bruke `Løs`{l=console}-funksjoner (`Solve`{l=console} på engelsk) eller ved å trykke på <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen.

:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} a
Under vises et *interaktivt* CAS-vindu der en lineær likning er løst med de to måtene.

Hvilken likning er det som løses i vinduet?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
2x + 3 = -x - 3
$$
:::
::::

::::{tab-item} b
Bruk CAS-vinduet til å løse likningen 

$$
3x + 5 = -2x + 7
$$

::::
:::::

:::::{tab-set}
::::{tab-item} Med `Løs`{l=console}-funksjonen
**Oppskrift**: <br>
1. Skriv inn likningen i CAS-vinduet.
2. Bruk `Løs`{l=console}-funksjonen for å løse likningen.

:::{raw} html
---
file: ggb/utforsk/utforsk_1_cmd.html
---
:::

::::

::::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>
**Oppskrift**: <br>
1. Skriv inn likningen i CAS-vinduet.
2. Trykk på <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen for å løse likningen.

:::{raw} html
---
file: ggb/utforsk/utforsk_1_click_interface.html
---
:::
::::
:::::


````

````{tab} Python
For å bruke CAS i Python til å løse likninger, må vi skrive disse to kodelinjene på starten av programmet:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x
```

* Linje 1 henter alle funksjonene fra `sympy`{l=python}-biblioteket som lar oss utføre matematiske utregninger som å løse likninger, lage likninger og mye mer.
* Linje 2 henter en **symbolsk** (algebraisk) variabel som lar oss lage likninger med ukjente variabler.

---

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a
For å løse en likning med Python, må vi først **lage** en likning som en variabel i Python. 

Under vises tre eksempler på dette. For hvert av programmene:

* Les og programmet.
* Bestem hvilken likning programmet lager basert på utskriften.

> Linje 4 i kodeeksemplene betyr: `likning = Eq(venstre_side, høyre_side)`{l=python}. 

:::::{tab-set}
::::{tab-item} Eksempel 1
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/a/eksempel_1.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
2*x + 4 = 0
```

**Likning**:

$$
2x + 4 = 0
$$
:::

::::

::::{tab-item} Eksempel 2
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/a/eksempel_2.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
2*x + 5 = 8
```

**Likning**:

$$
2x + 5 = 8
$$
:::

::::

::::{tab-item} Eksempel 3
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/a/eksempel_3.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
x            
- - 6 = 2 - x
2        
```

**Likning**:

$$
\dfrac{x}{2} - 6 = 2 - x
$$
:::

::::

:::::

:::{admonition} `pprint`{l=python} og ikke `print`{l=python} – hva skjer?
---
class: sidenote, dropdown
---
`pprint`{l=python} kommer fra `sympy`{l=python}-biblioteket. Det er en forkortelse for *pretty* `print`{l=python} og brukes for å skrive ut matematiske uttrykk i `sympy`{l=python} som likner på hvordan vi ville skrevet det for hånd. Prøv å bytt ut `pprint`{l=python} med `print`{l=python} for å se forskjellen.
:::

---

:::{admonition} Oppsummering: `Eq`{l=python}-funksjonen
---
class: summary, dropdown
---
`Eq`{l=python}-funksjonen står for *Equation* som betyr *likning* på engelsk.
For å lage en likning bruker vi `Eq`{l=python}-funksjonen på følgende måte:

```{code-block} python
likning = Eq(venstre_side, høyre_side)
```

For eksempel for likningen 

$$
5x + 2 = -3x + 7
$$ 

skriver vi

```{code-block} python
likning = Eq(5 * x + 2, -3 * x + 7)
```
:::

::::::


::::::{tab-item} b

Når man skal løse en likning med `sympy`{l=python}, bruker vi `solve`{l=python}-funksjonen.

Under vises tre eksempler på dette. 

Kjør koden for hvert eksempel og bestem løsningen til likningen ved hjelp av utskriften.

:::::{tab-set}
::::{tab-item} Eksempel 1
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/b/eksempel_1.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:
    
```console
[-2]
```

**Løsning av likningen**:

$$
x = -2
$$
:::
::::

::::{tab-item} Eksempel 2
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/b/eksempel_2.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
[3/2]
```

**Løsning av likningen**:

$$
x = \dfrac{3}{2}
$$
:::

::::

::::{tab-item} Eksempel 3
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/b/eksempel_3.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
[16/3]
```

**Løsning av likningen**:

$$
x = \dfrac{16}{3}
$$
:::
::::

::::::

::::::{tab-item} c
Fyll inn programmet under og løs likningene.

:::::{tab-set}
::::{tab-item} Likning 1 
$$
3x + 2 = 0
$$

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/c/oppgave_1.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(3 * x + 2, 0)

løsning = solve(likning)

print(løsning)
```

**Utskrift**:
    
```console
[-2/3]
```

**Løsning**:

$$
x = -\dfrac{2}{3}
$$
:::

::::

::::{tab-item} Likning 2
$$
4x + 2 = 7
$$

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/c/oppgave_2.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(4 * x + 2, 7)

løsning = solve(likning)

print(løsning)
```

**Utskrift**:
    
```console
[5/4]
```

**Løsning**:

$$
x = \dfrac{5}{4}
$$
:::

::::

::::{tab-item} Likning 3
$$
3x - 2 = -5x + 1
$$

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/c/oppgave_3.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4
---
from sympy import *
from sympy.abc import x

likning = Eq(3 * x - 2, -5 * x + 1)

løsning = solve(likning)

print(løsning)
```

**Utskrift**:
    
```console
[3/8]
```

**Løsning**:

$$
x = \dfrac{3}{8}
$$
:::

::::

::::::


````


:::::::

::::::::::::

---

::::::::::::{admonition} Underveisoppgave 1
---
class: check
---

````{tab} Geogebra

Løs følgende likninger med CAS-vinduet under.  

* $2x + 3 = 7$
* $3x - 5 = 2x + 1$
* $\dfrac{3}{2}x - 3 = 2x + 5$

Bruk både `Løs`{l=console}-funksjonen og <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen til å løse likningene.

:::{raw} html
---
file: ggb/underveisoppgaver/oppgaver/underveisoppgave_1_tomt_cas_vindu.html
---
:::

:::::{admonition} Løsning
---
class: solution, dropdown
---
::::{tab-set}
:::{tab-item} Med `Løs`{l=console}-funksjonen
Legg merke til at vi kan skrive likningen direkte inn i `Løs`{l=console}-funksjonen også (se celle 5).
```{raw} html 
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_1_cmd_solve.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
```{raw} html
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_1_gui_solve.html
---
```
:::
::::
:::::

````

````{tab} Python
Sjekk forståelsen din her! 

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a

Ta quizen! 

:::{raw} html
---
file: quiz/quiz_1/quiz_1.html
---
:::

::::::

::::::{tab-item} b

Bruk programmet under til å løse likningene. 

:::::{tab-set}
::::{tab-item} Oppgave 1
$$
3x + 1 = 0
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_1/oppgave_1.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

likning = Eq(3 * x + 1, 0)
løsning = solve(likning)

print(løsning)
```
**Utskrift**:

```console
[-1/3]
```
**Løsning**:

$$
x = -\dfrac{1}{3}
$$
:::

::::

::::{tab-item} Oppgave 2
$$
-2x + 3 = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_1/oppgave_2.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
Programkode:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

likning = Eq(-2 * x + 3, 1)
løsning = solve(likning)

print(løsning)
```

Utskrift:

```console
[1]
```

Løsning:

$$
x = 1
$$
:::

::::

::::{tab-item} Oppgave 3
$$
x + 2 = -4x + 5
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_1/oppgave_3.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

likning = Eq(x + 2, -4 * x + 5)
løsning = solve(likning)

print(løsning)
```

**Utskrift**:

```console
[3/5]
```

**Løsning**:

$$
x = \dfrac{3}{5}
$$
:::

::::
:::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_1.html
---
:::

::::::

:::::::
````

::::::::::::

---


## Likningssystemer med CAS

::::::::::{admonition} Utforsk 2: likningssystemer med CAS
---
class: explore
---

````{tab} Geogebra
Vi kan også løse likningssystemer med både `Løs`{l=console}-funksjonen og <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen i CAS.

Under vises et *interaktivt* CAS-vindu der et likningssystem er løst på to forskjellige måter. 

::::{tab-set}
:::{tab-item} Med `Løs`{l=console}-funksjonen
**Oppskrift**: <br>

1. Skriv inn hver likning i hver sin celle. 
2. Bruk `Løs`{l=console}-funksjonen for å løse likningssystemet. <br> Legg merke til at likningene og variablene plasseres i hver sin liste `{}`{l=python}.

```{raw} html
---
file: ggb/utforsk/utforsk_2_cmd.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
**Oppskrift**: <br>

1. Skriv inn hver likning i hver sin celle. 
2. Marker likningene (dra musepekeren over cellenumrene - ikke bare trykk på cellene). 
3. Trykk på <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen for å løse likningssystemet.

```{raw} html
---
file: ggb/utforsk/utforsk_2_gui.html
---
```
:::
::::


Deloppgave 1
: Hvilket likningssystem er løst i CAS-vinduet? <br> Kan du lese av løsningen som er funnet?


Deloppgave 2
: Bruk CAS-vinduene til å løse likningssystemet
    \begin{align*}
    2x + y & = 5 \label{1a} \quad\quad\quad \tag{1a} \\
    x - y & = 1 \label{1b} \quad\quad\quad \tag{1b} 
    \end{align*}

````

````{tab} Python

Vi kan også bruke `solve`{l=python}-funksjonen i `sympy`{l=python} til å løse likningssystemer. Men siden vi har mer enn én variabel, må vi nå hente alle variablene vi trenger fra `sympy.abc`{l=python}. 

For et likningssystem med to variabler $x$ og $y$, skriver vi dette på toppen av programmet:

```{code-block} python
from sympy import *
from sympy.abc import x, y  # Henter en symbolsk variabel for x og y
```

---

::::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a

For å bruke `sympy`{l=python} til å løse likningssystemer, må vi først lage likningene som variabler og plassere dem i en liste.

Under vises tre eksempler på dette. 

Kjør koden for hvert eksempel og bestem hvilket likningssystem hvert program representerer.

:::::{tab-set}
::::{tab-item} Eksempel 1
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/eksempel_1.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x + y = 2 \quad \land \quad x - y = 0
$$
:::

::::

::::{tab-item} Eksempel 2
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/eksempel_2.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x + 3y = -7 \quad \land \quad 3x - 2y = 12
$$
:::
::::

::::{tab-item} Eksempel 3
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/eksempel_3.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
-x + 2y = 5 \quad \land \quad 3x + y = -2
$$
:::
::::


::::::

::::::{tab-item} b
Når vi har laget et likningssystem, bruker vi `solve`{l=python}-funksjonen til å løse likningssystemet akkurat som vi gjorde med likninger!

Her ser vi på tre eksempler på dette. 

Kjør koden for hvert eksempel og bestem løsningen til likningssystemet ved hjelp av utskriften.

:::::{tab-set}
::::{tab-item} Eksempel 1
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b/eksempel_1.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
{x: 1, y: 1}
```

**Løsning av likningssystemet**:

$$
x = 1 \quad \land \quad y = 1
$$
:::

::::

::::{tab-item} Eksempel 2
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b/eksempel_2.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
{x: 2, y: -3}
```

**Løsning av likningssystemet**:

$$
x = 2 \quad \land \quad y = -3
$$
:::
::::

::::{tab-item} Eksempel 3
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b/eksempel_3.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**:

```console
{x: -9/7, y: 13/7}
```

**Løsning av likningssystemet**:

$$
x = -\dfrac{9}{7} \quad \land \quad y = \dfrac{13}{7}
$$
:::
::::



::::::

::::::{tab-item} c
Fyll inn programmet under og bruk programmet til å løse likningssystemene.

:::::{tab-set}
::::{tab-item} Oppgave 1

$$
x + 2y = 10 \quad \land \quad 3x - 2y = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/c/oppgave_1.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(x + 2 * y, 10)
likning2 = Eq(3 * x - 2 * y, 1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:

```console
{x: 11/4, y: 29/8}
```

**Løsning**:

$$
x = \dfrac{11}{4} \quad \land \quad y = \dfrac{29}{8}
$$
:::

::::

::::{tab-item} Oppgave 2

$$
-2x + y = 1 \quad \land \quad 3x + 7y = -1
$$

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/c/oppgave_2.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(-2 * x + y, 1)
likning2 = Eq(3 * x + 7 * y, -1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:

```console
{x: -8/17, y: 1/17}
```

**Løsning**:

$$
x = -\dfrac{8}{17} \quad \land \quad y = \dfrac{1}{17}
$$
:::

::::

::::{tab-item} Oppgave 3

$$
2x - 5y = 3 \quad \land \quad 3x + 2y = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/c/oppgave_3.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(2 * x - 5 * y, 3)
likning2 = Eq(3 * x + 2 * y, 1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:

```console
{x: 11/19, y: -7/19}
```

**Løsning**:

$$
x = \dfrac{11}{19} \quad \land \quad y = -\dfrac{7}{19}
$$
:::

::::

::::::

::::::::


````

::::::::::

---

::::::::::{admonition} Underveisoppgave 2
---
class: check
---

````{tab} Geogebra

Løs følgende likningssystemer med CAS vinduet under:

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
\begin{align*}
    3x + y & = 7 \\
    x - y & = 1
\end{align*}
:::::

:::::{tab-item} b
\begin{align*}
    x - 2y & = 7 \\
    2x + y & = 1
\end{align*}
:::::

:::::{tab-item} c
\begin{align*}
    x + 2y & = 5 \\
    4x & = 6 - y
\end{align*}
:::::

:::::{tab-item} d
\begin{align*}
    7x + 2y & = -1 \\
    -x + 5y & = 25
\end{align*}
:::::

::::::

:::{raw} html
---
file: ggb/underveisoppgaver/oppgaver/underveisoppgave_2_tomt_cas_vindu.html
---
:::


:::::{admonition} Løsning
---
class: dropdown, solution
---
::::{tab-set}
:::{tab-item} Med `Løs`{l=console}-funksjonen
```{raw} html
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_2_cmd_solve.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
```{raw} html
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_2_gui_solve.html
---
```
:::
::::
:::::

````

````{tab} Python

Test forståelsen din her!

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a

Ta quizen!

:::{raw} html
---
file: quiz/quiz_2/quiz_2.html
---
:::

::::::

::::::{tab-item} b

Fyll inn programmene og løs likningssystemene.

:::::{tab-set}
::::{tab-item} Oppgave 1

$$
3x + y = 7 \quad \land \quad x - y = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_2/oppgave_1.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(3 * x + y, 7)
likning2 = Eq(x - y, 1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:

```console
{x: 2, y: 1}
```

**Løsning**:

$$
x = 2 \quad \land \quad y = 1
$$
:::
::::

::::{tab-item} Oppgave 2

$$
x - 2y = 7 \quad \land \quad 2x + y = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_2/oppgave_2.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(x - 2 * y, 7)
likning2 = Eq(2 * x + y, 1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:

```console
{x: 9/5, y: -13/5}
```

**Løsning**:

$$
x = \dfrac{9}{5} \quad \land \quad y = -\dfrac{13}{5}
$$
:::

::::

::::{tab-item} Oppgave 3

$$
x + 2y = 5 \quad \land \quad 4x = 6 - y
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_2/oppgave_3.html
---
:::

---

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(x + 2 * y, 5)
likning2 = Eq(4 * x, 6 - y)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:

```console
{x: 1, y: 2}
```

**Løsning**:

$$
x = 1 \quad \land \quad y = 2
$$
:::

::::

:::::

::::::
:::::::
````

::::::::::


## Ulikheter med CAS

::::::::::{admonition} Utforsk 3
---
class: explore
---
````{tab} Geogebra
Under vises et *interaktivt* CAS-vindu der en lineær ulikhet er løst, både med `Løs`{l=console}-funksjonen og <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen. 

::::{tab-set}
:::{tab-item} Med `Løs`{l=console}-funksjonen
```{raw} html
---
file: ggb/utforsk/utforsk_3_cmd.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
```{raw} html
---
file: ggb/utforsk/utforsk_3_gui.html
---
```
:::

::::


Deloppgave 1
: Hvilken ulikhet er det som er løst? <br> Kan du lese av løsningen som er funnet?


Deloppgave 2
: Bruk CAS-vinduene til å løse ulikheten $3x + 5 \leq -2x + 7$. <br> Får du samme svar med begge metodene? <br> *Tips: for å få symbolet $\leq$ kan du skrive `<`{l=console} etterfulgt av `=`{l=console} i CAS-vinduet.*

````

````{tab} Python
Vi kan også løse ulikheter ved å bruke `solve`{l=python}-funksjonen i `sympy`{l=python}.

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a
Under vises tre eksempler på hvordan man lager ulikheter med `sympy`{l=python}. 

Les og kjør koden for hvert eksempel, og bestem hvilken ulikhet programmet lager.

:::::{tab-set}
::::{tab-item} Eksempel 1
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/a/eksempel_1.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
2x - 4 > 0
$$
:::

::::

::::{tab-item} Eksempel 2
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/a/eksempel_2.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
-2x + 3 < 0
$$
:::

::::

::::{tab-item} Eksempel 3
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/a/eksempel_3.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
-\dfrac{x}{3} + 5 \geq -x + 7
$$
:::

::::

:::::

::::::

::::::{tab-item} b
For å løse ulikheten, bruker vi `solve`{l=python}-funksjonen akkurat som før! 

Her følger tre eksempler på dette – kjør koden for hvert eksempel og bestem løsningen av ulikhetene ved hjelp av utskriften.

> Her bruker vi `pprint`{l=python} og ikke `print`{l=python} for å få en utskrift som likner på matematikken. Prøv gjerne å bruke `print`{l=python} i stedet. Da vil utskriften bruke "&" i stedet for "$\land$". 

:::::{tab-set}
::::{tab-item} Eksempel 1
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/b/eksempel_1.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**: 

```console
(-2 < x) ∧ (x < ∞)
```

**Løsning av ulikheten**:

$$
-2 < x \quad \land \quad x < \infty \quad \iff \quad -2 < x < \infty \quad \iff \quad x > -2
$$

(Det er overflødig å ta med at $x < \infty$ siden dette er underforstått når vi bare skriver $x > -2$ – men det ikke *feil* å gjøre det!). 

> Merk at tegnet $\infty$ betyr *uendelig*. 

:::

::::

::::{tab-item} Eksempel 2
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/b/eksempel_2.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**: 

```console
(-5/2 < x) ∧ (x < ∞)
```

**Løsning av ulikheten**:

$$
-\dfrac{5}{2} < x \quad \land \quad x < \infty \quad \iff \quad x > -\dfrac{5}{2}
$$

:::

::::

::::{tab-item} Eksempel 3
:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_3/b/eksempel_3.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Utskrift**: 

```console
(3 <= x) ∧ (x < ∞)
```

**Løsning av ulikheten**:

$$
3 \leq x \quad \land \quad x < \infty \quad \iff \quad x \geq 3
$$

:::

::::

:::::
::::::

:::::::


````

::::::::::

---

::::::::::{admonition} Underveisoppgave 3
---
class: check
---

````{tab} Geogebra

Bruk CAS-vinduet under til å løse ulikhetene.
:::::::::{tab-set}
---
class: tabs-parts
---
::::::::{tab-item} a
$$
2x + 5 < 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x < -\dfrac{5}{2}
$$
:::

::::::::

::::::::{tab-item} b
$$
2x - 3 \geq -2
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \geq \dfrac{1}{2}
$$
:::

::::::::

::::::::{tab-item} c
$$
-3x + 2 \leq -x + 2
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \geq 0
$$
:::

::::::::

:::::::::

:::{raw} html
---
file: ./ggb/underveisoppgaver/oppgaver/underveisoppgave_3_tomt_cast_vindu.html
---
:::


````

````{tab} Python 

Fyll inn programmene under og bestem løsningen av ulikhetene ved hjelp av programmene.

:::::::::{tab-set}
---
class: tabs-parts
---
::::::::{tab-item} a
$$
2x + 5 < 0
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_3/a.html
---
:::


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x < -\dfrac{5}{2}
$$
:::

::::::::

::::::::{tab-item} b
$$
2x - 3 \geq -2
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_3/b.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \geq \dfrac{1}{2}
$$
:::

::::::::

::::::::{tab-item} c
$$
-3x + 2 \leq -x + 2
$$

:::{raw} html
---
file: ./interaktiv_kode/underveisoppgaver/underveisoppgave_3/c.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \geq 0
$$
:::

::::::::

:::::::::

````

::::::::::

## Oppgaver

````{tab} Geogebra

```{tab} Windows <span style="display: inline-block; width: 20px; height: 20px; background-image: url('https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg'); background-size: cover;" aria-label="Windows-knappen"></span>
 

Når du løser oppgavene under, skal du bruke desktopversjonen av GeoGebra. Den åpner du som følger:
1. Trykk på Windows-knappen <span style="display: inline-block; width: 20px; height: 20px; background-image: url('https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg'); background-size: cover;" aria-label="Windows-knappen"></span> på tastaturet.
2. Søk etter "Geogebra 6" 
3. Trykk på *enter* på tastaturet. &#9166;

```

```{tab} Mac 
Når du løser oppgavene under, skal du bruke desktopversjonen av GeoGebra. Den åpner du som følger:
1.  Trykk på *⌘* og ␣ *(mellomrom)* på tastaturet samtidig.

2. Søk etter "Geogebra 6"
3. Trykk på *enter* på tastaturet. &#9166;
```


````

````{tab} Python

Her kommer det en samling oppgaver der du får trent på å løse likninger, likningssystemer og ulikheter ved å bruke `sympy`{l=python}.

````


::::::::{admonition} Oppgave 1 
---
class: problem-level-1
---

````{tab} Geogebra


Løs likningene ved hjelp av CAS. 

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
$$
-3x + 2 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \dfrac{2}{3}
$$
:::
:::::

:::::{tab-item} b
$$
4x + 2 = 5
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \dfrac{3}{4}
$$
:::

:::::

:::::{tab-item} c
$$
5x + 8 = -2x + 3
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -\dfrac{5}{7}
$$
:::

:::::

:::::{tab-item} d
$$
\dfrac{1}{2}x - 2 = 3x + 2
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -\dfrac{8}{5}
$$
:::

:::::
::::::

````

````{tab} Python 

Fyll ut programmet under og løs likningene.

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
$$
-3x + 2 = 0
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_1/a.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-5
---
from sympy import *
from sympy.abc import x

likning = Eq(-3 * x + 2, 0)
løsning = solve(likning)

print(løsning)
```

**Utskrift**:

```console
[2/3]
```

**Løsning**:

$$
x = \dfrac{2}{3}
$$
:::
:::::

:::::{tab-item} b
$$
4x + 2 = 5
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_1/b.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---

**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-5
---

from sympy import *
from sympy.abc import x

likning = Eq(4 * x + 2, 5)
løsning = solve(likning)

print(løsning)
```

**Utskrift**: 

```console
[3/4]
```

**Løsning**:

$$
x = \dfrac{3}{4}
$$
:::

:::::

:::::{tab-item} c
$$
5x + 8 = -2x + 3
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_1/c.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---

**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-5
---
from sympy import *
from sympy.abc import x

likning = Eq(5 * x + 8, -2 * x + 3)
løsning = solve(likning)

print(løsning)
```

**Utksrift**:

```console
[-5/7]
```

**Løsning**:

$$
x = -\dfrac{5}{7}
$$
:::

:::::

:::::{tab-item} d
$$
\dfrac{1}{2}x - 2 = 3x + 2
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_1/d.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---

**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-5
---
from sympy import *
from sympy.abc import x

likning = Eq(x / 2 - 2, 3 * x + 2)
løsning = solve(likning)

print(løsning)
```

**Utskrift**:

```console
[-8/5]
```

**Løsning**:

$$
x = -\dfrac{8}{5}
$$
:::

:::::
::::::


````

::::::::

---

::::::::{admonition} Oppgave 2
---
class: problem-level-1
---

````{tab} Geogebra

Løs likningssystemene ved hjelp av CAS.

:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a
$$
3x + y = 7 \quad \land \quad x - y = 1
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 2 \quad \land \quad y = 1
$$
:::

::::::

::::::{tab-item} b
$$
x - 2y = 7 \quad \land \quad x + y = 1
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 3 \quad \land \quad y = -2
$$
:::

::::::

::::::{tab-item} c
\begin{align*}
    x + 2y &= 5 \\
    4x &= 6 - y
\end{align*}

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 1 \quad \land \quad y = 2
$$
:::

::::::

::::::{tab-item} d
$$
-2x + y = -1 \quad \land \quad 4x + 2y + 14 = 0
$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -\dfrac{3}{2} \quad \land \quad y = -4
$$
:::

:::::::

````

````{tab} Python

Fyll inn programmene og løs likningsystemene. 


:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} a
$$
3x + y = 7 \quad \land \quad x - y = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_2/a.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(3 * x + y, 7)
likning2 = Eq(x - y, 1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```
**Utskrift**:

```console
{x: 2, y: 1}
```

**Løsning**:

$$
x = 2 \quad \land \quad y = 1
$$

:::

::::::

::::::{tab-item} b
$$
x - 2y = 7 \quad \land \quad x + y = 1
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_2/b.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(x - 2 * y, 7)
likning2 = Eq(x + y, 1)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```
**Utskrift**:

```console
{x: 3, y: -2}
```

**Løsning**:

$$
x = 3 \quad \land \quad y = -2
$$

:::

::::::

::::::{tab-item} c
\begin{align*}
    x + 2y &= 5 \\
    4x &= 6 - y
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_2/c.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(x + 2 * y, 5)
likning2 = Eq(4 * x, 2 - 3 * y)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```
**Utskrift**:

```console
{x: -11/5, y: 18/5}
```

**Løsning**:

$$
x = 1 \quad \land \quad y = 2
$$

:::

::::::

::::::{tab-item} d
\begin{align*}
    -2x + y &= -1 \\
    4x + 2y + 14 &= 0
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_2/d.html
---
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
**Programkode**:

```{code-block} python
---
linenos: true
emphasize-lines: 4-6
---
from sympy import *
from sympy.abc import x, y

likning1 = Eq(-2 * x + y, -1)
likning2 = Eq(4 * x + 2 * y + 14, 0)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```
**Utskrift**:

```console
{x: -3/2, y: -4}
```

**Løsning**:

$$
x = -\dfrac{3}{2} \quad \land \quad y = -4
$$

:::

:::::::

````

::::::::


---

::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---


````{tab} Geogebra
Løs ulikhetene med CAS.

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
$$
-2x + 3 \geq x - 5
$$

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x \leq \dfrac{8}{3}
$$
::::

::::::::::

::::::::::{tab-item} b
$$
2x - 1 < x + 4
$$

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x < 5
$$

::::

::::::::::

::::::::::{tab-item} c
$$
\dfrac{1}{2}x + 3 > x - 1
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x < 8
$$
::::

::::::::::

::::::::::{tab-item} d
$$
\dfrac{x}{3} + \dfrac{1}{2} \leq -\dfrac{x}{2} + \dfrac{1}{3}
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x \leq -\dfrac{1}{5} 
$$
::::

::::::::::
:::::::::::

````

````{tab} Python
Løs ulikhetene ved hjelp av `sympy`{l=python} i kodevinduet.


:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
$$
-2x + 3 \geq x - 5
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_3/a.html
---
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:
```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

ulikhet = (-2 * x + 3 >= x - 5)
løsning = solve(ulikhet)

pprint(løsning)
```

**Utskrift**:
```console
(x <= 8/3) ∧ (-∞ < x)
```

**Løsning**:

$$
x \leq \dfrac{8}{3}
$$
::::

::::::::::

::::::::::{tab-item} b
$$
2x - 1 < x + 4
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_3/b.html
---
:::

::::{admonition} Fasit
---
class: dropdown, answer
---

**Programkode**:
```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

ulikhet = (2 * x - 1 < x + 4)
løsning = solve(ulikhet)

pprint(løsning)
```

**Utskrift**:
```console
(-∞ < x) ∧ (x < 5)
```

**Løsning**:

$$
x < 5
$$

::::

::::::::::

::::::::::{tab-item} c
$$
\dfrac{1}{2}x + 3 > x - 1
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_3/c.html
---
:::

::::{admonition} Fasit
---
class: dropdown, answer
---

**Programkode**:
```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

ulikhet = (x / 2 + 3 > x - 1)
løsning = solve(ulikhet)

pprint(løsning)
```

**Utskrift**:
```console
(-∞ < x) ∧ (x < 8)
```

**Løsning**:

$$
x < 8
$$
::::

::::::::::

::::::::::{tab-item} d
$$
\dfrac{x}{3} + \dfrac{1}{2} \leq -\dfrac{x}{2} + \dfrac{1}{3}
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_3/d.html
---
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

ulikhet = (x / 3 + 1 / 2 <= -x / 2 + 1 / 3)
løsning = solve(ulikhet)

pprint(løsning)

```

**Utskrift**:
```console
(x <= -0.2) ∧ (-∞ < x)
```

**Løsning**:

$$
x \leq -0.2 \quad \iff \quad x \leq -\dfrac{1}{5} 
$$
::::

::::::::::
:::::::::::
````

::::::::::::

---


::::::::::::{admonition} Oppgave 4
---
class: problem-level-2
---

````{tab} Geogebra

Bruk CAS til å løse oppgavene under.

:::::::::::{tab-set} 
---
class: tabs-parts
---
::::::::::{tab-item} a

Løs likningen

$$
-3x + 2 = 4x - 9
$$

---

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x = \dfrac{11}{7}
$$

::::

::::::::::

::::::::::{tab-item} b
Løs likningssystemet

\begin{align*}
    2x + 3y &= -5 \\
    -x + 2y &= 6
\end{align*}

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x = -4 \quad \land \quad y = 1
$$
::::

::::::::::

::::::::::{tab-item} c
Løs ulikheter

$$
-2x + 5 > -\dfrac{1}{4}x + 11
$$

---

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x < -\dfrac{24}{7}
$$
::::

::::::::::

::::::::::{tab-item} d
Løs likningssystemet

\begin{align*}
    x + y + z &= 6 \\
    2x - y + z &= 3 \\
    3x + y - z &= 4
\end{align*}

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x = \dfrac{7}{5} \quad \land \quad y = \dfrac{11}{5} \quad \land \quad z = \dfrac{12}{5}
$$

::::

::::::::::

:::::::::::

````

````{tab} Python

> ⚠️ Her er det viktig at du prøver å **skrive koden** og ikke **bare kopierer** fra tidligere programmer. Du må få trent litt på å skrive koden selv så du blir rask og husker funksjonene bedre. Det står kommentarer i koden som hjelper deg på vei.

:::::::::::{tab-set} 
---
class: tabs-parts
---
::::::::::{tab-item} a
Skriv et program som løser likningen med `sympy`{l=python}

$$
-3x + 2 = 4x - 9
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_4/a.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import * 
from sympy.abc import x

likning = Eq(-3 * x + 2, 4 * x - 9)
løsning = solve(likning)

print(løsning)
```

**Utskrift**:
```console
[11/7]
```

**Løsning**:

$$
x = \dfrac{11}{7}
$$

::::

::::::::::

::::::::::{tab-item} b
Skriv et program som løser likningssystemet med `sympy`{l=python}

\begin{align*}
    2x + 3y &= -5 \\
    -x + 2y &= 6
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_4/b.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import * 
from sympy.abc import x, y

likning1 = Eq(2 * x + 3 * y, -5)
likning2 = Eq(-x + 2 * y, 6)
likningssystem = [likning1, likning2]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:
```console
{x: -4, y: 1}
```

**Løsning**:

$$
x = -4 \quad \land \quad y = 1
$$
::::

::::::::::

::::::::::{tab-item} c
Skriv et program som løser ulikheten med `sympy`{l=python}

$$
-2x + 5 > -\dfrac{1}{4}x + 11
$$

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_4/c.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x

ulikhet = (-2 * x + 5 > -x / 4 + 11)
løsning = solve(ulikhet)

pprint(løsning)
```

**Utskrift**:
```console
(-∞ < x) ∧ (x < -24/7)
```

**Løsning**:

$$
x < -\dfrac{24}{7}
$$
::::

::::::::::

::::::::::{tab-item} d
Skriv et program som løser likningssystemet med `sympy`{l=python}

\begin{align*}
    x + y + z &= 6 \\
    2x - y + z &= 3 \\
    3x + y - z &= 4
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_4/d.html
---
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x, y, z

likning1 = Eq(x + y + z, 6)
likning2 = Eq(2 * x - y + z, 3)
likning3 = Eq(3 * x + y - z, 4)

likningssystem = [likning1, likning2, likning3]

løsning = solve(likningssystem)

print(løsning)

```

**Utskrift**:
```console
{x: 7/5, y: 11/5, z: 12/5}
```

**Løsning**:

$$
x = \dfrac{7}{5} \quad \land \quad y = \dfrac{11}{5} \quad \land \quad z = \dfrac{12}{5}
$$
::::

::::::::::

:::::::::::

````

::::::::::::

---


::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---

````{tab} Geogebra 
Løs likningssystemene ved hjelp av CAS.

:::::::::::{tab-set}
---
class: tabs-parts
---

::::::::::{tab-item} a
\begin{align*}
    x + y - z &= 1 \\
    x - y - z &= -1 \\
    x + y + z &= 3
\end{align*}

---

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 1 \quad \land \quad y = 1 \quad \land \quad z = 1
$$
::::

::::::::::

::::::::::{tab-item} b


\begin{align*}
    2x + y - z &= 1 \\
    x - y + z &= 2 \\
    3x + 2y + z &= 3
\end{align*}


---


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 1 \quad \land \quad y = -\dfrac{1}{3} \quad \land \quad z = \dfrac{2}{3}
$$
::::

::::::::::

::::::::::{tab-item} c

\begin{align*}
    a - b + c &= -11 \\
    a + b + c &= 11 \\
    8a + 4b + 2c &= -4
\end{align*}

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
a = -8 \quad \land \quad b = 11 \quad \land \quad c = 8
$$
::::


::::::::::

::::::::::{tab-item} d

\begin{align*}
    r + 2s - t &= 1 \\
    2r - s + 3t &= 2 \\
    3r + 2s + 2t &= 3
\end{align*}

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
r = 1 \quad \land \quad s = 0 \quad \land \quad t = 0
$$
::::

::::::::::


:::::::::::

````

````{tab} Python 

Skriv et program som bruker `sympy`{l=python} til å løse likningssystemene. 

> ⚠️ Viktig at du prøver å skrive programmet fra bunnen av og ikke kopierer fra tidligere programmer!

:::::::::::{tab-set}
---
class: tabs-parts
---

::::::::::{tab-item} a
\begin{align*}
    x + y - z &= 1 \\
    x - y - z &= -1 \\
    x + y + z &= 3
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_5/a.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x, y, z

likning1 = Eq(x + y - z, 1)
likning2 = Eq(x - y - z, -1)
likning3 = Eq(x + y + z, 3)

likningssystem = [likning1, likning2, likning3]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:
```console
{x: 1, y: 1, z: 1}
```

**Løsning**:

$$
x = 1 \quad \land \quad y = 1 \quad \land \quad z = 1
$$
::::

::::::::::

::::::::::{tab-item} b


\begin{align*}
    2x + y - z &= 1 \\
    x - y + z &= 2 \\
    3x + 2y + z &= 3
\end{align*}


:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_5/b.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import x, y, z

likning1 = Eq(2 * x + y - z, 1)
likning2 = Eq(x - y + z, 2)
likning3 = Eq(3 * x + 2 * y + z, 3)

likningssystem = [likning1, likning2, likning3]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:
```console
{x: 1, y: -1/3, z: 2/3}
```

**Løsning**:

$$
x = 1 \quad \land \quad y = -\dfrac{1}{3} \quad \land \quad z = \dfrac{2}{3}
$$
::::

::::::::::

::::::::::{tab-item} c

\begin{align*}
    a - b + c &= -11 \\
    a + b + c &= 11 \\
    8a + 4b + 2c &= -4
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_5/c.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import a, b, c

likning1 = Eq(a - b + c, -11)
likning2 = Eq(a + b + c, 11)
likning3 = Eq(8 * a + 4 * b + 2 * c, -4)

likningssystem = [likning1, likning2, likning3]

løsning = solve(likningssystem)

print(løsning)

```

**Utskrift**:
```console
{a: -8, b: 11, c: 8}
```

**Løsning**:

$$
a = -8 \quad \land \quad b = 11 \quad \land \quad c = 8
$$
::::


::::::::::

::::::::::{tab-item} d

\begin{align*}
    r + 2s - t &= 1 \\
    2r - s + 3t &= 2 \\
    3r + 2s + 2t &= 3
\end{align*}

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_5/d.html
---
:::

---

::::{admonition} Fasit
---
class: dropdown, answer
---
**Programkode**:

```{code-block} python
---
linenos: true
---
from sympy import *
from sympy.abc import r, s, t

likning1 = Eq(r + 2 * s - t, 1)
likning2 = Eq(2 * r - s + 3 * t, 2)
likning3 = Eq(3 * r + 2 * s + 2 * t, 3)

likningssystem = [likning1, likning2, likning3]

løsning = solve(likningssystem)

print(løsning)
```

**Utskrift**:
```console
{r: 1, s: 0, t: 0}
```

**Løsning**:

$$
r = 1 \quad \land \quad s = 0 \quad \land \quad t = 0
$$
::::

::::::::::


:::::::::::


````

::::::::::::


---


<!-- ::::{admonition} Oppgave 6
---
class: problem-level-2
---
Sett opp likninger og løs ved hjelp av CAS

Deloppgave 1
: Amna, Berit og Celine delte en boks is. Amna spiste en tredel, Berit spiste to femtedeler, og Celine spiste resten. Hvor mye spiste Celine? 

:::{admonition} Fasit
---
class: answer, dropdown
---
Celine spiste $\dfrac{4}{15}$
:::

Deloppgave 2
: Tre venner, Emma, Sophie og Sara, har til sammen 110 bøker. Sara har dobbelt så mange bøker som Sophie, og Emma har 10 bøker mindre enn Sara. Finn ut hvor mange bøker hver av de tre vennene har.

:::{admonition} Fasit
---
class: answer, dropdown
---
Sophie har 24 bøker, Sara har 48 bøker, og Emma har 38 bøker.
:::

Deloppgave 3
: På en vinteraktivitetsdag ved skolen valgte 60 % av elevene skøyting. En tredel valgte aking. De siste 15 elevene hadde fått fritak. Hvor mange elever er det ved skolen? 

:::{admonition} Fasit
---
class: answer, dropdown
---
Det var $225$ elever ved skolen.
:::

Deloppgave 4
: Ole, Dole og Doffen er til sammen 66 år. Ole er dobbelt så gammel som Doffen, og Dole er 6 år eldre enn Doffen. Finn ut hvor gamle de tre guttene er. 

:::{admonition} Fasit
---
class: answer, dropdown
---
Doffen er 15 år, Ole er 30 år og Dole er 21 år. 
:::

:::: -->

<!-- ::::{admonition} Oppgave 6
---
class: problem-level-3, 
---
På en fotballkamp er det tre kategorier billetter: barn, voksne og pensjonister. 

Publikumstallet på kampen var 2100. Barnebilletten kostet 50 kr, voksenbilletten 200 kr og pensjonistbilletten 100 kr. Billettinntektene ble på 315 000 kr. Det var dobbelt så mange pensjonister som barn på kampen. 

Bestem antallet barn, voksne og pensjonister på kampen.

:::{admonition} Fasit
---
class: answer, dropdown
---
Det var 300 barn, 600 pensjonister og 1200 voksne på kampen.
:::
:::: -->
