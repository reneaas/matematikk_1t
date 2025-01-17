# Oppgaver: Optimering

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 16, \quad D_f = [-4, 4].
$$

Et rektangel har hjørnene $(-3, 0)$, $(-3, f(-3))$, $(3, 0)$ og $(3, f(3))$.


:::{figure} ./figurer/oppgaver/oppgave_1.svg
---
name: fig-polynomer-optimering-oppgave-1
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f(x) = -x^2 + 16$ og et rektangel med hjørnene $(-3, 0)$, $(-3, f(-3))$, $(3, 0)$ og $(3, f(3))$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet av rektangelet.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A = 42
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Lengden i trekanten er $6$ og høyden er 

$$
f(3) = -3^2 + 16 = -9 + 16 = 7.
$$

Arealet av rektangelet er derfor 

$$
A = 6 \cdot 7 = 42.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Et annet rektangel har hjørnene $(-k, 0)$, $(-k, f(-k))$, $(k, 0)$ og $(k, f(k))$ der $k \in \langle 0, 4 \rangle$.

Bestem arealet $A(k)$.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(k) = -2k^3 + 32k
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Lengden i rektangelet blir $k - (-k) = 2k$ og høyden blir $f(k)$. Arealet $A(k)$ er derfor 

$$
A(k) = 2k f(k) = 2k(-k^2 + 16) = -2k^3 + 32k.
$$

::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $k$ slik at arealet blir størst mulig.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
k = \dfrac{4}{\sqrt{3}} \, .
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme $k$ slik at arealet er størst mulig, kan vi finne løsningene til $A'(k) = 0$. Først deriverer vi $A(k)$ som gir:

$$
A'(k) = -6k^2 + 32.
$$

Deretter løser vi $A'(k) = 0$:

$$
A'(k) = 0 \liff -6k^2 + 32 \liff 6k^2 = 32 \liff k^2 = \dfrac{32}{6} = \dfrac{16}{3}
$$

som gir 

$$
k = \pm \sqrt{\dfrac{16}{3}} = \pm \dfrac{\sqrt{16}}{\sqrt{3}} = \pm \dfrac{4}{\sqrt{3}}
$$

Men $k \in \langle 0, 4 \rangle$ som betyr at vi må velge den positive løsningen. Dermed vil verdien av $k$ som gir størst mulig areal være 

$$
k = \dfrac{4}{\sqrt{3}} \, .
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
Du skal bygge en innhegning for en rektangulær hage. På den ene siden er det en stor fjellvegg. Du har $100$ meter med gjerde som du skal bruke til å bygge innhegningen til hagen. Se {numref}`fig-polynomer-optimering-oppgave-2`.

Bestem sidelengdene slik at arealet av hagen blir størst mulig. 

:::{figure} ./figurer/oppgaver/oppgave_2.svg
---
name: fig-polynomer-optimering-oppgave-2
width: 80%
class: no-click
---
viser en rektangulær hage med sidelengder $x$ og $y$ der den ene siden er dekket av et stor fjellvegg. Gjerde som skal settes opp har til sammen en lengde på $100$ meter.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 50 \, \mathrm{m} \and y = 25 \, \mathrm{m}
$$
::::


::::::::{admonition} Løsning
---
class: dropdown, solution
---
Først merker vi oss at vi har $100$ meter med gjerde til rådighet. Dette betyr at 

$$
y + x + y = 100 \liff x + 2y = 100 \liff 2y = 100 - x
$$

som vi kan skrive om til 

$$
y(x) = \dfrac{100 - x}{2}
$$

I tillegg er arealet sidelengdene ganget sammen, som betyr at 

$$
A(x) = x \cdot y(x) = x \cdot \dfrac{100 - x}{2} = -\dfrac{1}{2}x(x - 100) = -\dfrac{1}{2}x^2 + 50x
$$


For å bestemme $x$ slik at arealet blir størst mulig, har vi to muligheter:
1. Finne symmetrilinja til $A(x)$.
2. Løse $A'(x) = 0$.


Vi viser begge strategier for kompletthet, men du trenger naturligvis bare å velge én av de. 


:::::::{tab-set}
---
class: tabs-parts
---
::::::{tab-item} Finne symmetrilinje
Vi kan først observere at nullpunktene til $A(x)$ er 

$$
x = 0 \or x = 100
$$

Symmetrilinja er gjennomsnittet av nullpunktene som gir

$$
x_0 = \dfrac{0 + 100}{2} = 50.
$$

Dermed vil $x = 50$ gi størst mulig areal. Derfor blir sidelengdene til hagen

$$
x = 50 \, \mathrm{m} \and y = \dfrac{100 - 50}{2} \, \mathrm{m} = 25 \, \mathrm{m}.
$$
::::::

::::::{tab-item} Løse $A'(x) = 0$
Vi starter med å gange ut $A(x)$: 

$$
A(x) = -\dfrac{1}{2}x^2 + 50x
$$

Så løser vi $A'(x) = 0$:

$$
A'(x) = -x + 50 = 0 \liff x = 50.
$$

Dermed vil $x = 50$ gi størst mulig areal. Derfor blir sidelengdene til hagen

$$
x = 50 \, \mathrm{m} \and y = \dfrac{100 - 50}{2} \, \mathrm{m} = 25 \, \mathrm{m}.
$$
::::::
:::::::


Vi får derfor størst mulig areal dersom sidelengdene til hagen er 

$$
x = 50 \, \mathrm{m} \and y = 25 \, \mathrm{m}.
$$


::::::::


:::::::::::::::


---

::::{admonition} Påminnelse: arealet til en trekant
---
class: margin, reminder
---
Arealet $A$ til en trekant er 

$$
A = \dfrac{g \cdot h}{2}
$$

der $g$ er grunnlinjen og $h$ er høyden til trekanten.
::::

:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-2
---
I {numref}`fig-polynomer-optimering-oppgave-3` vises grafen til andregradsfunksjon $f$ som er gitt ved

$$
f(x) = -x^2 + 9,
$$

der $D_f = [0, 3]$, og en trekant som har hjørner i punktene $(0, 0)$, $(2, 0)$ og $(2, f(2))$.

:::{figure} ./figurer/oppgaver/oppgave_3.svg
---
name: fig-polynomer-optimering-oppgave-3
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$ og en trekant med hjørner $(0, 0)$, $(2, 0)$ og $(2, f(2))$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet $A$ av trekanten.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
A = 5.
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Grunnlinjen i trekanten er $2$ og høyden er 

$$
f(2) = -2^2 + 9 = -4 + 9 = 5.
$$

Arealet av trekanten er derfor 

$$
A = \dfrac{2\cdot 5}{2} = 5. 
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
En annen trekant går gjennom punktene $(0, 0)$, $(k, 0)$ og $(k, f(k))$ der $k \in \langle 0, 3 \rangle$.

Bestem arealet $A(k)$ til trekanten.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(k) = \dfrac{1}{2}(-k^3 + 9k)
$$
:::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $k$ slik at arealet til trekanten blir størst mulig.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
k = \sqrt{3}. 
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme når arealet er størst mulig, finner vi løsningene til $A'(k) = 0$. Først deriverer vi $A(k)$ som gir

$$
A'(k) = \dfrac{1}{2}(-3k^2 + 9).
$$

Deretter løser vi $A'(k) = 0$:

$$
A'(k) = 0 \liff \dfrac{1}{2}(-3k^2 + 9) = 0 \liff -3k^2 + 9 = 0
$$

som gir 

$$
3k^2 = 9 \liff k^2 = 3 \liff k = \pm \sqrt{3}
$$

Men $k \in \langle 0, 3 \rangle$ som betyr at vi må velge den positive løsningen. Dermed vil verdien av $k$ som gir størst mulig areal være

$$
k = \sqrt{3}.
$$
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-2
---
I {numref}`fig-polynomer-optimering-oppgave-4` vises grafen til andregradsfunksjon $f$ gitt ved 

$$
f(x) = -x^2 + 36, \quad D_f = [-6, 6],
$$

og et fargelagt området med hjørner i punktene $(-4, 0)$, $(-4, f(-4))$, $(4, 0)$ og $(4, f(4))$. 



::::{figure} ./figurer/oppgaver/oppgave_4.svg
---
name: fig-polynomer-optimering-oppgave-4
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f(x) = -x^2 + 36$ og et fargelagt område med hjørner $(-4, 0)$, $(-4, f(-4))$, $(4, 0)$ og $(4, f(4))$.
::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet til det fargelagte området.

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
A = 80
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Det fargelagte området består av to trekanter som har høyde $4$ og grunnlinje $f(4) = f(-4)$ siden $f$ er en andregradsfunksjon som er symmetrisk om $x = 0$. Derfor er arealet av det fargelagte området:

\begin{align*}
    A &= \dfrac{4 \cdot f(4)}{2} \cdot \textcolor{red}{2} && \text{Ganger med 2 siden det er to trekanter} \\
    \\
    &= 4 \cdot f(4) \\
    \\
    &= 4 \cdot (-4^2 + 36) \\
    \\
    &= 4 \cdot (-16 + 36) \\
    \\
    &= 4 \cdot 20 \\
    \\
    &= 80.
\end{align*}

Arealet er derfor $A = 80$.
:::
:::::::::::::


:::::::::::::{tab-item} b
Det fargelagte området endres slik at har hjørner i $(-k, 0)$, $(-k, f(-k))$, $(k, 0)$ og $(k, f(k))$ der $k \in \langle 0, 4 \rangle$.

Bestem arealet $A(k)$ av det fargelagte området.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(k) = -k^3 + 36k.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Det fargelagte området består av to trekanter med grunnlinje $f(k)$ og høyde $k$. Arealet av det fargelagte området blir derfor 

$$
A(k) = \dfrac{kf(k)}{2}\cdot 2 = kf(k) = k(-k^2 + 36) = -k^3 + 36k.
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
Bestem $k$ slik at arealet av det fargelagte området blir størst mulig.


:::{admonition} Fasit
--- 
class: dropdown, answer
---
$$
k = 2\sqrt{3}
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
For å bestemme $k$ slik at arealet blir størst mulig, finner vi løsningene til $A'(k) = 0$. Først deriverer vi $A(k)$ som gir

$$
A'(k) = -3k^2 + 36.
$$

Deretter løser vi $A'(k) = 0$:

$$
A'(k) = 0 \liff -3k^2 + 36 = 0 \liff 3k^2 = 36 \liff k^2 = 12 
$$

Vi merker oss at 

$$
k^2 = 4\cdot 3 \liff k = \pm \sqrt{4 \cdot 3} = \pm \sqrt{4}\cdot \sqrt{3} = 2\sqrt{3}
$$

Vi husker på at $k \in \langle 0, 4 \rangle$ som betyr at vi må velge den positive løsningen. Dermed vil verdien av $k$ som gir størst mulig areal være

$$
k = 2\sqrt{3}
$$
:::


:::::::::::::


::::::::::::::


:::::::::::::::

---



:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
I {numref}`fig-polynomer-optimering-oppgave-5` vises grafen til tredjegradsfunksjon $f$ som er gitt ved

$$
f(x) = -x^3 + 4x^2,
$$

der $D_f = [0, 4]$, og en trekant som har hjørner i punktene $(1, 0)$, $(4, 0)$ og $(1, f(1))$. 

:::{figure} ./figurer/oppgaver/oppgave_5.svg
---
name: fig-polynomer-optimering-oppgave-5
width: 80%
class: no-click
---
viser grafen til en tredjegradsfunksjon $f$ og en trekant med hjørner $(1, 0)$, $(4, 0)$ og $(1, f(1))$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet $A$ av trekanten. 


:::{admonition} Fasit
---
class: dropdown, answer
---
$$
A = \dfrac{9}{2}
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Først kan vi observere at grunnlinjen er $4 - 1 = 3$ og høyden er

$$
f(1) = -1^3 + 4\cdot 1^2 = -1 + 4 = 3.
$$

Arealet $A$ til trekanten blir derfor

$$
A = \dfrac{3 \cdot f(1)}{2} = \dfrac{3 \cdot 3}{2} = \dfrac{9}{2}.
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
En annen trekant har hjørner i punktene $(a, 0)$, $(4, 0)$ og $(a, f(a))$ der  $a \in \langle 0, 4 \rangle$.

Bestem arealet $A(a)$ til trekanten.

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
A(a) = \dfrac{1}{2}(4 - a)(-a^3 + 4a^2). 
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
Grunnlinja til trekanten er $(4 - a)$ siden to av hjørnene er $(a, 0)$ og $(4, 0)$ og $a \in \langle 0, 4 \rangle$. Høyden til trekanten er $f(a)$. Derfor blir arealet $A(a)$ til trekanten

$$
A(a) = \dfrac{(4 - a)\cdot f(a)}{2} = \dfrac{(4 - a)(-a^3 + 4a^2)}{2} = \dfrac{1}{2}(4 - a)(-a^3 + 4a^2). 
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $a$ slik at arealet av trekanten blir størst mulig.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = 2
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme $a$ slik at arealet er størst mulig, finner vi løsningene til $A'(a) = 0$. For å finne den deriverte $A'(a)$ trenger vi først å gange ut $A(a)$:

\begin{align*}
    A(a) &= \dfrac{1}{2}(4 - a)(-a^3 + 4a^2) \\
    \\
    &= \dfrac{1}{2}\left(4\cdot(-a^3 + 4a^2) - a\cdot(-a^3 + 4a^2)\right) \\
    \\
    &= \dfrac{1}{2}\left(-4a^3 + 16a^2 + a^4 - 4a^3\right) \\
    \\
    &= \dfrac{1}{2}(a^4 - 8a^3 + 16a^2).
\end{align*}

Så deriverer vi $A(a)$:

$$
A'(a) = \dfrac{1}{2}(4a^3 - 24a^2 + 32a).
$$

Deretter løser vi $A'(a) = 0$:

$$
A'(a) = 0 \liff \dfrac{1}{2}(4a^3 - 24a^2 + 32a) = 0 \liff 4a^3 - 24a^2 + 32a = 0
$$

Vi kan faktorisere ut $4a$ fra tredjegradspolynomet som gir 

$$
4a(a^2 - 6a + 8) = 0
$$

som betyr at

$$
4a = 0 \or a^2 - 6a + 8 = 0
$$

Vi bruker $abc$-formelen på andregradspolynomet som gir:

$$
a = \dfrac{6 \pm \sqrt{6^2 - 4\cdot 1 \cdot 8}}{2\cdot 1} = \dfrac{6 \pm \sqrt{36 - 32}}{2} = \dfrac{6 \pm \sqrt{4}}{2} = \dfrac{6 \pm 2}{2} 
= 
\begin{cases}
    4 \\
    2
\end{cases}
$$

Altså er $A'(a) = 0$ hvis 

$$
a = 0 \or a = 2 \or a = 4.
$$

Både $a = 0$ og $a = 4$ gir $A(a) = 0$ som betyr at $a = 2$ gir det største mulige arealet.

::::

:::::::::::::
::::::::::::::
:::::::::::::::


---

:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-3
---
En fjerdegradsfunksjon $f$ er gitt ved 

$$
f(x) = -x(x - 3)^3, \quad D_f = [0, 3].
$$

En trekant har hjørnene $(0, 0)$, $(2, 0)$ og $(2, f(2))$.

:::{figure} ./figurer/oppgaver/oppgave_6.svg
---
name: fig-polynomer-optimering-oppgave-6
width: 80%
class: no-click
---
viser grafen til en fjerdegradsfunksjon $f(x) = -x(x - 3)^3$ og en trekant med hjørner $(0, 0)$, $(2, 0)$ og $(2, f(2))$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem arealet $A$ til trekanten. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
A = 2.
$$
:::

:::{admonition} Løsning 
---
class: dropdown, solution
---
Trekanten har grunnlinje $2$ og høyde 

$$
f(2) = -2\cdot (2 - 3)^3 = -2\cdot(-1)^3 = -2\cdot (-1) = 2.
$$

Dermed er arealet av trekanten 

$$
A = \dfrac{2\cdot f(2)}{2} =  \dfrac{2\cdot 2}{2} = 2. 
$$
:::

:::::::::::::

:::::::::::::{tab-item} b
En annen trekant har hjørnene $(0, 0)$, $(r, 0)$ og $(r, f(r))$ der $r \in \langle 0, 3 \rangle$.

Bestem arealet $A(r)$ til trekanten. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
A(r) = -\dfrac{1}{2}r^2(r - 3)^3
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Grunnlinjen til trekanten er $r$ og høyden er $f(r)$. Derfor er arealet $A(r)$ til trekanten

$$
A(r) = \dfrac{r\cdot f(r)}{2} = \dfrac{r\cdot (-r(r - 3)^3)}{2} = -\dfrac{1}{2}r^2(r - 3)^3.
$$
:::


:::::::::::::

:::::::::::::{tab-item} c
Bestem $r$ slik at arealet til trekanten blir størst mulig. 

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
r = \dfrac{6}{5}
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
For å bestemme $r$ slik at arealet blir størst mulig, finner vi løsningene til $A'(r) = 0$. For å bestemme $A'(r)$ må vi først gange ut $A(r)$:

\begin{align*}
    A(r) &= -\dfrac{1}{2}r^2(r - 3)^3 \\
    \\
    &= -\dfrac{1}{2}r^2(r - 3)(r - 3)^2 \\
    \\
    &= -\dfrac{1}{2}r^2(r - 3)(r^2 - 6r + 9) \\
    \\
    &= -\dfrac{1}{2}r^2(r^3 - 6r^2 + 9r - 3r^2 + 18r - 27) \\
    \\
    &= -\dfrac{1}{2}r^2(r^3 - 9r^2 + 27r - 27) \\
    \\
    &= -\dfrac{1}{2}(r^5 - 9r^4 + 27r^3 - 27r^2).
\end{align*}

Så finner vi $A'(r)$:

$$
A'(r) = -\dfrac{1}{2}(5r^4 - 36r^3 + 81r^2 - 54r).
$$

Deretter løser vi $A'(r) = 0$:

$$
A'(r) = 0 \liff -\dfrac{1}{2}(5r^4 - 36r^3 + 81r^2 - 54r) = 0
$$

som gir 

$$
5r^4 - 36r^3 + 81r^2 - 54r = 0 \liff r(5r^3 - 36r^2 + 81r - 54) = 0.
$$

som med produktregelen gir 

$$
r = 0 \or 5r^3 - 36r^2 + 81r - 54 = 0.
$$

Vi må nå angripe tredjegradslikningen ved å lete etter mulige kandidater for røtter $r$. Først kan vi observere at alle koeffisientene er hele tall og konstantleddet er $-54$. Da må alle røtter som er *hele tall* (dersom de finnes) være en faktor i $-54$. Det betyr at det er mulig at 

$$
r \in \{\pm 1, \pm 2, \pm 3\}
$$

løser tredjegradslikningen siden $-54 = -1\cdot 2\cdot 3^3$. Vi tester ut heltallene for å se noen om dem løser likningen:

$r = 1$:
: $5 - 36 + 81 - 54 = 5 - 36 + 81 - 54 = -4 \neq 0$

$r = -1$:
: $-5 - 36 - 81 + 54 = -5 - 36 - 81 + 54 = -68 \neq 0$

$r = 2$:
: $40 - 144 + 162 - 108 = 40 - 144 + 162 - 108 = -50 \neq 0$

$r = -2$:
: $-40 - 144 - 162 + 108 = -40 - 144 - 162 + 108 = -238 \neq 0$

$r = 3$:
: $135 - 324 + 243 - 54 = 135 - 324 + 243 - 54 = 0$

Dermed vil $r = 3$ være en løsning som betyr at vi kan skrive 

$$
5r^3 - 36r^2 + 81r - 54 = (r - 3)(ar^2 + br + c)
$$

for noen koeffisienter $a$, $b$ og $c$. Vi kan finne $a$, $b$ og $c$ ved å utføre polynomdivisjon:

:::{figure} ./koder/oppgaver/oppgave_6_løsning.svg
---
width: 80%
class: no-click
---
:::

som betyr at 

$$
5r^3 - 36r^2 + 81r - 54 = (r - 3)(5r^2 - 21r + 18) = 0
$$

som gir 

$$
r - 3 = 0 \or 5r^2 - 21r + 18 = 0
$$

Vi bruker $abc$-formelen på andregradspolynomet som gir:

$$
r = \dfrac{21 \pm \sqrt{21^2 - 4\cdot 5 \cdot 18}}{2\cdot 5} = \dfrac{21 \pm \sqrt{441 - 360}}{10} = \dfrac{21 \pm \sqrt{81}}{10} = \dfrac{21 \pm 9}{10}
$$

Dermed er 

$$
r = \dfrac{21 + 9}{10} = \dfrac{30}{10} = 3 \or r = \dfrac{21 - 9}{10} = \dfrac{12}{10} = \dfrac{6}{5}.
$$

Vi kan merke oss at $r \in \langle 0, 3 \rangle$ som betyr at den eneste løsningen som er innenfor dette intervallet er 

$$
r = \dfrac{6}{5}, 
$$

som gir det største mulige arealet til trekanten.


::::





:::::::::::::

::::::::::::::

:::::::::::::::
