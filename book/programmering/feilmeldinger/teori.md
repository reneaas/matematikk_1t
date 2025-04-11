# Feilsøking og debugging


:::{admonition} Læringsmål
---
class: tip
---
* Kjenne til noen vanlige feilmeldinger og kunne rette opp i programmer som inneholder feil.
:::


:::::::::::::::{explore} Utforsk 1

> Her skal du få en oversikt over hvilke typer feilmeldinger som kan oppstå og hva de forteller oss om feilen i programmet.

For hvert program nedenfor skal du gjøre følgende:

1. Kjør programmet og les feilmeldingen som kommer i utskriften. Hvilken **type feil** forteller feilmeldingen om?
2. Bestemme hvor i programmet feilen ligger.
3. Rette opp i feilen.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a


:::{interactive-code}
s = 0
for i in range(10):
    s = S + i

print(s)


:::


::::{answer}
1. `NameError`: Programmet prøver å bruke en variabel som ikke er definert.
2. Linje 3. 
3. Programmet bruker stor bokstav `S`{l=python} for en variabel som er definert som `s`{l=python}. Python ser forskjell på store og små bokstaver, så vi må passe på at vi er konsekvente i bruken av dem. Ved å bytte ut `S`{l=python} med `s`{l=python} i linje 3, vil programmet fungere som det skal.

> Det er anbefalt å **alltid** bruke små bokstaver for alt i Python, så det er lettere å unngå slike feil.

::::

:::::::::::::





:::::::::::::{tab-item} b

:::{interactive-code}


:::

:::::::::::::

::::::::::::::


:::::::::::::::