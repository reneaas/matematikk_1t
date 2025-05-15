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
for x in range(5)
    print(x)

:::

:::::{answer}
1. `SyntaxError`. Vi har skrevet noe som ikke er gyldig Pythonkode. 
2. Linje 1.
3. Vi har glemt kolon `:`{l=python} på slutten av linje 1. Ved å legge til kolon på slutten av linje 1, vil programmet fungere som det skal.
:::::

:::::::::::::

:::::::::::::{tab-item} c

:::{interactive-code}
for x in range(5):
print(x)
:::

::::{answer}
1. `IndentationError`. Vi har ikke brukt innrykk på kodelinjen som skal stå inni `for`{l=python}-løkken.
2. Linje 2.
3. Vi må bare legge til et innrykk på linje 2 med tab, så fungerer programmet som det skal.
::::

:::::::::::::

::::::::::::::


:::::::::::::::