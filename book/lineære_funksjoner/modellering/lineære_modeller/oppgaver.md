
# Oppgaver: <br> Lineære modeller

::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Lise handler på en perlebutikk der man kan lage seg et perkesmykke ved å plukke ut et antallet perler og lage smykket. For å lage et smykke trenger man et kjede, det koster $15$ kr. Hver perle koster $2$ kr.

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Sett opp en funksjon $f$ som gir prisen i $f(x)$ kroner for å kjøpe ett smykke med $x$ perler.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 2x + 15
$$
:::
::::::::::

::::::::::{tab-item} b
Det er bare plass til 60 perler i et smykke. 

Sett opp en passende definisjonsmengde og tilhørende verdimengde for $f$. 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
D_f = \langle 0, 60] \quad \text{og} \quad V_f = \langle 15, 135] 
$$
:::
::::::::::

:::::::::::

::::::::::::

---

::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
For å ta en taxi betaler man en fastpris på $50$ kr og $9$ kr per minutt. 

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Sett opp en funksjon $f$ som gir prisen i $f(x)$ kroner for å ta en taxi i $x$ minutter.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 9x + 50
$$
:::
::::::::::

::::::::::{tab-item} b
Hvor mye koster det å kjøre taxi i $10$ minutter?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(10) = 9\cdot 10 + 50 = 140
$$

Det koster altså $140$ kr å kjøre taxi i $10$ minutter.
:::
::::::::::

::::::::::{tab-item} c
Hvor lenge kan du kjøre taxi for $230$ kr?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
$x = 20
$$

Man kan altså kjøre taxi i $20$ minutter for $230$ kr.
:::
::::::::::
::::::::::::

---

::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
I 1987 kostet en kroneis 6 kr. I 2022 hadde prisen steget til 27 kroner. Vi antar at prisutviklingen har vært tilnærmet lineær i perioden fra 1987 til 2022. 

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Sett opp en funksjon $f$ som gir prisen for en kroneis i $f(x)$ kroner $x$ år etter 1987.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = \dfrac{3}{5}x + 6
$$
:::
::::::::::

::::::::::{tab-item} b
Hvor mye endret prisen på en kroneis seg per år, ifølge modellen?


:::{admonition} Fasit
---
class: answer, dropdown
---
Stigningstallet til $f$ er $a = 3/5$. Prisen på en kroneis har derfor økt med 

$$
a = \dfrac{3}{5} = 0.6
$$

kroner per år.
:::
::::::::::

::::::::::{tab-item} c
En kroneis kostet 1 krone i 1970. 

Hvor mye kostet en krone i 1970 ifølge modellen?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(1970 - 1987) = f(-17) = \dfrac{3}{5} \cdot (-17) + 6 \approx -4.2
$$

Prisen blir negativ som ikke gir praktisk mening. Modellen fungerer altså ikke så langt tilbake i tid. 
:::
::::::::::

::::::::::{tab-item} d
Hvor mye vil en kroneis koste i 2030, ifølge modellen? 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(2030 - 1987) = \dfrac{3}{5} \cdot 43 + 6 \approx 32
$$

Isen koster 32 kroner, noe som kan være rimelig. Modellen ser dermed ut til å fungere greit fremover i tid.
:::

::::::::::
:::::::::::


::::::::::::

---


::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---


::::::::::::

---

::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---
Lydfarten i luft er ca. $343 \, \mathrm{m/s}$ (meter per sekund). Når det lyner ute, produseres det en kraftig lyd som vi kaller torden. 



:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Sett opp en funksjon $f$ som slik at modellen gir $f(x)$ meter lyden reiser på $x$ sekunder etter lynet har slått ned.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 343x
$$
:::
::::::::::

::::::::::{tab-item} b
Hvis du ser lynglimtet, og hører det tordner $6$ sekunder etterpå – hvor langt skjedde lynnedslaget fra deg?


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(6) = 343\cdot 6 = 2058
$$

Lynnedslaget skjedde dermed 2058 m unna der du stod, noe som tilsvarer litt over 2 km. 
:::
::::::::::

::::::::::{tab-item} c
Hvor lang tid vil det ta før du hører torden dersom du er $4 \, \mathrm{km}$ unna lynnedslaget?


:::{admonition} Fasit
---
class: answer, dropdown
---
For å finne svaret må vi løse likningen 
$ 343x = 4000 $

Vi finner da at $x \approx 11,66$. Du hører altså lynnedslaget etter 11,7 sekunder. 

:::
::::::::::
:::::::::::

::::::::::::

---


::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
To av aktørene i Oslo som tilbyr leie av el-sparkesykkel er Ryde og Bolt. De to aktørene har følgende prismodeller: 

:::::{grid}
---
gutter: 3
---

::::{grid-item-card} Ryde
* Startpris: 10 kr
* Pris per minutt: 2.5 kr
::::

::::{grid-item-card} Bolt
* Startpris: 5 kr
* Pris per kilometer: 12 kr
::::


:::::

---

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Sett opp en funksjon $R$ som gir prisen i $R(t)$ kroner for å leie en el-sparkesykkel fra Ryde i $t$ minutter.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
R(t) = 2.5t + 10 = \dfrac{5}{2}t + 10
$$
:::
::::::::::

::::::::::{tab-item} b
Sett opp en funksjon $B$ som gir prisen i $B(x)$ kroner for å leie en el-sparkesykkel fra Bolt for å kjøre $x$ kilometer.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
B(x) = 12x + 5
$$
:::
::::::::::

::::::::::{tab-item} c
Maksfarten til en el-sparkesykkel er 20 km/t. Vi antar at du i gjennomsnitt kjører i 15 km/t (siden du må bremse og følge trafikk og lignende i Oslo sine gater). 

Gjør beregninger og vurder hvilket tilbud som er billigst dersom du skal reise 2 km. 

:::::{admonition} Hint
---
class: dropdown, hints 
---
Du får bruk for vei-fart-tid formelen

$$
s = v\cdot t 
$$

der $s$ er strekning, $v$ er fart og $t$ er tid. 

---

Husk at du også må bruke riktig tidsenhet for å sammenlikne.
:::::
::::::::::

::::::::::{tab-item} d
René kjører ofte el-sparkesykkel og bruker i gjennomsnitt 5 minutter per tur. Anta at han kjører i 15 km/t i gjennomsnitt. 

Hvilket tilbud er mest gunstig for René?
::::::::::
:::::::::::


::::::::::::


---


::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
To biler begynner å kjøre samtidig fra to forskjellige steder. 

* Bil $\mathrm{A}$ kjører fra Oslo i retning nord med en konstant fart på 80 km/t.
* Bil $\mathrm{B}$ kjører fra Lillehammer sør med en konstant fart på 100 km/t. 
* Avstanden fra Oslo til Lillehammer er ca. 180 km.
:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Sett opp en funksjon $f$ som angir avstanden fra Oslo til bil $\mathrm{A}$ i $f(t)$ kilometer etter $t$ timer.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(t) = 80t
$$
:::
::::::::::

::::::::::{tab-item} b
Sett opp en funksjon $g$ som gir avstanden fra Oslo til bil $\mathrm{B}$ i $g(t)$ kilometer etter $t$ timer.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(t) = -100t + 180
$$
:::
::::::::::

::::::::::{tab-item} c
Når vil bilene møte hverandre? 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
t = 1
$$

Bilene møter hverandre etter 1 time. 
:::
::::::::::

::::::::::{tab-item} d
Bilene skal kun kjøre fram til din destinasjon. 

Hva er en passende definisjonsmengde og verdimengde for $f$ og $g$?

:::{admonition} Fasit
---
class: answer, dropdown
---
$ D_f = [0, 2.25] $

$ V_f = [0, 180] $

$ D_g = [0, 1.8] $

$ V_g = [0, 180] $

:::
::::::::::


:::::::::::

::::::::::::