# `for`{l=python}-løkker


:::{admonition} Læringsmål: `for`{l=python}-løkker
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Lese og forstå `for`{l=python}-løkker som bruker `range`{l=python}-funksjonen.
* Skrive grunnleggende `for`{l=python}-løkker som bruker `range`{l=python}-funksjonen til å løse matematiske problemer.

:::


En `for`{l=python}-løkke er noe som brukes til å gjenta en eller flere linjer med kode et bestemt antall ganger som er forhåndsbestemt. For å oppnå dette, brukes ofte `range`{l=python}-funksjonen.


:::::{admonition} Utforsk 1
---
class: explore
---
Her skal du bli kjent med `for`{l=python}-løkker på formen:

```{code-block} python
for i in range(a, b, c):
    ...
```

som ofte brukes når man løser matematiske problemer med Pythonkode.

Under vises et interaktivt kodevindu. Her kan du kjøre kode. 

```{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html
---
```


<br>

````{tab-set}
```{tab-item} Deloppgave 1
Undersøk hva de tre tallene i `range(1, 6, 1)`{l=python} gjør for noe ved å prøve ut forskjellige kombinasjoner av tall. 

Hva er rollen til de tre tallene?

:::{admonition} Hint
---
class: hints, dropdown
---
* Prøv å endre på **ett** tall av gangen!
* Du kan også bruke negative tall.
:::

:::{admonition} Løsning
---
class: solution, dropdown 
---
Vi bruker notasjonen `range(a, b, c)`{l=python} for å gjøre det enklere å beskrive de ulike tallene.
* `a`{l=python} beskriver startverdien til `i`{l=python} i løkka.
* `b`{l=python} beskriver sluttverdien, men er *ikke* inkludert. Vi stopper alltid før sluttverdien. 
* `c`{l=python} er steglengden (avstanden mellom hvert tall). 

Vi kan altså tenke på de det som at vi skriver `range(start, slutt, steglengde)`{l=python}. 
:::
```

```{tab-item} Deloppgave 2
Undersøk hva som skjer hvis du bare bruker **ett** tall som `range(6)`{l=python}. 

Hva er sammenhengen med når du bruker tre tall?

:::{admonition} Løsning
---
class: solution, dropdown
---
Hvis du bare bruker ett tall, som `range(6)`{l=python}, så vil startverdien være 0 og steglengden være 1. Det er det samme som å skrive `range(0, 6, 1)`{l=python}. 

Mer generelt kan vi tolke det som at vi skriver `range(slutt)`{l=python}. Da vil vi automatisk ha startverdien 0 og steglengden 1.
:::

```


```{tab-item} Deloppgave 3
Undersøk hva som skjer hvis du bruker **to** tall som `range(1, 6)`{l=python}. 

Hva er sammenhengen når du bruker tre tall?

:::{admonition} Løsning
---
class: solution, dropdown
---
Hvis vi bruker to tall, som `range(1, 6)`{l=python}, så vil startverdien være 1 og steglengden være 1. Det er det samme som å skrive `range(1, 6, 1)`{l=python}.

Mer generelt kan vi skrive `range(start, slutt)`{l=python}. Da vil vi automatisk ha steglengden 1.
:::
```

```{tab-item} Deloppgave 4
Endre på `for`{l=python}-løkka slik at du skriver ut de 10 første naturlige tallene.


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må endre stoppverdien til `11`{l=python} for å få med tallet 10. 

:::{code-block} python
---
linenos: true
emphasize-lines: 1
---
for i in range(1, 11, 1):
    print(i)
:::

Fra deloppgave 2, lærte vi også at vi ikke trenger å ta med steglengden når den er 1. Derfor kan vi skrive `range(1, 11)`{l=python} i stedet.
::::

```

```{tab-item} Deloppgave 5
Endre på `for`{l=python}-løkka slik at du skriver ut de 10 første naturlige tallene i synkende rekkefølge.

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må sette følgende verdier:
* Startverdi: 10
* Stoppverdi: 0 (husk at vi aldri får med det siste tallet)
* Steglengde: -1

:::{code-block} python
---
linenos: true
emphasize-lines: 1
---
for i in range(10, 0, -1):
    print(i)
:::
::::
```

````

:::::

---

::::{admonition} Underveisoppgave 1
---
class: check, full-width
---

Under vises noen `for`{l=python}-løkker og noen følger med tall. <br> Pusle sammen riktig løkke med riktig tallfølge.
:::{raw} html
---
file: ./pair_puzzles/underveisoppgave_1.html
---
:::

::::


---

Nå har du fått litt oversikt over hvordan en enkel `for`{l=python}-løkke fungerer. Nå skal du se på noen matematiske problemer du kan løse ved hjelp av `for`{l=python}-løkker.


:::::{admonition} Utforsk 2
---
class: explore
---
Under vises et program som regner ut summen av de 5 første naturlige tallene.


```{raw} html
---
file: interaktiv_kode/utforsk/utforsk_2.html
---
```

<br>

Deloppgave 1
: Kan du endre programmet slik at det regner ut summen av de 10 første naturlige tallene?


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi endrer stoppverdien til `11`{l=python} for å få med tallet 10. 

```{code-block} python
---
linenos: true
emphasize-lines: 2
---
s = 0 
for i in range(1, 11):
    s = s + i

print(f"{s = }")
```
::::

<br>

Deloppgave 2
: Endre programmet slik at det regner ut summen av de 100 første naturlige tallene. (Det kan lurt å ta bort `print`{l=python}-setningen i `for`{l=python}-løkka for å unngå for mye utskrift.)


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi endrer stoppverdien til `101`{l=python} for å få med tallet 100. 

```{code-block} python
---
linenos: true
emphasize-lines: 2
---
s = 0
for i in range(1, 101):
    s = s + i

print(f"Summen ble: {s = }")
```

::::

<br>

Deloppgave 3
: Endre programmet slik at det regner ut summen av de 100 første kvadrattallene. 

:::{admonition} Hint: Kvadrattall?
---
class: hints, dropdown
---
Et kvadrattall er et tall på formen $n^2$ for et naturlig tall $n$. 
:::


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi må endre på formelen som oppdaterer verdien til `s`{l=python} slik at vi legger til et kvadrattall `i**2`{l=python} i stedet for et naturlig tall `i` (linje 3).

```{code-block} python
---
linenos: true
emphasize-lines: 3
---
s = 0
for i in range(1, 101):
    s = s + i**2

print(f"Summen ble: {s = }")
```
::::


<br>

Deloppgave 4
: Et partall kan skrives på formen $2i$ for et naturlig tall $i \in \mathbb{N}$. Endre programmet slik at det regner ut summen av de 100 første partallene 


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi endrer på formelen som oppdaterer verdien til `s`{l=python} slik at vi legger til et partall `2*i`{l=python} i stedet for et naturlig tall `i` (linje 3).

```{code-block} python
---
linenos: true
emphasize-lines: 3
---
s = 0
for i in range(1, 101):
    s = s + 2*i

print(f"Summen ble: {s = }")
```
::::


:::::


---

## Oppgaver 

:::::{admonition} Oppgave 1
---
class: problem-level-1
---
Et tall $x$ er et kvadrattall hvis det kan skrives på formen $x = n^2$ der $n \in \mathbb{N}$. <br> 
Under vises et program i tilfeldig rekkefølge som regner ut summen av noen kvadrattall. 

Deloppgave 1
: Plasser kodelinjene i riktig rekkefølge for å få tilgang til det ferdig programmet. <br> Kan du forutsi hva programmet skriver ut? Kjør programmet og sjekk! 

<br>

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_1.html
---
:::

<br>

Delopppgave 2
: Endre programmet slik at det regner ut summen av de 10 første kvadrattallene. <br> Stemmer svaret du får ved å kjøre programmet?


Deloppgave 3
: Endre programmet til å regne ut summen av de 100 første kubikktallene. <br> Hva blir summen?


:::::






:::::{admonition} Oppgave 2
---
class: problem-level-2
---

En matematisk størrelse som dukker opp i mange sammenhenger er $n$-fakultet, som vi skiver som $n!$ - vi har definert $n!$ som produktet av alle heltall fra $1$ til $n$:

$$
n! = 1 \cdot 2 \cdot \ldots \cdot (n - 1) \cdot n.
$$

For eksempel er 

$$
4! = 1 \cdot 2 \cdot 3 \cdot 4 = 24.
$$


Deloppgave 1
: Under vises et program som regner ut $4!$ der kodelinjene er plassert i tilfeldig rekkefølge. <br> Plasser kodelinjene i riktig rekkefølge for å få tilgang til det ferdige programmet. <br> Lim inn programmet i det interaktivt kodevinduet og kjør det.  <br> Blir svaret riktig?

<br>

:::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_2.html
---
:::

<br>

Deloppgave 2
: Endre programmet slik at det regner ut $7!$. <br> Hva blir svaret? svaret ved regning.


<br>

Deloppgave 3
: Dobbeltfakultet $n!!$ er definert som at du tar produktet av annenhvert tall. Hvis tallet $n$ er et oddetall, starter du på $1$. Hvis $n$ er et partall, starter du på $2$. For eksempel er

    $$
    5!! = 1 \cdot 3 \cdot 5 = 15  \quad \text{og} \quad 6!! = 2 \cdot 4 \cdot 6 = 48.
    $$

    Endre programmet slik at det regner ut $6!!$ <br> Stemmer svaret overens med svaret over?
:::::

---

:::{admonition} Oppgave 3
---
class: problem-level-3
---
I denne oppgaven skal du jobbe med summer av oddetall:

\begin{align*}
    S_1 &= 1, \\
    S_2 &= 1 + 3, \\
    S_3 &= 1 + 3 + 5, \\
    S_4 &= 1 + 3 + 5 + 7, \\
    S_5 &= 1 + 3 + 5 + 7 + 9, \\
\end{align*}

og så videre. Vi lar $S_N$ være summen av de $N$ første oddetallene.

<br>

Deloppgave 1
: La $a_n$ være det $n$-te leddet i summen. Finn en formel for $a_n$. 

<br>

Under vises et interaktivt kodevindu med en uferdig kode. 

Deloppgave 2
: Fullfør programmet slik at det regner ut $S_5$. <br> Sjekk at svaret stemmer for hånd.

<br>

::::{raw} html
---
file: ./interaktiv_kode/oppgaver/oppgave_5.html
---
::::

<br>

:::