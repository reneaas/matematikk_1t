# Optimering


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke den deriverte til å bestemme topp- og bunnpunkter til polynomfunksjoner.
* Kunne bruke den deriverte til å finne maksimere eller minimere polynomfunksjoner.
:::


**Optimering** handler om å bestemme den største eller minste verdien av noe. Eksempler på dette kan være å bestemme det største mulige arealet av en trekant, det største overskuddet til en butikk, eller hvilken rute man bør ta for å bruke kortest mulig tid mellom to steder. 

I praksis handler optimering om å bestemme ekstremalpunktene til en funksjon $f$, der funksjonen $f$ modellerer det vi ønsker å gjøre størst eller minst mulig. 

:::::{admonition} Begreper: Maksimere og minimere
---
class: theory
---
Når en funksjon $f$ modellerer noe, har vi to tilfeller: 
* Hvis vi ønsker å gjøre noe **størst mulig**, sier vi at vi ønsker å **maksimere** $f$.
* Hvis vi ønsker å gjøre noe **minst mulig**, sier vi at vi ønsker å **minimere** $f$.
:::::


For å maksimere eller minimere en funksjon, finner vi ekstremalpunktene til $f$. Da får vi bruk for følgende setning:

:::::{admonition} Setning: Ekstremalpunkter
---
class: summary
---
Ekstremalpunktene til $f$ er punkter der hvor $f'(x) = 0$. 
:::::

Setningen forteller oss at når vi ønsker å maksimere eller minimere en funksjon, kan vi gjøre dette ved å lete etter nullpunktene til den deriverte.



:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Et rektangel har sidelengder $x$ og $y$. Til sammen er omkretsen av rektangelet $100$. 

Bestem sidelengdene slik at arealet av rektangelet er størst mulig.

:::{figure} ./figurer/eksempler/eksempel_1.svg
---
name: fig-polynomer-optimering-eksempel-1
width: 80%
class: no-click
---
viser et rektangel med sidelenger $x$ og $y$. 
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


Vi tar et eksempel til som er litt mer teoretisk: 

:::::::::::::::{admonition} Eksempel 2
---
class: example
---
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 9, \quad x \in [0, 3]. 
$$

Et rektangel har hjørnene $(0, 0)$, $(a, 0)$, $(a, f(a))$ og $(0, f(a))$.

Bestem $a$ slik at arealet av rektangelet blir størst mulig.

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
name: fig-polynomer-optimering-eksempel-2
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

:::::

:::::::::::::::


