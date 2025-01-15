# Den deriverte

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke polynomdivisjon til å bestemme likningen for en tangent.
* Kunne derivere polynomfunksjoner algebraisk.
* Kunne bestemme ekstremalpunktene til en polynomfunksjon ved hjelp av den deriverte.
:::


## Polynomdivisjon og tangenter

Vi har allerede sett at resten i polynomdivisjon med $f(x) : (x - r)$ lar oss bestemme $f(r)$. Her skal vi gå et steg videre å se at resten i en bestem polynomdivisjon kan brukes til å bestemme likningen til en tangent til grafen til polynomfunksjonen.


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
class: no-click
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
Gitt et polynom $f(x)$, vil resten i polynomdivisjonen $f(x) : (x - r)^2$ være likningen til tangenten $T$ som går gjennom punktet $(r, f(r))$ på grafen til $f$.

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
class: no-click
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

---

## Den deriverte til en polynomfunksjon
Når vi fant den deriverte $f'$ til en andregradsfunksjon $f$, så fant vi at den deriverte var en lineær funksjon. Sagt på en annen måte: vi får et førstegradspolynom $f'(x)$ når vi finner den deriverte av et andregradspolynom $f(x)$. Dette var ikke bare et sammentreff – generelt sett vil $f'(x)$ være et polynom som har én grad lavere for et hvert polynom $f(x)$.


:::::::::::::::{admonition} Den deriverte til en polynomfunksjon 1
---
class: theory
---
Gitt et polynom $f(x)$ av grad $n$, vil den deriverte av polynomet $f'(x)$ være et polynom av grad $n - 1$. 

:::::::::::::::

I praksis kan vi finne den deriverte algebraisk ved å følge noen bestemte regneregler som gjelder for alle polynomer.

::::{admonition} Definisjon: $x^0$
---
class: sidenote, margin
---
Vi definerer $x^0 = 1$ for alle $x \neq 0$. 
::::


:::::::::::::::{admonition} Derivasjonsregler for polynomer
---
class: summary
---
Regel 1
: For ethvert ledd $a x^n$ i et polynom $f(x)$, vil den deriverte av leddet være

$$
(a x^n)' = n\cdot a x^{n-1}
$$

Regel 2
: Hvert ledd i et polynom deriveres hver for seg:

$$
(ax^n + bx^m)' = (ax^n)' + (bx^m)'
$$

Regel 3
: Den deriverte av en konstant er null:

$$
C' = 0
$$

Regel 4
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

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bestem den deriverte til 

$$
f(x) = x^4 - 3x^2 + 5x - 1
$$

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f'(x) = 4x^3 - 6x + 5
$$
::::

:::::::::::::::



## Sammenheng mellom $f(x)$ og $f'(x)$

En viktig sammenheng mellom $f(x)$ og $f'(x)$ er at $f'(x)$ gir oss stigningstallet til tangenter til grafen til $f$. Spesielt vil vi kunne lese av fra $f'(x)$ hvor
* Grafen til $f$ er stigende eller synkende
* Grafen til $f$ har topp- eller bunnpunkter


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
class: no-click
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
class: no-click
---
viser fortegnslinja til $f'(x)$. Sammenhengen med grafen til $f$ er at $f'(x) > 0$ når grafen til $f$ stiger og $f'(x) < 0$ når grafen til $f$ synker. I ekstremalpunktene til $f$ er $f'(x) = 0$ fordi en tangent gjennom punktet vil være horisontal og dermed ha stigningstall $0$.
:::

:::::::::::::


:::::::::::::{tab-item} Grafen til $f'$

:::{figure} ./figurer/eksempler/eksempel_2/f_derivert.svg
---
name: fig-polnyomfunksjoner-derivasjon-eksempel-2-fortegnslinje
width: 80%
class: no-click
---
viser grafen til $f'$. Nullpunktene til $f'$ svarer til samme $x$-koordinater som ekstremalpunktene til $f$.
:::

:::::::::::::


::::::::::::::

:::::::::::::::



<!-- 
:::::::::::::::{admonition} Sammenheng 2 mellom $f(x)$ og $f'(x)$
---
class: summary
---
La $f$ være en polynomfunksjon. Da vil den deriverte $f'$ fortelle oss at:
* Grafen til $f$ stiger når $f'(x) > 0$.
* Grafen til $f$ synker når $f'(x) < 0$. 
* Grafen til $f$ har et ekstremalpunkt der $f'(x) = 0$ hvis:
    * $f'(x) > 0$ *rett før* ekstremalpunktet og $f'(x) < 0$ *rett etter*. Da er ekstremalpunktet et toppunkt.
    * $f'(x) < 0$ *rett før* ekstremalpunktet og $f'(x) > 0$ *rett etter*. Da er ekstremalpunktet et bunnpunkt.
* Hvis $f'(x)$ har samme fortegn *rett før* og *rett etter* et punkt hvor $f'(x) = 0$, er punktet et *terrassepunkt*.



::::::::::::::: -->

