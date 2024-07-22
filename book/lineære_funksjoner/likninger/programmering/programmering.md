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

::::{admonition} Hva er vitsen?
---
class: sidenote, margin
---
Å løse lineære likninger numerisk kan virke litt *teit*. Vi kan jo løse lineære likninger eksakt! Men det er mange likninger for praktiske problemer som ikke kan løses eksakt, og da er det viktig at vi får trent på å løse enklere likninger numerisk fordi vi også kan verifisere svaret. Dette gjør at vi kan løse de mer virkelighetsnære likningene med samme strategi, og at vi kan stole på at svaret vi får stemmer.

::::

Å løse likninger **numerisk** betyr å finne en tilnærmet tallverdi for løsningen ved hjelp av et program. For å bestemme løsningen av en likning numerisk, bruker man gjerne en systematisk metode for å gradvis nærme seg løsningen. En slik metode kalles for en **numerisk metode**. En numerisk metode kan oftest formuleres ved hjelp av en **algoritme**. En algoritme er en oppskrift som forteller oss nøyaktig hvilke steg vi skal gjøre for å utføre en bestemt numerisk metode.


Å løse lineære likninger numerisk kan virke litt tåpelig siden vi kan jo løse disse likningene analytisk (les: *finne et eksakt svar*). 

Vi skal gå løs på et eksempel for å illustrere hvordan vi kan løse en likning numerisk. 

:::::{admonition} Eksempel 1
---
class: example
name: lineær-likning-programmering-numerisk-eksempel-1
---

Vi skal løse likningen 

$$
2x - 4 = 0.
$$

Vi tenker oss at vi har en funksjon $f(x) = 2x - 4$ og at vi skal bestemme nullpunktet til $f$. En nokså rett fram algoritme er å starte med en startverdi for $x$ på nedsiden av nullpunktet til $f$, og så gradvis øke verdien til $x$ med en endring $\Delta x$ til vi har passert nullpunktet til $f$. Flytdiagrammet under illustrerer algoritmen.

:::{include} ./flytdiagrammer/eksempel_1.md
:::

<br>

Det vi må finne ut av nå, er hvordan vi skal kunne utføre stegene i algoritmen med et program. 

```{code-block} python
---
linenos: true
---
x_start = -10               # Startverdi for x
dx = 0.001                  # Liten endring Δx 
x = x_start                 # Sett første `x`-verdi lik startverdien

while abs(2*x - 4) > 0.000001:  # Så lenge |f(x)| > 0.000001  
    x = x + dx                  # Øk x med dx

print(x)
```

:::::


## Oppgaver