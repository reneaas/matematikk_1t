# Generalisering av representasjoner


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke skjæringen mellom en linje og en andregradsfunksjon til å bestemme funksjonsuttrykk. 
:::


Når vi har arbeidet med nullpunktsform, så har vi sett at vi kan skrive en andregradsfunksjon på formen

$$
f(x) = a(x - x_1)(x - x_2)
$$

der $x = x_1$ og $x = x_2$ er punktene der grafen skjærer $x$-aksen. Men $x$-aksen svarer til linja $y = 0$. Hva om vi vet hvor en andregradsfunksjonen skjærer en annen linje, for eksempel $y = b$? Eller en kanskje vi vet hvor grafen skjærer en skrå linje $y = mx + b$? Kan vi bruke denne informasjonen til å bestemme funksjonsuttrykket til andregradsfunksjonen? Svaret er ja, i begge tilfeller. Det er det vi skal bruke resten av dette kapittelet på å systematisere.



## Skjæring med en horisontal linje $y = b$

:::::::::::::::{summary} Representasjon: Skjæring med en linje $y = b$
Hvis grafen til $f$ skjærer en linje i to punkter $(x_1, b)$ og $(x_2, b)$, kan vi skrive funksjonsuttrykket til $f$ som

$$
f(x) = a(x - x_1)(x - x_2) + b
$$

der $a$ er den ledende koeffisienten til andregradsfunksjonen, akkurat som før. Se figuren nedenfor:


:::{plot}
width: 70%
function: (x - 1) * (x + 2) + 3, f
point: (1, f(1))
point: (-2, f(-2))
ticks: off
hline: 3
ymin: -2
annotate: (3, 0), (3, 3), "$y = b$", -0.3
:::


:::::::::::::::