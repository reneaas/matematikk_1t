# Algebraisk løsning

```{admonition} Læringsmål: algebraisk løsning
:class: tip
Målet med det delkapitlet er at du skal kunne:
* Kunne løse andregradsulikheter algebraisk ved hjelp av fortegnslinjer.
```

Andregradsulikheter løses algebraisk i to steg:

Steg 1
: Skriv ulikheten på formen $f(x) > 0$ eller $f(x) < 0$.

Steg 2
: Nullpunktsfaktoriser $f(x)$.

Steg 3
: Bruk fortegnslinjer til å bestemme fortegnet til $f(x)$ på ulike intervaller for å identifisere løsningsmengden. 


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
x = -2 \quad \text{eller} \quad x = 3.
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

må du huske å ta med den ledenede koeffisienten $a$ som en egen faktor i fortegnsskjemaet for at fortegnslinja til $f(x)$ skal bli riktig.
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