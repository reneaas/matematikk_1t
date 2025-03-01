# Eksponentialfunksjoner


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne veksle mellom prosentvis endring og vekstfaktor. 
* Kunne sette opp og tolke eksponentialfunksjoner i praktiske situasjoner.
* Kunne skrive enkle programmer som bruker prosentvis endring og eksponentiell vekst. 
* Kunne lage skreddersydde modeller som kombinerer eksponentiell vekst med andre modeller.
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


:::::{admonition} Quiz 1
---
class: quiz
---
Ta quizen! Flere svaralternativer kan være riktig.

:::{raw} html
---
file: ./quiz/teori/quiz_1/quiz_1.html
---
:::

:::::



---

## Vekstfaktor

Når en størrelse øker eller minker med en viss prosent, vil forholdet mellom mellom den nye verdien $N$ og den gamle verdien $G$ være noe vi kaller for **vekstfaktoren** $V$ til endringen. Vi skriver

$$
V = \dfrac{N}{G} \liff N = G \cdot V.
$$

Det kan da være naturlig å lure på om vi kan finne en generell beskrivelse av vekstfaktoren $V$ dersom vi vet hvor mange prosent $p$ en størrelse øker eller minker. Vi vet at verdien før endringen $G$ skal endres med en prosent $p$, så vi kan derfor skrive at verdien etter endringen er

$$
N = G + \underbrace{p \cdot G}_{\text{prosentvis endring}} = G \cdot (1 + p)
$$

Sammenlikner vi de to likningene over, må vi nødvendigvis konkludere at vekstfaktoren generelt sett kan uttrykkes som 

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

---

Prøv deg på Underveisoppgave 1 før du går videre!

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem vekstfaktoren $V$ ved en økning på $30 \%$. 

:::::{admonition} Løsning
---
class: solution, dropdown
---
Siden det er en økning på $30 \%$, setter vi $p = 30 \% = 0.3$. Vekstfaktoren er dermed

$$
V = 1 + p = 1 + 0.3 = 1.3.
$$
:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem vekstfaktoren ved en nedgang på $12 \%$.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Siden det er en nedgang på $12 \%$, setter vi $p = -12 \% = -0.12$. Vekstfaktoren er dermed

$$
V = 1 + p = 1 - 0.12 = 0.88.
$$
:::::

:::::::::::::

::::::::::::::

:::::::::::::::


---

:::::::::::::::{admonition} Quiz 2 
---
class: quiz 
---
Ta quizen! 

:::{raw} html
---
file: ./quiz/teori/quiz_2/quiz_2.html
---
:::

:::::::::::::::



---

Prøv deg på Underveisoppgave 2 der du skal bruke vekstfaktor for å regne ut verdien etter prosentvise endringer!

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
En vare koster $120 \, \text{kr}$. Varen øker først med $20 \%$ og deretter synker den med $10 \%$. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem prisen på varen etter den har økt med $20 \%$.

:::::{admonition} Løsning
---
class: solution, dropdown
---
Verdien før endringen er $G = 120 \ \text{kr}$. Varen øker med en prosent $p = 20 \%$ så vi kan regne ut vekstfaktoren som 

$$
V = 1 + p = 1 + 20 \% = 1 + 0.2 = 1.2.
$$

Prisen etter økningen er dermed 

$$
N_1 = G \cdot V = 120 \ \text{kr} \cdot 1.2 = 144 \ \text{kr}. 
$$
:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem verdien til varen etter den har sunket med $10 \%$.

:::::{admonition} Løsning
---
class: solution, dropdown
---
Verdien til varen er nå $N_1 = 144 \ \text{kr}$. Varen synker med en prosent $p = -10 \%$ så vi kan regne ut vekstfaktoren som

$$
V = 1 + p = 1 - 10 \% = 1 - 0.1 = 0.9.
$$

Prisen etter nedgangen er dermed

$$
N_2 = N_1 \cdot V = 144 \ \text{kr} \cdot 0.9 = 129.6 \ \text{kr}.
$$
:::::

:::::::::::::


::::::::::::::


:::::::::::::::


## Eksponentialfunksjoner
Vi tenker oss at en størrelse $a$ endres med en fast prosent $p$ gjentatte ganger. Vekstfaktoren blir da $V = 1 + p$ og er den samme for hver endring. Vi tenker oss at $N_0 = a$ er verdien *før* noen prosentvis endring har funnet sted. Verdien etter én endring $N_1$ blir da

$$
N_1 = N_0 \cdot V = a \cdot V
$$

Etter to endringer blir verdien $N_2$

$$
N_2 = N_1 \cdot V = a \cdot V \cdot V = a \cdot V^2.
$$

Vi tar med endringen etter tre endringer $N_3$ også:

$$
N_3 = N_2 \cdot V = a \cdot V^2 \cdot V = a \cdot V^3.
$$

Fra regningen over, er det tydelig at vi kan generalisere mønsteret til at verdien etter $x$ endringer er

$$
N(x) = a \cdot V^x
$$

der $a$ er startverdien $N(0) = a$ og $V$ er vekstfaktoren for den faste prosentvise endringen.


:::::{admonition} Eksponentialfunksjoner
---
class: summary
---
En **eksponentialfunksjon** $f$ er en funksjon på formen

$$
f(x) = a \cdot b^x, 
$$

der $a \in \mathbb{R} \setminus \{0\}$ og $b \in \langle 0, \to\rangle$ er konstanter. Den praktiske tolkningen av konstantene er:
* $a$ er "startverdien" $f(0)$.
* $b$ er **vekstfaktoren**.

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
name: eksponentialfunksjoner-representasjoner-grafisk-representasjon
width: 80%
---

viser den grafiske representasjonen av eksponentialfunksjoner for ulike verdier av $b$. Grafen skjærer $y$-aksen i $y = a$.
:::
:::::

> Du merket kanskje at vi byttet ut $V$ med $b$ i den generelle definisjonen av eksponentialfunksjoner. Det er ikke noe spesiell grunn til dette annet at det er vanligere å bruke $b$ for vekstfaktoren i eksponentialfunksjoner, så vi skal også følge denne konvensjonen.


:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Nedenfor vises to eksempler på eksponentialfunksjoner.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} Funksjon 1

$$
f(x) = 1 \cdot 2^x
$$

:::{figure} ./figurer/eksempler/eksempel_1/a.svg
---
width: 100%
class: no-click
---
viser grafen til $f(x) = 1 \cdot 2^x$. Vi kan se at $f(x)$ dobler seg for hver verdi av $x \in \mathbb{N}$ og at grafen skjærer $y$-aksen i $y = 1$. 
:::

:::::::::::::

:::::::::::::{tab-item} Funksjon 2

$$
f(x) = 100 \cdot \left(\dfrac{1}{2}\right)^x 
$$

:::{figure} ./figurer/eksempler/eksempel_1/b.svg
---
width: 100%
class: no-click
---
viser grafen til $f(x) = 100 \cdot \left(\dfrac{1}{2}\right)^x$. Vi kan se at $f(x)$ halverer seg for hver verdi av $x \in \mathbb{N}$ og at grafen skjærer $y$-aksen i $y = 100$.
:::


:::::::::::::
::::::::::::::


:::::::::::::::


---

## Eksponentielle modeller

Som vi beskrev innledningsvis, så er eksponentialfunksjoner egnet for å beskrive en del prosesser der noe vokser eller minker med en fast prosentvis endring. Her skal vi se på et par eksempler der vi bruker en eksponentialfunksjon som en modell for en praktisk situasjon. Når vi bruker en eksponentialfunksjon som en modell for en praktisk situasjon, kaller vi modellen for en **eksponentiell modell**.

Vi starter med et eksempel der vi kan sette opp en eksponentiell modell direkte fra informasjonen som er oppgitt. 

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
En bakteriekultur består av $100$ bakterier. Hver time øker antallet bakterier med $80 \%$ per time.


> Her velger du selv om du vil se på løsning med CAS i Geogebra eller Python. 

````{tab} Geogebra

<br>

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Lag en modell $f$ som gir $f(x)$ bakterier etter $x$ timer.


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = 100 \cdot 1.8^x
$$

::::

::::{admonition} Løsning
---
class: dropdown, solution
---
Siden antall bakterier øker med en fast prosent $80 \%$ per time, vil vekstfaktoren i modellen være 

$$
b = 1 + 80 \% = 1 + 0.8 = 1.8. 
$$

Bakteriekulturen består opprinnelig av $100$ bakterier, som betyr at $f(0) = a = 100$. Dermed får vi modellen

$$
f(x) = 100 \cdot 1.8^x. 
$$

::::

:::::::::::::

:::::::::::::{tab-item} b
Bestem hvor mange timer det tar før det er $1000$ bakterier i bakteriekulturen. 


::::{admonition} Løsning
---
class: solution
---
For å bestemme hvor lang tid det tar før det er $1000$ bakterier i bakteriekulturen, kan vi løse likningen 

$$
f(x) = 1000. 
$$

Vi bruker CAS til dette:

:::{raw} html
---
file: ./ggb/eksempler/eksempel_2/b.html
---
:::

<br>

Fra løsningen med CAS finner vi at $x \approx 3.92$ som betyr at det tar ca. 4 timer før det er 1000 bakterier i bakteriekulturen.

::::

:::::::::::::

::::::::::::::


````


````{tab} Python 

<br>

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Lag en modell $f$ som gir $f(x)$ bakterier etter $x$ timer.


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = 100 \cdot 1.8^x
$$

::::

::::{admonition} Løsning
---
class: dropdown, solution
---
Siden antall bakterier øker med en fast prosent $80 \%$ per time, vil vekstfaktoren i modellen være 

$$
b = 1 + 80 \% = 1 + 0.8 = 1.8. 
$$

Bakteriekulturen består opprinnelig av $100$ bakterier, som betyr at $f(0) = a = 100$. Dermed får vi modellen

$$
f(x) = 100 \cdot 1.8^x. 
$$

::::


:::::::::::::

:::::::::::::{tab-item} b
Bestem hvor mange timer det tar før det er $1000$ bakterier i bakteriekulturen. 


::::{admonition} Løsning
---
class: solution 
---
For å bestemme hvor lang tid det tar før det er $1000$ bakterier i bakteriekulturen, kan vi løse likningen 

$$
f(x) = 1000. 
$$

Vi bruker CAS til dette:

:::{raw} html
---
file: ./python/eksempler/eksempel_2/b.html
---
:::

<br>

Kjører vi programmet (gjør det!), finner vi at utskriften blir 

:::{code-block} console
x = 3.917
:::

som betyr at det tar ca. $4$ timer før det er $1000$ bakterier i bakteriekulturen.

::::

:::::::::::::


::::::::::::::

````

:::::::::::::::

---

Vi tar et eksempel der vi bruker regresjon til å bestemme en eksponentiell modell. 



:::::::::::::::{admonition} Eksempel 3
---
class: example 
---
En pasient får en medisin. I tabellen nedenfor vises konsentrasjonen av medisinen i $\mathrm{mg}/\mathrm{mL}$ i blodet til pasienten ved ulike tidspunkter etter at pasienten fikk medisinen.

| Tid (minutter) | Konsentrasjon ($\mathrm{mg}/\mathrm{mL}$) |
|-------------|------------------------------------------|
| 0           | 3.00                                      |
| 5          | 2.70                                      |
| 10          | 2.43                                      |
| 15          | 2.19                                      |
| 20          | 1.97                                      |
| 25          | 1.77                                      |
| 30          | 1.59                                      |

<br>

1. Bestem en modell $K$ som gir konsentrasjonen $K(x)$ i $\mathrm{mg}/\mathrm{mL}$ i blodet til pasienten etter $x$ minutter.

2. Bruk modellen til å bestemme når pasienten har mindre enn $1 \, \mathrm{mg}/\mathrm{mL}$ medisin i blodet.

:::::{admonition} Løsning
---
class: solution
---

````{tab} Geogebra 

* Vi definerer en liste med datapunktene i en liste med navn `data`.
* Vi bruker `Reg`-kommandoen i CAS for å lage eksponentialfunksjon.
* Vi løser likningen $K(x) = 1$ for å finne hvor mange minutter det tar før pasienten har mindre enn $1.5 \, \mathrm{mg}/\mathrm{mL}$ medisin i blodet.

:::{raw} html 
---
file: ./ggb/eksempler/eksempel_3/eksempel_3.html
---
:::

<br>

Fra CAS-vinduet kan vi se at det tar ca. 52 minutter før pasienten har mindre enn $1 \, \mathrm{mg}/\mathrm{mL}$ medisin i blodet.

````


````{tab} Python 

Vi lager modellen med regresjon i Python og løser likningen $K(x) = 1$ for å finne hvor mange minutter det tar før pasienten har mindre enn $1 \, \mathrm{mg}/\mathrm{mL}$ medisin i blodet.


:::{raw} html 
---
file: ./python/eksempler/eksempel_3/eksempel_3.html
---
:::

<br>

Kjører vi programmet (gjør det!) så finner vi at 

1. $K(x) = 3.001 \cdot 0.979^x$.
2. $x = 51.779$ som betyr at det tar omtrent 52 minutter før konsentrasjonen er mindre enn $1 \, \mathrm{mg}/\mathrm{mL}$.



````

:::::

:::::::::::::::











