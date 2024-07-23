# Grafisk løsning

:::{admonition} Læringsmål: grafisk løsning av andregradsulikheter
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Løse andregradsulikheter grafisk.
* Oppgi løsningene til en andregradsulikhet som en løsningsmengde eller som én eller flere ulikheter.
:::

## Ulikheter på formen $ax^2 + bx + c > 0$ og $ax^2 + bx + c < 0$


:::::{admonition} Andregradsulikheter: type 1
---
class: theory
---
Gitt en andregradsfunksjon $f(x) = ax^2 + bx + c$, kan vi løse følgende andregradsulikheter grafisk:


| Ulikhet | Løsningsmengde |
|---------|----------------|
| $ax^2 + bx + c > 0$ | Alle $x$ der grafen til $f$ ligger **over** $x$-aksen |
| $ax^2 + bx + c \geq 0$ | Alle $x$ der grafen til $f$ ligger **over eller på** $x$-aksen |
| $ax^2 + bx + c < 0$ | Alle $x$ der grafen til $f$ ligger **under** $x$-aksen |
| $ax^2 + bx + c \leq 0$ | Alle $x$ der grafen til $f$ ligger **under eller på** $x$-aksen |


:::{figure} ./figurer/teori/andregradsulikhet_type_1.svg
---
name: andregradsulikheter-grafisk-løsning-teori-1.svg
width: 100%
---
:::
:::::

Vi går løs på et eksempel

::::::{admonition} Eksempel 1
---
class: example
name: andregradsulikheter-grafisk-løsning-eksempel-1
---
En andregradsulikhet er gitt ved 

$$
x^2 - 4x + 3 > 0
$$

Løs ulikheten. 

:::::{admonition} Løsning
---
class: solution
---
Vi tegner grafen til andregradsfunksjonen 

$$
f(x) = x^2 - 4x + 3,
$$

og så finner vi alle $x$ der grafen ligger **over** $x$-aksen. Se {numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-1`.

:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-andregradsulikheter-grafisk-løsning-eksempel-1
width: 100%
---
Viser grafen til $f(x) = x^2 - 4x + 3$. Løsningsmengden der grafen til $f$ ligger over $x$-aksen er vist med rød farge.
:::

Fra grafen kan vi se at når $x < 1$ eller $x > 3$, så ligger grafen til $f$ over $x$-aksen. Ulikheten tillater ikke likhet, så nullpunktene til $f$ er ikke inkludert. Som vanlig kan vi oppgi løsningen til en ulikhet enten som én ulikhet eller flere ulikheter, eller som en løsningsmengde:

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \mathbb{R} \setminus [1, 3] \quad \text{eller} \quad x \in \langle \gets, 1 \rangle \cup \langle 3, \to \rangle
$$
:::
:::{tab-item} Ulikheter
$$
x < 1 \, \lor \, x > 3
$$
:::
::::


:::::
::::::

Så er det **din tur**!


::::::{admonition} Underveisoppgave 1
---
class: check
name: andregradsulikheter-grafisk-løsning-underveisoppgave-1
---
I {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-1` er grafen til  

$$
g(x) = -x^2 - 2x + 8
$$

tegnet inn. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-1
width: 100%
---
Viser grafen til $g(x) = -x^2 - 2x + 8$. 
:::


Bruk figuren til å løse ulikheten

$$
-x^2 + x + 2 \geq 0.
$$

Oppgi løsningen som
* En løsningsmengde
* Én eller flere ulikheter

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in [-4, 2]
$$
:::

:::{tab-item} Ulikheter
$$
-4 \leq x \leq 2
$$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-1` kan vi se at grafen ligger **over** $x$-aksen når $x > -4$ og $x < 2$. Vi kan illustrere løsningsmengden grafisk som i {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-1-løsning`.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1_løsning.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-1-løsning
width: 100%
---
Viser grafen til $g$ sammen med løsningsmengden markert i rødt.
:::

Derfor er løsningen til ulikheten 

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in [-4, 2]
$$
:::

:::{tab-item} Ulikheter
$$
-4 \leq x \leq 2
$$
:::
::::
:::::

:::::
::::::


## Andregradsulikheter $f(x) > g(x)$ og $f(x) < g(x)$

Teorien vår kan generaliseres til alle typer funksjoner, men vi skal anta at $f$ og $g$ er *opptil* en andregradsfunksjon. 

::::::{admonition} Grafisk løsning av andregradsulikheter: generell strategi
---
class: theory
---

Gitt en andregradsfunksjon $f$ og la $g$ være en konstant-, lineær- eller andregradsfunksjon. Da kan vi løse følgende andregradsulikheter grafisk som følger:

| Ulikhet | Løsningsmengde |
|---------|----------------|
| $f(x) > g(x)$ | Alle $x$ der grafen til $f$ ligger **over** grafen til $g$ |
| $f(x) \geq g(x)$ | Alle $x$ der grafen til $f$ ligger **over eller på** grafen til $g$ |
| $f(x) < g(x)$ | Alle $x$ der grafen til $f$ ligger **under** grafen til $g$ |
| $f(x) \leq g(x)$ | Alle $x$ der grafen til $f$ ligger **under eller på** grafen til $g$ |

<br>

Under vises en figur for hver av de tre typene funksjoner $g$ kan være:

:::::{tab-set}
::::{tab-item} $f$ *vs* konstant funksjon

:::{figure} ./figurer/teori/andregradsulikhet_f_vs_konstant.svg
---
name: fig-andregradsulikhet-grafisk-løsning-teori-2-andregrad-vs-konstant-fn
width: 100%
---
Viser en grafisk framstilling av en andregradsfunksjon $f$ og en konstant funksjon $g$. Figuren til venstre viser løsningsmengden for ulikheten $f(x) > g(x)$, mens figuren til høyre viser løsningsmengden for ulikheten $f(x) < g(x)$.
::::

::::{tab-item} $f$ *vs* lineær funksjon

:::{figure} ./figurer/teori/andregradsulikhet_f_vs_lineær.svg
---
name: fig-andregradsulikhet-grafisk-løsning-teori-2-andregrad-vs-lineær-fn
width: 100%
---
Viser en grafisk framstilling av en andregradsfunksjon $f$ og en lineær funksjon $g$. Figuren til venstre viser løsningsmengden for ulikheten $f(x) > g(x)$, mens figuren til høyre viser løsningsmengden for ulikheten $f(x) < g(x)$.
:::

::::

::::{tab-item} $f$ *vs* andregradsfunksjon

:::{figure} ./figurer/teori/andregradsulikhet_f_vs_andregradsfunksjon.svg
---
name: fig-andregradsulikhet-grafisk-løsning-teori-2-andregrad-vs-andregradsfunksjon
width: 100%
---
Viser en grafisk framstilling av en andregradsfunksjon $f$ og en andregradsfunksjon $g$. Figuren til venstre viser løsningsmengden for ulikheten $f(x) > g(x)$, mens figuren til høyre viser løsningsmengden for ulikheten $f(x) < g(x)$.
:::

::::
:::::

::::::


Vi går løs på noen eksempler på hver type ulikhet og så skal du få gjøre noen underveisoppgaver mellom hvert eksempel!


::::::{admonition} Eksempel 2: andregradsfunksjon *vs* konstant funksjon
---
class: example
name: andregradsulikheter-grafisk-løsning-eksempel-2
---
En ulikhet er gitt ved 

$$
-2x^2 + 4x + 4 > -2.
$$

Løs ulikheten grafisk og oppgi løsningen som 
* En løsningsmengde
* Én eller flere ulikheter


:::::{admonition} Løsning
---
class: solution
---
Vi trenger grafene til funksjonene

$$
f(x) = -2x^2 + 4x + 4 \quad \text{og} \quad g(x) = -2,
$$

og så finner vi alle $x$ der grafen til $f$ ligger **over** grafen til $g$. 

I {numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-2` har vi markert delene av $x$-aksen hvor grafen til $f$ ligger over grafen til $g$. 


::::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-andregradsulikheter-grafisk-løsning-eksempel-2
width: 100%
---
Viser grafen til $f(x) = -2x^2 + 4x + 4$ og $g(x) = -2$. Løsningsmengden til $f(x) > g(x)$ er markert i rødt på $x$-aksen.
::::

Fra {numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-2` kan vi lese av at grafen til $f$ ligger over grafen til $g$ når $x < 0$ og $x > 2$. Ulikheten tillater ikke likhet, så $x$-koordinaten til skjæringen mellom de to grafene er ikke en del av løsningsmengden. Dermed kan vi oppgi løsningen som

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \langle -1, 3 \rangle
$$
:::

:::{tab-item} Ulikheter
$$
-1 < x < 3 \quad \Leftrightarrow \quad -1 < x \, \land \, x < 3
$$
:::
::::
:::::

::::::

Så er det **din tur**!

::::::{admonition} Underveisoppgave 2
---
class: check
name: andregradsulikheter-grafisk-løsning-underveisoppgave-2
---
I {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-2` er grafen til

$$
f(x) = x^2 - 2x,
$$

tegnet inn.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-2
width: 100%
---
Viser grafen til $f(x) = x^2 - 2x$. 
::: 

Bruk {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-2` til å løse ulikheten 

$$
x^2 - 2x \geq 3.
$$

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \mathbb{R} \setminus \langle -1, 3 \rangle \quad \Leftrightarrow \quad x \in \langle \gets, -1 \rangle \cup \langle 3, \to \rangle
$$
:::

:::{tab-item} Ulikheter
$$
x \leq -1 \, \lor \, x \geq 3
$$
:::
::::
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi tegner inn en linje $y = 3$ i grafen og leser av alle $x$ der grafen til $f$ ligger **over eller på** linjen. Se {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-2-løsning`.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2_løsning.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-2-løsning
width: 100%
---
Viser grafen til $f(x) = x^2 - 2x$ sammen med linjen $y = 3$. Løsningsmengden er markert i rødt.
:::

Vi kan se at når $x < -1$ eller $x > 3$, så ligger grafen til $f$ over linja. Når $x = -1$ eller $x = 3$, så ligger $f$ på linja. Derfor er løsningen av ulikheten

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \mathbb{R} \setminus \langle -1, 3 \rangle \quad \Leftrightarrow \quad x \in \langle \gets, -1 \rangle \cup \langle 3, \to \rangle
$$
:::

:::{tab-item} Ulikheter
$$
x \leq -1 \, \lor \, x \geq 3
$$
:::
::::

::::::


::::::{admonition} Eksempel 3: andregradsfunksjon *vs* lineær funksjon
---
class: example
name: andregradsulikheter-grafisk-løsning-eksempel-3
---
En ulikhet er gitt ved

$$
x^2 + 5x + 1 \leq -x - 4.
$$

Løs ulikheten grafisk og oppgi løsningen som 
* En løsningsmengde
* Én eller flere ulikheter

:::::{admonition} Løsning
---
class: solution
---
Vi tegner grafene til funksjonene

$$
f(x) = x^2 + 5x + 1 \quad \text{og} \quad g(x) = -x - 4,
$$

Så leser vi av alle $x$-verdier der grafen til $f$ ligger **under eller på** grafen til $g$. Se {numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-3`.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-andregradsulikheter-grafisk-løsning-eksempel-3
width: 100%
---
Viser grafen til $f(x) = x^2 + 5x + 1$ og $g(x) = -x - 4$. Løsningsmengden til $f(x) \leq g(x)$ er markert i rødt på $x$-aksen.
:::

Fra {numref}`fig-andregradsulikheter-grafisk-løsning-eksempel-3` kan vi lese av at grafen til $f$ ligger under grafen til $g$ når $x > -5$ og $x < -1$. Grafen til $f$ ligger på grafne til $g$ når $x = -5$ og $x = -1$. Dermed er løsningen av ulikheten

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in [-5, -1]
$$
:::

:::{tab-item} Ulikheter
$$
-5 \leq x \leq -1
$$
:::
::::
:::::
::::::

**Din tur**!


::::::{admonition} Underveisoppgave 3
---
class: check
name: andregradsulikheter-grafisk-løsning-underveisoppgave-3
---
I {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-3` vises grafene til

$$
f(x) = x^2 + x + 1 \quad \text{og} \quad g(x) = -x + 4.
$$

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-3
width: 100%
---
Viser grafene til $f(x) = x^2 + x + 1$ og $g(x) = -x + 4$.
:::


Bruk figuren til å løse ulikheten 

$$
f(x) > g(x).
$$

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \mathbb{R} \setminus [-3, 1] \quad \Leftrightarrow \quad x \in \langle \gets, -3 \rangle \cup \langle 1, \to \rangle
$$
:::

:::{tab-item} Ulikheter
$$
x < -3 \, \lor \, x > 1
$$
:::
::::
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Siden vi skal løse ulikheten $f(x) > g(x)$, må vi lese av alle $x$ der grafen til $f$ ligger **over** grafen til $g$. Se {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-3-løsning`.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3_løsning.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-3-løsning
width: 100%
---
Viser grafene til $f(x) = x^2 + x + 1$ og $g(x) = -x + 4$. Løsningsmengden er markert i rødt på $x$-aksen.
:::

Vi kan se at grafen til $f$ ligger over grafen til $g$ når $x < -3$ og $x > 1$. Derfor er løsningen av ulikheten

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \mathbb{R} \setminus [-3, 1] \quad \Leftrightarrow \quad x \in \langle \gets, -3 \rangle \cup \langle 1, \to \rangle
$$
:::

:::{tab-item} Ulikheter
$$
x < -3 \, \lor \, x > 1
$$
:::
::::

:::::
::::::


**En til!**

::::::{admonition} Underveisoppgave 4: andregradsfunksjon *vs* andregradsfunksjon
---
class: check
name: andregradsulikheter-grafisk-løsning-eksempel-4
---
Grafene til andregradsfunksjonene


$$
f(x) = \dfrac{1}{2}x^2 + x - 3 \quad \text{og} \quad g(x) = -2x^2 - 4x - 3.
$$

er vist i {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-4`.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-4
width: 100%
---
Viser grafene til $f(x) = \dfrac{1}{2}x^2 + x - 3$ og $g(x) = -2x^2 - 4x - 3$.
:::

Bruk figuren til å løse ulikheten $f(x) < g(x)$. 


:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \langle -2, 0 \rangle
$$
:::

:::{tab-item} Ulikheter
$$
-2 < x < 0 \quad \text{eller} \quad -2 < x \, \land \, x < 0
$$
:::
::::


:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi tegner grafen til $f$ og $g$, og leser av hvor alle $x$ der grafen til $f$ ligger **under** grafen til $g$ er. Se {numref}`fig-andregradsulikheter-grafisk-løsning-underveisoppgave-4-løsning`.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4_løsning.svg
---
name: fig-andregradsulikheter-grafisk-løsning-underveisoppgave-4-løsning
width: 100%
---
Viser grafene til $f(x) = \dfrac{1}{2}x^2 + x - 3$ og $g(x) = -2x^2 - 4x - 3$. Løsningsmengden til $f(x) < g(x)$ er markert i rødt på $x$-aksen.
:::

Fra den grafiske framstillingen kan vi se at grafen til $f$ ligger på under grafen til $g$ når $x > -2$ og $x < 0$. Dermed er løsningen av ulikheten

::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \langle -2, 0 \rangle
$$
:::

:::{tab-item} Ulikheter
$$
-2 < x < 0 \quad \text{eller} \quad -2 < x \, \land \, x < 0
$$
:::
::::
:::::
::::::



## Oppgaver 


::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Grafen til 

$$
f(x) = x^2 - x - 2,
$$

er vist i {numref}`fig-andregradsulikheter-grafisk-løsning-oppgave-1`.


:::{figure} ./figurer/oppgaver/oppgave_1.svg
---
name: fig-andregradsulikheter-grafisk-løsning-oppgave-1
width: 80%
---
Viser grafen til $f(x) = x^2 - x - 2$.
:::

Bruk figuren til å løse ulikheten

$$
x^2 - x - 2 < 0,
$$

grafisk, og oppgi løsningen både som en løsningsmengde og som én eller flere ulikheter.


:::::{admonition} Fasit 
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in \langle -1, 2 \rangle
$$
:::

:::{tab-item} Ulikheter
$$
-1 < x < 2 \quad \text{eller} \quad -1 < x \, \land \, x < 2
$$
:::
::::
:::::
::::::


::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Grafen til 

$$
f(x) = x^2 - x - 4 \quad \text{og} \quad g(x) = x - 1,
$$

er vist i {numref}`fig-andregradsulikheter-grafisk-løsning-oppgave-2`.

:::{figure} ./figurer/oppgaver/oppgave_2.svg
---
name: fig-andregradsulikheter-grafisk-løsning-oppgave-2
width: 80%
---
Viser grafene til $f(x) = x^2 - x - 4$ og $g(x) = x - 1$.
:::

Bruk figuren til å

Oppgave 2a
: Løse ulikheten $f(x) > -2$ grafisk og oppgi løsningen som en løsningsmengde.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -1, 2 \rangle
$$
:::::


Oppgave 2b
: Løse ulikheten $f(x) \leq 2$ grafisk og oppgi løsningen som én eller flere ulikheter.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
-2 \leq x \leq 3
$$
:::::



Oppgave 2c
: Løse ulikheten $f(x) < g(x)$ grafisk og oppgi løsningen som en løsningsmengde.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x \in \langle -1, 3 \rangle
$$
:::::

::::::


:::::{admonition} Oppgave 3
---
class: problem-level-2
---
I {numref}`fig-andregradsulikheter-grafisk-løsning-oppgave-3` vises grafene til 

$$
f(x) = -x^2 + 5x - 4 \quad \text{og} \quad g(x) = x - 1 \quad \text{og} \quad h(x) = -x + 4.
$$

:::{figure} ./figurer/oppgaver/oppgave_3.svg
---
name: fig-andregradsulikheter-grafisk-løsning-oppgave-3
width: 80%
---
Viser grafene til $f(x) = -x^2 + 5x - 4$, $g(x) = x - 1$ og $h(x) = -x + 4$.
:::

I oppgavene under skal du bruke {numref}`fig-andregradsulikheter-grafisk-løsning-oppgave-3` og bruke grafene til $f$, $g$ og $h$.

Oppgave 3a
: Lag en ulikhet som har løsningen $x \in \langle 1, 4 \rangle$.

:::{admonition} Fasit: 3a
---
class: answer, dropdown
---
$$
-x^2 + 5x - 4 > 0
$$
:::

Oppgave 3b
: Lag en ulikhet som har løsningen $1 \leq x \leq 3$.

:::{admonition} Fasit: 3b
---
class: answer, dropdown
---
$$
-x^2 + 5x - 4 \geq x - 1
$$
:::

Oppgave 3c
: Lag en ulikhet som har løsningen $x \in \mathbb{R} \setminus [2, 4]$.

:::{admonition} Fasit: 3c
---
class: answer, dropdown
---
$$
-x^2 + 5x - 4 < -x + 4
$$
:::
:::::


::::::{admonition} Oppgave 4
---
class: problem-level-2
---
Under vises et interaktivt vindu for grafene til to funksjoner

$$
f(x) = ax^2 + bx + c \quad \text{og} \quad g(x) = px + q.
$$

:::{raw} html
---
file: ./figurer/oppgaver/oppgave_4.html
---
:::

<br>

Bruk figuren til å 

Oppgave 4a
: Løse ulikheten $-\dfrac{1}{2}x^2 -3x - 5 \geq x + 1$.

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Løsningsmengde
$$
x \in [-6, -2]
$$
:::

:::{tab-item} Ulikheter
$$
-6 \leq x \leq -2
$$
:::
::::
:::::



Oppgave 4b
: Lage en andregradsulikhet som har løsningen $x \in \langle -2, 1 \rangle$.

:::::{admonition} Fasit
---
class: answer, dropdown
---
Flere muligheter. En av dem er:

$$
x^2 < -x + 2
$$
:::::

::::::