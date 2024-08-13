# Numerisk løsning

:::{admonition} Læringsmål
---
class: tip
---
Etter å ha gått gjennom dette delkapittelet, er målet at du skal kunne:
* Lese mer kompliserte programmer som løser likninger numerisk.
* Kunne lese og forklare strategien/algoritmen som brukes i en programkode.
* Kunne justere og bruke et program til å løse likninger.
:::


## Halveringsmetoden
En metode for å finne en omtrentlig verdi for nullpunktet til en funksjon $f$, kalles for **halveringsmetoden**. Dette er en numerisk metode som som tar utgangspunkt i følgende algoritmisk idé

1. Velg to punkter $x = a$ og $x = b$ der vi *vet* at $f$ har forskjellig fortegn.
2. Bestem midtpunktet $m = \dfrac{a+b}{2}$.
3. Hvis $f(m) = 0$, er m en løsning. Hvis ikke:
    * Hvis $f$ har forskjellig fortegn i $x = a$ og $x = m$, så er nullpunktet i intervallet $[a, m]$ - vi velger dette som vårt nye intervall.
    * hvis $f$ har forskjellig fortegn i $x = m$ og $x = b$, så er nullpunktet i intervallet $[m, b]$. - vi velger dette som vårt nye intervall.
4. Gå tilbake og gjenta steg 2 og gjenta. 


:::::{admonition} Utforsk 1
---
class: explore
---
Under vises en programkode som bestemmer et nullpunkt til

$$
f(x) = x^2 - x - 6,
$$

ved å bruke halveringsmetoden slik den er beskrevet over. Men! Programmet står i tilfeldig rekkefølge!

Deloppgave 1
: Bruk beskrivelsen av halveringsmetoden og pusle sammen programmet i riktig rekkefølge for å få tilgang til det fullstendige programmet. <br> Lim inn programmet i det interaktive kodevinduet under.


:::{raw} html
---
file: parsons_puzzle/utforsk/utforsk_1.html
---
:::


<br>

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html
---
:::

<br>

Deloppgave 2
: Endre programmet slik at det finner det *andre* nullpunktet til $f$.


<br>

Deloppgave 3
: Hva skjer hvis du endrer setter `a = -10`{l=python} og `b = 10`{l=python} (hvis noe i det hele tatt)? <br> Hva er årsaken til dette?

:::::
