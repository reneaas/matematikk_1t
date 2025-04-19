# Lineære-over-lineære 

::::{admonition} Læringsmål
---
class: tip
---
* Kunne representere lineære-over-lineære rasjonale funksjoner algebraisk, grafisk og med fortegnslinjer.
* Kunne bestemme $f(x)$ for rasjonale funksjoner der tellergrad og nevnergrad er 1.
* Kunne bestemme asymptotene til rasjonale funksjoner.
* Kunne bestemme nullpunkter og løse ulikheter med rasjonale funksjoner.
::::

En **rasjonal funksjon** er en funksjon som kan skrives som en brøk der telleren og nevneren er polynomer.

:::::{admonition} Definisjon: Rasjonale funksjoner
---
class: theory
---
En rasjonal funksjon $f$ er en funksjon som kan skrives som

$$
f(x) = \dfrac{P(x)}{Q(x)}
$$

der $P(x)$ og $Q(x)$ er polynomer. 

Graden til $P$ kaller vi for **tellergraden** til $f$ og graden til $Q$ kaller vi for **nevnergraden** til $f$.
:::::

Vi skal først konsentrere oss om rasjonale funksjoner der tellergraden og nevnergraden er $1$. 
Det vil si der både teller og nevner er lineære polynomer. Vi skal kalle dette for **lineære-over-lineære** rasjonale funksjoner.


## Algebraisk og grafisk representasjon

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
En rasjonal funksjon $f = P / Q$ der $P$ og $Q$ er lineære funksjoner, kan skrives som

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

der $a, b, c \in \mathbb{R}$ er noen konstanter.

I det interaktive vinduet under vises grafen til $f$. 

1. Utforsk hva $a$ bestemmer for grafen til $f$.
2. Utforsk hva $b$ bestemmer for grafen til $f$.
3. Utforsk hva $c$ bestemmer for grafen til $f$. 

> Husk at du kan zoome inn og ut i vinduet og flytte rundt på koordinatssystemet. 
:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/utforsk_1.html
---
:::

::::::::::::::{admonition} Fasit
---
class: answer, dropdown
---
:::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::{tab-item} 1. $a$
$a$ bestemmer verdien til den horisontale linja $y = a$. Grafen til $f$ *nærmer* seg denne linja når $|x|$ er stor.
::::::::::::

::::::::::::{tab-item} 2. $b$
$b$ bestemmer nullpunktet til $f$. Grafen til $f$ skjærer $x$-aksen i $x = b$. Vi kan merke oss at når $b = c$, så forsvinner nullpunktet og grafen til $f$ blir en horisontal linje. 
::::::::::::

::::::::::::{tab-item} 3. $c$
Konstanten $c$ bestemmer den vertikale linje $x = c$. Grafen til $f$ nærmer seg denne linja når $x$ er i nærheten av $x = c$. Verdien til $|f(x)|$ blir veldig stor når $x$ er nærme $x = c$.
::::::::::::

:::::::::::::


::::::::::::::

:::::::::::::::

---

Vi kan oppsummere det vi utforsket i Utforsk 1 med følgende resultat:

:::::{admonition} Lineære-over-lineære rasjonale funksjoner
---
class: summary
---
En rasjonal funksjon $f$ der teller $P(x)$ og nevner $Q(x)$ er lineære polynomer kan alltid skrives som

:::{figure} ./figurer/teori/annoterte_figurer/linear_rational_function.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::


der definisjonsmengden er $D_f = \mathbb{R} \setminus \{c\}$ og verdimengden er $V_f = \mathbb{R} \setminus \{a\}$.

::::{figure} ./figurer/teori/teori_1.svg
---
width: 80%
class: no-click, adaptive-figure
---
::::


| Konstant | Betydning |
|:-----------:|------------|
| $a$ | **Horisontal asymptote**. Verdien $f(x)$ nærmer seg når $\|x\|$ er veldig stor. |
| $b$ | **Nullpunktet** til $f$. Samme som nullpunktet til telleren $P$. |
| $c$ | **Vertikal asymptote**. Grafen til $f$ vokser mot uendeligheten når $x$ er nær linja $x = c$. Samme som nullpunktet til nevneren $Q$. |

:::::

---

## Bestemme $f(x)$ fra grafisk representasjon

Vi går løs på et eksempel. 

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
I {numref}`fig-rasjonale-funksjoner-representasjoner-eksempel-1` vises grafen til en rasjonal funksjon $f$. 

I figuren vises det at grafen til $f$ har
* En horisontal asymptote $y = 2$.
* En vertikal asymptote $x = -1$.
* Et nullpunkt i $x = 3$.

Bestem $f(x)$.

:::{figure} ./figurer/eksempler/eksempel_1/graf.svg
---
name: fig-rasjonale-funksjoner-representasjoner-eksempel-1
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en rasjonal funksjon $f$ med en horisontal asymptote $y = 2$ og en vertikal asymptote $x = -1$ og et nullpunkt i $x = 3$. 
:::

::::{admonition} Løsning
---
class: solution
---
En rasjonal funksjon der teller og nevner er lineære polynomer, kan alltid skrives som

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

der $a$ er den horisontale asympoten, $x_1$ er nullpunktet og $x_\infty$ er den vertikale asymptoten. 

* Horisontal asymptote er $y = 2$, så $a = 2$.
* Nullpunktet er $x = 3$, så $b = 3$.
* Vertikal asymptote er $x = -1$, så $c = -1$.

Dermed er $f(x)$ gitt ved 

$$
f(x) = \dfrac{2\cdot (x - 3)}{x - (-1)} = \dfrac{2x - 6}{x + 1}
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
width: 90%
class: no-click, adaptive-figure
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


## Bestemme egenskaper fra $f(x)$

:::::{admonition} Eksempel 2
---
class: example
---
En rasjonal funksjon $f$ er gitt ved

$$
f(x) = \dfrac{2x + 6}{x - 1}
$$

Bestem nullpunktet og asymptotene til $f$.

::::{admonition} Løsning
---
class: solution
---
Vi kan skrive om uttrykket til $f(x)$ ved å faktorisere telleren:

$$
f(x) = \dfrac{2x + 6}{x - 1} = \dfrac{2(x + 3)}{x - 1} 
$$

som betyr at vi kan lese av nullpunktet og asymptotene til $f$:


* Horisontal asymptote: $y = 2$. 
* Vertikal asymptote: $x = 1$.
* Nullpunkt: $x = -3$.

::::
:::::

---

## Skissere grafen til $f$

Vi går løs på et eksempel der vi lager en skisse av grafen til en lineær rasjonal funksjon.


:::::::::::::::{admonition} Eksempel 3
---
class: example
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{-2x + 4}{x + 3}
$$

Lag en skisse av grafen til $f$. 

:::::{admonition} Løsning
---
class: solution
---
Vi starter med å bestemme egenskapene til $f$ ved å skrive om $f(x)$ så vi kan lese av nullpunktet og asymptotene:

$$
f(x) = \dfrac{-2x + 4}{x + 3} = \dfrac{-2(x - 2)}{x + 3}
$$

som betyr at 

* $y = -2$ er en horisontal asymptote.
* $x = 2$ er et nullpunkt.
* $x = -3$ er en vertikal asymptote. 

Vi tegner en fortegnslinje der vi passer på å få med at $x = -3$ et **bruddpunkt**: 

:::{figure} ./figurer/eksempler/eksempel_3/fortegnslinje.svg
---
name: fig-lineære-rasjonale-funksjoner-eksempel-3-fortegnslinje
width: 90%
class: no-click, adaptive-figure
---
viser fortegnsskjema for $f(x) = (-2x + 4) / (x + 3)$. Bruddpunktene til $f(x)$ er markert med et kryss "$\times$" i fortegnslinja.
::: 

Ut ifra fortegnslinja til $f(x)$ kan vi se at $f(x) < 0$ når $x < -3$ og $x > 2$ og at $f(x) > 0$ når $-2 < x < 3$. 
Samler vi dette med opplysningene om nullpunktet og asymptotene til $f$, kan vi lage en skisse av grafen til $f$ som følger:

:::{figure} ./figurer/eksempler/eksempel_3/graf.svg
---
name: fig-lineære-rasjonale-funksjoner-eksempel-3-graf
width: 90%
class: no-click, adaptive-figure
---
viser en skisse av grafen til $f(x) = (-2x + 4) / (x + 3)$ med nullpunktet $x = 2$, den vertikale asymptoten $x = -3$ og den horisontale asymptoten $y = -2$.
::: 

:::::

:::::::::::::::
