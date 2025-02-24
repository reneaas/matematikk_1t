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

## Prosent

Prosent kan representeres på tre måter:

:::::{admonition} Prosent
---
class: summary
---
$$
\underbrace{\dfrac{30}{100}}_{\text{brøk}} = \underbrace{0.3}_{\text{desimaltall}} = \underbrace{30 \%}_{\text{prosent}}
$$

Vi kan dermed tolke at $\% = \dfrac{1}{100}$.
:::::


## Vekstfaktor

Vi tar et eksempel som motiverer hvordan vi kan regne ut vekstfaktoren gitt en prosentvis endring.

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
En vare koster $300 \, \mathrm{kr}$. Prisen øker med $20 \%$. Hva er den nye prisen? 

:::::{admonition} Løsning
---
class: solution
---
La $P_\text{før} = 300$ være prisen før økningen og $P_\text{etter}$ være prisen etter økningen. Prisen øker med $30 \%$ som betyr at vi skal legge til $30 \%$ av $P_\text{før}$ til $P_\text{før}$ for å finne $P_\text{etter}$. Da får vi 

$$
30 \% \cdot 300 = 0.3 \cdot 300 = 90.
$$

Dermed skal den nye prisen bli 

$$
P_\text{etter} = P_\text{før} + 90 = 300 + 90 = 390. 
$$

Vi kan observere at regnestykket over kan skrives om til

$$
P_\text{etter} = P_\text{før} + 90 = 100\% \cdot P_\text{før} + 30\% \cdot P_\text{før} = 130\% \cdot P_\text{før}.
$$

Dermed kunne vi utført regnestykke direkte ved

$$
P_\text{etter} = 130\% \cdot P_\text{før} = 1.3 \cdot 300 = 390.
$$

Her er $130 \% = 1.3$ **vekstfaktoren**.
:::::

:::::::::::::::





:::::{admonition} Eksponentialfunksjoner
---
class: summary
---
En **eksponentialfunksjon** $f$ er en funksjon på formen

$$
f(x) = a \cdot b^x, 
$$

der $a \in \mathbb{R} \setminus \{0\}$ og $b \in \langle 0, \to\rangle$ er parameterne til funksjonen. Den praktiske tolkningen av parameterne er:
* $a$ er "startverdien" $f(0)$.
* $b$ er vekstfaktoren.

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
name: eksponentialfunksjoner-representasjoner-grafisk-representasjon
width: 80%
---

viser den grafiske representasjonen av eksponentialfunksjoner for ulike verdier av $b$. Grafen skjærer $y$-aksen i $y = a$.
:::
:::::

---

## Eksponentielle modeller

En **eksponentiell modell** er en matematisk funksjon som beskriver noe praktisk som vokser eller synker eksponentielt.










## Skreddersydde modeller

I noen praktiske situasjoner, må vi kombinere *skreddersy* modellen vår for å fange opp deler av virkeligheten vi forventer. 


:::::::::::::::{admonition} Eksempel X
---
class: example
---

:::::{admonition} Faktaboks: Newtons avkjølingslov
---
class: summary
---
* Newtons avkjølingslov forteller at temperaturen $T$ til et objekt vil synke proprosjonalt med forskjellen mellom objektets temperatur og omgivelsenes temperatur. 
* Temperaturen til objektet endrer seg eksponensielt.
:::::

En kaffekopp har en temperatur på $90^\circ \mathrm{C}$ og befinner seg i et rom med en temperatur på $20^\circ \mathrm{C}$. 

Nedenfor vises et datamateriale hvor det er blitt loggført temperaturen $T \, ^\circ \mathrm{C}$ i kaffekoppen $x$ minutter etter at kaffen ble satt på bordet.

| $x$ (minutter) | 0 | 5 | 10 | 15 | 20 |
|----------------|---|----|---|----|----|
| $T(x)$ ($^\circ \mathrm{C}$) | 90 | 81.9 | 74.0 | 68.0 | 62.0 |


Lag en modell $T$ som gir temperaturen $T(x) \, ^\circ \mathrm{C}$ $x$ minutter etter at kaffen ble satt på bordet.


:::::{admonition} Løsning
---
class: solution
---
Etter veldig lang tid, vil temperaturen i kaffekoppen nærme seg romtemperaturen. Vi kan derfor forvente at $y = 20$ er en horisontal asymptote for $T$. 

:::::

:::::::::::::::


:::::::::::::::{admonition} Eksempel XX
---
class: example
---
Når du ankom en hytte, viste termostaten at temperaturen var $0^\circ \mathrm{C}$. Du skrur termostaten til $20^\circ \mathrm{C}$. Du sjekker temperaturen regelmessig og notererer ned hva temperaturen er $x$ minutter etter at du skrudde på termostaten, som
gir datamateriale som er vist nedenfor. 


| $x$ (minutter) | 0 | 10 | 20 | 30 | 50 | 80 |
|----------------|---|----|---|----|----|----|
| $T(x)$ ($^\circ \mathrm{C}$) | 0 | 5.2 | 8.0 | 10.5 | 14.2 | 17.0 |

Lag en modell $T$ som gir temperaturen $T(x) \, ^\circ \mathrm{C}$ $x$ minutter etter at termostaten ble skrudd på. 


::::::::::::::{admonition} Løsning
---
class: solution
---
Her vet vi at temperaturen $T(x)$ øker med tiden $x$, men vi vet samtidig at temperaturen vil nærme seg $20^\circ \mathrm{C}$ etterhvert. Vi kan derfor forvente at dette er en horisontal asymptote for $T(x)$. 

En modell for dette kan være 

$$
T(x) = T_\mathrm{maks} + a \cdot b^x,
$$

::::::::::::::


:::::::::::::::
