# Setningslogikk 


```{admonition} Læringsmål: setningslogikk
:class: tip
Etter å ha gått gjennom dette delkapittelet, er målet at du skal:
* Kunne forklare hva en påstand er i matematikken.
* Kunne forklare begrepene *implikasjon* og *ekvivalens*, og bruke disse for å uttrykke sammenhenger mellom påstander.
* Kunne forklare begrepene *logisk og*, og *logisk eller*, og bruke disse for å uttrykke sammensatte påstander.
```

Setningslogikken er i grenseland mellom matematikk og filosofi, og er utviklet for å kunne uttrykke sammenhenger mellom påstander på en presis måte. Vi skal forholde oss til nytteverdien det har for å beskrive sammenhenger i matematikken på en presis og kompakt måte. 

## Påstander
En **påstand** i matematikken kan ofte beskrives som en likning eller en ulikhet. En påstand kan være usann, men vi skal alltid anta at en påstand er sann og utvikle teori der vi beskriver sanne påstander (ærlighet varer lengst, *amirite*?). 

```{admonition} Eksempel 1: påstander i matematikken
:class: example

La oss se på noen eksempler på påstander i matematikken:

| Påstand | Beskrivelse |
| :---: | :---: |
| $2x + 1 = 3$ | $2x + 1$ er lik $3$. |
| $x > 4$ |  $x$ er større enn 4. |
| $x \in [1, 2]$ | $x$ er et tall i intervallet $[1, 2]$. |
| $x \in \mathbb{N}$ | $x$ er et naturlig tall. |
| $x \in \mathbb{R}$ | $x$ er et reelt tall. |

```


## Implikasjon og ekvivalens
Ofte er det en sammenheng mellom to påstander. Noen vil en sann påstand medføre at en annen påstand er sann, andre ganger vil de begge medføre at den andre er sann samtidig. Vi har to måter å uttrykke slike sammenhenger på: 


```{admonition} Vanlige symboler for påstander
:class: note, margin

Det er vanlig å bruke symbolene $p$ og $q$ for påstander. 
```

```{admonition} Implikasjon og ekvivalens
:class: theory

La $p$ og $q$ være to påstander. Da har vi følgende definisjoner:

Implikasjon: $p \Rightarrow q$
: $q$ er sann hvis $p$ er sann. Hvis $p$ er sann, så er $q$ også sann, sier vi at $p$ **impliserer** $q$. Vi skriver $p \Rightarrow q$. Påstanden $p \Rightarrow q$ leses som "hvis $p$, så $q$". 

Ekvivalens: $p \Leftrightarrow q$
: $q$ er sann hvis $p$ er sann ($p \Rightarrow q$), og $p$ er sann hvis $q$ er sann ($p \Leftarrow q$). Vi sier at $p$ og $q$ er **ekvivalente** og skriver $p \Leftrightarrow q$. Symbolet $\Leftrightarrow$ leses som "hvis og bare hvis". 

```

La oss ta et litt hverdagslig eksempel først:

```{admonition} Eksempel 2: implikasjon
:class: example
Vi har to påstander $p$ og $q$ som følger:

$$
p = \text{Kari bor i Oslo} \quad \text{og} \quad q = \text{Kari bor i Norge}.
$$

Hvis $p$ er sann, så er også $q$ sann. Dermed kan vi skrive $p \Rightarrow q$. Men hvis $q$ er sann, så betyr ikke det at $p$ er sann, siden du kan bo i fryktelig mange andre steder i Norge enn Oslo. Dermed er $p \not \Leftarrow q$, så påstandene er ikke ekvivalente. (Vi slenger en skråstrek gjennom et symbol for å indikere motsetningen til symbolet).
```

Vi tar et eksempel som er mer matematisk orientert:

```{admonition} Eksempel 3: implikasjon og ekvivalens
:class: example

|Påstand $p$|  |
```

Vi tar et eksempel til, men nå litt mer matematisk orientert:

```{admonition} Eksempel 4: ekvivalens
:class: example

Vi har to påstander $p$ og $q$ som følger:

Påstand $p$:
: $x \in [1, 2]$

Påstand $q$:
: $1 \leq x \leq 2$

Hvis $p$ er sann, så er også $q$ sann. Hvis $q$ er sann, så er også $p$ sann. Dermed er $p$ og $q$ ekvivalente, og vi kan skrive $p \Leftrightarrow q$, eller da 

$$
x \in [1, 2] \quad \Leftrightarrow \quad 1 \leq x \leq 2.
$$

```

````{admonition} Underveisoppgave 1
:class: check

Fyll ut tabellen under:
Fyll inn med logikksymbolene $\Leftarrow$, $\Rightarrow$ eller $\Leftrightarrow$ i tabellen under slik at du får en sann påstand.

|Påstand $p$| Symbol | Påstand $q$ |
|:---:|:---:|:---:|
| $x > 6$ | | $x > 2$ |
| $x^2 = 25$ | | $x = 5$ |
| $x = -3$ | | $x^2 = 9$ |
| $x^2 = 4$ | | $\|x\| = 2$ |
| $2x - y = 5$ | | $x = 2 \, \land \, y = -1$ |

```{admonition} Løsning
:class: dropdown, solution

|Påstand $p$| Symbol | Påstand $q$ |
|:---:|:---:|:---:|
| $x > 6$ | $\Rightarrow$ | $x > 2$ |
| $x^2 = 25$ | $\Leftarrow$ | $x = 5$ |
| $x = -3$ | $\Rightarrow$ | $x^2 = 9$ |
| $x^2 = 4$ | $\Leftrightarrow$ | $\|x\| = 2$ |
| $2x - y = 5$ | $\Leftarrow$ | $x = 2 \, \land \, y = -1$ |
```

````

## Konjunksjon og disjunksjon


En annen måte å uttrykke sammensatte mengder på er ved hjelp av ulikheter. Før vi går videre, må vi gjøre det klart hva vi mener med en **påstand** i matematikk. En påstand er et utsagn om noe, for eksempel vil $2x + 1 = 3$ regnes som en påstand selv om vi vanligvis bruker begrepet *likning* om en slik påstand. Et annet eksempel på en påstand er $x > 4$. En påstand er enten sann eller usann. Typisk når vi ønsker å beskrive svaret på en likning, ulikhet eller et likningssystem, uttrykker vi det med påstander som er *sanne*.


Nå er vi klare for å innføre to nye begreper fra **setningslogikken** og en samsvarende skrivemåter:

```{admonition} Logiske operatorer: konjunksjon og disjunksjon
:class: theory
Vi tenker oss at vi har to påstander $p$ og $q$. Da har vi følgende logiske operatorer:

Disjunksjon (logisk eller): $p \lor q$
: Når enten $p$ eller $q$ er sanne, eller begge er sanne, sier vi at de er **disjunktive** påstander. Vi skriver $p \lor q$ og leser det som $p$ **eller** $q$ (eller *begge*). Altså er enten påstand $p$ sann, eller så er $q$ sann, eller så er begge sanne. 

Konjunksjon (logisk og): $p \land q$
: Når både $p$ og $q$ er sanne samtidig, sier vi at de er **konjuktive** påstander. Vi skriver $p \land q$ og leser det som $p$ **og samtidig** $q$. Altså må både påstand $p$ og $q$ være sanne samtidig!
```

Begrepene over er litt abstrakte, så la oss gjøre dem mer konkrete. 

```{admonition} Eksempel 4: disjunksjon (eller)
:class: example
Mengden bestående av alle $x \in [-1, 0] \cup \langle 1, 2 \rangle$ kan vi uttrykke som at enten så er $x\in [-1, 0]$ eller så er $x \in \langle 1, 2 \rangle$. Vi kan derfor uttrykke dette som at 

$$
x \in [-1, 0] \cup \langle 1, 2 \rangle \quad \Leftrightarrow \quad -1 \leq x \leq 0 \, \lor \, 1 < x < 2
$$

Knytter vi det til teorien over er den éne påstanden $-1 \leq x \leq 0$ og den andre påstanden $1 < x < 2$. Disse to påstandene er disjunktive siden de ikke trenger å være sanne samtidig (faktisk *kan* de ikke være sanne samtidig her), og vi bruker disjunksjon for å binde dem sammen. 
```

**Din tur!**

````{admonition} Underveisoppgave 3
:class: check
Fyll ut tabellen under:

| Intervall | Ulikheter |
| :---: | :---: |
| $x\in [1, 2] \cup [3, 4]$ | |
| $y\in[1, 2] \cup \langle 3, 4]$ | |
| $p\in \langle 1, 2] \cup [3, 4]$ | |
| $q\in \langle 1, 2] \cup \langle 3, 4]$ | |
| $r \in \mathbb{R} \setminus [-1, 1]$ | |

```{admonition} Fasit
:class: dropdown, answer
| Intervall | Ulikheter |
| :---: | :---: |
| $x\in [1, 2] \cup [3, 4]$ | $1 \leq x \leq 2 \, \lor \, 3 \leq x \leq 4$ |
| $y\in[1, 2] \cup \langle 3, 4]$ | $1 \leq y \leq 2 \, \lor \, 3 < y \leq 4$ |
| $p\in \langle 1, 2] \cup [3, 4]$ | $1 < p \leq 2 \, \lor \, 3 \leq p \leq 4$ |
| $q\in \langle 1, 2] \cup \langle 3, 4]$ | $1 < q \leq 2 \, \lor \, 3 < q < 4$ |
| $r \in \mathbb{R} \setminus [-1, 1]$ | $r < -1 \, \lor \, r > 1$ |
```
````

Vi tar også et eksempel på konjunksjon som illustrerer bruken av konjunksjon når vi jobber med likningssystemer senere i matematikken:

```{admonition} Eksempel 5: konjunksjon (og samtidig)
:class: example
Vi tenker oss et likningssystem 

\begin{align}
    x+y &= 3 \\
    x-y &= 1
\end{align}

I et likningssystem skal begge likninger være oppfylt samtidig. Vi kan se på dette som to påstander som må være sanne samtidig. Derfor kan vi skrive likningssystemet som

$$
x+y = 3 \, \land \, x-y = 1.
$$

Løsningen til dette likningssystemet vil i seg selv være et (trivielt) likningssystem som består av to likninger som er sanne samtidig. Prøver vi ut $x = 2$ og $y = 1$, så er begge likninger oppfylt samtidig, som betyr at

$$
x + y = 3 \, \land \, x - y = 1 \quad \Leftrightarrow \quad x = 2 \, \land \, y = 1
$$
```




```{admonition} Eksempel 6: Enkle intervaller som ulikheter
:class: example

Vi har sett at vi kan skrive enkle intervaller som en slags "dobbel"-ulikhet. For eksempel har vi skrevet 

$$
x \in [-1, 1] \quad \Leftrightarrow \quad -1 \leq x \leq 1
$$

Men vi kan også skriv dette ved hjelp av en konjunksjon som

$$
-1 \leq x \leq 1  \quad \Leftrightarrow \quad  -1 \leq x \, \land \, x \leq 1
$$

Denne skrivemåten er ikke nødvendigvis så fryktelig vanlig fordi den ikke er noe særlig enklere å skrive, men er likevel en helt gyldig uttrykksmåte. Vi velger vanligvis den enkleste skrivemåten som også er lettest mulig å lese. 
```
