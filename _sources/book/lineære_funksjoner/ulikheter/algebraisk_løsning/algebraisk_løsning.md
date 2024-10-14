# Algebraisk løsning

:::{admonition} Læringsmål: algebraisk løsning av lineære ulikheter
---
class: tip
---
Etter dette delkapittelet, er målet at du skal:
* Løse lineære ulikheter algebraisk.
* Kunne tegne og tolke en fortegnslinje for en lineær funksjon.
:::

---

## Løsning ved regning

Når vi jobber med lineære ulikheter, kan vi i stor grad bruke de samme metodene som vi bruker for å løse lineære likninger. Vi kan 
* legge til og trekke fra et tall på begge sider av ulikheten
* gange og dele med et tall på begge sider av ulikheten


:::::{admonition} Snu ulikhetstegnet når vi ganger med et negativt tall
---
class: sidenote, margin
---
Å snu ulikhetstegnet når vi ganger med et negativt tall har en logisk årsak. Tenk deg at vi ser på en ulikhet som ser sann, for eksempel

$$
3 < 5
$$

Hvis vi nå *bare* ganger med $-1$ på begge sider, får vi

$$
-3 < -5
$$

Men dette er ikke lenger en sann påstand. Snur vi derimot ulikhetstegnet, får vi en sann påstand

$$
-3 > -5
$$

Sånn kan vi forstå hvorfor vi snur ulikhetstegnet når vi ganger med et negativt tall.
:::::

::::::{admonition} Eksempel 1
---
class: example
---
Løs ulikheten

$$
2x + 3 < 3x - 4
$$

algebraisk. 

:::::{admonition} Løsning
---
class: solution
---
\begin{align*}
2x + 3 &< 3x - 4 \\
\\
2x \textcolor{red}{ - 3x} + 3 \textcolor{red}{ - 2x} &< 3x \textcolor{red}{ - 3x} - 4 && \text{Trekk fra $3x$ på hver side} \\
\\
-x + 3 &< -4 \\
\\
-x + 3 \textcolor{red}{- 3} &< -4 \textcolor{red}{- 3} && \text{Trekk fra $3$ på hver side} \\
\\
-x &< -7 \\
\\
-x \textcolor{red}{\cdot (-1)} &> -7 \textcolor{red}{\cdot (-1)} && \text{Ganger med $(-1)$ og snur ulikhetstegnet} \\
\\
x &> 7
\end{align*}


Løsningen kan derfor uttrykkes som

`````{tab-set}
````{tab-item} Ulikhet
$$
x > 7
$$
````

````{tab-item} Løsningsmengde
$$
x \in \langle 7, \to \rangle
$$
````

`````

:::::

::::::



::::::{admonition} Underveisoppgave 1
---
class: check
---
Løs ulikheten

$$
5x - 3 \geq -2x + 4
$$

algebraisk. 

:::::{admonition} Fasit
---
class: answer, dropdown
---
::::{tab-set}
:::{tab-item} Ulikhet
$$
x \geq 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left [1, \to \right \rangle
$$
:::
::::
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
5x - 3 &\geq -2x + 4 \\
\\
5x \textcolor{red}{ + 2x} - 3 \textcolor{red}{ + 3} &\geq -2x \textcolor{red}{ + 2x} + 4 && \text{Legger til $2x$ på hver side} \\
\\
7x - 3 &\geq 4 \\
\\
7x - 3 \textcolor{red}{ + 3} &\geq 4 \textcolor{red}{ + 3} && \text{Legger til $3$ på hver side} \\
\\
7x &\geq 7 \\
\\
\dfrac{\cancel{7}x}{\cancel{\textcolor{red}{7}}} &\geq \dfrac{7}{\textcolor{red}{7}} && \text{Deler med $7$ på hver side} \\
\\
x &\geq 1
\end{align*}

Vi kan oppgi løsningen enten som en ulikhet eller som en løsningsmengde

::::{tab-set}
:::{tab-item} Ulikhet
$$
x \geq 1
$$
:::

:::{tab-item} Løsningsmengde
$$
x \in \left [1, \to \right \rangle
$$
:::
::::
:::::
::::::


---

## Løsning med fortegnslinjer

::::{admonition} Må det være farger?
---
class: sidenote, margin
---
Merk at fortegnslinjene ikke må ha farger, men da er det om linja er heltrukken eller stiplet som er angir fortegnet:

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
* Vi bruker $0$ for å representere nullpunktet til funksjonen.


I {numref}`fig-lineære-funksjoner-ulikheter-algebraisk-løsning-teori-1` vises grafen til en lineær funksjon med $x_1$ som nullpunkt.

:::{figure} ./figurer/teori/graf.svg
---
name: fig-lineære-funksjoner-ulikheter-algebraisk-løsning-teori-1
width: 80%
---
viser grafen til en lineær funksjon $f$ med ett nullpunkt i $x_1$. 
:::

Fortegnslinjen til $f$ vil da være som vist i {numref}`fig-lineære-funksjoner-ulikheter-algebraisk-løsning-teori-2`.

:::{figure} ./figurer/teori/fortegnslinjer.svg
---
name: fig-lineære-funksjoner-ulikheter-algebraisk-løsning-teori-2
width: 100%
---
viser fortegnslinjen til $f$. De røde **heltrukne** linjene svarer til positivt fortegn. De blå **stiplede** linjene svarer til negativt fortegn.
:::

::::

---

::::{admonition} Eksempel 2
---
class: example
---
Her viser vi tre lineære funksjoner og deres tilhørende fortegnslinje. 

`````{tab-set}
````{tab-item} $f(x) = 2x - 4$

:::{figure} ./figurer/eksempler/eksempel_2/f_graf.svg
---
width: 80%
---
:::

---

:::{figure} ./figurer/eksempler/eksempel_2/f_fortegnslinje.svg
---
width: 100%
---
:::

````

````{tab-item} $g(x) = -3x + 6$

:::{figure} ./figurer/eksempler/eksempel_2/g_graf.svg
---
width: 80%
---
:::

---

:::{figure} ./figurer/eksempler/eksempel_2/g_fortegnslinje.svg
---
width: 100%
---
:::

````

````{tab-item} $h(x) = \dfrac{1}{3}x + 1$

:::{figure} ./figurer/eksempler/eksempel_2/h_graf.svg
---
width: 80%
---
:::

---

:::{figure} ./figurer/eksempler/eksempel_2/h_fortegnslinje.svg
---
width: 100%
---
:::

````
`````
::::

---

Men hvordan bruker vi fortegnslinjer til å løse ulikheter? La oss se på et eksempel.

:::::{admonition} Eksempel 3
---
class: example
---
En ulikhet er gitt ved

$$
3x + 5 \geq 2x - 1
$$

Løs ulikheten ved å bruke fortegnslinjer.

::::{admonition} Løsning
---
class: answer
---
Først skriver vi om ulikheten slik at høyre side er lik null:

\begin{align*}
-2x + 5 &\geq 2x - 7 \\
\\
-2x + 5 \textcolor{red}{- 2x + 7} &\geq 2x - 7 \textcolor{red}{- 2x + 7}\\
\\
\underbrace{-4x + 12}_{\displaystyle f(x)} &\geq 0
\end{align*}

Deretter faktoriserer vi den lineære funksjonen på venstre side:

$$
f(x) = -4x + 12 = -4(x - 3)
$$

Så tegner vi en fortegnslinje for *alle* faktorene i den lineære funksjonen. For å få den samlede fortegnslinjen til $f(x)$, ganger vi sammen fortegnene til hver faktor. Vi kaller figuren vi får under for **fortegnsskjemaet** til $f$.

:::{figure} ./figurer/eksempler/eksempel_3/fortegnslinje.svg
---
name: fig-lineære-funksjoner-ulikheter-algebraisk-løsning-eksempel-3
width: 100%
---
viser fortegnslinjene til $-2$, $x - 3$, og til $f(x) = -4(x - 3)$. For å få fortegnlinja til $f(x)$, ganger vi sammen fortegnene til hver faktor. Dette gir oss fortegnsskjemaet til $f$.
:::

Fra {numref}`fig-lineære-funksjoner-ulikheter-algebraisk-løsning-eksempel-3` kan vi se at $f(x) \geq 0$ når $x \leq 3$. Dermed er løsningen av den opprinnelige ulikheten

$$
-2x + 5 \geq 2x - 7 \quad \iff \quad x \leq 3 \quad \iff \quad x \in \left \langle \gets, 3 \right \rangle
$$

::::


:::::

---


:::::{admonition} Underveisoppgave 2
---
class: check
---

En ulikhet er gitt ved

$$
-2x + 8 < 0
$$

````{tab-set}
---
class: tabs-parts
---
```{tab-item} a

Tegn et fortegnsskjema for ulikheten.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
width: 100%
---
:::
::::

---

::::{admonition} Løsning
---
class: dropdown, solution
---
La oss kalle venstre side av ulikheten for $f(x) = -2x + 8$. Vi kan faktorisere $f(x)$ slik:

$$
f(x) = -2x + 8 = -2(x - 4)
$$

Så tegner vi fortegnsskjema som følger:
1. Tegn en fortegnslinje for hver faktor i $f(x)$ – en for $-2$ og en for $x - 4$.
2. Gang sammen fortegnene til hver faktor for å få fortegnslinja til $f(x)$.

Dette gir fortegnsskjemaet:

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
width: 100%
---
:::

::::

```

```{tab-item} b

Bruk fortegnsskjema til å bestemme løsningsmengden til ulikheten. 

::::{admonition} Fasit
---
class: dropdown, answer
---

$$
x \in \langle 4, \to \rangle
$$

::::

```

````
:::::


