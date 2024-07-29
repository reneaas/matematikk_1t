# Bestemme funksjonsuttrykk

::::{admonition} Læringsmål: bestemme funksjonsuttrykket til andregradsfunksjoner
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Bestemme funksjonsuttrykket til en andregradsfunksjon ved hjelp av lineære likningssystemer
* Bestemme funksjonsuttrykket til en andregradsfunksjon ved hjelp av nullpunktsfaktorisering
::::


## Bestemme $f(x)$ ved hjelp av lineære likningssystemer

En andregradsfunksjon har formen

$$
f(x) = ax^2 + bx + c.
$$

Når vi ikke kjenner til $f(x)$, er det *koeffisientene* $a$, $b$ og $c$ som er det *ukjente*. 


::::{admonition} Bestemme $f(x)$ med lineære likningssystemer
---
class: theory
---
For å bestemme en andregradsfunksjon

$$
f(x) = ax^2 + bx + c
$$

trenger vi

$$
\text{Tre punkter på grafen til } f \quad \Leftrightarrow \quad \text{Tre likninger}
$$
::::


:::::{admonition} Eksempel 1: Kjenner skjæring med $y$-aksen og to punkter
---
class: example
---
Grafen til en funksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-bestemme-funksjonsuttrykk-eksempel-1`. Tre punkter på grafen er markert.


:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-andregradsfunksjoner-bestemme-funksjonsuttrykk-eksempel-1
width: 100%
---
Viser grafen til en andregradsfunksjon $f$. Punktene $(0, 2)$, $(1, 2)$ og $(2, 4)$ ligger på grafen til $f$. 
:::

Bestem $f(x)$.

::::{admonition} Løsning
---
class: solution
---
Siden $f$ er en andregradsfunksjon, kan vi generelt uttrykke funksjonen som

$$
f(x) = ax^2 + bx + c.
$$

Fordi vi kjenner skjæringen med $y$-aksen fra punkt $(0, 2)$, kan vi bestemme konstantleddet $c$ direkte siden:

$$
f(0) = 2 \quad \Leftrightarrow \quad a\cdot 0^2 + b\cdot 0 + c = 2 \quad \Leftrightarrow \quad c = 2.
$$

Vi har to punkter igjen og to ukjente, så vi kan sette opp to likninger:

\begin{align*}
f(1) &= 2 \quad \Leftrightarrow \quad a\cdot 1^2 + b\cdot 1 + 2 = 2 \quad \Leftrightarrow \quad a + b + 2 = 2 \quad \Leftrightarrow \quad a + b = 0\\
\\
f(2) &= 4 \quad \Leftrightarrow \quad a\cdot 2^2 + b\cdot 2 + 2 = 4 \quad \Leftrightarrow \quad 4a + 2b + 2 = 4 \quad \Leftrightarrow \quad 2a + b = 1.
\end{align*}

Dermed sitter vi igjen med et lineært likningssystem:

\begin{align*}
a + b &= 0\\
2a + b &= 1.
\end{align*}

Vi kan løse dette med med innsettingsmetoden.


\begin{align*}
a + b &= 0 \quad \Leftrightarrow \quad a = -b && \text{Skriver om likning 1}\\
2(-b) + b &= 1 \quad \Leftrightarrow \quad -2b + b = 1 \quad \Leftrightarrow \quad -b = 1 \quad \Leftrightarrow \quad b = -1 && \text{Setter inn $a = -b$}\\
\end{align*}

:::::


Vi går løs på et eksempel.

:::::{admonition} Eksempel 2: kjenner tre punkter
---
class: example
---
Grafen til en funksjon $f$ er vist i {numref}`fig-andregradsfunksjoner-bestemme-funksjonsuttrykk-eksempel-2`. Punktene $(-1, 2)$, $(1, 4)$ og $(2, 2)$ ligger på grafen til $f$. 


:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-andregradsfunksjoner-bestemme-funksjonsuttrykk-eksempel-2
width: 100%
---
Viser grafen til en andregradsfunksjon $f$. Tre punkter på grafen er markert.
:::


Bestem $f(x)$. 

::::{admonition} Løsning
---
class: solution
---
Vi bruker den generelle formen for en andregradsfunksjon:

$$
f(x) = ax^2 + bx + c.
$$

Vi kan bruke de tre punktene til å sette opp én likning per punkt:

\begin{align*}
f(-1) &= 2 && \text{Punkt $(-1, 2)$}\\
\\
f(1) &= 4 && \text{Punkt $(1, 4)$} \\
\\
f(2) &= 2 && \text{Punkt $(2, 2)$}
\end{align*}

Her har vi tre likninger og tre ukjente. Å løse dette for hånd er tidkrevende, så vi bruker CAS for å løse dette fort:

:::{raw} html
---
file: geogebra/eksempler/cas_eksempel_2.html
::::

Fra CAS-programmet kan vi lese av at 

$$
f(x) = -x^2 + x + 4.
$$

:::::


## Nullpunktsfaktorisering

En annen metode for å bestemme funksjonsuttrykket til en andregradsfunksjon er å bruke nullpunktsfaktorisering.
:::::{admonition} Nullpunktsfaktorisering
---
class: theory
---
En andregradsfunksjon med nullpunkter $x_1$ og $x_2$ kan skrives på formen

$$
f(x) = a(x - x_1)(x - x_2)
$$

der $x_1$ og $x_2$ er løsningene av likningen

$$
ax^2 + bx + c = 0
$$
:::::

Vi kan anvende dette til å bestemme funksjonsuttrykket til andregradsfunksjoner både med ett og to nullpunkter.

:::::{admonition} Eksempel 3: to nullpunkter
---
class: example
---

I {numref}`fig-andregradsfunksjoner-likninger-anvendelser-eksempel-3` vises grafen til en andregradsfunksjon $f$.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-andregradsfunksjoner-likninger-anvendelser-eksempel-3
width: 100%
---
Viser grafen til en andregradsfunksjon $f$.
:::

Bestem $f(x)$. 

::::{admonition} Løsning
---
class: solution
---
Når $f$ har to nullpunkter, kan vi skrive funksjonsuttrykket på formen

$$
f(x) = a(x - x_1)(x - x_2).
$$

Vi kan lese av fra {numref}`fig-andregradsfunksjoner-likninger-anvendelser-eksempel-3` at nullpunktene til $f$ er 

$$
x_1 = -1 \quad \text{og} \quad x_2 = 2.
$$

Dermed kan vi skrive $f(x)$ som

$$
f(x) = a(x - (-1)) (x - 2) = a(x + 1)(x - 2).
$$

Vi må kjenne til ett punkt til på grafen slik at vi kan bestemme $a$. Vi ser for eksempel fra grafen at $f(0) = 2$, som gir likningen


\begin{align*}
f(\textcolor{red}{0}) &= 2 \\
&\Updownarrow \\
a(\textcolor{red}{0} + 1)(\textcolor{red}{0} - 2) &= 2 \\
&\Updownarrow \\
-2a &= 2 \\
&\Updownarrow \\
a &= -1.
\end{align*}

Dermed er 

$$
f(x) = -(x + 1)(x - 2).
$$
::::
:::::


**Din tur!**
