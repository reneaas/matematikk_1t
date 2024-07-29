# Regning med Python


```{admonition} Læringsmål: regning med Python
:class: tip

Etter å ha lest dette delkapittelet, er målet at du skal kunne:
* Bruke python til å regne ut enkle og sammensatte regnestykker.
```

Python kan på mange måter sees på som en kraftfull og fleksibel kalkulator som lar oss regne matematisk på en måte vi ikke ellers kan gjøre på noen annen måte. Dette kan være å gjenta en utregning millioner av ganger frem til vi oppnår et ønsket resultat, eller bare regne ut en enkel matematisk formel. 

## Regneoperasjoner i Python

Vi starter med de viktigste regneoperasjonene

```{admonition} Divisjon og brøker
:class: note, margin

I Python, så vil en brøk alltid regnes ut til et heltall (`int`{l=python}) eller et desimaltall (`float`{l=python}). Det er ingen innebygd måte å representere brøker på direkte.
```

````{admonition} Viktige regneoperasjoner i Python
:class: theory

| Operasjon | Symbol i Python | Kodeeksempel | Matematikk |
| --- | --- | --- | --- |
| Addisjon | `+`{l=python} | `3 + 4`{l=python} | $3 + 4$ |
| Subtraksjon | `-`{l=python} | `3 - 4`{l=python} |  $3 - 4$ |
| Multiplikasjon | `*`{l=python} | `3 * 4`{l=python} | $3 \cdot 4$ |
| Divisjon | `/`{l=python} | `3 / 4`{l=python} | $\dfrac{3}{4}$ |
| Potens | `**`{l=python} | `3 ** 4`{l=python} | $3^4$ |

````

Vi tar noen eksempler og ser hva vi får ut

````{admonition} Eksempel 1: enkle regneoperasjoner
:class: example

| Kode | Resultat | Matematikk |
| --- | --- | --- |
| `1 + 5`{l=python} | `6`{l=python} | $1 + 5 = 6$ |
| `3 - 2`{l=python} | `1`{l=python} | $3 - 2 = 1$ |
| `2 * 4`{l=python} | `8`{l=python} | $2 \cdot 4 = 8$ |
| `4 / 2`{l=python} | `2.0`{l=python} | $\dfrac{4}{2} = 2$ |
| `2 / 4`{l=python} | `0.5`{l=python} | $\dfrac{2}{4} = 2$ |
| `2 ** 4`{l=python} | `16`{l=python} | $2^4 = 16$ |

````

**Din tur**! 

````{admonition} Underveisoppgave 1
:class: check

Fyll ut tabellen under:

| Kode | Resultat |
| --- | --- |
| `-1 + 3`{l=python} |  |
| `5 - (-2)`{l=python} |  |
| `3 * 2`{l=python} |  |
| `6 / 3`{l=python} |  |
| `3 ** 3`{l=python} |  |
| `2 / 5`{l=python} | |
| `2 * (-1)`{l=python} | |
| `(-2) ** 3`{l=python} |

```{admonition} Løsning
:class: solution, dropdown

| Kode | Resultat |
| --- | --- |
| `-1 + 3`{l=python} | `2`{l=python} |
| `5 - (-2)`{l=python} | `7`{l=python} |
| `3 * 2`{l=python} | `6`{l=python} |
| `6 / 3`{l=python} | `2.0`{l=python} |
| `3 ** 3`{l=python} | `27`{l=python} |
| `2 / 5`{l=python} | `0.4`{l=python} |
| `2 * (-1)`{l=python} | `-2`{l=python} |
| `(-2) ** 3`{l=python} | `-8`{l=python} |

```

````

## Regnerekkefølge

Python følger samme regnerekkefølge du har møtt i matematikken, bortsett fra at divisjon kommer alltid før multiplikasjon. 

````{admonition} Regnerekkefølge i Python
:class: theory
Regnerekkefølgen i Python er:

1. Parenteser
2. Potenser
3. Divisjon
4. Multiplikasjon
5. Addisjon og subtraksjon

````

Vi tar et eksempel:

````{admonition} Eksempel 2: regnerekkefølgen
:class: example

Under vises en kode der vi regner ut et regnestykke og lagrer resultatet i en variabel. Men hva blir verdien som skrives ut av programmet?

```{code-block} python
---
linenos:
---

resultat = (-1 + 3) ** 4 / 2 * 3 - 4
print(f"{resultat = }")
```
Her vil Python gjør regnestykket slik:

1. $(-1 + 3) = 2$ (parentes)
2. $2^4 = 16$ (potens)
3. $16 / 2 = 8$ (divisjon)
4. $8 \cdot 3 = 24$ (multiplikasjon)
5. $24 - 4 = 20$ (subtraksjon)


Så det som skrives ut av programmet er 

```console 
resultat = 20
```

Merk spesielt
: Divisjon gjøres alltid etter multiplikasjon. For eksempel blir `4 / 2 * 2 = 4`{l=python}. Hvis du ønsker at multiplikasjon med en nevner skal skje først, må du skrive med parentes: `4 / (2 * 2) = 1`{l=python}.
````

**Din tur!**


`````{admonition} Underveisoppgave 2
:class: check

Bestem verdien til hver av variablene i programmet under:

**Regn for hånd!** Du kan kjøre programmet for å sjekke svaret ditt før du ser på løsningen.

````{code-block} python
---
linenos:
---

a = 2 + 3 * 4
b = 2 * (3 + 4)
c = 2 ** 4 / 2
p = 2 ** (4 / 2)
r = 3 ** 4 / 9 * 2 - 2
q = (5 - 2) ** (1 + 3) / (5 + 4) * 2 - 3 + 1


# Printer ut verdiene til variablene under hverandre
print(a, b, c, p, r, q, sep="\n")
````

````{admonition} Løsning
:class: solution, dropdown

Vi følger regnerekkefølgen til punkt og prikke:

| Variabel | Resultat | Utregning |
| --- | --- | --- |
| `a`{l=python} | `14`{l=python} | $2 + 3 \cdot 4 = 2 + 12 = 14$ |
| `b`{l=python} | `14`{l=python} | $2 \cdot (3 + 4) = 2 \cdot 7 = 14$ |
| `c`{l=python} | `8.0`{l=python} | $2^4 / 2 = 16 / 2 = 8$ |
| `p`{l=python} | `4.0`{l=python} | $2^{4/2} = 2^2 = 4$ |
| `r`{l=python} | `16.0`{l=python} | $\dfrac{3^4}{9} \cdot 2 - 2 = \dfrac{81}{9} \cdot 2 - 2 = 18 - 2 = 16$ |
| `q`{l=python} | `16.0`{l=python} | $\dfrac{(5-2)^{1+3}}{(5+4)}\cdot 2 - 3 + 1 = \dfrac{3^4}{9} \cdot 2 - 2 = 16$ |

````


`````


## Oppgaver

`````{admonition} Oppgave 1
:class: problem-level-1

Bruk Python til å regne ut

$$
a = 2\cdot 8 - \frac{1}{2}\cdot 2
$$

og skriv ut verdien. 

Du kan ta utgangspunkt i kodeskallet under. Du må fylle ut linje 1.

```{code-block} python
---
linenos:
emphasize-lines: 1
---
a = 
print(f"{a = }")
```

````{admonition} Løsning
:class: solution, dropdown

Vi kan skrive
```{code-block} python
---
linenos:
emphasize-lines: 1
---
a = 2 * 8 - 1 / 2 * 2
print(f"{a = }")
```

som gir utskriften

```console
a = 15.0
```
````
`````


`````{admonition} Oppgave 2
---
class: problem-level-1
---
En elev har forsøkt å regne ut 

$$
r = \frac{2^3}{4\cdot 2} + \frac{1}{2}
$$

men har skrevet feil i koden. Rett opp i programmet.

````{code-block} python
---
linenos:
---

r = 2 * 3 / 4 * 2 + 1 / 2
print(f"{r = }")
````

````{admonition} Løsning
---
class: solution, dropdown
---
Eleven har gjort to feil:
* Eleven prøver å regne ut $2^3$ som `2 * 3`{l=python} i stedet for `2 ** 3`{l=python}.
* Eleven har glemt at man må ta med parentes for å gjøre multiplikasjon i nevneren. Dermed blir koden i stedet

````{code-block} python
---
linenos:
---

r = 2 ** 3 / (4 * 2) + 1 / 2
print(f"{r = }")
````
`````
