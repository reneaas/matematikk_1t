# Sammensatte mengder

Noen ganger kan vi ikke beskrive en mengde med ett intervall eller med én ulikhet. Noen ganger kan vi ikke uttrykke de som ulikheter eller intervaller i det hele tatt.
Vi kan gi noen eksempler på tilfeller der vi teorien kjenner så langt ikke strekker til:
* Alle reelle tall bortsett fra $x = 0$. 
* Alle reelle tall over $x = 2$ og mindre enn $x = -1$.
* Alle reelle fra $x = -2$ til $x = 1$ og fra $x = 3$ til $x = 4$.
* Mengden av tallene $-1$, $1$ og $3$.
* Mengden av punktene $(1, 2)$ og $(3, 4)$ og $(-2, 3)$.

Etter denne seksjonen vil du kunne beskrive slike mengder på en kort og kompakt måte.


For å beskrive slike mengder, må vi finne ut hvordan vi setter sammen flere mengder, enten uttrykt som intervaller eller som ulikheter.

```{admonition} Læringsmål: sammensatte mengder
:class: tip
Målet for denne seksjon er at du skal:
* Kjenne til ulike regneregler for mengder.
* Kunne beskrive sammensatte mengder ved hjelp av intervaller, ulikheter og listenotasjon.
```

## Regneregler for mengder
Akkurat som reelle tall har regneregler, har også mengder sine egne regneregler. Vi trenger heldigvis bare noen få regneregler for å kunne beskrive sammensatte mengder.

```{admonition} Regneregler for mengder
:class: tip

La $A$ og $B$ være to mengder. Da har vi følgende regneregler:

Union: $A \cup B$
: Gir mengden av alle elementer som er i $A$ eller i $B$, eller i begge. Det vil si, alle elementer $x$ som enten oppfyller $x \in A$ eller $x \in B$, eller begge.

Snitt: $A \cap B$
: Gir mengden av alle elementer som er i både $A$ og $B$. Det vil si, alle elementer $x$ som oppfyller $x \in A$ og $x \in B$ samtidig. 

Differens (mengdeminus): $A \setminus B$
: Gir mengden av alle elementer som er i $A$, bortsett fra alle som også er i $B$. Det vil si, alle elementer $x$ som oppfyller $x \in A$ og $x \notin B$

Komplement: $A^c$
: Gir mengden av alle elementer som *ikke* er i $A$. Det vil si, mengden av alle elementer $x$ slik at $x \notin A$.
```

I tabellen under vises noen eksempler med listenotasjon og intervaller. Les den **nøye** og overbevis deg selv om at du forstår regnereglene:

````{margin}
```{admonition} Den tomme mengden
:class: tip
Noen ganger er det nyttig å kunne beskrive en mengde som ikke inneholder *noen elementer*. Vi kaller denne mengden for den **tomme mengden**. Vi bruker symbolet $\emptyset$ for denne mengden. På listeform kan vi skrive $\emptyset = \{\}$.
```
````

| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
| $\{1, 2, 3\}$ | $\{2, 3, 4\}$ | $\{1, 2, 3, 4\}$ | $\{2, 3\}$ | $\{-1, 1\}$ |
| $\{-2, -1\}$ | $\{1, 2\}$ | $\{-2, -1, 1, 2\}$ | $\emptyset$ | $\{-2, -1\}$ |
| $[1, 3]$ | $[2, 4]$ | $[1, 4]$ | $[2, 3]$ | $[1, 2 \rangle$ |
| $[1, 3]$ | $[4, 6]$ | $[1, 3] \cup [4, 6]$ | $\emptyset$ | $[1, 3]$ |
| $[-3, 3]$ | $[0, 2]$ | $[-3, 3]$ | $[0, 2]$ | $[-3, 0 \rangle$ |

```{admonition} Underveisoppgave 1
:class: note

Fyll ut tabellen under:
| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
|$\{-1, 1\}$| $\{0, 2\}$ | | | |
| $\{-4, 2, 4\}$ | $\{1, 2, 4\}$ | | | |
| $\{1, 2, 3\}$ | $\{3, 4, 5\}$ | | | |
| $[1, 2]$ | $[2, 4]$ | | | |
| $[-1, 2]$ | $[4, 6]$ | | | |
| $[-3, 3]$ | $[0, 2]$ | | | |
```

```{dropdown} Løsning

| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
|$\{-1, 1\}$| $\{0, 2\}$ | $\{-1, 0, 1, 2\}$ | $\emptyset$ | $\{-1\}$ |
| $\{-4, 2, 4\}$ | $\{1, 2, 4\}$ | $\{-4, 1, 2, 4\}$ | $\{2, 4\}$ | $\{-4\}$ |
| $\{1, 2, 3\}$ | $\{3, 4, 5\}$ | $\{1, 2, 3, 4, 5\}$ | $\{3\}$ | $\{1, 2\}$ |
| $[1, 2]$ | $[2, 4]$ | $[1, 4]$ | $[2, 2]$ | $[1, 2 \rangle$ |
| $[-1, 2]$ | $[4, 6]$ | $[-1, 2] \cup [4, 6]$ | $\emptyset$ | $[-1, 2]$ |
| $[-3, 3]$ | $[0, 2]$ | $[-3, 3]$ | $[0, 2]$ | $[-3, 0 \rangle \cup \langle 2, 3]$ |
```


## Sammensatte mengder som intervaller 
Når vi ønsker å beskrive flere deler av tallinja, kan vi bruke regnereglene for mengder til å uttrykke mengden av de reelle tallene vi ønsker å beskrive.
I tabellen under vises eksempler på sammensatte mengder uttrykt som intervaller. 

Les tabellen **nøye** og overbevis deg selv om at du forstår sammenhengen mellom beskrivelsen av mengden og intervallnotasjonen:

| Beskrivelse av mengde | Intervallnotasjon |
| :--- | :--- |
| Alle reelle tall fra og med $2$ til og med $4$, og fra $5$ til $8$ | $[2, 4] \cup \langle 5, 8 \rangle$ |
| Alle reelle tall fra og med $2$ til $3$, og fra og med $5$ til $6$ | $[2, 3\rangle \cup [5, 6 \rangle$ |
| Alle reelle tall, bortsett fra $0$ | $\langle \gets, 0 \rangle \cup \langle 0, \to \rangle = \mathbb{R} \setminus \{0\}$ |
| Alle reelle tall under $-2$ og over $3$ | $\langle \gets, -2 \rangle \cup \langle 3, \to \rangle$ |

```{admonition} Underveisoppgave 2
:class: note

Fyll ut tabellen under:
| Beskrivelse av mengde | Intervallnotasjon |
| :--- | :--- |
| Alle reelle tall fra og med $-1$ til og med $1$, og fra $2$ til $3$ | |
| Alle reelle tall fra og med $-2$ til $0$, og fra og med $1$ til $2$ | |
| Alle reelle tall, bortsett fra $1$ | |
| Alle reelle tall under $-3$ og over $2$ | |
| Alle reelle tall utenom $-1$, $0$ og $1$ | |
| Alle reelle tall utenom heltallene | |  
```

```{dropdown} Løsning
| Beskrivelse av mengde | Intervallnotasjon |
| :--- | :--- |
| Alle reelle tall fra og med $-1$ til og med $1$, og fra $2$ til $3$ | $[-1, 1] \cup [2, 3]$ |
| Alle reelle tall fra og med $-2$ til $0$, og fra og med $1$ til $2$ | $[-2, 0\rangle \cup [1, 2 \rangle$ |
| Alle reelle tall, bortsett fra $1$ | $\langle \gets, 1 \rangle \cup \langle 1, \to \rangle = \mathbb{R} \setminus \{1\}$ |
| Alle reelle tall under $-3$ og over $2$ | $\langle \gets, -3 \rangle \cup \langle 2, \to \rangle$ |
| Alle reelle tall utenom $-1$, $0$ og $1$ | $\mathbb{R} \setminus \{-1, 0, 1\}$ |
| Alle reelle tall utenom heltallene | $\mathbb{R} \setminus \mathbb{Z}$ |
```


## Sammensatte mengder som ulikheter
En annen måte å uttrykke sammensatte mengder på er ved hjelp av ulikheter. Da trenger vi to nye begreper og en notasjon:

```{admonition} Logiske operatorer: konjunksjon og disjunksjon
:class: tip
Vi tenker oss at vi har to påstander $p$ og $q$. Da har vi følgende logiske operatorer:

Disjunksjon
: Når enten $p$ eller $q$ er sanne, eller begge er sanne, sier vi at de er **disjunktive** påstander. Vi skriver $p \lor q$ og leser det som $p$ **eller** $q$ (eller *begge*).

Konjunksjon
: Når både $p$ og $q$ er sanne samtidig, sier vi at de er **konjuktive** påstander. Vi skriver $p \land q$ og leser det som $p$ **og samtidig** $q$.
```

Begrepene over er litt abstrakte, så la oss gjøre dem mer konkrete:



```{admonition} Eksempel 1: disjunksjon
:class: eksempel
Mengden bestående av alle $x \in [-1, 0] \cup \langle 1, 2 \rangle$ kan vi uttrykke som at enten så er $x\in [-1, 0]$ eller så er $x \in \langle 1, 2 \rangle$. Vi kan derfor uttrykke dette som at 

$$
x \in [-1, 0] \cup \langle 1, 2 \rangle \quad \Leftrightarrow \quad -1 \leq x \leq 0 \, \lor \, 1 < x < 2
$$
```

```{admonition} Eksempel 2: konjunksjon
:class: eksempel
Vi tenker oss et likningssystem 

\begin{align}
    x+y &= 3 \\
    x-y &= 1
\end{align}

Dette likningssystemet har løsningen $x = 2$ og $y = 1$. Vi kan uttrykke mengden av løsningene til likningssystemet som 

$$
(x, y) \in \{(2, 1)\} \quad \Leftrightarrow \quad x = 2 \, \land \, y = 1
$$

Vi merker oss at siden $x = 2$ og $y = 1$ samtidig, så bruker vi konjunksjon for å binde $x = 2$ og $y = 1$ sammen. De må altså være sanne samtidig.

```



````{comment}
```{admonition} Ekvivalens
:class: tip
Ekvivalens
: Når to utsagn som er uttrykt på forskjellig måte betyr det samme, sier vi at de er **ekvivalente**. Hvis $p$ og $q$ er to påstander som er ekvivalente, skriver vi $p \Leftrightarrow q$.

Implikasjon
: Når et utsagn fører til at et annet utsagn er sant, men ikke omvendt, sier vi at det første utsagnet **impliserer** det andre. Hvis $p$ impliserer $q$, skriver vi $p \Rightarrow q$. Vi kan også snu på det å skrive $q \Leftarrow p$. Begge skrivemåter uttrykker at $p$ implisere $q$.

Konjunksjon
: Når to utsagn er sanne, sier vi at de er **konjunktive**. Hvis $p$ og $q$ er sanne, skriver vi $p \land q$. Vi kan lese $\land$ som **og samtidig** fordi det uttrykker at $p$ og $q$ er sanne på én og samme tid.

Disjunksjon
: Når minst ett av to utsagn er sant, sier vi at de er **disjunktive**. Hvis $p$ eller $q$ er sanne, skriver vi $p \lor q$. Vi kan lese $\lor$ som **eller** fordi det uttrykker at enten $p$ er sann, eller $q$ er sann, eller så er begge sanne. 
```
````