

## Grafisk representasjon av lineære funksjoner
Vi tenker oss at vi har en linje $f(x) = 2x - 4$. Hvordan kan vi representere denne linja grafisk?
Sagt på en annen måte, hvordan ser grafen til linja ut? For å svare på dette, går vi via en verditabell til et koordinatsystem.


### Fra verditabell til koordinatsystem

En måte å finne ut hvordan grafen til linja ser ut er å sette opp en verditabell for ulike verdier av $x$. 
Vi bruker formelen $y = 2x - 4$ til å regne ut hvilken $y$-verdier som svarer til en $x$-verdi.

Under kan vi se en verditabell for linja $y = 2x - 4$:

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | $-4$ | $-2$ | $0$ | $2$ | $4$ |

Vi kan tegne opp punktene fra verditabellen i et koordinatsystem. 


````{admonition} Påminnelse: Koordinatsystemet
:class: dropdown, tip

Det *kartesiske* koordinatsystemet får vi ved å lage oss to tallinjer som står $90^\circ$ på hverandre, der null på hver tallinje ligger på samme sted. Vi kaller dette punktet for *origo*, og det har koordinatene $(0, 0)$.

Den vannrette linja kaller vi oftest $x$-aksen. Et annet navn for aksen er *førsteaksen*.
Den loddrette linja kaller vi $y$-aksen. Et annen navn for denne aksen er *andreaksen*. 
Hvis vi har et punkt $(x, y)$ i koordinatsystemet, betyr det at vi går $x$ enheter langs $x$-aksen og $y$ enheter langs $y$-aksen fra origo. For eksempel betyr $(3, 2)$ at vi først flytter oss 3 plasser langs $x$-aksen og deretter 2 plasser langs $y$-aksen. Da står vi på punktet $(3, 2)$. Se figuren under: 

```{figure} ./figurer/eksempler/koordinatsystem.svg
:name: koordinatsystem
:width: 80%

Figuren viser et eksempel på et koordinatsystem der punktet $(3, 2)$ er markert. For å lese av $x$-koordinaten, trekker vi en linje fra punktet normalt ned på $x$-aksen. For å lese av $y$-koordinaten, trekker vi en linje fra punktet normalt bort på $y$-aksen.
```
````

Ut ifra verdiene vi har fra verditabellen, kan vi tegne opp punktene i et koordinatsystem, og så trekker vi rette linjer mellom punktene. Da får vi en grafisk representasjon av linja $y = 2x - 4$ ut ifra verditabellen.

**Prøv å tegne linja i et koordinatsystem for hånd før du ser på fasiten under!**

````{admonition} Grafisk representasjon av $y = 2x - 4$
:class: dropdown

```{figure} ./figurer/eksempler/eksempel_rett_linje.svg
:name: rett_linje_eksempel
:width: 80%

Figuren viser grafen til $y = 2x - 4$ i et koordinatsystem der vi har tegnet inn punktene fra verditabellen og trukket linjer mellom punktene. Vi har også latt linja fortsette utenfor punktene for å vise hvordan linja ser ut.
```

````



## Algebraisk representasjon av skrå linjer
Først bør vi se på en algebraisk definisjon av en skrå linje. 

````{admonition} Algebraisk definisjon av skrå linjer
:class: tip

En skrå linje kan alltid skrives på formen

$$
y = ax + b
$$

der $a$ er *stigningstallet* og $b$ er skjæringen til linja med $y$-aksen. Konstanten $b$ kalles ofte også for konstantleddet eller $y$-skjæringen. 
````

````{admonition} Underveisoppgave

Bestem stigningstallet og skjæringen med $y$-aksen til linjene
1. $y = 3x - 1$
2. $y = -2x + 4$
3. $y = -x + 2$
````

````{admonition} Løsning
:class: solution, dropdown

1. For linja $y = 3x - 1$ er stigningstallet $a = 3$ og skjæring med $y$-aksen $b = -1$.
2. For linja $y = -2x + 4$ er stigningstallet $a = -2$ og skjæringen med $y$-aksen $b = 4$.
3. For linja $y = -x + 2$ har stigningstallet $a = -1$ og skjæringen med $y$-aksen $b = 2$.
````

## Fra graf til algebraisk uttrykk
Hvis kjenner grafen til en rett linje, hvordan kan vi da finne et algebraisk uttrykk for linja? 
Sagt på en annen måte, hvordan finner vi en formel $y = ax + b$ for linja?

Vi tar utgangspunkt i grafen under.

```{figure} ./figurer/eksempler/fra_graf_til_formel.svg
:name: graf_til_formel
:width: 80%

Figuren viser grafen til en skrå linje i et koordinatsystem. Men hva er likningen til linja? 

```

### Stigningstallet $a$
En måte å finne stigningstallet $a$ på, er å se hvor mye $y$-verdien endrer seg når vi øker verdien til $x$ med én. 
Hvis vi ser på grafen i {numref}`graf_til_formel`, ser vi at når vi går fra $x = 0$ til $x = 1$, går $y$-verdien fra $y = 3$ til $y = 1$. Endringen i $y$-verdien er $-2$. Dermed er stigningstallet $a = -2$. 

Men kan det tenkes at det er en mer generell måte å finne stigningstallet på?

````{margin}
```{admonition} Forklaring av notasjon
Betydningen av $\Delta x$
: Notasjonen leses som "delta"-$x$. Vi tenker på dette enten som avstanden mellom to punkter på $x$-aksen, eller som endringen i        $x$-verdi.

Betydningen av $\Delta y$
: Notasjonen leses som "delta"-$y$. Vi tenker på dette enten som avstanden mellom to punkter på $y$-aksen, eller som endringen i $y$-verdi.
```
````

`````{admonition} Generell formel for stigningstallet (topunktsformelen)
:class: tip
For en skrå linje på formen $y = ax + b$, og to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på linja, kan vi finne stigningstallet $a$ ved

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} ,
$$ (eq:stigningstall)

der $\Delta y = y_2 - y_1$ og $\Delta x = x_2 - x_1$. <br>


Stigningstallet forteller oss hvor mye $y$-verdien endrer seg i _forhold_ til $x$-verdien. En endring $\Delta x$, gir en endring 

$$
\Delta y = a\Delta x
$$

i $y$-verdien. Dersom $\Delta x = 1$, kan vi se at endringen i $y$-verdien blir 

$$
\Delta y = a\underbrace{\Delta x}_{=1} = a
$$ 

Vi kan derfor tolke stigningstallet som endringen i $y$-verdi dersom vi endrer $x$-verdien med én.

Figuren viser en geometrisk illustrasjon av formelen for stigningstallet.

```{figure} ./figurer/eksempler/stigningstall.svg
:name: stigningstall
:width: 80%

Figuren viser grafen til en skrå linje i et koordinatsystem der to punkter $(x_1, y_1)$ og $(x_2, y_2)$ ligger på linja.
Endringene i $x$-verdi og $y$-verdi er representert som striplete linjer. Lengden av den striplete linjen parallell med $x$-aksen er $\Delta x = x_2 - x_1$ og lengden av den striplete linjen parallell med $y$-aksen er $\Delta y = y_2 - y_1$.
```

````{admonition} Forklaring av formelen
:class: dropdown
Vi tenker oss linja $y = ax + b$ og to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på linja. Hvis vi regner ut endringen i $y$-verdi med formelen får vi:

$$
\Delta y = y_2 - y_1 = (ax_2 + b) - (ax_1 + b) = ax_2 - ax_1 = a(x_2 - x_1) = a\Delta x
$$

Dermed har vi at 

$$
a\Delta x = \Delta y
$$

Snur vi om på formelen ved å dele med $\Delta x$ på begge sider, får vi

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}
$$

Dette er likning {eq}`eq:stigningstall`, så vi har vist det vi skulle.
````

`````

````{admonition} Eksempel 1: Finne likningen for linja i Fig 5.
:class: eksempel
Vi tar utgangspunkt i {numref}`graf_til_formel` og ser på linja i figuren. Vi har to punkter $(x_1, y_1) = (0, 3)$ og $(x_2, y_2) = (1, 1)$ på linja. Da kan vi finne stigningstallet ved å bruke formelen for stigningstallet {eq}`eq:stigningstall`:

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{1 - 3}{1 - 0} = \frac{-2}{1} = -2
$$

Videre ser vi at linja skjærer $y$-aksen i $y = 3$, så betyr at konstantleddet $b = 3$. Dermed har vi at likningen til linja er 

$$
y = ax + b = -2x + 3.
$$

````


````{admonition} Eksempel 2: Finne stigningstallet
:class: eksempel
Vi tenker oss en linje der vi kjenner til to punkter på linja, $(1, 3)$ og $(2, 1)$. Hva er stigningstallet til linja?

**Prøv å finne stigningstallet før du ser på løsningen under**! 

```{admonition} Løsning
:class: solution, dropdown
Vi kjenner til to punkter $(1, 3)$ og $(2, 1)$ på linja. Vi kan la 

$$
(x_1, y_1) = (1, 3) \quad \text{og} \quad (x_2, y_2) = (2, 1). 
$$

Vi bruker formelen fra likning {eq}`eq:stigningstall` for å finne stigningstallet:

$$
a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{1 - 3}{2 - 1} = \frac{-2}{1} = -2.
$$

Altså er stigningstallet $a = -2$. 
```

````


Likning {eq}`eq:stigningstall` gir oss en generell formel for å finne stigningstallet til en linje når vi kjenner til to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på linja. Men hva skal til for at vi skal bestemme formelen for linja fullstendig? 


## Bestemme formelen for linja

For å bestemme formelen $y = ax + b$ for linja, må vi enten:
1. Kjenne til stigningstallet og skjæringen med $y$-aksen.
2. Kjenne til to punkter på linja.
3. Kjenne til stigningstallet $a$ og ett punkt på linja.

Vi skal i det følgende se ett eksempel på hvert tilfelle.

```{admonition} Eksempel 3 (formelen når vi kjenner stigningstallet og skjæring med $y$-aksen)
:class: eksempel
En skrå linje har stigningstall $3$ og skjærer $y$-aksen i $y = -3$. Bestem formelen for linja.

**Løsning**: <br>
Generelt er formelen for linja $y = ax + b$. Siden stiningstallet til linja er $3$, vet vi at $a = 3$. Siden linja skjærer $y$-aksen i $y = -3$, vet vi at $b = -3$. Derfor er formelen for linja 

$$
y = 3x - 3.
$$
```

````{admonition} Eksempel 4 (formelen når vi kjenner til to punkter på linja)
:class: eksempel
En rett linje går gjennom punktene $(2, 3)$ og $(4, 7)$. Bestem formelen for linja.

**Løsning**: <br>
Vi går ut ifra formelen $y = ax + b$. Da kan vi bestemme formelen for linja i to steg:

Steg 1: Bestemme stigningstallet
: For å gjøre regningen enklest mulig, starter vi med å bestemme stigningstallet. Vi kjenner to punkter $(x_1, y_1) = (2, 3)$ og $(x_2, y_2) = (4, 7)$. Vi kan dermed bruke formelen for stigningstallet:

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{7 - 3}{4 - 2} = \frac{4}{2} = 2
$$

Steg 2: Bestemme skjæringen med $y$-aksen
: Når vi har stigningstallet, kan vi bruke ett av punktene til å bestemme skjæringen med $y$-aksen (konstantleddet $b$). Vi kan for eksempel bruke punktet $(x_1, y_1) = (2, 3)$, så må vi løse en likning for $b$ ved å sette inn $x$-verdien og $y$-verdien i likningen 

$$
y = 2x + b
$$

Vi setter inn $x = 2$ og $y = 3$, og løser likningen vi får for $b$:

$$
3 = 2\cdot 2 + b \quad \Leftrightarrow \quad 3 = 4 + b \quad \Leftrightarrow \quad b = 3 - 4 = -1
$$

Dermed er likningen for linja

$$
y = 2x - 1
$$
````

```{admonition} Underveisoppgave
:class: note
Bestem konstantleddet $b$ fra ekempel 2 ved å bruke punktet $(4, 7)$ i stedet og vis at du kommer fram til samme formel for linja.
```

```{dropdown} Løsning
Vi vet at linja er på formen $y = 2x + b$. Vi bruker punkter $(x_2, y_2) = (4, 7)$ og setter inn $x = 4$ og $y = 7$ i likningen og løser for $b$:

$$
7 = 2\cdot 4 + b \quad \Leftrightarrow \quad 7 = 8 + b \quad \Leftrightarrow \quad b = 7 - 8 = -1
$$

Dermed blir formelen for linja 

$$
y = 2x - 1.
$$

```

Før vi går løs på neste eksempel, må vi komme fram til en formel for en skrå linje når vi bare kjenner til ett punkt. 

````{admonition} Ettpunktsformelen for en skrå linje
:class: tip
Hvis vi kjenner stigningstallet $a$ og ett punkt $(x_1, y_1)$ på linja, så er formelen for linja gitt ved 

$$
y - y_1 = a(x - x_1)
$$

```{admonition} Forklaring av formelen
:class: note, dropdown

For å komme fram til formelen starter vi fra formelen for stigningstallet til en rett linje:

$$
a = \frac{y_2 - y_1}{x_2 - x_1}
$$

Siden $a$ er konstant, spiller det ingen rolle hvilke to punkter $(x_1, y_1)$ og $(x_2, y_2)$ vi bruker så lenge de er *forskjellige*. Derfor kan vi velge oss et bestemt punkt $(x_1, y_1)$ på linja og et annet helt vilrkålig punkt $(x, y)$ på linja. Vi kan derfor la $(x, y)$ være et punkt som varierer så lenge $(x, y) \neq (x_1, y_1)$. Da får vi i stedet 

$$
a = \frac{y - y_1}{x - x_1} \quad \Leftrightarrow \quad y - y_1 = a(x - x_1)
$$

Dermed har vi vist hvordan vi kommer fram til ettpunktsformelen for en skrå linje.
```
````

```{admonition} Eksempel 5 (formelen når vi kjenner stigningstallet og ett punkt på linja - ettpunktsformelen)
:class: eksempel

Et skrå linje har stigningstall $2$ og går gjennom punktet $(4, 1)$. Bestem formelen for linja. 

**Løsning**: <br>
Vi bruker ettpunktsformelen $y - y_1 = a(x - x_1)$ der $(x_1, y_1) = (4, 1)$ og stigningstallet er $a = 2$. Da får vi

$$
y - 1 = 2(x - 4) \quad \Leftrightarrow \quad y - 1 = 2x - 8 \quad \Leftrightarrow \quad y = 2x - 7.
$$

Dermed er formelen for linja $y = 2x - 7$.
```

## Oppsummering
I denne seksjonen har vi sett følgende:

```{admonition} Oppsummering: viktige sammenhenger
:class: summary

Algebraisk uttrykk for en skrå linje
: $$y = ax + b$$

Formel for stigningstallet (topunktsformelen)
: $$a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

Ettpunktsformelen for en skrå linje
: $$y - y_1 = a(x - x_1)$$
```


## Oppgaver


### Level 1 🔥

#### Oppgave 1 
Under vises et interaktivt plott av en linje $y = ax + b$. Du kan endre på stigningstallet $a$ og konstantleddet $b$. 

Bruk det interaktive plottet til å bestemme ulike linjer (én linje for hvert punkt i lista) som:
1. Har stigningstall $a = 2$ og konstantledd $b = -4$. Bestem hvor grafen til linja skjærer $x$-aksen og $y$-aksen ved hjelp av den grafiske framstillingen.
2. Skjærer $y$-aksen i $y = 2$ og skjærer $x$-aksen i $x = 1$. 
3. Går gjennom punktene $(1, 3)$ og $(-4, -2)$

```{raw} html
:file: ./figurer/interaktive_plot/skrå_linjer_interaktiv.html
```


#### Oppgave 2

I denne oppgaven skal du tegne grafen til linja $y = x - 2$ i et koordinatsystem ved å bruke en verditabell.

##### Oppgave 2a
Fyll ut verditabellen under for linja $y = x - 2$. 

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ |  |  |  |  |  | |

```{admonition} Fasit
:class: solution, dropdown
| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
```

```{admonition} Løsning
:class: solution, dropdown
Først må vi regne ut $y$-verdiene for de ulike $x$-verdiene. Vi setter inn $x$-verdiene i formelen $y = x - 2$:

For $x = -2$:

$$
y = (-2) - 2 = -4
$$

For $x = -1$:

$$
y = (-1) - 2 = -3
$$

For $x = 0$:

$$
y = 0 - 2 = -2
$$

For $x = 1$:

$$
y = 1 - 2 = -1
$$

For $x = 2$:

$$
y = 2 - 2 = 0
$$

For $x = 3$:

$$
y = 3 - 2 = 1
$$

Dermed får vi verditabellen:

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
```

##### Oppgave 2b
Tegn grafen til linja $y = x - 2$ i et koordinatsystem ved å bruke verditabellen fra 1a.

````{admonition} Løsning
:class: solution, dropdown
```{figure} ./figurer/oppgaver/oppgave_1.svg
:name: rett_linje_oppgave_1b
:width: 80%

Figuren viser grafen til $y = x - 2$ i et koordinatsystem der vi har tegnet inn punktene fra verditabellen og trukket linjer mellom punktene. Vi har også latt linja fortsette utenfor punktene for å vise hvordan linja ser ut.
```

````

#### Oppgave 3

````{margin} 
```{admonition} Sentrale formler
:class: tip, dropdown
Algebraisk uttrykk for en skrå linje
: $$y = ax + b$$

Formel for stigningstallet
: $$a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$
```
````


Bestem formlene for de rette linjene i grafen som vises under. 

```{figure} ./figurer/oppgaver/oppgave_2.svg
:name: rett_linje_oppgave_2
:width: 80%
```


```{admonition} Fasit
:class: solution, dropdown

Den grønne linja har formelen 

$$
y = 2x - 3.
$$

Den lilla linja har formelen 

$$
y = -\frac{1}{2}x + 1.
$$
```

```{admonition} Løsning
:class: solution, dropdown
For å bestemme formelen for den grønne linja, kan vi lese av to punkter på grafen for å bestemme stigningstallet.
Vi kan se at punktene $(0, -3)$ og $(3, 3)$ ligger på linja. Dermed blir stigningstallet

$$
a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{3 - (-3)}{3 - 0} = \frac{6}{3} = 2.
$$

Vi kan lese av at grafen skjærer $y$-aksen i $y = -3$. Dermed er $b = -3$. Derfor er formelen for den grønne linja

$$
y = 2x - 3.
$$

For den lilla linja kan vi lese av at punktene $(0, 1)$ og $(2, 0)$ ligger på linja. Dermed blir stigningstallet til linja

$$
a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{0 - 1}{2 - 0} = \frac{-1}{2} = -\frac{1}{2}.
$$

Vi kan lese av at grafen skjærer $y$-aksen i $y = 1$. Dermed er $b = 1$. Derfor er formelen for den lilla linja

$$
y = -\frac{1}{2}x + 1
$$
```

### Level 2 🔥🔥

#### Oppgave 4
Bestem formelen for linja som går gjennom $(-1, 2)$ og $(3, -1)$. 

````{admonition} Løsning
:class: solution, dropdown
Steg 1: bestemme stigningstallet
: Vi bruker topunktsformelen for stigningstallet der $(x_1, y_1) = (-1, 2)$ og $(x_2, y_2) = (3, -1)$:

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{(-1) - 2}{3 - (-1)} = \frac{-3}{4}
$$

Steg 2: bestemme skjæringen med $y$-aksen
: Vi kan nå sette inn én av de to punktene i formelen for den skrå linja. Her velger vi $(x_1, y_1) = (-1, 2)$. Formelen for linja vår er

$$
y = -\frac{3}{4}x + b
$$

Setter vi inn $x = -1$ og $y = 2$ får vi:

$$
2 = -\frac{3}{4}\cdot (-1) + b \quad \Leftrightarrow \quad 2 = \frac{3}{4} + b \quad \Leftrightarrow \quad b = 2 - \frac{3}{4} = \frac{8}{4} - \frac{3}{4} = \frac{5}{4}
$$

Dermed er formelen for linja gitt ved 

$$
y = -\frac{3}{4}x + \frac{5}{4}.
$$
````

#### Oppgave 5
Bestem likningen for linja som har stigningstall $-3$ og går gjennom punktet $(2, 1)$.

```{dropdown} Hint
Bruk ettpunktsformelen!
```

```{admonition} Løsning
:class: solution, dropdown

Vi bruker ettpunktsformelen for å bestemme formelen for linja. Vi har at $(x_1, y_1) = (2, 1)$ og $a = -3$. Da får vi

$$
y - y_1 = a(x - x_1).
$$

Setter vi inn at $x_1 = 2$ og $y_1 = 1$ og $a = -3$ får vi:

$$
y - 1 = (-3)\cdot (x - 2),
$$

som gir

$$
y - 1 = -3x + 6.
$$

Altså er likningen for linja

$$
y = -3x + 7.
$$
```


#### Oppgave 6
Linja som er vist i figuren under har stigningstall $-2$ og går gjennom to punkter $(x_1, 1)$ og $(2, -1)$.

Bestem verdien til $x_1$.

```{figure} ./figurer/oppgaver/oppgave_6.svg
:name: oppgave_6
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown

Vi vet at stigningstallet til linja er $a = -2$. Videre kjenner vi ett punkt på linja, nemlig $(2, -1)$, så vi kan bruke ettpunktsformelen for å bestemme likningen til linja:

$$
y - (-1) = -2\cdot (x - 2),
$$

som gir 

$$
y + 1 = -2x + 4,
$$

som gir 

$$
y = -2x + 3.
$$

Når $x = x_1$, så er $y = 1$. Dermed får vi likningen

$$
1 = -2x_1 + 3 \quad \Leftrightarrow \quad -2x_1 = 1 - 3 = -2. 
$$

For at $-2x_1 = -2$, må derfor $x_1 = 1$.

```


#### Oppgave 7
En linje har stigningstall $4$ og går gjennom punktet $(-3, 2)$. Bestem hvor linja skjærer $y$-aksen.


```{admonition} Løsning
:class: solution, dropdown

Linja har stigningstall $a = 4$ og går gjennom punktet $(x_1, y_1) = (-3, 2)$. Vi kan dermed bruke ettpunktsformelen for å bestemme likningen til linja

$$
y - y_1 = a(x - x_1)
$$

som gir 

$$
y - 2 = 4(x - (-3)) = 4(x + 3) = 4x + 12.
$$

Vi kan skrive om likninga til 

$$
y = 4x + 14.
$$

Vi kan lese av at linja skjærer $y$-aksen i $y = 14$ (fra konstantleddet, eller ved å sette inn $x = 0$ i likningen).
```



#### Oppgave 8
En elev prøver å bestemme likningen til en linje ut ifra to punkter på linja. 

````{code-block} python
:emphasize-lines: 12, 13
# Punkt (x1, y1)
x1 = -2
y1 = 2

# Punkt (x2, y2)
x2 = 4
y2 = 5

dy = y2 - y1
dx = x2 - x1

a = NotImplemented
b = NotImplemented

print(f"Formelen for linja er y = {a}x + {b}")
````

##### Oppgave 8a

Hva må stå på de uthevede linjene for at programmet skal gi riktig utskrift?
Hva blir utskriften av programmet da?

````{admonition} Fasit
:class: solution, dropdown

På linja 12 kan det stå `a = dy / dx`{l=python} og på linje 13 kan det stå `b = y1 - a * x1`{l=python} eller `b = y2 - a * x2`{l=python}.
````


````{admonition} Løsningsforslag
:class: solution, dropdown

Vi tar for oss linje 12 først. Vi vet at stigningstallet $a$ er endringen i $y$-verdi delt på endringen i $x$-verdi. Vi kan se at $\Delta y = y_2 - y_1$ regnes ut i programmet som `dy = y2 - y1`{l=python} og $\Delta x$ regnes ut i programmet som `dx = x2 - x1`{l=python}. Dermed må vi skrive `a = dy / dx`{l=python} for å regne ut stigningstallet på linje 12.

På linje 13 skal vi finne skjæringen med $y$-aksen. For en linje betyr dette å bestemme $b$ i formelen $y = ax + b$. Vi kan ta utgangspunkt i punktet $(x_1, y_1)$ for å bestemme $b$:

$$
y_1 = ax_1 + b \quad \Leftrightarrow \quad b = y_1 - ax_1
$$

eller vi kan ta utgangspunkt i $(x_2, y_2)$:

$$
y_2 = ax_2 + b \quad \Leftrightarrow \quad b = y_2 - ax_2
$$

Derfor kan det stå `b = y1 - a * x1`{l=python} eller `b = y2 - a * x2`{l=python} på linje 13.

````

##### Oppgave 8b
Bestem hva som skrives ut av programmet.

````{admonition} Fasit
:class: dropdown, solution
```console
Formelen for linja er y = 0.5x + 3
```
````

````{admonition} Løsningsforslag
:class: dropdown, solution
Stigningstallet som regnes ut av programmet er 

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{5 - 2}{4 - (-2)} = \frac{3}{6} = \frac{1}{2} = 0.5
$$

Kontantleddet $b$ kan vi finne ved å sette inn $a = 1$ og $(x_1, y_1) = (-2, 2)$ i formelen $y = ax + b$:

$$
2 = \frac{1}{2}\cdot (-2) + b  \quad \Leftrightarrow \quad b = 2 + 1 = 3
$$

Dermed blir formelen for linja som skrives ut 

$$
y = \frac{1}{2}x + 3 = 0.5x + 3
$$

På datamaskin, representeres tall som desimaltall og ikke som brøk. Derfor får vi at utskriften blir

```console
Formelen for linja er y = 0.5x + 3
```

````

##### Oppgave 8c 
Gjør nødvendige endringer av programmet og prøv det ut med punktene for den rette linja fra fra eksempel 3. <br>
Blir utskriften som forventet?

````{admonition} Løsning
:class: solution, dropdown

Vi må bytte ut $(x_1, y_1) = (2, 3)$ og $(x_2, y_2) = (4, 7)$ i programmet. Vi får da

```{code-block} python
# Punkt (x1, y1)
x1 = 2
y1 = 3

# Punkt (x2, y2)
x2 = 4
y2 = 7

dy = y2 - y1
dx = x2 - x1

a = dy / dx
b = y1 - a * x1

print(f"Formelen for linja er y = {a}x + {b}")
```
som gir utkriften
```console
Formelen for linja er y = 2.0x + -1.0
```
Så vi får samme formel som i eksempel 3.
````