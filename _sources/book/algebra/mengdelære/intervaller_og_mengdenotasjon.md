# Mengder som intervaller, ulikheter og lister

```{admonition} Læringsmål: intervaller, ulikheter og listenotasjon
:class: tip
Etter du har gått gjennom denne seksjonen skal du:
* Kunne beskrive mengder ved hjelp av intervaller.
* Kunne beskrive mengder ved hjelp av ulikheter.
* Kunne beskrive mengder ved hjelp av listenotasjon.
```

Noen ganger ønsker vi å beskrive en mengde tall på en kort og presis måte. Vi skal se på tre forskjellige måter å skrive mengder på her:

Intervaller
: Hvis en mengde består av en eller flere sammenhengende deler av tallinja, kan vi uttrykke mengdene som intervaller.

Ulikheter
: Vi kan også bruke ulikheter til å uttrykke den samme mengden som vi kan uttrykke med intervaller. Ofte veksler vi mellom disse representasjonsformene - så det er viktig å kunne lese og bruke begge representasjonsformer.

Listenotasjon
: Noen ganger vil ikke en mengde bestå av sammenhengende deler på tallinja, men utvalgte tall. Mengden trenger ikke engang å bestå av tall, men kan bestå av utvalgte punkter. Da er listenotasjon en nyttig representasjonsform.

I dette delkapittelet skal du lære om de tre representasjonsformene for mengder.


## Intervaller
Noen ganger ønsker vi å beskrive en mengde reelle tall på tallinja på en kort og presis måte. Dersom vi ønsker å beskrive én eller flere sammenhengende deler av tallinja, kan vi bruke **intervaller**.  
Her skal vi bare se på én del av tallinja - senere skal vi se på hvordan vi kan beskrive flere deler av tallinja samtidig.

I tabellen under vises de vanligste måtene å uttrykke intervaller på. Les forklaringene i tabellen **nøye**:

```{admonition} Språkbruk for intervaller
:class: note, margin

Merk at når det nedre endepunktet er inkludert, sier vi **fra og med**. Når det ikke er inkludert, sier vi bare **fra**. På samme måte sier vi **til og med** når det øvre endepunktet er inkludert, og **opp til** eller bare **til** når det ikke er inkludert.
```

```{admonition} Alternativ skrivemåte
:class: note, margin

Notasjonen $[a, \to\rangle = [a, \infty\rangle$ og $\langle \gets, b] = \langle -\infty, b]$ er også vanlig, og du kan fritt velge hvilken notasjon du bruker. Vi kommer til å bruke pilene fordi det er så vanlig i matematikken på videregående skole. 
```

| Notasjon | Type intervall | Forklaring | Eksempel |
| :---: | :---: | --- | --- |
| $[a, b]$ | **Lukket** | Alle tall fra og med $a$ til og med $b$. | $[2, 5]$ betyr mengden av reelle tall fra og med $2$ til og med $5$. Både $2$ og $5$ er inkludert.|
| $\langle a, b\rangle$ | **Åpent** | Alle tall fra $a$ til $b$, men $a$ og $b$ er *ikke* inkludert. | $\langle1, 4\rangle$ betyr mengden av reelle tall fra $1$ opp til $4$, men $1$ og $4$ er ikke inkludert.|
| $\langle a, b]$ | **Halvåpent** | Alle tall fra $a$ opp til og med $b$. | $\langle -1, 3]$ betyr mengden av alle reelle tall fra $-1$ opp til og med $3$. $-1$ er *ikke* inkludert, men $3$ er inkludert. |
| $[a, b\rangle$ | **Halvåpent** | Alle tall fra og med $a$ til $b$. | $[0, 2\rangle$ betyr mengden av alle reelle tall fra og med $0$ opp til $2$. $0$ er inkludert, men $2$ er ikke. |
| $[a, \to \rangle$ | **Lukket** | Alle tall fra og med $a$ og oppover. | $[3, \to \rangle$ betyr mengden av alle reelle tall fra og med $3$ og oppover. |
| $\langle \gets, b]$ | **Lukket** | Alle tall opp til og med $b$. | $\langle \gets, 2]$ betyr mengden av alle reelle tall opp til og med $2$. |
|$\langle a, \to \rangle$| **Halvåpent** | Alle tall fra $a$ og oppover. | $\langle 0, \to \rangle$ betyr mengden av alle reelle tall fra $0$ og oppover, men $0$ er ikke inkludert. |
|$\langle \gets, b\rangle$| **Halvåpent** | Alle tall opp til $b$. | $\langle \gets, 2\rangle$ betyr mengden av alle reelle tall opp til $2$, men $2$ er ikke inkludert. |

```{admonition} Åpent, halvåpent eller lukket intervall?
:class: discussion, dropdown
Du legger kanskje merke til at når et intervall er åpent er ingen av endepunktene inkludert. Når det er halvåpent er det ene endepunktet inkludert, mens det andre er ikke. Likevel påstår tabellen at $[a, \to \rangle$ er et lukket intervall. Men dette er fordi vi mener at vi inkluderer **alle** tall fra og med $a$ og oppover. En annen måte å skrive dette på er $[a, \infty\rangle$. Men $\infty$ (uendelig) er ikke et punkt, det forteller oss bare at vi aldri stopper å gå oppover tallinja. Notasjonen uttrykker altså at vi inkluderer alle tall over $a$, så da må jo tallmengden være lukket, selv om $\infty$ ikke i seg selv er et tall.
```



````{admonition} Underveisoppgave 1
:class: check

Ta for deg mengdene i tabellen under og bestem type intervall og beskriv tallene som hører til mengdene:

| Mengde | Type intervall | Beskrivelse |
|:---:|:---:|---|
| $[-1, 1]$| | |
| $\langle 0, 3\rangle$| | |
| $\langle -2, 2]$| | |
| $[0, \to \rangle$| | |
| $\langle \gets, -3\rangle$ | | |


```{admonition} Løsning
:class: dropdown, solution
| Mengde | Type intervall | Beskrivelse |
|:---:|:---:|---|
| $[-1, 1]$| Lukket |Alle reelle tall fra og med $-1$ til og med $1$. |
| $\langle 0, 3\rangle$| Åpent | Alle reelle tall fra $0$ opp til $3$. Hverken $0$ eller $3$ er inkludert i mengden. |
| $\langle -2, 2]$| Halvåpent  | Alle reelle tall fra $-2$ opp til og med $2$. Her er $-2$ ekskludert, mens $2$ er inkludert i mengden. |
| $[0, \to \rangle$| Lukket | Alle reelle tall fra og med $0$ og oppover. Her er $0$ inkludert i mengden. |
| $\langle \gets, -3\rangle$ | Halvåpent | Alle reelle tall opp til $-3$. Her er $-3$ ekskludert fra mengden. |
```

````


## Mengder beskrevet som ulikheter

Mengder kan også beskrives med **ulikheter**. Før vi ser på sammenhengen mellom intervaller og ulikheter, trenger vi å forstå litt notasjon som brukes når man uttrykker ulikheter. Les tabellen under **nøye**:


| Ulikhet | Forklaring | Eksempel |
| :---: | --- | --- |
|  $<$ | Mindre enn | $2 < 3$ betyr at $2$ er mindre enn $3$.|
|  $>$ | Større enn enn | $5 > 4$ betyr at $5$ er større enn $4$. |
| $\leq$ | Mindre enn eller lik | $x \leq 3$ betyr at $x$ er mindre enn eller lik $3$.|
| $\geq$ | Større enn eller lik | $x \geq 5$ betyr at $x$ er større enn eller lik $5$.|

For å beskrive en mengde ved hjelp av en ulikhet, introduserer vi en variabel (for eksempel $x$) som oppfyller én eller flere ulikheter. Det vil da være et samsvar mellom et intervall $I$ og en ulikhet. Vi trenger bittelitt mer notasjon for å kunne uttrykke oss presist: 

```{admonition} Sammenheng mellom et lukket intervall $I = [a, b]$ og en ulikhet
:class: theory
Gitt en variabel $x \in I = [a, b]$, vil ulikheten $a \leq x \leq b$ bety akkurat det samme som intervallnotasjonen $I = [a, b]$. 
Vi sier at de to påstandene er **ekvivalente** og skriver

$$
x \in [a, b] \quad \Leftrightarrow \quad a \leq x \leq b
$$

der "$\Leftrightarrow$" betyr at de to utsagnene er ekvivalente. Vi kaller "$\Leftrightarrow$" for et **ekvivalenstegn**. Vi leser dette tegnet som *hvis og bare hvis*. 
```
Vi kan naturligvis utvide skrivemåten til å gjelde for halvåpne og åpne intervaller også.
Les tabellen under **nøye** og overbevis deg selv om at du forstår skrivemåtene:

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


````{admonition} Underveisoppgave 2
:class: check
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

```{admonition} Løsning
:class: dropdown, solution
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
````


````{admonition} Underveisoppgave 3
:class: check
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

```{admonition} Løsning
:class: dropdown, solution
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
````

## Listenotasjon for mengder
Noen kan ikke uttrykkes som intervaller eller ulikheter. I slike tilfeller kan vi ofte bruke **listenotasjon** eller **listeform**. Når en mengde er skrevet på listeform, vil du i de fleste tilfeller kunne *se* hvilke elementer som er i mengden, eller så vil det være et mønster som repetererer seg. 

```{admonition} Ellipse (...)
:class: note, margin
Vi skriver $...$ (kalles for en *ellipse*) når vi vil indikere at et mønster gjentar seg. Hvis det ikke følger noe etter ellipsen, betyr det at mønsteret gjentar seg for alltid. Hvis det følger noe etter ellipsen, betyr det at mønsteret gjentar seg opp til det tallet.
```

```{admonition} Definisjon: Listeform
:class: theory
En mengde $L$ kan skrives på listeform dersom mengden er en såkalt **tellbar** mengde. Notasjonen vi bruker for dette ser slik ut:

$$
L = \{\text{element 1}, \text{element 2}, \text{element 3}, \ldots\}
$$
```

I tabellen under følger eksempler på mengder skrevet på listeform. Les eksemplene i tabellen **nøye** og overbevis deg om du forstår skrivemåten:

```{admonition} Rekkefølgen spiller ingen rolle
:class: note, margin
Merk at *rekkefølgen* på elementene i en mengde skrevet på listeform er *ubetydelig*. Noen ganger er det naturlig å stille dem i stigende rekkefølge, men det er slettes ikke nødvendig.
```

| Mengde | Forklaring |
|:---|:---|
| $\{1, 2, 3, 4, 5\}$ | Mengden av de fem første naturlige tallene. |
| $\{1, 3, 5, 7, 9, \ldots, 21\}$ | Mengden av alle positive oddetall opp til og med $21$. |
| $\{2, 4, 6, 8, 10, \ldots\}$ | Mengden av alle positive partall. |
| $\{1, 4, 9, 16, 25, \ldots\}$ | Mengden av kvadrattallene. |
| $\{1, 2, 4, 8, 16, 32, \ldots\}$ | Mengden av potenser av $2$. |
| $\mathbb{N} = \{1, 2, 3, \ldots\}$| Mengden av naturlige tall. |
| $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$ | Heltallene. |
|$\{(1, 2), (-3, 4), (0, 0)\}$| Mengden bestående av punktene $(1, 2)$ og $(-3, 4)$ og $(0, 0)$.|

Som du kan se fra tabellen, så er det mange tilfeller hvor denne notasjonen vil være nyttig for å beskrive mengder. 
Nå skal du teste deg selv for å sjekke at du har forstått notasjonen.

````{admonition} Underveisoppgave 4
:class: check
Skriv om mengdene under til listeform:

| Mengde | Listeform |
|:---|:---|
| De naturlige tallene fra og med $5$ til og med $8$ | |
| De negative partallene | |
| Oddetallene fra $3$ til og med $7$ | |
| De positive kubikktallene | |
| Mengden som består av punktene $(1, 2)$ og $(-1, 1)$ | |
| Mengden som består av tallene $-1$, $1$ og $3$ | |

```{admonition} Løsning
:class: dropdown, solution
| Mengde | Listeform |
|:---|:---|
| De naturlige tallene fra og med $5$ til og med $8$ | $\{5, 6, 7, 8\}$ |
| De negative partallene | $\{-2, -4, -6, \ldots\}$ eller $\{\ldots, -6, -4, -2\}$ |
| Oddetallene fra $3$ til og med $7$ | $\{3, 5, 7\}$ |
| De positive kubikktallene | $\{1, 8, 27, 64, \ldots\}$ eller $\{1^3, 2^3, 3^3, 4^3, \ldots\}$ |
| Mengden som består av punktene $(1, 2)$ og $(-1, 1)$ | $\{(1, 2), (-1, 1)\}$ |
| Mengden som består av tallene $-1$, $1$ og $3$ | $\{-1, 1, 3\}$ |
```
````







