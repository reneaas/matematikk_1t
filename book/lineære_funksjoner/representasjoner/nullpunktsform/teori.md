# Nullpunktsform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere og tolke en lineær funksjon på nullpunktsform.
* Kunne bytte mellom nullpunktsform og standardform. 
:::


Vi har så langt sett at vi kan representere en lineær funksjon $f$ på standardform. Standardformen forteller oss grafisk hvor mye grafen stiger eller synker, og hvor den skjærer $y$-aksen. Her skal vi se på en annen representasjonsform som vi skal kalle for **nullpunktsform**. Denne vil også fortelle oss hvor mye grafen til $f$ stiger eller synker, men vil i stedet fortelle oss hvor grafen til $f$ skjærer $x$-aksen – det vi kaller for **nullpunktet** til $f$ fordi det er der $f(x) = 0$.


## Algebraisk representasjon

:::::::::::::::{theory} Nullpunktsform
En lineær funksjon $f$ kan skrives på nullpunktsform som følger:

:::{figure} ./figurer/teori/algebraisk_representasjon/nullpunktsform.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Her er $a$ stigningstallet til $f$ og $x_1$ er nullpunktet til $f$, altså der $f(x) = 0$.

:::{figure} ./figurer/teori/grafisk_representasjon/nullpunktsform.svg
---
width: 80%
class: no-click, adaptive-figure
:::



:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
I figuren nedenfor vises grafen til en lineær funksjon $f$.


Bestem $f(x)$ på nullpunktsform.


:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 75%
---
:::

::::{solution}
---
dropdown: 0
---
Vi skriver $f(x)$ på nullpunktsform

$$
f(x) = a(x - x_1)
$$

Vi ser at grafen til $f$ skjærer $x$-aksen i $(1, 0)$ som betyr at $x_1 = 1$. 

Øker vi verdien til $x$ med $1$ fra $(1, 0)$, finner vi et punkt på grafen i $(2, 2)$. Det betyr at $y$-verdien har økt med $2$ og derfor er stigningstallet $a = 2$. 

Altså er 

$$
f(x) = a(x - x_1) = 2(x - 1)
$$
::::


:::::::::::::::


---





<!-- :::::::::::::::{explore} Utforsk 1

Nedenfor vises grafen til en lineær funksjon $f$ i et interaktivt vindu der $f(x)$ er skrevet på nullpunktsform

$$
f(x) = a \cdot \left(x - x_1\right)
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $x_1$. 

Hvordan kan du lese av hvilken verdi $x_1$ har fra grafen til $f$?

::::{solution}
Vi kan lese verdien til $x_1$ ved å se på $x$-koordinaten til skjæringspunktet mellom grafen til $f$ og $x$-aksen.
::::

:::::::::::::


:::::::::::::{tab-item} b
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $a$. 

Kan du fortsatt lese av verdien til $a$ på samme måte som når vi bruke standardform?


::::{solution}
Stigningstallet $a$ kan leses av på samme måte som før ved å se på hvor mye $f(x)$ endrer seg når vi øker verdien til $x$ med $1$.
::::

:::::::::::::

::::::::::::::

:::{ggb} 720 600
---
material_id: zgxwf6c3
---
:::


::::::::::::::: -->




<!-- :::{quiz} Quiz 1
Q: Hva er stigningstallet til $f(x) = 2(x - 1)$?
+ $2$
- $-2$
- $1$
- $2x$

Q: Hva nullpunktet til $f(x) = 3(x - 2)$? 
+ $x = 2$
- $x = 3$
- $x = -2$
- $x = -3$

Q: Grafen til $f(x) = -4(x + 1)$ skjærer $x$-aksen i ...
+ $(-1, 0)$
- $(1, 0)$
- $(0, -4)$
- $(0, 1)$

Q: Hva er stigningstallet til $f(x) = -2(x + 3)$?
+ $-2$
- $2$
- $3$
- $-3$

Q: Nullpunktet til $f(x) = -5(x + 4)$ er ...
+ $x = -4$
- $x = 4$
- $x = 5$
- $x = -5$
::: -->



:::::::::::::::{exercise} Underveisoppgave 1
Nedenfor vises nullpunktsformen til en lineær funksjon $f$ som er gitt ved 

$$
f(x) = 3\cdot (x - 1)
$$

Hvilken av grafene nedenfor tilhører $f$? 



:::{clickable-figure} ./figurer/underveisoppgaver/underveisoppgave_1/merged_figure.svg
---
width: 100%
---
:::


:::{answer}
Graf C
:::

:::{solution}
Nullpunktet til $f$ er $x_1 = 1$ og stigningstallet er $3$. Vi kan lese av at graf A og C skjærer $x$-aksen i $x = 1$ som passer med opplysningene om $f$. Men graf A har negativt stigningstall, mens graf C har positivt stigningstall. Dermed må graf C være grafen til $f$.
:::



:::::::::::::::



---




:::::::::::::::{exercise} Underveisoppgave 2
Nedenfor vises grafen til en lineær funksjon $f$.

Bestem $f(x)$ på nullpunktsform.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::{answer}
$$
f(x) = -2\cdot (x - 3)
$$
::::



::::{solution}
Grafen til $f$ skjærer $x$-aksen i $x_1 = 3$, som betyr at dette er nullpunktet til $f$. Stigningstallet kan vi lese av til å være $a = -2$ siden $f(x)$ synker med $2$ når $x$ øker med $1$. Dermed kan vi skrive

$$
f(x) = a \cdot (x - x_1) = -2\cdot (x - 3).
$$


::::

:::::::::::::::



---

##  Fra standardform til nullpunktsform – og omvendt

Dersom vi kjenner til $f(x)$ på standardform, kan vi skrive den om til nullpunktsform ved å faktorisere ut stigningstallet $a$ fra alle ledd. La oss se på et eksempel:

:::::::::::::::{example} Eksempel 2
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2\cdot x + 4.
$$

Bestem nullpunktsformen til $f(x)$. 

::::{admonition} Løsning
---
class: solution
---
Vi starter med $f(x)$ på standardform og så faktoriserer vi ut stigningstallet $a = 2$ fra alle leddene:

\begin{align*}
    f(x) &= 2\cdot x + 4 \\
    \\
    &= \textcolor{red}{2}\cdot x + \textcolor{red}{2}\cdot 2 \\
    \\
    &= \textcolor{red}{2}\cdot \left(x + 2\right) \\
\end{align*}

Dermed er nullpunktsformen til $f(x)$ gitt ved 

$$
f(x) = 2\cdot \left(x + 2\right) = 2\cdot \left(x - (-2)\right).
$$

Vi leser av at $x_1 = -2$ som betyr at nullpunktet til $f$ gitt ved

$$
x = -2.
$$
::::


:::::::::::::::




---




:::::::::::::::{exercise} Underveisoppgave 3
En lineær funksjon $f$ er gitt ved 

$$
f(x) = -3\cdot x + 6
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktsformen til $f(x)$.

::::{answer}
$$
f(x) = -3\cdot \left(x + 2\right)
$$
::::

::::{solution}
\begin{align*}
    f(x) &= -3\cdot x + 6 \\
    \\
    &= \textcolor{red}{-3}\cdot x + \left(\textcolor{red}{-3}\right)\cdot (-2) \\
    \\
    &= \textcolor{red}{-3}\cdot \left(x - (-2)\right) \\
    \\
    &= -3\cdot \left(x + 2\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem nullpunktet til $f$.

::::{answer}
$$
x = -2
$$
::::

::::{solution}
Siden nullpunktsformen til $f(x)$ er gitt ved 

$$
f(x) = -3 \cdot (x + 2) = -3 \cdot (x - (-2)),
$$

betyr det at nullpunktet til $f$ er gitt ved 

$$
x = -2.
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2(x + 3)
$$

Bestem $f(x)$ på standardform.


::::{solution}
---
dropdown: 0
---
Vi ganger ut parentesen for å finne $f(x)$ på standardform: 

$$
f(x) = 2(x + 3) = 2x + 6
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 4
En lineær funksjon $f$ er gitt ved

$$
f(x) = -2(x - 2)
$$

Bestem $f(x)$ på standardform. 


::::{answer}
$$
f(x) = -2x + 4
$$
::::

::::{solution}
Vi ganger ut parentesen for å finne $f(x)$ på standardform:

$$
f(x) = -2(x - 2) = -2x + 4
$$
::::
:::::::::::::::
