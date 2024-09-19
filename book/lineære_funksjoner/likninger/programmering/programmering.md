# Løsning med programmering

:::{admonition} Læringsmål: lineære likninger med programmering
---
class: tip
---
Etter å ha gått gjennom denne delen, er målet at du skal kunne:
* Lese og tolke programmer som løser lineære likninger
* Justere og tilpasse programmer for å løse dine egne likninger
:::


## Numerisk løsning av likninger


Å løse en likning **numerisk**, betyr å finne en tilnærmet tallverdi for løsningen. For å gjøre dette bruker vi gjerne en strategi som er formulert som en oppskrift som vi kan følge for å nærme oss løsningen. En slik oppskrift kalles for en **algoritme**. Når vi har en algoritme, er målet vårt å oversette denne til et program som datamaskinen kan utføre for oss så vi kan *kick back, relax* og la datamaskinen gjøre jobben for oss. 

Her skal vi se på hvordan vi kan gjøre dette med likninger. I utforsk 1 skal du gradvis bygge opp et program som løser en lineær likning.

:::::{admonition} Utforsk 1
---
class: explore
---
Vi skal ta utgangspunkt i at vi skal bestemme nullpunktet til 

$$
f(x) = 2x - 4.
$$

Under vises et interaktivt kodevindu. 

````{tab-set}
```{tab-item} Steg 1
Se på koden i det interaktive kodevinduet. <br> Forutsi hvilke verdier av `x`{l=python} som skrives ut av programmet før du kjører det. 

Kjør koden og sjekk svaret ditt!
```

```{tab-item} Steg 2
For å bestemme nullpunktet til $f$, må vi løse likningen $f(x) = 0$. <br> Det betyr at vi trenger en funksjon som vi kan regne ut funksjonsverdier med. Kopier koden under og lim inn i kodevinduet. Erstatt `funksjonsuttrykk` med riktig funksjonsuttrykk. 
:::{code-block} python
---
linenos: true
---
def f(x):
    return funksjonsuttrykk # FYLL INN: skriv inn funksjonsuttrykket her

print(f(6))
:::

Kan du forklare hva programmet skriver ut?

::::{admonition} Fasit
---
class: dropdown, answer
---
Koden med riktig funksjonsuttrykk:
:::{code-block} python
---
linenos: true
---
def f(x):
    return 2 * x - 4

print(f(6))
:::

Programmet skrives ut funksjonsverdien $f(6)$ som er $8$.
::::

```

```{tab-item} Steg 3
En strategi for å bestemme nullpunktet til $f$ er å prøve ut mange verdier av $x$ og sjekke om $f(x) = 0$ eller ikke. 

For å sjekke om $f(x) = 0$, kan vi skrive `f(x) == 0`{l=python} der `x`{l=python} har en bestemt verdi. Typisk vil denne verdien være bestemt av en `for`{l=python}-løkke.

* Hvis påstanden $f(x) = 0$ ikke er sann, så vil `f(x) == 0`{l=python} gi `False`{l=python}. 
* Hvis påstanden $f(x) = 0$ er sann, vil `f(x) == 0`{l=python} gi `True`{l=python}.

Kopier programmet under og kjør det i kodevinduet med riktig funksjon fra steg 2.
:::{code-block} python
---
linenos: true
---
# TODO: bytt ut med funksjonen din fra steg 2
def f(x):
    return funksjonsuttrykk

for x in range(-5, 6):
    print(f(x) == 0)
:::

Kan du ut ifra utskriften fra programmet tenke deg fram til nullpunktet til $f$? 

::::{admonition} Fasit
---
class: dropdown, answer
---
I `for`{l=python}-løkken prøver vi ut alle heltallene $x \in \{-5, -4, \ldots, 4, 5\}$.

Ved å kjøre programmet får vi en utskrift med `True`{l=python} når $f(x) = 0$ stemmer og `False`{l=python} ellers. Under har vi markert hvilken linje det er 

:::{code-block} sh
False               # x = -5
False               # x = -4
False               # x = -3
False               # x = -2
False               # x = -1
False               # x = 0
False               # x = 1
True                # <-- nullpunktet! Her er x = 2
False               # x = 3
False               # x = 4
False               # x = 5
:::

Ut ifra programmet kan vi derfor konkludere at nullpunktet til $f$ er $x = 2$.

:::: 

```

```{tab-item} Steg 4
Det er fryktelig tungvint å måtte lese av en lang liste med `True`{l=python} og `False`{l=python} for å finne nullpunktet manuelt. Vi er jo strengt tatt ikke interessert i vite når det *ikke* er sant. Men det finnes heldigvis en innebygd måte å få programmet til å fortelle oss når det er sant, og ellers la være og si noe.

Vi kan bruke en såkalt `if`{l=python}-setning for å sjekke om en påstand er sann eller ikke. Hvis en påstand er sann, så kjøres programmet med innrykk under `if`{l=python}-setningen. Hvis påstanden er usann, så hopper programmet over kodelinjen. 

Vi kan derfor skrive om programmet fra steg 3 ved å legge inn en `if`{l=python}-setning slik:

:::{code-block} python
---
linenos: true
---
for x in range(-5, 6):
    if f(x) == 0:     # <-- Hvis f(x) = 0 er `True`, så skriver vi ut `x`
        print(x)
:::

Kopier programmet over og endre på programmet ditt slik at det skriver ut nullpunktet til $f(x) = 2x - 4$. 

Stemmer svaret?
```
````


:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1.html
---
:::

:::::
