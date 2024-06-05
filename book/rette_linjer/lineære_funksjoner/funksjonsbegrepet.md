# Funksjonsbegrepet

Her skal du få en innføring i funksjonsbegrepet. En funksjon kan noen ganger tenkes på som en graf, andre ganger tenker vi på det som en formel. Vi tenker på formelen og grafen som ulike representasjoner av et mer generelt objekt som vi kaller for en **funksjon**. 

## Funksjon som en graf
Når vi tenker på en funksjon som en graf, så tenker vi på en graf der hver $x$-verdi er tilordnet en $y$-verdi. Til sammen gir dette oss par $(x, y)$ der vi kan tegne en graf. Betingelsen for at det skal være en funksjon, er at det er **kun én** $y$-verdi for hver $x$-verdi. 

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
````

```{dropdown} Løsningsforslag
I {numref}`funksjonsgraf_vs_kurve_oppgave1` ser vi at graf $A$ bare har én $y$-verdi for hver $x$-verdi, så dette må være en funksjon. 

Graf $B$ har to $y$-verdier for alle $x \in \langle -2, 2 \rangle \setminus \{0\}$, så dette er ikke en funksjon.

Graf $C$ er en rett linje der $x = -1$ har uendelig mange $y$-verdier, så dette er ikke en funksjon heller.

Graf $D$ er en linje $y = -1$ der alle $x$-verdier har samme $y$-verdi. Men hver $x$-verdi har bare én $y$-verdi som betyr at grafen er en funksjon.
```

## Funksjon som en formel

Formelen for en skrå linje

$$
y = ax + b
$$

kan tenkes på som formelen for en funksjon fordi en $y$-verdi bestemmes av en $x$-verdi. Alt vi trenger å gjøre, er å plugge inn en $x$-verdi i formelen, så kan vi regne ut hvilken $y$-verdi som hører til $x$-verdien. Vi sier at $x$-verdien **tilordner** en $y$-verdi. 

Fordi vi mener at $y$-verdien er entydig bestemt av $x$-verdien, skriver vi $y = f(x)$, hvor $f$ er **navnet** på funksjonen. Når vi skriver $f(x)$, mener vi **funksjonsverdien** ($y$-verdien) du får dersom du plugger inn en verdi for $x$ i formelen for funksjonen $f$. 




## Definisjon av en funksjon
Vi er nå klare for å oppsummere en definisjon av en funksjon. 

```{admonition} Definisjon: Funksjon
:class: tip
En **funksjon** $f$ er en regel som for _hvert_ element $x \in D_f$ tilordner _nøyaktig én_ funksjonsverdi $f(x) \in V_f$.
Vi kaller $D_f$ for **definisjonsmengden** til $f$ som er alle tillatte $x$-verdier vi kan regne ut en funksjonsverdi $y = f(x)$. Vi kaller $V_f$ for **verdimengden** til $f$ som er alle $y$-verdier som kan regnes ut med $x \in D_f$.
```