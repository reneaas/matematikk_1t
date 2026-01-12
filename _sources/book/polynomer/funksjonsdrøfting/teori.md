# Funksjonsdrøfting

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive sammenhengen mellom den $f$ og $f'$, og bruke $f'$ til å bestemme ulike egenskaper ved $f$.
:::::


Funksjonsdrøfting handler om å finne ut alt om grafen til en funksjon $f$ ved hjelp av $f(x)$ og dens deriverte. 

## Stasjonære punkter

:::::::::::::::{summary} Stasjonære punkter
Et **stasjonært punkt** på grafen til $f$ er et punkt der $f'(x) = 0$. Det finnes tre typer stasjonære punkter:
1. **Bunnpunkt**: Den deriverte er positiv før og negativ etter punktet.
2. **Toppunkt**: Den deriverte er negativ før og positiv etter punktet.
3. **Terrassepunkt**: Den deriverte har samme fortegn før og etter punktet.

Se figuren nedenfor.


:::{plot}
width: 70%
ticks: off
function: -((x + 1) ** 2) * (x - 2) ** 3 + 3, f
xmin: -3
xmax: 3
ymin: -2
ymax: 14
point: (-1, f(-1))
point: (1/5, f(1/5))
point: (2, f(2))
text: -1, f(-1), "Bunnpunkt", bottom-center
text: 1/5, f(1/5), "Toppunkt", top-right
text: 2, f(2), "Terrassepunkt", top-right
:::




:::::::::::::::

---


:::::::::::::::{example} Eksempel 1
Bestem de stasjonære punktene og klassifiser dem for funksjonen $f$ gitt ved 

$$
f(x) = x^3 - 6x^2 + 9x
$$

:::::{solution}
---
dropdown: 0
---
Vi starter med å finne den deriverte:

$$
f'(x) = 3x^2 - 12x + 9
$$

deretter løser vi $f'(x) = 0$: 

$$
3x^2 - 12x + 9 = 0 \liff x^2 - 4x + 3 = 0 \liff (x-3)(x-1) = 0 
$$

som betyr at de stasjonære punktene til $f$ er 

$$
x = 1 \or x = 3
$$

Dermed kan vi skrive $f'(x)$ som 

$$
f'(x) = 3(x - 1)(x - 3)
$$

For å avgjøre om punktene er bunnpunkter, toppunkter eller terrassepunkter, tegner vi et fortegnsskjema for $f'(x)$:


:::{signchart}
width: 100%
function: 3*x**2 - 12*x + 9, f'(x)
:::


Fra fortegnsskjema ser vi at $f'(x)$ går fra positiv til negativ i $x = 1$, som betyr at $f$ har et toppunkt i $(1, f(1))$. I $x = 3$ går $f'(x)$ fra negativ til positiv, som betyr at $f$ har et bunnpunkt i $(3, f(3))$.
:::::


:::::::::::::::

---

Vi tar et eksempel til der alle tre typene dukker opp slik at vi vet hvordan vi kan lese de av fra et fortegnsskjema.

:::::::::::::::{example} Eksempel 2
En femtegradsfunksjon er gitt ved 

$$
f(x) = \dfrac{1}{5}x^5 - \dfrac{3}{4}x^4 - x^3 + \dfrac{11}{2}x^2 - 6x + 2
$$

Bestem de stasjonære punktene og klassifiser dem.

:::::{solution}
---
dropdown: 0
---
Vi starter med å finne den deriverte:

$$
f'(x) = x^4 - 3x^3 - 3x^2 + 11x - 6
$$

Deretter skal vi løse likningen $f'(x) = 0$. Her kan vi lete etter en rot med polynomdivisjon ved å se etter mulige kandidater som deler konstantleddet. Tallene som deler konstantleddet er 

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 6\}
$$

Så bruker vi et Horner-skjema til å sjekke om noen av disse er en rot (og utføre polynomdivisjon samtidig!):

:::{figure} ./koder/eksempler/eksempel_2/horner_skjema_1.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Vi får $0$ i rest som betyr at $x = 1$ er en rot i $f'(x)$. Fra Horner-skjema kan vi også lese av at $f'(x)$ kan faktoriseres som

$$
f'(x) = (x - 1)(x^3 - 2x^2 - 5x + 6)
$$

Nå må vi utføre samme prosedyre én gang til med tredjegradspolynomet 

$$
x^3 - 2x^2 - 5x + 6
$$

Vi bruker Horner-skjema én gang til: 

:::{figure} ./koder/eksempler/eksempel_2/horner_skjema_2.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

Her får vi også $0$ i rest med $x = 1$ som betyr at vi kan skrive tredjegradspolynomet som

$$
x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 - x - 6)
$$

Til slutt bruker vi $abc$-formelen for å sjekke å faktorisere andregradspolynomet:

$$
x^2 - x - 6 = 0
$$

som gir 

$$
x = \dfrac{1 \pm \sqrt{1 + 4 \cdot 6}}{2} = \dfrac{1 \pm 5}{2}
$$

som gir løsningene

$$
x = 3 \or x = -2
$$

Dermed kan vi skrive andregradspolynomet som

$$
x^2 - x - 6 = (x + 2)(x - 3)
$$

Kombinerer vi alle resultatene her, får vi 

\begin{align*}
    f'(x) &= (x - 1)(x^3 - 2x^2 - 5x + 6) \\
    \\
    & = (x - 1)(x - 1)(x^2 - x - 6) \\
    \\
    &= (x - 1)(x - 1)(x + 2)(x - 3) \\
    \\
    &= (x + 2)(x - 1)^2 (x - 3)
\end{align*}

Vi vet nå at de stasjonære punktene til $f$ er 

$$
x = -2 \or x = 1 \or x = 3.
$$

Nå kan vi tegne et fortegnsskjema for $f'(x)$ for å klassifisere dem som toppunkter, bunnpunkter eller terassepunkter:


:::{figure} ./figurer/eksempler/eksempel_2/fortegnsskjema.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


I $x = -2$ så skifter $f'(x)$ fortegn fra positiv til negativ som betyr at dette er et toppunkt. I $x = 1$ så skifter ikke $f'(x)$ fortegn, men synker både før og etter punktet som betyr at det er et terassepunkt. I $x = 3$ så skifter $f'(x)$ fortegn fra negativ til positiv som betyr at dette er et bunnpunkt.

:::::

:::::::::::::::


---



## Vendepunkter 
Et **vendepunkt** på grafen til $f$ forteller oss hvor grafen har minst eller størst stigning. For å finne vendepunkter på grafen til en funksjon $f$, bruker vi den **andrederiverte** som vi skriver som $f''(x)$. 


:::::::::::::::{summary} Vendepunkter
Et **vendepunkt** på grafen til en funksjon $f$, er et punkt der $f''(x) = 0$ og $f''(x)$ skifter fortegn rundt dette punktet.


:::{plot}
width: 70%
function: (x**3 - 3*x**2 + 4), f
ticks: off
point: (1, f(1))
:::

Vendepunkter svarer til topp- eller bunnpunkter på grafen til den deriverte $f'$. 

:::::::::::::::



---




:::::::::::::::{example} Eksempel 3
En funksjon $f$ er gitt ved 

$$
f(x) = x^3 - 3x^2 + 4
$$

Bestem koordinatene til vendepunktet til $f$.

::::{solution}
---
dropdown: 0
---
Først finner vi den andrederiverte:

$$
f'(x) = (x^3 - 3x^2 + 4)' = 3x^2 - 6x
$$

$$
f''(x) = (3x^2 - 6x)' = 6x - 6
$$

Så løser vi likningen $f''(x) = 0$:

$$
f''(x) = 0 \liff 6x - 6 = 0 \liff x = 1
$$

Nå har vi $x$-koordinaten til vendepunktet. Vi må ha $y$-koordinaten til punktet også:

$$
y = f(1) = 1^3 - 3 \cdot 1^2 + 4 = 2
$$

Dermed har grafen til $f$ et vendepunkt i $(1, 2)$. For å være sikker på at dette faktisk er et vendepunkt, så må $f''(x)$ skifte fortegn rundt $x = 1$. Vi tegner et fortegnsskjema for $f''(x)$:


:::{signchart}
width: 100%
function: 6*x - 6, f''(x)
:::

Vi ser at $f''(x)$ går fra negativ til positiv i $x = 1$, som betyr at grafen til $f$ har et vendepunkt i $(1, 2)$.

::::

:::::::::::::::