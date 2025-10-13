# Lineære ulikheter

:::{goals} Læringsmål
* Kunne løse lineære ulikheter grafisk, algebraisk ved regning, med CAS og ved bruk av fortegnslinjer.
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



### Med fortegnslinjer
En annen strategi som vi kommer til å benytte oss særdeles mye av når vi skal løse ulikheter generelt, er å bruke fortegnslinjer til å løse ulikhetene. La oss først definere hva vi mener med dette begrepet.


:::::::::::::::{summary} Fortegnslinjer
En **fortegnslinje** er en linje som viser hvor en funksjon er positiv, negativ eller lik null. 
Vi bruker **heltrukne** og **stiplede** linjer for å skille mellom fortegnene:

* <span style="display:inline-block; width:100px; border-bottom: 3px solid red; vertical-align:middle;"></span> $=$ Positivt fortegn
* <span style="display:inline-block; width:100px; border-bottom: 3px dashed royalblue; vertical-align:middle;"></span> $=$ Negativt fortegn
* Vi markerer med $0$ ved nullpunktene til funksjonen.

I figuren nedenfor vises fortegnslinja til $f(x) = 2(x - 1)$. 

:::{signchart}
width: 100%
function: 2*(x - 3), f(x)
factors: false
:::




:::::::::::::::


---


Strategien vi skal bruke når vi løser ulikheter kan oppsummeres som nedenfor.


:::::::::::::::{summary} Strategi: Løsning av ulikheter med fortegnslinjer
1. Vi skriver om ulikheten slik at vi for $0$ på den éne siden av ulikheten.
2. Vi tegner fortegnslinja til $f(x)$.
3. Vi leser av løsningen til ulikheten fra fortegnslinja til $f(x)$.
:::::::::::::::

---

La oss se på et eksempel


:::::::::::::::{example} Eksempel 6
Løs ulikheten

$$
x - 3 \lt -2x + 3
$$

::::{solution}
---
dropdown: 0
---
Vi sørger for at vi for $0$ på den éne siden av ulikheten først:

$$
x - 3 \lt -2x + 3
$$

$$
x + 2x - 3 - 3 \lt 0
$$

$$
3x - 6 \lt 0
$$

Vi setter $f(x) = 3x - 6$. Da er målet vårt å løse ulikheten $f(x) \lt 0$. Først bestemmer vi nullpunktsformen til $f(x)$:

$$
f(x) = 0 \liff 3x - 6 = 0 \liff 3x = 6 \liff x = 2.
$$

Dette gir oss at $f(x) = 3(x - 2)$.

Vi tegner deretter et **fortegnsskjema** for $f(x)$ ved å tenke oss følgende:
1. Vi tegner en tallinje for $x$-aksen og markerer nullpunktet $x = 2$.
2. Vi tegner en fortegnslinje for hver av faktorene i $f(x)$ som *her* er $3$ og $(x - 2)$.
3. Ganger vi fortegnene sammen for hver del av fortegnslinja til $3$ og $(x - 2)$, får vi fortegnslinja til $f(x)$. 

Se figuren nedenfor.

:::{signchart}
width: 100%
function: 3*x - 6, f(x)
:::

Fra fortegnslinja til $f(x)$, ser vi at $f(x) \lt 0$ når $x < 2$ siden det er her fortegnslinja til $f(x)$ er stiplet. Dermed er løsningen av ulikheten

$$
x < 2 \liff x \in \langle \gets , 2 \rangle.
$$

::::

:::::::::::::::
