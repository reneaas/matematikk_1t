# Grafisk løsning

Å løse andregradslikninger grafisk, handler om å finne skjæringspunkter med grafer til andregradsfunksjoner med andre andregradsfunksjoner eller lineære funksjoner. Generelt sett kan en andregradslikning alltid skrives om til formen

$$
ax^2 + bx + c = 0.
$$ (eq:generell_andregradslikning)

Når vi jobber algebraisk, vil vi alltid skrive om likningen på denne måten, men når vi jobber grafisk har vi større frihet til å angripe problemene direkte. 

## Skjæring med $x$-aksen (nullpunkter)

Vi har allerede sett at skjæringen til en funksjongraf med $x$-aksen svarer til å bestemme nullpunktene til en funksjon $f(x)$. For en andregradsfunksjon $f(x) = ax^2 + bx + c$, vil nullpunktene være løsningene til likningen $f(x) = 0$. Dette er akkurat det samme som å løse en andregradslikning $ax^2 + bx + c = 0$. 

````{admonition} Eksempel 1: grafisk løsning av $ax^2 + bx + c = 0$
:class: eksempel
Figuren under viser en grafen til andregradsfunksjonen 

$$
f(x) = x^2 - x - 6.
$$

Vi skal grafen til å løse likningen 

$$
f(x) = 0 \quad \Leftrightarrow \quad x^2 - x - 6 = 0.
$$

```{figure} ./figurer/eksempler/eksempel_1.svg
:name: eksempel-1
:width: 80%
```

Vi ser at grafen skjærer $x$-aksen i punktene $x = -2$ og $x = 3$. Dermed er løsningene til likningen 

$$
x^2 - x - 6 = 0
$$ 

gitt ved 

$$
x = -2 \quad \lor \quad x = 3.
$$
````

Nå er det **din tur**!

````{admonition} Underveisoppgave 1
:class: note
I figuren under vises grafen til en andregradsfunksjon

$$
g(x) = x^2 - 4x - 5.
$$

Bruk grafen til å løse likningen 

$$
x^2 - 4x - 5 = 0.
$$

```{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
:name: underveisoppgave-1
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown
Å løse likningen $x^2 - 4x - 5 = 0$, er det samme som å bestemme hvor grafen til funksjonen skjærer $x$-aksen. Vi kan se fra figuren at grafen til $g(x)$ skjærer $x$-aksen i punktene $x = -1$ og $x = 5$. Dermed er løsningene til likningen gitt ved

$$
x^2 - 4x - 5 = 0 \quad \Leftrightarrow \quad x = -1 \quad \lor \quad x = 5.
$$
```

````

## Skjæring mellom funksjoner

Hvis $f(x)$ er en andregradsfunksjon og $g(x)$ er enten en andregradsfunksjon eller en lineær funksjon, så hender det vi ønsker å løse likninger av typen

$$
f(x) = g(x). 
$$

Selv om vi strengt tatt alltid kan skrive om disse til den generelle formen i likning {eq}`eq:generell_andregradslikning}, kan det være enklere å løse likningen grafisk direkte. 

````{admonition} Eksempel 2: grafisk løsning av $f(x) = g(x)$
:class: eksempel
Figuren under viser grafene til funksjonene

$$
f(x) = x^2 - x - 2 \quad \text{og} \quad g(x) = 3x - 5.
$$

Vi skal bruke figuren til å løse likningen

$$
f(x) = g(x) \quad \Leftrightarrow \quad x^2 - x - 2 = 3x - 5.
$$

```{figure} ./figurer/eksempler/eksempel_2.svg
:name: eksempel-2
:width: 80%
```

For å løse likningen, ser vi etter skjæringspunktene mellom de to grafene. Vi kan observere at de skjærer hverandre i punktene $(x, y) = (1, -2)$ og $(x, y) = (3, 4)$. Vi må huske på at vi bare er ute etter $x$-verdiene når vi løser likningen. Dermed har vi at

$$
x^2 - x - 2 = 3x - 5 \quad \Leftrightarrow \quad x = 1 \quad \lor \quad x = 3.
$$

````

Så er det **din tur**!

````{admonition} Underveisoppgave 2
:class: note
I figuren under vises grafene til funksjonene

$$
f(x) = -x^2 + x + 6 \quad \text{og} \quad g(x) = x - 3.
$$

Bruk grafene til å løse likningen

$$
-x^2 + x + 6 = x - 3. 
$$


```{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
:name: underveisoppgave-2
:width: 80%
```

```{admonition} Løsning
:class: solution, dropdown
Vi ser etter eventuelle skjæringspunkter mellom grafene til $f(x)$ og $g(x)$. Vi kan observere at de skjærer hverandre i punktene

$$
(x, y) = (-3, -6) \quad \text{og} \quad (x, y) = (3, 0).
$$

Dermed blir løsningene av likningen

$$
-x^2 + x + 6 = x - 3 \quad \Leftrightarrow \quad x = -3 \quad \lor \quad x = 3.
$$

```
````


## Oppgaver

