# Ettpunktsformelen

Dersom vi kjenner stigningstallet og ett punkt på grafen til en lineær funksjon, kan vi bestemme bestemme funksjonsuttrykket. Vi gjør dette ved å bruke noe vi kaller for **ettpunktsformelen**. 


```{admonition} Læringsmål: ettpunktsformelen
:class: tip
Målet med dette kapittelet er at du skal kunne:
* Bestemme funksjonsuttrykket til en lineær funksjon ved å bruke ettpunktsformelen
```

## Ettpunktsformelen: hva er det?

Vi tar utgangspunkt i {numref}`fig-ettpunktsformelen`. 

```{figure} ./figurer/teori/ettpunktsformelen.svg
:name: fig-ettpunktsformelen
:width: 80%

Viser en lineær funksjon et kjent punkt $(x_1, y_1)$ og et vilkårlig punkt $(x, y)$ er tegnet inn.
```

Vi tenker oss en lineær funksjon $f(x) = ax + b$. Tidligere har vi sett at med topunktsformelen kan vi finne stigningstallet $a$ dersom vi kjenner to punkter $(x_1, y_1)$ og $(x_2, y_2)$ på grafen.
Men vi har også sett at uansett hvilke to punkter vi velger, så blir stigningstallet det samme. Det betyr at dersom vi har ett kjent punkt $(x_1, y_1)$, vil formelen

$$
a = \frac{y - y_1}{x - x_1},
$$

være sann for *alle* punkter $(x, y)$ på grafen (så lenge $x \neq x_1$). Men da kan vi finne at 

$$
a = \frac{y - y_1}{x - x_1} \quad \Leftrightarrow \quad y - y_1 = a(x - x_1) \quad \Leftrightarrow \quad y = a(x - x_1) + y_1.
$$

Dette er ettpunktsformelen.

```{admonition} Ettpunktsformelen
:class: theory
Dersom vi kjenner stigningstallet $a$ og et punkt $(x_1, y_1)$ på grafen til en lineær funksjon, kan vi bestemme funksjonsuttrykket til funksjonen ved hjelp av ettpunktsformelen

$$
y - y_1 = a(x - x_1)
$$

eller uttrykt som en funksjon

$$
f(x) = f(x_1) + a(x - x_1). 
$$
```

La oss se på et eksempel for å forstå hvordan vi kan bruke ettpunktsformelen.

```{admonition} Eksempel 1: ettpunktsformelen
:class: example

Et lineær funksjon $f$ har stigningstall $-2$ og går gjennom punktet $(1, 3)$. <br>
Bestem funksjonsuttrykket til funksjonen.

**Løsning**:

Vi har stigningstallet $a = -2$ og punktet $(x_1, y_1) = (1, 3)$. Da kan vi bruke ettpunktsformelen

$$
y - y_1 = a(x - x_1) \quad \Rightarrow \quad y - 3 = -2(x - 1),
$$

som gir

$$
y = -2(x - 1) + 3 = -2x + 2 + 3 = -2x + 5.
$$

Dermed er funksjonsuttrykket til den lineære funksjonen:

$$
f(x) = -2x + 5.
$$
```

Og så er det **din tur**!

````{admonition} Underveisoppgave 1
:class: check

En lineær funksjon $g$ har stigningstall $4$ og går gjennom punktet $(-1, -3)$. <br> 
Bestem funksjonsuttrykket til funksjonen.


```{admonition} Løsning
:class: solution, dropdown

Vi har stigningstallet $a = 4$ og punktet $(x_1, y_1) = (-1, -3)$. Da kan vi bruke ettpunktsformelen

$$
y - y_1 = a(x - x_1) \quad \Rightarrow \quad y + 3 = 4(x + 1),
$$

som gir

$$
y = 4(x + 1) - 3 = 4x + 4 - 3 = 4x + 1.
$$

Dermed er funksjonsuttrykket til den lineære funksjonen:

$$
g(x) = 4x + 1.
$$
```

````