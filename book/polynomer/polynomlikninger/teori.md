# Polynomlikninger

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bestemme nullpunktene til et tredjegradspolynom.
* Kunne løse tredjegradslikninger.
:::

Først må vi utvide begrepsapparatet vårt litt: 

::::{admonition} Definisjon: Røtter
---
class: summary
---
Et nullpunkt til en polynomfunksjon kalles for en **rot** til polynomet. Samlingen av alle nullpunktene til et polynom kalles for **røttene** til polynomet.
::::

## Nullpunktene til et tredjegradspolynom

For å bestemme nullpunktene, eller røttene, til et tredjegradspolynom, får vi bruk for følgende fremgangmåte:
1. Liste opp alle mulige heltallsrøtter, og bestemme én rot $r$.
2. Utføre polynomdivisjon med $(x - r)$ for å få et andregradspolynom. 
3. Bestemme røttene til andregradspolynomet med $abc$-formelen eller faktorisering.


## Tredjegradslikninger

:::::::::::::::{admonition} Setning: Heltallsrøtter for polynomer
---
class: summary
---
Et tredjegradspolynom 

$$
f(x) = ax^3 + bx^2 + cx + d,
$$

der koeffisientene er **hele tall**, vil alle heltallsrøttene til $f(x)$ være en faktor i konstantleddet $d$. 
:::::::::::::::

Setningen over lar oss systematisk finne alle *mulige* heltallsrøtter for et tredjegradspolynom. Polynomet må ikke ha heltallsrøtter, men hvis det har det, 
kan vi garantere at det må være i listen over alle tall som *kan* være en faktor i konstantleddet $d$.


:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Et tredjegradspolynom $f$ er gitt ved 

$$
f(x) = x^3 + 2x^2 - 4x - 8.
$$

Bestem nullpunktene til $f$. 

::::::::::::::{admonition} Løsning
---
class: solution
---
Vi starter med å observere at $d = -8$, så *hvis* $f$ har heltallsrøtter, så vil de være en faktor i $(-8)$. Dette gir mulighetene:

$$
x = \pm 1, \pm 2, \pm 4, \pm 8
$$

fordi $(-8)$ er delelig med alle disse tallene. 



Vi prøver ut noen av verdiene i lista. Vi kan enten 
1. Regne ut funksjonsverdier og utføre polynomdivisjon når vi finner en rot.
2. Bruke et Horner-skjema til å regne ut funksjonsverdier og utføre polynomdivisjon samtidig.

````{tab} Vanlig polynomdivisjon
Vi starter med å lete etter en rot ved å regne ut $f(x)$:

\begin{align*}
    f(1) &= 1^3 + 2\cdot 1^2 - 4\cdot 1 - 8 = -9, \\
    \\
    f(-1) &= (-1)^3 + 2\cdot (-1)^2 - 4\cdot (-1) - 8 = -3, \\
    \\
    f(2) &= 2^3 + 2\cdot 2^2 - 4\cdot 2 - 8 = 0.
\end{align*}

Så vi finner at $f(2) = 0$, som betyr at $(x - 2)$ er en faktor i $f(x)$. Dermed har vi

:::{figure} ./koder/eksempler/eksempel_1/eksempel_1_polydiv.svg
---
width: 90%
class: no-click, adaptive-figure
---
:::

````


````{tab} Horner-skjema

Bruker vi et Horner-skjema, får vi utført polynomdivisjon samtidig som vi regner ut funksjonsverdiene: 

:::{figure} ./koder/eksempler/eksempel_1/eksempel_1_syntetisk_1.svg
---
width: 50%
class: no-click, adaptive-figure
---
Horner-skjema for $x = 1$. Her finner vi at $f(1) = -9$. 
:::

Vi prøver videre.

:::{figure} ./koder/eksempler/eksempel_1/eksempel_1_syntetisk_-1.svg
---
width: 50%
class: no-click, adaptive-figure
---
Horner-skjema for $x = -1$. Her finner vi at $f(-1) = -3$.
:::

Vi prøver neste verdi:


:::{figure} ./koder/eksempler/eksempel_1/eksempel_1_syntetisk_2.svg
---
width: 50%
class: no-click, adaptive-figure
---
Horner-skjema for $x = 2$. Her finner vi at $f(2) = 0$. 
:::



Dermed vet vi at $x = 2$ er en rot for $f$. Vi kan også lese av koeffisientene til kvotienten i polynomdivisjon som

$$
f(x) : (x - 2) = x^2 + 4x + 4.
$$

````


Vi kan derfor skrive $f(x)$ som

$$
f(x) = x^3 + 2x^2 - 4x - 8 = (x - 2)(x^2 + 4x + 4).
$$

Videre kan vi faktorisere andregradspolynomet med 1.kvadratsetning:

$$
(x^2 + 4x + 4) = (x + 2)^2,
$$

som betyr at 

$$
f(x) = (x - 2)(x + 2)^2.
$$

Altså er røttene til $f$

$$
x = -2 \quad \lor \quad x = 2.
$$

Vi kan også observere her at **begge** røttene var i listen over *mulige kandidater* for heltallsrøtter! 
::::::::::::::
:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Et tredjegradspolynom $f$ er gitt ved

$$
f(x) = x^3 + 6x^2 + 3x - 10.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Skriv ned alle mulige heltallsrøtter for $f$.

Bestem en av røttene til $f$ ved å prøve ut verdier fra lista.

::::::::::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = \pm 1, \pm 2, \pm 5, \pm 10
$$
::::::::::::
:::::::::::::

:::::::::::::{tab-item} b
Bestem alle røttene til $f$. 

::::::::::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = -5 \quad \lor \quad x = -2 \quad \lor \quad x = 1
$$
::::::::::::
:::::::::::::

::::::::::::::

:::::::::::::::


---

Vi kan utvide setningen vår til å fungere mer generelt for alle rasjonale røtter:

:::{margin} Merk!
Selv om vi bruker tredjegradsfunksjoner som et eksempel her, så gjelder setningene vi ser på for **alle** polynomfunksjoner! Så bruk samme strategi uansett hvilken grad polynomet har!
:::

:::::::::::::::{summary} Setning: Rasjonale røtter for polynomer
For et tredjegradspolynom på formen

$$
f(x) = ax^3 + bx^2 + cx + d
$$

så vil alle rasjonale røtter være på formen $x = \dfrac{p}{q}$ der $p$ er en faktor i konstantleddet $d$ og $q$ er en faktor i den ledende koeffisienten $a$.

:::::::::::::::

La oss se på et eksempel der vi bruker setningen ovenfor til å lage en liste over alle mulige rasjonale røtter før vi leter etter røttene.


:::::::::::::::{example} Eksempel 2
En tredjegradsfunksjon er gitt ved 

$$
f(x) = 6x^3 - 7x^2 - 8x + 5.
$$

Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.


::::{solution}
---
dropdown: 0
---
Først lister vi opp alle mulige faktorer $p$ i konstantleddet $d = 5$. Dette vil være

$$
p \in \{\pm 1, \pm 5\}
$$

Deretter lister vi opp alle mulige faktorer $q$ i den ledende koeffisienten $a = 6$. Dette vil være

$$
q \in \{\pm 1, \pm 2, \pm 3, \pm 6\}
$$

Alle mulige rasjonale løsninger $x$ vil da være på formen $x = \dfrac{p}{q}$, som gir oss mulighetene

$$
x \in \left\{\pm 1, \pm 5, \pm \frac{1}{2}, \pm \frac{5}{2}, \pm \frac{1}{3}, \pm \frac{5}{3}, \pm \frac{1}{6}, \pm \frac{5}{6}\right\}
$$


Vi bruker et Horner-skjema for å finne én rot:

:::{horner}
---
p: 6x^3 - 7x^2 - 8x + 5
x: -1
width: 60%
---
:::

Det betyr at 

$$
6x^3 - 7x^2 - 8x + 5 = (x + 1)(6x^2 - 13x + 5).
$$

Vi bruker så $abc$-formelen til å finne de resterende løsningene:

$$
x = \dfrac{13 \pm \sqrt{(-13)^2 - 4 \cdot 6 \cdot 5}}{2 \cdot 6} = \dfrac{13 \pm \sqrt{49}}{12} = \dfrac{13 \pm 7}{12}
$$

som gir

$$
x = \dfrac{5}{3} \quad \lor \quad x = \dfrac{1}{2}
$$

Dermed skjærer grafen til $f$ gjennom $x$-aksen når

$$
x = -1 \quad \lor \quad x = \dfrac{1}{2} \quad \lor \quad x = \dfrac{5}{3}
$$

Vi kan spesielt merke oss at **alle** røttene var i lista over *mulige kandidater* for rasjonale røtter!


::::

:::::::::::::::

