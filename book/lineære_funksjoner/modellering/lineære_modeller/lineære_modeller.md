# Lineære modeller

Ettersom det finnes mange ulike matematiske modeller, finnes det også flere ulike metoder for å komme frem til matematiske modeller. Første steg er å velge ut hvilke variabler som er relevante for problemet. Men måten vi går frem for å bestemme en matematisk modell kan variere fra situasjon til situasjon. Typisk kan vi kategorisere dette inn i to hovedmetoder:
* Vi antar en rimelig sammenheng mellom den uavhengige og avhengige variabelen, og setter opp en funksjon som beskriver denne sammenhengen.
* Vi bruker datamateriale til å bestemme en matematisk modell.

Men i alle tilfeller må vi velge ut en funksjonstype. Her skal vi naturligvis begrense oss til at alle modeller vi ser på beskrives som lineære funksjoner.

## Identifisere variablene og sette opp en funksjon
I noen tilfeller velger å vi ut to variabler som vi tror har en sammenheng mellom seg, og så lager vi en funksjon som uttrykker denne sammenhengen. 

::::{admonition} Eksempel 1
---
class: example
---
Hvis du skal leie en el-sparkesykkel fra Voi, må du betale $10$ kr for å låse opp sparkesykkelen og $3$ kr per minutt du leier den. 

Sett opp en modell som gir hvor mye du må betale for å leie en el-sparkesykkel i $x$ minutter.

:::{admonition} Løsning
---
class: solution
---
En passende modell vil være en lineær modell der $f(x)$ gir prisen i kroner for å leie i $x$ minutter. Modellen vår er derfor på formen

$$
f(x) = ax + b.
$$

Siden startprisen er $10$ kr, vet vi at $f(0) = 10$. Dette gir oss at $b = 10$. Videre vet vi at prisen øker med $3$ kr for hvert minutt som betyr at stigningstallet er $a = 10$. Dermed er modellen vår beskrevet av 

$$
f(x) = 3x + 10.
$$

:::

::::

---

:::::{admonition} Underveisoppgave 1
---
class: check
---
Et annen el-sparkesykkelselskap har en annen prismodell. For å leie en el-sparkesykkel hos dette selskapet i $x$ minutter, er prisen i kroner gitt ved

$$
f(x) = 8x + 12.
$$

Hvor mye koster det å låse opp sparkesykkelen, og hvor mye koster det å leie sparesykkelen per minutt? 

::::{admonition} Fasit
---
class: answer, dropdown
---
Stigningstallet er $a = 8$ som betyr at det koster $8$ kr per minutt å leie sparkesykkelen. Konstantleddet er $b = 12$ kr som betyr at det koster $12$ kr å låse opp sparkesykkelen.
::::
:::::


## Definisjonsmengde og verdimengde

Funksjonene vi har arbeidet så langt med i 1T, har stort sett vært definert for alle mulige verdier av $x$ - vi tenker da på det som at så lenge vi ikke gjør en regneoperasjon som er udefinert (som å dele på null eller ta roten av et negativt tall), så kan vi regne ut $f(x)$. For lineære funksjoner, finnes det ingen $x$-verdier for vi ikke kan regne ut $f(x)$, men det finnes likevel praktiske situasjoner hvor det ikke gir mening å bruke alle mulige verdier av $x$ - spesielt i en situasjon hvor $x$ har en praktisk betydning. På tilsvarende vis finnes det funksjonsverdier $f(x)$ som heller ikke nødvendigvis gir mening ut ifra en praktisk situasjon. Dette gir opphav til begrepene **definisjonsmengde** og **verdimengde**, som vi ser nærmere på i boksen under.

:::::{admonition} Definisjonsmengde og Verdimengde
---
class: theory
---
Definisjonsmengde $D_f$
: Mengden av alle verdier $x$ som vi kan bruke til å regne ut funksjonsverdier $f(x)$.

Verdimengde $V_f$
: Mengden av alle funksjonsverdier $f(x)$ som vi kan få fra $x$-verdiene i definisjonsmengden.

::::{figure} ./figurer/teori/teori_1.svg
---
name: fig-lineære-funksjoner-modellering-lage-modell-teori
width: 80%
---
viser grafisk hva som er definisjonsmengden $D_f$ og verdimengden $V_f$ til en lineær funksjon $f$. 
::::
:::::

---

:::::{admonition} Eksempel 1
---
class: example
---
Under vises tre eksempler på lineære funksjoner og deres definisjonsmengde og verdimengde. Legg merke til symbolene for de to mengdene for hver funksjon.

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} Figur 1

$$
D_f = \langle 3, 8]  \quad \text{og} \quad V_f = \langle 1, 6]
$$ 

:::{figure} ./figurer/eksempler/eksempel_2/figur_1.svg
---
width: 80%
---
viser en lineær funksjon $f$ som har definisjonsmengde $D_f = \langle 3, 8]$ og verdimengde $V_f = \langle 1, 6]$.
:::


````

````{tab-item} Figur 2

$$
D_g = [2, 6] \quad \text{og} \quad V_g = [4, 8]
$$

:::{figure} ./figurer/eksempler/eksempel_2/figur_2.svg
---
width: 80%
---
viser en lineær funksjon $g$ som har definisjonsmengde $D_g = [2, 6]$ og verdimengde $V_g = [4, 8]$.
:::

````

````{tab-item} Figur 3

$$
\displaystyle{D_h = \langle 2, 6 \rangle \quad \text{og} \quad V_h = \langle 3, 5 \rangle}
$$

:::{figure} ./figurer/eksempler/eksempel_2/figur_3.svg
---
width: 80%
---
viser en lineær funksjon $h$ som har definisjonsmengde $D_h = \langle 2, 6 \rangle$ og verdimengde $V_h = \langle 3, 5 \rangle$.
:::

````

`````

:::::

---

::::{admonition} Eksempel 2
---
class: example
---
Alle lineære funksjoner vi har sett på opptil nå, har vært definert for alle verdier av $x$. Dermed kan vi skrive at definisjonsmengden til disse lineære funksjonene $f$ er 

$$
D_f = \mathbb{R}.
$$

Ved å bruke *alle* mulige $x \in \mathbb{R}$, vil man kunne lage alle mulige funksjonsverdier $f(x) \in \mathbb{R}$. Derfor kan vi også konkludere at verdimengden er

$$
V_f = \mathbb{R}. 
$$
::::

---

::::{admonition} Underveisoppgave 1
---
class: check
---
Test forståelsen din med quizen!

:::{raw} html
---
file: quiz/quiz_1/quiz_1.html
---
:::

::::

---

## Praktisk betydning av definisjonsmengde og verdimengde
I praktiske situasjoner finnes det ofte begrensninger på hva som gir mening å bruke som $x$-verdier, og hva som gir mening som $f(x)$-verdier. Da setter vi opp definisjonsmengde og verdimengde ut ifra hva som gir mening i den praktiske situasjonen. 

::::{admonition} Eksempel 3
---
class: example
---
Prisen $P(t)$ for å leie en elsparkesykkel i $t$ minutter er beskrevet av funksjonen

$$
P(t) = 10 + 2t.
$$

Bestem definisjonsmengden og verdimengden til $P$.

:::{admonition} Løsning
---
class: solution
---
Vi kan ikke leie sparkesykkelen et negativt antall minutter som betyr at $t \geq 0$ . Definisjonsmengden blir derfor 

$$
D_P = [0, \to \rangle.
$$ 

Fra $P(t)$ kan vi se at $P(0) = 10$ (startprisen for å leie sparkesykkelen). Verdien til $P(t)$ vil bare øke når vi øker verdien til $t$. Derfor vil verdimengden til $P$ være 

$$
V_P = [10, \to \rangle.
$$

:::

::::
