# Sammensatte mengder

```{admonition} Læringsmål: sammensatte mengder
:class: tip
Målet for denne seksjon er at du skal:
* Kjenne til ulike regneregler for mengder.
* Kunne beskrive sammensatte mengder ved hjelp av intervaller, ulikheter og listenotasjon.
```

Noen ganger kan vi ikke beskrive en mengde med ett intervall eller med én ulikhet. Noen ganger kan vi ikke uttrykke de som ulikheter eller intervaller i det hele tatt.
Vi kan gi noen eksempler på tilfeller der vi teorien kjenner så langt ikke strekker til:
* Alle reelle tall bortsett fra $x = 0$. 
* Alle reelle tall som oppfyller at $x > 2$ eller $x \leq -1$.
* Alle reelle som oppfyller $-2 < x \leq 1$ eller $3 <x < 4$. 
* Løsningen av likninger og likningssystemer som har flere løsninger.

Målet vårt nå, er å utvikle verktøy og notasjon som gir oss muligheten til å beskrive sammensatte mengder på en kort og kompakt måte.

## Regneregler for mengder
Akkurat som reelle tall har regneregler, har også mengder sine egne regneregler. Vi trenger heldigvis bare noen få regneregler for å kunne beskrive sammensatte mengder.

```{admonition} Regneregler for mengder
:class: theory

La $A$ og $B$ være to mengder. Da har vi følgende regneregler:

Union: $A \cup B$
: Gir mengden av alle elementer som er i $A$ eller i $B$, eller i begge. Det vil si, alle elementer $x$ som enten oppfyller $x \in A$ eller $x \in B$, eller begge.

Snitt: $A \cap B$
: Gir mengden av alle elementer som er i både $A$ og $B$. Det vil si, alle elementer $x$ som oppfyller $x \in A$ og $x \in B$ samtidig. 

Mengdeminus (differens): $A \setminus B$
: Gir mengden av alle elementer som er i $A$, bortsett fra alle som også er i $B$. Det vil si, alle elementer $x$ som oppfyller $x \in A$ og $x \notin B$
```

Vi tar et eksempel for å illustrere regnereglene med lister:


````{admonition} Eksempel 1: regneregler for mengder - liste *edition*
:class: example
La $A = \{1, 2, 3\}$ og $B = \{2, 3, 4\}$. Da har vi at


$A \cup B$ (union):
: $A \cup B$ skal bestå av alle elementene som er inkludert i både $A$ eller $B$. Vi tar ikke med et element mer enn én gang selv om elementet er i begge mengdene. Derfor har vi at

$$
A \cup B = \{1, 2, 3, 4\}.
$$

$A \cap B$ (snitt):
: $A \cap B$ skal bestå av alle elementene som er inkludert i både $A$ og $B$ samtidig. Derfor har vi at

$$
A \cap B = \{2, 3\}. 
$$

$A \setminus B$ (mengdeminus):
: $A \setminus B$ skal bestå av alle elementene som er i $A$, bortsett fra de som *også* er i $B$. Derfor har vi at

$$
A \setminus B = \{1\}.
$$


````

**Din tur**!

````{admonition} Underveisoppgave 1
:class: check

Gitt mengdene $A = \{1, 3, 5\}$ og $B = \{-1, 1, 5\}$. Bestem mengdene
* $A \cup B$
* $A \cap B$
* $A \setminus B$
* $B \setminus A$

```{admonition} Fasit
:class: answer, dropdown

* $A \cup B = \{-1, 1, 3, 5\}$
* $A \cap B = \{1, 5\}$
* $A \setminus B = \{3\}$
* $B \setminus A = \{-1\}$
```

```{admonition} Løsning
:class: solution, dropdown

Vi har at $A = \{1, 3, 5\}$ og $B = \{-1, 1, 5\}$.

$A \cup B$
: Her skal vi ta med alle elementene som er i enten $A$ eller $B$, eller begge. Vi husker på at vi bare skal ha ett eksemplar av et element selv om elementet er i både $A$ og $B$. Dermed for vi

$$
A \cup B = \{-1, 1, 3, 5\}.
$$

$A \cap B$
: Snittet er mengden som består av elementene som er i både $A$ og $B$ samtidig. Dette er bare $1$ og $5$, så vi får

$$
A \cap B = \{1, 5\}. 
$$

$A \setminus B$
: A minus B er mengden av elementene som er i $A$, bortsett fra de som også er i $B$. Dermed har vi

$$
A \setminus B = \{3\}.
$$

$B \setminus A$
: B minus A er mengden av elementene som er i $B$, bortsett fra de som også er i $A$. Dermed har vi

$$
B \setminus A = \{-1\}.
$$
```
````

Så tar vi et eksempel med intervaller:

````{admonition} Eksempel 2: regneregler for mengder - intervall *edition*
:class: example
La $A = [-1, 3]$ og $B = \langle 2, 5]$. Da har vi 

$A \cup B$:
: Mengden skal bestå av alle tallene som er i enten $A$ eller $B$ eller begge. Vi kan se at $A$ og $B$ delvis overlapper, så mengden vi får blir bare å sette sammen de to intervallene til ett større intervall:

$$
A \cup B = [-1, 3] \cup \langle 2, 5] = [-1, 5].
$$

$A \cap B$:
: Mengden skal bestå av alle tall som er i både $A$ og $B$ samtidig. Dette blir altså intervallet der $A$ og $B$ overlapper. Da får vi:

$$
A \cap B = [-1, 3] \cap \langle 2, 5] = \langle 2, 3].
$$

$A \setminus B$:
: Mengden skal bestå av alle tall som er i $A$, bortsett fra de som også er i $B$. Dette blir 

$$
A \setminus B = [-1, 3] \setminus \langle 2, 5] = [-1, 2].
$$
````

Så er **din tur**!

````{admonition} Underveisoppgave 2
:class: check
To mengder er gitt ved $A = \langle -2, 3 \rangle$ og $B = [1, 4]$. Bestem mengdene

* $A \cup B$
* $A \cap B$
* $A \setminus B$

```{admonition} Fasit
:class: answer, dropdown

* $A \cup B = \langle -2, 4]$
* $A \cap B = [1, 3 \rangle$
* $A \setminus B = \langle -2, 1 \rangle$
```

```{admonition} Løsning
:class: solution, dropdown

Vi har at $A = \langle -2, 3 \rangle$ og $B = [1, 4]$. 

$A \cup B$:
: Mengden skal bestå av alle tallene som enten er i $A$ eller $B$, eller i begge. Mengdene delvis overlapper, så vi bare inkluderer alle tallene som er i begge mengder:

$$
A \cup B = \langle -2, 3 \rangle \cup [1, 4] = \langle -2, 4].
$$

$A \cap B$:
: Mengden skal bestå av alle tallene som er i både $A$ og $B$ samtidig. Dette er intervallet der $A$ og $B$ overlapper, som er:

$$
A \cap B = \langle -2, 3 \rangle \cap [1, 4] = [1, 3 \rangle.
$$

$A \setminus B$:
: Mengden skal bestå av alle tallene som er i $A$, bortsett fra de som også er i $B$. Dette blir

$$
A \setminus B = \langle -2, 1 \rangle.
$$
```

````





## Sammensatte mengder som intervaller 
Ofte vil vi trenge å beskrive flere intervaller på tallinja som *ikke overlapper*. Da får vi bruk for regnereglene for mengder. 


````{admonition} Eksempel 3: sammensatte mengder som intervaller
:class: example 
I tabellen under vises noen eksempler på sammensatte mengder uttrykt som intervaller, der intervallene vi prøver å sette ikke overlapper på tallinja.
| Beskrivelse av mengde | Intervallnotasjon |
| :--- | :--- |
| Alle reelle tall fra og med $2$ til og med $4$, og fra $5$ til $8$ | $[2, 4] \cup \langle 5, 8 \rangle$ |
| Alle reelle tall fra og med $2$ til $3$, og fra og med $5$ til $6$ | $[2, 3\rangle \cup [5, 6 \rangle$ |
| Alle reelle tall, bortsett fra $0$ | $\langle \gets, 0 \rangle \cup \langle 0, \to \rangle = \mathbb{R} \setminus \{0\}$ |
| Alle reelle tall under $-2$ og over $3$ | $\langle \gets, -2 \rangle \cup \langle 3, \to \rangle = \mathbb{R} \setminus [-2, 3]$ |


````

**Din tur!**

````{admonition} Underveisoppgave 3
:class: check

Fyll ut tabellen under:
| Beskrivelse av mengde | Intervallnotasjon |
| :--- | :--- |
| Alle reelle tall fra og med $-1$ til og med $1$, og fra $2$ til $3$ | |
| Alle reelle tall fra og med $-2$ til $0$, og fra og med $1$ til $2$ | |
| Alle reelle tall, bortsett fra $1$ | |
| Alle reelle tall under $-3$ og over $2$ | |
| Alle reelle tall utenom $-1$, $0$ og $1$ | |
| Alle reelle tall utenom heltallene | |  

```{admonition} Fasit
:class: answer, dropdown
| Beskrivelse av mengde | Intervallnotasjon |
| :--- | :--- |
| Alle reelle tall fra og med $-1$ til og med $1$, og fra $2$ til $3$ | $[-1, 1] \cup [2, 3]$ |
| Alle reelle tall fra og med $-2$ til $0$, og fra og med $1$ til $2$ | $[-2, 0\rangle \cup [1, 2 \rangle$ |
| Alle reelle tall, bortsett fra $1$ | $\langle \gets, 1 \rangle \cup \langle 1, \to \rangle = \mathbb{R} \setminus \{1\}$ |
| Alle reelle tall under $-3$ og over $2$ | $\langle \gets, -3 \rangle \cup \langle 2, \to \rangle = \mathbb{R} \setminus [-3, 2]$ |
| Alle reelle tall utenom $-1$, $0$ og $1$ | $\mathbb{R} \setminus \{-1, 0, 1\}$ |
| Alle reelle tall utenom heltallene | $\mathbb{R} \setminus \mathbb{Z}$ |
```
````



## Sammensatte mengder som ulikheter


---

## Oppgaver

```{admonition} Den tomme mengden
:class: note, margin
Noen ganger er det nyttig å kunne beskrive en mengde som ikke inneholder *noen elementer*. Vi kaller denne mengden for den **tomme mengden**. Vi bruker symbolet $\emptyset$ for denne mengden. På listeform kan vi skrive $\emptyset = \{\}$.
```

````{admonition} Oppgave 1
:class: problem-level-1

Fyll ut tabellen under:
| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
|$\{-1, 1\}$| $\{0, 2\}$ | | | |
| $\{-4, 2, 4\}$ | $\{1, 2, 4\}$ | | | |
| $\{1, 2, 3\}$ | $\{3, 4, 5\}$ | | | |
| $[1, 2]$ | $[2, 4]$ | | | |
| $[-1, 2]$ | $[4, 6]$ | | | |
| $[-3, 3]$ | $[0, 2]$ | | | |

```{admonition} Fasit
:class: dropdown, answer
| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
|$\{-1, 1\}$| $\{0, 2\}$ | $\{-1, 0, 1, 2\}$ | $\emptyset$ | $\{-1, 1\}$ |
| $\{-4, 2, 4\}$ | $\{1, 2, 4\}$ | $\{-4, 1, 2, 4\}$ | $\{2, 4\}$ | $\{-4\}$ |
| $\{1, 2, 3\}$ | $\{3, 4, 5\}$ | $\{1, 2, 3, 4, 5\}$ | $\{3\}$ | $\{1, 2\}$ |
| $[1, 2]$ | $[2, 4]$ | $[1, 4]$ | $[2, 2] = \{2\}$ | $[1, 2 \rangle$ |
| $[-1, 2]$ | $[4, 6]$ | $[-1, 2] \cup [4, 6]$ | $\emptyset$ | $[-1, 2]$ |
| $[-3, 3]$ | $[0, 2]$ | $[-3, 3]$ | $[0, 2]$ | $[-3, 0 \rangle \cup \langle 2, 3]$ |
```
````

---

````{admonition} Oppgave 2
:class: problem-level-1

Fyll ut tabellen under:

|Intervall | Ulikheter |
|:---:|:---:|
| $x\in [0, 1] \cup [2, 5]$ | |
|  | $-2 \leq y \land y\leq 3$  |
| $z\in \langle -1, 1 \rangle \cup \langle 2, 3 \rangle$ | |
|  | $-3 \leq p < 2 \, \lor  p > 4$ |
| $q\in \mathbb{R} \setminus \langle 0, 1]$ | |


```{admonition} Fasit
:class: dropdown, answer
|Intervall | Ulikheter |
|:---:|:---:|
| $x\in [0, 1] \cup [2, 5]$ | $0 \leq x \leq 1 \, \lor \, 2 \leq x \leq 5$ |
| $y \in [-2, 3]$ | $-2 \leq y \land y\leq 3$ |
| $z\in \langle -1, 1 \rangle \cup \langle 2, 3 \rangle$ | $-1 < z < 1 \, \lor \, 2 < z < 3$ |
| $p \in [-3, 2 \rangle \cup \langle 4, \to \rangle$ | $-3 \leq p < 2 \, \lor  p > 4$ |
| $q\in \mathbb{R} \setminus \langle 0, 1]$ | $q \leq 0 \, \lor \, p > 1$ |
```

````

---