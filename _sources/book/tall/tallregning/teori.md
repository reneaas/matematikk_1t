# Tallregning 

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke regnerekkefølgen
* Kunne forklare hva et primtall er, og primtallsfaktorisere hele tall. 
* Kunne anvende brøkregler i regning
* Kunne forenkle kvadratrøtter
:::




## Regnerekkefølgen

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

:::::{exercise} Underveisoppgave 1
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



## Brøkregning

Ofte jobber med vi brøker og vi foretrekker gjerne å oppgi svaret vårt som brøk fremfor å regne det ut som desimaltall. For å kunne regne med brøker må vi kjenne til hvordan vi legger sammen, trekker fra, ganger og deler brøker.


### Legge sammen brøker

Når to brøker skal legges sammen eller trekkes fra hverandre, må vi ha felles nevner i brøkene. Dette kan vi oppnå ved å utvide brøkene.

::::{summary} Legge sammen brøker
$$
\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{a \cdot d + b \cdot c}{b \cdot d}
$$
::::

Vi tar et eksempel med tall:

:::::::::::::::{example} Eksempel 2
Regn ut

$$
\dfrac{3}{4} + \dfrac{1}{6}
$$

:::::{solution}
---
dropdown: 0
---
$$
\dfrac{3}{4} + \dfrac{1}{6} = \dfrac{3 \cdot 6}{4 \cdot 6} + \dfrac{1 \cdot 4}{6 \cdot 4} = \dfrac{18}{24} + \dfrac{4}{24} = \dfrac{22}{24} = \dfrac{11}{12}
$$
:::::


:::::::::::::::



### Gange brøker

Når vi ganger to brøker, ganger vi tellerne med hverandre og nevnerne med hverandre.

::::{summary} Ganging av brøker
$$
\dfrac{a}{b} \cdot \dfrac{c}{d} = \dfrac{a \cdot c}{b \cdot d}
$$
::::

Vi tar et eksempel med tall:

:::::::::::::::{example} Eksempel 3
Regn ut

$$
\dfrac{2}{3} \cdot \dfrac{4}{5}
$$
:::::{solution}
---
dropdown: 0
---
$$
\dfrac{2}{3} \cdot \dfrac{4}{5} = \dfrac{2 \cdot 4}{3 \cdot 5} = \dfrac{8}{15}
$$
:::::
:::::::::::::::


### Dele brøker
Når vi deler en brøk med en annen, ganger vi den første brøken med den omvendte av den andre brøken.

::::{margin} Annen skrivemåte
Noen ganger skriver vi dette som

$$
\dfrac{a / b}{c / d} = \dfrac{a}{b} \cdot \dfrac{d}{c}
$$
::::

::::{summary} Deling av brøker
$$
\dfrac{a}{b} : \dfrac{c}{d} = \
\dfrac{a}{b} \cdot \dfrac{d}{c}
$$
::::

Vi tar et eksempel med tall:

:::::::::::::::{example} Eksempel 4
Regn ut

$$
\dfrac{3}{4} : \dfrac{2}{5}
$$
:::::{solution}
---
dropdown: 0
---
$$
\dfrac{3}{4} : \dfrac{2}{5} = \dfrac{3}{4} \cdot \dfrac{5}{2} = \dfrac{3 \cdot 5}{4 \cdot 2} = \dfrac{15}{8}
$$
:::::
:::::::::::::::



## Kvadratrøtter

Kvadratroten $\sqrt{a}$ av et tall $a$, er hvilket tall $b$ vi må opphøye i $2$ for å få tallet vi tar kvadratroten av. 

:::::::::::::::{summary} Kvadratrøtter
Kvadratroten $\sqrt{a}$ av et tall $a$ er det tallet positive tallet $b$ som må opphøyes i $2$ for å få $a$. Det betyr at

$$
b = \sqrt{a} \liff b^2 = a
$$

:::::::::::::::

---

:::::::::::::::{example} Eksempel 5
Regn ut

$$
\sqrt{16}
$$

::::{solution}
---
dropdown: 0
---
Vi har at $\sqrt{16} = 4$ siden $4^2 = 16$. 

::::

:::::::::::::::


---

Ved regning, kan vi i praksis bare bestemme kvadratrøttene for kvadrattallene

$$
1, 4, 9, 16, 25, \ldots
$$

Vi er avhengig av en kalkulator for å beregne en tilnærmet verdi for alle andre kvadratrøtter. Ofte ønsker vi å oppgi svaret eksakt. Da er det vanlig å forenkle svaret så mye som mulig. Da får vi bruk for følgende regneregel: 

:::::::::::::::{summary} Produktregelen for kvadratrøtter
For to tall $a$ og $b$ gjelder:

$$
\sqrt{a\cdot b} = \sqrt{a} \cdot \sqrt{b}
$$
:::::::::::::::

---

La oss se på et eksempel: 

:::::::::::::::{example} Eksempel 6
Skriv kvadratroten så enkelt som mulig:

$$
\sqrt{72}
$$


::::{solution}
---
dropdown: 0
---
$$
\sqrt{72} = \sqrt{36 \cdot 2} = \sqrt{36} \cdot \sqrt{2} = 6\sqrt{2}
$$
::::


:::::::::::::::

