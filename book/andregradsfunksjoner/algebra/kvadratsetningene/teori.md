# Kvadratsetningene

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke kvadratsetningene til å skrive om $f(x)$ fra standardformen til nullpunktsform, og motsatt.
* Kunne forklare hva en matematisk identitet er, avgjøre om en sammenheng er en identitet, og gi konkrete eksempler på identiteter. 
:::

Vi har så langt sett på de tre ulike representasjonene til en andregradsfunksjon. 

Det finnes til sammen tre kvadratsetninger. Vi skal begrunne de to første geometrisk, og den siste algebraisk.

:::{admonition} Kvadratsetningene
---
class: theory
---
Gitt to vilkårlige tall $a, b \in \mathbb{R}$, så gjelder følgende tre setninger:

1.Kvadratsetning
: $(a + b)^2 = a^2 + 2ab + b^2$

2.Kvadratsetning
: $(a - b)^2 = a^2 - 2ab + b^2$

Konjugatsetningen
: $(a + b)(a - b) = a^2 - b^2$
:::

---

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Vi har møtt på andregradsuttrykk som passer rett inn i disse tre setningene. Her viser vi ett eksempel på hver av dem. 

::::::::::::::{tab-set}
:::::::::::::{tab-item} 1.kvadratsetning
$$
(x + 3)^2 = x^2 + 2\cdot x\cdot 3 + 3^2 = x^2 + 6x + 9
$$
:::::::::::::

:::::::::::::{tab-item} 2.kvadratsetning
$$
(x - 4)^2 = x^2 - 2\cdot x\cdot 4 + 4^2 = x^2 - 8x + 16
$$
:::::::::::::

:::::::::::::{tab-item} Konjugatsetningen
$$
(x + 2)(x - 2) = x^2 - 2^2 = x^2 - 4
$$
:::::::::::::
::::::::::::::


:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bruk kvadratsetningene til å skrive om andregradsuttrykkene til standardform.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
(x + 5)^2
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x^2 + 10x + 25
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
$$
(x - 2)^2 
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x^2 - 4x + 4
$$
:::
:::::::::::::

:::::::::::::{tab-item} c
$$
(x + 4)(x - 4)
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x^2 - 16
$$
:::
:::::::::::::

::::::::::::::
:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
Bruk kvadratsetningene til å skrive om andregradsuttrykkene til nullpunktsform.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
$$
x^2 - 2x + 1
$$
:::::::::::::

:::::::::::::{tab-item} b
$$
x^2 + 12x + 36
$$
:::::::::::::

:::::::::::::{tab-item} c
$$
x^2 - 49
$$
:::::::::::::
::::::::::::::

:::::::::::::::


## Matematiske identiteter
Kvadratsetningene er eksempler på det vi kaller for en **identitet**. For eksempel vil 

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

være sann *uansett* hvilke tall $a$ og $b$ er. Da sier vi at sammenhengen er en identitet fordi den er sann uansett hvilke verdier variablene har.

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Bestem $s$ slik at sammenhengen nedenfor blir en identitet:

$$
9x^2 - 30x + 25 = (3x - s)^2.
$$

::::{admonition} Løsning
---
class: solution
---
Vi kan bruke 2.kvadratsetningen til å utvide uttrykket på høyre side:

$$
(3x - s)^2 = (3x)^2 - 2\cdot 3x\cdot s + s^2 = 9x^2 - 6sx + s^2.
$$

For at sammenhengen skal bli en identitet, må vi bestemme $s$ slik at vi får likhet for disse to uttrykkene:

$$
9x^2 - 30x + 25 = 9x^2 - 6sx + s^2
$$

Ved sammenlikning, kan vi se at dette må bety at 

$$
-30 = -6s \quad \land \quad 25 = s^2
$$

Fra den første likningen, får vi 

$$
-30 = -6s \quad \iff \quad s = 5.
$$

Fra den andre likningen får vi at

$$
s^2 = 25 \quad \iff \quad s = \pm 5.
$$

Men bare den positive løsningen gir oss en identitet, som betyr at vi må ha $s = 5$.

::::
:::::::::::::::


<!-- 
## Geometrisk begrunnelse for 1. og 2.kvadratsetning

Du skal få prøve å begrunne de to første kvadratsetningene i underveisoppgavene under. Du starter med 1.kvadratsetning:

````{admonition} Underveisoppgave 1
:class: check

I figuren under vises et kvadrat med sidelengder $a + b$ som inneholder et kvadrat med sidelengder $a$, et kvadrat med sidelenger $b$ og to rektangler med sidelengder $a$ og $b$. 

Bruk figuren til å utlede 1.kvadratsetning ved hjelp av arealberegninger. 

```{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
:name: kvadratsetningene-underveisoppgave-1
:width: 80%
```

```{admonition} Løsning 
:class: solution, dropdown

Hele kvadratet har sidelengder $a + b$ som betyr at arealet $A$ er

$$
A = (p + q)\cdot (p + q) = (p + q)^2.
$$

Vi kan også uttrykke arealet ved å summere opp arealet av de mindre figurene den består av. Da har vi

$$
A = \underbrace{p\cdot p}_{\text{Grønt kvadrat}} + \underbrace{q\cdot q}_{\text{Rødt kvadrat}} + \underbrace{2\cdot p\cdot q}_{\text{To lilla rektangler}} = p^2 + q^2 + 2pq.
$$

Men disse to arealene må være like hverandre som gir

$$
(p + q)^2 = p^2 + q^2 + 2pq = p^2 + 2pq + q^2,
$$

som er 1.kvadratsetning.
```
````

Du skal få gå løs rett på 2.kvadratsetning også!

````{admonition} Underveisoppgave 2
:class: check

I figuren under vises et ytre kvadrat med sidelengder $p$ som inneholder et kvadrat med sidelengder $p - q$, og to rektangler med sidelengder $q$ og $p - q$. 

Bruk figuren til å utlede 2.kvadratsetning ved hjelp av arealberegninger. 

```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
:name: kvadratsetningene-underveisoppgave-2
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown
Hele kvadratet har areal

$$
A = p\cdot p = p^2.
$$

Vi kan også uttrykket arealet ved å summere opp arealet av de mindre figurene den består av. Da får vi

$$
A = \underbrace{(p - q)\cdot (p - q)}_{\text{Stort kvadrat}} + \underbrace{q\cdot q}_{\text{Lite kvadrat}} + 2 \cdot \underbrace{q\cdot(p - q)}_{\text{To rektangler}} = (p - q)^2 + q^2 + 2q(p - q),
$$

som vi kan forenkle til

$$
A = (p - q)^2 + q^2 +2pq - 2q^2 = (p - q)^2 + 2pq - q^2.
$$

Setter vi de to uttrykkene lik hverandre, får vi

$$
p^2 = (p - q)^2 + 2pq - q^2,
$$

som vi kan skrive om til

$$
p^2 - 2pq + q^2 = (p - q)^2
$$

Men da har vi vist 2.kvadratsetning geometrisk.
```

````

## Algebraisk begrunnelse for konjugatsetningen
Du skal få prøve å utlede konjugatsetningen algebraisk i underveisoppgaven under.

````{admonition} Underveisoppgave 3
:class: check

Gitt tall $a, b, c, d \in \mathbb{R}$, så gjelder følgende algebraiske sammenheng:

$$
(a + b)(c + d) = ac + ad + bc + bd.
$$

Bruk sammenhengen til å vise konjugatsetningen.

```{admonition} Løsning
:class: solution, dropdown
Vi starter fra venstre side av konjugatsetningen:

$$
(p + q)(p - q) = p\cdot p + p\cdot (-q) + q\cdot p + q\cdot (-q) = p^2 - pq + pq - q^2 = p^2 - q^2.
$$

Dermed har vi vist konjugatsetningen algebraisk.
```

```` -->
