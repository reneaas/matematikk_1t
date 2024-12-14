# Representasjoner

::::{admonition} Læringsmål
---
class: tip
---
* Kunne representere rasjonale funksjoner algebraisk.
* Kunne bestemme $f(x)$ for rasjonale funksjoner.
* Kunne bestemme horisontale, vertikale og skrå asymptoter for rasjonale funksjoner.
::::

En rasjonal funksjon er en brøk av to polynomfunksjoner. 
Vi skal gradvis bygge opp forståelsen vår av rasjonale funksjoner ved å starte med den enkleste typen og generalisere til mer komplekse tilfeller.

## Rasjonale funksjoner: Type 1

:::::{admonition} Rasjonal funksjon: Type 1
---
class: summary
---
En rasjonal funksjon $f$ der teller og nevner er lineære funksjoner kan skrives som

$$
f(x) = \dfrac{a(x - x_1)}{x - x_\infty}
$$

* $a$ er den **horisontale asymptoten**.
* $x_1$ er nullpunktet til $f$.
* $x_\infty$ er den **vertikale asymptoten**.

::::{figure} ./figurer/teori/teori_1.svg
---
width: 80%
class: no-click
---
::::

:::::

---

Vi går løs på et eksempel. 

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
I {numref}`fig-rasjonale-funksjoner-representasjoner-eksempel-1` vises grafen til en rasjonal funksjon $f$. Fra figuren kan vi lese av at 
* $f$ har en horisontal asymptote $y = 1$.
* $f$ har en vertikal asymptote $x = -2$.
* $f$ har et nullpunkt i $x = 3$.

Bestem $f(x)$.

:::{figure} ./figurer/eksempler/eksempel_1/graf.svg
---
name: fig-rasjonale-funksjoner-representasjoner-eksempel-1
width: 80%
class: no-click
---
viser grafen til en rasjonal funksjon $f$ med en horisontal asymptote $y = 1$ og en vertikal asymptote $x = -2$ og et nullpunkt i $x = 3$. 
:::

::::{admonition} Løsning
---
class: solution
---
En rasjonal funksjon der teller og nevner er lineære funksjoner, kan skrives som

$$
f(x) = \dfrac{a(x - x_1)}{x - x_\infty}
$$

der $a$ er den horisontale asympoten, $x_1$ er nullpunktet og $x_\infty$ er den vertikale asymptoten. 

* Horisontal asymptote er $y = 1$, så $a = 1$.
* Nullpunktet er $x = 3$, så $x_1 = 3$.
* Vertikal asymptote er $x = -2$, så $x_\infty = -2$.

Dermed er $f(x)$ gitt ved 

$$
f(x) = \dfrac{1\cdot (x - 3)}{x - (-2)} = \dfrac{x - 3}{x + 2}
$$
::::

:::::::::::::::

---

:::::::::::::::{admonition} Quiz 1
---
class: quiz
---
Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::


:::::::::::::::


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
I {numref}`fig-rasjonale-funksjoner-representasjoner-underveisoppgave-1` vises grafen til en rasjonal funksjon $f$.

Bestem $f(x)$.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/graf.svg
---
name: fig-rasjonale-funksjoner-representasjoner-underveisoppgave-1
width: 80%
class: no-click
---
viser grafen til en rasjonal funksjon $f$.
:::


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = \dfrac{2(x - 3)}{x + 1}
$$
::::


::::{admonition} Løsning
---
class: dropdown, solution
---
En rasjonal funksjon kan skrives som:

$$
f(x) = \dfrac{a(x - x_1)}{x - x_\infty}
$$

der $a$ er den horisontale asymptoten, $x_1$ er nullpunktet og $x_\infty$ er den vertikale asymptoten.

* Horisontal asymptote er $y = 2$, så $a = 2$.
* Nullpunktet til $f$ er $x = 3$, så $x_1 = 3$.
* Vertikal asymptote er $x = -1$, så $x_\infty = -1$.

Dermed er $f(x)$ gitt ved

$$
f(x) = \dfrac{2(x - 3)}{x + 1}
$$
::::


:::::::::::::::

---


## Rasjonale funksjoner: Type 2
Vi skal nå sette fokus på rasjonale funksjoner der telleren er et andregradspolynom og nevneren er en lineær funksjon.

:::::::::::::::{admonition} Rasjonal funksjon: Type 2
---
class: summary
---
En rasjonal funksjon der telleren er et andregradspolynom og nevneren er en lineær funksjon, kan skrives som

| Antall nullpunkter | $f(x)$ |
|---------------------|--------|
| 0                  | $\dfrac{ax^2 + bx + c}{x - x_\infty}$ |  
| 1                  | $\dfrac{a(x - x_1)^2}{x - x_\infty}$ |  
| 2                  | $\dfrac{a(x - x_1)(x - x_2)}{x - x_\infty}$ |  

Generelt sett har vi følgende egenskaper til denne typen rasjonale funksjoner:
* $f$ har like mange nullpunkter som polynomet i telleren.
* $f$ har én vertikal asymptote som svarer til nullpunktet til polynomet i nevneren.
* $f$ har en **skrå asymptote**. Funksjonen $f$ "oppfører seg" som en lineær funksjon når $|x|$ er stor.

::::::::::::::{tab-set} 
:::::::::::::{tab-item} 0 nullpunkter


:::{figure} ./figurer/teori/teori_2/ingen_nullpunkter.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::

:::::::::::::{tab-item} 1 nullpunkt

:::{figure} ./figurer/teori/teori_2/ett_nullpunkt.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::

:::::::::::::{tab-item} 2 nullpunkter

:::{figure} ./figurer/teori/teori_2/to_nullpunkter.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::
::::::::::::::


:::::::::::::::


---

Vi tar et eksempel:

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
I {numref}`fig-rasjonale-funksjoner-representasjoner-eksempel-2` vises grafen til en rasjonal funksjon $f$. 

1. Bestem $f(x)$.
2. Bestem likningen for den skrå asymptoten til $f$.

:::{figure} ./figurer/eksempler/eksempel_2/graf.svg
---
name: fig-rasjonale-funksjoner-representasjoner-eksempel-2
width: 80%
class: no-click
---
viser grafen til en rasjonal funksjon $f$. 
:::


::::::::::::::{admonition} Løsning
---
class: solution
---

:::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::{tab-item} 1. Bestem $f(x)$.

| Hva er kjent? | Hva betyr det? |
|----------------|----------------|
| $f$ har to nullpunkter i $x = -2$ og $x = 3$ | Telleren kan være et andregradspolynom $a(x + 2)(x - 3)$|
| $f$ har en vertikal asymptote $x = 2$ | Nevneren kan være en lineær funksjon $x - 2$ |
| $f$ har en skrå asymptote | Telleren et polynom som er én grad høyere enn polynomet i nevneren. |

<br>

Vi går ut ifra at $f$ er en brøk der telleren er et andregradspolynom og nevneren er en lineær funksjon. Da kan $f(x)$ skrives som

$$
f(x) = \dfrac{p(x)}{q(x)}
$$

der $p$ er et andregradspolynom og $q$ er en lineær funksjon. Siden $f$ har to nullpunkter i $x = -2$ og $x = 3$, kan vi skrive $p(x)$ som 

$$
p(x) = a(x - (-2))(x - 3) = a(x + 2)(x - 3)
$$

Siden $f$ har en vertikal asymptote i $x = 2$, kan vi velge $q(x)$ til å være 

$$
q(x) = x - 2
$$

Dermed har vi at $f(x)$ er gitt ved

$$
f(x) = \dfrac{p(x)}{q(x)} = \dfrac{a(x + 2)(x - 3)}{x - 2}
$$

Til slutt må vi bestemme $a$ som vi kan gjøre ved å finne ett punkt til på grafen til $f$. Vi kan observere at 

$$
f(0) = 3 \quad \iff \quad \dfrac{a\cdot (0 + 2)\cdot (0 - 3)}{0 - 2} = 3 \quad \iff \quad \dfrac{a \cdot 2 \cdot (-3)}{-2} = 3
$$

som gir at 

$$
a = 1.
$$

Dermed har vi at 

$$
f(x) = \dfrac{(x + 2)(x - 3)}{x - 2}
$$



::::::::::::



::::::::::::{tab-item} 2. Bestem likningen for den skrå asymptoten til $f$.
Siden $f(x)$ er en brøk der telleren er et andregradspolynom og nevneren er et førstegradspolynom, kan vi utføre polynomdivisjon for å skrive om $f(x)$ som en lineær funksjon pluss et (mulig) restledd.

:::{figure} ./figurer/eksempler/eksempel_2/polynomdivisjon.svg
---
width: 60%
class: no-click
---
:::

Den første delen er en lineær funksjon $x + 1$ og resten $r(x) = -4/(x - 2) \sim 0$ når $|x|$ er stor. Siden restleddet vil være neglisjerbart for store $|x|$, vil 

$$
f(x) \sim x + 1
$$

som betyr at den skrå asymptoten er 

$$
y = x + 1.
$$

::::::::::::

:::::::::::::


::::::::::::::



:::::::::::::::

