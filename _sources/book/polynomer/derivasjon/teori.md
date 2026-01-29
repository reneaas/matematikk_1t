# Den deriverte

:::{admonition} Læringsmål
---
class: tip
---
* Kunne derivere polynomfunksjoner algebraisk.
* Kunne bestemme likningen til tangenter til polynomfunksjoner.
* Kan beskrive sammenhengen mellom grafen til $f$ og grafen til $f'$.
:::


## Den deriverte til en polynomfunksjon
Når vi fant den deriverte $f'$ til en andregradsfunksjon $f$, så fant vi at den deriverte var en lineær funksjon. Sagt på en annen måte: vi får et førstegradspolynom $f'(x)$ når vi finner den deriverte av et andregradspolynom $f(x)$. Dette var ikke bare et sammentreff – generelt sett vil $f'(x)$ være et polynom som har én grad lavere for et hvert polynom $f(x)$.


:::::::::::::::{summary} Den deriverte til en polynomfunksjon
Gitt et polynom $f(x)$ av grad $n$, vil den deriverte av polynomet $f'(x)$ være et polynom av grad $n - 1$. 

:::::::::::::::

I praksis kan vi finne den deriverte algebraisk ved å følge noen bestemte regneregler som gjelder for alle polynomer.


:::::::::::::::{summary} Derivasjonsregler for polynomer
Regel 1
: For et ledd $x^n$ i et polynom $f(x)$, vil den deriverte av leddet være

$$
(x^n)' = n \cdot x^{n-1}
$$

Regel 2
: For ethvert ledd $a x^n$ i et polynom $f(x)$, vil den deriverte av leddet være

$$
(a x^n)' = a (x^n)'
$$

Regel 3
: Hvert ledd i et polynom deriveres hver for seg:

$$
(ax^n + bx^m)' = (ax^n)' + (bx^m)'
$$

Regel 4
: Den deriverte av en konstant er null:

$$
C' = 0
$$

Regel 5
: Den deriverte av et lineært ledd $ax$ er 

$$
(ax)' = a
$$
:::::::::::::::

---

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Bestem den deriverte til 

$$
f(x) = 2x^3 - 4x^2 + 6x - 2
$$

::::{admonition} Løsning
---
class: solution
---
\begin{align*}
    f'(x) &= (2x^3 - 4x^2 + 6x - 2)' \\
    \\
    &= 2\cdot (x^3)' - 4\cdot (x^2)' + 6\cdot x' - 2' \\
    \\
    &= 2 \cdot 3\cdot x^2 - 4\cdot 2 \cdot x^1 + 6 \cdot 1 \cdot x^0 - 0 \\
    \\
    &= 6x^2 - 8x + 6
\end{align*}
::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
Bestem den deriverte til 

$$
f(x) = x^4 - 3x^2 + 5x - 1
$$

::::{answer}
$$
f'(x) = 4x^3 - 6x + 5
$$
::::

:::::::::::::::


## Likningen til en tangent

:::{plot}
width: 100%
align: right
function: (x - 1) * (x + 2) * (x + 1), f
ymax: 3
ymin: -3
xmax: 3
xmin: -4
point: (0.75, f(0.75))
text: 0.75, f(0.75), "$(a, f(a))$", bottom-right
tangent: 0.75, f
ticks: off
fontsize: 30
:::



Hvis vi ser på en tangent til grafen til $f$ i et punkt $(a, f(a))$, så vet vi to ting:

1. Tangenten går gjennom punktet $(a, f(a))$.
2. Stigningstallet til tangenten er lik $f'(a)$. 

Vi vet også at vi alltid kan skrive likningen til en linje som har stigningstall $m$ som går gjennom et punkt $(x_0, y_0)$ på ettpunktsform: 

$$
y = m(x - x_0) + y_0,
$$

Siden vi vet at stigningstallet er $f'(a)$ så vet vi at $m = f'(a)$. Siden linjen går gjennom punktet $(a, f(a))$, så vet vi at $x_0 = a$ og $y_0 = f(a)$. Dermed kan vi skrive likningen til tangenten som

$$
y = f'(a)(x - a) + f(a).
$$


:::::::::::::::{summary} Likningen til en tangent
Likningen til en tangent til grafen til $f$ i et punkt $(a, f(a))$ er gitt ved 

$$
y = f'(a)(x - a) + f(a)
$$
:::::::::::::::



---


:::::::::::::::{example} Eksempel 2
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 - 4x + 12.
$$

Bestem likningen til tangenten til grafen til $f$ i punktet $(1, f(1))$.

::::{solution}
---
dropdown: 0
---
Likningen til tangenten er gitt ved 

$$
y = f'(1)(x - 1) + f(1)
$$

Vi har at 

$$
f(1) = 1^3 - 3\cdot 1^2 - 4\cdot 1 + 12 = 6
$$

Videre har vi at 

$$
f'(x) = (x^3 - 3x^2 - 4x + 12)' = 3x^2 - 6x - 4
$$

som gir

$$
f'(1) = 3\cdot 1^2 - 6\cdot 1 - 4 = -7
$$

Setter vi dette inn i likningen for tangenten, så får vi

$$
y = -7(x - 1) + 6 = -7x + 7 + 6 = -7x + 13
$$
::::
:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 2
En funksjon $f$ er gitt ved 

$$
f(x) = x^3 + 2x^2 - x + 1.
$$

Bestem likningen til tangenten til grafen til $f$ i punktet $(2, f(2))$.


::::{answer}
$$
y = 19x - 23
$$
::::

::::{solution}
Likningen til tangenten er 

$$
y = f'(2)(x - 2) + f(2)
$$

Vi har at 

$$
f(2) = 2^3 + 2\cdot 2^2 - 2 + 1 = 15
$$

Videre har vi at

$$
f'(x) = (x^3 + 2x^2 - x + 1)' = 3x^2 + 4x - 1
$$

som gir

$$
f'(2) = 3\cdot 2^2 + 4\cdot 2 - 1 = 12 + 8 - 1 = 19
$$

Setter vi dette inn i likningen for tangenten, så får vi

$$
y = 19(x - 2) + 15 = 19x - 38 + 15 = 19x - 23
$$
::::
:::::::::::::::









## Sammenheng mellom $f(x)$ og $f'(x)$

Vi har allerede nevnt at grafen til den deriverte $f'$ vil være en polynomfunksjon av én grad lavere enn $f$. Men vi kan peke ut flere sammenhenger som er viktig å forstå for å anvende teorien i praksis. 

### Ekstremalpunkter til $f$ og nullpunkter til $f'$

La oss forestille oss at vi har en tredjegradsfunksjon $f$. Da vil $f'$ være en andregradsfunksjon. La oss tegne tangenter til grafen til $f$ i ekstremalpunktene til $f$. Da får vi tangenter som er horisontale og dermed har stigningstall $0$. Dette vil derfor være punkter hvor $f'(x) = 0$. Altså punkter hvor grafen til $f'$ skjærer $x$-aksen. Se figuren nedenfor.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
width: 100%
function: 1/3 * x**3 + 1/2 * x**2 - 6 * x - 3, f
ymax: 20
ymin: -20
xmin: -10
xmax: 10
ticks: off
tangent: -3, f
tangent: 2, f
point: (-3, f(-3))
text: -3, f(-3), "$(a, f(a))$", top-center
point: (2, f(2))
text: 2, f(2), "$(b, f(b))$", bottom-center
fontsize: 26
:::

:::{plot}
function: x**2 + x - 6, f'
xmin: -8
xmax: 8
ymax: 15
ymin: -15
ticks: off
fontsize: 26
point: (-3, 0)
text: -3, 0, "$(a, 0)$", bottom-left
point: (2, 0)
text: 2, 0, "$(b, 0)$", bottom-right
:::


::::


Men det finnes også polynomfunksjoner som har punkter hvor tangenten blir horisontal, men punktet er verken et toppunkt eller et bunnpunkt. I figuren nedenfor viser vi en femtegradsfunksjon $f$ og dens deriverte $f'$ som er en fjerdegradsfunksjon. Vi ser at grafen til $f$ har to ekstremalpunkter, men det er et punkt hvor grafen til $f$ ikke snur, men hvor tangenten likevel er horisontal. Dette punktet kaller vi i stedet for et **terrassepunkt**.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
function: 1/5 * x**5 - 3/4 * x**4 - x**3 + 11/2 * x**2 - 6*x - 5, f
ymax: 25
ymin: -25
xmax: 5
xmin: -4
ticks: off
point: (-2, f(-2))
point: (1, f(1))
point: (3, f(3))
tangent: 1, f, dashed, red
:::

:::{plot}
function: x**4 - 3*x**3 - 3 * x**2 + 11*x - 6, f'
ymax: 25
ymin: -25
xmax: 5
xmin: -4
ticks: off
point: (-2, 0)
point: (1, 0)
point: (3, 0)
:::

::::




:::::::::::::::{admonition} Sammenheng mellom $f(x)$ og $f'(x)$
---
class: summary
---
La $f$ være en polynomfunksjon. Da vil følgende sammenhenger mellom grafene til $f$ og $f'$ gjelde:
* Punkter hvor grafen til $f'$ skjærer $x$-aksen svarer til punkter på grafen til $f$ hvor tangenter har stigningstall $0$.
* Punkter hvor $f'(x) = 0$, svarer til punkter på grafen til $f$ hvor tangenter har stigningstall $0$. 
* Grafen til $f$ stiger når $f'(x) > 0$.
* Grafen til $f$ synker når $f'(x) < 0$.
:::::::::::::::


Ut ifra sammenhengen over, vil det i mange tilfeller være slik at punkter hvor grafen til $f'$ skjærer $x$-aksen, så har grafen til $f$ et ekstremalpunkt.

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Grafen til en tredjegradsfunksjon $f$ er vist i {numref}`fig-polnyomfunksjoner-derivasjon-eksempel-2`.


:::{figure} ./figurer/eksempler/eksempel_2/graf.svg
---
name: fig-polnyomfunksjoner-derivasjon-eksempel-2
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en tredjegradsfunksjon $f$
:::

For å forstå hvordan grafen til $f'$ henger sammen med grafen til $f$ kan vi 
1. Tegne en fortegnslinje for $f'(x)$. 
2. Tegne grafen til $f'$ ved å bruke fortegnslinjen og passe på at nullpunktene til $f'$ svarer til ekstremalpunktene til $f$.

::::::::::::::{tab-set}
:::::::::::::{tab-item} Fortegnslinje til $f'(x)$

:::{figure} ./figurer/eksempler/eksempel_2/fortegnslinje.svg
---
name: fig-polnyomfunksjoner-derivasjon-eksempel-2-fortegnslinje
width: 100%
class: no-click, adaptive-figure
---
viser fortegnslinja til $f'(x)$. Sammenhengen med grafen til $f$ er at $f'(x) > 0$ når grafen til $f$ stiger og $f'(x) < 0$ når grafen til $f$ synker. I ekstremalpunktene til $f$ er $f'(x) = 0$ fordi en tangent gjennom punktet vil være horisontal og dermed ha stigningstall $0$.
:::

:::::::::::::


:::::::::::::{tab-item} Grafen til $f'$

:::{figure} ./figurer/eksempler/eksempel_2/f_derivert.svg
---
name: fig-polnyomfunksjoner-derivasjon-eksempel-2-f-derivert
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f'$. Nullpunktene til $f'$ svarer til samme $x$-koordinater som ekstremalpunktene til $f$.
:::

:::::::::::::


::::::::::::::

:::::::::::::::

---





## Utledning av derivasjonsreglene (*)

Vi har så langt bare påstått hva derivasjonsreglene for polynomer er. Her skal vi gå løs på å utlede én av reglene.

$$
\dfrac{f(x) - f(a)}{x - a}
$$


:::::::::::::::{theory} Bevis for derivasjonsregel 1
La $f(x) = x^3$ være en tredjegradsfunksjon. Vi ønsker å finne den deriverte $f'(a)$ i et punkt $(a, f(a))$ på grafen til $f$.

Vi starter med å finne den gjennomsnittlige vekstfarten til $f$ i intervallet $[a, x]$. Dette er gitt ved 

$$
\dfrac{f(x) - f(a)}{x - a} = \dfrac{x^3 - a^3}{x - a}
$$

Vi utfører polynomdivisjonen med et Horner-skjema:

:::{horner}
---
p: x^3 - a^3
x: a
width: 50%
---
:::

Vi får null i rest, og bare en kvotient:

$$
\dfrac{f(x) - f(a)}{x - a} = x^2 + ax + a^2
$$

Hvis vi nå tenker oss at vi lar punktet $(x, f(x))$ nærme seg punktet $(a, f(a))$. Da vil jo sekanten som går gjennom de punktene nærme seg en tangent i punktet $(a, f(a))$. Den gjennomsnittlige vekstfarten vil da nærme seg stigningstallet til tangenten fordi de to linjene blir gradvis mer og mer like. 

Setter vi $x = a$ i uttrykket, som svarer til å se at vi lar $(x, f(x))$ komme så nærme $(a, f(a))$ som overhode mulig, så får vi 

$$
a^2 + a\cdot a + a^2 = 3a^2
$$

Altså blir stigningstallet til tangenten $3a^2$. 





:::::::::::::::




## Polynomdivisjon og tangenter (*)

Vi har allerede sett at resten i polynomdivisjon med $f(x) : (x - r)$ lar oss bestemme $f(r)$. Her skal vi gå et steg videre å se at resten i en bestemt polynomdivisjon kan brukes til å bestemme likningen til en tangent til grafen til polynomfunksjonen.


:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = x^2 - 4x + 5.
$$



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem likningen for tangenten til grafen til $f$ i $(1, f(1))$ ved å bruke at $f'(x) = 2ax + b$ for en andregradsfunksjon.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -2x + 4
$$
:::

:::::::::::::


:::::::::::::{tab-item} b
Regn ut

$$
f(x) : (x - 1)^2 
$$


Sammenlikn **resten** med likningen for tangenten du fant i **a**. 

> Husk å utvide $(x - 1)^2$ før du gjør polynomdivisjonen.

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./koder/utforsk/utforsk_1/b_annotert.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::



::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Setning: Resten i polynomdivisjon $f(x) : (x - r)^2$
---
class: summary
---
Gitt et polynom $f(x)$, vil resten i polynomdivisjonen $f(x) : (x - r)^2$ være det algebraiske uttrykket til tangenten som går gjennom punktet $(r, f(r))$ på grafen til $f$.

:::::::::::::::


Før vi går videre, bør du prøve å anvende setningen.


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 - 4x + 12.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Regn ut

$$
f(x) : (x - 2)^2
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./koder/underveisoppgaver/underveisoppgave_1/a.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk resultatet ditt fra **a** til å bestemme likningen for tangenten til grafen til $f$ i $(2, f(2))$.


:::{admonition} Fasit
---
class: answer, dropdown
---
Fra oppgave **a** har vi at resten er gitt ved 

$$
y = -4x + 8,
$$

som er tangenten til grafen til $f$ i $(2, f(2))$.
:::
:::::::::::::




::::::::::::::


:::::::::::::::
