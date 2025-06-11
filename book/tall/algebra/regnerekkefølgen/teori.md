# Regnerekkefølgen

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke regnerekkefølgen til å regne ut uttrykk.
* Kunne Pythonprogram til å regne ut uttrykk. 
:::::


Regnerekkefølgen kan brukes når vi skal regne ut et sammensatt uttrykk som består av tall. Regnerekkefølgen gir oss en tommelregel på hvilken rekkefølge vi kan bruke når vi skal regne ut uttrykket:

1. Parenteser
2. Eksponenter
3. Multiplikasjon og divisjon
4. Addisjon og subtraksjon


Vi starter med et eksempel:

:::::{example} Eksempel 1
Regn ut 

$$
3\cdot (2 - 4)^3 + 5\cdot 2
$$

::::{admonition} Løsning
---
class: solution
---
Vi følger regnerekkefølgen og regner ut uttrykket steg for steg:

\begin{align*}
    3\cdot (2 - 4)^3 + 5\cdot 2 &= 3\cdot (-2)^3 + 5\cdot 2 && (\text{1. Parentes}) \\
    \\
    &= 3\cdot (-8) + 5\cdot 2 && (\text{2. Eksponent}) \\
    \\
    &= -24 + 10  && (\text{3. Multiplikasjon}) \\
    \\
    &= -14  && (\text{4. Addisjon})
\end{align*}
::::
:::::

---

:::::{underveisoppgave} Underveisoppgave 1
Regn ut

$$
2\cdot (3 + 5)^2 - 4\cdot 6 + 8
$$

::::{solution}
\begin{align*} 
    2\cdot (3 + 5)^2 - 4\cdot 6 + 8 &= 2\cdot (8)^2 - 4\cdot 6 + 8 && (\text{1. Parentes})\\
    \\
    &= 2\cdot 64 - 4\cdot 6 + 8 && (\text{2. Eksponent}) \\
    \\
    &= 128 - 24 + 8 && (\text{3. Multiplikasjon})\\
    \\
    &= 112 && (\text{4. Addisjon})
\end{align*}
::::

:::::

Vi kan også utføre regnestykker av denne typen med Pythonkode. I eksemplet nedenfor vises vi noen av de vanlige regneoperasjonene:

:::::{explore} Utforsk 1
Nedenfor vises noen regnestykker som skrives ut i Python. 

Les programmet og forutsi hva som skrives ut av programmet. Skriv inn hypotesen din og sjekk svaret ditt!

:::{interactive-code}
---
predict:
---
print(3 + 4) # addisjon
print(3 - 4) # subtraksjon
print(3 * 4) # multiplikasjon
print(3 / 4) # divisjon
print(3 ** 4) # potens
:::

:::::

---


:::::{underveisoppgave} Underveisoppgave 2
Bruk kodevinduet nedenfor til å regne ut og skrive ut svarene til følgende uttrykk:

* $8 + 2$
* $8 - 2$
* $8 \cdot 2$
* $\dfrac{8}{2}$
* $8^2$

:::{interactive-code}
# Din kode her

:::

::::{answer}
:::{code-block} python
---
linenos: true
---
print(8 + 2)
print(8 - 2)
print(8 * 2)
print(8 / 2)
print(8 ** 2)
:::
som gir utskriften

:::{code-block} console
10
6
16
4.0
64
:::
::::

:::::
