# Funksjoner (Del 1)

> Oppgavene skal løses **uten hjelpemidler**.

:::::::::::::::{admonition} Oppgave 1 (Vår 2023)
---
class: exercise
---
Funksjonen $f$ er gitt ved 

$$
f(x) = x^2 - 2x - 8.
$$

I hvilke punkter skjærer grafen til funksjonen $x$-aksen?

::::{admonition} Fasit
---
class: answer, dropdown
---
Grafen til $f$ skjærer gjennom $x$-aksen i $x = -2$ og $x = 4$. 
::::



::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker $abc$-formelen til å bestemme når $f(x) = 0$: 

$$
x = \dfrac{-(-2) \pm \sqrt{(-2)^2 + 4\cdot 8}}{2} = \dfrac{2 \pm \sqrt{36}}{2} = \dfrac{2 \pm 6}{2} = 1\pm 3
$$

som betyr at 

$$
x = 4 \or x = -2. 
$$

Dermed skjærer grafen til $f$ gjennom $x$-aksen i $x = -2$ og $x = 4$. 
::::




:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 2 (Høst 2023)
---
class: exercise
---
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 + 2x^2 - 5x - 6
$$

I hvilke punkter skjærer grafen til funksjonen $x$-aksen?

::::{admonition} Fasit
---
class: answer, dropdown
---
Grafen til $f$ skjærer gjennom $x$-aksen i $x = -1$, $x = 2$ og $x = -3$.
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må bestemme hvilke $x$ som medfører at $f(x) = 0$. Først kan vi lete etter et heltallige nullpunkter $x$ som deler konstantleddet i $f(x)$. Kandidater for dette er 

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}.
$$

Vi tester ut verdiene systematisk til vi får $f(x) = 0$:

\begin{align*}
    f(1) &= 1^3 + 2\cdot 1^2 - 5\cdot 1 - 6 = 1 + 2 - 5 - 6 = -8 \\
    \\
    f(-1) &= (-1)^3 + 2\cdot (-1)^2 - 5\cdot (-1) - 6 = -1 + 2 + 5 - 6 = 0 \\
\end{align*}

dermed finner vi at $f(-1) = 0$ som betyr at $(x + 1) | f(x)$, det vil si $(x + 1)$ er en faktor av $f(x)$. Vi kan utføre polynomdivisjon for å faktorisere $f(x)$: 

:::{figure} ./koder/oppgave_2/polydiv.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Så må vi finne røttene til $(x^2 + x - 6)$ som vi gjør med $abc$-formelen:

$$
x = \dfrac{-1 \pm \sqrt{1^2 + 4\cdot 6}}{2} = \dfrac{-1 \pm \sqrt{25}}{2} = \dfrac{-1 \pm 5}{2}
$$

som gir 

$$
x = 2 \or x = -3.
$$

Dermed skjærer grafen til $f$ gjennom $x$-aksen i $x = -1$, $x = 2$ og $x = -3$.


::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 3 (Høst 2023)
---
class: exercise
---
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 - x + 4
$$

Bestem likningen for tangenten til grafen til $f$ i punktet $(1, f(1))$.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -4x + 5.
$$
::::

::::::::{admonition} Løsning
---
class: solution, dropdown
---
:::::::{tab-set}
::::::{tab-item} Strategi 1: Den deriverte
Tangenten går gjennom punktet $(1, f(1))$ som har $y$-koordinat:

$$
f(1) = 1^3 - 3\cdot 1^2 - 1 + 4 = 1 - 3 - 1 + 4 = 1.
$$

Videre er stigningstallet til tangenten $a = f'(1)$ som vi finner ved å derivere $f(x)$:

$$
f'(x) = 3x^2 - 6x - 1
$$

som gir 

$$
a = f'(1) = 3\cdot 1^2 - 6\cdot 1 - 1 = 3 - 6 - 1 = -4.
$$

Ved ettpunktsformelen finner vi likningen til tangenten:

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - 1 &= -4(x - 1) \\
    \\
    y - 1 &= -4x + 4 \\
    \\
    y &= -4x + 5.
\end{align*}

som er likningen for tangenten. 

::::::


::::::{tab-item} Strategi 2: Polynomdivisjon
Vi utfører polynomdivisjonen $f(x) : (x - 1)^2$ og leser av resten i polynomdivisjonen som vil være uttrykket til tangenten:

:::{figure} ./koder/oppgave_3/polydiv.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi kan lese av at resten er $-4x + 5$ som betyr at likningen til tangenten er 

$$
y = -4x + 5.
$$

::::::

:::::::
::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 4 (Høst 2023)
---
class: exercise
---
Funksjonen $f$ og $g$ er gitt ved 

$$
f(x) = \dfrac{2x - 8}{x + 2} \quad \quad \quad g(x) = \dfrac{x^2 - 4}{(x - 3)(x + 3)}
$$


Nedenfor vises seks grafer. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvilke av grafene nedenfor er grafen til $f$?


::::{admonition} Fasit
---
class: answer, dropdown
---
Graf C. 
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan skrive om $f(x)$ til 

$$
f(x) = \dfrac{2(x - 4)}{x + 2}
$$

som betyr at $f$ har
* En horisontal asymptote $y = 2$
* En vertikal asymptote $x = -2$
* Et nullpunkt $x = 4$

Graf C er den eneste grafen som har en horisontal aysmptote $y > 0$, en vertikal asymptote $x < 0$ og et nullpunkt $x > 0$. Dermed er graf C grafen til $f$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Hvilke av grafene nedenfor er grafen til $g$? 


::::{admonition} Fasit
---
class: answer, dropdown
---
Graf F. 
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan bruke konjugatsetningen til å skrive om $g(x)$ til

$$
g(x) = \dfrac{(x + 2)(x - 2)}{(x - 3)(x + 3)}
$$

Vi kan merke oss at $g(x)$ har ingen felles faktorer i teller og nevner som betyr at 

$$
g(x) = 0 \liff (x + 2)(x - 2) = 0 \liff x = -2 \or x = 2
$$

som betyr at $g$ har to nullpunkter $x = -2$ og $x = 2$.

Siden teller og nevnerpolynomet til $g$ har samme grad, og ledende koeffisient for begge polynomer er $1$, må den horisontale asymptoten til $g$ være $y = 1$. 

Til slutt har nevnerpolynomet i $g(x)$ nullpunktene $x = \pm 3$ som blir $g$ sine vertikale asymptoter. 

Det er bare **graf F** som passer med egenskapene til $g$ fordi
1. Avstanden fra $y$-aksen til hvert nullpunkt er like stor. Dette er ikke tilfelle i graf D (som ikke har nullpunkter).
2. Avstanden fra $y$-aksen til hver vertikal asymptote er like stor. Dette er ikke tilfelle i graf E der avstanden til den éne asymptoten er større enn avstanden til den andre (fra $y$-aksen). 
3. Den horisontale asymptoten er en konstant linje $y = k$ der $k > 0$. Dette stemmer ikke for graf D.


Graf A, B og C har alle sammen bare én vertikal asymptote og er automatisk eliminert fra lista over kandidater.

::::

:::::::::::::

::::::::::::::


:::{clickable-figure} ./figurer/oppgave_4/merged_figure.svg
---
width: 100%
---
:::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 5 (Vår 2023)
---
class: exercise
---
Gitt likningen 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x + a)(x - b).
$$


Bestem $a$ og $b$ slik at likningen blir en identitet.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
(a = -6 \and b = -2) \or (a = 2 \and b = 6).
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi utfører polynomdivisjon for å få et andregradspolynom vi kan faktorisere:

:::{figure} ./koder/oppgave_5/polydiv.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså kan vi faktorisere tredjegradspolynomet som 

$$
x^3 - 5x^2 - 8x + 12 = (x - 1)(x^2 - 4x + 12)
$$


Vi må bestemme røttene til andregradspolynomet for å bestemme $a$ og $b$. 

$$
x = \dfrac{4 \pm \sqrt{16 + 4\cdot 12}}{2} = \dfrac{4 \pm \sqrt{64}}{2} = \dfrac{4 \pm 8}{2} = 2 \pm 4
$$

som gir 

$$
x = 6 \or x = -2.
$$

Dette betyr at 

$$
x^2 - 4x + 12 = (x + a)(x - b) = (x - 6)(x + 2) = (x + 2)(x - 6)
$$

som betyr at likningen er en identitet hvis

$$
(a = -6 \and b = -2) \or (a = 2 \and b = 6).
$$

::::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 6 (Vår 2023)
---
class: exercise
---
Nedenfor ser du grafen til en rasjonal funksjon $f$.

Bestem $f(x)$. 

Husk å argumentere for at svaret ditt er riktig.


:::{figure} ./figurer/oppgave_6/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = \dfrac{3(x - 2)}{x - 1} = \dfrac{3x - 6}{x - 1}
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Grafen til $f$ passer med en rasjonal funksjon der teller- og nevnerpolynomet er lineære polynomer. Da kan vi skrive $f(x)$ på formen

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

der 

* $y = a$ er den horisontale asymptoten
* $x = b$ er nullpunktet til $f$
* $x = c$ er den vertikale asymptoten til $f$


Fra grafen til $f$ kan vi lese av at 

* den horisontale asymptoten er $y = 3$.
* nullpunktet er $x = 2$.
* den vertikale asymptoten er $x = 1$.

Dermed er 

$$
f(x) = \dfrac{3(x - 2)}{x - 1} = \dfrac{3x - 6}{x - 1}
$$
::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 7 (Vår 2024)
---
class: exercise
---
I figuren nedenfor vises grafen til en funksjon $f$. 

:::{figure} ./figurer/oppgave_7/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f(x)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -2(x + 3)(x - 4)
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi skriver $f(x)$ på nullpunktsform siden vi kan lese av begge nullpunktene til $f$ som gir:

$$
f(x) = a(x + 3)(x - 4)
$$

Siden grafen til $f$ går gjennom $(0, 24)$, betyr det at 

\begin{align*}
    f(0) &= 24 \\
    \\
    a(0 + 3)(0 - 4) &= 24 \\
    \\
    a\cdot 3 \cdot (-4) &= 24 \\
    \\
    -12a &= 24 \\
    \\
    a &= -2
\end{align*}

Dermed er $f(x)$ gitt ved 

$$
f(x) = -2(x + 3)(x - 4)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten $f(x) > 12$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -2, 3 \rangle
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Ulikheten $f(x) > 12$ er gitt ved 

$$
-2(x + 3)(x - 4) > 12
$$

For å løse ulikheten, ganger vi ut venstresiden og samler alle ledd på én side så vi får

\begin{align*}
    -2(x + 3)(x - 4) &> 12 \\
    \\
    -2(x^2 - x - 12) &> 12 \\
    \\
    -2x^2 + 2x + 24 &> 12 \\
    \\
    -2x^2 + 2x + 12 &> 0 \\
    \\
    2x^2 - 2x - 12 &< 0 \\
    \\
    x^2 - x - 6 &< 0 \\
    \\
    (x - 3)(x + 2) &< 0
\end{align*}

der vi har brukt at $(x - 3)(x + 2) = x^2 - x - 6$. Vi tegner et fortegnsskjema for $g(x) = (x - 3)(x + 2)$ og leser av når $g(x) < 0$. Løsningen vil være ekvivalent med løsningen av $f(x) > 12$. 

:::{figure} ./figurer/oppgave_7/fortegnsskjema.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Fra fortegnslinja til $g(x)$ har vi at 

$$
g(x) < 0 \liff x \in \langle -2, 3 \rangle \liff f(x) > 12. 
$$

::::

:::::::::::::

::::::::::::::



:::::::::::::::

---



:::::::::::::::{admonition} Oppgave 8 (Vår 2024)
---
class: exercise 
---
Sett opp en matematisk identitet med utgangspunkt i arealet av det grønne fargelagte området.

:::{figure} ./figurer/oppgave_8/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a^2 - b^2 = (a + b)(a - b)
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan skrive arealet av det grønne fargelagte området som 

$$
\mathrm{areal} = a^2 - b^2
$$

ved å ta arealet av det store kvadratet med sidelenger $a$ og trekke fra det lille hvite kvadratet med sidelengde $b$.

Men vi kan også skrive arealet av det grønne fargelagte området direkte:

$$
\mathrm{areal} = a \cdot (a - b) + b \cdot (a - b) = (a + b)(a - b)
$$

Dermed er 

$$
a^2 - b^2 = (a + b)(a - b)
$$
::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 9 (Vår 2024)
---
class: exercise
---
Guri har utført to ulike polynomdivisjoner og påstår begge divisjonene viser at faktoriseringen nedenfor er riktig.

$$
2x^3 + 3x^2 - 11x - 6 = (2x^2 + 7x + 3)\cdot (x - 2)
$$


Hvilke to polynomdivisjoner kan hun ha utført?

Utfør de to polynomdivisjonene, og forklar at hver av dem viser at faktoriseringen er riktig.


::::{admonition} Løsning
---
class: solution, dropdown
---
Guri kan ha utført polynomdivisjonen:

:::{figure} ./koder/oppgave_9/polydiv1.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

eller hun kan ha utført polynomdivisjonen:

:::{figure} ./koder/oppgave_9/polydiv2.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra begge divisjonene følger det at 

$$
2x^3 + 3x^2 - 11x - 6 = (2x^2 + 7x + 3)\cdot (x - 2)
$$

::::


:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 10 (Høst 2024)
---
class: exercise
---
Funksjonen $f$ er gitt ved 

$$
f(x) = (x - 1)(x + 3).
$$


Bestem koordinatene til bunnpunktet på grafen til $f$.


::::{admonition} Fasit
---
class: answer, dropdown
---
Bunnpunktet er $(-1, -4)$. 
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Symmetrilinja til $f$ kan vi bestemme ved gjennomsnittet av nullpunktene som gir

$$
x_0 = \dfrac{(-3) + 1}{2} = \dfrac{-2}{2} = -1.
$$

$y$-koordinaten til punktet finner vi derfor med $f(-1)$ som gir

$$
f(-1) = (-1 - 1)\cdot (-1 + 3) = (-2)\cdot (2) = -4.
$$

Altså er bunnpunktet $(-1, -4)$. 
::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 11 (Høst 2024)
---
class: exercise 
---
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 + 7x^2 + 4x - 12
$$

Løs ulikheten $f(x) < 0$ og illustrer løsningen grafisk ved å lage en skisse.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle \gets , -6 \rangle \cup \langle -2, 1 \rangle
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må nullpunktsfaktorisere $f(x)$ for å løse ulikheten. Først leter vi etter et heltallig nullpunkt ved å prøve ut verdier av $x$ som deler konstantleddet i $f(x)$. Kandidatene for dette er 

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6, \pm 12\}. 
$$

Vi prøver oss fram systematisk frem til vi får $f(x) = 0$: 

$$
f(1) = 1^3 + 7\cdot 1^2 + 4\cdot 1 - 12 = 1 + 7 + 4 - 12 = 0
$$

Altså er $x = 1$ et nullpunkt til $f$ som betyr at $(x - 1) | f(x)$. Vi utfører polynomdivisjonen $f(x) : (x - 1)$ for å faktorisere $f(x)$ fullstendig: 

:::{figure} ./koder/oppgave_11/polydiv.svg
---
width: 90%
class: no-click, adaptive-figure
---
:::

Vi anvender $abc$-formelen på $x^2 + 8x + 12$ for å finne de andre nullpunktene:

$$
x = \dfrac{-8 \pm \sqrt{8^2 - 4\cdot 12}}{2} = \dfrac{-8 \pm \sqrt{16}}{2} = \dfrac{-8 \pm 4}{2} = -4 \pm 2
$$

som gir

$$
x = -2 \or x = -6.
$$

Altså kan vi skrive $f(x)$ som 

$$
f(x) = (x + 6)(x + 2)(x - 1).
$$

For å løse en ulikheten $f(x) < 0$ tegner vi et fortegnsskjema for $f(x)$: 

:::{figure} ./figurer/oppgave_11/fortegnsskjema.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi kan lese av fra fortegnsslinja til $f(x)$ at 

$$
f(x) < 0 \liff x \in \langle \gets , -6 \rangle \cup \langle -2, 1 \rangle
$$


Vi kan illustrere løsningen grafisk ved å lage en skisse av grafen til $f$ og markere områdene der $f(x) < 0$ med rødt.


:::{figure} ./figurer/oppgave_11/skisse.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 12 (Høst 2022)
---
class: exercise
---
Grafen til en andregradsfunksjon $f$ er vist nedenfor. 

:::{figure} ./figurer/oppgave_12/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Om andregradsfunksjonen $f$ får du vite at 

* Tangenten i punktet $(-2, 0)$ har likningen $y = 9x + 18$
* Tangenten i punktet $(8, -10)$ har likningen $y = -11x + 78$


Bestem $f'(x)$. 


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f'(x) = -2x + 5. 
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Siden $f$ er en andregradsfunksjon, betyr det at $f'$ er en lineær funksjon

$$
f'(x) = ax + b.
$$

Vi vet også at stigningstallet til tangenter til grafen til $f$ i $(x, f(x))$, har samme verdi som den momentane vekstfarten $f'(x)$ i punktet. Likningen til tangenten i punktet $(-2, 0)$ er gitt ved $y = 9x + 18$ som betyr at stigningstallet til tangenten er $9$. 

\begin{align*}
    f'(-2) &= 9 \\
    \\
    a\cdot (-2) + b &= 9 \\
    \\
    -2a + b &= 9
\end{align*}

Likningen til tangenten i punktet $(8, -10)$ er gitt ved $y = -11x + 78$ som betyr at stigningstallet til tangenten er $-11$. Da følger det at 

\begin{align*}
    f'(8) &= -11 \\
    \\
    a\cdot 8 + b &= -11 \\
    \\
    8a + b &= -11
\end{align*}

Siden den deriverte er en lineær funksjon, kan vi bestemme stigningstallet til $f'(x)$ ved å bruke topunktsformelen fremfor å gå løs på likningssystemet. Da får vi:

$$
a = \dfrac{f'(8) - f'(-2)}{8 - (-2)} = \dfrac{-11 - 9}{10} = \dfrac{-20}{10} = -2.
$$

Så setter vi inn verdien for $a$ i én av likningene vi har funnet:

$$
8 \cdot (-2) + b = -11 \liff -16 + b = -11 \liff b = 5.
$$

Dermed er 

$$
f'(x) = -2x + 5. 
$$


::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 13 (Høst 2022)
---
class: exercise
---
Funksjonen $f$ er gitt ved

$$
f(x) = (x - 4)(x - 2)(x + 4)
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvilken av grafene nedenfor kan være grafen til $f$? 

Husk å argumentere for svaret ditt.


:::{clickable-figure} ./figurer/oppgave_13/merged_figure.svg
---
width: 100%
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
Graf A
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan sjekke skjæringen med $y$-aksen for å se om vi kan eliminere graf $C$:

$$
f(0) = (0 - 4)\cdot(0 - 2)\cdot(0 + 4) = (-4)\cdot(-2)\cdot(4) = 32.
$$

Graf C skjærer $y$-aksen når $y < 0$ som betyr at det ikke kan være grafen til $f$.

Fra $f(x)$ kan vi hente ut at 

$$
f(x) = 0 \liff x = \pm 4 \or x = 2.
$$

Det betyr at to av nullpunktene er symmetrisk fordelt om $y$-aksen, og at ett nullpunkt må ligge *mellom* to de som er symmetrisk fordelt. Vi kan se at graf B ikke oppfyller kravet siden det er et nullpunkt som ligger på oversiden av de to som ligger symmetrisk fordelt om $y$-aksen. Graf A derimot oppfyller kravet og er derfor grafen til $f$. 
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs

$$
(x - 4)(x - 2)(x + 4) > 0
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -4, 2 \rangle \cup \langle 4, \to \rangle.
$$
::::


::::{admonition} Løsning
---
class: solution, dropdown
---
Løsningen av ulikheten 

$$
(x - 4)(x - 2)(x + 4) > 0 \liff f(x) > 0
$$

Dermed kan vi lese av fra graf A hvor $f(x) > 0$. Dette kan vi observere er når 

$$
x \in \langle -4, 2 \rangle \cup \langle 4, \to \rangle.
$$
::::

:::::::::::::

::::::::::::::




:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 14 (Vår 2022)
---
class: exercise
---
Bestem $r$ og $s$ slik at sammenhengen nedenfor blir en identitet

$$
9x^2 - 30x + r = (3x - s)^2
$$


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
s = 5 \and r = 25.
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi ganger ut høyresiden:

$$
(3x - s)^2 = 9x^2 - 6sx + s^2
$$

Så setter vi de lik hverandre som gir:

\begin{align*}

    9x^2 - 30x + r &= 9x^2 - 6sx + s^2 \\
    \\
    -30x + r &= -6sx + s^2
\end{align*}

Sammenligner vi koeffisientene til $x$ og konstantleddene, får vi to likninger som må være oppfylt uavhengig av verdien til $x$:

\begin{align*}
    -30 &= -6s \\
    \\
    r &= s^2
\end{align*}

Fra den første likningen får vi at $s = 5$. Setter vi inn verdien til $s$ i den andre likningen, får vi at

$$
r = 5^2 = 25.
$$

Dermed er sammenhengen en identitet hvis

$$
s = 5 \and r = 25.
$$
::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 15 (Vår 2022)
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen 

$$
(x - 2)(x + 1) = 0
$$

:::::::::::::


:::::::::::::{tab-item} b
Sett opp en ulikhet som har løsning $x \in \langle \gets, -1 \rangle \cup \langle 2, \to \rangle$.

Husk å begrunne svaret.

:::::::::::::

::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 16 ( )
































