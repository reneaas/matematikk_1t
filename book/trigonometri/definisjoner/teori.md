# $\sin v$, $\cos v$ og $\tan v$ 

:::::{admonition} Læringsmål 
---
class: tip
---
* Kunne bestemme $\sin v$, $\cos v$ og $\tan v$ for en vinkel $v$ i en rettvinklet trekant.
* Kunne finne ukjente sidelenger eller vinkler i en rettvinklet trekant ved hjelp av sinus, cosinus og tangens.
* Kunne regne ut sinus, cosinus og tangens for bestemte vinkler med CAS.
* Kunne bestemme ukjente vinkler med CAS. 
:::::

**Trigonometri** er en del av geometrien som handler om trekanter. Her skal vi se på tre trigonometriske størrelser som er sentrale i trigonometri: **sinus**, **cosinus** og **tangens**. Disse størrelsene er forholdstall som er avhengig av en bestemt vinkel $v$ i en rettvinklet trekant.

## Motstående og hosliggende kateter

Når vi jobber med rettvinklede trekanter, kommer vi til å få bruk for å kategorisere sidene i trekanten. 

:::::::::::::::{admonition} Motstående og hosliggende kateter
---
class: summary
---

I en rettvinklet trekant, vil katetene i trekanten ha to navn:
* Den **motstående** kateten er kateten som står på motsatt side av vinkelen.
* Den **hosliggende** kateten er kateten som spenner ut vinkelen.

Om en katet er motstående eller hosliggende er altså avhengig av hvilken vinkel vi ser på.

:::{figure} ./figurer/teori/merged_figure.svg
---
width: 100%
class: no-click
---
:::


:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

Bestem hvilke sidelengder som er motstående katet og hosliggende katet til vinkel $A$ i trekanten nedenfor.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/a.svg
---
width: 60%
class: no-click
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
* Hosliggende katet er $AB = 3$. 
* Motstående katet er $BC = 4$.
::::
:::::::::::::

:::::::::::::{tab-item} b
Bestem hvilke sidelenger som er motstående katet og hosliggende katet for vinkel $C$ i trekanten nedenfor. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/b.svg
---
width: 60%
class: no-click
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
* Motstående katet er $AB = 3$. 
* Hosliggende katet er $BC = 4$.
::::

:::::::::::::

::::::::::::::


:::::::::::::::


## $\sin v$ og $\cos v$

Vi skal nå se på de to mest grunnleggende trigonometriske størrelsene. Den ene er **sinus** til en vinkel $v$ og skrives som $\sin v$. Den andre er **cosinus** til en vinkel $v$ og skrives som $\cos v$. 


:::::::::::::::{admonition} Definisjon: Sinus og Cosinus
---
class: summary
---
Sinus og cosinus til en vinkel $v$ i en rettvinklet trekant er definert som **forholdstallene**:

$$
\sin v = \frac{\text{motstående katet}}{\text{hypotenus}} \quad \quad \quad \cos v = \frac{\text{hosliggende katet}}{\text{hypotenus}}
$$

:::{figure} ./figurer/teori/trekant3.svg
---
width: 60%
class: no-click
---
:::

Vi skriver ofte bare $\sin A$ og $\cos A$ hvis vi vi jobber med vinkelen i hjørnet $A$.

:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
En trekant er vist nedenfor. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/trekant.svg
---
width: 60%
class: no-click
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\sin A$.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\sin A = \dfrac{4}{5}
$$
:::
:::::::::::::


:::::::::::::{tab-item} b
Bestem $\cos A$.


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\cos A = \dfrac{3}{5}
$$
:::
:::::::::::::


:::::::::::::{tab-item} c
Bestem $\sin C$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\sin C = \dfrac{3}{5}
$$
:::
:::::::::::::


:::::::::::::{tab-item} d
Bestem $\cos C$.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
\cos C = \dfrac{4}{5}
$$
:::
:::::::::::::


::::::::::::::


:::::::::::::::



## $\sin v$ og $\cos v$ som funksjoner

Sinus og cosinus er forholdstall som er avhengig av en bestem vinkel $v$. Vi kan derfor tenke på $\sin v$ og $\cos v$ som funksjoner av vinkelen $v$. Dette er sjeldent vi klarer å bestemme verdien til sinus og cosinus uten å bruke en kalkulator. Vi må derfor vite hvordan vi kan regne ut disse størrelsene i praksis.

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
I figuren nedenfor vises en rettvinklet trekant. 

:::{figure} ./figurer/utforsk/utforsk_1/trekant.svg
---
width: 60%
class: no-click
---
:::

I trekanten er 

$$
\sin A = \frac{4}{5} \quad \quad \quad \cos A = \frac{3}{5}
$$

Nedenfor vises hvordan vi kan bestemme vinkel $A$ i trekanten ved hjelp av CAS. Her må vi
1. Lage en likning der vi skriver $\sin(A^\circ) = \dfrac{4}{5}$.
2. Løs likningen for $A$ med `Nløs`-kommandoen.

:::{raw} html
---
file: ./ggb/utforsk/utforsk_1/eksempel.html
---
:::

Altså er vinkel $A \approx 53.13^\circ$. Vi kan se at vi også får noen løsninger som ikke ligger mellom $0$ og $90$ grader. Vi kommer til å se nærmere på hva dette betyr senere. 

> For å skrive $\sin (A^\circ)$ i CAS, må vi trykke på "alt" og "o" på Windows, og "option" og "o" på Mac.

:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 3
---
class: check 
---
Trekanten fra Utforsk 1 er vist nedenfor. 

:::{figure} ./figurer/utforsk/utforsk_1/trekant.svg
---
width: 60%
class: no-click
---
:::

Bruk CAS-vindu nedenfor til å bestemme vinkel $C$. 

:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_3/cas_vindu.html
---
:::


::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_3/fasit.png
---
width: 100%
class: no-click
---
:::

Fra utskriften kan lese av at vinkelen $A$ er

$$
C \approx 36.87^\circ
$$

siden dette er den eneste løsningen av likningen som ligger mellom $0$ og $90$ grader.
::::




:::::::::::::::

---

Vi kan også regne ut sinus og cosinus til bestemte vinkler ved hjelp av CAS. 



:::::::::::::::{admonition} Utforsk 2
---
class: explore
---
Nedenfor vises en et CAS-vindu som regner ut sinus og cosinus til vinkelen $30^\circ$.


:::{raw} html
---
file: ./ggb/utforsk/utforsk_2/eksempel.html
---
:::

Fra utskriften i CAS-vinduet, kan vi se at 

$$
\sin 30^\circ = \frac{1}{2} \quad \quad \quad \cos 30^\circ = \frac{\sqrt{3}}{2}
$$

I oppgavene skal du komme fram til disse svarene **uten** å bruke CAS.

:::::::::::::::


---


:::::::::::::::{admonition} Underveisoppgave 4
---
class: check
---
Bruk CAS-vinduet nedenfor til å regne ut 

1. $\sin 60^\circ$
2. $\cos 60^\circ$

:::{raw} html
---
file: ./ggb/underveisoppgaver/underveisoppgave_4/cas_vindu.html
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
:::{figure} ./ggb/underveisoppgaver/underveisoppgave_4/fasit.png
---
width: 100%
class: no-click
---
:::

Altså er 

$$
\sin 60^\circ = \frac{\sqrt{3}}{2} \quad \quad \quad \cos 60^\circ = \frac{1}{2}
$$
::::

:::::::::::::::

---

## $\tan v$

Den tredje trigonometriske størrelsen vi skal se på er **tangens** til en vinkel $v$ og skrives som $\tan v$.

:::::::::::::::{admonition} Definisjon: Tangens
---
class: summary
---
Tangens til en vinkel $u$ i en rettvinklet trekant er definert som forholdstallet:

$$
\tan v = \frac{\text{motstående katet}}{\text{hosliggende katet}}
$$

som også er det samme som 

$$
\tan v = \frac{\sin v}{\cos v}
$$

:::{figure} ./figurer/teori/trekant3.svg
---
width: 60%
class: no-click
---
:::

:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 5
---
class: check
---
Bestem $\tan A$ og $\tan C$ for trekanten nedenfor.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_5/trekant.svg
---
width: 60%
class: no-click
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
\tan A = \dfrac{4}{3} \quad \quad \quad \tan C = \dfrac{3}{4}
$$
::::

:::::::::::::::

<!-- ## Bestemme ukjente sidelenger og vinkler

Vi kan bruke sinus, cosinus og tangens til å bestemme ukjente sidelenger og vinkler i en rettvinklet trekant.

:::::::::::::::{admonition} Eksempel 1
---
class: example
---


::::::::::::::: -->











