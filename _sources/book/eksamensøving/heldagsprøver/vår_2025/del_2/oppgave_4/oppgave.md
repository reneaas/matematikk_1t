:::::::::::::::{admonition} Oppgave 4
---
class: check
---
Nedenfor vises en sylinder fylt med vann med et lite hull i bunnen.

:::{figure} ./figurer/del_2/oppgave_4/merged_figure.svg
---
width: 80%
class: no-click
---
:::

Den horisontale avstanden vannstrålen beveger seg er $S_i$ meter når vannstanden er $x_i$ meter over bunnen av sylinderen. I tabellen nedenfor vises et datamateriale for dette.


| $x$ (meter) | $8$ | $6$ | $5$ | $3$ | $2$ | 
|:------------|:---:|:---:|:---:|:---:|:---:|
| $S$ (meter) | $5.66$ | $4.90$ | $4.47$ | $3.46$ | $2.83$ |

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en modell på formen 

$$
S(x) = a \cdot x^b
$$

som viser hvor mange meter $S(x)$ vannstrålen beveger seg horisontalt når vannstanden er $x$ meter over bunnen av sylinderen.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
S(x) \approx 2 \cdot x^{0.5} = 2\sqrt{x}
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi skriver inn datapunktene i et regneark i Geogebra:

:::{figure} ./figurer/del_2/oppgave_4/a/regneark.png
---
width: 30%
class: no-click
---
:::

Deretter gjør vi regresjonsanalyse og velger en potensfunksjon som modell siden dette er modelltypen som er oppgitt som gir:

:::{figure} ./figurer/del_2/oppgave_4/a/modell.png
---
width: 100%
class: no-click
---
:::

som betyr at 

$$
S(x) \approx 2\cdot x^{0.5} = 2\sqrt{x}
$$

er en passende modell for datamaterialet. 

> Vi definerer $S(x)$ som dette i resten av oppgaven.

:::::

:::::::::::::


:::::::::::::{tab-item} b
Etter at hullet ble åpnet, varierte høyden til vannstanden med tiden slik at den kan beskrives av en modell på formen 

$$
h(t) = k(t - r)^2. 
$$

Når hullet i bunnen ble åpnet var vannstanden $10$ meter over bunnen. Tanken ble halvfull etter $7$ sekunder.

Bestem $k$ og $r$. Gi en praktisk tolkning av konstanten $r$. 


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
k \approx 0.02 \and r \approx 23.9
$$

Den praktiske tolkningen av $r$ er at det tar $r \approx 23.9$ sekunder før tanken er tom for vann.
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Modellen $h$ er en andregradsfunksjon skrevet på ekstremalform. Fra opplysningene kan vi sette opp et likningssystem:

\begin{align*}
    h(0) &= 10 && \text{(høyden når hullet åpnes er 10 meter)} \\
    \\
    h(7) &= 5 && \text{(tanken er halvfull etter 7 sekunder)} \\
\end{align*}

Vi bestemmer $k$ og $r$ ved å løse likningssystemet i CAS:

:::{figure} ./figurer/del_2/oppgave_4/b/sol.png
---
width: 100%
class: no-click
---
:::

som gir oss at 

$$
k \approx 0.02 \and r \approx 23.9
$$

Siden $h(t)$ er skrevet på ekstremalform med en ekstremalverdi som er $y_0 = 0$, vil $t = r$ svare til $t$-koordinaten til bunnpunktet og nullpunktet til $h$. Den praktiske tolkningen er at det tar $r = 23.9$ sekunder før tanken er tom for vann.


:::::



:::::::::::::


:::::::::::::{tab-item} c
Hvor lang tid tar det før lengden av strålen og høyden på vannstanden er like?



:::::{admonition} Fasit
---
class: answer, dropdown
---
$t \approx 9.76$ sekunder
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi har to modeller:
* $S(x)$ som gir oss lengden av strålen for en gitt høyde $x$ på vannstanden.
* $h(t)$ som gir oss høyden på vannet for en gitt tid $t$.

For å bestemme hvor lang tid det tar før lengden av strålen og høyden på vannstanden er like, løser vi oppgaven i to steg:
1. Vi løser $S(x) = x$ for å avgjøre når strålen og høyden er like.
2. Vi løser $h(t) = x$ for løsningen vi fikk i steg 1 for å avgjøre *når* vi er ved høyden som er lik lengden av strålen.

Vi løser dette med CAS:

:::{figure} ./figurer/del_2/oppgave_4/c/sol.png
---
width: 100%
class: no-click
---
:::

Her finner vi fra steg 1 at $x = 4$ er høyden der lengden av strålen og høyden på vannstanden er like. Så løser vi $h(t) = 4$ for å avgjøre hvor lang tid det tok før vannstanden hadde denne høyden, som ga oss to løsninger:

$$
t \approx 9.76 \or t \approx 38.04.
$$

Men vi vet allerede at vanntanken er tom etter $t \approx 23.9$ sekunder, som betyr at vi kan konkludere at høyden til vannstanden og lengden på vannstrålen var like etter $t \approx 9.76$ sekunder.


:::::





:::::::::::::

::::::::::::::


:::::::::::::::