# $abc$-formelen

::::{admonition} Læringsmål
---
class: tip
---
* Kunne løse andregradslikninger ved å skrive om et andregradsuttrykk fra standardform til nullpunktsform.
* Kunne løse andregradslikninger med $abc$-formelen.
* Kunne bestemme antall løsninger for en andregradslikning. 
::::

## Andregradslikninger

En **andregradslikning** er en likning som alltid kan skrives på formen 

$$
ax^2 + bx + c = 0.
$$

Vi kan gjenkjenne dette som å bestemme nullpunktene til en andregradsfunksjon $f(x) = ax^2 + bx + c$. Vi har allerede sett på hvordan vi kan skrive om et andregradsuttrykk fra standardform til ekstremalform og deretter til nullpunktsform – dette er første steg mot å bestemme den helt generelle løsningen av en andregradslikning.

Vi tar et eksempel.

:::::{admonition} Eksempel 1: andregradslikning
---
class: example
---
Løs likningen 

$$
x^2 + 3x - 5 = 4x - 3
$$

::::{admonition} Løsning
---
class: solution
---
Vi starter med å samle alle leddene på én side av likningen:

\begin{align*}
    x^2 + 3x - 5 &= 4x - 3 \\
    \\
    x^2 + 3x - 5 \textcolor{red}{- 4x + 3} &= 4x - 3  \textcolor{red}{- 4x + 3} \\
    \\
    x^2 - x - 2 &= 0.
\end{align*}

Løsningen av likningen er derfor det samme som å nullpunktene til $f(x) = x^2 - x - 2$. Hvis vi skriver om $f(x)$ til nullpunktsform, har vi derfor effektivt løst likningen. 

Så skriver vi om andregradsuttrykket i likningen i følgende steg:
1. Fra standardform til ekstremalform med fullstendige kvadraters metode
2. Fra ekstremalform til nullpunktsform med konjugatsetningen


\begin{align*}
    x^2 - x - 2 &= \underbrace{x^2 - x + \textcolor{red}{\left(-\dfrac{1}{2}\right)^2}}_{\text{2.kvadratsetning}} - \textcolor{red}{\left(-\dfrac{1}{2}\right)^2} - 2 \\
    \\
    &= \left(x - \dfrac{1}{2}\right)^2 - \dfrac{1}{4} - 2 && \text{Brukte 2.kvadratsetning}\\
    \\
    &= \left(x - \dfrac{1}{2}\right)^2 - \dfrac{9}{4} \\
    \\
    &= \left(x - \dfrac{1}{2}\right)^2 - \left(\dfrac{3}{2}\right)^2 && \text{$a = x - \dfrac{1}{2}$ og $b = \dfrac{3}{2}$}\\
    \\
    &= \left(x - \dfrac{1}{2} + \dfrac{3}{2}\right)\left(x - \dfrac{1}{2} - \dfrac{3}{2}\right) && \text{Brukte konjugatsetning} \\
    \\
    &= \left(x + 1\right)\left(x - 2\right).
\end{align*}

Nå har vi uttrykket på nullpunktsform som gir oss løsningene til likningen:

$$
x = -1 \quad \lor \quad x = 2
$$

::::
:::::


På dette tidspunktet har vi gjort nok forberedelser til å kunne komme fram til en helt generell løsning for *alle* andregradslikninger når de er skrevet på formen

$$
ax^2 + bx + c = 0.
$$

Løsningen av likningen kalles ofte for **$abc$-formelen** fordi den inneholder koeffisientene $a$, $b$ og $c$. Vi skal første presentere den generelle løsningen og deretter utlede den ved hjelp av teknikkene vi har sett på så langt.

## Den generelle løsningen


:::{admonition} Husk: $\pm$-symbolet
---
class: reminder, margin
---
$\pm$-tegnet leses som "pluss eller minus" og betyr at vi skal regne ut formelen to ganger
* Én gang med "$+$"
* Én gang med "$-$".
:::


::::{admonition} Setning: $abc$-formelen
---
class: theory
---
Løsningen til en andregradslikning

:::{figure} ./figurer/teori/andregradslikning.svg
---
width: 30%
class: no-click, adaptive-figure
---
:::


er gitt ved

:::{figure} ./figurer/teori/abc-formel.svg
---
width: 35%
class: no-click, adaptive-figure
---
::::

:::

Senere skal du få utlede denne formelen med litt hjelp – nå tar vi et eksempel på bruken av den.

::::{admonition} Eksempel 2: $abc$-formelen
---
class: example
---

Løs likningen

$$
x^2 - 4x - 5 = 0.
$$

:::{admonition} Løsning
---
class: solution
---
Fra likningen kan vi lese av at koeffisientene er 

$$
a = 1 \quad \text{og} \quad b = -4 \quad \text{og} \quad c = -5.
$$

Vi setter inn disse i $abc$-formelen som gir:

\begin{align*}
x & = \frac{-(-4) \pm \sqrt{(-4)^2 - 4\cdot 1 \cdot (-5)}}{2\cdot 1} = \frac{4 \pm \sqrt{16 + 20}}{2} = \frac{4 \pm \sqrt{36}}{2} \\
\\
& = \frac{4 \pm 6}{2} 
\end{align*}


Vi regner ut de to mulige løsningene, en med "$+$" og en med "$-$" som gir

$$
x = 5 \quad \lor \quad x = -1.
$$
:::
::::

Nå kan du prøve deg på en oppgave for å teste forståelsen din!

::::{admonition} Har du glemt? $abc$-formelen
---
class: sidenote, margin
---
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
::::

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bruk $abc$-formelen til å løse likningene.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a

$$
x^2 - 3x - 4 = 0.
$$

:::{admonition} Fasit
---
class: dropdown, answer
---

$$
x = 4 \quad \lor \quad x = -1.
$$
:::

:::::::::::::

:::::::::::::{tab-item} b

$$
2x^2 + 8x + 8 = 0
$$

:::{admonition} Fasit
---
class: dropdown, answer
---

$$
x = -2
$$

:::

:::::::::::::

:::::::::::::{tab-item} c

$$
x^2 + 4x + 5 = 0
$$

:::{admonition} Hint
---
class: hints
---
Hvis noe ser ut til å gå galt, kan det hende du regner riktig likevel – hvis det er en eller annen regning som ikke er lov, kan det hende det forteller oss noe om løsningene. 
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
Ingen løsninger.
:::

:::::::::::::


::::::::::::::
:::::::::::::::


---



## Antall løsninger
Vi kan bruke $abc$-formelen til å bestemme hvor mange løsninger en andregradslikning har. 


::::{admonition} $abc$-formelen og diskriminanten
---
class: sidenote, margin
---
Med diskriminanten kan vi skrive $abc$-formelen på en annen måte:

\begin{align*}
x & = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
\\
x & = \frac{-b \pm \sqrt{D}}{2a}
\end{align*}

De ulike tilfellene handler altså om hva som skjer når vi tar roten av $D$. Spesielt får vi ingen løsning når $D
< 0$ fordi vi ikke kan ta roten av et negativt tall. 
::::

::::{admonition} Setning: Antall løsninger for en andregradslikning
---
class: theory
---
For en andregradslikning 

:::{figure} ./figurer/teori/andregradslikning.svg
---
width: 30%
class: no-click, adaptive-figure
---
:::

definerer vi **diskriminanten** $D$ som

:::{figure} ./figurer/teori/diskriminant.svg
---
width: 40%
class: no-click, adaptive-figure
---
:::

Antall løsninger likningen har er bestemt av betingelsene i tabellen under.

| Antall løsninger | Betingelse |
|:------------------:|:------------:|
| 2 | $D > 0$ |
| 1 | $D = 0$ |
| Ingen | $D < 0$ | 

::::

Vi tar et eksempel.

:::::::::::::::{admonition} Eksempel 3
---
class: example
---
Under ser vi hvordan vi kan bestemme antall løsninger i tre tilfeller. Du kan sammenligne med grafen under for å se at det stemmer. 

::::::::::::::{tab-set}
:::::::::::::{tab-item} To løsninger

````{card}
**Likning**

$$
x^2 - 2x - 8 = 0
$$

^^^
**Koeffisienter**

$$
a = 1 \quad \text{og} \quad b = -2 \quad \text{og} \quad c = -8.
$$

**Diskriminant**

$$
D = b^2 - 4ac = (-2)^2 - 4\cdot 1 \cdot (-8) = 4 + 32 = 36
$$

+++

**Graf**

:::{figure} ./figurer/eksempler/eksempel_2/to_løsninger.svg
---
width: 80%
---
viser at grafen til $f(x) = x^2 - 2x - 8$ skjærer $x$-aksen i to punkter som stemmer med at likningen har to løsninger.
:::

````


:::::::::::::

:::::::::::::{tab-item} Én løsning

````{card}

**Likning**

$$
x^2 + 4x + 4 = 0
$$

^^^

**Koeffisienter**

$$
a = 1 \quad \text{og} \quad b = 4 \quad \text{og} \quad c = 4.
$$

**Diskriminant**

$$
D = b^2 - 4ac = 4^2 - 4\cdot 1 \cdot 4 = 16 - 16 = 0.
$$

+++

**Graf**

:::{figure} ./figurer/eksempler/eksempel_2/en_løsning.svg
---
width: 80%
---
viser at grafen til $f(x) = x^2 + 4x + 4$ skjærer $x$-aksen i ett punkt som stemmer med at likningen bare har én løsning når $D = 0$.
:::

````

:::::::::::::

:::::::::::::{tab-item} Ingen løsning

````{card}
**Likning**: 

$$
x^2 + x + 1 = 0
$$

^^^

**Koeffisienter**

$$
a = 1 \quad \text{og} \quad b = 1 \quad \text{og} \quad c = 1.
$$

**Diskriminant**

$$
D = b^2 - 4ac = 1^2 - 4\cdot 1 \cdot 1 = 1 - 4 = -5.
$$

+++

**Graf**

:::{figure} ./figurer/eksempler/eksempel_2/ingen_løsning.svg
---
width: 80%
---
viser grafen til $f(x) = x^2 + x + 1$ som ikke skjærer $x$-aksen i noen punkter, som stemmer med at likningen ikke har noen løsninger når $D < 0$. 
:::

````

:::::::::::::

::::::::::::::

:::::::::::::::

---


## Utledning av $abc$-formelen
Du har vært med på å gjøre alt forarbeidet som skal til for å komme fram til $abc$-formelen. Du skal derfor få utlede den under med litt hjelp underveis.

:::::::::::::::{admonition} Utforsk 1: Utledning av $abc$-formelen
---
class: explore
---
Vi går ut ifra en helt generell andregradslikning 

$$
ax^2 + bx + c = 0.
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Vis ved regning at likningen

$$
ax^2 + bx + c = 0,
$$

kan skrives om til 

$$
x^2 + \frac{b}{a}x + \frac{c}{a} = 0.
$$

:::{admonition} Løsning
---
class: solution, dropdown
---

\begin{align*}
ax^2 + bx + c & = 0 \\
\\
\dfrac{\cancel{a}x^2}{\cancel{a}} + \dfrac{bx}{a} + \dfrac{c}{a} & = 0 && \text{Deler med $a$ i alle ledd}\\
\\
x^2 + \frac{b}{a}x + \frac{c}{a} & = 0.
\end{align*}

::: 

:::::::::::::

:::::::::::::{tab-item} b
For å gjøre stegene videre lettere å regne med, innfører vi to nye variabler 

$$
B = \dfrac{b}{2a} \quad \text{og} \quad C = \dfrac{c}{a}.
$$

Vis ved regning at dette betyr at likningen nå kan skrives som 

$$
x^2 + 2Bx + C = 0.
$$

> Dette er bare et midlertidig **variabelskifte**. Vi skal bytte tilbake igjen til slutt! Dette er vanlig å bruke i matematikken for å gjøre regning underveis enklere så vi unngår unødvendige feil.

:::{admonition} Hint
---
class: hints, dropdown
---
Du kan uttrykke de nye variablene slik at du kan bytte ut $b$ og $c$ i likningen. For eksempel så er 

$$
c = a\cdot C
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
Vi skriver om de nye variabelene:

\begin{equation*}
    \begin{matrix}
        B = \dfrac{b}{2a} \quad & \text{og} & \quad C = \dfrac{c}{a} \\
        \\
        2a\cdot B = \dfrac{b}{\cancel{2a}}\cdot \cancel{2a} \quad & \text{og} & \quad a\cdot C = \dfrac{c}{\cancel{a}} \cdot \cancel{a} \\
        \\
        2aB = b \quad & \text{og} & \quad aC = c
    \end{matrix}
\end{equation*}

så setter vi inn de nye uttrykkene for $b$ og $c$ i likningen:

\begin{align*}
    x^2 + \dfrac{b}{a}x + \dfrac{c}{a} &= 0 \\
    \\
    x^2 + \dfrac{2aB}{a}x + \dfrac{aC}{a} &= 0 \\
    \\
    x^2 + \dfrac{2\cancel{a}B}{\cancel{a}}x + \dfrac{\cancel{a}C}{\cancel{a}} &= 0 \\
    \\
    x^2 + 2Bx + C &= 0.
\end{align*}

:::

:::::::::::::

:::::::::::::{tab-item} c
Vis ved å bruke fullstendig kvadraters metode at du kan skrive om likningen

$$
x^2 + 2Bx + C = 0
$$

til 

$$
(x + B)^2 = B^2 - C
$$

:::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
    x^2 + 2Bx + C &= 0 \\
    \\
    \underbrace{x^2 + 2Bx + \textcolor{red}{B^2}}_{\displaystyle (x + B)^2} - \textcolor{red}{B^2} + C &= 0 \\
    \\
    \textcolor{red}{(x + B)^2} - B^2 + C &= 0 && \text{1.kvadratsetning}\\
    \\
    (x + B)^2 - B^2 \textcolor{red}{+ B^2} + C \textcolor{red}{- C} &= \textcolor{red}{B^2 - C} \\
    \\
    (x + B)^2 &= B^2 - C.
\end{align*}
:::

:::::::::::::

:::::::::::::{tab-item} d
Argumenter for at

$$
(x + B)^2 = B^2 - C
$$

betyr at 

$$
x + B = \pm \sqrt{B^2 - C}.
$$

:::{admonition} Løsning
---
class: solution, dropdown
---
Vi tar kvadratroten på hver side av likningen, men husker på at det betyr at den ene siden kan være både positiv og negativ:

\begin{align*}
    (x + B)^2 &= B^2 - C \\
    \\
    \sqrt{(x + B)^2} &= \pm \sqrt{B^2 - C} \\
    \\
    x + B &= \pm \sqrt{B^2 - C}.
\end{align*}

> Det spiller egentlig ingen rolle hvilken side vi plasserer $\pm$ ved. Men å plassere den sammen med variabelen vil gjøre det litt vanskeligere å komme fram til $abc$-formelen til slutt.
:::

:::::::::::::


:::::::::::::{tab-item} e
Vis ved regning at 

$$
x + B = \pm \sqrt{B^2 - C} \quad  \iff \quad x = -\dfrac{b}{2a} \pm \sqrt{\left(\dfrac{b}{2a}\right)^2 - \dfrac{c}{a}}
$$

ved å sette tilbake 

$$
B = \dfrac{b}{2a} \quad \text{og} \quad C = \dfrac{c}{a}
$$

i likningen.


:::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
    x + B &= \pm \sqrt{B^2 - C} \\
    \\
    x + B \textcolor{red}{-B} &= \textcolor{red}{-B} \pm \sqrt{B^2 - C} \\
    \\
    x &= -B \pm \sqrt{B^2 - C} \\
    \\
    x &= -\dfrac{b}{2a} \pm \sqrt{\left(\dfrac{b}{2a}\right)^2 - \dfrac{c}{a}} && \text{Husk: } B = \dfrac{b}{2a} \quad \text{og} \quad C = \dfrac{c}{a} \\
    \\
\end{align*}
:::

:::::::::::::

:::::::::::::{tab-item} f
Vis ved regning at 

$$
x = -\dfrac{b}{2a} \pm \sqrt{\left(\dfrac{b}{2a}\right)^2 - \dfrac{c}{a}}
$$

kan skrives om til $abc$-formelen

$$
x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$


:::{admonition} Hint
---
class: hints, dropdown
---
Når du tar kvadratroten av en brøk, så gjelder:

$$
\sqrt{\dfrac{A}{B}} = \dfrac{\sqrt{A}}{\sqrt{B}}
$$
:::


:::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
    x &= -\dfrac{b}{2a} \pm \sqrt{\left(\dfrac{b}{2a}\right)^2 - \dfrac{c}{a}} \\
    \\
    x &= -\dfrac{b}{2a} \pm \sqrt{\textcolor{red}{\dfrac{b^2}{4a^2}} - \dfrac{c}{a}} && \text{ganger ut potensen}\\
    \\
    x &= -\dfrac{b}{2a} \pm \sqrt{\dfrac{b^2}{4a^2} - \dfrac{\textcolor{red}{4a}}{\textcolor{red}{4a}} \cdot \dfrac{c}{a}} && \text{lager fellesnevner} \\
    \\
    x &= -\dfrac{b}{2a} \pm \sqrt{\dfrac{b^2}{4a^2} - \dfrac{4ac}{4a^2}} \\
    \\
    x &= -\dfrac{b}{2a} \pm \sqrt{\dfrac{b^2 - 4ac}{4a^2}} \\
    \\
    x &= -\dfrac{b}{2a} \pm \dfrac{\sqrt{b^2 - 4ac}}{\sqrt{4a^2}} && \text{Regneregel: } \sqrt{\dfrac{A}{B}} = \dfrac{\sqrt{A}}{\sqrt{B}} \\
    \\
    x &= -\dfrac{b}{2a} \pm \dfrac{\sqrt{b^2 - 4ac}}{2a} \\
    \\
    x &= \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
\end{align*}

:::

:::::::::::::


::::::::::::::

---

> Når du har gjennomført oppgave a - f, så har du bevist $abc$-formelen! 


:::::::::::::::


