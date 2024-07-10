# Grafisk løsning 

På samme måte som vi løste likninger, kan vi også løse likningssystemer grafisk. 


```{admonition} Læringsmål: grafisk løsning av lineære likningssystemer
:class: tip
Etter å ha lest dette delkapittelet, er målet at du skal kunne:
* Løse lineære likningssystemer grafisk.
* Kunne uttrykke løsningen av et lineært likningssystem som et likningssystem eller som en løsningsmengde.
```


Vi starter med å se på et eksempel:

`````{admonition} Eksempel 1
:class: example

$$
\begin{align}
    x - y & = -1 \\
    x + y & = 1 \\
\end{align}
$$ (eq:eksempel-1)


Vi ser at vi har to likninger med to ulike variabler, $x$ og $y$. For å løse likningssystemet grafisk tegner vi hver likning. Det er enklest å se hvis vi først skriver om hver likning slik at vi har $y$ på *venstre side* og alt annet på *høyre side*. 

\begin{align}
    - y & = -1 - x \\
    y & = 1 - 1 \\
\end{align}

Vi multipliserer hele den første likningen med $(-1)$ slik at det ser litt penere ut: 

\begin{align}
    y & = 1 + x \\
    y & = 1 - 1 \\
\end{align}

Vi kan nå tegne de to likningene grafisk, slik vi ha gjort før. 

```{figure} ./figurer/eksempler/eksempel1.svg
:name: eksempel1
:width: 80%

Grafene til de lineære funksjonene $f(x) = 1 + x$ og $g(x) = 1 - x$. Skjæringspunktet mellom de to grafene svarer til løsningen av likningssystemet i {eq}`eq:eksempel-1`. 
```

Løsningen av likningssystemet svarer til koordinatene til skjæringspunktet mellom de to lineære funksjonene. Vi kan lese av at dette er $(x, y) = (0, 1)$. Da kan vi uttrykke løsningen av likningssystemet enten som et likningssystem eller som en løsningsmengde:

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 0 \quad \land \quad y = 1.
$$
```

```{tab-item} Løsning som løsningsmengde 
$$
(x, y) \in \{(0, 1)\}.
$$
```
````

`````

``````{admonition} Underveisoppgave 1
:class: check

Bruk figuren under til å løse likningssystemet 

\begin{align}
4x + 3y &= 9 \\
x - 2y &= 5 \\
\end{align}

Uttrykk løsningen som
1. Et likningssystem
2. En løsningsmengde

```{figure} ./figurer/eksempler/eksempel2.svg
:name: eksempel2
:width: 80%

Grafisk representasjon av likningssystemet
```

`````{admonition} Fasit
:class: solution, dropdown

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 3 \quad \land \quad y = -1.
$$
```

```{tab-item} Løsning som løsningsmengde
$$
(x, y) \in \{(3, -1)\}.
$$
```
````


`````

`````{admonition} Løsning
:class: solution, dropdown
Fra figuren ser vi at de to linjene skjærer hverandre i $(x, y) = (3, -1)$. Dermed er løsningen av likningssystemet

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 3 \quad \land \quad y = -1.
$$
```

```{tab-item} Løsning som løsningsmengde
$$
(x, y) \in \{(3, -1)\}.
$$
```
````


`````
``````

<!-- ## Antall løsninger
På samme måte som en lineær likning kan ha ingen, én eller uendelig mange løsninger, kan også lineære likningssystemer ha ingen, én eller uendelig mange løsninger. 

## Likningssystem med flere enn to variabler
Et likningssystem kan ha flere enn to variabler, men disse likningssystemene vil være vanskelige å tegne opp i et todimensjonalt koordinatsystem, ettersom vi har en variabel representert langs hver akse. For likningssystemer med flere enn to variabler vil vi som regel heller velge en algebraisk løsningsmetode.  -->

## Oppgaver
--- 

``````{admonition} Oppgave 1
:class: problem
Bruk figuren under til å løse likningssystemet 
\begin{align} 
x - 2y &=2 \\
x + 4y & =8 \\
\end{align}

Uttrykk løsningen som 
1. Et likningssystem
2. En løsningsmengde

```{figure} ./figurer/oppgaver/oppgave1.svg
:name: oppgave 1
:width: 80%

Bruk figuren til å løse likningssystemet
```

`````{admonition} Fasit
:class: dropdown, solution
````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = 4 \quad \land \quad y = 1.
$$
```

```{tab-item} Løsning som løsningsmengde
$$
(x, y) \in \{(4, 1)\}.
$$
```
````
`````
``````

---

````{admonition} Oppgave 2
:class: problem
Bruk det interaktive vinduet under til å bestemme $k$ slik at likningssystemet 

\begin{align}
2x + 3y &= 5 \\
x + y + k &= 0
\end{align}

Oppgave 2a
: Har løsningen $x = 4 \, \land \, y = -1$.

Oppgave 2b
: Har løsningsmengden $(x, y) \in \{(-2, 3)\}$.

```{raw} html
:file: ./figurer/interaktive_plot/oppg_3.html
```


```{admonition} Fasit
:class: dropdown, solution
Oppgave 2a
: $k = -3$.

Oppgave 2b
: $k = -1$.
```

````

---


``````{admonition} Oppgave 3
:class: problem

Figuren under viser grafene til to lineære funksjoner. 

Lag et likningssystem som kan beskrives av de to funksjonene, og bruk figuren til å løse likningssystemet.


```{figure} ./figurer/oppgaver/oppgave_3.svg
:name: oppgave-3
:width: 80%
```


`````{admonition} Fasit
:class: dropdown, solution

$$
f(x) = 2x + 8 \quad \text{og} \quad g(x) = -2x - 4.
$$

Et likningssystem som beskrives av de to funksjonene er derfor

$$
\begin{align*}
    -2x + y &= 8 \\
    2x + y &= -4
\end{align*}
$$

Løsningen av likningssystemet kan uttrykkes som

````{tab-set}
```{tab-item} Løsning som likningssystem
$$
x = -3 \quad \land \quad y = 2.
$$
```

```{tab-item} Løsning som løsningsmengde
$$
(x, y) \in \{(-3, 2)\}.
$$
```
`````



```````