# Funksjoner (Del 2)

> Her kan du bruke digitale hjelpemidler som **CAS**, **graftegner** (Geogebra), **Python** og **regneark** til å løse oppgaver. 


::::::::::::::::{admonition} Oppgave 1 (Vår 2024)
---
class: exercise
---

:::{figure} ./figurer/oppgave_1/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Den rette linjen som er tegnet i koordinatsystemet ovenfor, er den deriverte av en funksjon $f$.

Punktet $P(1, 2)$ ligger på grafen til $f$.

Bestem likningen for tangenten til grafen til $f$ i punktet $P$. <br>
Husk å argumentere for at svaret ditt er riktig.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
y = -2x + 4.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Siden $P(1, 2) \in f$, så er $f(1) = 2$. Siden $x$-koordinaten er $x = 1$, betyr det stigningstallet til tangenten er $a = f'(1)$. Fra grafen til $f'$ ovenfor, kan vi se at grafen går gjennom punktet $(1, -2)$ som betyr at $f'(1) = -2$. <br> 
Bruker vi ettpunktsformelen, blir derfor likningen for tangenten til $f$ i punktet $P$ gitt ved 

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - 2 &= -2(x - 1) \\
    \\
    y - 2 &= -2x + 2 \\
    \\
    y &= -2x + 4
\end{align*}
:::::

::::::::::::::::

---


::::::::::::::::{admonition} Oppgave 2 (Høst 2024)
---
class: exercise
---
En rasjonal funksjon $f$ har asymptotene $x = 2$ og $y = 4$. <br>
Nullpunktet til funksjonen er $x = -3$.

Bestem et mulig funksjonsuttrykk $f(x)$. <br>
Gjør rede for hvordan du har tenkt for å komme fram til funksjonsuttrykket. 


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = \dfrac{4(x + 3)}{x - 2}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Ut ifra opplysningene kan vi skrive om en rasjonal funksjon på formen

$$
f(x) = \dfrac{a(x - b)}{x - c}
$$

der 

* $y = a$ er $f$ sin horisontale asymptote
* $x = c$ er $f$ sin vertikale asymptote
* $x = -b$ er $f$ sitt nullpunkt

Fra opplysningene har vi at 

* $a = 4$ fordi $y = 4$ er den horisontale asymptoten
* $b = -3$ fordi $x = -3$ er nullpunktet
* $c = 2$ fordi $x = 2$ er den vertikale asymptoten

Dermed er et mulig funksjonsuttrykk $f(x)$ gitt ved 

$$
f(x) = \dfrac{4(x + 3)}{x - 2}
$$
:::::

::::::::::::::::


---

::::::::::::::::{admonition} Oppgave 3 (Høst 2024)
---
class: exercise
---
Du får vite følgende om en tredjegradsfunksjon $f$ gitt ved

$$
f(x) = ax^3 + bx^2 + cx + d.
$$

* Grafen til $f$ går gjennom punktet $(2, 6)$. 
* Punktet $(-2, 8)$ er et toppunkt på grafen til $f$.
* Tangenten til grafen til $f$ i punktet $(3, f(3))$ har stigningstall $4$.


Bruk opplysningene ovenfor til å bestemme $a$, $b$, $c$ og $d$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = \dfrac{3}{20} \and b = \dfrac{7}{40} \and c = -\dfrac{11}{10} \and d = \dfrac{63}{10}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra opplysningene kan vi sette opp et likningssystem med fire likninger og fire ukjente. 

1) **Grafen til $f$ går gjennom punktet $(2, 6)$** <br>
Fra dette kan vi sette opp likningen

$$
f(2) = 6
$$

2) **Punktet $(-2, 8)$ er et toppunkt på grafen til $f$** <br>
Fra dette kan vi sette opp to likninger:

\begin{align*}
    f(-2) &= 8 && \text{Punktet ligger på grafen} \\
    \\
    f'(-2) &= 0 && \text{Toppunkt så den deriverte er null}
\end{align*}

3) **Tangenten til grafen til $f$ i punktet $(3, f(3))$ har stigningstall $4$** <br>
Stigningstallet til tangenten er lik den deriverte i punktet $x = 3$, så vi kan skrive

$$
f'(3) = 4
$$


Nå har vi likningssystemet

\begin{align*}
    f(2) &= 6 \\
    \\
    f(-2) &= 8 \\
    \\
    f'(-2) &= 0 \\
    \\
    f'(3) &= 4
\end{align*}

Vi løser likningssystemet med CAS:

:::{figure} ./figurer/oppgave_3/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså har vi at 

$$
a = \dfrac{3}{20} \and b = \dfrac{7}{40} \and c = -\dfrac{11}{10} \and d = \dfrac{63}{10}
$$


:::::   


::::::::::::::::


---


::::::::::::::::{admonition} Oppgave 4 (Høst 2023)
---
class: exercise
---

:::{figure} ./figurer/oppgave_4/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Ovenfor har sara tegnet grafene til funksjonene $f$ og $g$ gitt ved 

\begin{align*}
    f(x) &= 2x + 8 \\
    \\
    g(x) &= x^3 - x^2 - 4x + 8
\end{align*}

Linjen $x = 1$ skjærer grafen til $f$ i punktet $P$ og grafen til $g$ i punktet $Q$.

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem avstanden fra $P$ til $Q$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
PQ = 6
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
La $PQ$ være avstanden fra $P$ til $Q$. Siden $x$-koordinaten til de to punktene er like, følger det at avnstanden $PQ$ er lik avstanden mellom $y$-koordinatene til punktene $P$ og $Q$. Altså blir avstanden:

$$
PQ = f(1) - g(1)
$$

Vi regner ut avstanden med CAS:

:::{figure} ./figurer/oppgave_4/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er avstanden fra $P$ til $Q$ gitt ved $PQ = 6$. 
:::::

::::::::::::::


::::::::::::::{tab-item} b
Sara skal tegne en ny linje $x = a$ der $a \in \langle 1, 3 \rangle$ i koordinatsystemet. <br>
Hun vil kalle skjæringspunktet mellom linjen og grafen til $f$ for $R$ og skjæringspunktet mellom linjen og grafen til $g$ for $S$.

Bestem $a$ slik at avstanden fra $R$ til $S$ blir størst mulig. Oppgi svaret eksakt.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a_\mathrm{størst} = \dfrac{\sqrt{19} + 1}{3}
$$
:::::

:::::{admonition} Løsning 
---
class: solution, dropdown
---
La $d(a)$ være avstanden fra $R$ til $S$. Da har vi at 

$$
d(a) = f(a) - g(a)
$$

For å bestemme hvilken verdi av $a$ som gir størst mulig avstand, kan vi bruke CAS til å løse $d'(a) = 0$ for $a \in \langle 1, 3 \rangle$:

:::{figure} ./figurer/oppgave_4/b.png
---
width: 100%
class: no-click, adaptive-figure
---
Merk at definisjonene av $f(x)$ og $g(x)$ ligger igjen fra oppgave **a**.
:::

Vi finner altså at 

$$
d'(a) = 0 \limplies a_\mathrm{størst} = \dfrac{\sqrt{19} + 1}{3}
$$

gir størst mulig avstand mellom $R$ og $S$. Vi kan være sikre på at dette er den riktige verdien for $a$ ved å sjekke $d(a)$ i endepunktene og sjekke at verdiene er lavere enn $d(a)$ i $a_\mathrm{størst}$:

:::{figure} ./figurer/oppgave_4/exercise.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Ja. Vi *legger'n død*.

:::::




::::::::::::::


:::::::::::::::

::::::::::::::::


---


::::::::::::::::{admonition} Oppgave 5 (Høst 2023)
---
class: exercise
---
En tredjegradsfunksjon $f$ er gitt ved 

$$
f(x) = ax^3 + bx^2 + cx - 64.
$$

* Punktet $(-8, 0)$ er et toppunkt på grafen til $f$.
* Den gjennomsnittlige vekstfarten til $f$ i intervallet $[0, 5]$ er $\dfrac{64}{5}$.


Bestem $a$, $b$ og $c$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
a = \dfrac{1}{5} \and b = \dfrac{11}{5} \and c = -\dfrac{16}{5}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan sette opp et likningssystem med tre likninger og tre ukjente fra opplysningene i oppgaven.

1) **Punktet $(-8, 0)$ er et toppunkt på grafen til $f$** <br>
Fra dette kan vi sette opp to likninger:

\begin{align*}
    f(-8) &= 0 && \text{Punktet ligger på grafen} \\
    \\
    f'(-8) &= 0 && \text{Toppunkt så den deriverte er null}
\end{align*}

2) **Den gjennomsnittlige vekstfarten til $f$ i intervallet $[0, 5]$ er $\dfrac{64}{5}$** <br>
Fra dette kan vi sette opp likningen

$$
\frac{f(5) - f(0)}{5 - 0} = \frac{64}{5}
$$

Vi løser likningssystemet med CAS:

:::{figure} ./figurer/oppgave_5/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at 

$$
a = \dfrac{1}{5} \and b = \dfrac{11}{5} \and c = -\dfrac{16}{5}
$$

:::::

::::::::::::::::


---


::::::::::::::::{admonition} Oppgave 6 (Vår 2022)
---
class: exercise
---
Grafen til en andregradsfunksjon $f$ har

* en tangent i punktet $(1, f(1))$ med stigningstall $0$.
* en tangent i punktet $(4, f(4))$ med stigningstall $6$. 


:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem $f'(x)$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f'(x) = 2x - 2.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Siden $f$ er en andregradsfunksjon, kan vi skrive den på formen

$$
f(x) = ax^2 + bx + c \limplies f'(x) = 2ax + b
$$

Fra opplysningene i oppgaven kan vi sette opp to likninger for de to ukjente koeffisientene $a$ og $b$:
\begin{align*}
    f'(1) &= 0  \\
    \\
    f'(4) &= 6
\end{align*}

Likningene følger fra at stigningstallet til tangentene er lik den deriverte i de aktuelle punktene. Vi løser likningssystemet med CAS:

:::{figure} ./figurer/oppgave_6/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at 

$$
f'(x) = 2ax + b = 2x - 2.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} b
Grafen til $f$ skjærer $y$-aksen i punktet $(0, 4)$.

Bestem $f(x)$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = x^2 - 2x + 4.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Fra oppgave **a** vet vi at 

$$
a = 1 \and b = -2. 
$$

Siden vi nå vet at grafen til $f$ skjærer $y$-aksen i punktet $(0, 4)$, følger det at 

$$
f(0) = c = 4. 
$$

Dermed er 

$$
f(x) = ax^2 + bx + c = x^2 - 2x + 4.
$$
:::::

::::::::::::::

:::::::::::::::


::::::::::::::::






::::::::::::::::{admonition} Oppgave 7 (Høst 2024)
---
class: exercise
---

:::{figure} ./figurer/oppgave_7/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


Else skal gjerde inn tre områder for å lage en grønnsakshage. Det største området skal ha form som et rektangel og de to minste som likebeinte rettvinklede trekanter. Se figuren ovenfor.

Else skal sette opp gjerde langs alle linjestykkene vist i figuren ovenfor. <br>
Hun har til sammen 100 m gjerde som hun vil bruke.

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Hvor stor blir arealet av grønnsakhagen dersom hun velger at katetene i trekantene skal være $8$ meter?


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A = 245.5 \, \mathrm{m}^2
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Først må vi bestemme hvor lange linjestykkene $y$ i figuren er. Vi vet at $x = 8$ meter. Til sammen summerer linjestykkene til $L = 100$ meter. Vi kan skrive den samlede lengden av linjestykkene som

$$
L = \underbrace{2x}_{\mathrm{kateter}} + \underbrace{2x + 2y}_{\mathrm{rektangel}} + \underbrace{2\sqrt{2}x}_{\mathrm{hypotenuser}} = 100
$$

der vi har brukt Pytagoras' setning til å finne at begge hypotenusene i de rettvinklede trekantene må være 

$$
h^2 = x^2 + x^2 \limplies h = \sqrt{2}x.
$$

Vi kan først løse likningen for $y$ slik at vi kan regne ut $y$ for en hver verdi av $x$:

$$
4x + 2y + 2\sqrt{2}x = 100 \liff 2x + y + \sqrt{2}x = 50
$$

som gir 

$$
y = 50 - (2 + \sqrt{2})x.
$$

Det samlede arealet til grønnsakhagen blir

\begin{align*}
    A &= A_{\mathrm{rektangel}} + 2A_{\mathrm{trekant}} \\
    \\
    &= xy + 2 \cdot \frac{1}{2}x^2 \\
    \\
    &= x\left(50 - (2 + \sqrt{2})x\right) + x^2 \\
    \\
    &= 50x - (2 + \sqrt{2})x^2 + x^2 \\
    \\
    &= 50x - (1 + \sqrt{2})x^2
\end{align*}


Vi kan definere en funksjon $A(x)$ i CAS og regne ut arealet for $x = 8$:

:::{figure} ./figurer/oppgave_7/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at arealet av grønnsakhagen er omtrent $A = 245.5 \, \mathrm{m}^2$ dersom katetene i trekantene er $8$ meter lange.


:::::

::::::::::::::

::::::::::::::{tab-item} b
Lag en oversikt som viser hvordan arealet av grønnsakhagen endrer seg dersom hun velger andre lengder på katetene. Av oversikten skal Else kunne se omtrent hvor lange katetene må være for at arealet av grønnsakhagen skal bli størst mulig.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker en grafisk framstilling av arealet $A(x)$ for å se hvordan arealet endrer seg med lengden på katetene. Vi kan bruke Geogebra-vinduet til å lage grafen til $A$ siden vi allerede har definert $A(x)$ i CAS.

:::{figure} ./figurer/oppgave_7/b.png
---
width: 100%
class: no-click, adaptive-figure
---
viser en grafisk fremstilling av arealet $A(x) \, \mathrm{m}^2$ på $y$-aksen når katetene i trekanten er $x$ meter lange. 
:::

Fra den grafiske framstillingen kan vi se at arealet er størst når katetene i trekanten er omtrent $x = 10$ meter lange fordi dette svarer til et toppunkt på grafen til $A$.
:::::


::::::::::::::


::::::::::::::{tab-item} c
Lag en modell $A$ som Else kan bruke for å regne ut arealet $A(x)$ av grønnsakhagen for ulike verdier av $x$.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
A(x) = 50x - (1 + \sqrt{2})x^2.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi har allerede laget denne modellen i oppgave **a** som er gitt ved 

$$
A(x) = 50x - (1 + \sqrt{2})x^2.
$$
:::::

::::::::::::::


::::::::::::::{tab-item} d
Bruk modellen til å finne den lengden av katetene som vil gi det største arealet.

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = (25\sqrt{2} - 25) \, \mathrm{m} \approx 10.36 \, \mathrm{m}.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å bestemme den kateten som gir størst mulig areal, bruker vi CAS og løser $A'(x) = 0$ for å bestemme $x$-koordinaten til toppunktet til $A$:

:::{figure} ./figurer/oppgave_7/d.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at arealet er størst når katetene i trekantene er 

$$
x = (25\sqrt{2} - 25) \, \mathrm{m} \approx 10.36 \, \mathrm{m}.
$$

Men *vet* vi at dette er et toppunkt? Ja, for den ledende koeffisienten til $A(x)$ er negativ, så vi *legger'n død* – og vi hadde strengt tatt grafen som viste det i oppgave **b** også.

:::::

::::::::::::::


::::::::::::::{tab-item} e
Bestem modellens gyldighetsområde.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
0 < x < \dfrac{50}{\sqrt{2} + 2}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Modellen er gyldig så lenge $A(x) > 0$ og $y > 0$. Vi løser den første ulikheten i CAS:


:::{figure} ./figurer/oppgave_7/e.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså er $A(x) > 0$ når

$$
x \in \left\langle 0, 50 \sqrt{2} - 50 \right\rangle.
$$

Men vi må også sjekke at $y > 0$. Fra **a** vet vi at 

$$
y = 50 - (2 + \sqrt{2})x
$$

så vi løser ulikheten $y > 0$ i CAS:

:::{figure} ./figurer/oppgave_7/e2.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Kombinerer vi de to løsningene, ser vi at modellen er gyldig så lenge

$$
0 < x < \dfrac{50}{\sqrt{2} + 2}
$$

:::::


::::::::::::::

:::::::::::::::

::::::::::::::::


---



::::::::::::::::{admonition} Oppgave 8 (Vår 2022)
---
class: exercise
---
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 - 2b\cdot x^2 + (b^2 + 3) \cdot x \quad \mathrm{der} \quad b \in \mathbb{R}.
$$

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Vis at $f$ bare har ett nullpunkt uavhengig av verdien av $b$.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bestemmer nullpunktene til $f$ ved å løse likningen $f(x) = 0$ med CAS:

:::{figure} ./figurer/oppgave_8/a.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Altså ser vi at 

$$
f(x) = 0 \liff x = 0. 
$$

Denne løsningen er ikke avhengig av verdien til $b$, for da måtte $b$ ha dukket opp som en del av løsningen. Dermed har $f$ bare ett nullpunkt uavhengig av verdien til $b$, og dette nullpunktet er $x = 0$.

:::::

::::::::::::::


::::::::::::::{tab-item} b
Løs likningen $f'(x) = 0$. 

For hvilke verdier av $b$ har grafen til $f$ bare ett stasjonært punkt? 

> Et *stasjonært punkt* er et punkt der den deriverte er lik null.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
b = -3 \or b = 3.
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi løser likningen $f'(x) = 0$ med CAS:

:::{figure} ./figurer/oppgave_8/b.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Vi får bare én løsning til $f'(x) = 0$ dersom diskriminanten er null som betyr at $f$ bare har *ett* stasjonært punkt dersom 

$$
b^2 - 9 = 0 \liff b = -3 \or b = 3.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} c
Dersom $b \neq 0$ har grafen til $f$ to tangenter med stigningstall $3$.

Bestem likningene for disse tangentene.


:::::{admonition} Fasit
---
class: answer, dropdown
---

* Tangenten i punktet* $(b, f(b))$ er $y = 3x$ 
* Tangenten i punktet $\left(\dfrac{1}{3}b, f\left(\dfrac{1}{3}b\right)\right)$ er $y = 3x + \dfrac{4}{27}b^3$.

:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi løser likningen $f'(x) = 3$ med CAS for å bestemme ved hvilke $x$-verdier vi får tangenter som har stigningstall $3$.

:::{figure} ./figurer/oppgave_8/c1.png
---
width: 100%
class: no-click, adaptive-figure
---
viser løsningen av $f'(x) = 3$. Vi bruker fortsatt $f(x)$ fra oppgave **a**.
:::

Altså er 

$$
f'(x) = 3 \liff x = b \or x = \dfrac{1}{3}b.
$$

Vi bestemmer likningene for tangentene i to punktene med CAS direkte med `Tangent(punkt, funksjon)`-funksjonen:

:::{figure} ./figurer/oppgave_8/c2.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som betyr at likningen for tangenten i $x = b$ er gitt ved 

$$
y = 3x
$$

og likningen for tangenten i $x = \dfrac{1}{3}b$ er gitt ved

$$
y = 3x + \dfrac{4}{27}b^3.
$$


:::::

::::::::::::::

:::::::::::::::

::::::::::::::::


---



::::::::::::::::{admonition} Oppgave 9 
---
class: exercise
---
Anna skal reise fra en holme som ligger $8$ km fra strandkanten. $12$ km fra det punktet på stranden som ligger nærmest holmen, ligger det en hytte. Se figuren nedenfor.

:::{figure} ./figurer/oppgave_9/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


Anna kan ro med en fart på $2$ km/t og gå med en fart på $6$ km/t.

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem hvor lang tid Anna bruker til hytta dersom hun ror i land $6$ km fra det punktet på stranden som ligger nærmest holmen.


:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T = 6 \, \mathrm{t}
$$
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
Vi bruker Pytagoras' setning til å regne ut hvor langt Anna må ro for å komme i land $6$ km fra det punktet på stranden som ligger nærmest holmen. Da får vi at:

$$
L_\mathrm{robåt} = \sqrt{6^2 + 8^2} \, \mathrm{km} = \sqrt{100} \, \mathrm{km} = 10 \, \mathrm{km}.
$$

Siden Anna ror med en fart på $2$ km/t, bruker hun tiden

$$
T_\mathrm{robåt} = \frac{L_\mathrm{robåt}}{2 \, \mathrm{km/t}} = \frac{10 \, \mathrm{km}}{2 \, \mathrm{km/t}} = 5 \, \mathrm{t}
$$

til å ro til stranden. Hun må deretter gå $12 - 6 = 6$ km til hytta. Siden hun går med en fart på $6$ km/t, bruker hun tiden

$$
T_\mathrm{gåtur} = \frac{6 \, \mathrm{km}}{6 \, \mathrm{km/t}} = 1 \, \mathrm{t}
$$

til å gå til hytta. Den totale tiden hun bruker til hytta blir derfor

$$
T = T_\mathrm{robåt} + T_\mathrm{gåtur} = 5 \, \mathrm{t} + 1 \, \mathrm{t} = 6 \, \mathrm{t}.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} b
Lag en modell $T$ som viser mange timer $T(x)$ Anna bruker på å reise til hytta dersom hun ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen. 

:::::{admonition} Fasit
---
class: answer, dropdown
---
$$
T(x) = \dfrac{\sqrt{x^2 + 6^2}}{2} + \dfrac{12 - x}{6}
$$
:::::


:::::{admonition} Løsning
---
class: solution, dropdown
---
Hvis Anna ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen, må hun ro en avstand på

$$
L_\mathrm{robåt}(x) = \sqrt{x^2 + 8^2}
$$

Anna ror med en fart på $2$ km/t, så tiden hun bruker til å ro blir

$$
T_\mathrm{robåt}(x) = \frac{L_\mathrm{robåt}(x)}{2} = \frac{\sqrt{x^2 + 8^2}}{2}.
$$

Siden avstanden er 12 km fra punktet på strandlinja nærmest holmen bort til hytta, så må hun gå

$$
L_\mathrm{gåtur}(x) = 12 - x
$$

kilometer til hytta. Anna går med en fart på $6$ km/t, så tiden hun bruker til å gå blir

$$
T_\mathrm{gåtur}(x) = \frac{L_\mathrm{gåtur}(x)}{6} = \frac{12 - x}{6}.
$$

Dermed vil en modell for tiden Anna bruker til hytta når hun ror i land $x$ km fra det punktet på stranden som ligger nærmest holmen være gitt ved

$$
T(x) = T_\mathrm{robåt}(x) + T_\mathrm{gåtur}(x) = \frac{\sqrt{x^2 + 8^2}}{2} + \frac{12 - x}{6}.
$$

:::::

::::::::::::::


::::::::::::::{tab-item} c
Bestem hvor Anna må gå i land for at hun skal bruke minst mulig tid på å reise til hytta. <br>
Hva er den kortest tiden Anna kan bruke?


:::::{admonition} Fasit
---
class: answer, dropdown
---
* Anna må gå i land ved $x \approx 2.83 \, \mathrm{km}$ for å få kortest mulig reisetid.
* Anna bruker da $T \approx 5.77 \, \mathrm{t}$ på reisen.
:::::

:::::{admonition} Løsning
---
class: solution, dropdown
---
For å finne ut hvor Anna må gå i land for at hun skal bruke minst mulig tid på å reise til hytta, løser vi likningen $T'(x) = 0$ med CAS for å finne $x$-koordinaten til et eventuelt bunnpunkt for $T$:


:::{figure} ./figurer/oppgave_9/c.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

Dermed vil Anna bruke minst mulig tid dersom hun går i land ved

$$
x = 2 \sqrt{2} \, \mathrm{km} \approx 2.83 \, \mathrm{km}.
$$

Da bruker hun ca. $5.77$ timer på reisen. 

Vi bør dobbeltsjekke at dette svarer til et bunnpunkt ved å regne ut $T(x)$ i endepunktene og sjekke at verdiene vi får er høyere:

:::{figure} ./figurer/oppgave_9/exercise.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

* Hvis Anna ror båten direkte til nærmeste punkt på stranden, bruker hun $T(0) = 6$ timer. 
* Hvis Anna ror båten hele veien til hytta, bruker hun $T(12) \approx 7.21$ timer.


**Konklusjon**:
* Anna må gå i land ved $x \approx 2.83 \, \mathrm{km}$ for å få kortest mulig reisetid.
* Anna bruker da $T \approx 5.77 \, \mathrm{t}$ på reisen.

:::::

::::::::::::::

:::::::::::::::


::::::::::::::::


---



::::::::::::::::{admonition} Oppgave 10 (Høst 2023)
---
class: exercise
---
Nedenfor ser du grafen til funksjon $f$ gitt ved 

$$
f(x) = \dfrac{8}{x^2 + 20}
$$

Rektangelet under grafen har hjørner i punktene $(0, 0)$, $(5, 0)$, $(5, f(5))$ og $(0, f(5))$. 

:::{figure} ./figurer/oppgave_10/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem arealet av rektangelet.


:::::{admonition} Løsning
---
class: solution, dropdown
---
Arealet til rektangelet er gitt ved 

$$
A = 5 \cdot f(5)
$$

Vi regner ut arealet med CAS:

:::{figure} ./figurer/oppgave_10/a/sol.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er arealet av rektangelet 

$$
A = \dfrac{8}{9}
$$

:::::



::::::::::::::


::::::::::::::{tab-item} b
Lag en systematisk oversikt som viser arealet av rektanglene som har hjørner i punktene $(0, 0)$, $(n, 0)$, $(n, f(n))$ og $(0, f(n))$ for $n \in \{1, 2, 3, \ldots, 10\}$. 


:::::{admonition} Løsning
---
class: solution, dropdown
---
> Her er det mange muligheten for hva som menes med "systematisk oversikt". Vi velger å lage en grafisk framstilling, men man kan for eksempel lage en verditabell ved hjelp av en Pythonprogram eller regne ut verdiene med CAS og lage en tabell manuelt.

Vi kan lage en modell $A$ for arealet av rektangelet, og så vise en graf av arealet der vi marker punktene $(n, A(n))$ for $n \in \{1, 2, 3, \ldots, 10\}$ på grafen. Modellen $A(x)$ vil være 

$$
A(x) = x \cdot f(x) = \dfrac{8x}{x^2 + 20}.
$$

Vi tegner grafen til $A$ med en graftegner og markerer punktene $(n, A(n))$ for $n \in \{1, 2, 3, \ldots, 10\}$:

:::{figure} ./figurer/oppgave_10/b/sol.png
---
width: 100%
class: no-click, adaptive-figure
---
viser grafen til arealet $A$ med punktene $(n, A(n))$ for $n \in \{1, 2, 3, \ldots, 10\}$ markert med koordinater. Her viser $y$-aksen arealet $A(x)$. 
:::


:::::


::::::::::::::


::::::::::::::{tab-item} c
Bestem $k$ slik at arealet av rektangelet som har hjørner i punktene $(0, 0)$, $(k, 0)$, $(k, f(k))$ og $(0, f(k))$ blir størst mulig.


:::::{admonition} Løsning 
---
class: solution, dropdown
---
For å bestemme hvilke verdi av $k$ som gir størst mulig areal, kan vi løse likningen $A'(k) = 0$ med CAS:

:::{figure} ./figurer/oppgave_10/c/sol.png
---
width: 90%
class: no-click, adaptive-figure
---
:::

Den eneste kandidaten for $k$ som gir mening er $k = 2\sqrt{5}$ siden dette er den eneste verdien av $k$ der $k > 0$. At 

$$
k = 2\sqrt{5} \approx 4.47
$$

gir størst mulig areal stemmer bra med oversikten vi lagde i oppgave **b** der vi kan se fra grafen at toppunktet må ligge mellom $x = 4$ og $x = 5$. Dermed vil $k = 2\sqrt{5}$ gi størst mulig areal av rektangelet.


:::::

::::::::::::::




:::::::::::::::

::::::::::::::::


---


::::::::::::::::{exercise} Oppgave 11 (Høst 2021)


:::{figure} ./figurer/oppgave_11/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Skissen ovenfor viser grafen til funksjonen $f$ gitt ved $f(x) = \dfrac{1}{x}$ og tangenten til grafen i punktet $(s, f(s))$. 

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Vis at likningen for tangenten er

$$
y = -\dfrac{1}{s^2}\cdot x + \dfrac{2}{s}
$$


:::::{solution} 
Vi kan bestemme tangenten til grafen direkte med CAS: 

:::{figure} ./figurer/oppgave_11/a.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som vi kan skrive om som følger:

$$
y = \dfrac{2s - x}{s^2} = \dfrac{2s}{s^2} - \dfrac{x}{s^2} = -\dfrac{1}{s^2}\cdot x + \dfrac{2}{s}
$$

som var det vi skulle vise.

:::::

::::::::::::::


::::::::::::::{tab-item} b
Tangenten skjærer koordinataksene i punktene $A$ og $B$.

Bestem koordinatene til $A$ og $B$ uttrykt ved $s$.


:::::{answer}
$$
A = \left(2s, 0\right) \and B = \left(0, \dfrac{2}{s}\right)
$$
:::::

:::::{solution}
Vi kaller tangenten for $T$. Da vil skjæringen med $y$-aksen svaret til $T(0)$ og skjæringen med $x$-aksen svarer til løsningen av $T(x) = 0$. Vi regner ut begge disse verdiene med CAS:

:::{figure} ./figurer/oppgave_11/b.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Fra celle 3, kan vi lese av at punktet $B$ kan skrives som 

$$
B = \left(0, \dfrac{2}{s}\right)
$$

Og fra celle 4 kan vi lese av at punktet $A$ kan skrives som

$$
A = \left(2s, 0\right)
$$

:::::

::::::::::::::


::::::::::::::{tab-item} c 
Bestem arealet av $\triangle OAB$.

:::::{answer}
Arealet av $\triangle OAB$ er gitt ved

$$
T_{\triangle OAB} = 2.
$$
:::::



:::::{solution}
$OA$ er grunnlinjen i trekanten og $OB$ er høyden. Arealet av trekanten er da:

$$
T_{\triangle OAB} = \dfrac{OA \cdot OB}{2} = \dfrac{2s \cdot \dfrac{2}{s}}{2} = \dfrac{4}{2} = 2.
$$

:::::


::::::::::::::

:::::::::::::::


::::::::::::::::


---



::::::::::::::::{exercise} Oppgave 12 (Eksempelsett 2021)
En funksjon $f$ er gitt ved 

$$
f(x) = x^3 - x - 1. 
$$


Grafen til $f$ har to tangenter som er parallelle med linjen $y = \dfrac{1}{2}x + 2$. 

Bestem en eksakt verdi for nullpunktet til hver av disse tangentene.

:::::{answer}
Tangenten i punktet $\left(-\dfrac{\sqrt{2}}{2}, f\left(-\dfrac{\sqrt{2}}{2}\right)\right)$ har nullpunktet

$$
x = -\sqrt{2} + 2
$$

og tangenten i punktet $\left(\dfrac{\sqrt{2}}{2}, f\left(\dfrac{\sqrt{2}}{2}\right)\right)$ har nullpunktet



$$
x = \sqrt{2} + 2
$$

:::::

:::::{solution}
Tangentene vil ha stigningstall $\dfrac{1}{2}$ siden de er parallelle med linjen $y = \dfrac{1}{2}x + 2$. Det betyr at tangentene må gå gjennom punkter på grafen til $f$ der 

$$
f'(x) = \dfrac{1}{2}.
$$

Vi løser likningen med CAS for å avgjøre hvilke to punkter tangentene går gjennom:

:::{figure} ./figurer/oppgave_12/sol_1.png
---
width: 90%
class: no-click, adaptive-figure
---
:::

Altså må tangentene gå gjennom to punkter på grafen til $f$ der 

$$
x = -\dfrac{\sqrt{2}}{2} \or x = \dfrac{\sqrt{2}}{2}.
$$

Vi bruker så tangent-funksjonen i CAS til å bestemme likningene for de to tangentene og deres nullpunkter:

:::{figure} ./figurer/oppgave_12/sol_2.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Dermed kan vi se at den ene tangenten har nullpunkt i $x = -\sqrt{2} + 2$ og den andre tangenten har nullpunkt i $x = \sqrt{2} + 2$.


:::::

::::::::::::::::

---


::::::::::::::::{exercise} Oppgave 13 (Eksempelsett 2021)


:::{figure} ./figurer/oppgave_13/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Figuren ovenfor viser grafen til en tredjegradsfunksjon $f$. <br>
Figuren viser også tangenten til grafen i tre ulike punkter.

Bruk tangentene til å bestemme et eksakt uttrykk for den deriverte funksjonen $f'$.



:::::{answer}
$$
f'(x) = 3(x + 1)(x - 1) \quad \mathrm{eller} \quad f'(x) = 3x^2 - 3.
$$
:::::


:::::{solution}
Den deriverte funksjonen $f'$ er en andregradsfunksjon som vi kan skrive på formen 

$$
f'(x) = ax^2 + bx + c. 
$$

Fra tangentene i grafen kan vi se at det er en tangent med stigningstall $0$ i $x = -1$ og $x = 1$ som betyr at 

$$
f'(-1) = 0 \and f'(1) = 0.
$$

Videre har vi en tangent som går gjennom $(0, 4)$ på grafen og samtidig går gjennom et annet punkt $(1, 1)$ som ikke er på grafen. Stigningstallet til denne tangenten blir da $-3$. Siden tangenten går gjennom grafen i $x = 0$, så vet vi derfor at den deriverte også oppfyller

$$
f'(0) = -3.
$$

Siden $f'$ er en andregradsfunksjon med nullpunkter i $x = -1$ og $x = 1$, så kan vi skrive opp $f'(x)$ på formen

$$
f'(x) = a(x + 1)(x - 1). 
$$

Videre kan vi bruke at $f'(0) = -3$ til å bestemme $a$:

$$
f'(0) = -3 = a \cdot (0 + 1)(0 - 1) \liff -3 = -a \liff a = 3.
$$

Dermed er 

$$
f'(x) = 3(x + 1)(x - 1).
$$

> En annen måte å uttrykke $f'(x)$ på er $f'(x) = 3x^2 - 3$ (standardform/ekstremalpunktsform). Spiller ingen rolle hvilken vi velger å bruke.

:::::


::::::::::::::::


---


::::::::::::::::{exercise} Oppgave 14
En takrenne skal lages i form av et åpent trapes ved å brette to sidekanter fra et flatt rektangel med en vinkel $x$ slik at alle sidelengder i takrenna er $10$ cm. <br> Se figuren nedenfor.

:::{figure} ./figurer/oppgave_14/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bestem tverrsnittsarealet $T$ av takrenna dersom vinkelen er $30^\circ$.

:::::{answer}
$$
T = 50 + 25 \sqrt{3} \; \mathrm{cm}^2
$$
:::::

:::::{solution}
Vi lager oss en hjelpefigur der vi tegner inn et rettvinklet trekant på hver side av trapeset og definerer en grunnlinje $g$ og en høyde $h$ for de to trekantene. Se figuren nedenfor.

:::{figure} ./figurer/oppgave_14/hjelpefigur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Arealet $T$ av figuren vil da være 

$$
T = \underbrace{10 \cdot h}_{\mathrm{rektangel}} + \underbrace{g\cdot h}_{\mathrm{trekantene}} 
$$

For å bestemme grunnlinja $g$ og høyden $h$, bruker vi definisjonen av sinus og cosinus i trekantene med $x = 30\degree$ som gir:


$$
\sin 30\degree = \dfrac{h}{10} \liff h = 10 \cdot \sin 30\degree = 10 \cdot \dfrac{1}{2} = 5
$$

og 

$$
\cos 30\degree = \dfrac{g}{10} \liff g = 10 \cdot \cos 30\degree = 10 \cdot \dfrac{\sqrt{3}}{2} = 5\sqrt{3}.
$$

der vi har brukt at $\sin 30\degree = \dfrac{1}{2}$ og $\cos 30\degree = \dfrac{\sqrt{3}}{2}$. Dermed er tverrsnittsarealet $T$ til takrenna når vinkelen er $30\degree$ gitt ved

$$
T = 10\cdot 5 + 5\sqrt{3} \cdot 5 = 50 + 25\sqrt{3}
$$

der $T$ er målt i cm$^2$.

:::::

::::::::::::::


::::::::::::::{tab-item} b
Lag en modell $T$ for tverrsnittsarealet $T(x) \, \mathrm{cm}^2$ når sidekantene er brettet opp $x$ grader.

:::::{answer}
$$
T(x) = 100 \cdot \sin x \cdot (1 + \cos x) 
$$
:::::

:::::{solution}
Vi generaliserer regningen vi gjorde i oppgave **a** som betyr at 

$$
\sin x = \dfrac{h}{10} \liff h(x) = 10 \cdot \sin x
$$

og 

$$
\cos x = \dfrac{g}{10} \liff g(x) = 10 \cdot \cos x.
$$

Dermed er en modell for tverrsnittsarealet $T$ til takrenna når vinkelen er $x$ grader gitt ved

\begin{align*}
    T(x) &= 10 \cdot h(x) + g(x) \cdot h(x) \\
    \\
    &= 10 \cdot (10 \cdot \sin x) + (10 \cdot \cos x) \cdot (10 \cdot \sin x) \\
    \\
    &= 100 \cdot \sin x + 100 \cdot \sin x \cdot \cos x \\
    \\
    &= 100 \cdot \sin x \cdot (1 + \cos x) \\
\end{align*}

:::::

::::::::::::::


::::::::::::::{tab-item} c
Bestem hvilken vinkel som sørger for at mest mulig vann kan strømme gjennom takrenna.

:::::{answer}
$$
x = 60\degree
$$
:::::

:::::{solution}
Mest mulig vann kan strømme gjennom takrenna dersom det er størst mulig tverrsnittsareal $T(x)$. Vi kan derfor bestemme hvilken vinkel $x$ som gir størst mulig tverrsnittsareal ved å løse likningen $T'(x) = 0$ med CAS:

:::{figure} ./figurer/oppgave_14/c_sol.png
---
width: 100%
class: no-click, adaptive-figure
---
:::

som gir $x = 60\degree$ som den eneste løsningen. Vi bør sjekke at dette er den største verdien ved å regne ut $T(x)$ i endepunktene $x = 0\degree$ og $x = 90\degree$ og sammenligne med verdien av $T(x)$ i $x = 60\degree$:

:::{figure} ./figurer/oppgave_14/c_check.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

Fra utskriften kan vi se at $T(60)$ er størst som betyr at $x = 60\degree$ gir størst mulig tverrsnittsareal $T(x)$ og dermed også lar mest mulig vann strømme gjennom takrenna. 

:::::

::::::::::::::

:::::::::::::::


::::::::::::::::



---




:::::::::::::::{exercise} Oppgave 15 (Høst 2022)

:::{plot}
width: 80%
align: right
ticks: off
axis: off
xmin: -20
xmax: 160
ymax: 80
ymin: -1
lw: 1.5
figsize: (3, 3)
function: 70/75**2 * (x - 75)**2, (0, 150), blue
hline: 70, 0, 150, solid, blue
hline: 0, 0, 75, dashed, gray
bar: (-10, 0), 70, vertical
text: -10, 35, "70 cm", center-left
bar: (0, 75), 150, horizontal
text: 75, 75, "150 cm", top-center
:::

En bedrift produserer gardiner. Hvert gardin skal ha form som en parabel. Høyden skal være 70 cm og lengden øverst skal være 150 cm. 

Se figuren til høyre. 

:::{clear}
:::

Bedriften vil klippe ut gardinene fra tøyruller som er 140 cm brede. For å bruke så lite tøy som mulig vil en maskin klippe ut gardinene slik figuren nedenfor viser.

:::{plot}
width: 80%
ticks: off
axis: off
xmin: -20
xmax: 500
ymax: 100
ymin: -100
lw: 1
figsize: (7, 5)
function: 70/75**2 * (x - 75)**2, (0, 150), blue
function: -70/75**2 * (x - (75 * sqrt(2) + 75))**2 + 70, (106.06601717798213, 256.06601717798213), blue
function: 70/75**2 * (x - (2 * 75 * sqrt(2) + 75))**2, (212.13203435596427, 362.13203435596427), blue
function: -70/75**2 * (x - (3 * 75 * sqrt(2) + 75))**2 + 70, (318.1980515339464, 468.1980515339464), blue
function: -70/75**2 * (x - 75)**2, (0, 150), blue
function: 70/75**2 * (x - (75 * sqrt(2) + 75))**2 - 70, (106.06601717798213, 256.06601717798213), blue
function: -70/75**2 * (x - (2 * 75 * sqrt(2) + 75))**2, (212.13203435596427, 362.13203435596427), blue
function: 70/75**2 * (x - (3 * 75 * sqrt(2) + 75))**2 - 70, (318.1980515339464, 468.1980515339464), blue
vline: 0, -70, 70, solid, blue
hline: -70, 0, 468.1980515339464, solid, blue
vline: 468.1980515339464, -70, 70, solid, blue
hline: 70, 0, 468.1980515339464, solid, blue
hline: 0, 106.06601717798213, 256.06601717798213, solid, blue
hline: 0, 318.1980515339464, 468.1980515339464, solid, blue
hline: 35, 0, 468.1980515339464, dashed, gray
hline: 0, 0, 468.1980515339464, dashed, gray
bar: (0, 80), 150, horizontal
text: 75, 85, "150 cm", top-center
bar: (-12, 35), 35, vertical 
text: -12, 52.5, "35 cm", center-left
bar: (480, 0), 70, vertical
text: 480, 35, "70 cm", center-right
:::


:::{cas-popup}
---
layout: sidebar
---
:::


Gjør beregninger, og finn ut hvor langt tøystykke bedriften minst må bruke for å lage åtte gardiner.



:::{clear}
:::


::::{answer}
468.2 cm.
::::

::::{solution}
Vi velger oss et koordinatssystem slik at $x$-aksen ligger midt på gardinen. Så velger vi $x = 0$ til å samsvare med venstre side av gardinen. La $f(x)$ være funksjonsuttrykket for den første parabelen øverst til venstre i tøystykket. 
Da vet vi at $f(0) = 70$ og $f(150) = 70.$ Siden funksjonsverdiene er de samme, må symmetrilinja ligge midt mellom de to punktene. Da kan vi bestemme symmetrilinja ved å ta gjennomsnittet av $x$-koordinatene: 

$$
x_0 = \dfrac{0 + 150}{2} = 75.
$$

Ekstremalpunktet til $f$ ligger da på $x$-aksen i $(75, 0)$. Dermed kan vi skrive $f(x)$ på ekstremalpunktsform som

$$
f(x) = a(x - 75)^2
$$

Vi bestemmer $a$ ved å bruke at $f(0) = 70$:

$$
f(0) = 70 \liff a(0 - 75)^2 = 70 \liff a = \dfrac{70}{75^2}
$$

Siden alle parablene er like, så vil denne verdien for $a$ gjelde for alle parablene. Målet vårt er å bestemme hvor langt tøystykket minst må være. 
Fokuserer vi på den stiplede linja $y = 35$, så kan vi observere at alle parablene skjærer hverandre ved denne linja. Hvis vi da kjenner til avstanden mellom disse skjæringspunktet, så har vi nesten avstanden til hele tøystykket. 
Vi mangler bare en bit på venstre side og en bit på høyre side som er like lange. 

Vi starter med å finne avstanden mellom skjæringspunktene til $f$ og linja $y = 35$ siden dette vil gi oss begge avstandene vi trenger. Da løser vi likningen

$$
f(x) = 35
$$

Vi gjør dette med CAS:


:::{figure} ./figurer/oppgaver/oppgave_15/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Som betyr at 

$$
x_1 = \dfrac{-75\sqrt{2} + 150}{2} \qog x_2 = \dfrac{75\sqrt{2} + 150}{2}.
$$

Her er $x_2 > x_1$, så avstanden mellom de to punktene er 

$$
\Delta x = x_2 - x_1 = \dfrac{75\sqrt{2} + 150}{2} - \dfrac{-75\sqrt{2} + 150}{2} = \dfrac{150\sqrt{2}}{2} = 75\sqrt{2}.
$$

Videre vil $x_1$ være avstanden fra starten av tøystykket til det første skjæringspunktene. Denne lengden opptrer én gang på hver side av tøystykket. Vi har 4 parabler, som betyr at lengden $\Delta x$ opptrer 4 ganger.
Dermed må lengden $L$ av tøystykket minst være 


\begin{align*}
L &= 2 \cdot x_1 + 4 \cdot \Delta x\\
\\
&= 2 \cdot \dfrac{-75\sqrt{2} + 150}{2} + 4 \cdot 75\sqrt{2}\\
\\
&= -75\sqrt{2} + 150 + 300\sqrt{2} \\
\\&= 150 + 225\sqrt{2} \\
\\
&\approx 468.2.
\end{align*}

Tøystykket bør altså være minst 468.2 cm langt for å lage åtte gardiner.
::::



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 16
I figuren nedenfor vises grafen til en andregradsfunksjon $f$ gitt ved 

$$
f(x) = ax^2 \qder a \in \langle 0, \to \rangle
$$

En innkommende lysstråle går parallelt med $y$-aksen og treffer grafen i punktet $Q(s, f(s))$. Strålen reflekteres slik at den har samme innfallsvinkel og utfallsvinkel med en tangent i punktet $Q$. Tangenten danner en midtnormal ned på linjestykke $BS$. 
Strålen beveger seg deretter gjennom punktet $P(0, k)$. Et punkt $R(s, -k)$ ligger på en linje $y = -k$ og danner en trekant $\triangle PQR$. 


:::{plot}
width: 70%
function: 0.5 * x**2, blue
ticks: off
ymin: -1
ymax: 4
xmax: 3
xmin: -3
hline: -0.5, -10, 10, solid, gray
point: (0, 0.5)
point: (2, 2)
point: (2, -0.5)
vector: 2, 8, 0, -6, red
vector: 2, 2, -2, -1.5, red
line-segment: (2, 2), (2, -0.5), black
line-segment: (0, 0.5), (2, -0.5), black
text: 0, 0.5, "$P(0, k)$", center-left
text: 2, 2, "$Q(s, f(s))$", bottom-right
text: 2, -0.5, "$R(s, -k)$", bottom-center
line: 2, (2, 2), dashed, red
point: (1, 0)
text: 1, 0, "$M$", bottom-left
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til punktet $M$ der tangenten i $R$ skjærer $x$-aksen.



:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til punktet $B$.



:::::::::::::



:::::::::::::{tab-item} c
En annen andregradsfunksjon $g$ er gitt ved

$$
g(x) = \dfrac{1}{2}(x - 2)^2 + 4.
$$


En lysstråle kommer parallelt inn med symmetrilinja og treffer grafen til $g$ i punktet $P(6, g(6))$. 

I hvilket punkt på symmetrilinja til $g$ vil den reflekterte strålen gå gjennom?


:::::::::::::


::::::::::::::



:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 16 (alternativ 2)

Når en innkommende lysstråle kommer parallelt med symmetrilinja til en parabel og treffer parabelen, så reflekteres strålen alltid gjennom et fast punkt som kalles parabelens **brennpunkt**. Grafen til en andregradsfunksjon $f$ er gitt ved

$$
f(x) = ax^2 \qder a \in \langle 0, \to \rangle
$$

Da vil brennpunktet $B$ ha koordinatene $B\left(0, \dfrac{1}{4a}\right)$.



:::{plot}
width: 70%
function: 0.5 * x**2, blue
ticks: off
ymin: -1
ymax: 4
xmax: 3
xmin: -3
hline: -0.5, -10, 10, solid, gray
point: (0, 0.5)
point: (2, 2)
point: (2, -0.5)
vector: 2, 8, 0, -6, red
vector: 2, 2, -2, -1.5, red
line-segment: (2, 2), (2, -0.5), black
line-segment: (0, 0.5), (2, -0.5), black
text: 0, 0.5, "$B\left(0, \displaystyle \frac{1}{4a}\right)$", top-left
text: 2, 2, "$R(s, f(s))$", bottom-right
text: 2, -0.5, "$S\left(s, -\displaystyle \frac{1}{4a}\right)$", bottom-center
line: 2, (2, 2), dashed, red
point: (1, 0)
text: 1, 0, "$M$", bottom-left
:::


:::::::::::::::

