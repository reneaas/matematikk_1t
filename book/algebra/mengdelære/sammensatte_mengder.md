# Sammensatte mengder

Noen ganger kan vi ikke beskrive en mengde med ett intervall eller med én ulikhet. Noen ganger kan vi ikke uttrykke de som ulikheter eller intervaller i det hele tatt.
Vi kan gi noen eksempler på tilfeller der vi teorien kjenner så langt ikke strekker til:
* Alle reelle tall bortsett fra $x = 0$. 
* Alle reelle tall over $x = 2$ og mindre enn $x = -1$.
* Alle reelle fra $x = -2$ til $x = 1$ og fra $x = 3$ til $x = 4$.
* Løsningen av likninger og likningssystemer som har flere løsninger.

Etter denne seksjonen vil du kunne beskrive slike mengder på en kort og kompakt måte.


For å beskrive slike mengder, må vi finne ut hvordan vi setter sammen flere mengder, enten uttrykt som intervaller eller som ulikheter.

```{admonition} Læringsmål: sammensatte mengder
:class: tip
Målet for denne seksjon er at du skal:
* Kjenne til ulike regneregler for mengder.
* Kunne beskrive sammensatte mengder ved hjelp av intervaller, ulikheter og listenotasjon.
* Forstå begrepene konjuksjon og disjunksjon, og kunne bruke dem til å veksle mellom ulikheter og intervaller, og mellom listenotasjon og likninger.
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
| $\{1, 2, 3\}$ | $\{2, 3, 4\}$ | $\{1, 2, 3, 4\}$ | $\{2, 3\}$ | $\{1\}$ |
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
|$\{-1, 1\}$| $\{0, 2\}$ | $\{-1, 0, 1, 2\}$ | $\emptyset$ | $\{-1, 1\}$ |
| $\{-4, 2, 4\}$ | $\{1, 2, 4\}$ | $\{-4, 1, 2, 4\}$ | $\{2, 4\}$ | $\{-4\}$ |
| $\{1, 2, 3\}$ | $\{3, 4, 5\}$ | $\{1, 2, 3, 4, 5\}$ | $\{3\}$ | $\{1, 2\}$ |
| $[1, 2]$ | $[2, 4]$ | $[1, 4]$ | $[2, 2] = {2}$ | $[1, 2 \rangle$ |
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
En annen måte å uttrykke sammensatte mengder på er ved hjelp av ulikheter. Før vi går videre, må vi gjøre det klart hva vi mener med en **påstand** i matematikk. En påstand er et utsagn om noe, for eksempel vil $2x + 1 = 3$ regnes som en påstand selv om vi vanligvis bruker begrepet *likning* om en slik påstand. Et annet eksempel på en påstand er $x > 4$. En påstand er enten sann eller usann. Typisk når vi ønsker å beskrive svaret på en likning, ulikhet eller et likningssystem, uttrykker vi det med påstander som er *sanne*.


Nå er vi klare for å innføre to nye begreper fra **setningslogikken** og en samsvarende skrivemåter:

```{admonition} Logiske operatorer: konjunksjon og disjunksjon
:class: tip
Vi tenker oss at vi har to påstander $p$ og $q$. Da har vi følgende logiske operatorer:

Disjunksjon (logisk eller): $p \lor q$
: Når enten $p$ eller $q$ er sanne, eller begge er sanne, sier vi at de er **disjunktive** påstander. Vi skriver $p \lor q$ og leser det som $p$ **eller** $q$ (eller *begge*). Altså er enten påstand $p$ sann, eller så er $q$ sann, eller så er begge sanne. 

Konjunksjon (logisk og): $p \land q$
: Når både $p$ og $q$ er sanne samtidig, sier vi at de er **konjuktive** påstander. Vi skriver $p \land q$ og leser det som $p$ **og samtidig** $q$. Altså må både påstand $p$ og $q$ være sanne samtidig!
```

Begrepene over er litt abstrakte, så la oss gjøre dem mer konkrete:



```{admonition} Eksempel 1: disjunksjon (eller)
:class: eksempel
Mengden bestående av alle $x \in [-1, 0] \cup \langle 1, 2 \rangle$ kan vi uttrykke som at enten så er $x\in [-1, 0]$ eller så er $x \in \langle 1, 2 \rangle$. Vi kan derfor uttrykke dette som at 

$$
x \in [-1, 0] \cup \langle 1, 2 \rangle \quad \Leftrightarrow \quad -1 \leq x \leq 0 \, \lor \, 1 < x < 2
$$

Knytter vi det til teorien over er den éne påstanden $-1 \leq x \leq 0$ og den andre påstanden $1 < x < 2$. Disse to påstandene er disjunktive siden de ikke trenger å være sanne samtidig (faktisk *kan* de ikke være sanne samtidig her), og vi bruker disjunksjon for å binde dem sammen. Derfor binder vi de sammen med disjunksjonssymbolet $\lor$.
```

```{admonition} Eksempel 2: konjunksjon (og samtidig)
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

Vi merker oss at siden $x = 2$ og $y = 1$ samtidig, så bruker vi konjunksjon for å binde $x = 2$ og $y = 1$ sammen. De må altså være sanne samtidig. Knytter vi de over til teorien, så er $x = 2$ den *ene* påstanden og $y = 1$ den andre. Men disse *må* være sanne samtidig, så derfor bruker vi konjuksjonssymbolet $\land$.
```

Nå er vi klare for å se på hvordan vi kan skrive om sammensatte intervaller til ulikheter:

```{admonition} Sammensatte mengder som ulikheter
:class: tip
Hvis et intervall $I = [a, b] \cup [c, d]$ og $x \in I$, så kan vi skrive 

$$
x \in I \quad \Leftrightarrow \quad a \leq x \leq b \, \lor \, c \leq x \leq d
$$
```
Den generelle formen over kan utvides til åpne og halvåpne intervaller. Prøv deg på oppgaven under for å se om du forstår sammenhengen! **Prøv godt før du ser på løsningen**.

```{admonition} Underveisoppgave 3
:class: note
Fyll ut tabellen under:

| Intervall | Ulikheter |
| :---: | :---: |
| $x\in [1, 2] \cup [3, 4]$ | |
| $y\in[1, 2] \cup \langle 3, 4]$ | |
| $p\in \langle 1, 2] \cup [3, 4]$ | |
| $q\in \langle 1, 2] \cup \langle 3, 4]$ | |
| $r \in \mathbb{R} \setminus [-1, 1]$ | |
```

```{dropdown} Løsning
| Intervall | Ulikheter |
| :---: | :---: |
| $x\in [1, 2] \cup [3, 4]$ | $1 \leq x \leq 2 \, \lor \, 3 \leq x \leq 4$ |
| $y\in[1, 2] \cup \langle 3, 4]$ | $1 \leq y \leq 2 \, \lor \, 3 < y \leq 4$ |
| $p\in \langle 1, 2] \cup [3, 4]$ | $1 < p \leq 2 \, \lor \, 3 \leq p \leq 4$ |
| $q\in \langle 1, 2] \cup \langle 3, 4]$ | $1 < q \leq 2 \, \lor \, 3 < q < 4$ |
| $r \in \mathbb{R} \setminus [-1, 1]$ | $r < -1 \, \lor \, r > 1$ |
```

```{admonition} Eksempel 3: Enkle intervaller som ulikheter
:class: eksempel

Vi har sett at vi kan skrive enkle intervaller som en slags "dobbel"-ulikhet. For eksempel har vi skrevet 

$$
[-1, 1] \quad \Leftrightarrow \quad -1 \leq x \leq 1
$$

Men vi kan også skriv dette ved hjelp av en konjunksjon som

$$
-1 \leq x \leq 1  \quad \Leftrightarrow \quad  -1 \leq x \, \land \, x \leq 1
$$

Denne skrivemåten er ikke nødvendigvis så fryktelig vanlig fordi den ikke er noe særlig enklere å skrive, men er likevel en helt gyldig uttrykksmåte. Vi velger vanligvis den enkleste skrivemåten som også er lettest mulig å lese. 
```


## Oppgaver

### Oppgave 1
Fyll ut tabellen under:

|Intervall | Ulikheter |
|:---:|:---:|
| $x\in [0, 1] \cup [2, 5]$ | |
|  | $-2 \leq y \land y\leq 3$  |
| $z\in \langle -1, 1 \rangle \cup \langle 2, 3 \rangle$ | |
|  | $-3 \leq p < 2 \, \lor  p > 4$ |
| $q\in \mathbb{R} \setminus \langle 0, 1]$ | |


```{dropdown} Løsning
|Intervall | Ulikheter |
|:---:|:---:|
| $x\in [0, 1] \cup [2, 5]$ | $0 \leq x \leq 1 \, \lor \, 2 \leq x \leq 5$ |
| $y \in [-2, 3]$ | $-2 \leq y \land y\leq 3$ |
| $z\in \langle -1, 1 \rangle \cup \langle 2, 3 \rangle$ | $-1 < z < 1 \, \lor \, 2 < z < 3$ |
| $p \in [-3, 2 \rangle \cup \langle 4, \to \rangle$ | $-3 \leq p < 2 \, \lor  p > 4$ |
| $q\in \mathbb{R} \setminus \langle 0, 1]$ | $q \leq 0 \, \lor \, p > 1$ |
```

### Oppgave 2
