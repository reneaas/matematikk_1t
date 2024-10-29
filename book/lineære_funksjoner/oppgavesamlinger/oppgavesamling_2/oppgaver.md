# Oppgavesamling 1

::::{admonition} Fagstoff som dekkes i oppgavesamlingen
---
class: reminder, dropdown
---
* Ulikheter
* Fortegnslinjer
* Likningssystemer
* Modellering
* CAS
* Programmering av likninger og likningssystemer
::::

> Oppgaver som er markert med (*) er oppgaver som kan være litt vanskeligere enn de andre oppgavene og passer ikke nødvendigvis med hva som er gjort i timene i alle klasser. Spør faglærer om du er usikker på om du skal gjøre disse oppgavene.

---

:::::::::::::::{admonition} Oppgave 1
---
class: problem-level-1
---
I {numref}`fig-lineære-funksjoner-oppgavesamling-2-oppgave-1` vises grafene til to lineære funksjoner $f$ og $g$. 

:::{figure} ./figurer/oppgave_1/graf.svg
---
name: fig-lineære-funksjoner-oppgavesamling-2-oppgave-1
width: 80%
class: no-click
---
viser grafene til $f$ og $g$.
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Bestem løsningen av 

$$
f(x) > 0.
$$

::::::{admonition} Fasit
---
class: dropdown, answer
---
:::::{tab-set}
::::{tab-item} Ulikhet
$$
x > 2
$$
::::

::::{tab-item} Løsningsmengde
$$
x \in \langle 2, \to \rangle
$$
::::
:::::


::::::


:::::::::::::

:::::::::::::{tab-item} b
Bestem løsningen av 

$$
g(x) \leq 0.
$$


::::::{admonition} Fasit
---
class: dropdown, answer
---
:::::{tab-set}
::::{tab-item} Ulikhet
$$
x \geq 8
$$
::::

::::{tab-item} Løsningsmengde
$$
x \in [8, \to \rangle
$$
::::
:::::


::::::


:::::::::::::

:::::::::::::{tab-item} c
Bestem løsningsmengden til 

$$
f(x) < 3.
$$

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x \in \langle \gets, 5 \rangle
$$
::::

:::::::::::::

:::::::::::::{tab-item} d
Bestem løsningen av

$$
f(x) \leq g(x).
$$


::::::{admonition} Fasit
---
class: dropdown, answer
---
:::::{tab-set}
::::{tab-item} Ulikhet
$$
x \leq 4
$$
::::

::::{tab-item} Løsningsmengde
$$
x \in \langle \gets, 4]
$$
::::
:::::


::::::


:::::::::::::

:::::::::::::{tab-item} e
Tegn fortegnslinja til $f(x)$. 


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgave_1/e.svg
---
width: 100%
class: no-click
---
:::
::::


:::::::::::::

:::::::::::::{tab-item} f
Tegn fortegnslinja til $g(x)$. 


::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgave_1/f.svg
---
width: 100%
class: no-click
---
:::
::::
:::::::::::::

::::::::::::::

:::::::::::::::


---

:::::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Løs ulikhetene ved regning. Sjekk svarene dine med CAS.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
3x - 2 > 0
$$

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x > \frac{2}{3}
$$
:::::
:::::::::::::

:::::::::::::{tab-item} b
$$
-2x + 3 \leq 5
$$

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x \geq -1
$$
:::::
:::::::::::::

:::::::::::::{tab-item} c
$$
2x - 1 < -4x + 7
$$

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x < \dfrac{4}{3}
$$
:::::

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
Løs likningssystemene ved regning. Sjekk svaret med CAS.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
\begin{align*}
    3x - 2y &= 5 \\
    \\
    -x + y &= -1
\end{align*}

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = 3 \quad \land \quad y = 2
$$
:::::
:::::::::::::


:::::::::::::{tab-item} b
\begin{align*}
    -2x - y &= 1 \\
    \\
    2x - y &= 7
\end{align*}

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = \dfrac{3}{2} \quad \land \quad y = -4
$$
:::::
:::::::::::::

:::::::::::::{tab-item} c
\begin{align*}
    x + 2y &= -1 \\
    \\
    x - 3y &= 5
\end{align*}

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
x = \dfrac{7}{5} \quad \land \quad y = -\dfrac{6}{5}
$$
:::::
:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---
Et tivoli har følgende prismodell. Det koster 200 kr å komme inn i tivoliet. Hver tur du kjører koster 30 kr.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Sett opp en funksjon $f$ som gir prisen i $f(x)$ kroner når du har kjørt $x$ turer.

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(x) = 200 + 30x
$$
:::::
:::::::::::::

:::::::::::::{tab-item} b
Hvor mye må du betale hvis du kjører $5$ turer?

:::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(5) = 200 + 30\cdot 5 = 200 + 150 = 350
$$

Du må betale 350 kr. 
:::::
:::::::::::::

:::::::::::::{tab-item} c
Hvor mange turer må du kjøre før du betaler mer enn 500 kr?


:::::{admonition} Fasit
---
class: dropdown, answer
---
For å løse problemet må vi løse likninga $f(x)> 500$
\begin{align*}
200 + 30x &> 500 \\
30 x &> 300 \\
x &> \frac{300}{30} \\
x &> 10
\end{align*}
Du må kjøre mer enn 10 turer før du betaler mer enn 500 kr. 
:::::
:::::::::::::

:::::::::::::{tab-item} d
En kjøretur tar 5 minutter. Tivoli er åpent i 3 timer.

Sett opp en definisjonsmengde og verdimengde for $f$ som passer med den praktiske situasjonen.
:::::{admonition} Fasit
---
class: dropdown, answer
---
$x$ representerer antall turer. Det minste antallet turer du kan ta er 0. På 3 timer kan du maksimalt rekke 36 turer. Vi får derfor

$$
D_f = [0, 36]
$$

Det minste beløpet du kan betale er 200 kr, dersom du ikke tar noen kjøreturer. Det største antallet er $f(36) = 200 + 30\cdot 36 = 1280 $. Vi får da verdimengden

$$
V_f = [200, 1280]
$$
:::::

:::::::::::::

::::::::::::::


:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
I tabellen under vises dyrket jord i antall dekar (dekar er et areal som tilsvarer $1000 \, \mathrm{m^2}$) som er brukt til andre formål en landbruk. Vi kaller dette for å **omdisponere** dyrket jord i noen utvalgte år i Norge.

| År | Antall dekar |
|:----:|:--------------:|
| $2011$ | $7\,079$ |
| $2015$ | $6\,422$ |
| $2018$ | $3\,908$ |
| $2020$ | $4\,740$ |
| $2022$ | $3\,604$ |
| $2023$ | $2\,941$ |

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene i tabellen til å bestemme en lineær modell $f$ der $f(x)$ gir antall dekar med omdisponert jord $x$ år etter 2011. 

:::::{admonition} Fasit
---
class: dropdown, answer
---
Bruker regresjon og får modellen

$$
f(x) = -340x + 7222
$$


:::::
:::::::::::::

:::::::::::::{tab-item} b
Gi en praktisk tolkning av stigningstallet og konstantleddet til modellen. 

Er de praktisk rimelige?

:::::{admonition} Fasit
---
class: dropdown, answer
---
Stigningstallet til modellen er $-340 \quad \mathrm{ dekar/år}$ og representerer den årlige nedgangen i omdisponering. Det er rimelig at stigningstallet er negativt ettersom vi ser at omdisponeringen synker i perioden vi studerer. Konstantleddet til modellen er $7222\quad \mathrm{ dekar}$. Dette representerer omdisponeringen ved modellens start, dvs i 2011. Vi ser at tallet ikke er nøyaktig likt tallet i tabellen, men i nærheten. Det er ikke unormalt, ettersom den lineære modellen er linja som passer best med alle punktene, og ikke bare det første. 
:::::
:::::::::::::

:::::::::::::{tab-item} c
Bestem hvor mye jord som vil brukes til andre formål enn jordbruk – ifølge modellen din – i årene
* 2030.
* 2050. 
:::::{admonition} Fasit
---
class: dropdown, answer
---
2030 tilsvarer $x = 19$ og 2050 tilsvarer $x=39$ i modellen. Vi får da

$$
f(19) = -340\cdot 19 + 7222 = 762
$$

Ifølge modellen vil det altså være 762 dekar som er omdisponert i 2030. 

$$
f(39) = -340\cdot 39 + 7222 = -6038
$$

Ifølge modellen vil det altså være -6038 dekar som er omdisponert i 2050. 

:::::

:::::::::::::

:::::::::::::{tab-item} d
Vurder gyldighetsområdet til modellen ut ifra opplysningene du har funnet i oppgaven.

:::::{admonition} Fasit
---
class: dropdown, answer
---

Ut fra svarene i oppgave c) ser vi at det er mulig at modellen kan være gyldig i 2030, men at den ikke er gyldig i 2050 ettersom vi får et negativt antall omdisponert areal. 

:::::
:::::::::::::
::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
Ett eple koster 5 kroner og én banan koster 3 kroner. Du kjøper til sammen 10 frukt og betaler 38 kroner.

Hvor mange epler og hvor mange bananer kjøpte du?

::::{admonition} Fasit
---
class: dropdown, answer
---
4 epler og 6 bananer.
::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---
Fortegnslinja til en lineær funksjon $f$ er gitt vist under.

:::{figure} ./figurer/oppgave_7.svg
---
width: 100%
---
:::

Bruk fortegnslinja til å løse ulikheten 

$$
f(x) < 0
$$

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 8 (*)
---
class: problem-level-1
---
Fortegnslinja til 

$$
g(x) = (x - 2)(x + 1)
$$

er vist i figur {numref}`fig-lineære-funksjoner-oppgavesamling-2-oppgave-8`.

:::{figure} ./figurer/oppgave_8.svg
---
name: fig-lineære-funksjoner-oppgavesamling-2-oppgave-8
width: 100%
class: no-click
---
viser fortegnslinja til $g(x)$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Løs ulikheten 

$$
g(x) < 0
$$
:::::::::::::

:::::::::::::{tab-item} b
Løs ulikheten 

$$
g(x) \geq 0
$$

:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 9
---
class: problem-level-2
---
En elev har skrevet et program for å løse en oppgave.

:::{code-block} python
---
linenos: true
---
def f(x):
    return 2 * x + 1


def g(x):
    return -x + 2


for x in range(-10, 11):
    if f(x) == g(x):
        print(x, f(x))
:::

Under vises fire mulige oppgaver eleven jobber med. 

Bestem hvilke av oppgavene du kan løse med utskriften til programmet. 


::::::::::::::{grid}

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
A

$$
2x - 1 > -x + 2
$$
:::::::::::::

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
B

$$
2x - 1 = -x + 2
$$
:::::::::::::

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
C

\begin{align*}
    -2x + y &= -1 \\
    \\
    x + y &= 2
\end{align*}
:::::::::::::

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
D

$$
3x - 3 = 0
$$

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 10
---
class: problem-level-2
---
En lineær funksjon $f$ er gitt ved 

$$
f(x) = 2x - 4.
$$

:::::::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::::::{tab-item} a
Bruk $f(x)$ til å lage en ulikhet med løsningen

$$
x < 2
$$

::::::::::::::

::::::::::::::{tab-item} b
Bruk $f(x)$ til å lage en ulikhet med løsningsmengden

$$
x \in \langle \gets, 6]
$$
::::::::::::::

::::::::::::::{tab-item} c
Løsningsmengden til en ulikhet 

$$
f(x) > h(x)
$$

for en lineær funksjon $h$ er 

$$
x \in \langle -3, \to \rangle
$$

Bestem et mulig uttrykk for $h(x)$.

::::::::::::::
:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 11
---
class: problem-level-2
---

Grafene til to lineære funksjoner $f$ og $g$ er vist i {numref}`fig-lineære-funksjoner-oppgavesamling-2-oppgave-11`.

:::{figure} ./figurer/oppgave_11.svg
---
name: fig-lineære-funksjoner-oppgavesamling-2-oppgave-11
width: 80%
class: no-click
---
viser grafene til to lineære funksjoner $f$ og $g$.
:::

Under vises 4 likningssystemer. 

Bestem hvilke(t) likningssystem du kan løse med grafene i {numref}`fig-lineære-funksjoner-oppgavesamling-2-oppgave-11`.


::::::::::::::{grid}

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
A

\begin{align*}
    x - y &= 1 \\
    \\
    -2x + y &= -4
\end{align*}
:::::::::::::

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
B

\begin{align*}
    x + y &= 1 \\
    \\
    -x + 2y &= -4
\end{align*}
:::::::::::::

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
C

\begin{align*}
    -x + y &= -1 \\
    \\
    \dfrac{1}{2}x - y &= 2
\end{align*}
:::::::::::::

:::::::::::::{grid-item}
---
outline: true
columns: 6
---
D

\begin{align*}
    x + y &= -1 \\
    \\
    -\dfrac{1}{2}x - y &= -2
\end{align*}
:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 12
---
class: problem-level-2
---
Grafene til tre lineære funksjoner $f$ og $g$ og $h$ er vist i figur. 

:::{figure} ./figurer/oppgave_12/graf.svg
---
name: fig-lineære-funksjoner-oppgavesamling-2-oppgave-12-graf
width: 80%
class: no-click
---
viser grafene til tre lineære funksjoner $f$ og $g$ og $h$.
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En elev har tegnet et fortegnsskjema, men har glemt å markere hvilken funksjon fortegnslinja tilhører.

Bestem hvilken funksjon fortegnslinja tilhører.

:::{figure} ./figurer/oppgave_12/a.svg
---
width: 100%
class: no-click
---
:::

:::::::::::::

:::::::::::::{tab-item} b
Tegn fortegnslinjene til de gjenværende funksjonene.

:::::::::::::


::::::::::::::

:::::::::::::::

---

:::::::::::::::{admonition} Oppgave 13 (*)
---
class: problem-level-3
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fortegnslinja til 

$$
f(x) = -2(x - 1)(x + 3)
$$

er vist under. 

Bestem løsningen av ulikheten 

$$
f(x) < 0
$$

:::{figure} ./figurer/oppgave_13/a.svg
---
name: fig-lineære-funksjoner-oppgavesamling-2-oppgave-13-a
width: 100%
class: no-click
---
viser fortegnslinja til $f(x)$.
:::

:::::::::::::

:::::::::::::{tab-item} b
En annen funksjon er gitt ved 

$$
g(x) = 3(x + 1)(x - 4)
$$

Tegn fortegnsskjema til $g$. 

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{figure} ./figurer/oppgave_13/b.svg
---
width: 100%
class: no-click
---
:::
::::

:::::::::::::

:::::::::::::{tab-item} c
Bruk fortegnsskjema fra oppgave b til å løse ulikheten 

$$
g(x) \geq 0
$$
:::::::::::::

:::::::::::::{tab-item} d
En funksjon $h$ har en fortegnslinje som vist i {numref}`fig-lineære-funksjoner-oppgavesamling-2-oppgave-13-d`.

Bestem et mulig uttrykk for $h(x)$ som passer med fortegnslinja.

:::{figure} ./figurer/oppgave_13/d.svg
---
name: fig-lineære-funksjoner-oppgavesamling-2-oppgave-13-d
width: 100%
class: no-click
---
viser fortegnslinja til $h(x)$.
:::

:::::::::::::
::::::::::::::
:::::::::::::::