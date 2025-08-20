# Standardform

:::{admonition} Læringsmål
---
class: tip
---
* Kunne representere en lineær funksjon på standardform og beskrive sammenhengen med den grafiske representasjonen.
* Kunne bytte fra en representasjon til en annen.
:::

En lineær funksjon er en rett linje som du kanskje har lært å beskrive med en likning

$$
y = ax + b 
$$


der vi setter inn en verdi for $x$ for å finne den **tilhørende** verdien for $y$. Gjør vi dette med mange ulike verdier for $x$, får vi en samling punkter $(x, y)$ – dette kaller vi for **grafen** til den lineære funksjonen. Vi gir gjerne funksjonen et navn, for eksempel $f$, og skriver funksjonsuttrykket som

$$
f(x) = ax + b
$$

som betyr at $y = f(x)$. Vi kaller $f(x)$ for **funksjonsverdien** når vi tenker på et bestemt tall $x$, og **funksjonsuttrykket** når vi ikke tenker på noe spesielt tall for $x$.


:::::::::::::::{admonition} Påminnelse: Koordinatsystemet
---
class: dropdown, summary
---

Koordinatsystemet består av to tallinjer som vi kaller for **akser**. De to aksene er:
* $x$-aksen (den horisontale aksen - også kalt *førsteaksen*).
* $y$-aksen (den vertikale aksen - også kalt *andreaksen*).

Punktet der aksene møtes kaller vi for **origo**. Origo har koordinatene $(0, 0)$.

For å finne et punkt $(x, y)$ i koordinatsystemet, går vi $x$ plasser parallelt med $x$-aksen og $y$ plasser parallelt med $y$-aksen. Da står vi på punktet $(x, y)$. 
Vi kaller $x$-verdien til punktet for $x$-koordinaten og $y$-verdien for $y$-koordinaten.

I figuren nedenfor vises en konkret eksempel med punktet $(3, 2)$.

:::{figure} ./figurer/teori/koordinatssystem.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser et koordinatsystem med punktet $(3, 2)$. For å finne punktet går vi $3$ plasser parallelt med $x$-aksen og $2$ plasser parallelt med $y$-aksen. 
:::

:::::::::::::::


La oss se på et eksempel:


:::::::::::::::{example} Eksempel 1
I figuren nedenfor vises grafen til en lineær funksjon $f$ gitt ved 

$$
f(x) = 2x + 1.
$$


:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


I figuren har vi markert et punkt $(2, f(2))$ på grafen til $f$. Vi ser at $x$-koordinaten til dette punktet er $2$ og $y$-koordinaten er $5$. Det betyr at 

$$
f(2) = 5
$$

Vi kunne også sett dette ved å regne ut verdien med funksjonsuttrykket til $f$:

$$
f(\textcolor{red}{2}) = 2 \cdot \textcolor{red}{2} + 1 = 4 + 1 = 5. 
$$


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 3x - 2
$$

Bestem $f(4)$ ved
1. Å regne ut med funksjonsuttrykket
2. Ved å lese av fra grafen til $f$ vist i figuren nedenfor.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::{answer}
$$
f(4) = 10
$$
::::

::::{solution}
Ved regning:
: $f(\textcolor{red}{4}) = 3 \cdot \textcolor{red}{4} - 2 = 12 - 2 = 10$

Grafisk
: Vi ser at når $x = 4$, så er $y = 10$ på grafen. Det betyr at $f(4) = 10$. 
::::




:::::::::::::::


## Standardform: Algebraisk og grafisk representasjon


En **representasjon** er en måte å beskrive noe på. En lineær funksjon kan representeres på flere måter, for eksempel med en formel som vi gjerne kaller for en **algebraisk representasjon**. En lineær funksjon kan også representeres grafisk med en **graf**. Det finnes flere representasjoner, men disse er de to viktigste. 

En algebraisk representasjon kan gi oss umiddelbar informasjon om grafen til en funksjon. Å velge en representation som er hensiktmessig for å løse en oppgave er en viktig ferdighet i matematikk. Den første vi skal se på kaller vi for **standardform**. 


:::::::::::::::{summary} Standardform: Algebraisk representasjon

En lineær funksjon $f$ kan skrives på **standardform** som

:::{figure} ./figurer/teori/algebraisk/standardform.svg
---
width: 70%
class: no-click, adaptive-figure
:::

* Verdien til $a$ er hvor mye $f(x)$ endrer seg når vi øker $x$ med $1$. Vi kaller $a$ for **stigningstallet** til grafen til $f$.
* Verdien til $b$ er $y$-koordinaten til skjæringspunktet mellom grafen til $f$ og $y$-aksen. Vi kaller ofte $b$ for **konstantleddet** til $f(x)$.


:::{figure} ./figurer/teori/grafisk_representasjon/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::::

---


:::::::::::::::{example} Eksempel 2
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor. 

Bestem $f(x)$.


:::{figure} ./figurer/eksempler/eksempel_2/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::{solution}
---
dropdown: 0
---
En lineær funksjon på standardform er gitt ved

$$
f(x) = ax + b
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, 1)$ som betyr at $b = 1$. 

Hvis vi velger ut et punkt på grafen til $f$, for eksempel $(0, 1)$, så ser vi at når vi øker $x$ med $1$, så synker funksjonsverdien $f(x)$ med $-2$ (husk $y = f(x)$) som betyr at stigningstallet er $a = -2$. 

Da er $f(x)$ gitt ved

$$
f(x) = ax + b = -2 \cdot x + 1 = -2x + 1
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2 
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::

::::{answer}
$$
f(x) = 3x - 4
$$
::::

::::{solution}
En lineær funksjon på standardform er gitt ved 

$$
f(x) = ax + b
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -4)$ som betyr at $b = -4$. 

Hvis vi velger et punkt på grafen til $f$, for eksempel $(0, -4)$ og øker $x$ med $1$, så er vi at $f(x)$ øker med $3$ siden grafen går gjennom punktet $(1, -1)$. Det betyr at stigningstallet er $a = 3$. 

Da er 

$$
f(x) = 3 \cdot x - 4 = 3x - 4
$$
::::


:::::::::::::::



---


La oss se på et eksempel der vi går fra funksjonsuttrykk til graf. 

:::::::::::::::{example} Eksempel 3
En lineær funksjon $f$ er gitt ved 

$$
f(x) = -x + 2
$$

Lag en skisse av grafen til $f$. 


::::{solution}
---
dropdown: 0
---
Fra funksjonsuttrykket

$$
f(x) = -x + 2 = (-1) \cdot x + 2
$$

ser vi at stigningstallet til $f$ er $a = -1$ og konstantleddet er $b = 2$. Det betyr at grafen til $f$ skjærer $y$-aksen i $(0, 2)$. Da kan vi lage følgende skisse av grafen til $f$:

:::{figure} ./figurer/eksempler/eksempel_3/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
viser en skisse av grafen til $f$ der den skjærer $y$-aksen i $(0, 2)$ og har stigningstall $-1$. 
:::


::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
En lineær funksjon $f$ er gitt ved

$$
f(x) = -2x + 3
$$

Lag en skisse av grafen til $f$ der du markerer skjæringspunktet med $y$-aksen og stigningstallet.


::::{answer}
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::
::::

::::{solution}
Vi har at 

$$
f(x) = (-2) \cdot x + 3
$$

som betyr at stigningstallet er $a = -2$ og konstantleddet er $b = 3$. Grafen til $f$ skjærer derfor $y$-aksen i $(0, 3)$. 

Ut ifra denne informasjonen kan vi tegne følgende skisse av grafen til $f$.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::
::::


:::::::::::::::



## Topunktsformelen

Vi vet allerede nå at vi kan bestemme stigningstallet $a$ til en lineær funksjon ved å sjekke hvor mye $f(x)$ endrer seg når vi øker $x$ med $1$. Men vi vet ikke alltid funksjonsverdier til $f$ i $x$-verdier som ligger en avstand $1$ fra hverandre. Da trenger vi en annen metode for å bestemme stigningstallet. 


:::::::::::::::{summary} Topunktsformelen
Hvis grafen til en lineær funksjon $f$ går gjennom punktene $(x_1, y_1)$ og $(x_2, y_2)$, så er stigningstallet $a$ gitt ved 

$$
a = \dfrac{\Delta y}{\Delta x} = \dfrac{y_2 - y_1}{x_2 - x_1}
$$


der vi har definert

$$
\Delta y = y_2 - y_1 \qog \Delta x = x_2 - x_1
$$

Vi leser symbolet $\Delta$ som "endring i" slik at $\Delta y$ betyr "endring i $y$-verdien" og $\Delta x$ betyr "endring i $x$-verdien". Stigningstallet er altså endringen i $y$-verdien delt på endringen i $x$-verdien.

:::{figure} ./figurer/teori/topunktsformelen/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::



:::::::::::::::

---


:::::::::::::::{example} Eksempel 4
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor.

Bestem $f(x)$.

:::{figure} ./figurer/eksempler/eksempel_4/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::

::::{solution}
---
dropdown: 0
---
En lineær funksjon på standardform er gitt ved

$$
f(x) = ax + b.
$$

Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, -5)$ som betyr at $b = -5$. 

Vi ser at grafen til $f$ også går gjennom punktet $(2, 1)$. Vi kan bruke topunktsformelen til å bestemme stigningstallet:

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{1 - (-5)}{2 - 0} = \dfrac{6}{2} = 3
$$

Dermed er 

$$
f(x) = 3x - 5
$$
::::

:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 4
Grafen til en lineær funksjon $f$ er vist i figuren nedenfor. 

Bestem $f(x)$.


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_4/figur.svg
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::{answer}
$$
f(x) = -2x + 4
$$
::::

::::{solution}
Vi ser at grafen til $f$ skjærer $y$-aksen i $(0, 4)$ som betyr at $b = 4$. 

Vi ser grafen også går gjennom punktet $(3, -2)$. Vi bestemmer stigningstallet med topunktsformelen:

$$
a = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{-2 - 4}{3 - 0} = \dfrac{-6}{3} = -2
$$

Dermed er 

$$
f(x) = -2x + 4
$$
::::


:::::::::::::::










