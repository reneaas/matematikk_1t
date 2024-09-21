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



I mange tilfeller kan vi bare løse en likning algebraisk for å finne verdien til $x$ slik at en likning er sann - da finner vi det eksakte svaret. Men det finnes mange likninger hvor dette dessverre ikke lar seg gjøre. I disse tilfellene klarer vi bare ikke å få $x$ alene, uansett hvor hardt vi prøver. Et eksempel på en slik likning er 

$$
2^x = 6x
$$

Da kan vi ty til noe som kalles får å løse likningen numerisk. Å løse en likning **numerisk**, betyr å finne en tilnærmet tallverdi for løsningen. For å gjøre dette bruker vi gjerne en strategi som er formulert som en oppskrift som vi kan følge for å nærme oss løsningen. En slik oppskrift kalles for en **algoritme**. Når vi har en algoritme, er målet vårt å oversette denne til et program som datamaskinen kan utføre for oss så vi kan *kick back, relax* og la datamaskinen gjøre jobben for oss. 

Her skal vi se på hvordan vi kan gjøre dette med likninger. I utforsk 1 skal du gradvis bygge opp et program som løser en lineær likning.

:::{admonition} Påminnelse: nullpunkt
---
class: sidenote, margin
---
Vi minner om at nullpunktet til en funksjon $f$ er:
* $x$-verdien som medfører at $f(x) = 0$.
* $x$-koordinaten der hvor grafen til $f$ skjærer $x$-aksen.
:::

:::::{admonition} Utforsk 1
---
class: explore
---
Vi skal ta utgangspunkt i at vi skal bestemme nullpunktet til 

$$
f(x) = 2x - 4.
$$


````{tab-set}
---
class: tabs-custom
---
```{tab-item} Steg 1: <br> Lage ulike verdier for $x$
*Her skal du repetere hvordan en `for`{l=python}-løkke med `range`{l=python} fungerer.*

Se på koden under og forutsi hvilke tall som skrives ut **før** du kjører programmet.

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

```{tab-item} Steg 2: <br> Lage en funksjon
*Her skal du lære hvordan man lager en funksjon i Python, og hvordan man bruker den til å regne ut funksjonsverdier.*

Hvis vi skal kunne regne ut funksjonsverdier som i matematikken, må vi lage en funksjon i Python. 


::::{admonition} Eksempelkode
---
class: examplecode
---
Under vises en eksempelkode på hvordan man lager funksjonen

$$
f(x) = -3x + 1
$$

Programmet regner så ut $f(6)$ og skriver ut svaret. 
:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 1

y = f(6)
print(y)
:::

::::

**Prøv selv!** <br>
Fyll ut programmet under slik at det lager en funksjon for $f(x) = 2x - 4$ og skriver ut funksjonsverdien $f(3)$. 

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

```{tab-item} Steg 3: <br> Sjekke om $f(x) = 0$
*Her skal du lære hvordan man sjekker om en funksjonsverdi er lik null.*

Hvis vi skal finne nullpunktet til $f$, må vi ha en måte å sjekke om $f(x) = 0$ på. Man skulle tro at man da kanskje bare kunne skrevet `f(x) = 0`{l=python}, men likhetstegnet i Python betyr å "tilordne" en verdi til en variabel - *ikke* å sjekke om to verdier er like. <br> Man har derfor innført skrivemåten `a == b`{l=python} for å sjekke om `a`{l=python} og `b`{l=python} er like.


::::{admonition} Eksempelkode
---
class: examplecode
---
I eksempelkoden under lager vi en funksjon for $f(x) = -3x + 6$, så spør vi programmet om $f(2) = 0$ og $f(3) = 0$, og skriver ut svarene.

:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 6

print(f(1) == 0)    # <-- Er f(2) = 0? 
print(f(2) == 0)    # <-- Er f(3) = 0?
:::

For en bestemt verdi av $x$, så vil programmet gi:
* `True`{l=python} hvis $f(x) = 0$ er sant
* `False`{l=python} hvis $f(x) = 0$ er usant 
::::

**Prøv selv!** <br>
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
* `f(2) == 0`{l=python} gir `False`{l=python} siden 

$$
f(1) = -3 \cdot 1 + 6 = -3 + 6 = 3
$$

* `f(3) == 0`{l=python} gir `True`{l=python} siden 

$$
f(2) = -3 \cdot 2 + 6 = -6 + 6 = 0
$$

:::
```

```{tab-item} Steg 4: <br> Regne ut mange funksjonsverdier
*Her skal du lære hvordan vi kan kombinere `for`{l=python}-løkker og funksjoner til å regne ut mange funksjonsverdier.*

En måte å finne nullpunktet til $f$ er å prøve ut mange forskjellige verdier av $x$ og sjekke om $f(x) = 0$ for noen av dem.
Da må vi kunne regne ut $f(x)$ for mange forskjellige verdier av $x$, noe vi kan oppnå med en `for`{l=python}-løkke.


::::{admonition} Eksempelkode
---
class: examplecode
---
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
::::

**Prøv selv!** <br>
Fyll inn programmet under slik at det regner ut $f(x) = 2x - 4$ for $x \in \{-1, 0, 1\}$ og skriver ut hver verdi. 

Forutsi hvilke verdier programmet skriver ut **før** du tester ut programmet. <br> Kjør deretter programmet og sjekk svaret ditt!

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

```{tab-item} Steg 5: <br> Prøv ut mange verdier for $f(x) = 0$
*Her skal du lære hvordan vi kan sjekke om en funksjonsverdi er null for mange verdier av $x$.*

Nå skal vi prøve ut mange verdier for $x$ for å sjekke om $f(x) = 0$ for noen av dem.


::::{admonition} Eksempelkode
---
class: examplecode
---
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
::::


**Prøv selv!** <br>
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

Ved å kjøre programmet får vi en utskrift med `True`{l=python} når $f(x) = 0$ er sant og `False`{l=python} ellers. Under har vi lagt til hvilke verdier av `x`{l=python} hver linje tilsvarer og hvilken linje som tilsvarer nullpunktet.

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


```{tab-item} Steg 6: <br> Automatisere søket etter nullpunktet
*Her skal du lære hvordan vi kan få programmet til å fortelle oss når $f(x) = 0$ uten at vi må sjekke det manuelt.*

Å lese gjennom en lang liste med `True`{l=python} og `False`{l=python} for å finne nullpunktet er fryktelig tungvint, spesielt hvis vi tester ut mange verdier av $x$. Heldigvis kan vi da bruke noe som kalles for en `if`{l=python}-setning som sjekker om likningen er sann, og *kun* skriver ut verdien til $x$ hvis den er sann.

::::{admonition} Eksempelkode
---
class: examplecode
---
Under vises en eksempelkode som finner nullpunktet til $f(x) = -3x + 6$.

:::{code-block} python
---
linenos: true
---
def f(x):
    return -3 * x + 6

for x in range(-5, 6):
    if f(x) == 0:       # <-- Sjekker om f(x) = 0
        print(x)        # <-- Skriver ut x hvis f(x) = 0 er sant!
:::
::::

**Prøv selv!** <br>
Kopier programmet over og endre på programmet slik at det finner nullpunktet til 

$$
f(x) = 2x - 4
$$

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
Hvis programmet ikke gir noen utskrift, men du *vet* at den har en løsning $x \in \mathbb{Z}$ (husk: $\mathbb{Z} er heltallene), hva kan være årsaken til dette?
::::
```

```{tab-item} Steg 7: <br> Prøv ut andre funksjoner
*Her skal du prøve å anvende det du har lært med andre funksjoner.*

Prøv ut metoden du har lært på disse funksjonene

1. $f(x) = 3x - 9$
2. $f(x) = -2x + 8$
3. $f(x) = 4x + 12$

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
3. $f(x) = 4x + 12$ har nullpunktet $x = -3$.


**Refleksjonsspørsmål:** <br>
Hvorfor kan du ikke bruke strategien du har lært her til å finne nullpunktet til $f(x) = 3x - 1$?
:::

```

```{tab-item} Steg 8: <br> Oppsummering
*Her skal du oppsummere strategien du har lært om og reflektere over bruksområde til metoden.*

1. Gi en beskrivelse av løsningsstrategien du har brukt for å finne nullpunktet til en funksjon.
2. Hvilke lineære funksjoner kan du bruke strategien på for å finne nullpunktet?
3. Hvilke lineære funksjoner kan du *ikke* bruke strategien på for å finne nullpunktet?

:::{admonition} Fasit
---
class: dropdown, answer
---
1. Strategien tester ut mange verdier av $x$ og sjekker om $f(x) = 0$ for noen av dem. Hvis det er sant, skriver programmet ut verdien av $x$.
2. Strategien kan brukes på alle lineære funksjoner der hvor nullpunktet er en heltallsverdi.
3. Strategien kan *ikke* brukes på lineære funksjoner der nullpunktet ikke er et heltall.
:::
````

:::::


---


:::{admonition} Symbolet $\approx$
---
class: sidenote, margin
---
I utforsk 2 vil du møte på symbolet $\approx$. Når vi skriver 

$$
a \approx b
$$

leser vi dette som at $a$ er "tilnærmet lik" $b$. Verdiene til de to tallene er derfor nokså nærme hverandre, men hva som er "nærme" vil ofte være avhengig av hvilken sammenheng vi ser på.
:::

:::::{admonition} Utforsk 2
---
class: explore
---
Her skal vi ta utgangspunkt i at vi skal bestemme nullpunktet til 

$$
f(x) = 2x - 1.
$$

`````{tab-set}
---
class: tabs-custom
---
````{tab-item} Steg 1: <br> Hvorfor finner vi ikke svaret?
Bruker vi strategien fra utforsk 1, vil vi oppdage at vi ikke får noen løsning.

Bestem nullpunktet til $f$. <br> Bruk svaret ditt til å forklare hvorfor strategien fra utforsk 1 ikke vil gi oss nullpunktet til $f$.
:::{admonition} Fasit
---
class: dropdown, answer
---
Nullpunktet er 

$$
x = \dfrac{1}{2}
$$

Med strategien fra utforsk 1 vil ikke programmet finne løsningen siden vi bare prøver ut heltallsverdier for $x$.
:::
````

````{tab-item} Steg 2: <br> Justere strategi
*Her skal du lære hvordan vi kan bruke en `while`{l=python}-løkke til å lage mange verdier for $x$ som ikke bare er heltall*.

Vi har så langt bare sett på hvordan vi kan få et program til å lage mange heltallsverdier for $x$. Men når nullpunktet ikke er et heltall, finner vi ikke løsningen på denne måten. Vi trenger derfor en ny måte å få programmet til å lage mange verdier for $x$. Da bruker vi noe kalles for en `while`{l=python}-løkke.


**Eksempelkode** <br>
En `while`{l=python}-løkke fortsetter å kjøre så lenge en betingelse er sann. Under vises en eksempelkode som lager alle tallene $x \in \{-5, -4, \ldots, 4, 5\}$ ved hjelp av en `while`{l=python}-løkke og en kode som gjør det samme med en `for`{l=python}-løkke så du kan sammenligne.


:::{tab} `while`{l=python}-løkke

```{code-block} python
---
linenos: true
---
x = -5
while x < 6:    # <-- Vi fortsetter så lenge x er mindre enn 6
    print(x)
    x = x + 1   # <-- Øker x med 1 for hver runde
```

:::

:::{tab} `for`{l=python}-løkke

```{code-block} python
---
linenos: true
---
for x in range(-5, 6):
    print(x)
```

:::


**Prøv selv!** <br>

Hvis vi endrer på linje 4 i programmet under, kan vi endre på hvordan vi øker verdien til $x$ hver runde. Dette gir oss muligheten til å lage andre lister med tall, inkludert desimaltall! <br>

::::{tab-set}
:::{tab-item} a
Kjør programmet og sjekk at det faktisk lager alle tallene $x \in \{-5, -4, \ldots, 4, 5\}$ som forventet. <br> Hvorfor tror du ikke programmet skriver ut $6$? 
:::

:::{tab-item} b
Endre på linje 4 slik at det står `x = x + 2`{l=python}. <br> Forutsi hva som blir skrevet ut, og kjør deretter programmet for å sjekke svaret ditt! 
:::

:::{tab-item} c
Endre på linje 4 slik at det står `x = x + 0.5`{l=python}. <br> Forutsi hva som blir skrevet ut, og kjør deretter programmet for å sjekke svaret ditt!
:::
::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/steg_2.html
---
:::
````

`````
:::::
