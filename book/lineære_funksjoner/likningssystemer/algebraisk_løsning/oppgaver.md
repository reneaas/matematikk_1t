# Oppgaver: <br> Algebraisk løsning av lineære likningssystemer

:::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Løs likningssystemene ved å bruke addisjonsmetoden. Sett deretter prøve på svaret. 

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
\begin{align*}
x + y &= 0\\
\\
x - y &= 2
\end{align*}

`````{admonition} Fasit
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 1 \quad \land \quad y = -1.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(1, -1\right)\right\}
$$
```
````
`````
:::::

:::::{tab-item} b
\begin{align*}
2x - 3y &= 4\\
\\
-x + y &= 1
\end{align*}

`````{admonition} Fasit
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = -7 \quad \land \quad y = -6.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(-7, -6\right)\right\}
$$
```
````
`````
:::::

:::::{tab-item} c
\begin{align*}
x - y &= -2\\
\\
x + 2y &= 1
\end{align*}

`````{admonition} Fasit
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = -1 \quad \land \quad y = 1.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(-1, 1\right)\right\}
$$
```
````
`````
:::::

::::::

:::::::

:::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Løs likningssystemene ved å bruke innsettingsmetoden. Sett deretter prøve på svaret. 

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
\begin{align*}
2x - 4y &= -1\\
\\
3x + 5y &= 4
\end{align*}

`````{admonition} Fasit
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = \frac{1}{2} \quad \land \quad y = \frac{1}{2}.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(\frac{1}{2}, \frac{1}{2}\right)\right\}
$$
```
````
`````
:::::

:::::{tab-item} b
\begin{align*}
-x +5 &= y\\
\\
x &= y - 3
\end{align*}

`````{admonition} Fasit
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 1 \quad \land \quad y = 4.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(1, 4\right)\right\}
$$
```
````
`````
:::::

:::::{tab-item} c
\begin{align*}
7x + 4y &= 74\\
\\
5x + 8y &= 76
\end{align*}

`````{admonition} Fasit
---
class: dropdown, answer
---
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 8 \quad \land \quad y = \frac{9}{2}.
$$
```

```{tab-item} Løsningsmengde
$$
(x, y) \in \left\{\left(8, \frac{9}{2}\right)\right\}
$$
```
````
`````
:::::
::::::

:::::::

---

::::::{admonition} Oppgave 3
---
class: problem-level-1
---
En lineær funksjon $f$ oppfyller likningene 

$$
\begin{align*}
f(2) &= 3 \\
\\
f(5) &= -3
\end{align*}
$$

:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} a
Sett opp et likningssystem for koeffisientene $a$ og $b$ til den lineære funksjonen.

:::{admonition} Fasit
---
class: answer, dropdown
---
\begin{align*}
2a + b &= 3 \\
\\
5a + b &= -3
\end{align*}
:::
::::

::::{tab-item} b
Bestem $f(x)$ ved å løse likningssystemet.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -2x + 7
$$
:::
::::
::::::

---

::::::{admonition} Oppgave 4
---
class: problem-level-2
---
En lineær funksjon $f$ oppfyller likningene

\begin{align*}
f(1) &= 3 \\
\\
f(4) &= 6
\end{align*}

Bestem $f(x)$ ved hjelp av et likningssystem.

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = x + 2
$$
::::
::::::

---

::::{admonition} Oppgave 5
---
class: problem-level-2
---

I fotball får et lag tre poeng for seier og ett poeng for uavgjort. I fjor vant laget til Siri fire flere kamper enn de spilte uavgjort. Laget fikk til sammen 36 poeng. Hvor mange kamper vant laget til Siri?

:::{admonition} Fasit
---
class: answer, dropdown
---
Laget vant $10$ kamper og spilte $6$ kamper uavgjort. 
:::

:::{admonition} Løsningsforslag
---
class: solution, dropdown
---

Vi starter med å sette opp likninger. Vi har to ukjente, antall kamper laget vant ($v$) og antall kamper laget spilte uavgjort ($u$). Ut fra teksten vet vi følgende: 

1) Laget vant $4$ flere kamper enn de spilte uavgjort.  
Det kan vi uttrykke som 

$$v = u + 4$$

2) Laget fikk $36$ poeng totalt, og de får $3$ poeng når de vinner og $1$ poeng for uavgjort. 
Det kan vi uttrykke som

$$3v + u = 36$$

Da har vi to likninger. Disse kan vi løse ved å bruke enten innsettingsmetoden eller addisjonsmetoden. Her velger jeg innsettingsmetoden. Jeg starter ved å skrive om den første likningen til:

$$u = v - 4$$

Deretter setter jeg inn for $u$ i den andre likningen og regner ut: 

\begin{align*}
3v + (v - 4) &= 36 \\
\\
3v + v - 4 &= 36 \\
\\
4v &= 36 + 4 \\
\\
4v &= 40 \\
\\
v &= 10 \\
\end{align*}

Vi setter deretter løsningen inn i likningen for $u$ og får

$$u = v - 4 = 10 - 4 = 6$$

Vi ser da at vi får løsningen 

$$
v = 10 \, \land \, u = 6.
$$ 

Altså har laget vunnet $10$ kamper og spilt $6$ kamper uavgjort. 
:::
::::

---

::::::::{admonition} Oppgave 6
---
class: problem-level-2
---

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Alex og Bella er med i samme idrettslag. Sammen med treneren har de en total alder på 54 år. Bella er dobbelt så gammel som Alex, og treneren er tre ganger så gammel som Bella. Finn ut hvor gamle Alex, Bella og treneren er. 

Bestem hvor gamle Alex, Bella og treneren er.

:::{admonition} Fasit
---
class: answer, dropdown
---
Alex er 6 år, Bella er 12 år, treneren er 36 år. 
:::
:::::

:::::{tab-item} b
I en liten landsby bor det tre generasjoner: en mor, hennes sønn Kåre, og bestefaren. Moren er tre ganger så gammel som Kåre, og bestefaren er dobbel så gammel som moren. Sammen har de en total alder på 120 år. Finn ut hvor gamle Kåre, moren, og bestefaren er.

Bestem hvor gamle Kåre, moren og bestefaren er.
:::{admonition} Fasit
---
class: answer, dropdown
---
Kåre er 12 år, mor er 36 år og bestefar er 72 år.
:::
:::::


:::::{tab-item} c
I en by bor en tante og hennes nevø. Tanten var 22 år da nevøen ble født. I dag er hun dobbelt så gammel som nevøen. Finn ut hvor gamle tanten og nevøen er.

Bestem hvor gammel tanten og nevøen er.
:::{admonition} Fasit
---
class: answer, dropdown
---
Nevøen er 22, tante er 44.
:::
:::::


:::::{tab-item} d
Sara, og hennes far og onkel Lars er i selskap. Faren er tre ganger så gammel som Sara, og han er seks år eldre enn onkel Lars. Sammen har de tre en total alder på 92 år. 

Bestem hvor gammel Sara, faren og onkel Lars er.

:::{admonition} Fasit
---
class: answer, dropdown
---
Sara er 14 år, far er 42 år, onkel Lars er 36 år.
:::
:::::

:::::{tab-item} e

Mor er 21 år eldre enn datter. Bestefar er tre ganger så gammel som mor. Om to år vil deres totale alder være 100 år. 

Bestem hvor gammel datter, mor og bestefar er.

:::{admonition} Fasit
---
class: answer, dropdown
---
Datter er 2 år, mor er 23 år, bestefar er 69 år. 
:::

:::::
::::::::

---

::::::{admonition} Oppgave 7
---
class: problem-level-3
---
La $f(x) = ax + b$ og $g(x) = cx + d$ være to lineære funksjoner som oppfyller likningene

\begin{align*}
f(2) - g(-2) &= 0 & \dfrac{f(2) - f(0)}{2} &= 2(g(1) - g(0)) \\
\\
f(0) + g(0) &= 0 & f(-2) + g(2) &= 4 \\
\\
\end{align*}

:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} a
Sett opp et likningssystem for koeffisientene til $f$ og $g$.


:::{admonition} Fasit
---
class: answer, dropdown
---
\begin{align*}
    2a + b &= -2c + d \\
    \\
    b + r &= 0 \\
    \\
    a &= 2c \\
    \\
    -2a + b + 2c + d &= 4
\end{align*}
:::
::::

::::{tab-item} b
Bestem $f(x)$ og $g(x)$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = -4x + 6 \quad \text{og} \quad g(x) = -2x - 6
$$
:::
::::

::::::
