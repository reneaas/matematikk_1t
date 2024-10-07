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


## Ulikheter med CAS

:::::{admonition} Utforsk 3
---
class: explore
---
Under vises et *interaktivt* CAS-vindu der en lineær ulikhet er løst, både med `Løs`{l=geogebra}-funksjonen og <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen. 

::::{tab-set}
:::{tab-item} Med `Løs`{l=geogebra}-funksjonen
```{raw} html
---
file: ggb/utforsk/utforsk_3_cmd.html
---
```
:::

:::{tab-item} Med <img src="figurer/icons/mode_solve.svg" class="inline-image"/>-knappen
```{raw} html
---
file: ggb/utforsk/utforsk_3_gui.html
---
```
:::

::::


Deloppgave 1
: Hvilken ulikhet er det som er løst? <br> Kan du lese av løsningen som er funnet?


Deloppgave 2
: Bruk CAS-vinduene til å løse ulikheten $3x + 5 \leq -2x + 7$. <br> Får du samme svar med begge metodene? <br> *Tips: for å få symbolet $\leq$ kan du skrive `<`{l=geogebra} etterfulgt av `=`{l=geogebra} i CAS-vinduet.*

:::::

## Oppgaver
Når du løser oppgavene under, skal du bruke desktopversjonen av GeoGebra. Den åpner du ved å skrive "Geogebra 6" i søkefeltet på maskina di. For å få opp CAS, velger du *vis* i menyen til høyre, og huker av for CAS. 

::::{admonition} Oppgave 1 
---
class: problem-level-1, full-width
---
Løs likningene ved hjelp av CAS. 

Deloppgave 1
: $ \dfrac{1}{2}x - 1 = \dfrac{1}{3}x + \dfrac{1}{6}$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 7$
:::

Deloppgave 2
: $ \dfrac{x}{2} - 2 = \dfrac{x}{3} + 1$
:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 18$
:::

Deloppgave 3
: $ \dfrac{1}{2}\left(2x-3\right)=-\left(x+3/2\right)$
:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 0$
:::

Deloppgave 4
: $ \dfrac{x-2}{2}=\dfrac{2-x}{3}$
:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 2$
:::
:::: 

::::{admonition} Oppgave 2
---
class: problem-level-1, full-width
---
Løs likningene ved hjelp av CAS. 

Deloppgave 1
: $ 3\left(\dfrac{x}{2}-\dfrac{4}{3}\right)=2\left(\dfrac{3}{4}-\dfrac{x}{6}\right)$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 3$
:::

Deloppgave 2
: $ 3\left(\dfrac{s}{4}-\dfrac{1}{10}\right)=2\left(w-\dfrac{1}{5}\right)$

:::{admonition} Fasit
---
class: answer, dropdown
---
$s = \dfrac{2}{25}$
:::

Deloppgave 3
: $\dfrac{3}{2}\left(t-1\right) - 2\left(\dfrac{1}{4}-t\right)=0$

:::{admonition} Fasit
---
class: answer, dropdown
---
$t = \dfrac{4}{7}$
:::

Deloppgave 4
: $ \dfrac{1}{3}y-2y + 3 = -\dfrac{1}{9}y + \dfrac{1}{9}$

:::{admonition} Fasit
---
class: answer, dropdown
---
$y = \dfrac{13}{7}$
:::
::::

::::{admonition} Oppgave 3
---
class: problem-level-1, full-width
---
Løs likningssettene ved hjelp av CAS. 

Deloppgave 1
: \begin{align*}
    3x+y &=7 \\
    x−y &=1
\end{align*}

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 2, y= 1$
:::

Deloppgave 2
: \begin{align*}
    x-2y &=7 \\
    x+y &=1
\end{align*}

:::{admonition} Fasit
---
class: answer, dropdown
---
$x=3, y=-2$
:::

Deloppgave 3
: \begin{align*}
    x+2y &=5 \\
    4x &=6−y
\end{align*}

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 1, y=2$
:::

Deloppgave 4
: \begin{align*}
    −2x+y &=−1 \\
4x+2y+14 &=0
\end{align*}

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = -\dfrac{3}{2}, y= -4$
:::

::::

::::{admonition} Oppgave 4
---
class: problem-level-1, full-width
---
Løs ulikhetene ved hjelp av CAS. 

Deloppgave 1
: $\dfrac{x}{3}+\dfrac{1}{2} \leq \dfrac{x}{2}+\dfrac{1}{3}$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x \geq 1$
:::

Deloppgave 2
: $−2x+3≥\geq x−5$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x \leq \dfrac{8}{3} $
:::

Deloppgave 3
: $2x-1<x+4$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x < 5$
:::

Deloppgave 4
: $\dfrac{x}{2}+3 >x-1$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x < 8$
:::
::::

::::{admonition} Oppgave 5
---
class: problem-level-2, full-width
---
Sett opp likninger og løs ved hjelp av CAS

Deloppgave 1
: Stian, Erik og Øyvind delte en pizza. Stian spiste en tredel, Erik spiste to femtedeler, og Øyvind spiste resten. Hvor mye spiste Øyvind? 

:::{admonition} Fasit
---
class: answer, dropdown
---
Øyvind spiste $\dfrac{4}{15}$
:::

Deloppgave 2
: Kristin, Anette og Ellen har til sammen 1 100 kroner. Ellen har dobbelt så mange penger som Anette, og Kristin har 100 kroner mindre enn Ellen. Hvor mye penger harr hver av de tre jentene?

:::{admonition} Fasit
---
class: answer, dropdown
---
Anette har 240 kr, Ellen har 480 kroner, Kristin har 380 kroner.
:::

Deloppgave 3
: På en aktivitetsdag ved skolen valgte 60 % av elevene fotball. En tredel valgte volleyball. De siste 12 elevene hadde fått fritak. Hvor mange elever er det ved skolen? 

:::{admonition} Fasit
---
class: answer, dropdown
---
Det var $180$ elever ved skolen.
:::

Deloppgave 4
: Per, Pål og Espen er til sammen 66 år. Per er dobbelt så gammel som Espen, og Pål er 6 år eldre enn Espen. Finn ut hvor gamle de tre guttene er. 

:::{admonition} Fasit
---
class: answer, dropdown
---
Espen er 15 år, Per er 30 år og Pål er 21 år. 
:::


Deloppgave 5
: Ari, Anette og far er til sammen 54 år. Anette er dobbelt så gammel som Ari, og far er tre ganger så gammel som Anette. Hvor gamle er Ari, Annette og far? 

:::{admonition} Fasit
---
class: answer, dropdown
---
Ari er 6 år, Anette er 12 år, Far er 36 år. 
:::


Deloppgave 6
: Far er tre ganger så gammel som Per, og bestefar er dobbelt så gammel som far. Til sammen er de 120 år. Hvor gamle er de?

:::{admonition} Fasit
---
class: answer, dropdown
---
Per er 12 år, far er 36 år og bestefar er 72 år.
:::


Oppgave 7
: Mormor var 22 år da mor ble født. I dag er hun dobbelt så gammel som mor. Hvor gamle er mor og mormor?

:::{admonition} Fasit
---
class: answer, dropdown
---
Mor er 22, mormor er 44.
:::

Deloppgave 8
: Far er tre ganger så gammel som Camilla. Far er seks år eldre enn onkel Kåre. Til sammen er de tre 92 år. Hvor gamle er Camilla, far og onkel Kåre? 

:::{admonition} Fasit
---
class: answer, dropdown
---
Camilla er 14 år, far er 42 år, Kåre er 36 år.
:::

Deloppgave 9
: Mor er 21 år eldre enn Maja. Bestefar er tre ganger så gammel som mor. Om to år er de til sammen 100 år. Hvor gamle er de?

:::{admonition} Fasit
---
class: answer, dropdown
---
Maja er 2 år, mor er 23 år, bestefar er 69 år. 
:::

::::

::::{admonition} Oppgave 6
---
class: problem-level-3, full-width
---
På en fotballkamp er det tre kategorier billetter: barn, voksne og pensjonister. 

Publikumstallet på kampen var 2100. Barnebilletten kostet 50 kr, voksenbilletten 200 kr og pensjonistbilletten 100 kr. Billettinntektene ble på 315 000 kr. Det var dobbelt så mange pensjonister som barn på kampen. 

Bestem antallet barn, voksne og pensjonister på kampen.

:::{admonition} Fasit
---
class: answer, dropdown
---
Det var 300 barn, 600 pensjonister og 1200 voksne på kampen.
:::
::::

::::{admonition} Oppgave 7
---
class: problem-level-3, full-width
---

Bestem $a, b, c$ når du vet at:
\begin{align*}
a - b + c &= -11 \\
a + b + c &= 11 \\
8a + 4b + 2c &= -4
\end{align*}    

:::{admonition} Fasit
---
class: answer, dropdown
---
$a=-8, b=11, c=8$
:::
::::