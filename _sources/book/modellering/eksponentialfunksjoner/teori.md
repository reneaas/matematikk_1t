# Eksponentialfunksjoner


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne veksle mellom prosentvis endring og vekstfaktor. 
* Kunne sette opp og tolke eksponentialfunksjoner i praktiske situasjoner.
* Kunne lage matematiske modeller ved bruk av regresjon. 
* Kunne skrive enkle programmer som bruker prosentvis endring og eksponentiell vekst. 
:::::

Eksponentialfunksjoner er en type funksjon som brukes til å beskrive prosesser der noe vokser eller minker med en fast prosentvis endring. Funksjonen dukker opp i mange sammenhenger i naturvitenskap, økonomi, samfunnsvitenskap og teknologi. 

For at vi skal kunne forstå eksponentialfunksjoner, er det viktig at vi har en god forståelse av prosentregning og vekstfaktor *først*. 

## Prosent

Når vi jobber med prosentregning, kan vi representere en prosent på tre ulike måter:

:::::{admonition} Prosent
---
class: summary
---
Tre ulike måter å representere en prosent på:

$$
\underbrace{\dfrac{30}{100}}_{\text{brøk}} = \underbrace{0.3}_{\text{desimaltall}} = \underbrace{30 \%}_{\text{prosent}}
$$

Vi kan dermed tolke at prosenttegnet betyr $\% = \dfrac{1}{100} = 0.01$.
:::::

---


:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen! Flere alternativer kan være riktig. 


:::{quiz}
Q: Hva er det samme som $20\%$
+ $0.2$
+ $\dfrac{20}{100}$
- $0.02$
- $\dfrac{2}{100}$

Q: Hva er det samme som $0.75$?
+ $75\%$
+ $\dfrac{3}{4}$
- $7.5\%$
- $\dfrac{75}{10}$

Q: Hva er det samme som $\dfrac{1}{4}$?
+ $25\%$
+ $0.25$
- $2.5\%$
- $0.025$

Q: Hva er det samme som $150\%$?
+ $1.5$
+ $\dfrac{3}{2}$
- $0.15$
- $\dfrac{15}{100}$

Q: Hva er det samme som $0.08$?
+ $8\%$
+ $\dfrac{8}{100}$
- $80\%$
- $\dfrac{8}{10}$

Q: Hva er det samme som $\dfrac{3}{5}$?
+ $60\%$
+ $0.6$
- $35\%$
- $0.35$
:::


:::::::::::::::

## Vekstfaktor

Når en størrelse øker eller minker med en viss prosent, vil forholdet mellom den nye verdien $N$ og den gamle verdien $G$ være noe vi kaller for **vekstfaktoren** $V$ til endringen. Vi skriver

$$
V = \dfrac{N}{G} \liff N = G \cdot V.
$$

Det kan da være naturlig å lure på om vi kan finne en generell beskrivelse av vekstfaktoren $V$ dersom vi vet hvor mange prosent $p$ en størrelse øker eller minker med. Vi vet at verdien før endringen $G$ skal endres med en prosent $p$, så vi kan derfor skrive at verdien etter endringen er

$$
N = G + \underbrace{p \cdot G}_{\text{prosentvis endring}} = G \cdot (1 + p)
$$

Sammenlikner vi de to likningene over, kan vi konkludere at vekstfaktoren generelt sett kan uttrykkes som 

$$
V = 1 + p. 
$$

:::::{admonition} Vekstfaktor
---
class: summary
---
Vekstfaktoren $V$ når en verdi endres med en viss prosent $p$ er gitt ved 

$$
V = 1 + p
$$

der $p$ er den prosentvise endringen. 

* $p > 0$ brukes for økning. Da er $V > 1$.
* $p < 0$ brukes for nedgang. Da er $0 < V < 1$.
:::::

:::::::::::::::{example} Eksempel 1
Bestem vekstfaktoren til $20\%$ økning. 


::::{solution}
---
dropdown: 0
---
Vekstfaktoren $V$ til $20\%$ økning er

$$
V = 100\% + 20\% = 120\% = 1.2
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
Bestem vekstfaktoren til $30\%$ nedgang.


::::{answer}
$$
V = 0.7
$$
::::

::::{solution}
Vekstfaktoren til $30\%$ nedgang er

$$
V = 100\% - 30\% = 70\% = 0.7
$$
::::


:::::::::::::::

---

## Eksponentialfunksjoner

Nå er vi klare for å se på hva en eksponentialfunksjon er. Vi skriver en eksponentialfunksjon $f$ på formen 

$$
f(x) = a \cdot b^x.
$$

For å se hva det har med en prosentregning og vekstfaktorer å gjøre, kan vi se på sammenhengen mellom $f(x)$ og $f(x + 1)$:

$$
f(x + 1) = a \cdot b^{x + 1} = \underbrace{a \cdot b^x}_{\displaystyle f(x)} \cdot b = f(x) \cdot b.
$$

Altså får vi funksjonsverdien i neste punkt $x + 1$ ved å gange funksjonsverdien i $x$ med faktoren $b$. Dermed kan vi tolke $b$ som en vekstfaktor!

:::::::::::::::{summary} Eksponentialfunksjoner

En **eksponentialfunksjon** $f$ er en funksjon på formen


:::{figure} ./figurer/teori/algebraisk_representasjon.svg
---
width: 50%
class: no-click, adaptive-figure
---
:::

der $a \in \mathbb{R} \setminus \{0\}$ og $b \in \langle 0, \to\rangle$ er konstanter.

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
name: eksponentialfunksjoner-representasjoner-grafisk-representasjon
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 2
Nedenfor vises to eksempler på eksponentialfunksjoner:

:::::{grid} 1 1 2 2
::::{grid-item-card}
$$
f(x) = 1 \cdot 2^x
$$
^^^
:::{figure} ./figurer/eksempler/eksempel_2/a.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

::::


::::{grid-item-card}
$$
f(x) = 100 \cdot \left(\dfrac{1}{2}\right)^x
$$
^^^
:::{figure} ./figurer/eksempler/eksempel_2/b.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

::::

:::::




:::::::::::::::


---

## Bestemme $f(x)$
Vi kan anvende to strategier for å bestemme funksjonsuttrykket til en eksponentialfunksjon.
1. Fra informasjon om to punkter på grafen til $f$
2. En eksponentiell modell med regresjon


La oss se på et eksempel der vi bestemme $f(x)$ ut ifra informasjon om to punkter på grafen til $f$.



:::{margin}
Bruk CAS-vinduet til å følge eksempelet!
:::

:::::::::::::::{example} Eksempel 3
En eksponentialfunksjon $f$ går gjennom punktene $(0, 2)$ og $(3, 32)$. 

::::{solution}
---
dropdown: 0
---


:::{cas-popup}
---
layout: sidebar
---
:::



En eksponentialfunksjoner er på formen

$$
f(x) = a \cdot b^x
$$

Grafen til $f$ går gjennom punktene $(0, 2)$ og $(3, 32)$ som betyr at

$$
f(0) = 2 \and f(3) = 32
$$

Vi kan bruke CAS til å bestemme verdiene til $a$ og $b$ ved hjelp av de to likningene:


:::{figure} ./videoer/cas_bestemme_funksjonsuttrykk.gif
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra gif-en ser vi at vi får at 

$$
a = 2 \and b = 2 \sqrt[3]{2}
$$

Vekstfaktoren $b$ har en eksakt verdi, men i praksis er den ikke så lett å tolke. Hvis vi trykker på {ggb-icon}`mode_numeric` får vi en tilnærmet verdi for $b$ som gir 

$$
a = 2 \and b\approx 2.52. 
$$

Det betyr at $f(x)$ er gitt ved

$$
f(x) = 2 \cdot \left(2 \sqrt[3]{2}\right)^x \approx 2 \cdot 2.52^x
$$

::::


:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 3 

:::{cas-popup}
---
layout: sidebar
---
:::


En eksponentialfunksjon $f$ går gjennom punktene $(1, 10)$ og $(3, 40)$. 

Bestem $f(x)$.


:::{clear}
:::


::::{answer}
$$
f(x) = 5 \cdot 2^x 
$$
::::

::::{solution}
En eksponentialfunksjon $f$ er på formen 

$$
f(x) = a \cdot b^x.
$$

Vi bruker CAS for å bestemme $a$ og $b$ slik at grafen til $f$ går gjennom punktet $(1, 10)$ og $(3, 40)$:

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi velge den løsningen som gir at $b \in \langle 0, \to\rangle$. Dermed får vi

$$
a = 5 \and b = 2. 
$$

Det betyr at 

$$
f(x) = 5 \cdot 2^x 
$$


::::
:::::::::::::::

---

Eksponentialfunksjoner kan brukes til å beskrive en del praktiske situasjoner. Vi sier at funksjonen **modellerer** situasjonen. Hvis en eksponentialfunksjon $f$ brukes for å modellere en praktisk situasjon, kaller vi den for en **eksponentiell modell**.

I de fleste situasjoner, ønsker vi å lage en eksponentiell modell ut ifra et datamateriale som viser hvordan to størrelser henger sammen. La oss se på et eksempel på hvordan dette gjøres:


:::{margin}
Prøv å følge eksempelet nedenfor ved å bruke CAS-vinduet!
:::

:::::::::::::::{example} Eksempel 4
:::{cas-popup}
:::

En pasient får en medisin. I tabellen nedenfor vises konsentrasjonen av medisinen i mg/mL i blodet til pasienten ved ulike tidspunkter etter at pasienten fikk medisinen.

:::{clear}
:::

| Tid (minutter) | $0$ | $5$ | $10$ | $15$ | $20$ |
|----------------|---|---|----|----|----|
| Konsentrasjon ($\mathrm{mg}/\mathrm{mL}$) | $3.00$ | $2.70$ | $2.43$ | $2.19$ | $1.97$ |


<br>

Lag en modell $K$ som gir konsentrasjonen $K(x)$ mg/mL når det har gått $x$ minutter siden pasienten har fått medisinen.


::::{solution}
---
dropdown: 0
---

Vi skriver inn punktene i en liste i CAS og bruker `RegEksp(data)` for å bestemme en eksponentiell modell $K(x)$ med regresjon. Se gif-en nedenfor.


:::{figure} ./videoer/regresjon_cas_cropped.gif
---
class: no-click, adaptive-figure
width: 100%
---
:::


Fra gif-en ser vi at modellen vi får med regresjon er gitt ved 

$$
K(x) = 3 \cdot 0.98^x
$$

::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 4

:::{cas-popup}
:::



Befolkningen i en kommune i noen av årene mellom 2015 og 2024 er vist i figuren nedenfor.

| År | 2015 | 2017 | 2018 | 2020 | 2024 |
|---|---|---|---|---|---|
| Befolkningstall | 10000 | 10404 | 10612 | 11484 | 11944 |

<br>

Bestem en eksponentiell modell $B$ som gir befolkningstallet $B(x)$ der $x$ er antall år etter 2015. Det vil si $x = 0$ er 2015, $x = 1$ er 2016 og så videre. 



::::{answer}
$$
B(x) = 10041.72 \cdot 1.02^x
$$
::::

::::{solution}
Vi skriver inn datamateriale i CAS, men passer på at vi skriver inn årstallene $x$ slik at de er antall år etter 2015. Deretter bruker vi `RegEksp(data)` for å bestemme den eksponentielle modellen:

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4/sol.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Fra utskriften ser vi at 

$$
B(x) = 10041.72 \cdot 1.02^x
$$

::::

:::::::::::::::

