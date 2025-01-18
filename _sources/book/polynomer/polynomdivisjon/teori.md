# Polynomdivisjon


::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive og utføre polynomdivisjon. 
* Kunne forklare hva som er kvotient og rest i en polynomdivisjon, og forklare hva resten forteller oss om dividenden.
* Kunne bruke polynomdivisjon til å regne ut funksjonsverdier.
::::

::::{admonition} Divisjon: Begreper
--- 
class: theory
---
Når vi deler et tall $a$ med et tall $b$, kan vi alltid skrive utregningen som 


$$
\dfrac{a}{b} = k + \dfrac{r}{b}
$$

der 

* $a$ kalles for **dividenden**
* $b$ kalles for **divisoren**
* $k$ kalles for **kvotienten**
* $r$ kalles for **resten**

Disse begrepene vil også gjelde dersom vi deler polynomer, som vi snart skal se på.
::::

Polynomdivisjon er en metode for å dele et polynom med et annet polynom og skrive det på en enklere måte. Før vi ser på dette, skal vi motivere hvorfor vi trenger polynomdivisjon i det hele tatt. Følgende setning forteller oss hvorfor. 

:::::{admonition} Algebraens fundamentalsetning for tredjegradspolynomer
---
class: theory
---
Et tredjegradspolynom $f(x)$ kan alltid skrives som et produkt av et førstegradspolynom og et andregradspolynom

$$
f(x) = (x - r)(ax^2 + px + q). 
$$

Her er $x = r$ et nullpunkt for $f$. Andregradspolynomet kan ha ingen, ett eller to nullpunkter.
:::::

Setningen over forteller oss at hvis vi klarer å finne en faktor $(x - r)$ som deler $f(x)$, så får vi et andregradspolynom. Siden vi vet hvordan vi bestemmer alle egenskapene til andregradspolynomer allerede, betyr det at vi har en mulig metode for å finne ut alt om tredjegradspolynomer også. 

Vårt neste steg er derfor å se på en algoritme for å dele et polynom med en faktor $(x - r)$. Vi starter med å se på et eksempel med et andregradspolynom.


## Polynomdivisjon uten rest

::::::::::::::::{admonition} Eksempel 1
---
class: example
---
Utfør polynomdivisjonen:

$$
(3x^2 + 3x - 6) : (x + 2). 
$$


:::::::::::::::{admonition} Løsning
---
class: solution
---
For å utføre divisjonen, følger vi disse stegene: 

::::::::::::::{tab-set}
:::::::::::::{tab-item} Steg 1
Først finner vi hva vi må gange $(x + 2)$ slik at vi får $3x^2$ som høyeste potens av $x$. Dette er $3x$. Deretter trekker vi fra $3x(x + 2)$ fra $(3x^2 + 3x - 6)$.

::::{figure} ./koder/eksempler/eksempel_1/stage_3.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::

:::::::::::::{tab-item} Steg 2
Nå er resten vår $-3x - 6$. Vi må derfor finne hva vi må gange $(x + 2)$ med for at vi skal få $-3x$ som ett av leddene. 

Dette er $-3$. Deretter trekker vi fra $-3(x + 2)$ fra $(-3x - 6)$.

::::{figure} ./koder/eksempler/eksempel_1/stage_6.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::


:::::::::::::{tab-item} Steg 3
Legger vi sammen de to linjene, så sitter vi igjen med $0$ i rest, og vi er ferdig med divisjonen.

::::{figure} ./koder/eksempler/eksempel_1/stage_7.svg
---
width: 60%
class: no-click
---
::::

:::::::::::::
::::::::::::::



Hele utregningen kan derfor skrives ned som: 


::::{figure} ./koder/eksempler/eksempel_1/eksempel_1.svg
---
width: 60%
class: no-click
---
::::

Utregningen vår forteller oss at 

$$
\dfrac{3x^3 + 3x - 6}{x + 2} = 3x - 3 \liff 3x^2 + 3x - 6 = (x + 2)(3x - 3).
$$

:::::::::::::::
::::::::::::::::

---


Vi ser på et eksempel til med et tredjegradspolynom i telleren. 

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Utfør polynomdivisjonen

$$
(x^3 - 3x^2 - 6x + 8) : (x + 2).
$$

::::::::::::::{admonition} Løsning
---
class: solution
---

:::::::::::::{tab-set}

::::::::::::{tab-item} Steg 1
Vi starter med å dele høyeste potens av $x$ i teller som er $x^3$ med høyeste potens av $x$ i nevner som er $x$. Dette gir $x^2$. 


:::{figure} ./koder/eksempler/eksempel_2/stage_2.svg
---
width: 80%
class: no-click
---
:::

::::::::::::

::::::::::::{tab-item} Steg 2
Vi ganger svaret fra steg 1 med $(x + 2)$ som gir $x^2(x + 2) = x^3 + 2x^2$. Deretter trekker vi fra dette fra $(x^3 - 3x^2 - 6x + 8)$.

:::{figure} ./koder/eksempler/eksempel_2/stage_3.svg
---
width: 80%
class: no-click
---
:::

::::::::::::

::::::::::::{tab-item} Steg 3
Vet å regne ut differansen fra steg 2, får vi polynomet $-5x^2 - 6x + 8$ (men merk at vi ikke trekker ned alle tallene før vi trenger dem i divisjonen). 


:::{figure} ./koder/eksempler/eksempel_2/stage_4.svg
---
width: 80%
class: no-click
---
:::


::::::::::::


::::::::::::{tab-item} Steg 4

Vi deler leddet med høyeste potens av $x$ fra det resterende polynomet som er $-5x^2$ med høyeste potens av $x$ i nevner som er $x$. Dette gir $-5x$.

:::{figure} ./koder/eksempler/eksempel_2/stage_5.svg
---
width: 80%
class: no-click
---
:::

::::::::::::


::::::::::::{tab-item} Steg 5
Vi ganger tilbake svaret fra steg 4 med $(x + 2)$ som gir $-5x(x + 2) = -5x^2 - 10x$. Deretter trekker vi fra dette fra $( -5x^2 - 6x + 8)$ og legger sammen.


:::{figure} ./koder/eksempler/eksempel_2/stage_7.svg
---
width: 80%
class: no-click
---
:::

::::::::::::

::::::::::::{tab-item} Steg 6
Vi deler leddet med høyeste potens av det resterende polynomet som er $4x$ med høyeste potens av $x$ i nevner som er $x$. Dette gir $4$. 
Deretter vi svaret $4$ med $(x + 2)$ som gir $4(x + 2) = 4x + 8$ og trekker dette fra det resterende polynomet. Da får vi $0$.


:::{figure} ./koder/eksempler/eksempel_2/stage_10.svg
---
width: 80%
class: no-click
---
:::

::::::::::::


:::::::::::::


Vi kan oppsummere hele regnestykket som følger: 

:::{figure} ./koder/eksempler/eksempel_2/eksempel_2.svg
---
width: 80%
class: no-click
---
:::

Utregningen forteller oss at 

$$
\dfrac{x^3 - 3x^2 - 6x + 8}{x + 2} = x^2 - 5x + 4,
$$

som betyr at 

$$
x^3 - 3x^2 - 6x + 8 = (x + 2)(x^2 - 5x + 4).
$$

::::::::::::::

:::::::::::::::


---

Vi kan også utføre polynomdivisjon når divisoren er et andregradspolynom.


:::::::::::::::{admonition} Eksempel 3
---
class: example
---
Utfør polynomdivisjonen 

$$
(x^3 - 8x^2 + 21x - 18) : (x^2 - 6x + 9). 
$$


::::::::::::::{admonition} Løsning
---
class: solution
---

:::{figure} ./koder/eksempler/eksempel_3/eksempel_3.svg
---
width: 85%
class: no-click
---
:::

Utregningen forteller oss at

$$
\dfrac{x^3 - 8x^2 + 21x - 18}{x^2 - 6x + 9} = x - 2
$$

som betyr at vi kan skrive at

$$
x^3 - 8x^2 + 21x - 18 = (x - 2)(x^2 - 6x + 9).
$$

::::::::::::::

:::::::::::::::



## Polynomdivisjon med rest

Som vi så i begynnelsen av dette delkapittelet, så er $f(x)$ bare delelig med en faktor $(x - r)$ hvis faktoren er i $f(x)$. Hvis ikke vil vi få en **rest** i divisjonen. Vi skal ta et eksempel som viser hvordan dette ser ut:


:::::::::::::::{admonition} Eksempel 4
---
class: example
---
Regn ut 

$$
(x^3 - 5x^2 + 8x - 4) : (x - 3).
$$

::::::::::::::{admonition} Løsning
---
class: solution
---
Vi utfører polynomdivisjon:


:::{figure} ./koder/eksempler/eksempel_4/eksempel_4.svg
---
width: 90%
class: no-click
---
:::

Ved å følge stegene som før, får vi nå $2$ i rest. Dette betyr at vi må legge på et ledd $\dfrac{2}{x - 3}$ siden vi ikke kan dele noe mer. Dette forteller oss at 

$$
\dfrac{x^3 - 5x^2 + 8x - 4}{x - 3} = x^2 - 2x + 2 + \dfrac{2}{x - 3}.
$$

Siden vi ikke har $0$ i rest, vil ikke $(x - 3)$ være en faktor i $x^3 - 5x^2 + 8x - 4$.
::::::::::::::

:::::::::::::::

 
I eksempel 1, 2 og 2 utførte vi polynomdivisjon som ikke ga noen rest fordi $(x - r)$ var en faktor i dividenden (telleren). I eksempel 3 fikk vi en rest som betydde at $(x - r)$ *ikke* var en faktor i dividenden. Basert på eksemplene, kan vi formulere en setning: 

:::::::::::::::{admonition} Setning: Polynomdivisjonen $f(x) : (x - r)$
---
class: summary
---
Gitt et polynom $f$, vil polynomdivisjonen $f(x) : (x - r)$ alltid kunne skrives på formen

$$
\dfrac{f(x)}{x - r} = K(x) + \dfrac{R}{x - r}
$$

der $R$ er **resten** i divisjonen og $K(x)$ er et polynom som kalles for **kvotienten**. 

:::::::::::::::

---

Setningen over har noen konsekvenser vi skal utforske videre: 


:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = x^3 + 4x^2 + x - 6.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
Regn ut $f(-1)$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(-1) = -4
$$
:::

:::::::::::::

:::::::::::::{tab-item} b
Regn ut polynomdivisjonen

$$
(x^3 + 4x^2 + x - 6) : (x + 1)
$$

Sammenlikn resten med svaret ditt fra **a**.

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./koder/utforsk/utforsk_1/utforsk_1.svg
---
width: 90%
class: no-click
---
:::

Vi kan merke oss at resten $R = -4$ og $f(-1) = -4$. Altså er resten i $(x + 1)$ og $f(-1)$ den samme.
::::

:::::::::::::

::::::::::::::



:::::::::::::::

---

Observasjonene gjort i Utforsk 1 lar oss skrive en setning som er viktig for polynomdivisjon:


:::::::::::::::{admonition} Setning: Resten i polynomdivisjon med $(x - r)$
---
class: summary
---
Gitt et polynom $f$, så er resten $R$ i polynomdivisjon $f(x) : (x - r)$ lik $R = f(r)$.

Hvis $R = 0$, betyr det at $f(r) = 0$ og $(x - r)$ er en faktor i $f(x)$. 

::::::::::::::{admonition} Bevis
---
class: dropdown, theory
---
Ved polynomdivisjon $f(x) : (x - r)$ får vi generelt

\begin{align*}
    \dfrac{f(x)}{x - r} &= K(x) + \dfrac{R}{x - r} \\
    \\
    \textcolor{red}{(x - r)} \cdot\dfrac{f(x)}{x - r} &= K(x) \cdot \textcolor{red}{(x - r)} + \dfrac{R}{x - r} \cdot \textcolor{red}{(x - r)} \\
    \\
    f(x) &= K(x) \cdot (x - r) + R \\
\end{align*}

Setter vi inn $x = r$ i den siste likningen, får vi 

$$
f(r) = K(r) \cdot (r - r) + R = R.
$$

Altså er resten $R = f(r)$ og vi har bevist setningen.

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Hjelpesetning: Resten i polynomdivisjonen $f(x) : (x - r)$
---
class: summary
---
Hvis resten i polynomdivisjonen $f(x) : (x - r)$ er $R = f(r) = 0$, så er

* $x = r$ et nullpunkt for $f$ siden $f(r) = 0$.
* $(x - r)$ er en faktor i $f(x)$.
* $f(x)$ er delelig med $(x - r)$. Noen ganger sier vi at polynomdivisjonen $f(x) : (x - r)$ "går opp" og vi skriver $(x - r) \, |  \, f(x)$ og leser det som "$(x - r)$ deler $f(x)$".

:::::::::::::::




Setningene over lar oss gjøre to ting:
* Avgjøre om et punkt $x = r$ er et nullpunkt for $f$, og dermed faktorisere $f$.
* Regne ut funksjonsverdier $f(r)$ **raskt** ved å dele med $(x - r)$ og lese av resten $R$.


Vi tar et eksempel som illustrer setningen i praksis:

:::::::::::::::{admonition} Eksempel 4
---
class: example
---
Et tredjegradspolynom $f$ er gitt ved 

$$
f(x) = x^3 - 2x^2 - 5x + 6.
$$

Regn ut $f(-1)$ ved hjelp av polynomdivisjon.

:::::{admonition} Løsning
---
class: solution
---
Vi utfører polynomdivisjon og får:

:::{figure} ./koder/eksempler/eksempel_5/eksempel_5_longdiv.svg
---
width: 90%
class: no-click
---
:::

Resten i polynomdivisjonen er $8$, og derfor er $f(-1) = 8$.
:::::

:::::::::::::::

---

## Horner-skjema

Når du leste gjennom eksempel 4 kan du ha stusset litt over en ting – hvordan i alle dager er dette mindre regning enn å bare sette inn verdien for $x$ i $f(x)$? Trikset her er at vi gjør svært mye unødvendig skriving når vi gjør polynomdivisjonen – vi kan heller bare holde styr på koeffisientene og fokusere på de viktige regnestykkene som vi skal vise i neste eksempel:

Vi skal ta i bruk noe vi kaller for et **Horner-skjema** for å utføre divisjonen. 

:::::::::::::::{admonition} Horner-skjema
---
class: summary
---
Et **Horner-skjema** kan brukes til å regne ut polynomdivisjonen $f(x) : (x - r)$. La 

$$
f(x) = a_3x^3 + a_2x^2 + a_1x + a_0
$$

og $K(x)$ være kvotienten i polynomdivisjonen gitt ved 

$$
K(x) = b_2x^2 + b_1x + b_0. 
$$


Da kan vi bestemme koeffisientene til $K(x)$ og resten $R$ ved å lage et Horner-skjema som vist under:

$$
\begin{array}{r|cccc}
 & a_3 & a_2 & a_1 & a_0 \\ % Dividend coefficients
    x = r  &   & b_2\cdot r  & b_1\cdot r  & b_0\cdot r \\ % Linear term
\hline
        & b_2 & b_1 &  b_0 & R \\ % Resulting coefficients
\end{array}
$$


der $b_2 = a_3$ og de resterende tallene $b_1, b_0$ og $R$ regnes ut ved å summere tallene i kolonnen over streken. Vi jobber oss gjennom én og én kolonne fra venstre mot høyre.


:::::::::::::::

Det viktigste å merke seg med den generelle teorien er hvor koeffisientene til telleren $f(x)$ plasseres, og hvor koeffisientene til kvotienten $K(x)$ og resten $R$ plasseres. Rent praktisk trenger vi ikke huske formlene som står i hver kolonne – det hele blir klart med et eksempel.


:::::::::::::::{admonition} Eksempel 5
---
class: example
---
Polynomdivisjonen fra eksempel 4 krever mye skriving:

:::{figure} ./koder/eksempler/eksempel_5/eksempel_5_longdiv.svg
---
width: 80%
class: no-click
---
:::

Vi kan se at mange av leddene forsvinner som en trapp, så vi trenger ikke holde styr på de leddene. Rent praktisk lager vi **Horner-skjemaet** slik:

:::{figure} ./koder/eksempler/eksempel_5/eksempel_5.gif
---
width: 60%
class: no-click
---
viser hvordan vi algoritmisk regner ut verdiene i tabellen.
:::

Prøv å sammenligne med polynomdivisjonen for å gjenkjenne hvor tallene i Horner-skjemaet dukker opp i polynomdivisjonen.


Vi kan oppsummere resultatet vi fikk med Horner-skjemaet som

:::{figure} ./koder/eksempler/eksempel_5/eksempel_5.svg
---
width: 60%
class: no-click
---
På øverste rad står koeffisientene til $f(x)$ med høyeste grad først og konstantledd til slutt. På nederste rad er de tre første tallene koeffisientene til kvotienten $K(x)$ med høyest grad til venstre og konstantledd til slutt. Det siste tallet (i rødt) på siste rad er resten $R$. 
:::

Basert på Horner-skjemaet kan vi derfor lese av at 

$$
K(x) = x^2 - 3x - 2 \quad \text{og} \quad R = 8. 
$$

Slår vi det hele sammen finner vi derfor at 

$$
(x^3 - 2x^2 - 5x + 6) : (x + 1) = x^2 - 3x - 2 + \dfrac{8}{x + 1}
$$


:::::::::::::::




---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bruk et Horner-skjema til å regne ut kvotienten $K(x)$ og resten $R$ i polynomdivisjonen 

$$
(x^3 - 4x^2 + 3x - 2) : (x - 2). 
$$

:::::{admonition} Fasit
---
class: answer, dropdown
---

:::{figure} ./koder/underveisoppgaver/underveisoppgave_1/underveisoppgave_1.svg
---
width: 60%
class: no-click
---
:::

**Kvotienten**:

$$
K(x) = x^2 - 2x - 1
$$

**Rest**:

$$
R = -4
$$

:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---

:::{figure} ./koder/underveisoppgaver/underveisoppgave_1/underveisoppgave_1_tutor.svg
---
width: 60%
class: no-click
---
:::


**Kvotienten**:

$$
K(x) = x^2 - 2x - 1
$$

**Rest**:

$$
R = -4
$$

:::::

:::::::::::::::

