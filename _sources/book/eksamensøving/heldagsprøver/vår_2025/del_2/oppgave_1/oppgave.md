:::::::::::::::{admonition} Oppgave 1 
---
class: check
---
På bakkenivå er lufttrykket 1 atm (atmosfærisk trykk). Lufttrykket avtar med $12 \, \%$ per km i høyden.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar at en modell som passer med beskrivelsen ovenfor er 

$$
L(x) = 1 \cdot 0.88^x
$$

der $L(x)$ er det atmosfæriske trykket $x$ kilometer over bakken.

:::::{admonition} Løsning
---
class: solution, dropdown
---
$L$ vil være en eksponentiell modell siden lufftrykket avtar med en prosentvis endring per km. Derfor er det modell på formen

$$
L(x) = a \cdot b^x 
$$

der $a$ er startverdien ved $x = 0$ og $b$ er vekstfaktoren. Ved $x = 1$ er $L(0) = 1$ som betyr at $a = 1$. Siden lufttrykket avtar med $12 \, \%$ per km, er vekstfaktoren $b = 1 - 0.12 = 0.88$. Dermed får vi at

$$
L(x) = a \cdot b^x = 1 \cdot 0.88^x
$$
:::::



:::::::::::::


:::::::::::::{tab-item} b
Ved hvilken høyde er lufttrykket halvparten av det på bakkenivå?


:::::{admonition} Fasit
---
class: answer, dropdown
---
Ca. $5.42$ km over bakken.
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme hvilken høyde lufttrykket er halvparten av det på bakkenivå, må vi løse likningen

$$
L(x) = \frac{1}{2}L(0)
$$

Vi bruker CAS til å løse likningen:

:::{figure} ./figurer/del_2/oppgave_1/b.png
---
width: 100%
class: no-click
---
:::

som betyr at lufttrykket er halvparten av det på bakkenivå ved $x \approx 5.42$ km over bakken.

:::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem stigningstallet til linja som går gjennom $(0, L(0))$ og $(8, L(8))$. <br> Gi en praktisk tolkning av svaret.


:::::{admonition} Fasit
---
class: answer, dropdown
---

:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Stigningstallet til linja som går gjennom punktene $(0, L(0))$ og $(8, L(8))$ svarer til den gjennomsnittlige vekstfarten til $L$ i intervallet $[0, 8]$. Vi regner ut dette med CAS:

:::{figure} ./figurer/del_2/oppgave_1/c.png
---
width: 100%
class: no-click
---
:::

Stigningstallet til linja er altså ca. $-0.08$ atm/km. Det betyr at lufttrykket i gjennomsnitt blir $0.08$ atm lavere per km i høyden fra bakkenivå opp til $8$ km over bakken.

:::::

:::::::::::::

::::::::::::::

:::::::::::::::

