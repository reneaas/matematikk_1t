# Nullpunktsform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere og tolke en lineær funksjon på nullpunktsform.
* Kunne bytte mellom nullpunktsform og standardform. 
:::


Vi har så langt sett at vi kan representere en lineær funksjon $f$ på {popup}`standardform<Standardformen til en lineær funksjon er $$f(x) = ax + b$$>`. Standardformen forteller oss grafisk hvor mye grafen stiger eller synker, og hvor den skjærer $y$-aksen. Her skal vi se på en annen representasjonsform som vi skal kalle for **nullpunktsform**. Denne vil fortelle oss hvor mye grafen til $f$ stiger eller synker, men vil i stedet fortelle oss hvor grafen til $f$ skjærer $x$-aksen. 


## Nullpunktsform

:::::::::::::::{theory} Nullpunktsform
En lineær funksjon $f$ kan skrives på nullpunktsform som følger:

:::{figure} ./figurer/teori/algebraisk_representasjon/nullpunktsform.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::


:::{figure} ./figurer/teori/grafisk_representasjon/nullpunktsform.svg
---
width: 80%
class: no-click, adaptive-figure
:::



:::::::::::::::


---



:::::::::::::::{explore} Utforsk 1

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


:::::::::::::::


---


:::::::::::::::{underveisoppgave} Underveisoppgave 1
Nedenfor vises nullpunktsformen til en lineær funksjon $f$ som er gitt ved 

$$
f(x) = 3\cdot (x - 1)
$$

Hvilken av grafene nedenfor tilhører $f$? 


:::{answer}
Graf C
:::

:::{solution}
Nullpunktet til $f$ er $x_1 = 1$ og stigningstallet er $3$. Vi kan lese av at graf A og C skjærer $x$-aksen i $x = 1$ som passer med opplysningene om $f$. Men graf A har negativt stigningstall, mens graf C har positivt stigningstall. Dermed må graf C være grafen til $f$.
:::


:::{clickable-figure} ./figurer/underveisoppgaver/underveisoppgave_1/merged_figure.svg
---
width: 100%
---
:::



:::::::::::::::


---

##  Fra standardform til nullpunktsform – og omvendt

Dersom vi kjenner til $f(x)$ på standardform, kan vi skrive den om til nullpunktsform ved å faktorisere ut stigningstallet $a$:

:::::::::::::::{example} Eksempel 1
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

Dette betyr også at nullpunktet til $f$ er gitt ved 

$$
f(x) = 0 \liff x = -2. 
$$
::::


:::::::::::::::

:::::::::::::::{underveisoppgave} Underveisoppgave 2
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
