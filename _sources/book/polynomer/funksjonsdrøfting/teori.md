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
Et stasjonært punkt på grafen til $f$ er et punkt der $f'(x) = 0$. Det finnes tre typer stasjonære punkter:
1. **Bunnpunkt**
2. **Toppunkt**
3. **Terassepunkt**

Se figuren nedenfor.

:::{figure} ./figurer/teori/funksjonsdrøfting/figur.svg
---
width: 80% 
class: no-click, adaptive-figure
---
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

For å avgjøre om punktene er bunnpunkter, toppunkter eller terrassepunkter, tegner vi et fortegnsskjema for $f'(x)$:

:::{figure} ./figurer/eksempler/eksempel_1/fortegnsskjema.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra fortegnsskjema ser vi at $f'(x)$ går fra positiv til negativ i $x = 1$, som betyr at $f$ har et toppunkt i $(1, f(1))$. I $x = 3$ går $f'(x)$ fra negativ til positiv, som betyr at $f$ har et bunnpunkt i $(3, f(3))$.
:::::


:::::::::::::::

---

Vi tar et eksempel til der alle tre typene dukker opp slik at vi vet hvordan vi kan lese de av fra et fortegnsskjema.

:::::::::::::::{exercise} Eksempel 2
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

## Andrederiverttesten
Vi har sett at vi kan bruke fortegnsskjema for den deriverte $f'(x)$ til å klassifisere stasjonære punkter. Her skal vi se på en annen strategi som kalles for andrederiverttesten. Men først må vi forstå hva den andrederiverte er. 

:::{summary} Den andrederiverte
For en funksjon $f$, er den andrederiverte $f''(x)$ den funksjonen vi får dersom vi deriverer $f(x)$ to ganger.
:::


---

:::::::::::::::{example} Eksempel 3
En andregradsfunksjon $f$ er gitt ved 

$$
f(x) = 2x^2 - 4x + 3
$$

Bestem den andrederiverte. 

::::{solution}
---
dropdown: 0
---
Vi deriverer funksjonen to ganger. Først finner vi den førstederiverte:

$$
f'(x) = 4x - 4
$$

deretter deriverer vi én gang til:

$$
f''(x) = (4x - 4)' = 4
$$



::::


:::::::::::::::



:::{summary} Andrederiverttesten
Hvis $x = c$ er et stasjonært punkt slik at $f'(c) = 0$, så vil følgende gjelde:

* Hvis $f''(c) > 0$, så er $x = c$ et bunnpunkt
* Hvis $f''(c) < 0$, så er $x = c$ et toppunkt

Hvis $f''(c) = 0$, så kan vi ikke trekke noen konklusjon om punktet.
:::






## Vendepunkter