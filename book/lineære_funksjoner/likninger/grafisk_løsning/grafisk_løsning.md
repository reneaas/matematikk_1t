# Grafisk løsning


:::{admonition} Læringsmål: grafisk løsning av lineære likninger
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Kunne løse lineære likninger ved hjelp av den grafiske representasjonen til lineære funksjoner.
* Kunne forklare hva nullpunktet til en funksjon er og hvordan det henger sammen med grafen til en funksjon og en lineær likning. 
:::

Å løse likninger grafisk betyr at vi bruker den grafiske representasjonen til én eller flere funksjoner til å løse likningen ved å se på skjæringen mellom grafer.

## Lineære likninger av typen $ax + b = 0$
Vi skal starte med å se på lineære likninger av typen $ax + b = 0$. 


::::{admonition} Nullpunkter vs røtter
---
class: sidenote, margin
---
Nullpunkter kalles ofte for **røttene** til en funksjon. Dette er bare et annet mye brukt begrep for det samme. Begrepet har *ingenting* med kvadratrøtter eller $n$-te røtter å gjøre.
::::

::::{admonition} Lineære likninger på formen $ax + b = 0$
---
class: theory
---
Løsningen av likningen

$$
ax + b = 0,
$$

svarer til $x$-koordinaten til skjæringspunktet mellom $x$-aksen og grafen til den lineære funksjonen 

$$
f(x) = ax + b.
$$

Vi kaller dette for **nullpunktet** til funksjonen.  

{numref}`fig-lineære-funksjoner-likninger-grafisk-teori-1` illustrerer ideen.

:::{figure} ./figurer/teori/ax+b=0.svg
---
name: fig-lineære-funksjoner-likninger-grafisk-teori-1
width: 80%
---
viser grafen til en lineær funksjon $f(x) = ax + b$ og skjæringen med $x$-aksen. Løsningen av likningen $ax + b = 0$ er $x$-koordinaten til skjæringspunktet $(x_0, 0)$.
:::

::::

---

:::::{admonition} Eksempel 1: likning av typen $ax + b = 0$
---
class: example
---
Løs likningen

$$
2x - 4 = 0.
$$

::::{admonition} Løsning
---
class: solution
---

For å løse denne likningen grafisk, tegner vi grafen til funksjonen 

$$
f(x) = 2x - 4,
$$

og undersøker hvor grafen skjærer $x$-aksen (vi finner nullpunktet!). 

Vi kan se grafen til $f$ i {numref}`fig-lineære-funksjoner-likninger-grafisk-eksempel-1`. 

:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-lineære-funksjoner-likninger-grafisk-eksempel-1
width: 90%
---

Grafen til $f(x) = 2x - 4$. Grafen skjærer $x$-aksen i $x = 2$. 
:::
Siden grafen skjærer $x$-aksen i $x = 2$, vil løsningen av likningen være 

$$
x = 2.
$$ 

::::
:::::

---

Så er det **din tur**!


:::::{admonition} Underveisoppgave 1
---
class: check
---
I {numref}`lineære-likninger-grafisk-underveisoppgave-1` vises grafen til en lineær funksjon $f$ som er gitt ved

$$
f(x) = -2x + 6.
$$ 

Bestem nullpunktet til $f$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: lineære-likninger-grafisk-underveisoppgave-1
width: 80%
---

Viser grafen til $f(x) = -2x + 6$. 
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 3
$$
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må bestemme hvor grafen til $f$ skjærer $x$-aksen. I {numref}`fig-lineære-funksjoner-likninger-grafisk-underveisoppgave-1-løsning` har vi annotert hvor grafen skjærer $x$-aksen. 


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1_løsning.svg
---
name: fig-lineære-funksjoner-likninger-grafisk-underveisoppgave-1-løsning
width: 90%
---
viser en annotert versjon av {numref}`lineære-likninger-grafisk-underveisoppgave-1` som tydelig viser skjæringen mellom grafen til $f$ og $x$-aksen. Grafen skjærer $x$-aksen i $x = 3$.
:::

Vi kan se at grafen skjærer $x$-aksen i $x = 3$. Dermed er nullpunktet til $f$ gitt ved $x = 3$.
::::

:::::

---

## Likninger på formen $ax + b = k$
Vi skal nå se på likninger av typen $ax + b = k$. 

::::{admonition} Lineære likninger på formen $ax + b = k$
---
class: theory
---
Løsningen av likningen 

$$
ax + b = k,
$$

svarer til $x$-koordinaten til skjæringspunktet mellom grafene til de lineære funksjonene

$$
f(x) = ax + b \quad \text{og} \quad g(x) = k.
$$


:::{figure} ./figurer/teori/ax+b=k.svg
---
name: fig-lineære-funksjoner-likninger-grafisk-teori-2
width: 80%
---
viser grafen til to lineære funksjoner $f(x) = ax + b$ og $g(x) = k$ og skjæringen mellom dem. Løsningen av likningen er $ax + b = k$ er $x$-koordinaten til skjæringspunktet, som navngitt $x_0$.
::::

Vi går løs på et eksempel:

:::::{admonition} Eksempel 2: likning av typen $ax + b = k$
---
class: example
---
Løs likningen

$$
2x + 3 = 5. 
$$

::::{admonition} Løsning
---
class: solution
---
Vi starter med å lage en grafisk representasjon av funksjonene 

$$
f(x) = 2x + 3 \quad \text{og} \quad g(x) = 5.
$$

Grafene til $f$ og $g$ er vist i {numref}`lineære-likninger-grafisk-eksempel-2`. I figuren har vi også annotert hvor grafene skjærer hverandre.

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: lineære-likninger-grafisk-eksempel-2
width: 90%
---
Grafen til $f(x) = 2x + 3$ og $g(x) = 5$. 
:::

Skjæringspunktet mellom de to grafene er $(1, 5)$ som har $x$-koordinaten $x = 1$. Dermed er løsningen av likningen 

$$
2x + 3 = 5 \, \iff \, x = 1.
$$
::::
:::::

---

Så var det over til **deg igjen**!

::::{admonition} Underveisoppgave 2
---
class: check
---
Under vises en interaktiv figur med de lineære funksjonene 

$$
f(x) = 2x + 3 \quad \text{og} \quad g(x) = k.
$$

Du kan endre på verdien til $k$ med en slider.

<!-- :::{raw} html
---
file: ./figurer/interaktive_plot/lineær_likning_2x+3=k.html
---
::: -->

:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_2.html
---
:::

````{tab-set}
```{tab-item} Deloppgave 1
Bruk den interaktive figuren til å bestemme løsningen av likningen 

$$
2x + 3 = -3.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = -3$. 
::: 


:::{admonition} Løsning
---
class: solution, dropdown
---
Setter vi $k = -3$, så skjærer grafen til $f$ og linja $y = -3$ i $(x, y) = (-3, -3)$. Løsningen av likningen er derfor $x = -3$.
::: 


```

```{tab-item} Deloppgave 2
Bruk den interaktive figuren til å bestemme løsningen av likningen

$$
2x + 3 = 1
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = -1$.
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
Setter vi $k = 1$, så skjærer grafen til $f(x)$ og linja $y = 1$ i $(x, y) = (-1, 1)$. Løsningen av likningen er derfor $x = -1$.
::: 
```

````

::::


## Likninger på formen $ax + b = cx + d$

Vi skal nå se på likninger av typen $ax + b = cx + d$. 

::::{admonition} Lineære likninger på formen $ax + b = cx + d$
---
class: theory
---
Løsningen av likningen 

$$
ax + b = cx + d,
$$

svarer til $x$-koordinaten til skjæringspunktet mellom grafene til de to lineære funksjonene

$$
f(x) = ax + b \quad \text{og} \quad g(x) = cx + d.
$$

I {numref}`fig-lineære-funksjoner-likninger-grafisk-teori-3` er dette illustrert.


:::{figure} ./figurer/teori/ax+b=cx+d.svg
---
name: fig-lineære-funksjoner-likninger-grafisk-teori-3
width: 80%
---
Viser grafene til to lineære funksjoner $f(x) = ax + b$ og $g(x) = cx + d$ og skjæringen mellom dem. Løsningen av likningen er $ax + b = cx + d$ er $x$-koordinaten til skjæringspunktet, som navngitt $x_1$.
:::

::::

Vi går løs på et eksempel:

:::::{admonition} Eksempel 3: likning av typen $ax + b = cx + d$
---
class: example
---
Løs likningen

$$
x - 1 = -x + 3.
$$

::::{admonition} Løsning
---
class: solution
---
Vi tegner opp funksjonene til de lineære funksjonene:

$$
f(x) = x - 1 \quad \text{og} \quad g(x) = -x + 3.
$$

Grafene til $f$ og $g$ er vist i {numref}`lineære-likninger-grafisk-eksempel-3`. I figuren har vi også annotert hvor grafene skjærer hverandre.

:::{figure} ./figurer/eksempler/eksempel_3.svg
:name: lineære-likninger-grafisk-eksempel-3
:width: 80%

viser grafene til $f(x) = x - 1$ og $g(x) = -x + 3$. 
:::

Grafene skjærer hverandre i punktet $(x, y) = (2, 1)$. Løsningen er $x$-koordinaten til skjæringspunktet som er $x = 2$. Dermed har vi at løsningen er 

$$
x - 1 = -x + 3 \, \iff \, x = 2.
$$
::::
:::::

**Din tur**!

::::{admonition} Underveisoppgave 3
:class: check
I {numref}`lineære-likninger-grafisk-underveisoppgave-3`, vises grafene til funksjonene

$$
f(x) = -2x + 1 \quad \text{og} \quad g(x) = x - 2.
$$

Bruk grafene til å løse likningen

$$
-2x + 1 = x - 2.
$$

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
:name: lineære-likninger-grafisk-underveisoppgave-3
:width: 80%

Grafene til $f(x) = -2x + 1$ og $g(x) = x - 2$. 
:::

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 1
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution 
---
I {numref}`lineære-likninger-grafisk-underveisoppgave-3-løsning` ser vi en utvidet versjon av {numref}`lineære-likninger-grafisk-underveisoppgave-3` der vi har markert skjæringspunktet mellom grafene, og har lagt inn en annotering av løsningen av likningen. 

```{figure} ./figurer/underveisoppgaver/underveisoppgave_3_løsning.svg
---
name: lineære-likninger-grafisk-underveisoppgave-3-løsning
width: 90%
---
viser grafene til $f$ og $g$, samt skjæringspunktet $(1, -1)$ og annotering av løsningen til likningen $f(x) = g(x)$. 
```

Fra {numref}`lineære-likninger-grafisk-underveisoppgave-3-løsning` kan vi se at $x$-koordinaten til skjæringspunktet er $x = 1$. Dermed er løsningen av likningen 

$$
-2x + 1 = x - 2
$$

gitt ved 

$$
x = 1.
$$


:::
::::

<!-- 
## Ingen, én eller uendelig mange løsninger
Eksemplene vi har sett på så langt har hatt én løsning, men det finnes også lineære likninger som har ingen løsninger, eller uendelig mange løsninger. 

::::{admonition} Eksempel 4: likninger uten løsninger
:class: example

Likningen

$$
x + 1 = x + 3,
$$

er et eksempel på en likningen uten noen løsning. Grafisk svarer dette til to parallelle linjer, som vi kan se i {numref}:lineære-likninger-grafisk-eksempel-4:.

:::{figure} ./figurer/eksempler/eksempel_4.svg
:name: lineære-likninger-grafisk-eksempel-4
:width: 80%

Likningen $x + 3 = x + 1$ har ingen løsninger siden grafene til $f(x) = x+1$ og $g(x) = x + 3$ aldri skjærer hverandre.
:::

::::

::::{admonition} Eksempel 5: uendelige mange løsninger
:class: example

Likningen 

$$
2(x+1) = 2x + 2,
$$ 

vil ha uendelig mange løsninger siden det er en **identitet**. Husk at med dette begrepet, så mener vi at likningen er sann for **alle** verdier av $x$. Grafisk svarer dette til to overlappende grafer, som vi kan se i {numref}:lineære-likninger-grafisk-eksempel-5:.

:::{figure} ./figurer/eksempler/eksempel_5.svg
:name: lineære-likninger-grafisk-eksempel-5
:width: 80%

Grafene til $f(x) = 2x + 2$ og $g(x) = 2(x+1)$ overlapper fordi likningen $2(x + 1) = 2x + 2$ er en identitet. 
:::
:::: -->
