# Spesielle andregradslikninger

Vi skal starte med å se på en spesiell type andregradslikning som løses ved hjelp av lineære likninger. 

```{admonition} Læringsmål: spesielle andregradslikninger
:class: tip
Etter å ha gått gjennom denne delen, er målet at du skal kunne:
* Kunne bruke produktregelen for likninger. 
* Kunne løse andregradslikninger av typene:
    - $(x - x_1)(x - x_2) = 0$
    - $(ax + b)^2 = 0$
    - $ax^2 + bx = 0$
    - $ax^2 + c = 0$
```

## Hva er produktregelen for likninger?

Vi starter med en setning:

```{admonition} Produktregelen for likninger
:class: theory
Gitt to funksjoner $f(x)$ og $g(x)$, og likningen

$$
f(x) \cdot g(x) = 0,
$$

så må enten $f(x) = 0$, eller $g(x) = 0$, eller begge. Matematisk skriver vi:

$$
f(x)\cdot g(x) = 0 \quad \Leftrightarrow \quad f(x) = 0 \quad \lor \quad g(x) = 0
$$

```

Hovedpoenget her er at vi løser likningen ved å sette hver faktor lik null og løser de to likningene hver for seg.

## Andregradslikninger på formen $(x - x_1)(x - x_2) = 0$

Vi går løs på et eksempel med en gang for å illustrere ideen:

```{admonition} Eksempel 1: produktregelen 
:class: example
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
:class: check
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
:class: check
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
:class: example
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
:class: check
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
:class: example

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
:class: check

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


## Andregradslikninger på formen $ax^2 + c = 0$

### Strategi 1: Konjugatsetningen

En siste type spesiell andregradslikning vi skal angripe er likninger på formen

$$
ax^2 + c = 0.
$$

Så lenge $c < 0$, så vil det være to løsningen til likningen. Vi tar et eksempel:

```{admonition} Eksempel 4: Andregradslikning på formen $ax^2 + c = 0$
:class: example

Vi skal løse likningen

$$
x^2 - 4 = 0.
$$

Vi kan klart bruke konjugatsetningen her siden

$$
x^2 - 4 = x^2 - 2^2 = (x + 2)(x - 2).
$$

Dermed får vi at

$$
x^2 - 4 = 0 \quad \Leftrightarrow \quad (x + 2)(x - 2) = 0 \quad \Leftrightarrow \quad x + 2 = 0 \quad \lor \quad x - 2 = 0,
$$

så løsningene av likningen er

$$
x = -2 \quad \lor \quad x = 2.
$$
```

Så er det **din tur**!

````{admonition} Underveisoppgave 5
:class: check

Løs likningen

$$
x^2 - 9 = 0.
$$

```{admonition} Løsning
:class: solution, dropdown
Med konjugatsetningen kan vi skrive:

$$
x^2 - 9 = x^2 - 3^2 = (x + 3)(x - 3),
$$

som gir

$$
x^2 - 9 = 0 \quad \Leftrightarrow \quad (x + 3)(x - 3) = 0 \quad \Leftrightarrow \quad x + 3 = 0 \quad \lor \quad x - 3 = 0,
$$

så løsningene er

$$
x = -3 \quad \lor \quad x = 3.
$$
```
````

### Strategi 2: 

Vi tar eksempel 4 som utgangspunkt og ser på en annen strategi for å løse likningen $x^2 - 4 = 0$:

```{admonition} Eksempel 5: Andregradslikning på formen $ax^2 + c = 0$
:class: example

Vi skal løse likningen

$$
x^2 - 4 = 0,
$$

som vi kan skrive om til

$$
x^2 = 4.
$$

Hvilke tall $x$ er det vi kan gange med seg selv for å få 4? Vel, det er $x = \sqrt{4} = 2$, men også $x = -\sqrt{4} = -2$. Dette kan vi bekrefte med:

$$
x^2 = (-2)^2 = 4 \quad \text{og} \quad x^2 = 2^2 = 4.
$$

Dermed kan vi løse likningen ved å skrive

$$
x^2 = 4 \quad \Leftrightarrow \quad x = \pm \sqrt{4} = \pm 2. 
$$

Vi kan selvsagt også oppgi løsningen som 

$$
x = 2 \quad \lor \quad x = -2.
$$


Vi kan merke oss fra eksempelet at vi kan ta kvadratroten på hver side av likningen så lenge vi husker på at det både en positiv og en negativ løsning!
```

**Din tur** til å prøve strategien!

````{admonition} Underveisoppgave 6
:class: check
Løs likningen

$$
x^2 - 36 = 0
$$

```{admonition} Løsning
:class: solution, dropdown
Vi skriver om likningen til

$$
x^2 = 36,
$$

så tar vi kvadratroten på hver side av likningen og husker at det finnes en positiv og en negativ løsning:

$$
x = \pm \sqrt{36} = \pm 6,
$$

som er løsningen av likningen. Vi må ikke, men vi kan skrive dette som

$$
x = 6 \quad \lor \quad x = -6,
$$

også.

```

````

## Oppgaver

