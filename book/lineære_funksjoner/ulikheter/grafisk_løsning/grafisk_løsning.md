# Grafisk løsning

:::{admonition} Læringsmål: grafisk løsning av lineære ulikheter
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Løse lineære ulikheter grafisk av typene
    * $ax + b > 0$
    * $ax + b > k$
    * $ax + b > cx + d$
* Løse tilsvarende ulikheter med sammenlikningsoperatorene $\geq$, $<$ og $\leq$.
* Kunne oppgi løsningen til en ulikhet som
    * En ulikhet
    * En løsningsmengde
:::


## Ulikheter på formen $ax + b > 0$

::::{admonition} Ulikheter på formen $ax + b > 0$
---
class: theory
---
Gitt en lineær funksjon $f(x) = ax + b$, kan vi sette opp fire ulikheter som vist i tabellen under. Løsningsmengden til ulikheten vil variere avhengig av type ulikhet.

| Ulikhet | Løsningsmengde |
|---------|----------------|
| $ax + b > 0$ | $x \in L$ der grafen til $f$ er **over** $x$-aksen |
| $ax + b \geq 0$ | $x \in L$ der grafen til $f$ er **på** eller **over** $x$-aksen |
| $ax + b < 0$ | $x \in L$ der grafen til $f$ er **under** $x$-aksen |
| $ax + b \leq 0$ | $x \in L$ der grafen til $f$ er **på** eller **under** $x$-aksen |

<br>

Løsningen til en ulikhet oppgis enten som en ulikhet eller som en løsningsmengde.

Figuren under illustrerer de fire tilfellene.

:::{figure} ./figurer/teori/ulikhet_type_1.svg
---
name: lineære-ulikhter-grafisk-teori-1
width: 100%
---
Figuren til venstre viser løsningsmengden for ulikhetene $ax + b < 0$ og $ax + b \leq 0$. Figuren til høyre viser løsningsmengden for ulikhetene $ax + b > 0$ og $ax + b \geq 0$. Nullpunktet til $f$ er inkludert i løsningsmengden når likhet er tillatt.
:::
::::


Vi går løs på et eksempel.

:::::{admonition} Eksempel 1
---
class: example
name: lineære-ulikheter-grafisk-eksempel-1
---
En lineær ulikhet er gitt ved 

$$
-2x + 4 > 0.
$$

Bestem løsningsmengden til ulikheten.

::::{admonition} Løsning
---
class: solution
---
Vi tegner grafen til den lineære funksjonen $f(x) = -2x + 4$ som er vist i figuren under. Deretter finner vi alle $x$-verdier der grafen til $f$ ligger på oversiden av $x$-aksen. 

:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-lineære-ulikheter-grafisk-eksempel-1
width: 80%
---
Figuren viser grafen til $f(x) = -2x + 4$ og løsningsmengden til ulikheter $-2x + 4 > 0$. Merk at $x = 2$ ikke er inkludert i løsningsmengden.
:::

Fra grafen til $f$, kan vi se at så lenge $x < 2$, så ligger grafen på oversiden av $x$-aksen. 

Vi oppgir løsningen av en ulikhet enten som en ulikhet eller som en løsningsmengde. Dermed blir løsningen av ulikheten her

$$
\underbrace{x < 2}_\text{Ulikhet} \quad \text{eller} \quad \underbrace{x \in \langle \gets, 2\rangle}_\text{Løsningsmengde}
$$
::::
:::::

Så er det **din tur**!

::::::{admonition} Underveisoppgave 1
---
class: check
---
En lineær ulikhet er gitt ved

$$
x - 3 \leq 0.
$$

Grafen til den lineære funksjonen $f(x) = x - 3$ er vist i figuren under. 


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: fig-lineære-ulikheter-grafisk-underveisoppgave-1
width: 80%
---
Figuren viser grafen til $f(x) = x - 3$.
:::

<br>

Bestem løsningen til ulikheten grafisk og oppgi den som
* En ulikhet
* En løsningsmengde

:::{admonition} Hint: hva skal du se etter grafisk nå?
---
class: hints, dropdown
---
Siden du skal bestemme $x - 3 \leq 0$, må du se etter hvor grafen til $f(x) = x - 3$ er **på** eller **under** $x$-aksen.
:::

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Ulikhet
$x \leq 3$
:::

:::{tab-item} Løsningsmengde
$x \in \langle \gets, 3]$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Siden vi skal løse ulikheten $x - 3 \leq 0$, ser vi etter hvor grafen til $f(x) = x - 3$ er **på** eller **under** $x$-aksen. Se figuren under:

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1_løsning.svg
---
name: fig-lineære-ulikheter-grafisk-underveisoppgave-1-løsning
width: 80%
---
:::

Grafen til $f$ ligger på undersiden av $x$-aksen når $x < 3$. Grafen ligger *på* $x$-aksen når $x = 3$. Dermed er løsningen til ulikheten

$$
x \leq 3 \quad \text{eller} \quad x \in \langle \gets, 3]
$$
:::::

::::::


## Ulikheter  på formen $ax + b > k$
Vi kan i prinsippet alltid skrive om en lineær ulikhet til formen $ax + b > 0$. Men når vi jobber grafisk, kan vi også løse ulikheter på formen $ax + b > k$ direkte.

::::{admonition} Ulikheter  på formen $ax + b > k$
---
class: theory
---
Gitt en lineær funksjon $f(x) = ax + b$ og en horisontal linje $y = k$, kan vi løse fire ulikheter som forklart i tabellen nedenfor.

| Ulikhet | Løsningsmengde |
|---------|----------------|
| $ax + b > k$ | $x \in L$ der grafen til $f$ er **over** linja $y = k$ |
| $ax + b \geq k$ | $x \in L$ der grafen til $f$ er **på** eller **over** linja $y = k$ |
| $ax + b < k$ | $x \in L$ der grafen til $f$ er **under** linja $y = k$ |
| $ax + b \leq k$ | $x \in L$ der grafen til $f$ er **på** eller **under** linja $y = k$ |

Løsningen til ulikheten oppgis enten som en ulikhet eller som en løsningsmengde.

Figuren under illustrerer de ulike tilfellene:

:::{figure} ./figurer/teori/ulikhet_type_2.svg
---
name: lineære-ulikhter-grafisk-teori-2
width: 100%
---
Figuren viser løsningsmengden til ulikhetene $ax + b < k$ og $ax + b \leq k$ til venstre, og $ax + b > k$ og $ax + b \geq k$ til høyre. $x$-verdien til skjæringspunktet mellom grafen til $f$ og linja $y = k$ er inkludert i løsningsmengden når likhet er tillatt.
:::
::::

Vi går løs på et eksempel med det samme:

:::::{admonition} Eksempel 2
---
class: example
name: lineære-ulikheter-grafisk-eksempel-2
---
En lineær ulikhet er gitt ved 

$$
2x + 1 \leq 3.
$$

Løs ulikheten grafisk og oppgi løsningen som en ulikhet og som en løsningsmengde.

::::{admonition} Løsning
---
class: solution
---
Vi starter med å tegne grafen til $f(x) = 2x + 1$ og en linje $y = 3$. Deretter finner vi alle $x$-verdier der grafen til $f$ ligger **på** eller **under** linja $y = 3$.

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-lineære-ulikheter-grafisk-eksempel-2
width: 80%
---
Figuren viser grafen til $f(x) = 2x + 1$ og linja $y = 3$. Løsningsmengden er illustrert på $x$-aksen. $x$-verdien til skjæringen mellom grafen til $f$ og linja $y = 3$ er inkludert i løsningsmengden fordi likhet er tillatt.
:::

Fra den grafiske framstillingen, kan vi se at grafen til $f$ ligger på linja $y = 3$ når $x = 1$. Videre ligger grafen til $f$ under linja så lenge $x < 1$. Dermed er løsningen av ulikheten

$$
\underbrace{x \leq 1}_\text{Ulikhet} \quad \text{eller} \quad \underbrace{x \in \langle \gets, 1]}_\text{Løsningsmengde}
$$
::::

:::::

Nå er det **din tur**!

::::::{admonition} Underveisoppgave 2
---
class: check
---
Figuren under viser grafen til $f(x) = -3x + 2$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
name: fig-lineære-ulikheter-grafisk-underveisoppgave-2
width: 80%
---
Grafen til $f(x) = -3x + 2$
:::

Bruk figuren til å løse ulikheten 

$$
-3x + 2 > -1
$$

og oppgi løsningen som
* En ulikhet
* En løsningsmengde


:::{admonition} Hint: hva skal du se etter grafisk nå?
---
class: hints, dropdown
---
Her må du tegne den horisontale linja selv, eller lese av hvor den går.
:::


:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Ulikhet
$$
x < 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \langle \gets, 1\rangle
$$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi starter med å tegne grafen til $f(x) = -3x + 2$ og linja $y = -1$. Deretter finner vi alle $x$-verdier der grafen til $f$ ligger **over** linja $y = -1$.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2_løsning.svg
---
name: fig-lineære-ulikheter-grafisk-underveisoppgave-2-løsning
width: 80%
---
:::

Fra grafen kan vi lese av at grafen til $f$ ligger over linja $y = -1$ når $x < 1$. Dermed er løsningen av ulikheten

$$
\underbrace{x < 1}_\text{Ulikhet} \quad \text{eller} \quad \underbrace{x \in \langle \gets, 1\rangle}_\text{Løsningsmengde}
$$
:::::


::::::


## Ulikheter  på formen $ax + b > cx+d$

Vi kan også løse ulikheter av typen $ax + b > cx + d$ grafisk.


:::::{admonition} Ulikheter  på formen $ax + b > cx+d$
---
class: theory
---

Gitt to lineære funksjoner $f(x) = ax + b$ og $g(x) = cx + d$, kan vi sette opp fire ulikheter som forklart i tabellen nedenfor.

| Ulikhet | Løsningsmengde |
|---------|----------------|
| $ax + b > cx + d$ | $x \in L$ der grafen til $f$ er **over** grafen til $g$ |
| $ax + b \geq cx + d$ | $x \in L$ der grafen til $f$ er **på** eller **over** grafen til $g$ |
| $ax + b < cx + d$ | $x \in L$ der grafen til $f$ er **under** grafen til $g$ |
| $ax + b \leq cx + d$ | $x \in L$ der grafen til $f$ er **på** eller **under** grafen til $g$ |

Løsningen til ulikheten oppgis enten som en ulikhet eller som en løsningsmengde.

Figuren under illustrerer de ulike tilfellene:

:::{figure} ./figurer/teori/ulikhet_type_3.svg
---
name: lineære-ulikhter-grafisk-teori-3
width: 100%
---
Grafisk representasjon av løsningsmengden til ulikhetene i tabellen over. $x$-verdien til skjæringspunktet mellom grafen til $f$ og grafen til $g$ er inkludert i løsningsmengden når likhet er tillatt.
:::
:::::



:::::{admonition} Eksempel 3
---
class: example
name: lineære-ulikheter-grafisk-eksempel-3
---

En lineær ulikhet er gitt ved

$$
-3x - 1 \geq x + 3.
$$

Løs ulikheten grafisk.



::::{admonition} Løsning
---
class: solution
---
Vi starter med å tegne grafene til de to lineære funksjonene

$$
f(x) = -3x - 1 \quad \text{og} \quad g(x) = x + 3.
$$

Deretter finner vi alle $x$-verdier der grafen til $f$ ligger **på** eller **over** grafen til $g$. Figuren illustrerer løsningsmengden grafisk.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-lineære-ulikheter-grafisk-eksempel-3
width: 80%
---

Figuren viser grafene til $f(x) = -3x - 1$ og $g(x) = x + 3$. Løsningsmengden er illustrert på $x$-aksen. $x$-verdien til skjæringen mellom grafen til $f$ og grafen til $g$ er inkludert i løsningsmengden fordi likhet er tillatt.
:::

Fra den grafiske framstillingen, kan vi konkludere at løsningen av ulikheten er 

$$
\underbrace{x \leq -2}_\text{Ulikhet} \quad \text{eller} \quad \underbrace{x \in \langle \gets, -2]}_\text{Løsningsmengde}
$$
::::
:::::

Nå er det **din tur**!

::::::{admonition} Underveisoppgave 3
---
class: check
---
Figuren under viser grafene til

$$
f(x) = 3x - 1 \quad \text{og} \quad g(x) = x + 1.
$$

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3.svg
---
name: fig-lineære-ulikheter-grafisk-underveisoppgave-3
width: 80%
---
:::

Bruk den grafiske framstillingen til å løse ulikheten

$$
3x - 1 < x + 1.
$$

Oppgi løsningen både som en ulikhet og en løsningsmengde.

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Ulikhet
$$
x < 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \langle \gets, 1\rangle
$$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å løse ulikheten 

$$
3x - 1 < x + 1 \quad \Leftrightarrow \quad f(x) < g(x),
$$

der vi etter hvilke verdier av $x$ der grafen til $f$ ligger **under** grafen til $g$. Dette kan vi lese av er når $x < 1$, som er illustrert grafisk i figuren under.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3_løsning.svg
---
name: fig-lineære-ulikheter-grafisk-underveisoppgave-3-løsning
width: 80%
---
:::

Løsningen av ulikheten er derfor
::::{tab-set}
:::{tab-item} Ulikhet
$$
x < 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \langle \gets, 1\rangle
$$
:::
::::
:::::

::::::