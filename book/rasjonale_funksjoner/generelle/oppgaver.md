# Oppgaver: <br> Generelle rasjonale funksjoner 



:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Bestem nullpunktene til funksjonene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = \dfrac{x^2 - 4}{x + 1}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -2 \or x = 2
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi leter først etter nullpunktene til tellerpolynomet:

$$
x^2 - 4 = 0 \liff (x + 2)(x - 2) = 0 \liff x = -2 \or x = 2.
$$

Til slutt vi må sjekke at sjekke nullpunktet til nevnerpolynomet og ekskludere nullpunkter de har til felles:

$$
x + 1 = 0 \liff x = -1.
$$

Teller- og nevnerpolynomet har ingen felles nullpunkter som betyr at $f$ har samme nullpunkter som tellerpolynomet. Dermed har vi at nullpunktene til $f$ er 

$$
x = -2 \or x = 2.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = \dfrac{x - 1}{(x + 3)^2}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 1
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---

::::

:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = \dfrac{(x - 2)(x + 3)}{x^2 - 4}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = \dfrac{x^2 - x - 2}{x^2 - 9}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \or x = 2.
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
**Bruk polynomdivisjon** til å bestemme likningene til de horisontale eller skrå asymptotene til funksjonene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = \dfrac{4x - 6}{2x + 1}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 2
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjon for å lese av kvotienten $K(x)$ i divisjonen:

:::{figure} ./koder/oppgaver/oppgave_2/a.svg
---
width: 50%
class: no-click
---
:::

Vi kan se at kvotienten er $K(x) = 2$ som betyr at likningen for den horisontale asymptoten er $y = 2$.
::::

:::::::::::::

:::::::::::::{tab-item} b
$$
g(x) = \dfrac{4x^2 + x - 8}{x^2 + 1}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 4
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjon for å bestemme kvotienten $K(x)$ i divisjonen:

:::{figure} ./koder/oppgaver/oppgave_2/b.svg
---
width: 60%
class: no-click
---
:::

Fra divisjonen får vi at $K(x) = 4$ som betyr at likningen for den horisontale asymptoten er $y = 4$.

::::


:::::::::::::

:::::::::::::{tab-item} c
$$
h(x) = \dfrac{x^2 + x - 2}{x + 5}
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = x - 4.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjon for å bestemme kvotienten $K(x)$ i divisjonen:

:::{figure} ./koder/oppgaver/oppgave_2/c.svg
---
width: 60%
class: no-click
---
:::

Fra divisjonen får vi at $K(x) = x - 4$ som betyr at likningen for den skrå asymptoten er $y = x - 4$.

::::

:::::::::::::

:::::::::::::{tab-item} d
$$
p(x) = \dfrac{x + 3}{x^2 + 2x + 1}
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 0
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Tellergraden er lavere enn nevnergraden som betyr at telleren allerede *er* et restpolynom i divisjonen. Derfor vil kvotienten være $K(x) = 0$ og vi får at likningen til den horisontale asymptoten er $y = 0$.
::::



:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
Bestem likningene til de vertikale asymptotene til hver av funksjonene (dersom de eksisterer).

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = \dfrac{x^2 - 4}{x^2 - 9}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \or x = 3.
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må starte med å nullpunktsfaktorisere teller- og nevnerpolynomet for å sjekke om de har noen felles faktorer. Med konjugatsetningen kan vi skrive: 

$$
x^2 - 4 = x^2 - 2^2 = (x + 2)(x - 2)
$$

og

$$
x^2 - 9 = x^2 - 3^2 = (x + 3)(x - 3).
$$

Dermed har vi at 

$$
f(x) = \dfrac{(x + 2)(x - 2)}{(x + 3)(x - 3)}
$$

Vi kan se at telleren og nevner ikke har noen felles faktorer, som betyr at vi nå trygt kan finne de vertikale asymptotene ved å se på nullpunktene til nevneren: 

$$
(x + 3)(x - 3) = 0 \liff x = -3 \or x = 3.
$$

som er likningene til de vertikale asymptotene til $f$.
::::


:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = \dfrac{x^2 - x - 6}{(x + 3)(x - 4)}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---

::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å nullpunktsfaktorisere tellerpolynomet for å se etter lineære faktorer som er felles:

$$
x^2 - x - 6 = (x - 3)(x + 2)
$$

Dermed får vi 

$$
g(x) = \dfrac{(x - 3)(x + 2)}{(x + 3)(x - 4)}
$$

Vi ser at tellerpolynomet og nevnerpolynomet ikke deler noen lineære faktorer, så vi kan bestemme de vertikale asymptotene ved å se på nullpunktene til nevnerpolynomet:

$$
(x + 3)(x - 4) = 0  \liff x = -3 \or x = 4.
$$

Dermed likningene til de vertikale asymptotene $x = -3$ og $x = 4$.
::::


:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = \dfrac{x + 3}{x^2 + 6x + 9}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å se de lineære faktorene i teller- og nevnerpolynomet. Vi kan skrive om nevnerpolynomet med 1.kvadratsetning:

$$
x^2 + 6x + 9 = (x + 3)^2
$$

som betyr at $f(x)$ kan skrives om til

$$
f(x) = \dfrac{x + 3}{(x + 3)^2} = \dfrac{1}{x + 3}
$$

Vi har eliminert alle felles lineære faktorer, og kan gå videre på se etter vertikale asymptoter ved å bestemme nullpunktene til nevnerpolynomet: 

$$
x + 3 = 0  \liff x = -3.
$$

Dermed har $f$ er en vertikal asymptote i $x = -3$. 
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = \dfrac{x^2 + 4x + 3}{x + 1}
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
Ingen vertikale asymptoter.
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å se om teller- og nevnerpolynomet har felles lineære faktorer og kvitter oss med dem. Vi skriver om tellerpolynomet med fullstendig kvadraters metode:

$$
x^2 + 4x + 3 = x^2 + 4x + 2^2 - 2^2 + 3 = (x + 2)^2 - 1 = (x + 1)(x + 3)
$$

Dermed kan vi skrive $p(x)$ som 

$$
p(x) = \dfrac{(x + 1)(x + 3)}{x + 1} = x + 3, \quad x \neq -1.
$$

Vi ser at selv om $x = -1$ er et bruddpunkt for $p$ siden det er nullpunktet til nevnerpolynomet, så vil det ikke være en vertikal asymptote fordi tellerpolynomet hadde én av den samme lineære faktoren. Dermed har $p$ ingen vertikale asymptoter.
::::


:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-2
---
En rasjonal funksjon er gitt ved 

$$
f(x) = \dfrac{x^2 - 16}{(x + 2)(x - 2)}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktene til $f$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \pm 4.
$$
::::

::::{admonition} Løsning
---
class: answer, dropdown
---
Vi starter med å se etter nullpunktene til tellerpolynomet:

$$
x^2 - 16 = 0 \liff x^2 = 16 \liff x = \pm 4.
$$

Ingen av disse er også nullpunkter for nevnerpolynomet, så som betyr at nullpunktene til $f$ er 

$$
x = \pm 4.
$$
:::: 

:::::::::::::


:::::::::::::{tab-item} b
Bestem likningen til den horisontale asymptoten til $f$. 

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = 1.
$$
:::: 


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjon for å bestemme kvotienten $K(x)$: 

:::{figure} ./koder/oppgaver/oppgave_4/b.svg
---
width: 60%
class: no-click
---
:::

Dermed er $K(x) = 1$ som betyr at likningen til den horisontale asymptoten er 

$$
y = 1.
$$

:::: 



:::::::::::::



:::::::::::::{tab-item} c
Bestem likningene til $f$ sine vertikale asymptoter, dersom de eksisterer.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = \pm 2.
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å nullpunktsfaktorisere teller- og nevnerpolynomet for å eliminere felles faktorer. Fra **a** har vi at nullpunktene til tellerpolynomet er $x = \pm 4$. Det betyr at vi kan skrive $f(x)$ som 

$$
f(x) = \dfrac{(x + 4)(x - 4)}{(x + 2)(x - 2)}
$$

siden den ledende koeffisientene til tellerpolynomet var $1$. Vi kan ikke eliminere noen lineære faktorer som betyr at vi kan gå rett på å bestemme nullpunktene til nevnerpolynomet for å bestemme likningene til $f$ sine vertikale asymptoter:

$$
(x + 2)(x - 2) = 0 \liff x = -2 \or x = 2. 
$$

som er likningene til de vertikale asymptotene til $f$.
::::

:::::::::::::


:::::::::::::{tab-item} d
Tegn et fortegnsskjema for $f(x)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_4/d.svg
---
width: 100%
class: no-click
---
:::

::::

:::::::::::::


:::::::::::::{tab-item} e
Lag en skisse av grafen til $f$. Skissen skal inneholde:

* Nullpunktene til $f$.
* Horisontale asymptoter.
* Vertikale asymptoter.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_4/e.svg
---
width: 100%
class: no-click
---
:::
::::


:::::::::::::


:::::::::::::{tab-item} f
Løs ulikheten $f(x) \geq 0$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle \gets, -4] \cup \langle -2, 2 \rangle \cup [4, \to \rangle.
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker fortegnslinja til $f(x)$ som vi tegnet i **d** til å bestemme hvor $f(x) \geq 0$:

:::{figure} ./figurer/oppgaver/oppgave_4/f.svg
---
width: 100%
class: no-click
---
:::

Fra fortegnslinja til $f(x)$ kan vi se at $f(x) \geq 0$ når 

$$
x \in \langle \gets, -4] \cup \langle -2, 2 \rangle \cup [4, \to \rangle.
$$
::::

:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 - 8x + 12}{(x - 2)(x + 3)}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktene til $f$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 6.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Nullpunktene til $f$ er gitt ved nullpunktene til tellerpolynomet så lenge nevnerpolynomet ikke også har samme nullpunkter. Nullpunktene til tellerpolynomet kan vi bestemme med $abc$-formelen som gir

\begin{align*}
x &= \dfrac{-(-8) \pm \sqrt{(-8)^2 - 4\cdot 1 \cdot 12}}{2\cdot 1} \\
\\
&= \dfrac{8 \pm \sqrt{64 - 48}}{2} \\
\\
&= \dfrac{8 \pm \sqrt{16}}{2} \\
\\
&= \dfrac{8 \pm 4}{2} \\
\\
&= 4 \pm 2. 
\end{align*}

Dermed er nullpunktene til tellerpolynomet

$$
x = 2 \or x = 6.
$$

Nullpunktene til nevnerpolynomet er 

$$
(x - 2)(x + 3) = 0 \liff x = 2 \or x = -3.
$$

Dermed er $x = 2$ et felles nullpunkt for både teller- og nevnerpolynomet og dette kan derfor ikke være et nullpunkt for $f$. Dermed har $f$ kunn ett nullpunkt ved

$$
x = 6.
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Bestem likningene til asymptotene til $f$ dersom de eksisterer.


::::::::::::{admonition} Fasit
---
class: answer, dropdown
---
:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} Horisontale/skrå asymptoter
$$
y = 1. 
$$
::::::::::


::::::::::{tab-item} Vertikale asymptoter
$$
x = -3.
$$
::::::::::
:::::::::::

::::::::::::

::::::::::::{admonition} Løsning
---
class: solution, dropdown
---
:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} Horisontale/skrå asymptoter
For å bestemme eventuelle horisontale eller skrå asymptoter, utfører polynomdivisjon for å bestemme kvotienten $K(x)$: 

:::{figure} ./koder/oppgaver/oppgave_5/b.svg
---
width: 80%
class: no-click
---
:::

Fra polynomdivisjonen finner vi at $K(x) = 1$ som betyr at likningen til den horisontale asymptoten til $f$ er 

$$
y = 1.
$$ 

::::::::::


::::::::::{tab-item} Vertikale asymptoter
For å bestemme likningene til eventuelle vertikale asymptoter, faktoriserer vi teller- og nevnerpolynomet og eliminerer alle lineære faktorer som er felles. Vi har at 

$$
f(x) = \dfrac{x^2 - 8x + 12}{(x - 2)(x + 3)} = \dfrac{(x - 2)(x - 6)}{(x - 2)(x + 3)} = \dfrac{x - 6}{x + 3}
$$

der vi forutsetter at $x \neq 2$. For å bestemme de vertikale asymptotene til $f$ ser vi på nullpunktene til nevnerpolynomet som gjenstår som gir:

$$
x + 3 = 0 \liff x = -3. 
$$

Likningen til den vertikale asymptoten til $f$ er derfor 

$$
x = -3.
$$ 
::::::::::

:::::::::::

::::::::::::


:::::::::::::

:::::::::::::{tab-item} c
Lag en skisse av grafen til $f$. Skissen skal inneholde:

* Nullpunkter
* Horisontale/skrå asymptoter
* Vertikale asymptoter
* "Hull" i grafen til $f$ (bruddpunkter). 

> Hint: Det kan være lurt å tegne et fortegnsskjema for $f(x)$ først.


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/oppgaver/oppgave_5/c_graf.svg
---
width: 100%
class: no-click
---
:::
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi har allerede sett at vi kan skrive $f(x)$ som

$$
f(x) = \dfrac{x - 6}{x + 3}
$$

så lenge $x \neq 2$. I $x = 2$ vil grafen til $f$ ha et hull, men vil ellers oppføre som en lineær-over-lineær rasjonal funksjon slik som vi har uttrykt over. Vi kan tegne et fortegnsskjema for det forenklede uttrykket for $f(x)$ og så må vi huske på at $x = 2$ representerer et bruddpunkt.

:::{figure} ./figurer/oppgaver/oppgave_5/c_fortegnslinje.svg
---
width: 100%
class: no-click
---
:::

Denne informasjonen om fortegnet til $f(x)$ sammen med asymptotene $y = 1$ og $x = -3$ kan vi skissere grafen til $f$ som følger:

:::{figure} ./figurer/oppgaver/oppgave_5/c_graf.svg
---
width: 100%
class: no-click
---
:::

::::

:::::::::::::

:::::::::::::{tab-item} d
Løs ulikheten $f(x) \leq 0$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -3, 6] \setminus \{2\}.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
For å løse ulikheten $f(x) \leq 0$ bruker vi fortegnslinja til $f(x)$ som vi tegnet i **c**: 

:::{figure} ./figurer/oppgaver/oppgave_5/c_fortegnslinje.svg
---
width: 100%
---
:::

Fra fortegnslinja til $f(x)$ kan vi lese av at for det *forenklede* uttrykket er $f(x) \leq 0$ når 

$$
x \in \langle -3, 6].
$$

Men så var $x = 2$ et bruddpunkt for $f$ og siden $2 \in \langle -3, 6]$ så må vi ekskludere $2$ fra løsningsmengden. Dermed er løsningen til ulikheten

$$
x \in \langle -3, 6] \setminus \{2\}.
$$

::::

:::::::::::::
::::::::::::::

:::::::::::::::

