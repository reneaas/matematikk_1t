# Algebraisk løsning

```{admonition} Læringsmål: algebraisk løsning
:class: tip
Målet med det delkapitlet er at du skal kunne:
* Kunne løse andregradsulikheter algebraisk ved hjelp av fortegnslinjer.
```


## Fortegnslinjer
Et viktig verktøy vi bruker når vi løser andregradsulikheter algebraisk, er **fortegnslinjer**. Fortegnslinjer er en måte å representere fortegnet til en funksjon på ulike intervaller. 

::::{admonition} Farger? 
---
class: sidenote, margin
---
Merk at fortegnslinjene ikke må ha farger. Vi kommer til å bruke farger i illustrasjonene, men de kan også tegnes i svart-hvitt som

* positiv $=$ <span style="display:inline-block; width:50px; border-bottom: 3px solid black; vertical-align:middle;"></span> 
* negativ $=$ <span style="display:inline-block; width:50px; border-bottom: 3px dashed black; vertical-align:middle;"></span> 
::::

::::{admonition} Fortegnslinjer
---
class: theory
---
En **fortegnslinje** er en linje som viser fortegnet til en funksjon på et intervall. Vi bruker **heltrukne** og **stiplede** linjer for å skille mellom fortegnene som følger:

* <span style="display:inline-block; width:100px; border-bottom: 3px solid red; vertical-align:middle;"></span> $=$ Positivt fortegn
* <span style="display:inline-block; width:100px; border-bottom: 3px dashed blue; vertical-align:middle;"></span> $=$ Negativt fortegn


I {numref}`fig-andregradsulikheter-algebraisk-løsning-teori-1` vises grafen til en andregradsfunksjon med to nullpunkter.

:::{figure} ./figurer/teori/fortegnslinje_graf.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-teori-1
width: 80%
---
Viser grafen til en andregradsfunksjon $f$ med to nullpunkter $x_1$ og $x_2$. 
:::

Fortegnslinjen til $f$ vil da være som vist i {numref}`fig-andregradsulikheter-algebraisk-løsning-teori-2`.

:::{figure} ./figurer/teori/teori_fortegnslinjer_colored.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-teori-2
width: 100%
---
Viser fortegnslinjen til $f$. De røde **heltrukne** linjene svarer til positivt fortegn. De blå **stiplede** linjene svarer til negativt fortegn.
:::

::::

Vi tar et eksempel:

::::::{admonition} Eksempel 1: fortegnslinjer
---
class: example
---
I {numref}`fig-andregradsulikheter-algebraisk-løsning-eksempel-1` vises grafene til

$$
f(x) = x^2 - 4x \quad \text{og} \quad g(x) = x - 2.
$$

:::{figure} ./figurer/eksempler/eksempel_1_grafer.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-1
width: 80%
---
Viser grafene til $f(x) = x^2 - 4x$ og $g(x) = x - 2$. 
:::

Tegn fortegnslinjene til $f$ og $g$. 

:::::{admonition} Løsning
---
class: solution
---
Vi markerer nullpunktene til grafene på en tallinje, og så tegner vi stiplede linjer der funksjonene er negative (grafen er *under* $x$-aksen) og heltrukne linjer der funksjonene er positive (grafen er *over* $x$-aksen).
Da får vi 

::::{tab-set}
:::{tab-item} $f(x) = x^2 - 4x$
```{figure} ./figurer/eksempler/eksempel_1_fortegnslinje_f.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-1-f
width: 100%
---
Viser fortegnslinjen til $f(x) = x^2 - 4x$. Grafen til $f$ ligger **over** $x$-aksen når $x < 0$ eller $x > 4$, og **under** $x$-aksen når $0 < x < 4$.
```
:::

:::{tab-item} $g(x) = x - 2$
```{figure} ./figurer/eksempler/eksempel_1_fortegnslinje_g.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-1-g
width: 100%
---
Viser fortegnslinjen til $g(x) = x - 2$. Grafen til $g$ ligger **over** $x$-aksen når $x > 2$, og **under** $x$-aksen når $x < 2$.
```
:::::
::::::

**Din tur**!

::::::{admonition} Underveisoppgave 1
---
class: check
---
I {numref}`fig-andregradsulikheter-algebraisk-løsning-underveisoppgave-1` vises grafen til

$$
f(x) = -x^2 + 3x + 4 \quad \text{og} \quad g(x) = -x + 2.
$$

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-underveisoppgave-1
width: 80%
---
Viser grafene til $f(x) = -x^2 + 3x + 4$ og $g(x) = -x + 2$.
:::

Tegn fortegnslinjene til $f$ og $g$.


:::::{admonition} Løsning
---
class: solution, dropdown
---
::::{tab-set}
:::{tab-item} $f(x) = -x^2 + 3x + 4$
```{figure} ./figurer/underveisoppgaver/underveisoppgave_1_fortegnslinje_f.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-underveisoppgave-1-f
width: 100%
---
Viser fortegnslinjen til $f(x) = -x^2 + 3x + 4$. Grafen til $f$ ligger **over** $x$-aksen når $x < -1$ eller $x > 4$, og **under** $x$-aksen når $-1 < x < 4$.
```
:::

:::{tab-item} $g(x) = -x + 2$
```{figure} ./figurer/underveisoppgaver/underveisoppgave_1_fortegnslinje_g.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-underveisoppgave-1-g
width: 100%
---
Viser fortegnslinjen til $g(x) = -x + 2$. Grafen til $g$ ligger **over** $x$-aksen når $x < 2$, og **under** $x$-aksen når $x > 2$.
```
:::::
::::::


## Algebraisk løsning av andregradsulikheter

Når vi løser andregradsulikheter, får vi bruk for å kunne løse andregradslikninger som en del av løsningsprosessen.

::::{admonition} Algebraisk løsning av andregradsulikheter
:class: theory
Andregradsulikheter kan løses algebraisk gjennom følgende steg:

Steg 1: Få null på høyre side
: Få alle ledd over på én side av ulikheten slik at vi får en andregradsfunksjon på formen 

    $$
    f(x) = ax^2 + bx + c
    $$ 

: på venstre side av ulikheten og null på høyre side.

Steg 2: Nullpunktsfaktoriser $f(x)$
: Bestem nullpunktene til $f$ og nullpunktfaktoriser $f(x)$ som

$$
f(x) = ax^2 + bx + c = a(x - x_1)(x - x_2),
$$

Steg 3: Fortegnsskjema
: Vi tegner et **fortegnsskjema** for $f(x)$ med en **fortegnslinje** for hver lineær faktor i $f(x)$. Fortegnslinja til $f(x)$ får vi ved å ta produktet av fortegnslinjene til de lineære faktorene.

::::


Vi går løs på et eksempel

:::::{admonition} Eksempel 2: algebraisk løsning
:class: example
Bestem løsningsmengden til ulikheten

$$
x^2 - x - 6 > 0.
$$

::::{admonition} Løsning
---
class: solution
---
Først nullpunktsfaktoriserer vi $f(x) = x^2 - x - 6$:

$$
x = \frac{1 \pm \sqrt{1 + 4 \cdot 6}}{2} = \frac{1 \pm \sqrt{25}}{2} = \frac{1 \pm 5}{2},
$$

som gir 

$$
x = -2 \quad \lor \quad x = 3.
$$

Dermed kan vi skrive

$$
f(x) = x^2 - x - 6 = (x + 2)(x - 3).
$$

Deretter tegner vi noe som kalles for et fortegnsskjema ved å tegne inn en fortegnslinje for hver lineære faktor i $f(x)$. Deretter ganger vi fortegnene sammen for å få fortegnslinja til $f(x)$. 
Se {numref}`fig-andregradsulikheter-algebraisk-løsning-eksempel-2`.

```{figure} ./figurer/eksempler/eksempel_2.svg
:name: fig-andregradsulikheter-algebraisk-løsning-eksempel-2
:width: 100%

Fortegnslinje for $f(x) = x^2 - x - 6 = (x + 2)(x - 3)$. De blå heltrukne linjene representerer at faktoren er **positiv** på intervallet, mens de røde stiplede linjene representerer at faktoren er **negativ** på intervallet. Fortegnslinja til $f(x)$ får man ved å gange sammen fortegnene til faktorene.
```

Fra fortegnsskjema, kan vi se at $f(x) > 0$ når $x < -2$ og $x > 3$. Vi kan derfor uttrykke løsningsmengden som 

$$
x^2 - x - 6 > 0 \quad \Leftrightarrow \quad x \in \langle \gets, -2\rangle \cup \langle 3, \to \rangle = \mathbb{R} \setminus [-2, 3].
$$
::::
:::::

Nå kan du prøve deg på en oppgave!

:::::{admonition} Underveisoppgave 2
:class: check
En andregradsulikhet er gitt ved:

$$
x^2 - 4x - 5 < 0.
$$

Deloppgave 1
: Nullpunktsfaktoriser $f(x) = x^2 - 4x - 5$.

::::{admonition} Fasit: deloppgave 1
---
class: answer, dropdown
---
$$
f(x) = (x + 1)(x - 5).
$$
::::

::::{admonition} Løsning: deloppgave 1
---
class: solution, dropdown
---
Vi finner nullpunktene til $f(x)$ ved å bruke $abc$-formelen på likningen $f(x) = 0$. Vi får

$$
x = \frac{4 \pm \sqrt{4^2 + 4 \cdot 5}}{2} = \frac{4 \pm \sqrt{16 + 20}}{2} = \frac{4 \pm \sqrt{36}}{2} = \frac{4 \pm 6}{2} = 2 \pm 3.
$$

Altså er 

$$
x = -1 \quad \lor \quad x = 5.
$$

Dermed kan vi nullpunktsfaktorisere $f(x)$ som

$$
f(x) = (x - (-1))(x - 5)= (x + 1)(x - 5).
$$
::::

<br>

Deloppgave 2
: Tegn et fortegnsskjema for $f(x)$ som inkluderer de lineære faktorene.

::::{admonition} Fasit: deloppgave 2
---
class: answer, dropdown
---
```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
:name: fig-andregradsulikheter-algebraisk-løsning-underveisoppgave-2
:width: 100%
```
::::

<br>

Deloppgave 3
: Bestem løsningsmengden av ulikheten $x^2 - 4x - 5 < 0$.

::::{admonition} Fasit: deloppgave 3
---
class: answer, dropdown
---
$$
x \in \langle -1, 5 \rangle.
$$
::::

::::{admonition} Løsning: deloppgave 3
---
class: solution, dropdown
---
Fra fortegnslinja til $f(x)$ i deloppgave 2, kan vi lese av at $f(x) < 0$ når $-1 < x < 5$. Dermed er løsningsmengden til ulikheten

$$
x \in \langle -1, 5 \rangle.
$$
::::
:::::

Vi tar et eksempel til der vi må gjøre noen flere steg.

::::::{admonition} Eksempel 3: algebraisk løsning
---
class: example
---
Bestem løsningsmengden til ulikheten

$$
-x^2 + 3x + 3 \leq 2x - 3.
$$

:::::{admonition} Løsning
---
class: solution
---
Steg 1: Få null på høyre side
: Vi må først få alle ledd over på én side slik at vi kan nullpunktsfaktorisere en andregradsfunksjon:

\begin{align*}

-x^2 + 3x + 3 &\leq 2x - 3 \\
& \Updownarrow \\
-x^2 + 3x + 3 \textcolor{red}{- (2x - 3)} &\leq  2x - 3 \textcolor{red}{- (2x - 3)} \\
& \Updownarrow \\
-x^2 + 3x + 3 \textcolor{red}{-} 2x \textcolor{red}{+} 3 &\leq 0 \\
& \Updownarrow \\
-x^2 + x + 6 &\leq 0.
\end{align*}

Steg 2: Nullpunktsfaktoriser $f(x)$
: Vi nullpunktsfaktoriserer $f(x) = -x^2 + x + 6$:

    $$
    x = \frac{-1 \pm \sqrt{1 + 4 \cdot 6}}{-2} = \frac{-1 \pm \sqrt{25}}{-2} = \frac{-1 \pm 5}{-2}
    $$

: som gir

    $$
    x = -3 \quad \lor \quad x = 2.
    $$

: Altså er 

    $$
    f(x) = -x^2 + x + 6 = -(x + 3)(x - 2).
    $$

Steg 3: Tegn fortegnsskjema
: Vi tegner et fortegnsskjema med de lineære faktorene til $f(x)$. Vi **inkluderer den ledende koeffisienten $a = -1$** som en egen faktor for at fortegnslinja til $f(x)$ skal bli riktig, som vist i {numref}`fig-andregradsulikheter-algebraisk-løsning-eksempel-3`.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-3
width: 100%
---
Viser fortegnsskjema for $f(x) = -x^2 + x + 6 = -(x + 3)(x - 2)$. Det er viktig å ta med den ledende koeffisienten $a = -1$ som en egen faktor slik at fortegnslinja til $f(x)$ blir riktig.
:::

Fra {numref}`fig-andregradsulikheter-algebraisk-løsning-eksempel-3`, kan vi se at $f(x) \leq 0$ når

$$
x \leq -2 \, \lor \, x \geq 3 \quad \Leftrightarrow \quad x \in \mathbb{R} \setminus \langle -2, 3 \rangle.
$$

Dermed har vi bestemt løsningen til ulikheten.

:::::
::::::


Så er det **din tur**!

::::::{admonition} Underveisoppgave 3
---
class: check
---
En andregradsulikhet er gitt ved

$$
-x^2 + 4x - 2 < 5x - 4.
$$


Deloppgave 1
: Skriv om ulikheten til formen $f(x) < 0$ og bestem $f(x)$. 

:::{admonition} Fasit: deloppgave 1
---
class: answer, dropdown
---
$$
f(x) = -x^2 - x + 2.
$$
:::

<br>

Deloppgave 2
: Nullpunktsfaktoriser $f(x)$.

:::{admonition} Fasit: deloppgave 2
---
class: answer, dropdown
---
$$
f(x) = -(x + 1)(x - 2).
$$
:::

<br>

Deloppgave 3
: Tegn et fortegnsskjema for $f(x)$ som inkluderer alle faktorene i $f(x)$. 

:::{admonition} Fasit: deloppgave 3
---
class: answer, dropdown
---
```{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-underveisoppgave-3
width: 100%
---
```
:::

<br>

Deloppgave 4
: Bestem løsningsmengden til ulikheten $-x^2 + 4x - 2 < 5x - 4$.

:::{admonition} Fasit: deloppgave 4
---
class: answer, dropdown
---
$$
x \in \mathbb{R} \setminus [-2, 1].
$$
:::


::::::




## Oppgaver

`````{admonition} Oppgave 1
:class: problem-level-1

Bestem løsningsmengden til ulikheten

$$
x^2 - 4x \geq 0.
$$

````{admonition} Fasit
:class: solution, dropdown

$$
x \in \mathbb{R} \setminus \langle 0, 4 \rangle.
$$

eller

$$
x \in \langle \gets, 0] \cup [4, \to \rangle.
$$
````

````{admonition} Løsning
:class: solution, dropdown
Vi tenker oss en andregradsfunksjon $f(x) = x^2 - 4x$ som vi skal nullpunktsfaktorisere:

$$
f(x) = x^2 - 4x = x(x - 4). 
$$

Deretter tegner vi et fortegnsskjema for $f(x)$: 

```{figure} ./figurer/oppgaver/oppgave_1.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-1
:width: 100%
```

Fra fortegnslinja til $f(x)$, kan vi se at $f(x) \geq 0$ når

$$
x \in \mathbb{R} \setminus \langle 0, 4 \rangle.
$$

````

`````

`````{admonition} Oppgave 2
:class: problem-level-1

En andregradsfunksjon er gitt ved $f(x) = -x^2 + 3x + 4$.

Bestem løsningsmengden for $f(x) \leq 0$.


````{admonition} Fasit
:class: solution, dropdown

```{figure} ./figurer/oppgaver/oppgave_2_uten_faktorer.svg
:name: oppgave-2-uten-faktorer
:width: 100%
```


$$
x \in \mathbb{R} \setminus \langle -1, 4 \rangle.
$$
````

````{admonition} Løsning
:class: solution, dropdown
Vi må først bestemme nullpunktene til $f(x)$ for å kunne nullpunktsfaktorisere: 

$$
x = \frac{-3 \pm \sqrt{(-3)^2 - 4\cdot (-1)\cdot 4}}{2\cdot (-1)} = \frac{-3 \pm \sqrt{9 + 16}}{-2} = \frac{-3\pm 5}{-2} = \frac{3 \mp 5}{2}
$$

som gir

$$
x = -1 \quad \lor \quad x = 4. 
$$

Vi husker på at den ledende koeffisienten er $a = -1$, som gir

$$
f(x) = -x^2 + 3x + 4 = -1\cdot(x + 1)(x - 4) = -(x + 1)(x - 4).
$$

Nå kan vi tegne fortegnsskjema for funksjonen:

```{figure} ./figurer/oppgaver/oppgave_2.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-2
:width: 100%
```

Fra fortegnsskjemaet kan vi se at $f(x) \leq 0$ når 

$$
x \in \mathbb{R} \setminus \langle -1, 4 \rangle.
$$
````
`````


`````{admonition} Oppgave 3
:class: problem-level-2
En funksjon $g$ har fortegnslinje som vist i {numref}`andregradsulikheter-algebraisk-oppgaver-oppgave-3`. Bestem et mulig uttrykk for $g(x)$. 

```{figure} ./figurer/oppgaver/oppgave_3_uten_faktorer.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-3
:width: 100%

Fortegnsskjema for en funksjon $g(x)$.
```


````{admonition} Fasit
:class: solution, dropdown
Et eksempel på en funksjon som passer:

$$
g(x) = -(x - 2)(x + 2)
$$

Alle funksjoner på formen

$$
g(x) = a(x - 2)(x + 2), \quad a < 0
$$

passer med fortegnslinja til $g$. 
````

````{admonition} Løsning
:class: solution, dropdown
Vi kan tegne et mer detaljert fortegnsskjema der vi har én lineær faktor med nullpunkt i $x = -2$ og én lineær faktor med nullpunkt i $x = 2$: 

```{figure} ./figurer/oppgaver/oppgave_3.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-3-solution
:width: 100%
```

Vi kan se at så lenge den ledende koeffisienten er negativ, får vi riktig fortegnslinje. Dermed er det meste generelle uttrykket for $g(x)$

$$
g(x) = a(x - 2)(x + 2), \quad a < 0.
$$

I fortegnslinja har vi valgt ett eksempel som passer:

$$
g(x) = -(x - 2)(x + 2)
$$
````
`````