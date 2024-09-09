# Grafisk løsning


```{admonition} Læringsmål: grafisk løsning av lineære likninger
:class: tip
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Løse lineære likninger grafisk av typene:
    - $ax + b = 0$
    - $ax + b = k$
    - $ax + b = cx + d$
* Forstå sammenhengen mellom likninger, nullpunkter og skjæring mellom grafene til funksjoner.
```

Å løse likninger grafisk betyr at vi bruker den grafiske representasjonen til en eller flere funksjoner til å løse likningen ved å se på skjæringen mellom grafer.

## Lineære likninger av typen $ax + b = 0$
Vi skal starte med å se på lineære likninger av typen $ax + b = 0$. 


::::{admonition} Nullpunkter vs røtter
---
class: sidenote, margin
---
Nullpunkter kalles ofte for **røttene** til en funksjon. Dette er bare et annet mye brukt begrep for det samme. Begrepet har *ingenting* med kvadratrøtter eller $n$-te røtter å gjøre.
::::

````{admonition} Lineære likninger på formen $ax + b = 0$
:class: theory
Gitt en lineær funksjon $f(x) = ax + b$, så vil løsningen av likningen

$$
ax + b = 0,
$$

svare til $x$-verdien til skjæringen mellom $x$-aksen og grafen til $f$. Vi kaller dette for **nullpunktet** til funksjonen.  

:::{figure} ./figurer/teori/nullpunkter.svg
---
name: lineære-likninger-grafisk-nullpunkt
width: 80%
---
Viser grafen til en lineær funksjon $f(x) = ax + b$ og skjæringen med $x$-aksen. Løsningen av likningen $ax + b = 0$ er $x$-koordinaten til skjæringspunktet, som er navngitt $x_1$.
:::

````

````{admonition} Eksempel 1: likning av typen $ax + b = 0$
:class: example
Vi tar utgangspunkt i likningen

$$
2x - 4 = 0.
$$

For å løse denne likningen grafisk, tegner vi grafen til funksjonen $f(x) = 2x - 4$, og undersøker hvor grafen skjærer $x$-aksen (vi finner nullpunktet!). Vi kan se grafen til $f$ i {numref}`lineære-likninger-grafisk-eksempel-1`. 

```{figure} ./figurer/eksempler/eksempel_1.svg
:name: lineære-likninger-grafisk-eksempel-1
:width: 80%

Grafen til $f(x) = 2x - 4$. Grafen skjærer $x$-aksen i $x = 2$. 
```
Siden grafen skjærer $x$-aksen i $x = 2$, vil løsningen av likningen være $x = 2$. 
````

Så er det **din tur**!

````{admonition} Underveisoppgave 1
:class: check

En lineær funksjon er gitt ved 

$$
g(x) = -2x + 6.
$$ 

Grafen til $g$ vises i {numref}`lineære-likninger-grafisk-underveisoppgave-1`.

Bestem nullpunktet til $g$.

```{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
:name: lineære-likninger-grafisk-underveisoppgave-1
:width: 80%

Viser grafen til $g(x) = -2x + 6$. 
```

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 3
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan se at grafen skjærer $x$-aksen i $x = 3$. Dermed er $x = 3$ nullpunktet til $g$. 
:::

````

## Likninger på formen $ax + b = k$
Vi skal nå se på likninger av typen $ax + b = k$. 

````{admonition} Lineære likninger på formen $ax + b = k$
:class: theory

Gitt en lineær funksjon $f(x) = ax + b$, så vil løsningen av likningen

$$
ax + b = k,
$$

svare til $x$-verdien til skjæringen mellom grafen til $f$ og en horisontal linje $y = k$. 

:::{figure} ./figurer/teori/skjæring_lineær_fn_horisontal_linje.svg
---
name: lineær-likning-grafisk-skjæring-horisontal-linje
width: 80%
---
Viser grafen til en lineær funksjon $f(x) = ax + b$ og skjæringen med en horisontal linje $y = k$. Skjæringspunktet mellom grafen til $f$ og linja $y = k$ er markert. Løsningen av likningen $ax + b = k$ er $x$-koordinaten til skjæringspunkt, som er navngitt $x_1$.
````

Vi går løs på et eksempel:

````{admonition} Eksempel 2: likning av typen $ax + b = k$
:class: example
Vi skal løse likningen

$$
2x + 3 = 5,
$$

grafisk. Vi tegner grafen til den lineære funksjonen $f(x) = 2x + 3$, og undersøker for hvilken $x$-verdi grafen skjærer linja $y = 5$. Grafen til $f$ og linja $y = 5$ er tegnet inn i {numref}`lineære-likninger-grafisk-eksempel-2`.

```{figure} ./figurer/eksempler/eksempel_2.svg
:name: lineære-likninger-grafisk-eksempel-2
:width: 80%

Grafen til $f(x) = 2x + 3$ og linja $y = 5$. 
```

Vi kan se at grafen til $f$ skjærer linja $y = 5$ i punktet $(x, y) = (1, 5)$ som betyr at løsningen av likningen er $x = 1$. 
````

Så var det over til **deg igjen**!

````{admonition} Underveisoppgave 2
:class: check
Under vises et interaktivt plott av den lineære funksjon $f(x) = 2x + 3$ og en linje $y = k$. <br>
Du kan endre på linja $y = k$. 

```{raw} html
---
file: ./figurer/interaktive_plot/lineær_likning_2x+3=k.html
---
```

<br>

Deloppgave 1
: Bestem løsningen av likningen $2x + 3 = -3$

:::{admonition} Fasit: deloppgave 1
---
class: answer, dropdown
---
$$
x = -3
$$
:::

:::{admonition} Løsning: deloppgave 1 
---
class: solution, dropdown
---
Setter vi $k = -3$, så skjærer grafen til $f$ og linja $y = -3$ i $(x, y) = (-3, -3)$. Løsningen av likningen er derfor $x = -3$.
::: 

<br>

Deloppgave 2
: Bestem løsningen av likningen $2x + 3 = 1$

:::{admonition} Fasit: deloppgave 2
---
class: answer, dropdown
---
$$
x = -1
$$
:::

:::{admonition} Løsning: deloppgave 2
---
class: solution, dropdown
---
Setter vi $k = 1$, så skjærer grafen til $f(x)$ og linja $y = 1$ i $(x, y) = (-1, 1)$. Løsningen av likningen er derfor $x = -1$.
::: 

<br>

Deloppgave 3
: Bestem hvilken linje $y = k$ som gir løsningen $x = -2$.

:::{admonition} Fasit: deloppgave 3
---
class: answer, dropdown
---
$$
k = -1
$$
:::

:::{admonition} Løsning: deloppgave 3
---
class: solution, dropdown
---
Grafen til $f(x)$ går gjennom punktet $(x, y) = (-2, -1)$, som betyr at når $y = -1$, så er $x = -2$. Dermed vil $k = -1$ gi løsningen $x = -2$.
::: 

````


## Likninger på formen $ax + b = cx + d$

Vi skal nå se på likninger av typen $ax + b = cx + d$. 

````{admonition} Lineære likninger på formen $ax + b = cx + d$
:class: theory
Gitt to lineære funksjoner

$$
f(x) = ax + b \quad \text{og} \quad g(x) = cx + d,
$$

så svarer løsningen av likningen

$$
ax + b = cx + d,
$$

til $x$-koordinaten til skjæringspunktet mellom grafene til $f$ og $g$. 

:::{figure} ./figurer/teori/skjæring_mellom_to_lineære_fn.svg
---
name: lineære-likninger-grafisk-skjæring-to-lineære-fn
width: 80%
---
Viser grafene til to lineære funksjoner $f(x) = ax + b$ og $g(x) = cx + d$ og skjæringen mellom dem. Løsningen av likningen er $ax + b = cx + d$ er $x$-koordinaten til skjæringspunktet, som navngitt $x_1$.
:::

````

Vi går løs på et eksempel:

````{admonition} Eksempel 3: likning av typen $ax + b = cx + d$
:class: example
Vi skal løse likningen 

$$
x - 1 = -x + 3.
$$

Grafisk løser vi dette ved å tegne grafene til de lineære funksjonene

$$
f(x) = x - 1 \quad \text{og} \quad g(x) = -x + 3,
$$

og så ser vi på skjæringen mellom grafene til de to funksjonene. $x$-verdien til skjæringspunktet vil være løsningen av likningen. Grafene til $f$ og $g$ er tegnet inn i {numref}`lineære-likninger-grafisk-eksempel-3`.

```{figure} ./figurer/eksempler/eksempel_3.svg
:name: lineære-likninger-grafisk-eksempel-3
:width: 80%

Grafen til $f(x) = x - 1$ og $g(x) = -x + 3$. 
```

Grafene skjærer hverandre i punktet $(x, y) = (2, 1)$, som betyr at løsningen av likningen er $x = 2$. 

````

**Din tur**!

````{admonition} Underveisoppgave 3
:class: check
I {numref}`lineære-likninger-grafisk-underveisoppgave-3`, vises grafene til funksjonene

$$
f(x) = -2x + 1 \quad \text{og} \quad g(x) = x - 2.
$$

Bruk grafene til å løse likningen

$$
-2x + 1 = x - 2.
$$

```{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
:name: lineære-likninger-grafisk-underveisoppgave-3
:width: 80%

Grafene til $f(x) = -2x + 1$ og $g(x) = x - 2$. 
```

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
Fra figuren ser vi at de to linjene krysser hverandre når $x = 1$. Løsningen av likningen er derfor $x = 1$
:::
````


## Ingen, én eller uendelig mange løsninger
Eksemplene vi har sett på så langt har hatt én løsning, men det finnes også lineære likninger som har ingen løsninger, eller uendelig mange løsninger. 

````{admonition} Eksempel 4: likninger uten løsninger
:class: example

Likningen

$$
x + 1 = x + 3,
$$

er et eksempel på en likningen uten noen løsning. Grafisk svarer dette til to parallelle linjer, som vi kan se i {numref}`lineære-likninger-grafisk-eksempel-4`.

```{figure} ./figurer/eksempler/eksempel_4.svg
:name: lineære-likninger-grafisk-eksempel-4
:width: 80%

Likningen $x + 3 = x + 1$ har ingen løsninger siden grafene til $f(x) = x+1$ og $g(x) = x + 3$ aldri skjærer hverandre.
```

````

````{admonition} Eksempel 5: uendelige mange løsninger
:class: example

Likningen 

$$
2(x+1) = 2x + 2,
$$ 

vil ha uendelig mange løsninger siden det er en **identitet**. Husk at med dette begrepet, så mener vi at likningen er sann for **alle** verdier av $x$. Grafisk svarer dette til to overlappende grafer, som vi kan se i {numref}`lineære-likninger-grafisk-eksempel-5`.

```{figure} ./figurer/eksempler/eksempel_5.svg
:name: lineære-likninger-grafisk-eksempel-5
:width: 80%

Grafene til $f(x) = 2x + 2$ og $g(x) = 2(x+1)$ overlapper fordi likningen $2(x + 1) = 2x + 2$ er en identitet. 
```
````
