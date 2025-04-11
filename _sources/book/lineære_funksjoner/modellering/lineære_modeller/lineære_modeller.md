# Lineære modeller

::::{admonition} Læringsmål
---
class: tip
---
Etter det delkapitlet, er målet at du skal:
* Kunne forklare og lage lineære modeller for praktiske situasjoner.
* Kunne beskrive og bestemme definisjonsmengden og verdimengden til en lineær funksjon i en praktisk situasjon.

::::

Lineære modeller er en type matematisk modell som beskriver en sammenheng mellom to variabler $x$ og $y$ der vi antar at sammenhengen mellom dem er lineær, som vil si at 

$$
y = ax + b
$$

der $a$ og $b$ er koeffisientene til modellen. Når vi snakker om lineære modeller, kaller vi ofte koeffisientene for **parametere**. 

## Lage lineære modeller for praktiske situasjoner

I en del tilfeller er det rimelig å anta en lineær sammenhengen mellom to variabler $x$ og $y$. Vi ser på en slik situasjon i eksempel 1.

::::{admonition} Eksempel 1
---
class: example
---
Hvis du skal leie en el-sparkesykkel fra Voi, må du betale $10$ kr for å låse opp sparkesykkelen og $3$ kr per minutt du leier den. 

Sett opp en lineær modell $f$ slik at $f(x)$ gir prisen i kroner for å leie sparkesykkelen i $x$ minutter.

:::{admonition} Løsning
---
class: solution
---
Modellen vår har formen

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
Et annet el-sparkesykkelselskap har en annen prismodell. For å leie en el-sparkesykkel hos dette selskapet i $x$ minutter, er prisen i kroner gitt ved

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

---

Når vi skriver $y = f(x)$, antar vi at $x$ bestemmer verdien til $y$. Da sier vi at $x$ er den **uavhengige** variabelen og $y$ er den **avhengige** variabelen.

:::::{admonition} Oppsummering: lage lineære modeller
---
class: summary
---
Gitt en **uavhengig** variabel $x$ og en **avhengig** variabel $y$, kan vi lage en lineær modell $f$ som beskriver sammenhengen mellom $x$ og $y$ på formen

$$
f(x) = ax + b
$$

der $y = f(x)$. 

> Når vi jobber med lineære modeller, kaller vi ofte koeffisientene $a$ og $b$ for **parameterne** til modellen. 

:::::

---


## Definisjonsmengde og verdimengde

To nye typer mengder som hører til en funksjon $f$ er **definisjonsmengden** $D_f$ og **verdimengden** $V_f$. Rent praktisk betyr dette at hvis vi har grafen til $f$, vil de to mengdene inneholde følgende tall:

* **Definisjonsmengde $D_f$** – Mengden av alle $x$-verdier som ligger på grafen til $f$.
* **Verdimengde $V_f$** – Mengden av alle $f(x)$-verdier ($y$-verdier) som ligger på grafen til $f$.

La oss prøve å forstå dette gjennom et par eksempler.

:::::{admonition} Eksempel 1
---
class: example
---
Under vises tre eksempler på lineære funksjoner og deres definisjonsmengde og verdimengde. I figurene har vi marker med klammeparentes hvis endepunktet er inkludert i mengden, og vinkelparentes hvis ikke. 

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} Figur 1

For grafen til $f$ har vi at 

$$
x \in \langle 3, 8] \quad \text{og} \quad f(x) \in \langle 1, 6]
$$

Dermed er definisjonsmengden og verdimengden til $f$ gitt ved

$$
D_f = \langle 3, 8]  \quad \text{og} \quad V_f = \langle 1, 6]
$$ 

:::{figure} ./figurer/eksempler/eksempel_2/figur_1.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser en lineær funksjon $f$ som har definisjonsmengde $D_f = \langle 3, 8]$ og verdimengde $V_f = \langle 1, 6]$.
:::


````

````{tab-item} Figur 2

Fra grafen til $g$ kan vi se at 

$$
x \in [2, 6] \quad \text{og} \quad g(x) \in [4, 8].
$$

Derfor er definisjonsmengden og verdimengden til $g$ gitt ved

$$
D_g = [2, 6] \quad \text{og} \quad V_g = [4, 8]
$$

:::{figure} ./figurer/eksempler/eksempel_2/figur_2.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser en lineær funksjon $g$ som har definisjonsmengde $D_g = [2, 6]$ og verdimengde $V_g = [4, 8]$.
:::

````

````{tab-item} Figur 3

Fra grafen til $h$ kan vi se at 

$$
x \in \langle 2, 6 \rangle \quad \text{og} \quad h(x) \in \langle 3, 5 \rangle.
$$

Dermed er definisjonsmengden og verdimengden til $h$ gitt ved

$$
\displaystyle{D_h = \langle 2, 6 \rangle \quad \text{og} \quad V_h = \langle 3, 5 \rangle}
$$

:::{figure} ./figurer/eksempler/eksempel_2/figur_3.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser en lineær funksjon $h$ som har definisjonsmengde $D_h = \langle 2, 6 \rangle$ og verdimengde $V_h = \langle 3, 5 \rangle$.
:::

````

`````

:::::


---

:::::{admonition} Oppsummering: Definisjonsmengde og Verdimengde
---
class: summary
---
For en funksjon $f$, kan vi gi flere tolkninger av definisjonsmengde og verdimengde ut ifra hvilken representasjon vi bruker. 

Definisjonsmengde $D_f$
: Mengden av alle $x$-verdier som vi kan bruke til å regne ut funksjonsverdier $f(x)$.
: Mengden av alle $x$-verdier som ligger på grafen til $f$. 

Verdimengde $V_f$
: Mengden av alle funksjonsverdier $f(x)$ som vi kan få fra $x$-verdiene i definisjonsmengden.
: Mengden av alle $f(x)$-verdier ($y$-verdier) som ligger på grafen til $f$.  

::::{figure} ./figurer/teori/teori_1.svg
---
name: fig-lineære-funksjoner-modellering-lage-modell-teori
width: 80%
class: no-click, adaptive-figure
---
viser grafisk hva som er definisjonsmengden $D_f$ og verdimengden $V_f$ til en lineær funksjon $f$. 
::::
:::::

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
I praktiske situasjoner finnes det ofte begrensninger på hva som gir mening å bruke som $x$-verdier, og hva som gir mening som $f(x)$-verdier. Da setter vi opp definisjonsmengden og verdimengden ut ifra hva som gir mening i den praktiske situasjonen. 

::::{admonition} Eksempel 3
---
class: example
---
Prisen i $f(x)$ kroner for å leie en el-sparkesykkel i $x$ minutter var i eksempel 1 gitt ved funksjonen

$$
f(x) = 3x + 10.
$$

Sparkesykkelselskapet tillatter bare at du leier sparkesykkelen i inntil 90 minutter.

Hva er definisjonsmengden og verdimengden til $f$ i denne situasjonen?

:::{admonition} Løsning
---
class: solution
---
Den minste mulige tiden vi kan leie en sparkesykkel må være $0$ minutter som betyr at $x \geq 0$. Men vi kan heller ikke leie sparkesykkelen i mer enn 90 minutter, som betyr at $x \leq 90$. Dette betyr derfor at

$$
x \geq 0 \, \land \, x \leq 90 \quad \iff \quad 0 \leq x \leq 90 \quad \iff \quad x \in [0, 90].
$$

Derfor blir definisjonsmengden

$$
D_f = [0, 90]. 
$$

For å bestemme den tilhørende verdimengden, kan vi merke oss at $f$ vokser hele tiden og vi kan derfor se at verdimengden blir avgrenset av $f(0)$ og $f(90)$. Dette gir oss begrensningene

$$
f(0) = 10 \quad \text{og} \quad f(90) = 280.
$$

Derfor er verdimengden

$$
V_f = [10, 280]. 
$$

Den praktiske tolkningen av dette er at vi kan ikke betale mindre enn 10 kroner (hvis vi leier i 0 minutter) og ikke mer enn 280 kroner (hvis vi leier i 90 minutter).
:::

::::
