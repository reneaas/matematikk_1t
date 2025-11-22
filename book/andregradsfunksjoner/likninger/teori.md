# Andregradslikninger

:::{goals} Læringsmål
* Kunne løse andregradslikninger grafisk, algebraisk og med programmering.
* Kunne bruke $abc$-formelen til å løse andregradslikninger
* Kunne bruke diskriminanten til å avgjøre hvor mange løsninger en andregradslikning har.
:::

Som vi så med lineære likninger, kan vi bruke flere løsningsstrategier for å løse andregradslikninger. Strategier vi skal se på er:
1. Grafisk løsning
2. Algebraisk løsning
3. Løsning med programmering


## Grafisk løsning
Når vi løser en andregradslikning grafisk, tegner vi grafene til funksjonsuttrykket på venstre og høyre side av likningen, så finner vi skjæringspunktene mellom grafene. Da er det $x$-koordinatene til skjæringspunktene som er løsningene til likningen.

:::::::::::::::{example} Eksempel 1
Løs likningen 

$$
x^2 + x + 1 = x + 2
$$

::::{solution}
---
dropdown: 0
---
Vi tegner grafene til funksjonsuttrykkene på venstre og høyre side av likningen:

$$
f(x) = x^2 + x + 1 \quad \text{og} \quad g(x) = x + 2
$$

Det gir oss følgende figur: 

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

Vi ser at grafene skjærer hverandre i to punkter: $(-1, 1)$ og $(1, 3)$. $x$-koordinatene til disse punktene er løsningene av likningen. Det første punktet gir oss $x = -1$. Det andre punktet gir oss $x = 1$. Dermed er løsningen av likningen

$$
x = -1 \or x = 1.
$$

::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
I figuren nedenfor vises grafene til 

$$
f(x) = x^2 + 3x - 5 \qog g(x) = 2x - 3.
$$

Bruk figuren til å løse likningen 

$$
x^2 + 3x - 5 = 2x - 3.
$$

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
x = -2 \or x = 1
$$
::::

::::{solution}
Vi ser at grafene skjærer hverandre i punktene $(-2, -7)$ og $(1, -1)$. Løsningen av likningen er $x$-koordinatene til disse punktene som gir løsningen

$$
x = -2 \or x = 1.
$$
::::

:::::::::::::::


---

Vi kan også løse dette med digitale hjelpemidler. La oss se på et eksempel med graftegneren i Geogebra.


:::::::::::::::{example} Eksempel 2
En andregradslikning er gitt ved 

$$
x^2 - 4x + 3 = -2x + 6
$$

Nedenfor ser du en gif som viser hvordan man løser likningen med grafvinduet i Geogebra. Vi trykker på {ggb-icon}`mode_intersect` (Skjæring mellom to objekt) etterfulgt av å trykke på hver graf for å finne skjæringspunktet.

:::{figure} ./videoer/grafisk_løsning.gif
---
class: no-click, adaptive-figure
width: 90%
---
:::

Skjæringspunktene mellom de to grafene er $(3, 0)$ og $(-1, 8)$. Løsningen av likningen er $x$-koordinatene til skjæringspunktene som betyr at løsningen av likningen er 

$$
x = -1 \or x = 3
$$



:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 2
En andregradslikning er gitt ved

$$
x^2 - 3x + 3 = 2x - 1
$$

Løs likningen grafisk. 

:::{ggb}
:::


::::{answer}
$$
x = 1 \or x = 4. 
$$
::::


::::{solution}
Vi skriver inn venstresiden og høyresiden i av likningen i Geogebra for å tegne grafene til de to funksjonene. Deretter bruker vi "skjæring mellom to objekt" {cas-icon}`mode_intersect` for å finne skjæringspunktene mellom grafene. Se figuren nedenfor.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/sol.png
---
class: no-click, adaptive-figure
width: 90%
---
:::

Skjæringspunktene mellom grafene er $(1, 1)$ og $(4, 7)$. Det er $x$-koordinatene til disse punktene som er løsningen av likningen. Dermed er løsningen av likningen

$$
x = 1 \or x = 4. 
$$

::::


:::::::::::::::





## Algebraisk løsning 

Når vi løser en andregradslikning algebraisk, så kan vi alltid faktorisere andregradspolynomet til nullpunktsform. Men her skal vi se at det også finnes noen spesielle andregradslikninger der vi kan faktorisere direkte. Vi skal også se at det finnes en helt generell formel for løsningen av en andregradslikning, som kalles for $abc$-formelen.

### Spesielle Andregradslikninger

#### Produktregelen

Når vi har faktorisert andregradspolynomer til nullpunktsform og lest av nullpunktene, har vi i prinsippet brukt det som kalles for **produktregelen** for likninger:


:::::::::::::::{summary} Setning: Produktregelen

Hvis $A$ og $B$ er to tall og

$$
A \cdot B = 0,
$$

så er

$$
A = 0 \or B = 0.
$$

:::::::::::::::

La oss nå se hvordan vi bruker produktregelen i praksis:

:::::::::::::::{example} Eksempel 3
Løs likningen

$$
(x - 1)(x + 2) = 0
$$

::::{solution}
---
dropdown: 0
---
Vi kan bruke produktregelen ved å tenke på hver faktor som to tall $A$ og $B$: 

$$
\underbrace{(x - 1)}_{\displaystyle A} \cdot \underbrace{(x + 2)}_{\displaystyle B} = 0. 
$$

Altså står det egentlig bare $A \cdot B = 0$, som betyr at 

\begin{align*}
    A = 0 \quad & \lor \quad B = 0 \\
    \\
    x - 1 = 0 \quad & \lor \quad x + 2 = 0 \\
    \\
    x = 1 \quad & \lor \quad x = -2.
\end{align*}
::::

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 3
Løs likningen

$$
(x + 2)(x - 4) = 0.
$$

::::{answer}
$$
x = -2 \or x = 4.
$$
::::


::::{solution}
Vi bruker produktregelen ved å tenke på hver faktor som to tall $A$ og $B$:

$$
\underbrace{(x + 2)}_{\displaystyle A} \cdot \underbrace{(x - 4)}_{\displaystyle B} = 0.
$$

som gir oss

$$
x + 2 = 0 \or x - 4 = 0
$$

som vi skriver om til

$$
x = -2 \or x = 4.
$$
::::


:::::::::::::::

#### Uten konstantledd

Når et andregradspolynom mangler konstantleddet, kan vi faktorisere det direkte og bruke produktregelen: 

:::::::::::::::{example} Eksempel 4
Løs likningen

$$
x^2 - 3x = 0.
$$

::::{solution}
---
dropdown: 0
---

Vi faktoriserer ut en faktor $x$ fra hvert ledd:

$$
x^2 - 3x = x(x - 3) = 0.
$$

Så bruker vi produkteregelen:

$$
x = 0 \or x - 3 = 0
$$

som vi skriver om til

$$
x = 0 \or x = 3.
$$

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 4
Løs likningen

$$
x^2 + 3x = 0.
$$


::::{answer}
$$
x = 0 \or x = -3
$$
::::


::::{solution}
Vi faktoriserer ut en faktor $x$ fra hvert ledd:

$$
x^2 + 3x = 0 \liff x(x + 3) = 0.
$$

Deretter bruker vi produktregelen:

$$
x(x + 3) = 0 \liff x = 0 \or x + 3 = 0
$$

som betyr at

$$
x = 0 \or x = -3.
$$
::::

:::::::::::::::


#### Uten lineært ledd
Når et andregradspolynom mangler det lineære leddet $bx$, så kan vi bruke konjugatsetningen eller bare ta kvadratroten på hver side av likningen:


:::::::::::::::{example} Eksempel 5
Løs likningen

$$
x^2 - 9 = 0.
$$

::::{solution}
---
dropdown: 0
---
Vi skriver om likningen

$$
x^2 - 9 = 0 \liff x^2 = 9
$$

Deretter kan vi ta kvadratroten på hver side av likningen. Men da får vi to muligheter:

$$
x = \pm \sqrt{9} = \pm 3.
$$

Dette gir mening siden både $(-3)^2 = 9$ og $3^2 = 9$. Dermed er løsningene av likningen

$$
x = -3 \or x = 3.
$$

::::

:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 5
Løs likningen

$$
x^2 - 49 = 0
$$


::::{answer}
$$
x = -7 \or x = 7.
$$
::::

::::{solution}
Vi skriver om likningen
$$
x^2 - 49 = 0 \liff x^2 = 49.
$$

Deretter kan vi ta kvadratroten på hver side av likningen:

$$
x = \pm \sqrt{49} = \pm 7.
$$

Altså er løsningen 

$$
x = -7 \or x = 7.
$$
::::

:::::::::::::::



### $abc$-formelen

Vi har tidligere sett at vi kan faktorisere et andregradspolynom $ax^2 + bx + c$ ved å første skrive det om til ekstremalpunktsform med fullstendig kvadraters metode, og deretter skrive det om til nullpunktsform med konjugatsetningen. Det lar oss bestemme nullpunktene som er det samme som å løse likningen $ax^2 + bx + c = 0$. Det er naturlig å lure på om vi kan løse dette én gang for alle, uten å måtte utføre alle disse stegene hver gang. Det kan vi, og det gir oss en formel som kalles for $abc$-formelen:


:::{margin} $\pm$-symbolet
$\pm$-tegnet leses som "pluss eller minus" og betyr at vi skal regne ut med formelen to ganger; én gang med pluss og én gang med minus.
:::

:::::::::::::::{summary} Setning: $abc$-formelen

Løsningen til en andregradslikning

:::{figure} ./figurer/teori/andregradslikning.svg
---
width: 30%
class: no-click, adaptive-figure
---
:::


er gitt ved

:::{figure} ./figurer/teori/abc-formel.svg
---
width: 35%
class: no-click, adaptive-figure
---
:::
:::::::::::::::


---

I oppgavene skal du få utlede $abc$-formelen. For nå, la oss se på hvordan vi bruker den. 


:::::::::::::::{example} Eksempel 6

Løs likningen

$$
x^2 - 4x - 5 = 0.
$$

:::{admonition} Løsning
---
class: solution
---
Fra likningen kan vi lese av at koeffisientene er 

$$
a = 1 \quad \text{og} \quad b = -4 \quad \text{og} \quad c = -5.
$$

Vi setter inn disse i $abc$-formelen som gir:

\begin{align*}
x & = \frac{-(-4) \pm \sqrt{(-4)^2 - 4\cdot 1 \cdot (-5)}}{2\cdot 1} = \frac{4 \pm \sqrt{16 + 20}}{2} = \frac{4 \pm \sqrt{36}}{2} \\
\\
& = \frac{4 \pm 6}{2} 
\end{align*}


Vi regner ut de to mulige løsningene, en med "$+$" og en med "$-$" som gir

$$
x = 5 \or x = -1.
$$
:::
:::::::::::::::

---

Nå kan du prøve deg!


:::::::::::::::{exercise} Underveisoppgave 6
Bruk $abc$-formelen til å løse likningen 

$$
x^2 - 3x - 4 = 0.
$$


::::{answer}
$$
x = -1 \or x = 4.
$$
::::

::::{solution}
Vi bruker $abc$-formelen med koeffisientene $a = 1$, $b = -3$ og $c = -4$:

$$
x = \frac{-(-3) \pm \sqrt{(-3)^2 - 4\cdot 1 \cdot (-4)}}{2\cdot 1} = \frac{3 \pm \sqrt{9 + 16}}{2} = \frac{3 \pm \sqrt{25}}{2} = \frac{3 \pm 5}{2}
$$

Så regner vi ut de to mulige løsningene, en med "$+$" og en med "$-$":

$$
x = \dfrac{3+ 5}{2} \or x = \dfrac{3 - 5}{2} \liff x = 4 \or x = -1.
$$


::::


:::::::::::::::


---

### Antall løsninger
Vi har tidligere sett at en andregradsfunksjon kan ha ingen, ett eller to nullpunkter. Med $abc$-formelen har vi et nytt verktøy for å avgjøre hvor mange nullpunkter en andregradsfunksjoner har – og dermed hvor mange løsninger en andregradslikning har.


:::::::::::::::{summary} Diskriminanten og antall løsninger
En andregradslikning på formen

$$
ax^2 + bx + c = 0
$$

har løsningen

$$
x = \frac{-b \pm \sqrt{D}}{2a} \qder D = b^2 - 4ac.
$$

Vi kaller $D$ for **diskriminanten**. Ut ifra diskriminanten kan vi se hvor mange løsninger likningen har:
* Hvis $D < 0$, har likningen ingen løsninger.
* Hvis $D = 0$, har likningen én løsning.
* Hvis $D > 0$, har likningen to løsninger.

Se figuren nedenfor.

:::{figure} ./figurer/teori/diskriminanter/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
Hvis $D < 0$, har likningen ingen løsninger. Hvis $D = 0$ har likningen én løsning. Hvis $D > 0$ har likningen to løsninger. Dette tilsvarer at grafen til en andregradsfunksjon enten ikke skjærer $x$-aksen, skjærer den i ett punkt eller skjærer den i to punkter.
:::

:::::::::::::::


---

:::::::::::::::{example} Eksempel 7
Bestem hvor mange løsninger likningen nedenfor

$$
x^2 - 4x + 4 = 0.
$$

::::{solution}
---
dropdown: 0
---
Vi regner ut diskriminanten med $a = 1$, $b = -4$ og $c = 4$:

$$
D = (-4)^2 - 4\cdot 1 \cdot 4 = 16 - 16 = 0.
$$

Siden $D = 0$, har likningen én løsning. 

::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 7
Bestem hvor mange løsninger likningen nedenfor har.


$$
x^2 + 2x + 8 = 0.
$$


::::{answer}
Ingen løsninger.
::::


::::{solution}
Vi regner ut diskriminanten med $a = 1$, $b = 2$ og $c = 8$:

$$
D = (2)^2 - 4\cdot 1 \cdot 8 = 4 - 32 = -28.
$$

Siden $D < 0$, har likningen ingen løsninger.
::::

:::::::::::::::


### CAS
Å løse andregradslikninger med CAS gjøres på samme måte som for lineære likninger. 


:::::::::::::::{explore} Utforsk 1
Nedenfor vises en gif som viser hvordan man løser en andregradslikning med CAS:

:::{figure} ./videoer/cas.gif
---
class: no-click, adaptive-figure
width: 90%
---
viser hvordan man løser en andregradslikning med CAS. Løsningene er $x = -\sqrt{3} + 2 \or x = \sqrt{3} + 2$.
:::




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS til å løse likningen som er vist i gif-en.


:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å løse likningen

$$
x^2 - 4x + 4 = 0.
$$

::::{answer}
:::{figure} ./figurer/cas/utforsk/utforsk_1/b.png
---
class: no-click, adaptive-figure
width: 60%
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å løse likningen 

$$
x^2 + 2x + 6 = 0.
$$

Hvorfor tror du svaret blir som det blir? 

::::{answer}
:::{figure} ./figurer/cas/utforsk/utforsk_1/c.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Det betyr at likningen ikke har noen løsning. Vi kan se dette ved å tegne grafen til $f(x) = x^2 + 2x + 6$ og se at den aldri skjærer $x$-aksen:

:::{figure} ./figurer/utforsk/utforsk_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::



::::

:::::::::::::

::::::::::::::

:::::::::::::::


## Løsning med programmering

Når vi løste lineære likninger med programmering, skrev vi et program som systematisk prøvde ut mange heltallige verdier for $x$ og sjekke om likningen var oppfylt. Dersom likningen var oppfylt, skrev programmet ut verdien av $x$ som en løsning. Denne strategien lar seg naturlig oversette direkte til andregradslikninger også. 


:::::::::::::::{explore} Utforsk 2
Nedenfor vises et eksempel på et program som løser en andregradslikning ved å prøve ut heltallsverdier for $x$. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å bestemme hva programmet skriver ut når det kjøres. 

Skriv inn svaret ditt nedenfor og sjekk om du får riktig svar.

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


Endre på programmet slik at det løser likningen

$$
x^2 - 3x - 4 = 0.
$$

Sjekk om du får samme svar med CAS. 


::::{answer}
:::{code-block} python
---
linenos:
emphasize-lines: 2
---
for x in range(-10, 11):
    if x**2 - 3*x - 4 == 0:
        print(x)
:::
::::


:::::::::::::


::::::::::::::

:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    if x**2 - x - 6 == 0:
        print(x)


:::


:::::::::::::::



