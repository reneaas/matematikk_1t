# Cosinussetningen


:::::::::::::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke cosinussetningen til å regne ut ukjente sider og vinkler i en trekant.
* Kunne begrunne cosinussetningen.
:::::::::::::::



Cosinussetningen er en *generalisert* versjon av Pytagoras' setning som gjelder for *alle* trekanter. Vi skal se hvordan vi kommer fram til setningen senere, samt hvordan Pytagoras' setning kan betraktes som et spesialtilfelle av cosinussetningen.

Vi starter med å se på hva cosinussetningen sier.

:::::::::::::::{admonition} Cosinussetningen
---
class: summary
---
En trekant $\triangle ABC$ er vist nedenfor.

:::{figure} ./figurer/teori/generell_trekant/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


Da gjelder følgende:

\begin{align*}
    a^2 &= b^2 + c^2 - 2\cdot b\cdot c \cdot \cos A \\
    \\
    b^2 &= a^2 + c^2 - 2\cdot a\cdot c \cdot \cos B \\
    \\
    c^2 &= a^2 + b^2 - 2\cdot a \cdot b \cdot \cos C
\end{align*}

:::::::::::::::


---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Nedenfor vises en trekant $\triangle ABC$. 

:::{figure} ./figurer/underveisoppgaver/oppgave_1.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Bestem $AC$ ved hjelp av cosinussetningen.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
AC = 4
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Siden vi kjenner til vinkelen hjørne $A$, tar vi utgangspunkt i dette hjørnet for å bestemme $AC$ med cosinussetningen. Setningen forteller oss da at 

$$
AC^2 = AB^2 + BC^2 - 2\cdot AB\cdot BC \cdot \cos A.
$$

Vi bruker CAS til å bestemme $AC$:

:::{figure} ./ggb/underveisoppgaver/oppgave_1/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså får vi at 

$$
AC = 4.
$$

::::


:::{cas-window}
:::

:::::::::::::::


---

Cosinussetningen er en slagkraftig setning som sammen med sinussetningen og arealsetningen lar oss finne finne ut svært mye om trekanter fra lite informasjon. Vi tar et sammensatt eksempel for å se hvordan vi kan bruke cosinussetningen i praksis.


:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Nedenfor vises en firkant $\square ABCD$. 

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Bestem omkretsen $\mathcal{O}$ til $\square ABCD$.

:::::{admonition} Løsning
---
class: solution
---
Omkretsen til $\square ABCD$ er summen av lengdene til alle sidene:

$$
\mathcal{O} = AB + BC + CD + AD
$$

Vi mangler å bestemme $AD$ som vi må kan gjøre i steg. Først bestemme vi diagonale $BD$, deretter $AD$. Begge disse lengene kan vi bestemme ved hjelp av cosinussetningen som følger.

Vi starter med å dele opp firkanten i to trekanter, $\triangle ABD$ og $\triangle BCD$. Vi lar diagonalen $BD = x$. Da kan vi bruke cosinussetningen med utgangspunkt i hjørne $C$ i $\triangle BCD$ for å bestemme $x$:

$$
x^2 = BC^2 + CD^2 - 2\cdot BC\cdot CD \cdot \cos C.
$$

Vi bestemmer $x$ med CAS:

:::{figure} ./figurer/eksempler/eksempel_1/part_1.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er $x = BD = 4\sqrt{3}$.

Vi lar så $y = AD$. Vi kan bruke cosinussetningen én gang til for å bestemme $AD$ ved å ta utgangspunkt i hjørne $A$ i $\triangle ABD$:

$$
BD^2 = AB^2 + y^2 - 2\cdot AB \cdot y \cdot \cos A.
$$

Vi bestemmer $y$ med CAS:

:::{figure} ./figurer/eksempler/eksempel_1/part_2.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed er $y = AD = 4$. Omkretsen $\mathcal{O}$ av $\square ABCD$ er da:

$$
\mathcal{O} = AB + BC + CD + AD = 8 + 12 + 8\sqrt{3} + 4 = 24 + 8\sqrt{3}.
$$

:::::



:::::::::::::::


---

Det kan nå være naturlig å stille seg spørsmål: hvordan vet vi at cosinussetningen stemmer? Vi skal nå snu oss mot dette problemet og se hvordan vi kan komme fram til setningen for en vilkårlig trekant.

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Nedenfor vises en trekant $\triangle ABC$ og en rettvinklet "hjelpetrekant" $\triangle DAC$. <br>
Til sammen utgjør de en rettvinklet trekant $\triangle DBC$.

:::{figure} ./figurer/utforsk/utforsk_1/figur.svg
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
Bruk trignometri til å uttrykke lengden $y$ ved hjelp av lengden $b$ og vinkelen $u$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = b\cdot \sin u
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra definisjonen av $\sin u$ i $\triangle DAC$ har vi at $y$ er motstående katet til $v$ og $b$ er hypotenusen. Da følger det at

$$
\sin u = \dfrac{y}{b} \liff y = b\cdot \sin u.
$$
:::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk trignometri til å uttrykke lengden $x$ ved hjelp av lengden $b$ og vinkelen $u$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = b\cdot \cos u
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra definisjonen av $\cos u$ i $\triangle DAC$ har vi at $x$ er hosliggende katet til $u$ og $b$ er hypotenusen. Da følger det at

$$
\cos u = \dfrac{x}{b} \liff x = b\cdot \cos u.
$$
:::::

:::::::::::::


:::::::::::::{tab-item} c
Bruk Pytagoras' setning på trekant $\triangle DBC$ til å finne beskrive sammenhengen mellom lengdene $a$, $b$, $c$ og vinkelen $u$.

> Husk på Pytagoras' identitet for cosinus og sinus: $(\sin u)^2 + (\cos u)^2 = 1$.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a^2 = b^2 + c^2 + 2\cdot b\cdot c \cdot \cos u
$$
:::::

:::::::::::::


:::::::::::::{tab-item} d
Beskriv en sammenheng mellom $\cos v$ og $\cos u$.
Bruk dette til å komme fram til cosinussetningen for $\triangle ABC$ uttrykt ved hjelp av lengdene $a$, $b$, $c$ og vinkelen $v$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\cos u = -\cos v
$$

og

$$
a^2 = b^2 + c^2 - 2\cdot b\cdot c \cdot \cos v
$$
:::::


:::::::::::::

::::::::::::::



:::::::::::::::







