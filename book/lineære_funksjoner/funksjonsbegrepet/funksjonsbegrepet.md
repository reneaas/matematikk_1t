# Funksjonsbegrepet

Her skal du få en litt grundigere innføring i funksjonsbegrepet. En funksjon kan noen ganger tenkes på som en graf, andre ganger tenker vi på det som en formel. Vi tenker på formelen og grafen som ulike representasjoner av en mer generell sammenheng som vi kaller for en **funksjon**. 

```{admonition} Læringsmål: funksjonsbegrepet
Etter å ha arbeidet med dette kapittelet er målet at du skal kunne:
* Forklare hva en funksjoner er og hva som skiller en funksjon fra en kurve.
* Forstå begrepene definisjonsmengde og verdimengde til en funksjon.
```


## Funksjon som formel
Når vi har jobbet med rette linjer hittil, har vi brukt formelen for en skrå linje $y = ax + b$, eller vi har jobbet med en graf der vi har punkter $(x, y)$ som ligger på linja. For skrå linjer, er det naturlig å tenke oss at $y$-verdien er bestemt av $x$-verdien når vi jobber med formelen $y = ax + b$. Vi kaller $x$ for den **uavhengige** variabelen, og $y$ for den **avhengige** variabelen. Vi kan tenke på det som at den uavhengige variabelen _bestemmer_ den avhengige variabelen - altså $x$ bestemmer verdien til $y$. Vi sier da at $y$ er en _funksjon_ av $x$. 

````{margin}
```{admonition} En $x$-verdi kan bare gi én $y$-verdi
:class: note
Det er viktig å merke seg at for at en sammenheng mellom $x$ og $y$ skal regnes som en funksjon, kan vi for en verdi av $x$ _kun_ få nøyaktig én $y$-verdi. Dersom vi har flere $y$-verdier for en $x$-verdi, er det ikke en funksjon.
```
````

```{admonition} Funksjon som algebraisk formel
:class: tip
Dersom vi har en uavhengig variabel $x$ og en avhengig variabel $y$, der vi tenker oss at $x$ entydig bestemmer verdien til $y$, så kaller vi sammenhengen mellom dem for en funksjon $f$. I matematikken har vi bestemt at:
* $f$ er **funksjonsnavnet** eller bare _funksjonen_. Vi sier ofte "en funksjon $f$" eller "funksjonen $f$".
* Vi skriver $y = f(x)$ for å understreke at $y$ er en funksjon av $x$. Vi kaller $f(x)$ for **funksjonsverdien** til $f$ for bestemt verdi av $x$.

Vi skriver oftest bare $f(x)$ i stedet for $y = f(x)$. 
```

Ut ifra forklaringen over, kan vi nå skrive en skrå linje $y = ax + b$ ved å sette $y = f(x)$ der vi mener at $f$ er funksjonen som gir oss sammenhengen mellom $x$ og $y$ i formelen. Da får vi

$$
f(x) = ax + b
$$ (eq:lineær_funksjon1)

Vi kaller funksjonen i likning {eq}`eq:lineær_funksjon1` for en **lineær funksjon**.

````{admonition} Underveisoppgave
En lineær funksjon er gitt ved funksjonsuttrykket

$$
f(x) = 3x - 1
$$

1. Bestem $f(0)$. Hva betyr dette?
2. Bestem koordinatene til punktet $(2, f(2))$ på grafen til funksjonen.

**Prøv godt selv før du ser på løsningsforslaget. Det kan hende du bør lese gjennom forklaringene over et par ganger for å forstå den godt.**

```{admonition} Løsning
:class: solution, dropdown
1. For å bestemme $f(0)$, setter vi $x = 0$ i funksjonsuttrykket. Da får vi

    $$
    f(0) = 3 \cdot 0 - 1 = -1
    $$

    Dette betyr at funksjonsverdien til den lineære funksjoen er $y = f(0) = -1$ når $x = 0$.
2. For å bestemme koordinatene til $(2, f(2))$ på grafen, må vi bestemme $y$-verdien $y = f(2)$. Da setter vi $x = 2$ i funksjonsuttrykket. Da får vi

    $$
    f(2) = 3 \cdot 2 - 1 = 5
    $$

    Dermed er punktet $(2, f(2)) = (2, 5)$ på grafen til funksjonen.
```
````



## Funksjon som en graf
Når vi tenker på en funksjon som en graf, så tenker vi på en graf der hver $x$-verdi er tilordnet nøyaktig én $y$-verdi. Til sammen gir dette oss par $(x, y)$ der vi kan tegne en graf. Betingelsen for at det skal være en funksjon, er at det er **kun én** $y$-verdi for hver $x$-verdi. Her også erstatter vi $y = f(x)$ dersom sammenhengen mellom $x$ og $y$ kan beskrives av en funksjon. Da blir et punkt på grafen $(x, y) = (x, f(x))$.

Med betingelsen over, er det derfor sånn at en graf ikke nødvendigvis er en funksjon. 
I {numref}`funksjonsgraf_vs_kurve` under vises et eksempel på to grafer, der kun én av dem representerer en funksjon.

```{figure} ./figurer/eksempler/funksjonsbegrepet/funksjonsgraf_vs_kurve.svg
:name: funksjonsgraf_vs_kurve
:width: 100%

Grafen til venstre viser en funksjon fordi det for _hver_ $x$-verdi finnes nøyaktig én $y$-verdi. Punktene $(x, y)$ definerer derfor en funksjon. Grafen til høyre viser en kurve (en sirkel med radius 2) som _ikke_ er en funksjon fordi det _ikke_ finnes nøyaktig én $y$-verdi for hver $x$-verdi. For eksempel har vi to $y$-verdier for $x = 0$. Dermed kan ikke en sirkel beskrives som en funksjon.
```

````{admonition} Underveisoppgave
Under vises fire grafer. Bestem hvilke av de som representerer en funksjon, og hvilke av de som ikke representerer en funksjon. Begrunn svarene dine.

```{figure} ./figurer/underveisoppgaver/funksjonsbegrepet/funksjonsgraf_vs_kurve_oppgave1.svg
:name: funksjonsgraf_vs_kurve_oppgave1
:width: 90%

Her vises fire grafer $A$, $B$, $C$ og $D$. Men hvilke av de er funksjoner? Hvilke av de er bare kurver?

```{admonition} Løsning
:class: solution, dropdown
I {numref}`funksjonsgraf_vs_kurve_oppgave1` ser vi at graf $A$ bare har én $y$-verdi for hver $x$-verdi, så dette må være en funksjon. 

Graf $B$ har to $y$-verdier for alle $x \in \langle -2, 2 \rangle \setminus \{0\}$, så dette er ikke en funksjon.

Graf $C$ er en rett linje der $x = -1$ har uendelig mange $y$-verdier, så dette er ikke en funksjon heller.

Graf $D$ er en linje $y = -1$ der alle $x$-verdier har samme $y$-verdi. Men hver $x$-verdi har bare én $y$-verdi som betyr at grafen er en funksjon.
```
````



## Definisjon av en funksjon
Vi er nå klare for å oppsummere en definisjon av en funksjon. 

```{admonition} Definisjon: Funksjon
:class: tip
En **funksjon** $f$ er en regel som for _hvert_ element $x \in D_f$ tilordner _nøyaktig én_ funksjonsverdi $f(x) \in V_f$.

Vi kaller $D_f$ for **definisjonsmengden** til $f$ som er mengden av alle $x$-verdier vi kan regne ut en funksjonsverdi $y = f(x)$ med. Vi kaller $V_f$ for **verdimengden** til $f$ som er mengden av alle $y$-verdier som kan regnes ut med $x \in D_f$.
```

Definisjonen over er litt abstrakt, så vi tar utgangspunkt i et konkret eksempel. 

````{admonition} Eksempel 1: Lineær funksjon med definisjonsmengde og verdimengde
:class: eksempel

Vi lar en funksjon $f$ være gitt ved funksjonsuttrykket 

$$
f(x) = 2x + 1, \quad D_f = [-2, 2].
$$

Bestem verdimengden til $f$. 

```{admonition} Løsning
:class: solution, dropdown
Fra funksjonsuttrykket, er definisjonsmengden gitt ved $D_f = [-2, 2]$. Dette betyr at vi bare kan bruke $x \in [-2, 2]$ til å regne ut funksjonsverdier $f(x)$. For å bestemme verdimengden, kan vi regne ut den største og minste mulige verdien vi kan få for $f(x)$ gitt $x \in D_f$. Siden det er en skrå rett linje, er det rimelig å bare se på endepunktene for å finne største og minste verdi:

$$
f(-2) = 2 \cdot (-2) + 1 = -3, \quad f(2) = 2 \cdot 2 + 1 = 5.
$$

Dermed finner vi at verdimengden til $f$ er $V_f = [-3, 5]$. 
```
````

````{admonition} Eksempel 2: En annerledes funksjon
:class: eksempel
Noen ganger har vi en funksjon som ikke kan skrives som en algebraisk formelen. Under vises en funksjon $g$ som er gitt ved 

$$
g(x) = \begin{cases}
1, & \text{hvis } x \in \mathbb{Z}, \\
0, & \text{ellers}.
\end{cases}
$$

Her har vi i stedet en oppskrift på hvordan vi skal regne ut funksjonsverdiene. 

Hva er $g(2)$ og $g(1/2)$?

```{admonition} Løsning
:class: solution, dropdown
$g(2) = 1$ fordi $2 \in \mathbb{Z}$ og $g(1/2) = 0$ fordi $1/2 \notin \mathbb{Z}$.
```
````

### Oppgaver 

#### Oppgave 1

En lineær funksjon er gitt ved

$$
f(x) = 3x - 3, \quad D_f = [-2, 2].
$$

Oppgave 1a
: Bestem $f(0)$. 

```{admonition} Løsning
:class: solution, dropdown
Får å bestemme $f(0)$, setter vi $x = 0$ i funksjonsuttrykket. Da får vi

$$
f(0) = 3\cdot 0 - 3 = -3.
$$
```

Oppgave 1b
: Bestem koordinatene til punktet $(1, f(1))$ på grafen til $f$.

```{admonition} Løsning
:class: solution, dropdown
For å bestemme koordinatene til punktet $(1, f(1))$, må vi bestemme $y$-verdien $y = f(1)$. Da setter vi $x = 1$ i funksjonsuttrykket. Da får vi

$$
f(1) = 3 \cdot 1 - 3 = 0.
$$

Dermed er koordinatet til punktet $(1, f(1)) = (1, 0)$ på grafen til $f$.
```

Oppgave 1c
: Bestem verdimengden til $f$. 

```{admonition} Løsning
:class: solution, dropdown
Får å bestemme verdimengden til $f$, bruker vi at linja er en rett linje som enten alltid stiger eller synker, så vi ser på endepunktene for å finne største og minste verdi. Endepunktene i definisjonsmengden er $x = -2$ og $x = 2$:

$$
f(-2) = 3 \cdot (-2) - 3 = -9, \quad f(2) = 3 \cdot 2 - 3 = 3.
$$

Dermed blir verdimengden til $f$ gitt ved $V_f = [-9, 3]$.
```

#### Oppgave 2

En lineær funksjon er gitt ved 

$$
g(x) = -2x + 4, \quad D_g = [-1, 3].
$$

Oppgave 2a
: Bestem $g(1)$.

```{admonition} Løsning
:class: solution, dropdown
For å bestemme $g(1)$, må vi sette inn $x = 1$ i funksjonsuttrykket:

$$
g(1) = -2 \cdot 1 + 4 = 2.
$$
```

Oppgave 2b
: Bestem koordinatene til punktet $(2, g(2))$ på grafen til $g$.

```{admonition} Løsning
:class: solution, dropdown
For å bestemme koordinatene til punktet, må vi regne ut $y = g(2)$:

$$
g(3) = -2 \cdot 2 + 4 = 0.
$$

Dermed er koordinatene til punktet på grafen gitt ved $(2, g(2)) = (2, 0)$.
```

Oppgave 2c
: Bestem verdimengden til $g$.

```{admonition} Løsning
:class: solution, dropdown
For å bestemme verdimengden til $g$, ser vi funksjonsverdiene til endepunktene i definisjonsmengden som er $x = -1$ og $x = 3$:

$$
g(-1) = -2 \cdot (-1) + 4 = 6, \quad g(3) = -2 \cdot 3 + 4 = -2.
$$

Dermed er verdimengden til $g$ gitt ved $V_g = [-2, 6]$.
```


#### Oppgave 3

En lineær funksjon $h$ er gitt ved 

$$
h(x) = 2x - 6, \quad V_h = [-4, 4].
$$

Oppgave 3a
: Bestem definisjonsmengden $D_h$. 

```{admonition} Løsning
:class: solution, dropdown

Vi vet at $h(x) = 2x - 6$. For å bestemme definisjonsmengden, ser vi på verdimengden. Vi vet at siden $h(x)$ er en lineær funksjon som bare stiger, så vil den minste og største verdien i verdimengden være funksjonsverdiene til endepunktene i definisjonsmengden. For å bestemme definisjonsmengden, må vi derfor finne $x$-verdiene som gir $y$-verdiene $-4$ og $4$:

$$
h(x) = -4 \quad \Leftrightarrow \quad 2x - 6 = -4 \quad \Leftrightarrow \quad 2x = 2 \quad \Leftrightarrow \quad x = 1
$$

og 

$$
h(x) = 4 \quad \Leftrightarrow \quad 2x - 6 = 4 \quad \Leftrightarrow \quad 2x = 10 \quad \Leftrightarrow \quad x = 5.
$$

Dermed blir definisjonsmengden til $h$ gitt ved $D_h = [1, 5]$.
```

Oppgave 3b
: Bestem $h(0)$.

```{admonition} Løsning
:class: solution, dropdown

Vi setter inn $x = 0$ i funksjonsuttrykket for å finne $h(0)$:

$$
h(0) = 2 \cdot 0 - 6 = -6.
$$
```

Oppgave 3c
: Bestem koordinatene til punktet $(4, h(4))$ på grafen til $h$. Er punktet faktisk på grafen til $h$? 
```{dropdown} Hint
Du må sjekke om $4 \in D_h$ og $h(4) \in V_h$.
```

```{admonition} Løsning
:class: solution, dropdown
For å bestemme koordinatene til punktet, må vi regne ut $y = h(4)$:

$$
h(4) = 2 \cdot 4 - 6 = 2.
$$

Dermed er koordinatene til punktet $(4, h(4)) = (4, 2)$ på grafen til $h$. Siden $4 \in D_h$ og $2 \in V_h$, er punktet faktisk på grafen til $h$.
```