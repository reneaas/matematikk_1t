# Optimering


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke den deriverte til å bestemme topp- og bunnpunkter til polynomfunksjoner.
* Kunne bruke den deriverte til å maksimere eller minimere polynomfunksjoner.
:::


**Optimering** handler om å bestemme den største eller minste verdien av noe, for eksempel det største arealet til en trekant.

I praksis handler optimering om å bestemme ekstremalpunktene til en funksjon $f$, der funksjonen $f$ er en modell for det vi ønsker å maksimere eller minimere.
:::::{admonition} Begreper: Maksimere og minimere
---
class: theory
---
Når en funksjon $f$ modellerer noe, har vi to tilfeller: 
* Hvis vi ønsker å gjøre noe **størst mulig**, sier vi at vi ønsker å **maksimere** $f$.
* Hvis vi ønsker å gjøre noe **minst mulig**, sier vi at vi ønsker å **minimere** $f$.
:::::


For å maksimere eller minimere en funksjon, finner vi ekstremalpunktene til $f$. Da får vi bruk for følgende setning:

:::{admonition} Begreper: Ekstremalpunkter og ekstremalverdier
---
class: sidenote, margin
---
Vi har tidligere jobbet med at **ekstremalpunkter** er en fellesbetegnelse for toppunkt eller bunnpunkt. I praksis er dette en *halv* sannhet fordi ekstremalpunkter beskriver **$x$-koordinaten** til disse punktene. Navnet på $y$-koordinaten til disse punktene kalles for **ekstremalverdier**.

:::

:::::{admonition} Setning: Ekstremalpunkter
---
class: summary
---
Ekstremalpunkter er $x$-koordinaten til et toppunkt eller bunnpunkt til en funksjon $f$.

Versjon 1:
: Ekstremalpunktene til $f$ svarer til nullpunktene til den deriverte $f'$. 

Versjon 2:
: Ekstremalpunktene til $f$ er gitt ved løsningen til $f'(x) = 0$. 
:::::

Setningen forteller oss at når vi ønsker å maksimere eller minimere en funksjon, kan vi gjøre dette ved å lete etter nullpunktene til den deriverte.


:::::::::::::::{admonition} Eksempel 1
---
class: example
---
En polynomfunksjon $f$ er gitt ved 

$$
f(x) = x^3 + 3x^2 - 9x + 1.
$$

Bestem toppunktet og bunnpunktet til funksjonen $f$.

:::::{admonition} Løsning
---
class: solution
---
For å bestemme toppunktet og bunnpunktet til $f$, løser vi likningen $f'(x) = 0$. Da trenger vi først den deriverte:

$$
f'(x) = (x^3 + 3x^2 - 9x + 1)' = 3x^2 + 6x - 9.
$$

Deretter løser vi likningen $f'(x) = 0$:

$$
3x^2 + 6x - 9 = 0 \liff x^2 + 2x - 3 = 0.
$$

Vi bruker $abc$-formelen for å finne røttene til andregradspolynomet:

$$
x = \dfrac{-2 \pm \sqrt{2^2 - 4\cdot (-3) \cdot 1}}{2\cdot 1} = \dfrac{-2 \pm \sqrt{16}}{2} = \dfrac{-2 \pm 4}{2} = \begin{cases} 1 \\ -3 \end{cases}
$$

Dermed har $f'(x)$ røttene $x = 1$ og $x = -3$. For å avgjøre hvilket punkt som gir et toppunkt og hvilket som gir et bunnpunkt kan vi bruke en fortegnslinje for $f'(x)$:

:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-polynomer-optimering-eksempel-1
width: 100%
class: no-click
---
viser fortegnsskjema til $f'(x)$. Vi kan lese av at $f'(x)$ er positiv rett før $x = -3$ og negativ rett etter, som betyr at grafen til $f$ stiger rett før punktet og synker rett etter. Det betyr at punktet er et toppunkt. Tilsvarende er $f'(x)$ negativ rett før $x = 1$ og positiv rett etter, som betyr at grafen til $f$ synker rett før punktet og stiger rett etter. Det betyr at punktet er et bunnpunkt.
:::

Fra fortegnsskjemaet kan vi altså konkludere at $x = -3$ gir et toppunkt og $x = 1$ gir et bunnpunkt. Koordinatene til de to punktene blir:


\begin{align*}
    f(-3) & = (-3)^3 + 3(-3)^2 - 9(-3) + 1 = -27 + 27 + 27 + 1 = 28 \\
    \\
    f(1) & = 1^3 + 3\cdot 1^2 - 9\cdot 1 + 1 = 1 + 3 - 9 + 1 = -4.
\end{align*}


så toppunktet er i $(-3, 28)$ og bunnpunktet er i $(1, -4)$.



:::::


:::::::::::::::


---

Vi tar et eksempel med en mer praktisk betydning:

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
Et rektangel har sidelengder $x$ og $y$. Til sammen er omkretsen av rektangelet $100$. 

Bestem sidelengdene slik at arealet av rektangelet er størst mulig.

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-polynomer-optimering-eksempel-2
width: 80%
class: no-click
---
viser et rektangel med sidelenger $x$ og $y$. Omkretsen av rektangelet er $100$.
:::


:::::{admonition} Løsning
---
class: solution
---
Vi ønsker å bestemme sidelengdene slik at arealet til rektangelet blir størst mulig. Vi må derfor finne en formel for arealet til rektangelet. 


Først kan vi merke oss at omkretsen av rektangelet er $100$ som betyr at 

$$
x + y + x + y = 100 \liff 2x + 2y = 100 \liff x + y = 50
$$

Videre er arealet av et rektangel sidelengdene ganget sammen som betyr at arealet $A$ er

$$
A = x\cdot y.
$$

Men her har vi to variabler, men vi vet også at 

$$
x + y = 50 \liff y = 50 - x. 
$$

Erstatter vi $y$ i formelen for arealet med denne likningen, får vi 

$$
A(x) = x\cdot(50 - x) = -x^2 + 50x. 
$$

Dette er en andregradsfunksjon. For å bestemme når arealet er størst mulig kan vi enten finne symmetrilinja, eller vi kan løse $A'(x) = 0$. Den sistnevnte metoden er mer generell, så vi velger denne her for å illustrere den generelle strategien:

$$
A'(x) = 0 \liff -2x + 50 = 0 \liff x = 25.
$$

Altså er arealet størst når 

$$
x = 25 \and y = 50 - 25 = 25.
$$

Altså blir arealet størst mulig dersom rektangelet er et *kvadrat*.

Merk at vi også kunne fått dette ved å bestemme symmetrilinja som vi gjør via nullpunktene $x = 0$ og $x = 50$ som gir symmetrilinja

$$
x = \dfrac{0 + 50}{2} = 25.
$$
:::::



:::::::::::::::


---

Vi tar med et annet "praktisk" eksempel der variabelen vi jobber med ikke lenger har merkelappen $x$. Strategien er fortsatt den samme, men det kan være litt uvant å
måtte forholde seg til en funksjon som ikke har $x$ som variabel, slik som i eksempelet under.

:::::::::::::::{admonition} Eksempel 3
---
class: example
---
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 9, \quad x \in [0, 3]. 
$$

Et rektangel har hjørnene $(0, 0)$, $(a, 0)$, $(a, f(a))$ og $(0, f(a))$.

Bestem $a$ slik at arealet av rektangelet blir størst mulig.

:::{figure} ./figurer/eksempler/eksempel_3.svg
---
name: fig-polynomer-optimering-eksempel-3
width: 80%
class: no-click
---
viser grafen til en andregradsfunksjon $f$.
::: 


:::::{admonition} Løsning
---
class: solution
---
Vi må starte med å finne en formel for arealet til rektangelet. 

Sidelengdene til rektangelet er $a$ og $f(a)$ som betyr at arealet er 

$$
A(a) = a\cdot f(a) = a\cdot(-a^2 + 9) = -a^3 + 9a.
$$

For å finne når arealet er størst mulig, må vi finne nullpunktene til $A'(a)$. Dette gir 

$$
A'(a) = -3a^2 + 9 = 0 \liff 3a^2 = 9 \liff a^2 = 3 \limplies a = \sqrt{3}. 
$$

Altså blir arealet av rektangelet størst mulig når $a = \sqrt{3}$. 

> Vi forkastet $a = -\sqrt{3}$ i løsningen over på grunn av avgrensingen $a \in [0, 3]$.

:::::

:::::::::::::::


