# Produktregelen

Vi skal starte med å se på en spesiell type andregradslikning som løses ved hjelp av lineære likninger. 

```{admonition} Læringsmål: produktregelen
:class: tip
Etter å ha gått gjennom denne delen, er målet at du skal kunne:
* Kunne bruke produktregelen til å løse andrelikninger av typene:
    - $(x - x_1)(x - x_2) = 0$,
    - $ax^2 + bx = 0$,
    - $(ax + b)^2 = 0$.
```


## Hva er produktregelen for likninger?

Vi starter med en forklaring:

```{admonition} Produktregelen for likninger
:class: tip
Gitt to funksjoner $f(x)$ og $g(x)$, og likningen

$$
f(x) \cdot g(x) = 0,
$$

så må enten $f(x) = 0$, eller $g(x) = 0$, eller begge. Matematisk skriver vi:

$$
f(x)\cdot g(x) = 0 \quad \Leftrightarrow \quad f(x) = 0 \quad \lor \quad g(x) = 0
$$

```

## Andregradslikninger på formen $(x - x_1)(x - x_2) = 0$

Vi går løs på et eksempel med en gang for å illustrere ideen:

```{admonition} Eksempel 1: produktregelen 
:class: eksempel
Vi tenker oss en likning bestående av produktet av to lineære funksjoner $f(x) = x - 2$ og $g(x) = x + 3$ som:

$$
(x - 2)(x + 3) = 0.
$$

I følge produktregelen, vil løsningen av denne likningen være å løse $f(x) = 0$ og $g(x) = 0$ hver for seg. Altså:

$$
(x - 2)(x + 3) = 0 \quad \Leftrightarrow \quad x - 2 = 0 \quad \lor \quad x + 3 = 0.
$$

Vi løser de to likningene hver for seg:

$$
x - 2 = 0 \quad \lor \quad x + 3 = 0 \quad \Leftrightarrow \quad x = 2 \quad \lor \quad x = -3.
$$

Dermed er løsningene til likningen $(x - 2)(x + 3) = 0$ gitt ved $x = 2 \lor x = -3$.
```

Når er det **din tur**!

````{admonition} Underveisoppgave 1
:class: note
Løs likningen

$$
(x + 2)(x - 4) = 0.
$$

```{admonition} Løsning
:class: solution, dropdown
Vi løser likningen med produktregelen direkte:

$$
(x + 2)(x - 4) = 0 \quad \Leftrightarrow \quad x + 2 = 0 \quad \lor \quad x - 4 = 0,
$$

som gir

$$
x = -2 \quad \lor \quad x = 4.
$$
```
````

Du kan prøve på enda en:

````{admonition} Underveisoppgave 2
:class: note
Løs likningen

$$
x\left(x + 2\right) = 0.
$$


```{admonition} Løsning
:class: solution, dropdown
Vi løser likningen med produktregelen:

$$
x\left(x + 2\right) = 0 \quad \Leftrightarrow \quad x = 0 \quad \lor \quad x + 2 = 0 \quad \Leftrightarrow \quad x = 0 \quad \lor \quad x = -2.
$$

```
````

## Andregradslikninger på formen $ax^2 + bx = 0$

I underveisoppgave 2 møtte du på en spesiell andregradslikning. Utvider vi parentesen, finner vi at 

$$
x(x + 2) = 0 \quad \Leftrightarrow \quad x^2 + 2x = 0.
$$

Med andre ord er dette også likninger som er egnet for å løses med produktregelen, så lenge vi faktoriserer først. Vi tar et eksempel:

```{admonition} Eksempel 2: Andregradslikning på formen $ax^2 + bx = 0$
:class: eksempel
Vi skal løse likningen

$$
4x^2 + 16x = 0.
$$

Vi kan merke oss at

$$
4x^2 + 16x = 4x(x + 4), 
$$

som betyr at

$$
4x^2 + 16x = 0 \quad \Leftrightarrow \quad 4x(x + 4) = 0 \quad \Leftrightarrow \quad 4x = 0 \quad \lor \quad x + 4 = 0.
$$

Dermed finner vi at løsningene er

$$
x = 0  \quad \lor \quad x = -4.
$$

```

Når er det **din tur**!

````{admonition} Underveisoppgave 3
:class: note
Løs likningen 

$$
3x^2 - 6x = 0.
$$


```{admonition} Løsning
:class: solution, dropdown
Vi faktoriserer først:

$$
3x^2 - 6x = 3x(x - 2),
$$

som betyr at 

$$
3x^2 - 6x = 0 \quad \Leftrightarrow \quad 3x(x - 2) = 0 \quad \Leftrightarrow \quad 3x = 0 \quad \lor \quad x - 2 = 0,
$$

som gir løsningene 

$$
x = 0 \quad \lor \quad x = 2.
$$
```

````


## Andregradslikninger på formen $(ax+b)^2 = 0$ 
Et siste tilfelle vi kommer til å møte på der produktregelen er nyttig, er likningen på formen

$$
(ax + b)^2 = 0.
$$

Løsningen av denne likningen er rett og slett bare løsningen av likningen $ax + b = 0$ fordi produktregelen gir

$$
(ax + b)^2 = 0 \quad \Leftrightarrow \quad (ax + b)(ax + b) = 0 \quad \Leftrightarrow \quad ax + b = 0.
$$

Vi tar et eksempel:

```{admonition} Eksempel 3: Andregradslikning på formen $(ax + b)^2 = 0$
:class: eksempel

Vi skal løse likningen

$$
(2x - 3)^2 = 0.
$$

Etter produktregelen er dette ekvivalent med å bare løse likningen

$$
2x - 3 = 0 \quad \Leftrightarrow \quad 2x = 3 \quad \Leftrightarrow \quad x = \frac{3}{2}.
$$

Altså er det bare én løsning av likningen gitt ved $x = 3/2$. 

```

Nå er det **din tur**!

````{admonition} Underveisoppgave 4
:class: note

Løs likningen

$$
(3x + 4)^2 = 0.
$$

```{admonition} Løsning
:class: solution, dropdown
Vi løser likningen ved å løse $3x + 4 = 0$:

$$
(3x + 4)^2 = 0 \quad \Leftrightarrow \quad 3x + 4 = 0 \quad \Leftrightarrow \quad 3x = -4 \quad \Leftrightarrow \quad x = -\frac{4}{3}.
$$
```
````


## Oppgaver

