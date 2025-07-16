# Regning med Python


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke Python til å løse enkle regnestykker.
* Kunne bruke Python til å regne med formler
:::




Python kan på mange måter sees på som en kraftfull og fleksibel kalkulator. Den kan brukes for å regne ut en enkel matematisk formel, men også gjennomføre millioner av utregninger i løpet av noen få sekunder. 

## Regnearter i Python

Vi starter med å bli kjent med de vanlige regneartene vi bruker i matematikken.

:::{margin} `print`{l=python}-funksjonen
I Python bruker vi `print`{l=python} for å skrive ut noe fra et program. For eksempel vil `print(8 + 2)`{l=python} skrive svaret på regnestykket `8 + 2`{l=python}.
:::

:::::{admonition} Utforsk 1
---
class: explore
---

::::{tab-set}
---
class: tabs-parts
---
:::{tab-item} a
Nedenfor vises et program som bruker de ulike regneartene i Python til å regne ut noe og skrive ut svaret.

Les programmet og forutsi hva som skrives ut. Skriv inn hypotesen din under for å sjekke.

```{interactive-code}
---
predict: true
---
print(8 + 2)            # Pluss
print(8 - 2)            # Minus
print(8 * 2)            # Gange
print(8 / 2)            # Dele
print(8 ** 2)           # Potens
```
:::

:::{tab-item} b
Bruk programmet til å regne ut svarene på følgende regnestykker:

* $3 + 4$
* $3 - 4$
* $3 \cdot 4$
* $\dfrac{3}{4}$
* $3^4$

```{interactive-code}
# Skriv din kode her



```

````{admonition} Fasit
---
class: dropdown, answer
---
```{code-block} python
---
linenos: true
---
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 ** 4) 
```
````
:::
::::

<br>


:::::


::::{summary} Regneartene i Python

| Operasjon | Symbol i Python | Kodeeksempel | Matematikk |
| --- | --- | --- | --- |
| Addisjon | `+`{l=python} | `3 + 4`{l=python} | $3 + 4$ |
| Subtraksjon | `-`{l=python} | `3 - 4`{l=python} |  $3 - 4$ |
| Multiplikasjon | `*`{l=python} | `3 * 4`{l=python} | $3 \cdot 4$ |
| Divisjon | `/`{l=python} | `3 / 4`{l=python} | $\dfrac{3}{4}$ |
| Potens | `**`{l=python} | `3 ** 4`{l=python} | $3^4$ |

::::


:::::::::::::::{exercise} Underveisoppgave 1 
Ta quizen!

:::{quiz}
Q: Hva skrives ut av programmet? <pre><code class="python">print(2 * 3 + 5)</code></pre>
+ $11$
- $16$
- $10$
- $30$

Q: Hva skrives ut av programmet? <pre><code class="python">x = 2 \ny = 3 * x + 6 \n\nprint(y)</code></pre>
+ $12$
- $24$
- $6$
- $15$

:::



:::::::::::::::



## Formler

Det er sjelden vi skriver regnestykker manuelt slik som vi så på i utforsk 1. Vi er oftest interessert i å regne ut noe med en formel som inneholder variabler. Vi ønsker med andre ord å bruke Python som en avansert kalkulator.


:::::{admonition} Utforsk 2: formler
---
class: explore
---
Strekning, fart og tid er tre størrelser som henger sammen. Vi kan bruke formelen 

$$
s = v\cdot t
$$

til å regne ut strekningen $s$ dersom vi har farten $v$ og tiden $t$. 

::::{tab-set}
---
class: tabs-parts
---

:::{tab-item} a
I programkoden under regnes det ut en strekning $s$ basert på en fart $v$ og en tid $t$.

Les programmet og forutsi hva som skrives ut. Skriv inn hypotesen din under for å sjekke.
:::

:::{tab-item} b
Bruk programmet til å regne ut strekningen når $v = 80 \ \mathrm{km / h}$ og $t = 2.5 \ \mathrm{h}$.

Hva blir strekningen?

````{admonition} Fasit
---
class: dropdown, answer
---
```{code-block} python
---
linenos: true
---
v = 80          # kilometer per time
t = 2.5         # timer

s = v * t       # strekning i kilometer

print(s)
```
````
:::

:::{tab-item} c
En bil kjører i $90 \ \mathrm{km / h}$ og kjører en avstand på $342 \ \mathrm{km}$. 

Juster programmet slik at du kan regne ut tiden det tok å kjøre denne strekningen. Hvor lang tid tok det?

````{admonition} Fasit
---
class: dropdown, answer
---
Vi kan enten prøve oss frem med ulike verdier av $t$ til vi får riktig avstand, eller så kan vi skrive om formelen til å regne ut tiden $t$:

$$
t = \dfrac{s}{v}
$$
```{code-block} python
---
linenos: true
---
v = 90
s = 342

t = s / v

print(t)
```
````
:::
::::

<br>



:::{interactive-code}
---
predict: true
---
v = 20      # kilometer per time
t = 2       # timer

s = v * t   # strekning i kilometer

print(s)
:::

::::: 

