# Nullpunkter og likninger

I dette kapittelet skal vi se på sammenhengen mellom likninger og nullpunkter til funksjoner. 


```{admonition} Læringsmål: nullpunkter og likninger
:class: tip

Etter å ha arbeidet med dette kapittelet, skal du kunne:
* Finne nullpunkter til lineære funksjoner.
* Forstå sammenhengen mellom nullpunkter og løsning av likninger.
* Kunne finne nullpunkter grafisk og ved regning.
* Forstå at nullpunkter svarer til grafen til en funksjon med $x$-aksen (førsteaksen). 
```

## Nullpunkter
Nullpunkter står sentralt i matematikken og vil dukke opp i mange sammenhenger. Først og fremst ser vi på en definisjon:

```{admonition} Definisjon: nullpunkter
:class: tip
**Nullpunktene** til en funksjon $f$ er definert som verdiene av $x$ som medfører at $f(x) = 0$. 
En funksjon kan ha ett eller flere nullpunkter. 

Nullpunkter handler derfor om å løse likninger av typen $f(x) = 0$, der $x$ er ukjent. 

Merknad 1
: Det også vanlig å bruke begrepet **rot** om et nullpunkt eller **røtter** om nullpunkter. Dette har ingenting med kvadratrøtter eller $n$-te røtter å gjøre.

Merknad 2
: Selv om vi bruker begrepet *nullpunkter*, er det vanlig å oppgi nullpunkter som $x$-verdier, siden $y$-verdien uansett er null.

Merknad 3
: En lineær funksjon vil *alltid* ha nøyaktig ett nullpunkt.
```

La oss se på et konkret eksempel:

````{admonition} Eksempel 1: Nullpunkter
:class: eksempel
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2x - 4.
$$

Bestem nullpunktet til $f$. 

**Prøv gjerne på problemet før du ser på løsningen!**

```{admonition} Løsning
:class: solution, dropdown
Etter definisjonen, må vi løse likningen $f(x) = 0$ for å finne nullpunktet til $f$. Da erstatter vi $f(x)$ med funksjonsuttrykket i likningen, og løser for $x$:

$$
f(x) = 0 \quad \Leftrightarrow \quad 2x - 4 = 0 \quad \Leftrightarrow \quad 2x = 4 \quad \Leftrightarrow \quad x = 2.
$$

Altså er nullpunktet til $f$ gitt ved $x = 2$. 

Vi kan merke oss at nullpunkter til $f(x)$ bare svarer til løsningen av likningen $2x - 4 = 0$.
```
````

## Bestemme nullpunkter grafisk
Vi har sett på hvordan vi kan bestemme nullpunkter algebraisk ved å løse en likning $f(x) = 0$ ved hjelp av funksjonsuttrykket til $f$. Men vi kan også løse dette grafisk ved å tegne grafen til $f$ å undersøke hvor grafen skjærer $x$-aksen. 
Men hvorfor der hvor grafen skjærer $x$-aksen? Vel, det skal vi utvide definisjonen vår for å forstå:

```{admonition} Definisjon: nullpunkter og grafen til en funksjon
:class: tip

Nullpunktene til en funksjon $f$ er verdiene av $x$ der hvor grafen til $f$ skjærer $x$-aksen.
Dette er fordi $y = f(x) = 0$ for disse $x$-verdiene, som samsvarer med der grafen skjærer $x$-aksen.
```


````{admonition} Eksempel 2: Bestemme nullpunkter grafisk
:class: eksempel

La oss på grafen til en lineær funksjon $g$:

```{figure} ./figurer/eksempler/eksempel_nullpunkter_grafisk.svg
:width: 80%
```

Hva er nullpunktet til $g$?

```{admonition} Løsning
:class: solution, dropdown
Vi kan lese av fra grafen at $g$ skjærer $x$-aksen i $x = 2$. Dermed er nullpunktet til $g$ gitt ved $x = 2$.
```
````


## Nullpunkter og likninger
Vi har sett at nullpunkter til en funksjon svarer til:
* Løsningen av likningen $f(x) = 0$,
* Der grafen til $f$ skjærer $x$-aksen.

Vi kan faktisk tenke på løsning av **alle** likninger som å finne nullpunkter. Noen ganger må vi bare definere en ny funksjon og bestemme nullpunktene til den nye funksjonen. 

```{admonition} Likninger og nullpunkter
:class: tip
La $f$ og $g$ være to funksjoner. Da kan vi løse likningen $f(x) = g(x)$ ved å finne nullpunktene til funksjonen $h(x) = f(x) - g(x)$. 

Hvis $f(x) = g(x)$, så må $f(x) - g(x) = 0$ som betyr at $h(x) = 0$. Dermed er nullpunktene til $h$ løsningene til likningen $f(x) = g(x)$.
```

```{admonition} Eksempel 3: Løse likninger ved å finne nullpunkter
:class: eksempel

La oss se på sammenhengen mellom nullpunkter og løsning av likningen $2x + 3 = 7$. Her kan vi tenke på det som at vi har en funksjon $f(x) = 2x + 3$ og en funksjon $g(x) = 7$ (en konstant funksjon, bare). Vi kan da definere en ny funksjon

$$
h(x) = f(x) - g(x) = 2x + 3 - 7 = 2x - 4.
$$

Deretter bestemmer vi nullpunktene til $h(x)$:

$$
h(x) = 2x - 4 = 0 \quad \Leftrightarrow \quad 2x = 4 \quad \Leftrightarrow \quad x = 2.
$$

Altså er løsningen av den opprinnelige likningen $x = 2$.
```

```{admonition} Eksempel 4: Løse likninger ved å finne nullpunkter
:class: eksempel
La oss si vi har likningen 

$$
4x + 1 = 2x - 3.
$$

Vi kan definere to funksjoner, 

$$
f(x) = 4x + 1 \quad \text{og} \quad g(x) = 2x - 3,
$$

og deretter tenke på det som at vi skal løse likningen $f(x) = g(x)$. Men igjen, er dette det samme som å finne nullpunktene til funksjonen

$$
h(x) = f(x) - g(x) = 4x + 1 - (2x - 3) = 2x + 4.
$$

Vi løser derfor $h(x) = 0$ og finner:

$$
h(x) = 2x + 4 = 0 \quad \Leftrightarrow \quad 2x = -4 \quad \Leftrightarrow \quad x = -2.
$$

Altså er nullpunktet til $h$, og dermed løsningen av den opprinnelgie likningen, gitt ved $x = -2$.
```

````{admonition} Underveisoppgave 
:class: note
Bestem løsningen av likningen $3x - 2 = 5x + 1$ og finn en funksjon som har løsningen som sitt nullpunkt.

```{admonition} Løsning
:class: solution, dropdown
Vi kan definere en funksjon $h(x)$ ved å ta venstre side minus høyre side:

$$
h(x) = 3x - 2 - (5x + 1) = 3x - 2 - 5x - 1 = -2x - 3.
$$

Deretter bestemmer vi nullpunktet til funksjonen ved å løse $h(x) = 0$:

$$
h(x) = -2x - 3 = 0 \quad \Leftrightarrow \quad -2x = 3 \quad \Leftrightarrow \quad x = -\frac{3}{2}.
$$

Dermed er løsningen av den opprinnelige likninger $x = -3/2$, som også svarer til nullpunktet til $h(x)$.
```
````

