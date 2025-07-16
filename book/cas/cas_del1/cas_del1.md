# CAS-kurs: Del 1

:::{admonition} Læringsmål
---
class: tip
---
* Kunne løse lineære likninger med CAS.
* Kunne løse lineære likningssystemer med CAS.
* Kunne løse lineære ulikheter med CAS.
:::


CAS er en forkortelse for *Computer Algebra System*. CAS består av en samling funksjoner som er utviklet for å løse matematiske problemer symbolsk (algebraisk) på datamaskin på liknende vis som vi gjør når vi regner for hånd. Kan et problem løses for hånd, kan det også løses med CAS. Men CAS kan også løse problemer som ikke kan lar seg løses for hånd også! 


## Likninger

For å løse likninger med CAS, skriver vi inn likningen først – deretter bruker vi én av to innebygde funksjoner:
1. Vi bruker <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> for å løse likningen {popup}`eksakt.<Eksakt løsning vil si at vi får et svar som er det nøyaktige svaret. Svaret kan blant annet inneholde kvadratrøtter eller brøker.>`
2. Vi bruker <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/> for å løse likningen {popup}`numerisk.<Numerisk løsning vil så si at vi får et tall som svar som ikke nødvendigvis er det nøyaktige svaret, men et omtrentlig svar. Svaret er ofte et desimaltall.>` 



### Eksakt løsning


:::{margin}
For å skrive gangetegn i CAS-vinduet, bruker vi `*` mellom tall og variabler.
:::

:::::::::::::::{explore} Utforsk 1
I {numref}`fig-cas-kurs-del-1-likninger-gif` nedenfor vises det hvordan man kan løse en likning eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> i CAS.


:::{figure} ./videoer/cas-likninger.gif
---
width: 80%
class: no-click, adaptive-figure
name: fig-cas-kurs-del-1-likninger-gif
---
viser hvordan vi løser en likning eksakt med CAS. Vi skriver inn likningen og trykker på <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> for å løse den.
:::


:::{cas-popup} 400 500
:::

<br>

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvilken likning er det som er løst i {numref}`fig-cas-kurs-del-1-likninger-gif`?


:::::{answer}
$$
2x - 6 = 0
$$
:::::


:::::::::::::


:::::::::::::{tab-item} b
Bruk CAS til å løse likningen som er vist i {numref}`fig-cas-kurs-del-1-likninger-gif` med å følge fremgangsmåten som er vist i figuren.


:::::{answer}

:::{figure} ./figurer/utforsk/utforsk_1/b.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Løsningen av likningen er derfor 

$$
x = 3
$$

:::::

:::::::::::::

::::::::::::::


:::::::::::::::


---



:::::::::::::::{underveisoppgave} Underveisoppgave 1
> I denne oppgaven skal du bruke CAS-vinduet til å løse likninger. Klikk på det, så popper det opp et CAS-vindu kan flytte rundt og endre størrelse på. 

:::{cas-popup} 400 500
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen 

$$
x + 5 = 0
$$


::::{solution}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/a.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er løsningen av likningen

$$
x = -5
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Løs likningen

$$
2x - 7 = 0
$$


::::{solution}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/b.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er løsningen av likningen

$$
x = \frac{7}{2}
$$

::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningen

$$
x^2 - x - 2 = 0
$$

> For å skrive $x^2$ i CAS-vinduet kan du skrive `x^2` eller
> * <img src="/_static/icons/misc/windows-logo.svg" class="inline-image"/> skriv `x` etterfulgt av "alt" + "2" på tastaturet
> *  skriv `x` etterfulgt av trykke på "option" + "2"


::::{solution}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/c.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er løsningen av likningen

$$
x = 2 \quad \text{eller} \quad x = -1
$$

::::


:::::::::::::

::::::::::::::


:::::::::::::::


### Numerisk løsning

I tilfeller hvor vi regner på noe praktisk kan det være naturlig å bruke numerisk løsning med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>. I disse tilfellene vil det gjerne være beregninger der vi er ute at et omtrentlig tallsvar som vi kunne målt i praksis. Andre ganger finnes det ikke en eksakt løsning i det hele tatt, men det går likevel an å finne en numerisk løsning.


:::::::::::::::{explore} Utforsk 2
---
class: tabs-parts
---
Nedenfor vises et CAS-vindu som løser en likning **eksakt** med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> og **numerisk** med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
1. Hvilken likning er det som er løst i CAS-vinduet?
2. Hva er den **eksakte** løsningen?
3. Hva er den **numeriske** løsningen?

:::::::::::::

:::::::::::::{tab-item} b
Bruk CAS-vinduet til å løse likningen

$$
x^2 - 3x + 1 = 0
$$

1. Eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/>
2. Numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>

::::{solution}
:::{figure} ./figurer/utforsk/utforsk_2/b.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::
::::::::::::::


:::{ggb} 600 300
---
material_id: wmageskb
toolbar: "true"
---
:::

:::::::::::::::


---


:::::::::::::::{underveisoppgave} Underveisoppgave 2
> Bruk CAS-vinduet til å løse likningene nedenfor. Løs de både eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> og numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>.

:::{cas-popup} 400 500
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
x^2 - 5 = 0
$$

::::{solution}
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/a.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::


:::::::::::::{tab-item} b
Løs likningen

$$
x^2 - 4x = 8
$$


::::{solution}
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/b.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningen

$$
x^3 - 4x^2 + 3x + 2 = -x + 3
$$


::::{solution}
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/c.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::

:::::::::::::

::::::::::::::


:::::::::::::::


## Ulikheter

For å løse ulikheter med CAS, bruker vi akkurat de samme funksjonene som vi bruker for å løse likninger. Forskjellen ligger i at vi må bruke ulikhetstegn i stedet for likhetstegn når vi skriver inn ulikhetene. 



### Eksakt løsning

:::::::::::::::{explore} Utforsk 3
I {numref}`fig-cas-kurs-del-1-ulikheter-eksakt-gif` nedenfor viser vi hvordan vi løser en ulikhet eksakt med CAS. Fremgangsmåten er lik den for likninger hvor vi:
1. Skriver inn ulikheten
2. Trykket på <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> for å løse den.


:::{figure} ./videoer/cas-ulikheter-eksakt.gif
---
width: 80%
class: no-click, adaptive-figure
name: fig-cas-kurs-del-1-ulikheter-eksakt-gif
---
viser hvordan vi løser en ulikhet eksakt med CAS. Vi skriver inn ulikheter og så trykker vi på <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> for å løse dem.
:::


:::{cas-popup} 400 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk CAS-vinduet til å løse ulikheten som løses i {numref}`fig-cas-kurs-del-1-ulikheter-eksakt-gif`.

:::::::::::::

:::::::::::::{tab-item} b
Bruk CAS-vinduet til å løse ulikheten

$$
-2x + 5 < 0 
$$


:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{underveisoppgave} Underveisoppgave 3
Bruk CAS-vinduet til å løse ulikheten nedenfor. 

:::{cas-popup} 400 500
:::


::::::::::::::{tab-set}
---
class: tabs-parts 
---
:::::::::::::{tab-item} a
$$
2x - 1 > 0
$$


:::::{answer}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/a.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::


:::::::::::::


:::::::::::::{tab-item} b
$$
-4x + 5 < 0
$$

:::::{answer}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/b.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::
:::::::::::::


:::::::::::::{tab-item} c
$$
7x + 3 \geq 0
$$

> For å få tegnet $\geq$ i CAS, skriver vi `>` etterfulgt av `=`.


:::::{answer}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/c.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::
:::::::::::::


:::::::::::::{tab-item} d
$$
-2x - 16 \leq 0
$$

> For å få tegnet $\leq$ i CAS, skriver vi `<` etterfulgt av `=`.


:::::{answer}

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/d.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::
:::::::::::::

::::::::::::::


:::::::::::::::


### Numerisk løsning

Når vi løste likninger, kunne vi løse dem numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>. Det kan vi **ikke** gjøre med ulikheter. 
Ønsker vi å finne en numerisk løsning av en ulikhet, må vi i stedet
1. Løse ulikheten eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/>
2. Bruk <img src="/_static/icons/ggb/mode_numeric.svg" class="inline-image"/> til å finne en numerisk verdi for løsningen fra punkt 1.

I Utforsk 4 ser vi på hvordan.

:::::::::::::::{explore} Utforsk 4
I {numref}`fig-cas-kurs-del-1-ulikheter-numerisk-gif` nedenfor viser vi hvordan man kan finne en numerisk løsning av en ulikhet med CAS. Det gjøres med følgende fremgangsmåte:
1. Løs ulikheten eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/>
2. Bruk <img src="/_static/icons/ggb/mode_numeric.svg" class="inline-image"/> for å finne en numerisk verdi for løsningen fra punkt 1.


:::{figure} ./videoer/cas-ulikheter-numerisk.gif
---
width: 80%
class: no-click, adaptive-figure
name: fig-cas-kurs-del-1-ulikheter-numerisk-gif
---
viser hvordan man løser en ulikhet numerisk med CAS. Først løser vi den eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> og deretter bruker vi <img src="/_static/icons/ggb/mode_numeric.svg" class="inline-image"/> for å finne en numerisk verdi for løsningen.
:::


:::{cas-popup} 400 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs ulikheten i {numref}`fig-cas-kurs-del-1-ulikheter-numerisk-gif` eksakt og numerisk på tilsvarende måte i CAS-vinduet. 

:::::::::::::

:::::::::::::{tab-item} b
Løs ulikheten nedenfor eksakt og numerisk på tilsvarende måte i CAS-vinduet.

$$
3x + 2 < 0
$$


:::::::::::::

::::::::::::::


:::::::::::::::

---


:::::::::::::::{underveisoppgave} Underveisoppgave 4
Bruk CAS-vinduet til å bestemme en eksakt og numerisk løsning av ulikhetene nedenfor.

:::{cas-popup} 400 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

$$
-2x + 9 > 0 
$$

:::::::::::::


:::::::::::::{tab-item} b

$$
2x + 3 < 0 
$$

:::::::::::::


:::::::::::::{tab-item} c

$$
5x - 2 \geq 0 
$$

:::::::::::::


:::::::::::::{tab-item} d

$$
-3x + 19 \leq 0
$$

:::::::::::::

::::::::::::::




:::::::::::::::



## Likningssystemer
Likningssystemer kan vi løse både eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> og numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>. I Utforsk 5 ser vi på hvordan vi kan gjøre dette.



:::::::::::::::{explore} Utforsk 5

I figuren nedenfor vises det hvordan vi løser et likningssystem med CAS.
1. Først markerer vi likningene i likningssystemet.
2. Så løser vi likningssystemet eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> eller numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>.


:::{figure} ./videoer/cas-løs-likningssystemer.gif
---
class: no-click, adaptive-figure
width: 80%
---
viser hvordan vi først markerer likningene (*klikk-og-dra*) og deretter trykker på <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> eller <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/> for å løse likningssystemet.
:::


Bruk fremgangsmåten i figuren ovenfor til å løse likningssystemene nedenfor. Løs de både eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> og numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>.


:::{cas-popup} 400 500
:::

::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::{tab-item} a

\begin{align*}
    x + 2y &= 3 \\
    \\
    2x - 4y &= 8
\end{align*}

> Ja, det er samme likningssystem som i figuren ovenfor! 


::::::{answer}


:::{figure} ./figurer/utforsk/utforsk_5/a.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::{grid}
::::{grid-item-card}
---
columns: 6
---
Eksakt
^^^
$$
x = \dfrac{7}{2} \and y = -\dfrac{1}{4}
$$
::::

::::{grid-item-card}
---
columns: 6
---
Numerisk
^^^

$$
x \approx 3.5 \and y \approx -0.25
$$
::::

:::::

::::::

:::::::::


:::::::::{tab-item} b


\begin{align*}
    3x - y  &= 5 \\
    \\
    -2x + y &= 10
\end{align*}


:::::{answer}

:::{figure} ./figurer/utforsk/utforsk_5/b.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Siden løsningene er hele tall, så får vi det samme uansett om vi bruker eksakt eller numerisk løsning. Løsningen er

$$
x = 15 \and y = 40
$$

:::::

:::::::::
::::::::::

:::::::::::::::


---



:::::::::::::::{underveisoppgave} Underveisoppgave 5

Bruk CAS til å løse likningssystemene nedenfor. Løs de både eksakt med <img src="/_static/icons/ggb/mode_solve.svg" class="inline-image"/> og numerisk med <img src="/_static/icons/ggb/mode_nsolve.svg" class="inline-image"/>.

:::{cas-popup} 400 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

\begin{align*}
    2x + 3y &= 5 \\
    \\
    -x + 4y &= 8
\end{align*}

:::::::::::::


:::::::::::::{tab-item} b


\begin{align*}
    3x + 2y &= 7 \\
    \\
    -x - 3y = -\dfrac{7}{2}
\end{align*}

:::::::::::::


:::::::::::::{tab-item} c


\begin{align*}
    -x + 5 &= -y \\
    \\
    2x + 5y &= -11
\end{align*}

:::::::::::::


:::::::::::::{tab-item} d


\begin{align*}
    2x - y &= -2 \\
    \\
    x + 2y &= 8
\end{align*}

:::::::::::::

::::::::::::::
