# Oppgaver: <br> Grafisk løsning av lineære likninger

````{admonition} Oppgave 1
---
class: problem-level-1
---
I {numref}`lineære-likninger-grafisk-løsning-oppg-1` er grafen til $f(x) = x + 3$ tegnet inn. 

```{figure} ./figurer/oppgaver/oppg_1.svg
---
name: lineære-likninger-grafisk-løsning-oppg-1
width: 80%
---

Grafen til $f(x) = x + 3$.
```

Bruk grafen til å løse likningene under.

Oppgave 1a
: $$x + 3 = 0$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -3
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Grafen skjærer $x$-aksen i $x = -3$, som betyr at løsningen av likningen er $x = -3$.
:::


<br>

Oppgave 1b
: $$x + 3 = 4$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 1
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Grafen skjærer linja $y = 4$ i $(x, y) = (1, 4)$, som betyr at løsningen av likningen er $x = 1$.
:::


<br>

Oppgave 1c
: $$x + 3 = -2$$

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -5
$$
:::

:::{admonition} Løsning
---
class: dropdown, solution
---
Grafen skjærer linja $y = -2$ i $(x, y) = (-5, -2)$, som betyr at løsningen av likningen er $x = -2$.
:::
````


::::{admonition} Oppgave 2
:class: problem-level-1
Under vises en interaktiv graf av funksjonen $f(x) = 2x + 1$ og en linje $y = k$. Du kan endre på verdien av $k$.

```{raw} html
---
file: ./figurer/interaktive_plot/lineær_likning_2x+1=k.html
---
```

Oppgave 2a
: Bestem hvilken verdi av $k$ som gir løsningen $x = -2$. 

:::{admonition} Fasit: 2a
---
class: answer, dropdown
---
$k = -3$. 
:::

:::{admonition} Løsning: 2a
---
class: solution, dropdown
---
Justerer vi linja $y = k$ til $y = -3$, så skjærer grafen til $f$ linja i $(x, y) = (-2, -3)$. Dermed gir $k = -3$ løsningen $x = -2$. 
:::


<br>

Oppgave 2b
: Bruk grafen til å forklare hvorfor likningen $2x + 1 = k$ har en løsning for alle $k \in \mathbb{R}$.


::::



:::::{admonition} Oppgave 3
---
class: problem-level-1
---
I figur {numref}`lineære-likninger-grafisk-løsning-oppg-3` er grafene til to lineære funksjoner $f$ og $g$ tegnet inn. 

:::{figure} ./figurer/oppgaver/oppg_3.svg
---
name: lineære-likninger-grafisk-løsning-oppg-3
---
Grafene til to lineære funksjoner $f$ og $g$.

:::

Oppgave 3a
: Bestem likningen som svarer til skjæringen mellom grafene til $f$ og $g$. 

::::{admonition} Fasit: 3a
---
class: answer, dropdown
---
$$
x - 2 = -2x - 5.
$$
::::

<br>

Oppgave 3b
: Løs likningen fra oppgave 3a ved hjelp av figuren.



::::{admonition} Fasit: 3b
---
class: answer, dropdown
---
$$
x = -1.
$$
::::
:::::



::::::{admonition} Oppgave 4
---
class: problem-level-2
---

I {numref}`lineære-likninger-grafisk-løsning-oppg-4` vises grafene til to lineære funksjoner. 
Bruk figuren til å lage
* En likning på formen $ax + b = 0$
* En likning på formen $ax + b = k$
* En likning på formen $ax + b = cx + d$

Løs likningene ved hjelp av figuren.

```{figure} ./figurer/oppgaver/oppg_4.svg
---
name: lineære-likninger-grafisk-løsning-oppg-4
width: 80%
---

Grafene til to lineære funksjoner.
``` 

:::{admonition} Hint
---
class: hints, dropdown
---
For å lage likningene, må du bestemme funksjonsuttrykkene til de to lineære funksjonene ut ifra grafene.
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
Det finnes flere muligheter enn de som er listet her.

Likning 1
: $$-x + 3 = 0 \quad \Leftrightarrow \quad x = 3$$

Likning 2
: $$3x - 1 = 5 \quad \Leftrightarrow \quad x = 2 $$

Likning 2
: $$-x + 3 = 3x - 1 \quad \Leftrightarrow \quad x = 1$$
::::

:::::{admonition} Løsning
---
class: solution, dropdown
---

Vi må bestemme funksjonsuttrykkene til de to grafene først. Vi lar den grønne grafen væren $f$ og den lilla være $g$. 
Vi bruker tabellen under til å bestemme funksjonsuttrykkene

| Funksjon | $(x_1, y_1)$ | $(x_2, y_2)$ | $\Delta x$ | $\Delta y$ | $a = \dfrac{\Delta y}{\Delta x}$ | $b$ | 
|:--------:|:------------:|:------------:|:----------:|:----------:|:--------------------------------:|:---:|
| $f$      | $(0, 3)$     | $(1, 2)$     | $1$        | $-1$       | $-1$                             | $3$ |
| $g$      | $(0, -1)$    | $(1, 2)$     | $1$        | $3$        | $3$                              | $-1$|

<br>

Dermed er funksjonsuttrykkene til $f$ og $g$ gitt ved

$$
f(x) = -x + 3 \quad \text{og} \quad g(x) = 3x - 1.
$$


Nå kan vi lage tre likninger.

Likning 1
: $$-x + 3 = 0$$
: Likningen svarer til $x$-verdien til der grafen til $g$ skjærer $x$-aksen. Grafen skjærer $x$-aksen i $(x, y) = (3, 0)$, så løsningen av likningen er $x = 3$.

Likning 2
: $$3x - 1 = 5$$
: Likningen svarer $x$-verdien til skjæringen mellom grafen til $f$ og linja $y = 5$. Skjæringen skjer i $(x, y) = (2, 5)$, så løsningen av likningen er $x = 2$.

Likning 2
: $$-x + 3 = 3x - 1$$
: Likningen svarer til $x$-verdien til skjæringen mellom grafene til $f$ og $g$. De skjærer hverandre i $(x, y) = (1, 2)$, så løsningen av likningen er $x = 1$.
:::::

::::::




