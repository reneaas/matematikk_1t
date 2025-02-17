# Eksponentialfunksjoner


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne veksle mellom prosentvis endring og vekstfaktor. 
* Kunne sette opp og tolke eksponentialfunksjoner i praktiske situasjoner.
* Kunne skrive enkle programmer som bruker prosentvis endring og eksponentiell vekst. 
:::::





:::::{admonition} Eksponentialfunksjoner
---
class: summary
---
En **eksponentialfunksjon** $f$ er en funksjon på formen

$$
f(x) = a \cdot b^x, 
$$

der $a \in \mathbb{R} \setminus \{0\}$ og $b \in \langle 0, \to\rangle$ er parameterne til funksjonen.

:::{figure} ./figurer/teori/grafisk_representasjon.svg
---
name: eksponentialfunksjoner-representasjoner-grafisk-representasjon
width: 80%
---

viser den grafiske representasjonen av eksponentialfunksjoner for ulike verdier av $b$. Grafen skjærer $y$-aksen i $y = a$.
:::
:::::


---


## Prosentvis endring og vekstfaktor


## Eksponentialfunksjoner i praktiske situasjoner 



## Skreddersydde modeller

I noen praktiske situasjoner, må vi kombinere *skreddersy* modellen vår for å fange opp deler av virkeligheten vi forventer. 


:::::::::::::::{admonition} Eksempel X
---
class: example
---
En kaffekopp har en temperatur på $90^\circ \mathrm{C}$ og befinner seg i et rom med en temperatur på $20^\circ \mathrm{C}$. 

Over lang tid vil kaffekoppen og luften i rommet være i *termisk likevekt* som betyr at de vil ha samme temperatur. Siden rommet er fryktelig stort sammenlignet med kaffekoppen,
er det rimelig å anta at temperaturen i rommet ikke endrer seg til tross for varmeoverføring fra kaffen til luften i rommet. Dermed vil kaffekoppen før eller siden få en temperatur på $20^\circ \mathrm{C}$.

Nedenfor vises et datamateriale hvor det er blitt loggført temperaturen $T \, ^\circ \mathrm{C}$ i kaffekoppen $x$ minutter etter at kaffen ble satt på bordet.

| $x$ (minutter) | 0 | 5 | 10 | 15 | 20 |
|----------------|---|----|---|----|----|
| $T(x)$ ($^\circ \mathrm{C}$) | 90 | 81.9 | 74.0 | 68.0 | 62.0 |

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
