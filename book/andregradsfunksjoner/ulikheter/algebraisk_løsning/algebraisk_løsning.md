# Algebraisk løsning

```{admonition} Læringsmål: algebraisk løsning
:class: tip
Målet med det delkapitlet er at du skal kunne:
* Kunne løse andregradsulikheter algebraisk ved hjelp av fortegnslinjer.
```

Når vi løser andregradsulikheter, får vi bruk for å kunne løse andregradslikninger som en del av løsningsprosessen.

````{admonition} Algebraisk løsning av andregradsulikheter
:class: theory
Andregradsulikheter kan løses algebraisk gjennom følgende steg:

Steg 1: Nullpunktsfaktorisering
: Vi nullpunktsfaktoriserer en andregradsfunksjon 

$$
f(x) = ax^2 + bx + c = a(x - x_1)(x - x_2),
$$

Steg 2: Fortegnsskjema
: Vi tegner et **fortegnsskjema** for $f(x)$ ved å tegne en **fortegnslinje** for hver lineær faktor i $f(x)$, og deretter ett for produktet av faktorene. Vi ser på fortegnene til faktorene for å bestemme fortegnet til $f(x)$ på hvert intervall. 

````

Andregradsulikheter løses algebraisk i to steg:



Vi går løs på et eksempel

````{admonition} Eksempel 1
:class: example
Bestem løsningsmengden til ulikheten

$$
x^2 - x - 6 > 0.
$$

**Løsning:**
Først nullpunktsfaktoriserer vi $f(x) = x^2 - x - 6$:

$$
x = \frac{1 \pm \sqrt{1 + 4 \cdot 6}}{2} = \frac{1 \pm \sqrt{25}}{2} = \frac{1 \pm 5}{2},
$$

som gir 

$$
x = -2 \quad \lor \quad x = 3.
$$

Dermed kan vi skrive

$$
f(x) = x^2 - x - 6 = (x + 2)(x - 3).
$$

Deretter tegner vi noe som kalles for et **fortegnskjema**. Måten vi gjør det på, er å tegne en **fortegnslinje** for hver lineær faktor i $f(x)$, og deretter ett for produktet av faktorene. Se {numref}`eksempel-1`.

```{figure} ./figurer/eksempler/eksempel_1.svg
:name: eksempel-1
:width: 80%

Fortegnslinje for $f(x) = x^2 - x - 6 = (x + 2)(x - 3)$. De blå heltrukkede linjene representerer at faktoren er **positiv** på intervallet, mens de røde striplede linjene representerer at faktoren er **negativ** på intervallet. Fortegnslinja til $f(x)$ får man ved å gange sammen fortegnene til faktorene.
```

Fra fortegnsskjema, kan vi se at $f(x) > 0$ når $x < -2$ og $x > 3$. Vi kan derfor uttrykke løsningsmengden som 

$$
x^2 - x - 6 > 0 \quad \Leftrightarrow \quad x \in \langle \gets, -2\rangle \cup \langle 3, \to \rangle = \mathbb{R} \setminus [-2, 3].
$$
````

Nå kan du prøve deg på en oppgave!

````{admonition} Underveisoppgave 1
:class: check

Under vises fortegnsskjema til en andregradsfunksjon $f(x) = x^2 - 4x - 5$. <br> 
Bruk fortegnsskjema til å bestemme løsningsmengden til

$$
x^2 - 4x - 5 < 0.
$$


```{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
:name: underveisoppgave-1
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown
Fra fortegnsskjema, kan vi se at $f(x) < 0$ når $-1 < x < 5$ (ved å se der hvor fortegnslinja til $f(x)$ er rød og striplete). Dermed er løsningsmengden til ulikheten

$$
x \in \langle -1, 5 \rangle.
$$
```
````

Og så en oppgave der du må lage fortegnslinjene selv:

`````{admonition} Underveisoppgave 2
:class: check
En andregradsfunksjon er gitt ved $f(x) = -x^2 + 4x + 6$.
Bestem løsningsmengden til ulikheten

$$
f(x) \leq 0.
$$

```{admonition} Hint
:class: hints, dropdown
Når du nullpunktsfaktoriserer andregradsfunksjonen på formen

$$
f(x) = a(x - x_1)(x - x_2),
$$

må du huske å ta med den ledende koeffisienten $a$ som en egen faktor i fortegnsskjemaet for at fortegnslinja til $f(x)$ skal bli riktig.
```

````{admonition} Løsning
:class: solution, dropdown

Først finner vi nullpunktene til $f(x) = -2x^2 + 4x + 6 = -2(x^2 - 2x - 3)$ og nullpunktsfaktoriserer:

$$
x = \frac{-(-2) \pm \sqrt{(-2)^2 - 4\cdot 1 \cdot (-3)}}{2\cdot 1} = \frac{2 \pm 4}{2} = 1 \pm 2,
$$

som gir nullpunktene $x = -1$ og $x = 3$. Dermed kan vi skrive

$$
-2x^2 + 4x + 6 \leq 0 \quad \Leftrightarrow \quad -2(x + 1)(x - 3) \leq 0.
$$

Så tegner vi et fortegnsskjema med de tre faktorene som $f(x)$ består av:

```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
:name: underveisoppgave-2
:width: 80%
```

Fra fortegnsskjema, kan vi se at $f(x) \leq 0$ når $x \leq -1 \, \lor x \geq 3$. Dermed er løsningsmengden til ulikheten

$$
x \in \mathbb{R} \setminus \langle -1, 3\rangle.
$$
````

`````


## Oppgaver

`````{admonition} Oppgave 1
:class: problem-level-1

Bestem løsningsmengden til ulikheten

$$
x^2 - 4x \geq 0.
$$

````{admonition} Fasit
:class: solution, dropdown

$$
x \in \mathbb{R} \setminus \langle 0, 4 \rangle.
$$

eller

$$
x \in \langle \gets, 0] \cup [4, \to \rangle.
$$
````

````{admonition} Løsning
:class: solution, dropdown
Vi tenker oss en andregradsfunksjon $f(x) = x^2 - 4x$ som vi skal nullpunktsfaktorisere:

$$
f(x) = x^2 - 4x = x(x - 4). 
$$

Deretter tegner vi et fortegnsskjema for $f(x)$: 

```{figure} ./figurer/oppgaver/oppgave_1.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-1
:width: 80%
```

Fra fortegnslinja til $f(x)$, kan vi se at $f(x) \geq 0$ når

$$
x \in \mathbb{R} \setminus \langle 0, 4 \rangle.
$$

````

`````

`````{admonition} Oppgave 2
:class: problem-level-1

En andregradsfunksjon er gitt ved $f(x) = -x^2 + 3x + 4$.

Bestem løsningsmengden for $f(x) \leq 0$.


````{admonition} Fasit
:class: solution, dropdown

```{figure} ./figurer/oppgaver/oppgave_2_uten_faktorer.svg
:name: oppgave-2-uten-faktorer
:width: 100%
```


$$
x \in \mathbb{R} \setminus \langle -1, 4 \rangle.
$$
````

````{admonition} Løsning
:class: solution, dropdown
Vi må først bestemme nullpunktene til $f(x)$ for å kunne nullpunktsfaktorisere: 

$$
x = \frac{-3 \pm \sqrt{(-3)^2 - 4\cdot (-1)\cdot 4}}{2\cdot (-1)} = \frac{-3 \pm \sqrt{9 + 16}}{-2} = \frac{-3\pm 5}{-2} = \frac{3 \mp 5}{2}
$$

som gir

$$
x = -1 \quad \lor \quad x = 4. 
$$

Vi husker på at den ledende koeffisienten er $a = -1$, som gir

$$
f(x) = -x^2 + 3x + 4 = -1\cdot(x + 1)(x - 4) = -(x + 1)(x - 4).
$$

Nå kan vi tegne fortegnsskjema for funksjonen:

```{figure} ./figurer/oppgaver/oppgave_2.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-2
:width: 80%
```

Fra fortegnsskjemaet kan vi se at $f(x) \leq 0$ når 

$$
x \in \mathbb{R} \setminus \langle -1, 4 \rangle.
$$
````
`````


`````{admonition} Oppgave 3
:class: problem-level-2
En funksjon $g$ har fortegnslinje som vist i {numref}`andregradsulikheter-algebraisk-oppgaver-oppgave-3`. Bestem et mulig uttrykk for $g(x)$. 

```{figure} ./figurer/oppgaver/oppgave_3_uten_faktorer.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-3
:width: 100%

Fortegnsskjema for en funksjon $g(x)$.
```


````{admonition} Fasit
:class: solution, dropdown
Et eksempel på en funksjon som passer:

$$
g(x) = -(x - 2)(x + 2)
$$

Alle funksjoner på formen

$$
g(x) = a(x - 2)(x + 2), \quad a < 0
$$

passer med fortegnslinja til $g$. 
````

````{admonition} Løsning
:class: solution, dropdown
Vi kan tegne et mer detaljert fortegnsskjema der vi har én lineær faktor med nullpunkt i $x = -2$ og én lineær faktor med nullpunkt i $x = 2$: 

```{figure} ./figurer/oppgaver/oppgave_3.svg
:name: andregradsulikheter-algebraisk-oppgaver-oppgave-3-solution
:width: 80%
```

Vi kan se at så lenge den ledende koeffisienten er negativ, får vi riktig fortegnslinje. Dermed er det meste generelle uttrykket for $g(x)$

$$
g(x) = a(x - 2)(x + 2), \quad a < 0.
$$

I fortegnslinja har vi valgt ett eksempel som passer:

$$
g(x) = -(x - 2)(x + 2)
$$
````
`````