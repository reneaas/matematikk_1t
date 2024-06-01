# Algebraisk og grafisk representasjon av skrå linjer

En representasjon er en måte å uttrykke noe på. Når vi jobber med rette linjer, er de to vanligste måtene å representer linjer på algebraisk og grafisk. Med algebraisk representasjon, mener vi en formel som beskriver linja. Med grafisk representasjon, mener vi en tegning av linja i et koordinatsystem.

---

## Grafisk representasjon av linjer
Vi tenker oss at vi har en linje $y = 2x - 4$. Hvordan kan vi representere denne linja grafisk?
Sagt på en annen måte, hvordan ser grafen til linja ut? For å svare på dette, går via en verditabell til et koordinatsystem.

### Fra verditabell til koordinatsystem

En måte å finne ut hvordan grafen til linja ser ut er å sette opp en verditabell for ulike verdier av $x$. 
Vi bruker formelen $y = 2x - 4$ til å regne ut hvilken $y$-verdier som svarer til en $x$-verdi.

Under kan vi se en verditabell for linja $y = 2x - 4$:

| $x$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| --- | --- | --- | --- | --- | --- |
| $y$ | $-4$ | $-2$ | $0$ | $2$ | $4$ |

Vi kan tegne opp punktene fra verditabellen i et koordinatsystem. 


````{admonition} Påminnelse: Koordinatsystemet
:class: dropdown, tip

Det *kartesiske* koordinatsystemet får vi vet å lage oss to tallinjer som står $90^\circ$ på hverandre, der null på hver tallinje ligger på samme sted. Vi kaller dette punktet for *origo*, og det har koordinatene $(0, 0)$.

Den vannrette linja kaller vi oftest $x$-aksen. Et annet navn for aksen er *førsteaksen*.
Den loddrette linja kaller vi $y$-aksen. Et annen navn for denne aksen er *andreaksen*. 
Hvis vi har et punkt $(x, y)$ i koordinatsystemet, betyr det at vi går $x$ enheter langs $x$-aksen og $y$ enheter langs $y$-aksen fra origo. For eksempel betyr $(3, 2)$ at vi først flytter oss 3 plasser langs $x$-aksen og deretter 2 plasser langs $y$-aksen. Da står vi på punktet $(3, 2)$. Se figuren under: 

```{figure} ./figurer/eksempler/koordinatsystem.pdf
:name: koordinatsystem
:width: 80%

Figuren viser et eksempel på et koordinatsystem der punktet $(3, 2)$ er markert. For å lese av $x$-koordinaten, trekker vi en linje fra punktet normalt ned på $x$-aksen. For å lese av $y$-koordinaten, trekker vi en linje fra punktet normalt bort på $y$-aksen.
```
````

Ut ifra verdiene vi har fra verditabellen, kan vi tegne opp punktene i et koordinatsystem, og så trekker vi rette linjer mellom punktene. Da får vi en grafisk representasjon av linja $y = 2x - 4$ ut ifra verditabellen.

**Prøv å tegne linja i et koordinatsystem for hånd før du ser på fasiten under!**

````{admonition} Grafisk representasjon av $y = 2x - 4$
:class: dropdown

```{figure} ./figurer/eksempler/eksempel_rett_linje.pdf
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
:class: 
Bestem stigningstallet og skjæringen med $y$-aksen til linjene
1. $y = 3x - 1$
2. $y = -2x + 4$
3. $y = -x + 2$
````

````{admonition} Løsning
:class: dropdown, note

1. Linja $y = 3x - 1$ har stigningstallet $a = 3$ og skjæringen med $y$-aksen $b = -1$.
2. Linja $y = -2x + 4$ har stigningstallet $a = -2$ og skjæringen med $y$-aksen $b = 4$.
3. Linja $y = -x + 2$ har stigningstallet $a = -1$ og skjæringen med $y$-aksen $b = 2$.
````

## Fra graf til algebraisk uttrykk
Hvis kjenner grafen til en rett linje, hvordan kan vi da finne et algebraisk uttrykk for linja? 
Sagt på en annen måte, hvordan finner vi en formel $y = ax + b$ for linja?

Vi tar utgangspunkt i grafen under.

```{figure} ./figurer/eksempler/fra_graf_til_formel.pdf
:name: fra_graf_til_formel
:width: 80%
```

### Stigningstallet $a$
En måte å finne stigningstallet $a$ på, er å se hvor mye $y$-verdien endrer seg når vi går én enhet langs $x$-aksen.
Hvis vi ser på grafen i {numref}`fra_graf_til_formel`, ser vi at når vi går fra $x = 0$ til $x = 1$, går $y$-verdien fra $y = 3$ til $y = 1$. Endringen i $y$-verdien er $-2$. Dermed er stigningstallet $a = -2$. 

Men kan det tenkes at det er en mer generell måte å finne stigningstallet på?

`````{admonition} Generell formel for stigningstallet
:class: tip
For en skrå linje på formen $y = ax + b$, og to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på linja, kan vi finne stigningstallet $a$ ved

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} ,
$$

der $\Delta y = y_2 - y_1$ og $\Delta x = x_2 - x_1$. Figuren under viser formelens betydning grafisk:

```{figure} ./figurer/eksempler/stigningstall.pdf
:name: stigningstall
:width: 80%

Figuren viser en skrå linje i et koordinatsystem der to punkter $(x_1, y_1)$ og $(x_2, y_2)$ er ligger på linja.
Endringene i $x$-verdi og $y$-verdi er representert som striplete linjer. Lengden av den striplete linjen parallell med $x$-aksen er $\Delta x = x_2 - x_1$ og lengden av den striplete linjen parallell med $y$-aksen er $\Delta y = y_2 - y_1$.
```


````{admonition} Bevis for formelen
:class: dropdown
Vi tenker oss linja $y = ax + b$ og to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på linja. Hvis vi regner ut endringen i $y$-verdi med formelen får vi:

$$
\Delta y = y_2 - y_1 = = (ax_2 + b) - (ax_1 + b) = ax_2 - ax_1 = a(x_2 - x_1) = a\Delta x
$$

Dermed har vi at 

$$
a\Delta x = \Delta y
$$

Snur vi om på formelen ved å dele med $\Delta x$ på begge sider, får vi

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}
$$

som var det vi skulle vise.
````

`````


For å bestemme formelen $y = ax + b$ for linja, må vi enten:
1. Kjenne til to punkter på linja.
2. Kjenne til stigningstallet $a$ og ett punkt på linja.
3. Kjenne til stigningstallet og skjæringen med $y$-aksen.


### Bestemme stigningstall og skjæring med $y$-aksen

Kjenner vi grafen til linja, kan vi bestemme stigningstallet $a$ 




## Oppgaver


### Level 1 🔥

#### Oppgave 1

I denne oppgaven skal du tegne grafen til linja $y = x - 2$ i et koordinatsystem ved å bruke en verditabell.

##### Oppgave 1a
Fyll ut verditabellen under for linja $y = x - 2$. 

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| --- | --- | --- | --- | --- | --- | --- |
| $y$ |  |  |  |  |  | |

```{admonition} Fasit
:class: note, dropdown
| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
| --- | --- | --- | --- | --- | --- | --- |
| $y$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
```

```{admonition} Løsning
:class: note, dropdown
Først må vi regne ut $y$-verdiene for de ulike $x$-verdiene. Vi setter inn $x$-verdiene i formelen $y = 3x - 1$:

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
| --- | --- | --- | --- | --- | --- | --- |
| $y$ | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ |
```

##### Oppgave 1b
Tegn grafen til linja $y = 3x - 1$ i et koordinatsystem ved å bruke verditabellen fra 1a.

````{admonition} Fasit
:class: dropdown, note
```{figure} ./figurer/oppgaver/oppgave_1.pdf
:name: rett_linje_oppgave_1b
:width: 80%

Figuren viser grafen til $y = x - 2$ i et koordinatsystem der vi har tegnet inn punktene fra verditabellen og trukket linjer mellom punktene. Vi har også latt linja fortsette utenfor punktene for å vise hvordan linja ser ut.
```

````

#### Oppgave 2

```{margin} Sentrale formler:
<br>

Algebraisk uttrykk for en skrå linje
: $$y = ax + b$$

Formel for stigningstallet
: $$a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$
```


Bestem formlene for de rette linjene i grafen som vises under. 

```{figure} ./figurer/oppgaver/oppgave_2.pdf
:name: rett_linje_oppgave_2
:width: 80%
```


```{admonition} Fasit
:class: dropdown, note

Den grønne linja har formelen 

$$
y = 2x - 3.
$$

Den lilla linja har formelen 

$$
y = -x + 3.
$$
```

```{admonition} Løsning
:class: dropdown, note
For å bestemme formelen for den grønne linja, kan vi lese av to punkter på grafen for å bestemme stigningstallet.
Vi kan se at punktene $(0, -3)$ og $(3, 3)$ ligger på linja. Dermed blir stigningstallet

$$
a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{3 - (-3)}{3 - 0} = \frac{6}{3} = 2.
$$

Vi kan lese av at grafen skjærer $y$-aksen i $y = -3$. Dermed er $b = -3$. Derfor er formelen for den grønne linja

$$
y = 2x - 3.
$$

For den lilla linja kan vi lese av at punkteke $(0, 1)$ og $(2, 0)$ ligger på linja. Dermed blir stigningstallet til linja

$$
a = \frac{y_2 - y_1}{x_2 - x_1} = \frac{0 - 1}{2 - 0} = \frac{-1}{2} = -\frac{1}{2}.
$$

Vi kan lese av at grafen skjærer $y$-aksen i $y = 1$. Dermed er $b = 1$. Derfor er formelen for den lilla linja

$$
y = -\frac{1}{2}x + 1
$$

```




### Level 2 🔥🔥

### Level 3 🔥🔥🔥