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


:::{admonition} Påminnelse: nullpunkt
---
class: sidenote, margin
---
Vi minner om at nullpunktet til en funksjon $f$ er:
* Verdien $x$ slik at $f(x) = 0$.
* Grafisk er dette punktet der grafen til $f$ skjærer $x$-aksen.
:::

I mange tilfeller kan vi bare løse en likning algebraisk for å finne verdien til $x$ slik at en likning er sann - da finner vi det eksakte svaret. Men det finnes mange likninger hvor dette dessverre ikke lar seg gjøre. I disse tilfellene klarer vi bare ikke å få $x$ alene, uansett hvor hardt vi prøver. Da tyr vi til noe som kalles får å løse en likningen numerisk.

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
```{tab-item} Steg 1: Lage ulike tall
Her skal du repetere hvordan en `for`{l=python}-løkke med `range`{l=python} fungerer.

Se på koden og forutsi hvilke tall som skrives ut.

Kjør koden og sjekk svaret ditt!

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_1.html
---
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
Koden skriver ut heltallene $x \in \{-5, -4, \ldots, 4, 5\}$.

**Refleksjonsspørsmål:** <br>
Hvordan hadde blitt hvis vi i stedet brukte `range(-3, 7)`{l=python}?

Tenk ut en forutsigelse - deretter endre på programmet og kjør det for å sjekke svaret ditt!
:::
```

```{tab-item} Steg 2: Lage en funksjon
Her skal du lære hvordan man lager en funksjon i Python, og hvordan man bruker den til å regne ut funksjonsverdier.

Hvis vi skal kunne regne ut funksjonsverdier som i matematikken, må vi lage en funksjon i Python. 

Under vises en eksempelkode på hvordan man lager funksjonen $f(x) = -3x + 1$ som regner ut funksjonsverdien $f(6)$ og skriver ut svaret. 
:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 1

y = f(6)
print(y)
:::

Fyll ut programmet under slik at det regner ut lager en funksjon for $f(x) = 2x - 4$ og skriver ut funksjonsverdien $f(3)$. 

Kjør programmet og sjekk at du får riktig verdi!

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_2.html
---
:::

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

y = f(3)
print(y)
:::

Når programmet kjøres, skal det skrive ut funksjonsverdien

$$
f(3) = 2 \cdot 3 - 4 = 6 - 4 = 2.
$$


**Refleksjonsspørsmål:** <br>
Hva skjer hvis du i stedet bare skriver `print(f(3))`{l=python} i stedet for å lagre funksjonsverdien i variabelen `y`{l=python} først?

Forutsi hva du tror skjer - deretter endre på programmet og kjør det for å sjekke svaret ditt!
::::

```

```{tab-item} Steg 3: Sjekke om $f(x) = 0$
Her skal du lære hvordan man sjekker om en funksjonsverdi er lik null.

I eksempelkoden under vises en sjekk der $f(x) = -3x + 6$ og vi spør programmet om $f(2) = 0$ og $f(3) = 0$.

:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 6

# MERK: `==` sjekker om to verdier er like!
print(f(2) == 0)    # <-- Er f(2) = 0? 
print(f(3) == 0)    # <-- Er f(3) = 0?
:::

For en bestem verdi av $x$, så vil programmet gi:
* `True`{l=python} hvis $f(x) = 0$ er sant
* `False`{l=python} hvis $f(x) = 0$ er usant 

Forutsi hva utskriften blir fra programmet. Kopier programmet og kjør det under for å sjekke svaret ditt!

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_3.html
---
:::

:::{admonition} Fasit
---
class: dropdown, answer
---
* `f(2) == 0`{l=python} gir `True`{l=python} siden 

$$
f(2) = -3 \cdot 2 + 6 = -6 + 6 = 0
$$

* `f(3) == 0`{l=python} gir `False`{l=python} siden 

$$
f(3) = -3 \cdot 3 + 6 = -9 + 6 = -3
$$
:::
```

```{tab-item} Steg 4: Regne ut mange funksjonsverdier
Her skal du lære hvordan vi kan kombinere `for`{l=python}-løkker og funksjoner til å regne ut mange funksjonsverdier.

Vi kan bruke en `for`{l=python}-løkke til å regne ut funksjonsverdier for mange verdier av $x$.

Under vises en eksempelkode som regner ut $f(x) = -3x + 6$ for $x \in \{-1, 0, 1\}$ og skriver ut hver verdi.

:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 6

for x in range(-1, 2):
    y = f(x)
    print(y)
:::

Fyll inn programmet under slik at det regner ut $f(x) = 2x - 4$ for $x \in {-1, 0, 1}$ og skriver ut hver verdi. 

Forutsi hvilke verdier programmet skriver ut først. Kjør deretter programmet og sjekk svaret ditt!

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_4.html
---
:::

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

for x in range(-1, 2):
    y = f(x)
    print(y)
:::

Utskriften vi får er 

:::{code-block} sh
---
linenos: false
---
-6
-4
-2
:::

**Refleksjonsspørsmål:** <br>
Hva hadde den første og siste verdien som blir skrevet ut blitt hvis vi i stedet brukte `range(-4, 3)`{l=python} i `for`{l=python}-løkken?

Forutsi hva du tror skjer - deretter endre på programmet og kjør det for å sjekke svaret ditt!
::::
```

```{tab-item} Steg 5: Prøv ut mange verdier for $f(x) = 0$
Her skal du lære hvordan vi kan sjekke om en funksjonsverdi er null for mange verdier av $x$.

Nå skal vi prøve ut mange verdier for $x$ for å sjekke om $f(x) = 0$ for noen av dem.

Under vises en eksempelkode som prøver ut alle heltallene $x \in \{-5, -4, \ldots, 4, 5\}$ og skriver ut om $f(x) = 0$ eller ikke.

:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 6

for x in range(-5, 6):
    print(f(x) == 0)
:::

Kopier programmet under og endre på programmet ditt slik at det gjør det samme for $f(x) = 2x - 4$.

Tolk programmet og se om du kan forklare hva nullpunktet til $f$ er ved hjelp av utskriften.

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_5.html
---
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
I `for`{l=python}-løkken prøver vi ut alle heltallene $x \in \{-5, -4, \ldots, 4, 5\}$.

Ved å kjøre programmet får vi en utskrift med `True`{l=python} når $f(x) = 0$ er sant og `False`{l=python} ellers. Under har vi hvilke verdier av `x`{l=python} hver linje tilsvarer og hvilken linje som tilsvarer nullpunktet.

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


```{tab-item} Steg 6: Automatisere søket etter nullpunktet
Her skal du lære hvordan vi kan få programmet til å fortelle oss når $f(x) = 0$ uten at vi må sjekke det manuelt.

Å lese gjennom en lang liste med `True`{l=python} og `False`{l=python} for å finne nullpunktet er fryktelig tungvint, spesielt hvis vi tester ut mange verdier av $x$. Heldigvis kan vi da bruke noe som kalles for en `if`{l=python}-setning som sjekker om likningen er sann, og *kun* skrives ut hvis den er sann.

Under vises en eksempelkode som finner nullpunktet til $f(x) = -3x + 6$.

:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 6

for x in range(-5, 6):
    if f(x) == 0:       # <-- Sjekker om f(x) = 0
        print(x)        # <-- Skriver ut x kun hvis f(x) = 0 er sant!
:::

Kopier programmet over og endre på programmet slik at det finner nullpunktet til $f(x) = 2x - 4$.

Kjør programmet og sjekk at det gir riktig svar! <br> Kan du gi en forklaring på hvordan alle bitene av programmet fungerer nå?

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_6.html
---
::: 

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

for x in range(-5, 6):
    if f(x) == 0:
        print(x)
:::

som gir utskriften

:::{code-block} sh
---
linenos: false
---
2
:::

Dette betyr at nullpunktet til $f(x) = 2x - 4$ er $x = 2$.

**Refleksjonsspørsmål:** <br>

Hvis programmet ikke gir noen utskrift, men du *vet* at den har en løsning $x \in \mathbb{Z}$ (løsningen er et heltall), hva kan være årsaken til dette?
::::
```

```{tab-item} Steg 7: Prøv ut andre funksjoner
Her skal du prøve å anvende det du har lært med andre funksjoner. 

Prøv ut metoden du har lært på disse funksjonene

1. $f(x) = 3x - 9$
2. $f(x) = -2x + 8$
3. $f(x) = 4x - 12$

For hver av funksjonene, finn nullpunktet ved å bruke programmet du har laget.

Hva er nullpunktet til hver av funksjonene?

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_7.html
---
::: 

:::{admonition} Fasit
---
class: dropdown, answer
---
1. $f(x) = 3x - 9$ har nullpunktet $x = 3$.
2. $f(x) = -2x + 8$ har nullpunktet $x = 4$.
3. $f(x) = 4x - 12$ har nullpunktet $x = 3$.


**Refleksjonsspørsmål:** <br>
Hvorfor kan du ikke bruke strategien du har lært her til å finne nullpunktet til $f(x) = 3x - 1$?
:::

```
````

:::::
