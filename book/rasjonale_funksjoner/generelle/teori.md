# Generelle rasjonale funksjoner


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne bestemme horisontale eller skrå asymptoter til en rasjonal funksjon. 
* Kunne bestemme nullpunktene til en rasjonal funksjon. 
* Kunne bestemme vertikale asymptoter til en rasjonal funksjon.
* Kunne lage fortegnslinjer og skissere grafen til en rasjonal funksjon, å bruke dette til å løse rasjonale ulikheter.
:::::

---


Når vi jobbet med lineære-over-lineære rasjonale funksjoner fant vi at funksjonen alltid hadde en horisontal asymptote, en vertikal asymptote og et nullpunkt. Men for rasjonale funksjoner generelt sett, vil antall nullpunkter og vertikale asymptoter variere, og det finnes også rasjonale funksjoner som ikke har noen av delene. Men disse tre egenskapene er likevel de mest sentrale egenskapene for rasjonale funksjoner.


:::::::::::::::{admonition} Sentrale egenskaper ved rasjonale funksjoner
---
class: summary
---
For rasjonale funksjoner, er de mest sentrale egenskapene:
* **Nullpunkter**
* **Horisontale og skrå asymptoter**
* **Vertikale asymptoter**

:::::::::::::::

Målet vårt er å utvikle verktøy for å avgjøre hvilke egenskaper en rasjonal funksjon har. Men først tar vi et eksempel som illustrerer hvor variert antallet av disse egenskapene kan være – for de må slett ikke ha vertikale asymptoter, nullpunkter eller horisontale asymptoter i det hele tatt. Mangfoldet av egenskaper er for mange til å vise *alle* tilfeller, men dette vil gi oss en idé om variasjonen vi kan møte på. Deretter skal vi se på hvordan vi kan avgjøre hvilke egenskaper en rasjonal funksjon har.

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Nedenfor vises fire eksempler på rasjonale funksjoner med ulike egenskaper. Det *ikke* meningen at du skal forstå *hvorfor* grafene ser ut som de gjør enda, men få et inntrykk av hvor stort mangfold rasjonale funksjoner kan ha.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} Funksjon 1

::::{figure} ./figurer/teori/eksempel_1.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til en rasjonal funksjon $f(x) = \dfrac{(x - 2)(x + 3)}{x^2 - 1}$. Her har $f$ en horisontal asymptote $y = 1$, to vertikale asymptoter med likningene $x = \pm 1$, og to nullpunkter $x = -3$ og $x = 2$.
::::

:::::::::::::


:::::::::::::{tab-item} Funksjon 2

::::{figure} ./figurer/teori/eksempel_2.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = \dfrac{x^2 - 4}{x - 1}$. Grafen har to nullpunkter $x = \pm 2$, en vertikal asymptote i $x = 1$ og en **skrå** asymptote $y = x + 1$. Grafen til $f$ nærmer seg altså en lineær funksjon når $|x|$ blir stor.
::::

:::::::::::::


:::::::::::::{tab-item} Funksjon 3

::::{figure} ./figurer/teori/eksempel_3.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = \dfrac{1}{x - 2}$. Grafen har en vertikal asymptote i $x = 2$, men ingen nullpunkter. Grafen til $f$ har en horisontal asymptote $y = 0$.
::::

:::::::::::::

:::::::::::::{tab-item} Funksjon 4

::::{figure} ./figurer/teori/eksempel_4.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = \dfrac{x - 1}{x^2 + 1}$. Grafen har et nullpunkt i $x = 1$ og en horisontal asymptote $y = 0$. Grafen har ingen vertikale asymptoter.
::::

:::::::::::::

::::::::::::::


:::::::::::::::


## Nullpunkter

Når vi jobbet med lineære-over-lineære rasjonale funksjoner, så var det polynomet i telleren som bestemte nullpunktet. Dette var ikke tilfeldig, og dette kan vi generalisere til alle rasjonale funksjoner – med én forsiktighetsregel. 

:::::{admonition} Setning: Nullpunktene til rasjonale funksjoner
---
class: summary
---
For en rasjonal funksjon $f$ på formen 

$$
f(x) = \dfrac{P(x)}{Q(x)}
$$

har $f$ og $P$ samme nullpunkter så lenge et nullpunkt **ikke** også er et nullpunkt for $Q$.
:::::

Setningen over forteller oss at hvis vi ønsker å lete etter nullpunktene til en rasjonal funksjon $f$, trenger vi først og fremst å lete etter nullpunktene til tellerpolynomet $P$. Deretter må vi ekskludere eventuelle nullpunkter som også er nullpunkter til nevnerpolynomet $Q$. Dette er forsiktighetsregelen vi **må følge**.


:::::{admonition} Eksempel 2
---
class: example
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 - 9}{x^2 - x - 6}
$$

Bestem nullpunktene til $f$. 

::::{admonition} Løsning
---
class: solution
---
Tellerpolynomet er gitt ved 

$$
P(x) = x^2 - 9 = x^2 - 3^2 = (x + 3)(x - 3)
$$

som betyr at 

$$
P(x) = 0 \liff (x + 3)(x - 3) = 0 \liff x = -3 \or x = 3. 
$$

Det betyr at $x = \pm 3$ er kandidater for nullpunktene til $f$. Vi må sjekke nullpunktene til nevnerpolynomet $Q(x)$ for å se om $Q$ har noen av disse til felles. Dette kan vi gjøre ved å faktorisere:

$$
Q(x) = x^2 - x - 6 = (x - 3)(x + 2)
$$

som betyr at 

$$
Q(x) = 0 \liff (x - 3)(x + 2) = 0 \liff x = -2 \or x = 3
$$

Vi ser derfor at $x = 3$ også er et nullpunkt for $Q$ som betyr at det eneste nullpunktene til $f$ er $x = -3$. 
::::
:::::





## Horisontale og skrå asymptoter

Når vi jobbet med lineære-over-lineære rasjonale funksjoner, så vi at vi fikk horisontale asymptoter som var horisontale linjer som $f(x)$ nærmet seg når $|x|$ ble stor. Vi kan også få skrå asymptoter som er skrå linjer som $f(x)$ nærmer seg når $|x|$ blir stor. For å bestemme disse generelt sett, utfører vi polynomdivisjon og leser av kvotienten i polynomdivisjonen.

:::::::::::::::{admonition} Setning: Horisontale og skrå asymptoter
---
class: summary
---
La $f$ være en rasjonal funksjon på formen 

$$
f(x) = \dfrac{P(x)}{Q(x)} \, . 
$$

Da kan vi alltid utføre polynomdivisjon å skrive $f(x)$ som 

$$
f(x) = K(x) + \dfrac{R(x)}{Q(x)} \, ,
$$

der $K(x)$ er kvotienten (som er et polynom) og $R(x)$ er restpolynomet. Da gjelder følgende påstander:

* Hvis **tellergraden og nevnergraden er like**, så er $K(x) = \mathrm{konstant}$ en horisontal asymptote til $f$.
* Hvis **tellergraden er én større enn nevnergraden**, er $K(x)$ en skrå asymptote til $f$.
* Hvis **tellergraden er mindre enn nevnergraden**, er $K(x) = 0$ den horisontale asymptoten til $f$. 

:::::::::::::::

Setningen over forteller oss hvis vi skal bestemme horisontale eller skrå asymptoter til en rasjonal funksjon $f$, så må vi utføre polynomdivisjon så vi kan lese av hva **kvotienten** er. 


Vi tar et eksempel på en lineær-over-lineær rasjonal funksjon for å se at vi får samme resultat som ved avlesning slik vi har gjort så langt:

:::::::::::::::{admonition} Eksempel 3: Horisontale asymptote $y \neq 0$
---
class: example
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{-2(x - 3)}{x - 2} = \dfrac{-2x + 6}{x - 2}
$$


::::::::::::::{admonition} Løsning
---
class: solution
---
Med avlesning, kan vi se at $a = -2$ som betyr at den horisontale asymptoten til $f$ er $y = -2$. Bruker vi polynomdivisjon, får vi


:::{figure} ./koder/eksempler/eksempel_2/eksempel_2.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

Fra polynomdivisjonen, kan vi se at $K(x) = -2$ som betyr at $y = -2$ er en horisontal asymptote til $f$.

::::::::::::::

:::::::::::::::

---


Vi tar et eksempel der tellergraden er én større enn nevnergraden. 


:::::::::::::::{admonition} Eksempel 4: Skrå asymptoter
---
class: example
---

En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 + x - 2}{x + 3}
$$

Bestem eventuelle horisontale eller skrå asymptoter til $f$.

::::::::::::::{admonition} Løsning
---
class: solution
---
Siden tellergraden til $f$ er én grad høyere enn nevnergraden, kan vi forvente at $K(x)$ er et lineært polynom og at vi derfor får en skrå asymptote. Vi utfører polynomdivisjon:

:::{figure} ./koder/eksempler/eksempel_3/eksempel_3.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Dette betyr at kvotienten er 

$$
K(x) = x - 2.
$$

Dette vil være likningen til den skrå asymptoten. Grafen til $f$ vil nærme seg denne linjen når $|x|$ blir stor.
::::::::::::::

:::::::::::::::

---

Vi bør også diskutere hva som skjer når tellergraden er mindre enn nevnergraden. 

:::::::::::::::{admonition} Eksempel 5: Horisontal asymptote $y = 0$
---
class: example
---
La $f$ være en rasjonal funksjon gitt ved 

$$
f(x) = \dfrac{x - 2}{x^2 + 1}
$$

Siden tellergraden er mindre enn nevnergraden, kan vi ikke utføre polynomdivisjon – det fungerer bare hvis vi har en tellergrad som er *minst* like stor som nevnergraden. Det betyr at tellerpolynomet er **resten** og kvotienten må derfor være $K(x) = 0$. Det betyr at denne rasjonale funksjonen har en horisontal asymptote ved $y = 0$. 

> **Observasjon**: Den horisontale asymptoten er alltid $y = 0$ når tellergraden er mindre enn nevnergraden.

:::::::::::::::






## Vertikale asymptoter
Når vi jobbet med lineære-over-lineære rasjonale funksjoner, kan det hende du oppdaget at den vertikale asymptoten egentlig bare svarte til at vi delte på $0$. Med andre ord at det svarte til nullpunktet til nevneren. 
Dette gjelder nesten helt generelt, men med noen **forsiktighetsregler**. 

Men først trenger vi en definisjon av et begrep som vi kommer til å bruke stadig vekk og derfor trenger å ha en felles forståelse av: 

:::::{admonition} Definisjon: Bruddpunkter
---
class: theory
---
For en rasjonal funksjon $f$ på formen 

$$
f(x) = \dfrac{P(x)}{Q(x)}
$$

vil alle punktene $x$ der nevnerpolynomet oppfyller $Q(x) = 0$ kalles for **bruddpunktene** til $f$. Dette betyr at:
* Nullpunktene til nevnerpolynomet $Q$ er bruddpunktene til $f$.
* Bruddpunkter er punkter der $f$ ikke er definert. Disse må ekskluderes fra definisjonsmengden $D_f$ til $f$.
* Bruddpunkter er punkter $x$ der vi deler på $0$ i $f(x)$.
:::::

Men et bruddpunkt må ikke nødvenigvis gi en vertikal asymptote! Neste steg er å se når et bruddpunkt gir en vertikal asymptote, og når det bare gir et "hull" i grafen til en rasjonal funksjon.


:::::{admonition} Setning: Vertikale asymptoter til rasjonale funksjoner
---
class: summary
---
Gitt en rasjonal funksjon $f$ på formen 

$$
f(x) = \dfrac{P(x)}{Q(x)}
$$

Da er $x = r$ en vertikal asymptote hvis:
* $x = r$ er et nullpunkt for $Q$. 
* $Q(x)$ inneholder flere faktorer av $(x - r)$ enn $P(x)$ gjør.

:::::

Setningen forteller oss at 
1. Vi må finne nullpunktene til $Q$ (bruddpunktene til $f$).
2. Vi må nullpunktsfaktorisere både $P(x)$ og $Q(x)$ og sjekke om $Q(x)$ har flere lineære faktorer av typen $(x - r)$ enn $P(x)$ har for hvert nullpunkt $x = r$.

Hvis $Q(x)$ har flere lineære faktorer enn $P(x)$, vil bruddpunktet $x = r$ også gi en vertikal asymptote. Hvis ikke gir det bare et "hull" i grafen til $f$.


Vi går løs på et eksempel som viser tre spesialtilfeller som illustrerer dette poenget.


:::::::::::::::{admonition} Eksempel 6
---
class: example
---

::::::::::::::{tab-set}
:::::::::::::{tab-item} 1. Teller har flest faktorer
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{(x - 1)^2}{x - 1}
$$

Ved å forkorte så mye som mulig, kan vi skrive om $f(x)$ til

$$
f(x) = x - 1 \and x \neq 1.
$$

Her kan vi se at $f(x)$ oppfører seg som en lineær funksjon $y = x + 1$ så lenge $x \neq 1$ og den har derfor bare et "hull" i grafen sin når $x = 1$, men ikke et vertikal asymptote.

:::::::::::::


:::::::::::::{tab-item} 2. Likt i teller og nevner
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{(x + 3)^2}{(x + 3)^2}
$$

Ved å forkorte så mye som mulig, kan vi skrive om $f(x)$ til

$$
f(x) = 1 \and x \neq -3.
$$

som forteller oss at $f(x)$ oppfører seg som en konstant $1$ så lenge $x \neq -3$. Også her kan vi konkludere at $x = -3$ bare gir et "hull" i grafen og ikke en vertikal asymptote.

:::::::::::::


:::::::::::::{tab-item} 3. Nevner har flest faktorer
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x + 1}{(x + 1)^2}
$$

Ved å forkorte så mye som mulig, kan vi skrive om $f(x)$ til

$$
f(x) = \dfrac{1}{x + 1} \and x \neq -1.
$$

Her har vi flere lineære faktorer $(x + 1)$ i nevneren, som betyr at $x = -1$ er en vertikal asymptote til $f$ i tillegg til å være et bruddpunkt.

:::::::::::::

::::::::::::::

:::::::::::::::

---

Nå er det lurt at vi tar et eksempel der vi må faktorisere teller- og nevnerpolynomet for å finne vertikale asymptoter.

:::::::::::::::{admonition} Eksempel 7
---
class: example
---
En rasjonal funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 - 3x + 2}{x^2 + 2x - 3}
$$

Bestem eventuelle vertikale asymptoter til $f$.

::::::::::::::{admonition} Løsning
---
class: solution
---
For å bestemme de vertikale asymptotene til $f$, må vi først nullpunktsfaktorisere teller- og nevnerpolynomet. Ved å bruke $abc$-formelen for tellerpolynomet får vi

\begin{align*}
    x &= \dfrac{-(-3) \pm \sqrt{(-3)^2 - 4\cdot 1 \cdot 2}}{2 \cdot 1} \\
    \\
    &= \dfrac{3 \pm \sqrt{9 - 8}}{2} \\
    \\
    &= \dfrac{3 \pm 1}{2} \\
\end{align*}

som gir 

$$
x = 1 \or x = 2. 
$$

Dermed kan tellerpolynomet skrives som 

$$
x^2 - 3x + 2 = (x - 1)(x - 2)
$$

Vi bruker samme strategi for nevnerpolynomet:

\begin{align*}
x &= \dfrac{-2 \pm \sqrt{2^2 - 4 \cdot 1 \cdot (-3)}}{2 \cdot 1} \\
\\
&= \dfrac{-2 \pm \sqrt{4 + 12}}{2} \\
\\
&= \dfrac{-2 \pm \sqrt{16}}{2} \\
\\
&= \dfrac{-2 \pm 4}{2} \\
\\
&= -1 \pm 2
\end{align*}

som gir 

$$
x = -3 \or x = 1.
$$

Dette betyr at vi kan skrive nevnerpolynomet som 

$$
x^2 + 2x - 3 = (x + 3)(x - 1).
$$

Dermed kan vi skrive $f(x)$ om til

$$
f(x) = \dfrac{x^2 - 3x + 2}{x^2 + 2x - 3} = \dfrac{(x - 1)(x - 2)}{(x + 3)(x - 1)} = \dfrac{x - 2}{x + 3} \, ,
$$

så lenge $x \neq 1$. Med det forenklede uttrykket til $f(x)$ kan vi nå lete etter nullpunktene til det gjenværende nevnerpolynomet for å finne vertikale asymptoter. Dette gir: 

$$
x + 3 = 0 \liff x = -3.
$$

Dermed er $x = -3$ en vertikal asymptote til $f$, mens $x = 1$ *kun* er et bruddpunkt.



::::::::::::::

:::::::::::::::
