# Kvadratsetningene

---

:::{admonition} HUSK
---
class: warning
---
Ta med at kvadratsetningene svarer til andregradsfunksjoner der ekstremalformen og nullpunktsformen av $f(x)$ er den samme. 
:::

---

Kvadratsetningene er viktige setninger i algebra som lar oss faktorisere andregradsuttrykk. Oftest vil vi bruke dem i sammenhenger der vi skal analysere andregradsfunksjoner.

```{admonition} Læringsmål
:class: tip

* Kjenne til de tre kvadratsetningene, og kunne bruke dem til å faktorisere andregradsuttrykk.
* Kunne bruke kvadratsetningene til å bestemme nullpunktene til andregradsfunksjoner.
* Kunne bruke kvadratsetningene til å bestemme koeffisienter til identiteter.
```

Det finnes til sammen tre kvadratsetninger. Vi skal begrunne de to første geometrisk, og den siste algebraisk.

```{admonition} Kvadratsetningene
:class: theory
Gitt to vilkårlige tall $p, q \in \mathbb{R}$, så gjelder følgende tre setninger:

1.Kvadratsetning
: $(p + q)^2 = p^2 + 2pq + q^2$

2.Kvadratsetning
: $(p - q)^2 = p^2 - 2pq + q^2$

Konjugatsetningen
: $(p + q)(p - q) = p^2 - q^2$
```


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

````

## Sammenheng med andregradsfunksjoner

Kvadratsetningene er viktige fordi de gir oss en metode for å faktorisere andregradsfunksjoner. Vi skal se på et eksempel for å vise hvordan vi kan bruke kvadratsetningene til å faktorisere noen spesielle andregradsfunksjoner som kun har ett nullpunkt. 

```{admonition} Eksempel 1: Faktorisering av andregradsfunksjoner
:class: example

La oss se på andregradsfunksjonen 

$$
f(x) = x^2 + 8x + 16.
$$

Vi kan merke oss at vi kan skrive $f(x)$ som

$$
f(x) = x^2 + 2\cdot x \cdot 4 + 4^2, 
$$

og da kan vi merke oss at vi kan bruke 1.kvadratsetning med $p = x$ og $q = 4$, som gir

$$
f(x) = (x + 4)^2.
$$

Vi kan se at $f(x)$ bare har ett nullpunkt fordi

$$
f(x) = 0 \quad \Leftrightarrow \quad (x + 4)^2 = 0 \quad \Leftrightarrow \quad (x + 4) = 0 \quad \Leftrightarrow \quad x = -4.
$$
```

Så er det **din tur**!


````{admonition} Underveisoppgave 4
:class: check

En funksjon $g(x)$ er gitt ved

$$
g(x) = x^2 - 4x + 4.
$$

Faktoriser $g(x)$ ved hjelp av en kvadratsetning og bestem nullpunktet til andregradsfunksjonen.

```{admonition} Løsning
:class: solution, dropdown

Vi kan skrive $g(x)$ som

$$
g(x) = x^2 - 2\cdot x \cdot 2 + 2^2,
$$

og dersom vi setter $p = x$ og $q = 2$, kan vi gjenkjenne dette som 2.kvadratsetning. Vi faktoriserer og får:

$$
g(x) = (x - 2)^2.
$$

Vi kan bestemme nullpunktet til $g(x)$ som følger:

$$
g(x) = 0 \quad \Leftrightarrow \quad (x - 2)^2 = 0 \quad \Leftrightarrow \quad (x - 2) = 0 \quad \Leftrightarrow \quad x = 2.
$$

````

Du klarer en til! 

````{admonition} Underveisoppgave 5
:class: check

En andregradsfunksjon $h(x)$ er gitt ved

$$
h(x) = (3x - 4)^2.
$$

Bruk en kvadratsetning til å bestemme koeffisientene til $h(x)$. Finn også nullpunktet.


```{admonition} Løsning
:class: solution, dropdown
Først kan vi bruke 2.kvadratsetning til å utvide uttrykket til $h(x)$ med $p = 3x$ og $q = 4$. Da får vi 

$$
h(x) = (3x - 4)^2 = (3x)^2 - 2\cdot (3x)\cdot 4 + 4^2 = 9x^2 - 24x + 16.
$$

Altså er koeffisientene til $h(x)$:

$$
a = 9 \quad \land \quad b = -24 \quad \land \quad c = 16.
$$

```
````

```{admonition} Eksempel 2: konjugatsetningen og andregradsfunksjoner
:class: example

En andregradsfunksjon er gitt ved

$$
f(x) = x^2 - 9.
$$

Vi kan faktorisere $f(x)$ ved å bruke konjugatsetningen ved å skrive $f(x)$ som

$$
f(x) = x^2 - 3^2 = (x + 3)(x - 3).
$$

I motsetning til andregradsfunksjoner som faktoriseres med 1. og 2.kvadratsetning, så vil andregradsfunksjoner som kan faktoriseres med konjugatsetningen ha to nullpunkter. Dette kan vi se ved å sette $f(x) = 0$:

$$
f(x) = 0 \quad \Leftrightarrow \quad (x + 3)(x - 3) = 0 \quad \Leftrightarrow \quad (x + 3) = 0 \quad \lor \quad (x - 3) = 0,
$$

som betyr at nullpunktene til $f(x)$ er

$$
x = -3 \quad \lor \quad x = 3.
$$

```


## Oppgaver