:::::::::::::::{admonition} Oppgave 5
---
class: check
---
En båt skal reise fra en øy $A$ til en øy $C$. <br>
Båten må innom land på en kystlinje på et punkt $B$ for å hente ferskvann. Båten skal reise en så kort som mulig avstand for å spare drivstoff.

Kystlinjen er $9$ km lang. Øy $A$ ligger $2$ km fra land og øy $C$ ligger $4$ km fra land. Se figuren nedenfor.


:::{figure} ./figurer/del_2/oppgave_5/figur.svg
---
width: 90%
class: no-click
---
:::

En strandkiosk $S$ er plassert på starten av kystlinja.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem lengden båten må kjøre fra $A$ til $C$ dersom den går i land $2$ km fra strandkiosken.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å bruke Pytagoras' setning til å bestemme lengdene $AB$ og $BC$.
* Inntil 1 poeng for å bestemme den totale lengden på reisen fra $A$ til $C$.
:::::

:::::{admonition} Fasit
---
class: answer, dropdown
---
Ca. $10.89$ km
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker Pytagoras' setning på de to trekantene med $x = 2$ km som gir at de horisontale katetene er henholdsvis $2$ km og $(9 - 2)$ km. 
Vi regner ut summen av lengdene $AB + BC$ med CAS:

:::{figure} ./figurer/del_2/oppgave_5/a/sol.png
---
width: 80%
class: no-click
---
:::

som betyr at båten da kjører ca. $10.89$ km.

:::::

:::::::::::::


:::::::::::::{tab-item} b
Lag en modell $L$ som gir lengden $L(x)$ som båten må kjøre dersom den går i land en avstand $x$ fra strandkiosken.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å bruke Pytagoras' setning til å bestemme lengdene $AB$ og $BC$.
* Inntil 1 poeng for å sette opp modellen $L(x)$.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
L(x) = \sqrt{4 + x^2} + \sqrt{16 + (9 - x)^2}
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Lengden $L(x)$ vil være summen av lengdene $AB$ og $BC$ for en bestemt verdi av $x \in [0, 9]$. Med Pytagoras' setning følger det at:

\begin{align*}
    AB^2 &= 2^2 + x^2 \limplies AB = \sqrt{4 + x^2} \\
    \\
    BC^2 &= 4^2 + (9 - x)^2 \limplies BC = \sqrt{16 + (9 - x)^2} \\
\end{align*}

Dermed er modellen $L$ gitt ved 

$$
L(x) = AB + BC = \sqrt{4 + x^2} + \sqrt{16 + (9 - x)^2}
$$
:::::

:::::::::::::



:::::::::::::{tab-item} c
Bestem hvor langt unna strandkiosken båten må gå i land for å få kortest mulig reisevei fra $A$ til $C$.

:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å velge riktig fremgangsmåte.
* Inntil 1 poeng for å bestemme $x$ slik at reiseveien er kortest mulig. Maksimalt 0,5 poeng hvis det ikke argumentert for at $x$ gir et bunnpunkt.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 3
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme hvor langt unna strandkiosken båten må gå i land for å få kortest mulig reisevei, løser vi likningen $L'(x) = 0$ for å finne kandidater for bunnpunkter til $L$. Vi løser likningen med CAS:

:::{figure} ./figurer/del_2/oppgave_5/c/sol_1.png
---
width: 100%
class: no-click
---
:::

som forteller oss at $x = 3$ er en kandidat for et bunnpunkt. For å være sikre på at dette er et bunnpunkt, holder det å sjekke $L(x)$ i endepunktene og sammenligne med $L(3)$:

:::{figure} ./figurer/del_2/oppgave_5/c/sol_2.png
---
width: 80%
class: no-click
---
:::

Vi ser altså at $L(3) < L(0)$ og $L(3) < L(9)$, og dermed er $x = 3$ et bunnpunkt. Dermed må båten gå i land $3$ km fra strandkiosken for å få kortest mulig reisevei fra $A$ til $C$.

:::::

:::::::::::::


::::::::::::::


:::::::::::::::
