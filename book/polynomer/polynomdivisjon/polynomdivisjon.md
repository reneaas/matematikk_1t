# Polynomdivisjon

Polynomdivisjon er en algoritme som lar oss systematisk dele et polynom med et annet. Når vi deler et polynom $p(x)$ med et annet polynom $q(x)$, vil vi få en **kvotient** $k(x)$ og en **rest** $r(x)$ slik at 

$$
\frac{p(x)}{q(x)} = k(x) + \frac{r(x)}{q(x)}
$$

Det er ikke alltid vi får en rest. Da sier vi at polynomdivisjonen **går opp**. Ofte skriver vi polynomdivisjon som $p(x) \div q(x)$ i stedet for som en brøk $p(x) / q(x)$. Men begge skrivemåter er meningsfulle og betyr det samme.

```{admonition} Læringsmål: polynomdivisjon
Etter å gått gjennom dette kapittelet skal du kunne:
* Utføre polynomdivisjon der nevneren er et førstegradspolynom.
* Kjenne til sammenhengen mellom nullpunkter, faktorer og rest, og kunne bruke dette til å bestemme nullpunktene til tredjegradspolynomer.

Vi starter med et konkret eksempel:
```

````{admonition} Eksempel 1 (uten rest)
:class: eksempel
Vi skal dele polynomet $x^3 + 2x^2 - 5x - 6$ med $x - 2$. Først skal vi se hele resultatet:

```{figure} ./figurer/eksempler/eksempel1.svg
:scale: 200%
```
Ser overveldende ut, men vi skal ta det stegvis under.

Steg 1
: Vi starter med å se på leddet med høyest potens av $x$ i $x^3 + 2x^2 - 5x - 6$, som er $x^3$. Vi deler dette leddet på høyeste potens av $x$ i nevneren som er $x$, som gir $x^2$. Dette er første ledd i kvotienten. Deretter trekker vi fra $x^2\cdot(x - 2) = x^3 - 2x^2$ fra polynomet i teller:
\begin{align*}
& (\quad \, x^3 + 2x^2 - 5x - 6) \div (x - 2) = x^2 \\
& -x^3 - 2x^2 & \\
\hline
& \quad\quad\quad\, 4x^2 - 5x & \\
\end{align*}

Steg 2
: Vi gjentar prosessen, men nå med $4x^2$ siden dette er den høyeste potensen av $x$ i det nye polynomet vi sitter igjen med. Vi deler med $x$ som gir oss $4x$. Dette er andre ledd i kvotienten. Deretter trekker vi fra $4x^2(x - 2) = 4x^2 - 8x$:

\begin{align*}
& (\quad \, x^3 + 2x^2 - 5x - 6) \div (x - 2) = x^2 + 4x \\
& -x^3 - 2x^2 & \\
\hline
& \quad\quad\quad\, 4x^2 - 5x & \\
& \quad\quad\,\, -4x^2 + 8x & \\
\hline
& \quad\quad\quad\quad\quad\,\,\,\,\, 3x - 6 & \\
\end{align*}

Steg 3
: Vi gjentar prosessen, men nå med $3x - 6$. Vi deler da $3x$ med $x$ som gir $3$ til kvotienten. Deretter trekker vi fra $3(x - 2) = 3x - 6$:

\begin{align*}
& (\quad \, x^3 + 2x^2 - 5x - 6) \div (x - 2) = x^2 + 4x + 3 \\
& -x^3 - 2x^2 & \\
\hline
& \quad\quad\quad\, 4x^2 - 5x & \\
& \quad\quad\,\, -4x^2 + 8x & \\
\hline
& \quad\quad\quad\quad\quad\,\,\,\,\, 3x - 6 & \\
& \quad\quad\quad\quad\quad\, -3x + 6 & \\
\hline
& \quad\quad\quad\quad\quad\quad\quad\quad\, 0 & \\
\end{align*}


Konklusjonen vi kan trekke er at siden 

$$
(x^3 + 2x^2 - 5x - 6) \div (x - 2) = x^2 + 4x + 3
$$

så kan vi skrive 

$$
x^3 + 2x^2 - 5x - 6 = (x - 2)(x^2 + 4x + 3)
$$

Merk
: Siden vi får null i rest her, så sier vi at divisjonen **går opp**. Det betyr at $x - 2$ er en faktor i $x^3 + 2x^2 - 5x - 6$ og at $x = 2$ er et nullpunkt for tredjegradspolynomet.
````

```{admonition} Underveisoppgave 1
:class: note
Utfør polynomdivisjonen

$$
(x^3 -7x - 6) \div (x - 3)
$$

**Hint**: Det kan være lurt å skrive $x^3 - 7x - 6$ som $x^3 + 0x^2 - 7x - 6$ slik at du kan følge algoritmen i eksempelet over. Eventuelt bare husk å legge til litt plass der det skulle stått et ledd med $x^2$.
```

````{dropdown} Løsning
```{figure} ./figurer/underveisoppgaver/underveisoppgave1.svg
:scale: 200%
```
````


````{admonition} Eksempel 2 (med rest)
:class: eksempel
Vi skal se på polynomdivisjonen

$$
(x^3 - 5x - 2) \div (x + 1)
$$

Hvis vi utfører denne polynomdivisjonen, får vi:
    
```{figure} ./figurer/eksempler/eksempel2.svg
:scale: 200%
```
Vi kan merke oss at når vi gikk gjennom alle stegene her, så endte vi ikke opp med $0$ til slutt, men med $2$. Det betyr at vi har en **rest** på $2$ etter divisjonen og vi legger derfor på et ledd $2/(x + 1)$ til slutt. 
````

```{admonition} Underveisoppgave 2
:class: note

Utfør polynomdivisjonen under:

$$
(x^3 + 5x^2 - 1) \div (x + 1)
$$

**Hint:** Skriv polynomet som $x^3 + 5x^2 + 0x - 1$ når du utfører polynomdivisjonen. Eller etterlat en plass der hvor leddet til $x$ mangler så du ikke glemmer å ta med det i divisjonen!
```

````{dropdown} Løsning
```{figure} ./figurer/underveisoppgaver/underveisoppgave2.svg
:scale: 200%
```
````