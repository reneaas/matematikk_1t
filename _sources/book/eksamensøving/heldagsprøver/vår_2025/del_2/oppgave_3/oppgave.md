:::::::::::::::{admonition} Oppgave 3
---
class: check
---
Nedenfor vises grafen til en andregradsfunksjon $f$ og to tangenter som skjærer gjennom nullpunktene til $f$.
* Den ene tangenten har stigningstall $4$.
* Tangentene skjærer hverandre i $(-1, -8)$. 

:::{figure} ./figurer/del_2/oppgave_3/figur.svg
---
width: 80%
class: no-click
---
:::


:::::{admonition} Retteveiledning
---
class: summary, dropdown
---
* Inntil 1 poeng for å sette opp et gyldig likningssystem for koeffisientene til $f(x)$ eller $f'(x)$.
* 1 poeng for å bestemme $f(x)$ med en gyldig fremgangsmåte.
* 1 poeng for å bestemme $f'(x)$ med en gyldig fremgangsmåte.

Andre gyldige fremgangsmåter som leder fram til $f(x)$ og $f'(x)$ vil også gi full uttelling.
:::::


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = x^2 + 2x - 3 \limplies f'(x) = 2x + 2.
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan sette opp et likningssystem ut ifra opplysningene i oppgaven. Vi trenger tre likninger der minst én av de ikke er en nullpunktslikning. 

Begge tangenter går ggjennom punkten $(-1, -8)$. Den ene har stigningstall $4$. Fra ettpunktsformelen får vi dermed skrive ned likningen til denne tangenten som:

$$
y - (-8) = 4(x - (-1)) \liff y = 4x - 4 = 4(x - 1)
$$

Her kan vi konkludere at tangenten skjærer $x$-aksen i

$$
y = 0 \liff 4(x - 1) = 0 \liff x = 1
$$

Det betyr at vi fra denne tangenten kan sette opp likningene

\begin{align*}
    f(1) &= 0 && \text{Nullpunkt i $x = 1$} \\
    f'(1) &= 4 && \text{Stigningstallet til tangenten i $x = 1$} \\
\end{align*}

Den andre tangenten går gjennom det andre nullpunktet til $f$. På grunn av symmetrien til en andregradsfunksjon, betyr det at $x$-koordinaten til skjæringspunktet mellom de to tangentene svarer til symmetrilinja til $f$. Dermed vil en tangent i punktet ha stigningstall $0$ slik at den siste likningen vi trenger er

\begin{align*}
    f'(-1) &= 0 && \text{Stigningstallet til tangenten i $x = -1$. Bunnpunkt} \\
\end{align*}

En andregradsfunksjon $f$ er generelt sett gitt ved 

$$
f(x) = ax^2 + bx + c.
$$

Vi løser likningssystemet med CAS for å bestemme koeffisientene til $f(x)$:

:::{figure} ./figurer/del_2/oppgave_3/sol.png
---
width: 100%
class: no-click
---
:::

som betyr at 

$$
f(x) = x^2 + 2x - 3. 
$$

Deriverer vi uttrykket, får vi:

$$
f'(x) = (x^2 + 2x - 3)' = 2x + 2.
$$



> Andre likninger vi kunne hentet ut fra opplysningene i oppgaven er: 
> 1) $f(-3) = 0$
> 2) $f'(-3) = -4$

:::::

:::::::::::::::

