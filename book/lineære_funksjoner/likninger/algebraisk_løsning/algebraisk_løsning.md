# Algebraisk løsning

:::{admonition} Læringsmål: algebraisk løsning av lineære likninger
---
class: tip
---
Etter dette kapittelet, er målet at du skal:
* Kunne løse lineære likninger algebraisk.
* Kunne koble sammen algebraiske problemer med grafiske tolkninger.
* Kunne uttrykke løsningene som både likninger og løsningsmengder.
:::

## Algebraisk løsning av lineære likninger

Å løse likninger algebraisk handler om å isolere variabelen i likningen ved hjelp av algebraisk regning. For å gjøre dette, har vi følgende regneregler å benytte oss av:

::::{admonition} Regneregler for likninger
---
class: theory
---
Når vi jobber med en likning algebraisk, kan vi:
1. Legge til det samme på begge sider.
2. Trekke fra det samme på begge sider.
3. Gange med det samme på begge sider.
4. Dele med det samme på begge sider.

::::

Vi tar et eksempel

::::{admonition} Eksempel 1
---
class: example
---
Løs likningen 

$$
-x + 2 = 2x + 5.
$$

:::{admonition} Løsning
---
class: solution
---
Målet er å bestemme hvilken verdi $x$ må ha for at likningen er sann. Typisk vil vi få alle ledd med $x$ på én side og alle ledd bestående av tall på den andre siden av likhetstegnet.

\begin{align*}
-x + 2 &= 2x + 5 \\
\\
-x + 2 \textcolor{red}{- 2} &= 2x + 5 \textcolor{red}{- 2} && \text{Trekker fra 2 på begge sider}\\
\\
-x &= 2x + 3 \\
\\
-x \textcolor{red}{- 2x} &= 2x \textcolor{red}{- 2x} + 3 && \text{Trekker fra $2x$ på begge sider}\\
\\
-3x &= 3 \\
\\
\frac{\bcancel{-3}x}{\bcancel{\textcolor{red}{-3}}} &= \frac{3}{\textcolor{red}{-3}} && \text{Deler med $-3$ på begge sider}\\
\\
x &= -1
\end{align*}

Altså er løsningen av likningen $x = -1$.
:::
::::

**Din tur!**

::::{admonition} Underveisoppgave 1
---
class: check
---
Løs likningen

$$
x + 2 = 3x - 2.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 2.
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
\begin{align*}
x + 2 &= 3x - 2 \\
\\
x + 2 \textcolor{red}{- 2} &= 3x - 2 \textcolor{red}{- 2} && \text{Trekker fra 2 på begge sider}\\
\\
x &= 3x - 4 \\
\\
x \textcolor{red}{- 3x} &= 3x \textcolor{red}{- 3x} - 4 && \text{Trekker fra $3x$ på begge sider}\\
\\
-2x &= -4 \\
\\
\frac{\bcancel{-2}x}{\bcancel{\textcolor{red}{-2}}} &= \frac{-4}{\textcolor{red}{-2}} && \text{Deler med $-2$ på begge sider}\\
\\
x &= 2
\end{align*}

Altså er løsningen av likningen $x = 2$.
:::

::::

---

## Lineære likninger og lineære funksjoner

I mange tilfeller vil vi bestemme ulike egenskaper ved en lineær funksjon ved hjelp av regning algebraisk. Dette kan blant annet være å bestemme nullpunktet til en lineær funksjon, skjæring med en linje eller skjæring mellom grafene til to funksjoner.

Vi tar et eksempel:

::::{admonition} Eksempel 2
---
class: example
---
En lineær funksjon er gitt ved 

$$
f(x) = 3x + 6.
$$

Bestem hvilket punkt grafen til $f$ skjærer $x$-aksen.

:::{admonition} Løsning
---
class: solution
---
Når grafen til $f$ skjærer $x$-aksen, må $f(x) = 0$. Dermed må vi løse likningen

$$
f(x) = 0 \quad \iff \quad 3x + 6 = 0.
$$

Da finner vi:

\begin{align*}
3x + 6 &= 0 \\
\\
3x + 6 \textcolor{red}{- 6} &= 0 \textcolor{red}{- 6} && \text{Trekker fra 6 på begge sider}\\
\\
3x &= -6 \\
\\
\frac{\bcancel{3}x}{\bcancel{\textcolor{red}{3}}} &= \frac{-6}{\textcolor{red}{3}} && \text{Deler med 3 på begge sider}\\
\\
x &= -2
\end{align*}

Dermed skjærer grafen $x$-aksen i punktet $(-2, 0)$.
:::
::::

---

**Din tur!**

::::{admonition} Underveisoppgave 2
---
class: check
---
En lineær funksjon er gitt ved 

$$
g(x) = -2x + 4.
$$

Bestem $x$-koordinaten til skjæringspunktet mellom grafen til $g$ og linja $y = 2$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 2.
$$

:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Når grafen til $g$ skjærer linja $y = 2$, må $g(x) = 2$. Dermed må vi løse likningen

$$
g(x) = 2 \quad \iff \quad -2x + 4 = 2.
$$

Da finner vi:

\begin{align*}
-2x + 4 &= 2 \\
\\
-2x + 4 \textcolor{red}{- 4} &= 2 \textcolor{red}{- 4} && \text{Trekker fra 4 på begge sider}\\
\\
-2x &= -2 \\
\\
\frac{\bcancel{-2}x}{\bcancel{\textcolor{red}{-2}}} &= \frac{-2}{\textcolor{red}{-2}} && \text{Deler med $-2$ på begge sider}\\
\\
x &= 2
\end{align*}

Dermed skjærer grafen $g$ linja $y = 2$ i punktet $(2, 2)$. Dette har $x$-koordinaten $x = 2$. 
:::
::::

---

Vi kan også bruke lineære likninger som en del av å bestemme funksjonsuttrykket til en lineær funksjon. La oss ta et eksempel:

::::{admonition} Eksempel 3
---
class: example
---
En lineær funksjon $f$ går gjennom punktene $(1, 2)$ og $(3, 6)$. 

Bestem $f(x)$.

:::{admonition} Løsning
---
class: solution
---
En lineær funksjon kan alltid skrives på formen

$$
f(x) = ax + b.
$$

Først bestemmer vi stigningstallet ved topunktsformelen:

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{6 - 2}{3 - 1} = \dfrac{4}{2} = 2.
$$

Det betyr at 

$$
f(x) = 2x + b.
$$

Nå kan vi sette opp en lineær likning der $b$ er den ukjente. Bruker vi punktet $(1, 2)$ vet vi at 

$$
f(1) = 2 \quad \iff \quad 2 = 2 \cdot 1 + b.
$$

Dermed har kan vi bestemme $b$ ved å løse likningen:

\begin{align*}
2 &= 2 \cdot 1 + b \\
\\
2 &= 2 + b \\
\\
2 \textcolor{red}{-2} &= 2 + b \textcolor{red}{-2} && \text{Trekker fra 2 på begge sider}\\
\\
0 &= b
\end{align*}

Dermed er $b = 0$ og funksjonsuttrykket til $f$ er

$$
f(x) = 2x.
$$
:::

::::

---

**Din tur!**

::::{admonition} Underveisoppgave 3
---
class: check
---

En lineær funksjon $g$ går gjennom punktene $(2, 3)$ og $(4, 5)$ på samme måte som i eksempel 3.

Bestem $g(x)$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(x) = x + 1.
$$

:::

:::{admonition} Løsning
---
class: dropdown, solution
---
En lineær funksjon kan alltid skrives på formen

$$
g(x) = ax + b.
$$

Først bestemmer vi stigningstallet ved topunktsformelen:

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{5 - 3}{4 - 2} = \dfrac{2}{2} = 1.
$$

Det betyr at

$$
g(x) = x + b.
$$

Nå kan vi sette opp en lineær likning der $b$ er den ukjente. Bruker vi punktet $(2, 3)$ vet vi at

$$
g(2) = 3 \quad \iff \quad 3 = 2 + b.
$$

Dermed har kan vi bestemme $b$ ved å løse likningen:

\begin{align*}
3 &= 2 + b \\
\\
3 \textcolor{red}{-2} &= 2 + b \textcolor{red}{-2} && \text{Trekker fra 2 på begge sider}\\
\\
1 &= b
\end{align*}

Dermed er $b = 1$ og funksjonsuttrykket til $g$ er

$$
g(x) = x + 1.
$$

:::
::::

