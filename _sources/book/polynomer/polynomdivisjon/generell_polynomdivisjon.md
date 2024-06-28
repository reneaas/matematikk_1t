# Mer komplisert polynomdivisjon

## Polynomdivisjon generelt
Hittil har vi sett på polynomdivisjon der vi har delt et tredjegradspolynom på et lineært polynom.
Men så lenge teller har større grad enn nevner, kan vi utføre polynomdivisjon. I denne seksjonen skal vi se på noen eksempler på dette. Men først skal vi skrive ned et mer generelt resultat:

````{margin} 
```{admonition} Polynomgrad
:class: tip
Når vi snakker om graden til et polynom $p$ skriver vi $\deg(p)$ (fra det engelske ordet *degree*). Dette er den høyeste potensen av $x$ i polynomet. For eksempel for $p(x) = x^3 - 5x + 1$, så er $\deg(p) = 3$ fordi det er den høyeste potensen av $x$.
```
````


```{admonition} Polynomdivisjon (generelt)
:class: tip
Gitt et polynom $p(x)$ av grad $\deg(p) = n$ og et polynom $q(x)$ av grad $\deg(q) = m$, vil polynomdivisjonen $p(x) \div q(x)$ gi

$$
\frac{p(x)}{q(x)} = k(x) + \frac{r(x)}{q(x)}
$$

der $k(x)$ kalles for **kvotienten** og er et polynom av grad $\deg(k) = n - m$, og $r(x)$ kalles for **resten** og er et polynom med en grad $\deg(r) \leq m - 1$.

Alternativt kan vi skrive sammenhengen over som

$$
p(x) = k(x)q(x) + r(x)
$$

Observasjon
: Dersom polynomdivisjonen går opp, så er $r(x) = 0$. Dette betyr at $q(x)$ er en faktor i $p(x)$.
```



```{admonition} Eksempel 1 (tredjegradspolynom delt med andregradspolynom)
:class: eksempel

Vi tenker oss at vi skal utføre polynomdivisjonen

$$
(x^3 - 5x^2 + 3x - 1) \div (x^2 - 3x + 2)
$$

Fremgangsmåten er som før, men nå deler vi med $x^2$ og ikke med $x$ siden dette er den høyeste potensten av $x$ i nevneren. 

Steg 1
: Vi starter med å dele $x^3$ med $x^2$ som gir $x$, etterfulgt av å trekke fra $x\cdot(x^2 - 3x + 2) = x^3 - 3x^2 + 2x$:

\begin{align*}
& (\quad x^3 - 5x^2 + 3x - 1) \div (x^2 - 3x + 2) = x^2 \\
& \,\,\, -x^3 + 3x^2 - 2x & \\
\hline
& \quad\quad\,\,\,\, -2x^2 + x - 1 & \\
\end{align*}

Steg 2
: Nå sitter vi igjen med et andregradspolynom $-2x^2 + x - 1$. Vi gjentar med å dele med høyeste potens av $x$ i polynomet med høyeste potens i nevneren. Derfor deler vi $-2x^2$ med $x^2$ som gir $-2$ til kvotienten vår. Deretter trekker vi fra $-2\cdot(x^2 - 3x + 2) = -2x^2 + 6x - 4$:

\begin{align*}
& (\quad x^3 - 5x^2 + 3x - 1) \div (x^2 - 3x + 2) = x^2 - 2 \\
& \,\,\, -x^3 + 3x^2 - 2x & \\
\hline
& \quad\quad\,\,\,\, -2x^2 + x - 1 & \\
& \quad\quad\,\,\,\,\, 2x^2 - 6x + 4 & \\
\hline
& \quad\quad\quad\quad\,\,\,\, -5x + 3 & \\
\end{align*}

Steg 3
: Nå sitter vi igjen med et førstegradspolynom $-5x + 3$. Siden graden til polynomet er lavere enn graden til polynomet i nevneren, så kan vi ikke dele videre. Vi får derfor en rest på $r(x) = -5x + 3$ og kan skrive ned resultatet vårt som

$$
(x^3 - 5x^2 + 3x - 1) \div (x^2 - 3x + 2) = x^2 - 2 + \frac{-5x + 3}{x^2 - 3x + 2}
$$
```

````{admonition} Eksempel 2 (tredjegradspolynom delt med andregradspolynom)
:class: eksempel
Vi tenker oss at vi skal utføre polynomdivisjonen

$$
(x^3 - 3x + 1) \div (x^2 - 2)
$$

Fremgangsmåten er ganske lik, bortsett fra at vi nå deler med $x^2$ og ikke med $x$. 

Steg 1
: Vi starter med å dele $x^3$ med $x^2$ som gir $x$, etterfulgt av å trekke fra $x(x^2 - 2) = x^3 - 2x$:

\begin{align*}
& (\quad x^3 - 3x + 1) \div (x^2 - 2) = x \\
& -x^3 + 2x & \\
\hline
& \quad\quad\quad\, -x + 1 & \\
\end{align*}

Steg 2
: Det vi kan merke oss nå er at siden $-x + 1$ er et førstegradsspolynom, så kan vi fortsette å dele dette med $x^2 - 2$. Derfor blir resten vår $-x + 1$ og vi har at 

$$
(x^3 - 3x + 1) \div (x^2 - 2) = x + \frac{-x + 1}{x^2 - 2}
$$
````

```{admonition} Underveisoppgave 1
:class: note
Utfør polynomdivisjonen

$$
(x^3 - 6x^2 - 3x + 2) \div (x^2 - x - 6)
$$
```

````{dropdown} Løsning
Polynomdivisjonen gir
```{figure} ./figurer/underveisoppgaver/generell_polynomdivisjon_underveisoppgave1.svg
:scale: 200%
```
````