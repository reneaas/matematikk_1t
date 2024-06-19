# Algebraisk løsning
På samme måte som vi kan løse lineære likninger algebraisk (ved hjelp av algebra), kan vi også løse likningssystemer algebraisk. Antakeligvis har du gjort det på ungdomsskolen også. I så fall kan det hende du husker at det finnes to ulike metoder for å løse likningssystemer ved regning, addisjonsmetoden og innsettingsmetoden. Addisjonsmetoden er den enkleste, men den vil ikke fungere like godt på alle likningssett. Derfor er det en god idé å kunne bruke begge metodene. 

## Addisjonsmetoden
Addisjonsmetoden brukes på likningssystemer der vi kan eliminere en av variablene ved å **addere** (legge sammen) de to likningene, eller **subtrahere** (trekke fra) den ene fra den andre. Vi kan også gjøre dette etter å ha **multiplisert** en av likningene med et tall først. Vi adderer/subtraherer *venstre side* for seg og *høyre side* for seg. 

\begin{align}
    x - y & = -1 \\
    x + y & = 1 \\
\end{align}

I eksempelet vi har sett på tidligere, ser vi at dersom vi legger sammen de to likningene, vil vi få:

\begin{align}
    (x - y) + (x + y) &= -1 + 1 \\
    2x  & = 0 \\
    x & = 0 \\
\end{align}

Vi ser at $x = 0$. Når vi løser likningssystemer, må vi også huske å bestemme $y$. Det gjør vi vet å sette inn $x$ i en av likningene:

\begin{align}
    0 + y & = 1 \\
    y & = 1 \\
\end{align}

Vi ser at likningssettet har løsningen $x = 0, y = 1$, som stemmer med det vi fant da vi løste likningssettet grafisk. 

Vi kan også forsøke å bruke addisjonsmetoden på et mer komplisert likingssystem: 

````{admonition} Underveisoppgave 1
:class: note
Prøv å løse likningsystemet først. 

\begin{align}
    2x + y &= 5 \\
    x - 3y &= 6  \\
\end{align}

```{dropdown} Løsning

Her er ikke løsninen like åpenbar, men vi kan for eksempel multiplisere den nederste likningen med 2 og deretter trekke den fra den øverste. 

\begin{align}
    2x + y - (2x - 6y) &= 5 - 12\\
    7 y &= -7 \\
    y &= -1
\end{align}

Deretter setter vi $y$ inn i en av likningene og finner $x$: 

\begin{align}
    2x + (-1) &= 5
    2x &= 6
    x &= 3
 \end{align}

 Vi får da at løsningen er $x = 3, y=-1$. 

```
````

## Innsettingsmetoden
I underveisoppgaven over brukte vi addisjonsmetoden, men her kunne vi like gjerne ha brukt innsettingsmetoden. Innsettingsmetoden går ut på at vi velger oss ut en av likningene og løser denne slik at vi får den ene variabelen alene. Deretter setter vi likningen inn i den andre, og slik *eliminerer* vi en variabel. 

vi starter med det samme eksempelet som tidligere: 

\begin{align}
    2x + y &= 5 \\
    x - 3y &= 6  \\
\end{align}

Her kan vi for eksempel velge å ta utgangspunkt i den andre likningen, og løse denne for $x$. Da får vi: 

$$ x = 6 + 3y$$

Deretter setter vi det inn i den første likningen, løser likningen og får: 

\begin{align}
    2\left(6 + 3y\right) + y &= 5\\
    12 + 6y + y = 5 \\
    12 + 7y &= 5 \\
    7y  &= 5 - 12 \\
    7y &= -7 \\
    y &= -1 \\
\end{align}

Deretter gjør vi som tidligere og setter $y$ inn i en av likningene for å finne $x$. 

\begin{align}
    2x + (-1) &= 5
    2x &= 6
    x &= 3
 \end{align}

 Vi får da at løsningen er $x = 3, y=-1$. 

 ## Oppgaver 
 ---
 ### Oppgave 1
Løs likningssettene ved regning og sett prøve på svaret. 

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

```{dropdown} Fasit
1)  $x = 2, y = 1$
2) $ x = \frac{9}{5}, y = \frac{-13}{5}$
3) $ x= 1, y = 2$
4) $ x = \frac{-3}{2}, y = -4$    
    
```
---
### Oppgave 2
I vinter-OL i 2014 tok Norge til sammen 16 gull- og sølvmedaljer. En gullmedalje gir 7 olympiske poeng, og en sølvmedalje gir 5 olympiske poeng. Norge fikk til sammmen 102 olympiske poeng for sine gull- og sølvmedaljer. 

Bruk disse opplysningene til å bestemme hvor mange gullmedaljer Norge tok i vinter-OL i 2014. 

```{dropdown} Løsning
Vi identifiserer variablene $g$ for gullmedaljer og $s$ for sølvmedaljer, og setter opp to likninger basert på opplysningene over: 

\begin{align}
    g + s &= 16 \\
    7g + 5s &= 102 \\
\end{align}

Vi bruker innsettingsmetoden. Først løser vi den første likningen for $s$ og får $s = 16 - g$. Deretter setter vi den inn i den andre likningen og får: 

\begin{align}
    7g + 5s &= 102 \\
    7g + 5(16-g) &= 102\\
    7g +  80 - 5g &= 102 \\
    2g &= 102 - 80 \\
    2g &= 22 \\
    g &= 11
\end{align}

Norge fikk 11 gullmedaljer. Vi setter det inn i likningen for $s$ og får at $s = 16 - g = 16 - 11 = 5$. Norge fikk dermed 11 gullmedaljer og 5 sølvmedaljer. 

```
---
### Oppgave 3
På gården til Truls er det griser og høns. I følge Truls, har disse dyrene til sammen 40 ben og 24 øyne.

1) Finn ut hvor mange griser og hvor mange høns Truls har på gården sin. 
2) Anta deretter at det i tillegg til griser og høns, er et ukjent antall stålormer på gården. Det totale antall øyne og ben er det samme som før. Hvor mange griser, hvor mange høns og hvor mange stålormer har Truls på gården sin nå?

```{dropdown} Løsning
1) Vi identifiserer variablene $g$ for griser og $h$ for høns, og setter opp to likninger basert på opplysningene over: 

\begin{align}
    2g + 2h &= 24 \\
    4g + 2h &= 40 \\
\end{align}

Vi bruker addisjonsmetoden og trekker den første likningen fra den andre. Vi får da: 

\begin{align}
    4g + 2h - (2g + 2h) &= 40 - 24\\
    4g - 2g + 2h - 2h &= 16 \\
    2g &= 16 \\
    g &= 8 \\
\end{align}

Dermed må Truls ha 8 griser. Vi setter dette inn i likninga for øyne og får 

\begin{align}
    2g + 2h &= 24 \\
    2\cdot 8 + 2h &= 24 \\
    16 + 2h = 24 \\
    2h &= 8 \\
    h = 4 \\
\end{align}

Vi ser dermed at det må være 8 griser og 4 høns på gården. 

2) Stålorm har to øyne, men ingen ben. Vi får da likningssettet: 
\begin{align}
    2g + 2h + 2o &= 24 \\
    4g + 2h + &= 40 \\
\end{align}

Vi ser at vi nå har tre ukjente og to likninger. Det betyr at likningssystemet vil ha flere løsninger. Men ettersom vi velger å se på dyr på en gård, kan vi sette som en betingelse at variablene skal være heltall eller 0. Til å løse dette kan vi bruke glidere i GeoGebra, men vi kan også prøve oss frem. Fra oppgave 1) vet vi at 0 stålorm er en løsning. Vi lager en tabell for å prøve ut andre mulige antall stålorm: 

Dersom vi setter antallet stålorm til 1, vil det være 11 griser og høns til sammen (fordi det er 22 øyne igjen). Disse har til sammen 40 bein. Det betyr at 9 dyr må ha 4 bein, og to dyr 2 bein. 

|Stålorm | Griser | Høns |
| --- | --- | --- |
| 0 | 8 | 4 |
| 1 | 9 | 2 |
| 2 | 10 | 0 |

Dersom vi øker antallet ytterligere, vil vi få negativt antall høns, noe vi ikke tillater. Det er derfor kun tre mulige løsninger av likningssystemet. 
```



