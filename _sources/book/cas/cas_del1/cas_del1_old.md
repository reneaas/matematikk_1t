# CAS-kurs del 1
Dette er en introduksjon til CAS. Etter hvert som du lærer mer matematikk i 1T, vil du også lære å ta i bruk flere funksjoner. 

## Finn CAS
Du finner fram til CAS ved å åpne geogebra og trykke på "hamburgermenyen" (tre streker) øverst til høyre. Klikk på denne og sørg for at CAS er huket av. 

I CAS kan du velge mellom å løse likninger eller gjøre utregninger symbolsk eller numerisk. Symbolsk-tegnet er $=$ og gir oss nøyaktige tall og brøker. Numerisk-tegnet er $\approx$ og gir oss et desimaltall. 

Du kan prøve ut dette ved å skriv inn sqrt(2) og observere at du får opp et kvadratrottegn. Du kan også få frem $\sqrt{\quad}$ ved å finne den på tastaturet. Prøv nå å trykke på $\approx$ og sammenlign med dersom du trykker på $=$. 

```{figure} ./figurer/cas0.png
:name: eks0
:width: 50%

CAS kan både regne eksakt og numerisk.
```


````{margin}
```{admonition} Tips
:class: note
Har tastaturet ditt forsvunnet? Finn tastatursymbolet nederst i høyre hjørne, så kommer du tilbake. 
```
````

## Løse likninger i CAS
Skriv inn likningen $2x + 3 = -x - 3$ i CAS. Det er lurt å sjekke at du har skrevet inn riktig før du går videre, for ellers løser du jo en helt annen likning!

Løs likningen ved å trykke på knappen som er merket med  "x=" Denne skal vi heretter kalle "Løs-knappen". 

```{figure} ./figurer/cas1.png
:name: eks1
:width: 80%

Vi kan løse likninger både numerisk og eksakt. 
```

````{admonition} Underveisoppgave 1
:class: note
Bruk CAS til å løse likningene:

1) $ 2x−10+x=x+20 $
2) $ \frac{5}{2}x+9x−2=12x $
3) $ \frac{x}{3}=12 $

```{dropdown} Løsning
1) $x = 15$
2) $ x = -4$
3) $ x = \frac{3}{2}$

```
````

## Likningssystemer
Vi kan også løse likningssystemer i CAS. Da skriver vi inn hver likning for seg, markerer linjene og trykker på Løs-knappen. 

Vi prøver med likningssettet

\begin{align}
    2x+3y-4 & =0
    2x+1 &= 2-y
\end{align}

```{figure} ./figurer/cas2.png
:name: eks2
:width: 60%

Når vi løser likningssett må vi huske å markere likningene vi skal løse.
```

````{admonition} Underveisoppgave 2
:class: note
Bruk CAS til å løse likningssettene:

1) \begin{align}
        3x+y &=7 \\
        x−y &=1 \\
    \end{align}

2) \begin{align}
        x−2y &= 7 \\
        2x+y &= 1 \\
    \end{align}

3) \begin{align}
        x+2y &= 5 \\
        4x &= 6−y \\
    \end{align}

4) \begin{align}
        −2x+y &= −1 \\
        4x+2y+14 &= 0 \\
    \end{align}

```{dropdown} Løsning
1)  $x = 2, y = 1$
2) $ x = \frac{9}{5}, y = \frac{-13}{5}$
3) $ x= 1, y = 2$
4) $ x = \frac{-3}{2}, y = -4$    
    
```
````

### Likningssystemer med flere enn to ukjente
Når vi bruker CAS, er det også lett å løse likningssystemer med flere enn to ukjente. Prøv selv!

````{admonition} Underveisoppgave 4
:class: note
Løs likningssystemet

\begin{align}
    a - b + c &= -11
    a + b + c &= 11
    8a + 4b + 2c &= -4
\end{align}

```{dropdown} Løsning
$a = -8, b = 11, c = 8$

```
````

## Ulikheter
Vi kan også løse ulikheter i CAS. Vi prøver oss frem med ulikheten $\frac{x}{3}+\frac{1}{2}\leq \frac{x}{2}+\frac{1}{3}$. Vi bruker Løs-knappen som tidligere og får $x \geq 1$, som vist under. 

```{figure} ./figurer/cas3.png
:name: eks3
:width: 40%

Vi løser ulikheter på samme måte som likninger. 
```

````{admonition} Underveisoppgave 4
:class: note
Bruk CAS til å løse ulikhetene: 

1) $ −2x+3 \geq 3x−5 $
2) $ 3(y+3) < 5(y+3) $
3) $3(x+3)-\frac{1}{2}\left(x+4\right) < x+5(x-2)$

```{dropdown} Løsning
1) $x \leq \frac{4}{3} $
2) $ x > -3$
3) $ x > \frac{34}{7}$

```
````



