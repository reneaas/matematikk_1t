# Mengder som intervaller og ulikheter

Noen ganger ønsker vi å beskrive en mengde tall på en kort og presis måte. Dersom vi ønsker å beskrive én eller flere sammenhengende deler av tallinja, kan vi bruke **intervaller**. 
Vi kan også uttrykke intervaller som **ulikheter**. I denne seksjonen skal vi først se på hvordan vi kan uttrykke mengdene som intervaller, deretter som ulikheter.

## Intervaller
Noen ganger ønsker vi å beskrive en mengde tall på en kort og presis måte. Dersom vi ønsker å beskrive én eller flere sammenhengende deler av tallinja, kan vi bruke **intervaller**.  

### Intervaller
I tabellen under vises de vanligste måte å uttrykke intervaller på. Les forklaringene i tabellen **nøye**:

```{margin}
<br>

Merk at når det nedre endepunktet er inkludert, sier vi **fra og med**. Når det ikke er inkludert, sier vi bare **fra**. På samme måte sier vi **til og med** når det øvre endepunktet er inkludert, og **opp til** eller bare **til** når det ikke er inkludert.
```

````{margin}
```{admonition} Åpent, halvåpent eller lukket intervall?
:class: tip
Du legger kanskje merke til at når et intervall er åpent er ingen av endepunktene inkludert. Når det er halvåpent er det ene endepunktet inkludert, mens det andre er ikke. Likevel påstår tabellen at $[a, \to \rangle$ er et lukket intervall. Men dette er fordi vi mener at vi inkluderer **alle** tall fra og med $a$ og oppover. En annen måte å skrive dette på er $[a, \infty\rangle$. Men $\infty$ (uendelig) er ikke et punkt, det forteller oss bare at vi aldri stopper å gå oppover tallinja. Notasjonen uttrykker altså at vi inkluderer alle tall over $a$, så da må jo tallmengden være lukket, selv om $\infty$ ikke i seg selv er et tall.
```
````

| Notasjon | Type intervall | Forklaring | Eksempel |
| :---: | :---: | --- | --- |
| $[a, b]$ | **Lukket** | Alle tall fra og med $a$ til og med $b$ | $[2, 5]$ betyr mengden av reelle tall fra og med $2$ til og med $5$. Både $2$ og $5$ er inkludert.|
| $\langle a, b\rangle$ | **Åpent** | Alle tall fra $a$ til $b$, men $a$ og $b$ er *ikke* inkludert. | $\langle1, 4\rangle$ betyr mengden av reelle tall fra $1$ opp til $4$, men $1$ og $4$ er ikke inkludert.|
| $\langle a, b]$ | **Halvåpent** | Alle tall fra $a$ opp til og med $b$. | $\langle -1, 3]$ betyr mengden av alle reelle tall fra $-1$ opp til og med $3$. $-1$ er *ikke* inkludert, men $3$ er inkludert. |
| $[a, b\rangle$ | **Halvåpent** | Alle tall fra og med $a$ til $b$. | $[0, 2\rangle$ betyr mengden av alle reelle tall fra og med $0$ opp til $2$. $0$ er inkludert, men $2$ er ikke. |
| $[a, \to \rangle$ | **Lukket** | Alle tall fra og med $a$ og oppover. | $[3, \to \rangle$ betyr mengden av alle reelle tall fra og med $3$ og oppover. |
| $\langle \gets, b]$ | **Lukket** | Alle tall opp til og med $b$. | $\langle \gets, 2]$ betyr mengden av alle reelle tall opp til og med $2$. |
|$\langle a, \to \rangle$| **Halvåpent** | Alle tall fra $a$ og oppover. | $\langle 0, \to \rangle$ betyr mengden av alle reelle tall fra $0$ og oppover, men $0$ er ikke inkludert. |
|$\langle \gets, b\rangle$| **Halvåpent** | Alle tall opp til $b$. | $\langle \gets, 2\rangle$ betyr mengden av alle reelle tall opp til $2$, men $2$ er ikke inkludert. |




````{admonition} Underveisoppgave 1
:class: note

Ta for deg mengdene i tabellen under og bestemm type intervall og beskriv tallene som hører til mengdene:

| Mengde | Type intervall | Beskrivelse |
|:---:|:---:|---|
| $[-1, 1]$| | |
| $\langle 0, 3\rangle$| | |
| $\langle -2, 2]$| | |
| $[0, \to \rangle$| | |
| $\langle \gets, -3\rangle$ | | |

````


````{dropdown} Løsning
| Mengde | Type intervall | Beskrivelse |
|:---:|:---:|---|
| $[-1, 1]$| Lukket intervall |Alle reelle tall fra og med $-1$ til og med $1$. |
| $\langle 0, 3\rangle$| Åpent intervall | Alle reelle tall fra $0$ opp til $3$ |
| $\langle -2, 2]$| Halvåpent intervall | Alle reelle tall fra $-2$ opp til og med $2$ |
| $[0, \to \rangle$| Lukket intervall | Alle reelle tall fra og med $0$ og oppover |
| $\langle \gets, -3\rangle$ | Halvåpent intervall | Alle reelle tall opp til $-3$ |
````

## Mengder beskrevet som ulikheter

Mengder kan også beskrives med **ulikheter**. Før vi ser på sammenhengen mellom intervaller og ulikheter, trenger vi å forstå litt notasjon som brukes når man uttrykker ulikheter. Les tabellen under **nøye**:

| Ulikhet | Forklaring | Eksempel |
| :---: | --- | --- |
|  $<$ | Mindre enn | $2 < 3$ betyr at $2$ er mindre enn $3$.|
|  $>$ | Større enn enn | $5 > 4$ betyr at $5$ er større enn $4$. |
| $\leq$ | Mindre enn eller lik | $x \leq 3$ betyr at $x$ er mindre enn eller lik $3$.|
| $\geq$ | Større enn eller lik | $x \geq 5$ betyr at $x$ er større enn eller lik $5$.|

### Sammenhengen mellom intervaller og ulikheter
For å beskrive et intervall, så introduserer vi en variabel (for eksempel $x$) som oppfyller én eller flere ulikheter. Dette vil være en beskrivelse av intervallet. Vi trenger bittelitt mer notasjon for å kunne uttrykke oss presist:

Definisjonen over er svært abstrakt, men heldigvis skal vi nå gjøre det mer konkrete. Vi skal vise hvordan vi kan uttrykke intervallet ved hjelp av ulikheter. Les tabellen under **nøye** (du må nok lese definisjonene over flere ganger mens du leser tabellen under for å forstå det ordentlig):


I tabellen vises hvordan de ulike intervallene kan uttrykkes ved hjelp av ulikheter:

| Intervall | Ulikhet | Eksempel |
| :---: | :---: | :---: |
| $x \in [a, b]$ | $a \leq x \leq b$ | $x \in [1, 2] \quad \Leftrightarrow \quad 1 \leq x \leq 2 $ |
| $x \in \langle a, b\rangle$ | $a < x < b$ | $x \in \langle 1, 2\rangle \quad \Leftrightarrow \quad 1 < x < 2 $ |
| $x \in \langle a, b]$ | $a < x \leq b$ | $x \in \langle 1, 2] \quad \Leftrightarrow \quad 1 < x \leq 2 $ |
| $x \in [a, b\rangle$ | $a \leq x < b$ | $x \in [1, 2\rangle \quad \Leftrightarrow \quad 1 \leq x < 2$ |
| $x \in [a, \to \rangle$ | $a \leq x$ | $x \in [3, \to \rangle \quad \Leftrightarrow \quad 3 \leq x $|
| $x \in \langle \gets, b]$ | $x \leq b$ | $x \in \langle \gets, 2] \quad \Leftrightarrow \quad x \leq 2$ |
|$x \in \langle a, \to \rangle$| $a < x$ | $x \in \langle 0, \to \rangle \quad \Leftrightarrow \quad 0 < x $ |
|$x \in \langle \gets, b\rangle$| $x < b$ | $x \in \langle \gets, 2\rangle \quad \Leftrightarrow \quad x < 2$ |


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

```{admonition} Underveisoppgave 2
:class: note
Skriv om intervallene i tabellen under til ulikheter:

| Intervall | Ulikhet |
|:---:|:---:|
| $x \in [0, 3]$ | |
| $x \in \langle -2, 2]$ | |
| $x \in [0, \to \rangle$ | |
| $x \in \langle \gets, -3\rangle$ | |
| $x \in \langle 1, 4\rangle$ | |
| $x \in [2, 5\rangle$ | |
| $x \in \langle -5, \to \rangle$ | |
| $x \in \langle \gets, 2\rangle$ | |
```

```{dropdown} Løsning
| Intervall | Ulikhet |
|:---:|:---:|
| $x \in [0, 3]$ | $0 \leq x \leq 3$ |
| $x \in \langle -2, 2]$ | $-2 < x \leq 2$ |
| $x \in [0, \to \rangle$ | $0 \leq x$ |
| $x \in \langle \gets, -3\rangle$ | $x < -3$ |
| $x \in \langle 1, 4\rangle$ | $1 < x < 4$ |
| $x \in [2, 5\rangle$ | $2 \leq x < 5$ |
| $x \in \langle -5, \to \rangle$ | $-5 < x$ |
| $x \in \langle \gets, 2\rangle$ | $x < 2$ |
```

```{admonition} Underveisoppgave 3
:class: note
Skriv om ulikhetene under som intervaller:

| Ulikhet | Intervall |
|:---:|:---:|
| $-1 \leq x \leq 1$ | |
| $-3 < x \leq 4$ | |
| $-6 \leq x$ | |
| $x < -7$ | |
| $-2 < x < 1$ | |
| $3 \leq x < 8$ | |
| $13 < x$ | |
| $x < -17$ | |
```

```{dropdown} Løsning
| Ulikhet | Intervall |
|:---:|:---:|
| $-1 \leq x \leq 1$ | $x \in [-1, 1]$ |
| $-3 < x \leq 4$ | $x \in \langle -3, 4]$ |
| $-6 \leq x$ | $x \in [-6, \to \rangle$ |
| $x < -7$ | $x \in \langle \gets, -7\rangle$ |
| $-2 < x < 1$ | $x \in \langle -2, 1\rangle$ |
| $3 \leq x < 8$ | $x \in [3, 8\rangle$ |
| $13 < x$ | $x \in \langle 13, \to \rangle$ |
| $x < -17$ | $x \in \langle \gets, -17\rangle$ |
```



