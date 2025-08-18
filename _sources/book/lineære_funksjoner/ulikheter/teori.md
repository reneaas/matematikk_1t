# Lineære ulikheter

:::{goals} Læringsmål
* Kunne løse lineære ulikheter grafisk, algebraisk ved regning og med CAS.
:::

Vi skal se på tre strategier for å løse lineære ulikheter:
1. **Grafisk løsning**: Vi tegner grafen til ulikheten og ser hvilke verdier som oppfyller den.
2. **Algebraisk løsning**: Vi løser ulikheten ved å bruke algebraiske metoder, som å isolere variabelen. Dette kan vi gjøre ved regning eller med CAS. 



## Grafisk løsning

For å løse en lineær ulikhet grafisk, tegner vi grafen til den tilhørende lineære funksjonen og ser hvilke verdier som oppfyller ulikheten. Dette innebærer først å lete etter skjæringspunkter, og deretter sjekke om grafen ligger over eller under en graf. La oss se på et eksempel:


:::::::::::::::{example} Eksempel 1
Nedenfor vises grafen til funksjonen

$$
f(x) = 2x - 4
$$

Bruk grafen til å løse ulikheten 

$$
f(x) \geq 0
$$

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{solution}
---
dropdown: 0
---
Grafen til $f$ skjærer $x$-aksen i $x = 2$. Siden vi skal bestemme når $f(x) \geq 0$, må vi sjekke hvor grafen til $f$ ligger over eller på $x$-aksen. Vi ser fra grafen at når $x > 2$ ligger grafen over $x$-aksen. Siden grafen til $f$ er på $x$-aksen når $x = 2$, så er løsningen av ulikheten 

$$
x \geq 2.
$$
::::


:::::::::::::::

---

La oss se på et eksempel der vi har en annen type ulikhet: 


:::{margin}
Det er sjelden vi faktisk tegner den horisontale linja som i Eksempel 2. Vanligvis visualiserer vi den bare, mens vi tegner grafen til den lineære funksjonen. 
:::

:::::::::::::::{example} Eksempel 2
Løs ulikheten 

$$
2x - 1 < 3
$$


::::{solution}
---
dropdown: 0
---
Vi tegner først grafen til $f(x) = 2x - 1$ og så undersøker vi hvor grafen til $f$ ligger under linja $y = 3$. 

:::{figure} ./figurer/eksempler/eksempel_2/figur.svg
---
class: no-click, adaptive-figure
width: 90%
---
:::

Vi ser at grafen til $f$ skjærer linja $y = 3$ når $x = 2$. Vi ser også at grafen til $f$ ligger under denne linja så lenge $x < 2$. Dermed er løsningen av ulikheten

$$
x < 2 \liff x \in \langle \gets , 2 \rangle.
$$




::::


:::::::::::::::

---

La oss se på et siste eksempel der vi har en ulikhet der både venstre og høyre side er lineære funksjoner:


:::::::::::::::{example} Eksempel 3
Løs ulikheten

$$
x - 2 \leq -x + 4
$$

::::{solution}
---
dropdown: 0
---
Vi tegner grafene til 

$$
f(x) = x - 2 \qog g(x) = -x + 4
$$

:::{figure} ./figurer/eksempler/eksempel_3/figur.svg
---
class: no-click, adaptive-figure
width: 90%
---
:::

Løsningen av ulikheten vil være mengden av $x$-verdier der grafen til $f$ ligger under eller på grafen til $g$. Grafene skjærer hverandre når $x = 3$. Før dette punktet, så ligger grafen til $f$ under grafen til $g$ som betyr at løsningen av ulikheten er

$$
x \in \langle \gets , 3].
$$


::::


:::::::::::::::


## Algebraisk løsning

### Ved regning

Å løse lineære ulikheter algebraisk likner en del på å løse lineære likninger. Den store forskjellen ligger i hvordan vi håndterer ulikhetstegnene. Når vi jobber med en lineær likning, trenger vi ikke tenke oss om når vi ganger med et negativt tall på hver side av likheten. Når det kommer til en lineær ulikhet, må vi imidlertid holde tunga rett i munnen å passe på at vi snur ulikhetstegnet når vi ganger eller deler med et negativt tall.

La oss se på et eksempel. 


:::{margin}
Vi kan forstå hvorfor vi må snu ulikhetstegnet fra følgende tankegang. Hvis vi ganger hver side av ulikheten 

$$
2 < 4
$$

med $(-1)$ *uten* å snu ulikhetstegnet, så får vi 

$$
-2 < -4
$$

Men dette er ikke sant. Men dersom vi snur ulikhetstegnet når vi ganger med $(-1)$, så får vi

$$
-2 > -4
$$

som er sant!
:::

:::::::::::::::{example} Eksempel 4
Løs ulikheten

$$
2x - 1 < 3x + 2
$$


::::{solution}
---
dropdown: 0
---
Vi starter med å trekke fra $3x$ på hver side av ulikheten:

$$
2x - 1 - 3x < 3x + 2 - 3x
$$

Dette gir oss

$$
-x - 1 < 2
$$

Deretter plusser på vi på $1$ på hver side:

$$
-x - 1 + 1 < 2 + 1
$$

som gir oss 

$$
-x < 3.
$$

Så ganger vi med $(-1)$ på hver side av ulikheten, men da må vi passe på at vi snur ulikhetstegnet:

$$
-x \cdot (-1) > 3 \cdot (-1) \liff x > -3. 
$$

Dermed er løsningen av ulikheten

$$
x \in \langle -3, \to \rangle.
$$

::::

:::::::::::::::


### Med CAS

Vi kan få datamaskinen til å løse lineære ulikheter for oss og gi et svar på samme måte som vi ville fått dersom vi utførte regningen selv. La oss se på et eksempel:


::::{margin}
Bruk gjerne CAS-vinduet til å utføre regningen i Eksempel 5.

:::{cas-popup}
:::
::::


:::::::::::::::{example} Eksempel 5


Løs ulikheten 

$$
2x + 3 < -3x + 5
$$


::::{solution}
---
dropdown: 0
---
Vi bruker CAS til å løse ulikheten slik som vi viser i gif-en nedenfor:



:::{figure} ./videoer/cas.gif
---
class: no-click, adaptive-figure
width: 100%
---
:::

Fra gif-en ser vi at løsningen er 

$$
x < \dfrac{2}{5}
$$



::::



:::::::::::::::


<!-- ## Løsning med programmering
Å løse ulikheter med programmering handler har mye til felles med hvordan vi løser lineære likninger. Men for å gjøre dette effektivt, har vi bruk for en ny type løkke som kalles for en `while`{l=python}-løkke. En `while`{l=python}-løkke lar oss gjenta en kodeblokk så lenge en betingelse er sann. Dette er nyttig når vi ikke vet på forhånd hvor mange ganger vi må gjenta koden, som ofte er tilfellet når vi jobber med ulikheter.

:::::::::::::::{explore} Utforsk 1
Nedenfor vises en `while`{l=python}-løkke som skriver ut noen tall i en tallfølge.
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises en `while`{l=python}-løkke som skriver ut noen tall i en tallfølge.

Les programmet og prøv å forutsi hvilke tall programmet skriver ut.


:::{interactive-code}
---
predict:
---
x = -3
while x <= 3:
    print(x)
    
    x = x + 1 # øker verdien til x med 1


:::

:::::::::::::



:::::::::::::{tab-item} b
Nedenfor vises et program som bruker en `while`{l=python}-løkke for å løse en lineær ulikhet. 

Les programmet og bruk utskriften til å bestemme løsningen av ulikheten.


:::{interactive-code}
x = -10
while 2*x - 6 < 0: # så lenge 2x - 6 < 0 ...
    x = x + 0.125 # øker verdien til x med 0.125

print(x)

:::


:::::::::::::



::::::::::::::


::::::::::::::: -->