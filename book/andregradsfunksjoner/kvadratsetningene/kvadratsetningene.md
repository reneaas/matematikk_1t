# Kvadratsetningene

Det finnes til sammen tre kvadratsetninger. Vi skal begrunne disse på to måter: geometrisk og algebraisk. Kvadratsetningene er som følger:

```{admonition} Kvadratsetningene
:class: tip 
Gitt to vilkårlige tall $a, b \in \mathbb{R}$, så gjelder følgende tre setninger:

1.Kvadratsetning
: $(a + b)^2 = a^2 + 2ab + b^2$

2.Kvadratsetning
: $(a - b)^2 = a^2 - 2ab + b^2$

3.Kvadratsetning (*konjugatsetningen*)
: $(a + b)(a - b) = a^2 - b^2$
```


## Geometrisk begrunnelse

Du skal få prøve å begrunne de to første kvadratsetningene i underveisoppgavene under. Du starter med 1.kvadratsetning:

````{admonition} Underveisoppgave 1
:class: note

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
A = (a + b)\cdot (a + b) = (a + b)^2.
$$

Vi kan også uttrykke arealet ved å summere opp arealet av de mindre figurene den består av. Da har vi

$$
A = \underbrace{a\cdot a}_{\text{Grønt kvadrat}} + \underbrace{b\cdot b}_{\text{Rødt kvadrat}} + \underbrace{2\cdot a\cdot b}_{\text{To lilla rektangler}} = a^2 + b^2 + 2ab.
$$

Men disse to arealene må være like hverandre som gir

$$
(a + b)^2 = a^2 + b^2 + 2ab = a^2 + 2ab + b^2,
$$

som er 1.kvadratsetning.
```
````

Du skal få gå løs rett på 2.kvadratsetning også!

````{admonition} Underveisoppgave 2
:class: note

I figuren under vises et ytre kvadrat med sidelengder $a$ som inneholder et kvadrat med sidelengder $a - b$, og to rektangler med sidelengder $a$ og $b$. 

Bruk figuren til å utlede 2.kvadratsetning ved hjelp av arealberegninger. 

```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
:name: kvadratsetningene-underveisoppgave-2
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown
Hele kvadratet har areal

$$
A = a\cdot a = a^2.
$$

Vi kan også uttrykket arealet ved å summere opp arealet av de mindre figurene den består av. Da får vi

$$
A = \underbrace{(a - b)\cdot (a - b)}_{\text{Stort kvadrat}} + \underbrace{b\cdot b}_{\text{Lite kvadrat}} + 2 \cdot \underbrace{b\cdot(a - b)}_{\text{To rektangler}} = (a - b)^2 + b^2 + 2b(a - b),
$$

som vi kan forenkle til

$$
A = (a - b)^2 + b^2 +2ab - 2b^2 = (a - b)^2 + 2ab - b^2.
$$

Setter vi de to uttrykkene lik hverandre, får vi

$$
a^2 = (a - b)^2 + 2ab - b^2,
$$

som vi kan skrive om til

$$
a^2 - 2ab + b^2 = (a - b)^2 = (b - a)^2,
$$

der vi har brukt at alle tall opphøyd i 2 er positive, så $(a - b)^2 = (b - a)^2$. <br>
Men da har vi vist 2.kvadratsetning geometrisk.
```

````

