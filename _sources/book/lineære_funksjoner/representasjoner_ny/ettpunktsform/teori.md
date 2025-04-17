# Ettpunktsform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en lineær funksjon på ettpunktsform og beskrive sammenhengen med den grafiske representasjonen.
* Kunne bytte fra en representasjon til en annen.
:::

Hittil har vi sett på to måter å representere en lineær funksjon på, nemlig {popup}`standardform<$f(x) = ax + b$>` og {popup}`nullpunktsform<$f(x) = a(x - x_0)$>`. Standardform fortalte oss stigningen til grafen og hvor grafen skjærer gjennom $y$-aksen, mens nullpunktsform fortalte oss stigningen og hvor grafen skjærer gjennom $x$-aksen. 

Her skal vi se på en tredje måte å representere en lineær funksjon som vi skal kalle for **ettpunktsform**. Denne måten å uttrykke en lineær funksjon forteller oss stigningen til grafen og ett punkt som grafen går gjennom.


:::::::::::::::{theory} Ettpunktsform
En lineær funksjon $f$ kan skrives på ettpunktsform som følger: 

:::{figure} ./figurer/teori/algebraisk_representasjon/ettpunktsform.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

:::{figure} ./figurer/teori/grafisk_representasjon/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


:::::::::::::::


---


:::::::::::::::{explore} Utforsk 1
Nedenfor vises grafen til en lineær funksjon $f$ i et interaktivt vindu der $f(x)$ er skrevet på ettpunktsform 

$$
f(x) = a\cdot (x - x_0) + y_0
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $x_0$. 

Gi en beskrivelse av hva som skjer med grafen.

:::::::::::::


:::::::::::::{tab-item} b
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $y_0$. 

Gi en beskrivelse av hva som skjer med grafen.

:::::::::::::


:::::::::::::{tab-item} c
Undersøk hva som skjer med grafen til $f$ når du justerer verdien til $a$.

Er det noen forskjell fra standardform og nullpunktsform? Kan du fortsatt lese av verdien til $a$ på samme måte som før?

:::::::::::::

::::::::::::::


:::{ggb} 720 600
---
material_id: u8hkthry
---
:::


:::::::::::::::





---




:::::::::::::::{underveisoppgave} Underveisoppgave 1
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2\cdot (x - 1) + 3
$$

Hvilken av grafene nedenfor viser grafen til $f$?


::::{answer}
Graf B
::::

::::{solution}
Fra ettpunktsformen til $f(x)$ kan vi lese av at grafen må gå gjennom punktet $(1, 3)$. Dette passer med graf A, B og C. Stigningstallet til $f$ er $a = 2$ som eliminerer graf A siden den har negativ stigning. Sjekker vi stigningstallet til graf B er stigningstallet $a = 2$, mens stigningstallet til graf C er $a = 1$. 

Dermed er graf B grafen til $f$.
::::


:::{clickable-figure} ./figurer/underveisoppgaver/underveisoppgave_1/merged_figure.svg
---
width: 100%
---
:::

:::::::::::::::

---


:::::::::::::::{underveisoppgave} Underveisoppgave 2
Nedenfor vises grafen til en lineær funksjon $f$.


Bestem $f(x)$ på ettpunktsform med utgangspunkt i punktet på grafen når $x_0 = 1$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::{answer}
$$
f(x) = -3 \cdot (x - 1) - 4
$$
::::

::::{solution}
Stigningstallet til grafen kan vi lese av som $a = -3$ ved å se at funksjonsverdien til $f(x)$ synker med $3$ når $x$ øker med $1$. For eksempel kan vi se dette ved at grafen går gjennom punktene $(-1, 2)$ og $(0, -1)$. 

Når $x_0 = 1$ er $y_0 = -4$ som betyr at vi kan skrive $f(x)$ på ettpunktsform som:

$$
f(x) = a \cdot (x - x_0) + y_0 = -3 \cdot (x - 1) - 4
$$
::::


:::::::::::::::


## Ettpunktsformelen

Ettpunktsformen til en lineær funksjon er en måte å uttrykke en sammenheng som kalles for **ettpunktsformelen**. Vi skal se nærmere på denne sammenhengen nå.


:::::::::::::::{theory} Ettpunktsformelen
En linje som har stigningstall $a$ og går gjennom et punkt $(x_0, y_0)$, så kan vi skrive likningen for linja som 

$$
y = a\cdot(x - x_0) + y_0
$$



:::::::::::::::


