# CAS-kurs: del 1

:::{admonition} Læringsmål: CAS-kurs del 1
---
class: tip
---
Etter du har gått gjennom dette delkapittelet, er målet at du skal kunne:
* Løse lineære likninger med CAS
* Løse lineære likningssystemer med to ukjente med CAS
* Løse lineære ulikheter med CAS.

:::


## Likninger med CAS

Å løse likninger i CAS kan gjøres enten ved å bruke `Løs`{l=geogebra}-funksjoner (`Solve`{l=geogebra} på engelsk) eller ved å trykke på <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen.


::::{admonition} Hva gjør `$1`{l=geogebra}?
---
class: sidenote, margin
---
I CAS-vinduet i {ref}`Utforsk 1 <cas-del-1-utforsk-1>` har vi brukt `Løs($1, x)`{l=geogebra} for å løse likningen. Dette er fordi likningen står i celle nr. 1 og ved å skrive `$1`{l=geogebra}, setter vi inn innholdet i celle 1 inn i `Løs`{l=geogebra}-funksjonen.
::::

::::::{admonition} Utforsk 1: likninger med CAS
---
class: explore
name: cas-del-1-utforsk-1
---
Under vises et *interaktivt* CAS-vindu der en lineær likning er løst på to forskjellige måter. 
:::::{tab-set}

::::{tab-item} Med `Løs`{l=geogebra}-funksjonen
**Oppskrift**: <br>
1. Skriv inn likningen i CAS-vinduet.
2. Bruk `Løs`{l=geogebra}-funksjonen for å løse likningen.

:::{raw} html
---
file: ggb/utforsk/utforsk_1_cmd.html
---
:::

::::

::::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>
**Oppskrift**: <br>
1. Skriv inn likningen i CAS-vinduet.
2. Trykk på <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen for å løse likningen.

:::{raw} html
---
file: ggb/utforsk/utforsk_1_click_interface.html
---
:::
::::

:::::


Deloppgave 1
: Hvilken lineær likning er løst i CAS-vinduet? <br> Løs likningen for hånd og sjekk svaret.


<br>

Deloppgave 2
: Bruk CAS-vinduene til å løse likningen $3x + 5 = -2x + 7$. <br> Får du samme svar med begge metodene? <br> *Tips: du trenger ikke slette det som står der allerede, bare start i celle 3!*


::::::


::::::{admonition} Underveisoppgave 1
---
class: check
---
Løs følgende likninger med CAS-vinduet under.  

* $2x + 3 = 7$
* $3x - 5 = 2x + 1$
* $\dfrac{3}{2}x - 3 = 2x + 5$

Bruk både `Løs`{l=geogebra}-funksjonen og <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen til å løse likningene.

:::{raw} html
---
file: ggb/underveisoppgaver/oppgaver/underveisoppgave_1_tomt_cas_vindu.html
---
:::

:::::{admonition} Løsning
---
class: solution, dropdown
---
::::{tab-set}
:::{tab-item} Med `Løs`{l=geogebra}-funksjonen
Legg merke til at vi kan skrive likningen direkte inn i `Løs`{l=geogebra}-funksjonen også (se celle 5).
```{raw} html 
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_1_cmd_solve.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
```{raw} html
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_1_gui_solve.html
---
```
:::
::::
:::::

::::::


## Likningssystemer med CAS
Vi kan også løse likningssystemer med både `Løs`{l=geogebra}-funksjonen og <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen i CAS.


:::::{admonition} Utforsk 2: likningssystemer med CAS
---
class: explore
---
Under vises et *interaktivt* CAS-vindu der et likningssystem er løst på to forskjellige måter. 

::::{tab-set}
:::{tab-item} Med `Løs`{l=geogebra}-funksjonen
**Oppskrift**: <br>

1. Skriv inn hver likning i hver sin celle. 
2. Bruk `Løs`{l=geogebra}-funksjonen for å løse likningssystemet. <br> Legg merke til at likningene og variablene plasseres i hver sin liste `{}`{l=python}.

```{raw} html
---
file: ggb/utforsk/utforsk_2_cmd.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
**Oppskrift**: <br>

1. Skriv inn hver likning i hver sin celle. 
2. Marker likningene (dra musepekeren over cellenumrene - ikke bare trykk på cellene). 
3. Trykk på <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen for å løse likningssystemet.

```{raw} html
---
file: ggb/utforsk/utforsk_2_gui.html
---
```
:::
::::


Deloppgave 1
: Hvilket likningssystem er løst i CAS-vinduet? <br> Kan du lese av løsningen som er funnet?


Deloppgave 2
: Bruk CAS-vinduene til å løse likningssystemet
    \begin{align*}
    2x + y & = 5 \label{1a} \quad\quad\quad \tag{1a} \\
    x - y & = 1 \label{1b} \quad\quad\quad \tag{1b} 
    \end{align*}
:::::



::::::{admonition} Underveisoppgave 2
---
class: check
---
Løs følgende likningssystemer med CAS vinduet under:

Likningssystem 1
:    \begin{align*}
    3x + y & = 7 \\
    x - y & = 1
    \end{align*}

Likningssystem 2
:    \begin{align*}
    x - 2y & = 7 \\
    2x + y & = 1
    \end{align*}

Likningssystem 3
:    \begin{align*}
    x + 2y & = 5 \\
    4x & = 6 - y
    \end{align*}


:::{raw} html
---
file: ggb/underveisoppgaver/oppgaver/underveisoppgave_2_tomt_cas_vindu.html
---
:::


:::::{admonition} Løsning
---
class: dropdown, solution
---
::::{tab-set}
:::{tab-item} Med `Løs`{l=geogebra}-funksjonen
```{raw} html
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_2_cmd_solve.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
```{raw} html
---
file: ggb/underveisoppgaver/løsninger/underveisoppgave_2_gui_solve.html
---
```
:::
::::
:::::

::::::