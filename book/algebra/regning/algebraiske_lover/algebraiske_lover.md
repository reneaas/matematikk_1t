# Algebraiske lover

:::{admonition} Læringsmål
---
class: tip
---
Etter å ha gått gjennom dette kapittelet, er målet at du skal:
* Kunne regne med de algebraiske lovene med tall.
* Kunne regne med de algebraiske lovene med bokstaver.
* Kunne gi praktiske tolkninger for de algebraiske lovene.
:::

Fundamentet for all algebra er de algebraiske lovene. Vi kan til sammen formulere 10 lover, som vi skal se nærmere på i dette kapittelet. Noen av disse lovene vil du trolig tenke på som selvfølgeligheter - andre kan det hende du ikke har sett eller tenkt over før.

## De kommutative lovene

De kommutative lovene forteller oss at rekkefølgene
* Rekkefølgen til leddene i addisjon er likegyldig.
* Rekkefølgen til faktorene i multiplikasjon er likegyldig.

Vi sier at addisjon og multiplikasjon *kommuterer*.

:::{admonition} De kommutative lovene
---
class: theory
---
For to tall $a$ og $b$ gjelder:

Addisjon: 
: $a + b = b + a$

Multiplikasjon
: $a \cdot b = b \cdot a$
:::

Vi tar et eksempel:

::::{admonition} Eksempel 1: kommutativ lov for addisjon
---
class: example
---
At addisjon er kommutativ kan vi se ved å se på regnestykkene

$$
3 + 2 \quad \text{og} \quad 2 + 3
$$

En begrunnelse kan vi finne grafisk. Det første regnestykke er illustrert i {numref}`fig-algebra-algebraiske-lover-eksempel-1a`. 

:::{figure} ./figurer/eksempler/eksempel_1a.svg
---
name: fig-algebra-algebraiske-lover-eksempel-1a
width: 80%
---
viser grafisk en tolkning av regnestykket $\textcolor{green}{3} + \textcolor{blue}{2}$. Vi starter i $0$ og flytter oss først $\textcolor{green}{3}$ plasser, etterfulgt av $\textcolor{blue}{2}$ plasser, mot høyre. Vi lander på $5$.
:::

Det andre regnestykke er illustrert i {numref}`fig-algebra-algebraiske-lover-eksempel-1b`.

:::{figure} ./figurer/eksempler/eksempel_1b.svg
---
name: fig-algebra-algebraiske-lover-eksempel-1b
width: 80%
---
viser grafisk en tolkning av regnestykket $\textcolor{blue}{2} + \textcolor{green}{3}$. Vi starter i $0$ og flytter oss først $\textcolor{blue}{2}$ plasser, etterfulgt av $\textcolor{green}{3}$ plasser, mot høyre. Vi lander på $5$.
:::

Som vi kan se fra figurene, så lander vi på samme posisjon på tallinja uavhengig av rekkefølgen vi velger - altså er addisjon kommutativ.

::::

---

## De assosiative lovene

De assosiative lovene forteller oss at 
* Rekkefølgen på hvilke ledd som adderes i en sum med tre eller flere ledd er likegyldig.
* Rekkefølgen på hvilke faktorer som multipliseres i et produkt med tre eller flere faktorer er likegyldig.

:::{admonition} De assosiative lovene
---
class: theory
---
Gitt tre tall $a$, $b$ og $c$ gjelder:

Addisjon
: $(a + b) + c = a + (b + c)$

Multiplikasjon
: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

:::

Vi tar et eksempel:

::::{admonition} Eksempel 2: assosiative lov for addisjon
---
class: example
---
Vi setter prøve på de to lovene:

Addisjon
: Vi ser på regnestykket 

    $$
    2 + 3 + 5
    $$

    Vi regner det ut på de to måtene:

    $$
    (2 + 3) + 5 = 5 + 5 = 10 \quad \text{og} \quad 2 + (3 + 5) = 2 + 8 = 10
    $$

    Vi får altså samme svar uansett hvilke to ledd vi legger sammen først.

<br>

Multiplikasjon
: Vi ser på regnestykket
    
    $$
    2 \cdot 3 \cdot 5
    $$

    Vi regner det ut på to måter:

    $$
    (2 \cdot 3) \cdot 5 = 6 \cdot 5 = 30 \quad \text{og} \quad 2 \cdot (3 \cdot 5) = 2 \cdot 15 = 30
    $$

    Vi får altså det samme svar uansett hvilke to faktorer vi multipliserer først.
::::

---

## De distributive lovene

De distributive lovene forteller oss hvordan vi skal åpne parenteser:

:::{admonition} De distributive lovene
---
class: theory
---
Gitt tre tall $a$, $b$ og $c$, gjelder:

Addisjon
: $a + (b - c) = a + b - c$
: $ a - (b - c) = a - b + c$

Multiplikasjon
: $a \cdot (b + c) = a \cdot b + a \cdot c$
:::