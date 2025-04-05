:::::::::::::::{admonition} Oppgave 6
---
class: check
---
Nedenfor vises et kvadrat med sidelengder $3$. 

Kvadratet er fylt med mindre fargelagte kvadrater som blir mindre og mindre.

:::{figure} ./figurer/del_2/oppgave_6/figur.svg
---
width: 80%
class: no-click
---
:::

Lag et program som regner ut summen av arealet til de 100 største fargelagte kvadratene.


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å skrive et program som bruker en løkke som regner ut arealet av $100$ kvadrater.
* Inntil 1 poeng for å bestemme riktig sum av arealene. 

Mindre mangler i programmet kan fortsatt gi noe uttelling. Programmet bør være rimelig forklart med kommentarer eller en overordnet forklaring for å gi full utelling.
:::::


:::::{admonition} Løsning
---
class: answer, dropdown
---
Først kan vi legge merke til at sidelengdene i det største fargelagte kvadratet er $3/2$. Deretter halveres sidelengden for hvert mindre fargelagte kvadrat. For å summere arealet til de 100 største fargelagte kvadratene, kan vi derfor bruke en løkke som gjør følgende:

1. Regner ut arealet $A$ av kvadrat med sidelengde $\ell$ ved $A = \ell^2$.
2. Legger til arealet til summen $s \to s + A$. 
3. Halverer sidelengden $\ell \to \ell / 2$.

Vi gjentar dette 100 ganger.

**Programkode**:
:::{code-block} python
---
linenos:
---
s = 0 # sum av arealer
lengde = 3 / 2 # sidelengder i første kvadrat

# summerer de 100 største fargelagte kvadratene
for i in range(100):
    areal = lengde ** 2 # areal av kvadrat
    s = s + areal    # legg til arealet
    
    lengde = lengde / 2 # halver sidelengden

print(s)
:::

**Utskrift**:

:::{code-block} console
2.9999999999999996
:::

Arealet til de 100 største fargelagte kvadratene er ca. $3$.

:::::

:::::::::::::::


