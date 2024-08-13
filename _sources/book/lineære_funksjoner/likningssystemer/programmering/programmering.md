# Programmering av likningssystemer

:::{admonition} Læringsmål
---
class: tip
---
Målet etter dette delkapittelet er at du skal kunne:
* Lese og forstå enkle program som løser lineære likningssystemer. 
* Kunne bruke og justere programkode for å løse lineære likningssystemer.
:::

:::{admonition} Bakgrunnsteori
---
class: warning, margin
Her kan det være lurt å ha vært borti minst én type løkke. Ta en titt på (`for`{l=python}-løkker)[../../../programmering/for_loops/for_loops.md]
:::


Akkurat som med likninger, kan vi bruke numeriske metoder for å finne omtrentlige løsninger til likningssystemer. I fåtall av tilfeller kan vi bestemme de eksakt, men i den virkelige verden må man som oftest si seg fornøyd med omtrentlige løsninger.

:::::{admonition} Utforsk 1
---
class: explore
---
Under vises et interaktivt kodevindu med et program som forsøker å løse et likningssystem. 


:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html
---
:::

<br>

Deloppgave 1
: Kan du forklare hvilket likningssystem programmet prøver å løse? <br> Gir programmet riktig løsning?


<br>

Deloppgave 2
: Kan du gi en forklaring av strategien programmet bruker for å løse likningssystemet? 


<br>

Deloppgave 3
: Endre programmet slik at det finner løsningen til likningssystemet

    \begin{align*}
    x + 2y &= 5 \\
    4x + y &= 6
    \end{align*}

<br>

Deloppgave 4
: Hvis du endrer programmet til å forsøke og løse likningssystemet 

    \begin{align*}
    x - 2y &= 7 \\
    2x + y &= 1
    \end{align*}
    
    finner ikke programmet noen løsning. Hva er grunnen til det?

:::::
