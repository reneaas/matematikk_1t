# Funksjonsbegrepet

Her skal du få en innføring i funksjonsbegrepet. En funksjon kan noen ganger tenkes på som en graf, andre ganger tenker vi på det som en formel. Vi tenker på formelen og grafen som ulike representasjoner av en mer generell sammenheng som vi kaller for en **funksjon**. 


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

```{dropdown} Løsningsforslag
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
:width: 100%

Her vises fire grafer $A$, $B$, $C$ og $D$. Men hvilke av de er funksjoner? Hvilke av de er bare kurver?

```{dropdown} Løsningsforslag
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