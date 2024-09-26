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

Da kan vi ty til noe som kalles for å løse likningen numerisk. Å løse en likning **numerisk**, betyr å finne en tilnærmet tallverdi for løsningen. For å gjøre dette bruker vi gjerne en strategi som er formulert som en oppskrift som vi kan følge for å nærme oss løsningen. En slik oppskrift kalles for en **algoritme**. Når vi har utformet en algoritme, er målet vårt å oversette denne til et program som datamaskinen kan utføre for oss så vi kan lene oss tilbake og la datamaskinen gjøre jobben for oss. 

Her skal vi se på hvordan vi kan gjøre dette med likninger. I utforsk 1 skal du gradvis bygge opp et program som løser en lineær likning.

:::{admonition} Påminnelse: nullpunkt
---
class: sidenote, margin
---
Vi minner om at nullpunktet til en funksjon $f$ er:
* $x$-verdien som medfører at $f(x) = 0$.
* $x$-koordinaten der hvor grafen til $f$ skjærer $x$-aksen.
:::

::::::::{admonition} Utforsk 1
---
class: explore
---
Vi skal ta utgangspunkt i at vi skal bestemme nullpunktet til 

$$
f(x) = 2x + 4.
$$


````{tab-set}
---
class: tabs-custom
---
```{tab-item} Steg 1: <br> Lage ulike verdier for $x$
*Her skal du repetere hvordan en `for`{l=python}-løkke med `range`{l=python} fungerer.*

::::::{tab-set}
:::::{tab-item} a
Les programmet under og prøv å forutsi hva programmet skriver ut. <br> Skriv det inn under for å sjekke svaret ditt!
:::::

:::::{tab-item} b
Endre på programmet slik at det skriver ut tallene $x \in \{-5, -4, \ldots, 4, 5\}$. <br>
::::{admonition} Fasit
---
class: dropdown, answer
---
:::{code-block} python
---
linenos: true
---
for x in range(-5, 6):
    print(x)
:::
::::
:::::
::::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_1.html
---
:::
```

```{tab-item} Steg 2: <br> Lage en funksjon
*Her skal du lære hvordan man lager en funksjon i Python, og hvordan man bruker den til å regne ut funksjonsverdier.*

Hvis vi skal kunne regne ut funksjonsverdier som i matematikken, kan vi lage en funksjon i Python. 

::::::{tab-set}
:::::{tab-item} a
Under vises et program som regner ut en funksjonsverdi for $f(x) = -3x + 6$. 

Les programmet og forutsi hvilken verdi programmet skriver ut. <br> Skriv det inn under for å sjekke!
:::::

:::::{tab-item} b
Endre på programmet slik at det i stedet regner ut $f(-2)$. <br> Sjekk om svaret gir mening ved regning!

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
def f(x):
    return -3 * x + 6

y = f(-2)
print(y)
:::

$$
f(-2) = -3 \cdot (-2) + 6 = 6 + 6 = 12
$$
::::
:::::

:::::{tab-item} c
Endre på programmet slik det regner ut $f(-1)$ for 

$$
f(x) = 2x + 4.
$$

Kjør programmet og sjekk at svaret stemmer.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{code-block} python
---
linenos: true
emphasize-lines: 2
---
def f(x):
    return 2 * x + 4

y = f(-1)
print(y)
:::

$$
f(-1) = 2 \cdot (-1) + 4 = -2 + 4 = 2
$$
::::
:::::
::::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_2.html
---
:::

```

```{tab-item} Steg 3: <br> Sjekke om $f(x) = 0$
*Her skal du lære hvordan man sjekker om en funksjonsverdi er lik null.*

Hvis vi skal få et program til å finne nullpunktet for oss, må vi kjenne til hvordan vi kan be et program sjekke at $f(x) = 0$. 

For å sjekke om $f(x) = 0$ med et program, skriver vi `f(x) == 0`{l=python}. Dette vil gi
* `True`{l=python} hvis det er sant
* `False`{l=python} hvis det er usant


::::::{tab-set}
:::::{tab-item} a
Les programmet og forutsi hva programmet skriver ut. <br> Skriv det inn under for å sjekke svaret ditt!
:::::

:::::{tab-item} b
Hva må verdien av $x$ være for at programmet skal skrive ut `True`{l=python}? <br> 

Endre på programmet og sjekk at du får det du forventer!

::::{admonition} Fasit
---
class: dropdown, answer
---
Programkode:
:::{code-block} python
---
linenos: true
emphasize-lines: 4
---
def f(x):
    return -3 * x + 6

x = 2 
print(f(x) == 0)
:::

Dette stemmer fordi

$$
f(2) = -3 \cdot 2 + 6 = -6 + 6 = 0
$$
::::
:::::

:::::{tab-item} c
Endre på programmet slik at du sjekker om $f(x) = 0$ for 

$$
f(x) = 2x + 4.
$$

Finn også hvilken verdi av $x$ du må sette inn for at programmet skal skrive ut `True`{l=python}.

::::{admonition} Fasit
---
class: dropdown, answer
---
Programkode:

:::{code-block} python
---
linenos: true
emphasize-lines: 2, 4
---
def f(x):
    return 2 * x + 4

x = -2
print(f(x) == 0)
:::

Dette stemmer fordi

$$
f(-2) = 2 \cdot (-2) + 4 = -4 + 4 = 0
$$
::::
:::::
::::::


<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_3.html
---
:::

```

```{tab-item} Steg 4: <br> Regne ut mange funksjonsverdier
*Her skal du lære hvordan vi kan kombinere `for`{l=python}-løkker og funksjoner til å regne ut mange funksjonsverdier.*

Når vi leter etter nullpunktet til $f$, er det litt tungvint å endre på verdien til $x$ manuelt. I stedet kan vi bruke en `for`{l=python}-løkke til å lage mange verdier for $x$ og prøve ut om $f(x) = 0$ for hver av dem. 

::::::{tab-set}
:::::{tab-item} a
Les programmet under og forutsi verdiene programmet skriver ut. <br> Skriv det inn under for å sjekke svaret ditt!
:::::

:::::{tab-item} b
Endre på programmet slik at det regner ut $f(x) = -3x + 6$ for $x \in \{-3, -2, \ldots, 2, 3\}$. <br> Kjør programmet og sjekk at du får det du forventer!
:::::

::::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_4.html
---
:::

```

```{tab-item} Steg 5: <br> Prøv ut mange verdier for $f(x) = 0$
*Her skal du lære hvordan vi kan få et program til å fortelle oss om $f(x) = 0$.*

Nå skal vi prøve ut mange verdier for $x$ for å sjekke om $f(x) = 0$ for hver av dem.


::::::{tab-set}
:::::{tab-item} a
Kjør programmet under og se om du kan lese av nullpunktet til funksjonen i programmet.
:::::

:::::{tab-item} b
Endre på programmet og bruk det til å bestemme nullpunktene til 

1. $f(x) = 3x - 9$
2. $f(x) = -2x + 8$
3. $f(x) = 4x + 12$
:::::
::::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_5.html
---
:::

```


```{tab-item} Steg 6: <br> Automatisere søket etter nullpunktet
*Her skal du lære hvordan vi kan få programmet til å fortelle oss når $f(x) = 0$ uten at vi må lese det av manuelt.*

Å lese gjennom en lang liste med `True`{l=python} og `False`{l=python} for å finne nullpunktet er tungvint, spesielt hvis vi tester ut mange verdier av $x$. Heldigvis kan vi da bruke noe som kalles for en `if`{l=python}-setning.

En `if`{l=python}-setning lar oss sjekke om $f(x) = 0$ og skrive ut verdien *kun* hvis det er sant.

::::::{tab-set}
:::::{tab-item} a
Les programmet under og forutsi hva programmet skriver ut. <br> Skriv det inn under for å sjekke svaret ditt!
:::::

:::::{tab-item} b
Endre på programmet slik at du kan bruke det til å finne nullpunktene til

1. $f(x) = 3x - 9$
2. $f(x) = -2x + 8$
3. $f(x) = 4x + 12$

Kjør programmet og sjekk at du får det du forventer!
:::::
::::::

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/steg_6.html
---
::: 


```


```{tab-item} Steg 7: <br> Oppsummering
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

::::::::


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

Bestem nullpunktet til $f$ ved regning. <br> Bruk svaret ditt til å forklare hvorfor strategien fra utforsk 1 ikke vil gi oss nullpunktet til $f$.
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
