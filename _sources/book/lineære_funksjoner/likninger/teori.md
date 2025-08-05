# Lineære likninger

:::{goals} Læringsmål
* Kunne løse lineære likninger grafisk.
* Kunne løse lineære likninger algebraisk.
* Kunne tolke programmer som løser lineære likninger, og skrive egne programmer som løser lineære likninger.
:::

En lineær likning kan generelt sett skrives på formen 

$$
ax + b = cx + d
$$

der uttrykkene på venstre og høyre side kan tolkes som lineære funksjoner. Vi har tre mulige strategier vi kan bruke for å angripe disse likningene:
1. **Grafisk løsning**: Vi bruker grafene til funksjonene og leser av løsningen. 
2. **Algebraisk løsning**: Vi løser likningen ved å bruke algebraiske metoder der målet er å få $x$ alene. 
3. **Løsning med programmering**: Vi skriver et program som finner løsningen ved å bruke ulike strategier for å finne en tallverdi for $x$ slik at likningen er oppfylt.


## Grafisk løsning
Når vi løser en lineær likning grafisk, tegner vi grafene til funksjonene på hver side av likningen og leser av skjæringspunktet mellom dem. Løsningen av likningen er da $x$-koordinaten til skjæringspunktet. 



:::{margin}
I noen oppgaver vil du bare få oppgitt grafer og så er oppgaven din å løse en likning. Da kan du velge å gjøre dette ved hjelp av grafene. Ofte sparer du tid på å bruke denne metoden når du allerede har grafene klare.
:::

:::::::::::::::{example} Eksempel 1
En likning er gitt ved 

$$
2x + 1 = 3x - 2
$$

Løs likningen grafisk.

::::{solution}
---
dropdown: 0
---
Vi tegner grafene til funksjonene

$$
f(x) = 2x + 1 \quad \text{og} \quad g(x) = 3x - 2
$$

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Fra figuren ovenfor kan vi se at grafene til $f$ og $g$ skjærer hverandre i punktet $(3, 7)$. Men det er $x$-koordinaten som løser likningen, som betyr at løsningen av likningen er 

$$
x = 3.
$$

::::

:::::::::::::::


---


Typisk må vi faktisk tegne grafen når vi skal løse likningen. Da kan vi bruke graftegneren i Geogebra og løse likningen grafisk. La oss se på et eksempel:




:::::::::::::::{example} Eksempel 2
En likning er gitt ved 

$$
3x - 1 = -4
$$

Nedenfor ser du en gif som viser hvordan man løser likningen med grafvinduet i Geogebra. Vi trykker på {ggb-icon}`mode_intersect` (Skjæring mellom to objekt) etterfulgt av å trykke på hver graf for å finne skjæringspunktet.

:::{figure} ./videoer/grafisk_løsning.gif
---
class: no-click, adaptive-figure
width: 100%
---
:::

Fra gif-en ser vi at skjæringspunktet mellom grafen til $y = 3x - 1$ og linja $y = -4$ er $(-1, -4)$. Det er $x$-koordinaten til skjæringspunktet som er løsningen av likningen, så løsningen er

$$
x = -1
$$

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1

Løs likningen nedenfor grafisk. 

$$
x - 1 = -x + 3
$$

:::{ggb}
:::


::::{answer}
$$
x = 2.
$$
::::

::::{solution}
Vi tegner grafene til funksjonene på venstre og høyre side av likningen og finner skjæringspunktet mellom dem ved å bruke "skjæring mellom to objekt" {ggb-icon}`mode_intersect`. Se figuren nedenfor:


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/sol.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at skjæringspunktet er $(2, 1)$. Det er $x$-koordinaten til skjæringspunktet som er løsningen av likningen, så løsningen er

$$
x = 2.
$$
::::


:::::::::::::::



Grafisk løsning gir oss en visuell måte å komme fram til løsningen av en likning, men den har en klar begrensning. Ved mindre vi kan lese av eksakte skjæringspunkter, vil vi i beste fall kunne finne en tilnærmet verdi for løsningen av likningen. I slike tilfeller trenger vi en annen strategi hvis vi skal komme fram til nøyaktige svar, og det er der algebraisk løsning kommer inn i bildet.



## Algebraisk løsning



Algebraisk løsning handler om å få $x$ alene slik at vi kan lese av verdien $x$ må ha for at likningen skal være oppfylt. Dette kan vi gjøre ved å
1. Legge til eller trekke fra et ledd på begge sider av likningen.
2. Gange eller dele alle ledd på hver side av likningen med et tall som ikke er null. Det er også lov med variabler.

Vi går løs på et eksempel

:::::::::::::::{example} Eksempel 3
Løs likningen

$$
2x + 1 = 3x - 2
$$

::::{solution}
---
dropdown: 0
---
Vi kan starte med å trekke fra $2x$ på begge sider av likningen:

$$
2x + 1 - 2x = 3x - 2 - 2x
$$

som gir 

$$
1 = x - 2
$$

Deretter kan vi legge til $2$ på begge sider av likningen:

$$
1 + 2 = x - 2 + 2
$$

som gir 

$$
3 = x
$$

Dermed er løsningen av likningen 

$$
x = 3.
$$
::::

:::::::::::::::


## Algebraisk løsning med CAS
Vi kan også bruke CAS til å løse lineære likninger algebraisk. Dette innebærer at vi lar datamaskinen utføre den algebraiske utregningen for oss og gir oss svaret. 

:::::::::::::::{explore} Eksempel 4
Nedenfor ser du en *gif* som viser hvordan man løser en likning med CAS.

:::{figure} ./videoer/cas-likninger.gif
---
width: 80%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::



Bruk CAS-vinduet til å løse likningen akkurat slik det vises i *gif-en* ovenfor. 


:::::::::::::

:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



Bruk CAS-vinduet til å løse likningen 

$$
4x - 6 = x + 3
$$

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS-vinduet til å løse likningen 

$$
3x - 2 = \dfrac{1}{2}x + 1
$$

:::::::::::::



::::::::::::::


:::::::::::::::




## Løsning med programmering

Når vi løser likninger med programmering, er en vanlig strategi å systematisk prøve ut mange forskjellige verdier av $x$ for å se om likningen er oppfylt. Før vi går videre, bør du repetere hvordan vi lager tallfølger med `for`{l=python}-løkker så du husker hvordan vi kan lage mange forskjellige verdier av $x$. 

:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen! 

:::{quiz}
Q: Hvilke tall skrives ut av programmet? <pre><code class="python">for x in range(-2, 3):\n    print(x)</code></pre>
+ $-2, -1, 0, 1, 2$
- $-2, 3$
- $-2, -1, 0, 1, 2, 3$
- $-2, 0, 3$

Q: Hvilke tall skrives ut av programmet? <pre><code class="python">for x in range(2, 6):\n    print(x)</code></pre>
+ $2, 3, 4, 5$
- $2, 3, 4, 5, 6$
- $2, 6$
- $2, 5$

Q: Hvilke tall skrives ut av programmet? <pre><code class="python">for x in range(-5, 6, 2):\n    print(x)</code></pre>
+ $-5, -3, -1, 1, 3, 5$
- $-5, 6, 2$
- $-5, 2, 6$
- $-5, -3, -1, 1, 3, 5, 6$

Q: Hvilke tall skrives ut av programmet? <pre><code class="python">for x in range(-3, 4, 1):\n    print(x)</code></pre>
+ $-3, -2, -1, 0, 1, 2, 3$
- $-3, -2, -1, 0, 1, 2, 4$
- $-3, 4, 1$
- $-3, 1, 4$



:::


:::::::::::::::


---

:::{margin}
Siden vi bare sjekker heltall med strategien, så er det ikke sikkert at vi finner en løsning selv om det finnes en. Vi skal senere se på strategier der vi kan finne løsninger selv når de ikke er heltall.
:::

Strategien vi skal se på her, går ut på å prøve ut heltallige verdier for $x$ og sjekke om likningen er oppfylt for noen av dem.

:::::::::::::::{explore} Utforsk 1
Programmet nedenfor prøver ut noen heltallsverdier for $x$ og sjekker om en likning er oppfylt.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet og svar på følgende:

1. Hvilken likning er det programmet prøver å løse?
2. Hvordan skiller skrivemåten for å sjekke om en likning er oppfylt seg fra når vi definerer variabler?
3. Hvilken verdi er det programmet skriver ut? Skriv inn forutsigelsen din og sjekk svaret ditt.

:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det løser likningen

$$
4x - 6 = x + 3
$$

:::::::::::::


:::::::::::::{tab-item} c
Endre på programmet og prøv å bruke det til å løse likningen

$$
3x - 1 = x + 2
$$

Kan du forklare hvorfor du ikke får en løsning med programmet?

:::::::::::::

::::::::::::::


:::{interactive-code} 
---
predict: 
---
for x in range(-5, 6):
    if 2*x - 1 == -x + 2:
        print(x)
:::


:::::::::::::::


Strategien ovenfor har en klar begrensning: Den sjekker bare heltallige verdier for $x$, og bare innenfor et begrenset intervall. Det betyr at vi ikke nødvendigvis finner en løsning selv om det faktisk finnes en. Senere skal vi se på strategier som gjør at vi kan komme rundt denne begrensningen og finne løsninger likevel.