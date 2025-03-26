# Eksamensøving

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::


:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Nedenfor vises en programkode. 

Forklar hva programmet regner ut og bestem verdien som skrives ut av programmet. Skriv inn svaret ditt i feltet nedenfor.

:::{raw} html
---
file: ./python/oppgave_2/kodevindu.html
---
:::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
Nedenfor vises en programkode. 

Forklar hva programmet regner ut og avgjør hvilke verdier som skrives ut av programmet. Skriv inn svaret ditt i feltet nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar hva programmet regner ut og avgjør hvilke verdier som skrives ut av programmet. 

Skriv inn svaret ditt i feltet nedenfor.

:::::::::::::

:::::::::::::{tab-item} b
Endre på programmet slik at det løser likningen 

$$
x^2 - x - 6 = 0
$$

Bestem løsningene med programmet ditt.

:::::::::::::

::::::::::::::

:::{raw} html
---
file: ./python/oppgave_3/kodevindu.html
---
:::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---
En programkode er vist nedenfor. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar hva programmet regner ut og bestem hvilken verdi som skrives ut av programmet. 

Sjekk svaret ved å skrive inn i feltet nedenfor.

:::::::::::::


:::::::::::::{tab-item} b
Da en matematiker som het Gauss gikk på skolen, fikk han i oppgave å summere de 100 første heltallene som straff for at han var urolig i timen. 

Endre på programmet og bruk det til å løse oppgaven til Gauss.

:::::::::::::


::::::::::::::

:::{raw} html
---
file: ./python/oppgave_4/kodevindu.html
---
:::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
I denne oppgaven skal du jobbe med summer av oddetall og partall. Vi lar $S_n$ være summen av de $n$ første oddetallene. Nedenfor vises noen av disse summene: 

\begin{align*}
    S_1 &= 1 \\
    S_2 &= 1 + 3 \\
    S_3 &= 1 + 3 + 5 \\
    S_4 &= 1 + 3 + 5 + 7 \\
    S_5 &= 1 + 3 + 5 + 7 + 9 \\
    S_6 &= 1 + 3 + 5 + 7 + 9 + 11 \\
    \vdots & \quad \quad \quad \vdots \quad \quad \quad \vdots \quad \quad \quad \vdots \\
\end{align*}


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som regner ut og skriver ut summene $S_1, S_2, S_3, \ldots, S_{20}$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
s = 0

for n in range(20):
    oddetall = 2 * n + 1
    s = s + oddetall
    print(s)
:::

som gir utskriften

:::{code-block} console
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør om summen av de 20 første partallene er større enn summen av de 20 første oddetallene.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
emphasize-lines: 3,4,5
---
s = 0

for n in range(1, 21):
    partall = 2 * n
    s = s + partall

print(s)
:::

som gir utskriften

:::{code-block} console
420
:::

Altså er summen av de 20 første partallene større enn summen av de 20 første oddetallene.


::::

:::::::::::::

::::::::::::::

:::{raw} html
---
file: ./python/oppgave_5/kodevindu.html
---
:::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
Nedenfor vises en figur som er satt sammen av uendelig mange linjestykker.

Lengden til et linjestykke er alltid $90 \%$ av lengden til det forrige linjestykket. Det første linjestykket er $100$ cm langt.

:::{figure} ./figurer/oppgave_6/figur.svg
---
width: 100%
class: no-click
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som bestemmer summen av lengdene til de $10$ første linjestykkene.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
s = 0 # summen av lengdene
lengde = 100 # første linjestykke
n = 0 # antall linjestykker

while n < 10:
    s = s + lengde     # plusser på lengden
    n = n + 1        # øk antall linjestykker med 1
    lengde = 0.9 * lengde     # neste lengde = 90% av forrige lengde
    
print(s)
:::

gir utskriften

:::{code-block} console
651.3215599000001
:::

som betyr at summen av lengdene til de 10 første linjestykkene er ca. $651.32$ cm.
::::

:::::::::::::


:::::::::::::{tab-item} b
Hvor mange linjestykker må du legge sammen for at summen av lengdene skal bli minst 9 meter?



::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
emphasize-lines: 5,10
---
s = 0 # summen av lengdene
lengde = 100 # første linjestykke
n = 0 # antall linjestykker

while s < 900: # så lengde summen er mindre enn 9 m = 900 cm
    s = s + lengde     # plusser på lengden
    n = n + 1        # øk antall linjestykker med 1
    lengde = 0.9 * lengde     # neste lengde = 90% av forrige lengde
    
print(n)
:::

gir utskriften

:::{code-block} console
22
:::

som betyr at vi trenger 22 linjestykker før linjestykket blir lenger enn 9 meter (900 cm).
::::

:::::::::::::



:::::::::::::{tab-item} c
Hvilken lengde vil lengden av hele figuren nærme seg?

::::{admonition} Fasit
---
class: answer, dropdown
---
Kjører vi programmet med veldig mange linjestykker, vil summen av lengdene nærme seg $1000$ cm.
::::

:::::::::::::



::::::::::::::


:::{raw} html
---
file: ./python/oppgave_6/kodevindu.html
---
:::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---
I figuren nedenfor vises grafen til en rasjonal funksjon gitt ved

$$
f(x) = \dfrac{8}{x^2 + 4}
$$

Et rektangel har hjørner i punktene $(0,0)$, $(3, 0)$, $(3, f(3))$ og $(0, f(3))$.

:::{figure} ./figurer/oppgave_7/figur.svg
---
width: 80%
class: no-click
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som regner ut arealet til rektangelet.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 4)
    
def A(x):
    return x * f(x)
    

areal = A(3)

print(areal)
:::

som gir utskriften

:::{code-block} console
1.8461538461538463
:::

som betyr at arealet av rektangelet er omtrent $1.85$. 
::::

:::::::::::::


:::::::::::::{tab-item} b
Utvid programmet ditt slik at det skriver ut arealet av rektangelene med hjørner i punktet $(0, 0)$, $(k, 0)$, $(k, f(k))$ og $(0, f(k))$ for $k = \{1, 2, 3, \ldots, 9, 10\}$.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 4)
    
def A(x):
    return x * f(x)
    
for k in range(1, 11):
    print(k, A(k))
:::

som gir utskriften 

:::{code-block} console
1 1.6
2 2.0
3 1.8461538461538463
4 1.6
5 1.3793103448275863
6 1.2000000000000002
7 1.0566037735849056
8 0.9411764705882353
9 0.8470588235294118
10 0.7692307692307693
:::

Første kolonne er verdiene av $k$ og andre kolonne er arealene av rektanglene.

:::::::::::::


:::::::::::::{tab-item} c
Utvid programmet ditt og bestem hvilken verdi av $k [0, \to\rangle$ som gir størst mulig areal.


::::{admonition} Fasit
---
class: answer, dropdown
---

Vi starter med den laveste mulige verdien av $k$, så øker vi $k$ med en liten verdi så lenge det neste arealet er større enn det nåværende. Når det neste arealet er mindre enn det nåværende, har vi funnet den verdien av $k$ som gir størst areal:

:::{code-block} python
---
linenos:
---
def f(x):
    return 8 / (x**2 + 4)
    
def A(x):
    return x * f(x)
    
k = 0
while A(k) < A(k + 0.01): # Så lenge neste areal er større 
    k = k + 0.01
    
print(k)
:::

som gir utskriften

:::{code-block} console
2.0000000000000013
:::

som betyr at $k \approx 2$ gir størst mulig areal.
::::

:::::::::::::

::::::::::::::

:::{raw} html
---
file: ./python/oppgave_7/kodevindu.html
---
:::

:::::::::::::::








