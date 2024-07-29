# Anvendelser

::::{admonition} Læringsmål
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Bestemme funksjonsuttrykket til en andregradsfunksjon ved hjelp av nullpunktsfaktorisering.
::::


## Nullpunktsfaktorisering


:::::{admonition} Nullpunktsfaktorisering
---
class: theory
---
En andregradsfunksjon med nullpunkter $x_1$ og $x_2$ kan skrives på formen

$$
f(x) = a(x - x_1)(x - x_2).
$$


:::::

Vi kan anvende dette til å bestemme funksjonsuttrykket til andregradsfunksjoner både med ett og to nullpunkter.

:::::{admonition} Eksempel 1: to nullpunkter
---
class: example
---

I {numref}`fig-andregradsfunksjoner-likninger-anvendelser-eksempel-1` vises grafen til en andregradsfunksjon $f$.

:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-andregradsfunksjoner-likninger-anvendelser-eksempel-1
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

Vi kan lese av fra {numref}`fig-andregradsfunksjoner-likninger-anvendelser-eksempel-1` at nullpunktene til $f$ er 

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
