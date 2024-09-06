# Oppgaver: <br> Algebraisk løsning av lineære likningssystemer

::::{admonition} Oppgave 1
---
class: problem-level-1
---
Løs likningssystemene ved å bruke addisjonsmetoden. Sett deretter prøve på svaret. 

Deloppgave 1
: \begin{align}
x + y &= 0\\
x - y &= 2
\end{align}

`````{admonition} Fasit
:class: dropdown, answer
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
<br>

Deloppgave 2
: \begin{align}
2x - 3y &= 4\\
-x + y &= 1
\end{align}

`````{admonition} Fasit
:class: dropdown, answer
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
<br>

Deloppgave 3
: \begin{align}
x - y &= -2\\
x + 2y &= 1
\end{align}

`````{admonition} Fasit
:class: dropdown, answer
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
::::

::::{admonition} Oppgave 2
---
class: problem-level-1
---
Løs likningssystemene ved å bruke innsettingsmetoden. Sett deretter prøve på svaret. 

Deloppgave 1
: \begin{align}
2x - 4y &= -1\\
3x + 5y &= 4
\end{align}

`````{admonition} Fasit
:class: dropdown, answer
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
<br>

Deloppgave 2
: \begin{align}
-x +5 &= y\\
x &= y - 3
\end{align}

`````{admonition} Fasit
:class: dropdown, answer
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
<br>

Deloppgave 3
: \begin{align}
7x + 4y &= 74\\
5x + 8y &= 76
\end{align}

`````{admonition} Fasit
:class: dropdown, answer
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
::::

::::{admonition} Oppgave 3
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

2) Laget finn $36$ poeng totalt, og de får $3$ poeng når de vinner og $1$ poeng for uavhgjort. 
Det kan vi uttrykke som
$$3v + u = 36$$

Da har vi to likninger. Disse kan vi løse ved å bruke enten innsettingsmetoden eller addisjonsmetoden. Her velger jeg innsettningsmetoden. Jeg starter ved å skrive om den første likningen til:
$$u = v - 4$$
Deretter setter jeg inn for $u$ i den andre likningen og regner ut: 
\begin{align}
3v + (v - 4) &= 36 \\
3v + v - 4 &= 36 \\
4v &= 36 + 4 \\
4v &= 40 \\
v &= 10 \\

Vi setter deretter løsningen inn i likningen for $u$ og får
$$u = v - 4 = 10 - 4 = 6$$

Vi ser da at vi får løsningen $v = 10 \vee u = 6$. Altså har laget vunnet $10$ kamper og spilt $6$ kamper uavgjort. 
:::
::::

::::{admonition} Oppgave 4 **Flyttes til etter CAS**
---
class: problem-level-3
---
På en fotballkamp er det tre kategorier billetter: barn, voksne og pensjonister. 

Publikumstallet på kampen var 2100. Barnebilletten kostet 50 kr, voksenbilletten 200 kr og pensjonistbilletten 100 kr. Billettinntektene ble på 315 000 kr. Det var dobbelt så mange pensjonister som barn på kampen. 

Bestem antallet barn, voksne og pensjonister på kampen.

:::{admonition} Fasit
---
class: answer, dropdown
---
Det var 300 barn, 600 pensjonister og 1200 voksne på kampen. 
:::
:::{admonition} Løsningsforslag
---
class: solution, dropdown
---
Vi starter med å sette opp likninger. Vi har tre ukjente, som vi kaller $b$ (barn), $v$ (voksne) og $p$ (pensjonister). Ut fra teksten vet vi følgende: 

1) Det totale billettantallet er $2100$. 
Det kan vi uttrykke som 
$$b + v + p = 2100$$

2) De totale billettinntektene er $315 000$ kr, og det koster $50$ kr for en barnebillett, $200$ kr for en voksenbillett og $100$ kr for en pensjonistbillett. Det kan vi uttrykke som
$$50 b + 200 v + 100 p = 315 000$$

3) Sist, men ikke minst vet vi at det er dobbelt så mange pensjonister som voksne. Det kan vi uttrykke som 
$$ 2b = p$$

Da har vi tre likninger. Disse kan vi løse for hånd, men i dette tilfellet vil det være enklere å bruke CAS. Vi får da at det var 300 barn, 600 pensjonister og 1200 voksne på kampen. 

:::
::::