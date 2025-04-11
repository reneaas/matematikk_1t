# Algebraisk løsning

:::{admonition} Læringsmål
---
class: tip
---
* Kunne løse andregradsulikheter algebraisk ved hjelp av fortegnslinjer.
:::


## Fortegnslinjer
Et viktig verktøy vi bruker når vi løser andregradsulikheter algebraisk, er **fortegnslinjer**. 

::::{admonition} Farger? 
---
class: sidenote, margin
---
Merk at fortegnslinjene ikke må ha farger. Vi kommer til å bruke farger i illustrasjonene, men de kan også tegnes i svart-hvitt som

* positiv $=$ <span style="display:inline-block; width:50px; border-bottom: 3px solid black; vertical-align:middle;"></span> 
* negativ $=$ <span style="display:inline-block; width:50px; border-bottom: 3px dashed black; vertical-align:middle;"></span> 
::::

::::{admonition} Repetisjon: Fortegnslinjer
---
class: reminder
---
En **fortegnslinje** er en linje som viser fortegnet til en funksjon på et intervall. Vi bruker **heltrukne** og **stiplede** linjer for å skille mellom fortegnene:

* <span style="display:inline-block; width:100px; border-bottom: 3px solid red; vertical-align:middle;"></span> $=$ Positivt fortegn
* <span style="display:inline-block; width:100px; border-bottom: 3px dashed blue; vertical-align:middle;"></span> $=$ Negativt fortegn


<!-- I {numref}`fig-andregradsulikheter-algebraisk-løsning-teori-1` vises grafen til en andregradsfunksjon med to nullpunkter.

:::{figure} ./figurer/teori/fortegnslinje_graf.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-teori-1
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en andregradsfunksjon $f$ med to nullpunkter $x_1$ og $x_2$. 
::: -->

<!-- Fortegnslinjen til $f$ vil da være som vist i {numref}`fig-andregradsulikheter-algebraisk-løsning-teori-2`. -->

:::{figure} ./figurer/teori/sign_chart_theory.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-teori-2
width: 100%
class: no-click, adaptive-figure
---
viser en fortegnslinje for en andregradsfunksjon $f$ med to nullpunkter $x_1$ og $x_2$. De røde **heltrukne** linjene svarer til positivt fortegn. De blå **stiplede** linjene svarer til negativt fortegn.
:::

::::

Vi tar et eksempel:

::::::{admonition} Eksempel 1: fortegnslinjer
---
class: example
---
I {numref}`fig-andregradsulikheter-algebraisk-løsning-eksempel-1` vises grafen til

$$
f(x) = x^2 - 4x
$$

:::{figure} ./figurer/eksempler/eksempel_1/grafer.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-1
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = x^2 - 4x$ 
:::

Tegn fortegnslinjen til $f(x)$.

:::::{admonition} Løsning
---
class: solution
---
Vi markerer nullpunktene til grafen på en tallinje, og så tegner vi stiplede linjer der $f(x)$ er negativ (grafen er *under* $x$-aksen) og heltrukne linjer der $f(x)$ er positiv (grafen er *over* $x$-aksen).



```{figure} ./figurer/eksempler/eksempel_1/f.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-1-f
width: 100%
class: no-click, adaptive-figure
---
viser fortegnslinjen til $f(x) = x^2 - 4x$. Grafen til $f$ ligger **over** $x$-aksen når $x < 0$ eller $x > 4$, og **under** $x$-aksen når $0 < x < 4$.
```
::::::


---

**Din tur**!

::::::{admonition} Underveisoppgave 1
---
class: check
---
Ta quizen! 

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::


::::::




## Algebraisk løsning av andregradsulikheter

Når vi løser andregradsulikheter, får vi bruk for å kunne løse andregradslikninger som en del av løsningsprosessen.

::::{admonition} Algebraisk løsning av andregradsulikheter
:class: summary
Andregradsulikheter løses algebraisk slik:

Steg 1: Få null på høyre side
: Få alle ledd over på én side av ulikheten slik at vi får en andregradsfunksjon på formen 

    $$
    f(x) = ax^2 + bx + c
    $$ 

: på venstre side av ulikheten og null på høyre side.

Steg 2: Nullpunktsfaktoriser $f(x)$
: Finn nullpunktene og skriv $f(x)$ på nullpunktsform

$$
f(x) = a(x - x_1)(x - x_2),
$$

Steg 3: Fortegnsskjema
: Vi tegner et **fortegnsskjema** for $f(x)$ med en **fortegnslinje** for hver lineær faktor i $f(x)$. Fortegnslinja til $f(x)$ får vi ved å ta produktet av fortegnslinjene til de lineære faktorene. Deretter leser vi av løsningen.

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
Vi finner nullpunktene til $f$:

$$
x = \frac{1 \pm \sqrt{1 + 4 \cdot 6}}{2} = \frac{1 \pm \sqrt{25}}{2} = \frac{1 \pm 5}{2},
$$

som gir 

$$
x = -2 \quad \lor \quad x = 3.
$$

Dermed kan vi skrive

$$
f(x) = (x - (-2))(x - 3) = (x + 2)(x - 3).
$$

Først tegner vi fortegnsskjema ved å tegne inn en fortegnslinje for *hver* lineære faktor i $f(x)$. Deretter ganger vi fortegnene sammen for å få fortegnslinja til $f(x)$. 
Se {numref}`fig-andregradsulikheter-algebraisk-løsning-eksempel-2`.

```{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-andregradsulikheter-algebraisk-løsning-eksempel-2
width: 100%
class: no-click, adaptive-figure
---

viser fortegnsskjema til $f(x) = x^2 - x - 6 = (x + 2)(x - 3)$. Vi tegner en fortegnslinje for hver lineære faktor. For å få fortegnslinja til $f(x)$, ganger vi fortegnene til de lineære faktorene sammen. 
```

Fra fortegnsskjema, kan vi se at $f(x) > 0$ når $x < -2$ eller $x > 3$. Løsningen kan derfor skrives som

$$
x \in \mathbb{R} \setminus [-2, 3]
$$
::::
:::::

---

**Din tur!**

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
En ulikhet er gitt ved

$$
x^2 - 4x - 5 < 0.
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem nullpunktsformen til 

$$
f(x) = x^2 - 4x - 5.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = (x + 1)(x - 5)
$$
:::
:::::::::::::

:::::::::::::{tab-item} b
Tegn et fortegnsskjema for $f(x)$ ved hjelp av de lineære faktorene.

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/b.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::
::::
:::::::::::::

:::::::::::::{tab-item} c
Bestem løsningen av ulikheten.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -1, 5 \rangle.
$$
:::
:::::::::::::
::::::::::::::



:::::::::::::::


