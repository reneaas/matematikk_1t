# Trigonometri (Del 1)

> Disse oppgavene skal løses **uten** hjelpemidler.

:::::::::::::::{exercise} Oppgave 1 (Vår 2023)
::::{sidebar}
:::{figure} ./figurer/oppgave_1/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

En rettvinklet trekant har sidelengder $8$, $6$ og $10$. <br> Se figuren til høyre.

Vis at 

$$
\left(\cos u\right)^2 + \left(\sin u\right)^2 = 1
$$


:::{clear}
:::

:::::{solution}
Fra figuren, kan vi regne ut cosinus til vinkel $u$ som

\begin{align*}
    \cos u & = \dfrac{\mathrm{hosliggende \, katet \, til} \, u}{\mathrm{hypotenus}} \\
    \\
    \cos u & = \dfrac{6}{10} = \dfrac{3}{5} \\
\end{align*}

Tilsvarende kan vi for sinus til vinkel $u$ regne ut:

\begin{align*}
    \sin u & = \dfrac{\mathrm{motstående \, katet \, til} \, u}{\mathrm{hypotenus}} \\
    \\
    \sin u & = \dfrac{8}{10} = \dfrac{4}{5} \\
\end{align*}

Til slutt regner vi ut:

\begin{align*}
    \left(\cos u\right)^2 + \left(\sin u\right)^2 &= \left(\dfrac{3}{5}\right)^2 + \left(\dfrac{4}{5}\right)^2 \\
    \\
    &= \dfrac{3^2}{5^2} + \dfrac{4^2}{5^2} \\
    \\
    &= \dfrac{9}{25} + \dfrac{16}{25} \\
    \\
    &= \dfrac{9 + 16}{25} \\
    \\
    &= \dfrac{25}{25} \\
    \\
    &= 1.
\end{align*}


:::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2 (Høst 2023)
::::{sidebar}
:::{figure} ./figurer/oppgave_2/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

En likesidet trekant har sidelengder $2$. <br> Se figuren til høyre.

Bruk trekanten til å vise at 

$$
\cos 60\degree = \dfrac{1}{2}
$$


:::{clear}
:::

:::::{solution}
Vi tegner oss en hjelpefigur der vi slår en normal fra toppunktet ned på grunnlinja i trekanten. Da vil grunnlinja være delt i to like store deler som begge har lengde $1$. 


::::{sidebar}
:::{figure} ./figurer/oppgave_2/hjelpefigur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

Deretter kan vi bruke definisjonen av cosinus direkte:

Så bruker vi at 

$$
\cos 60\degree = \dfrac{\mathrm{hosliggende \, katet}}{\mathrm{hypotenus}} = \dfrac{1}{2}
$$

:::::


:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 3 (Høst 2023)

:::{figure} ./figurer/oppgave_3/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Hvilken av de to trekantene har størst areal?

Husk å argumentere for at svaret ditt er riktig.


:::::{solution}
Fra arealsetningen har vi at 

$$
T = \dfrac{1}{2}\cdot 6^2 \cdot \sin u
$$

der $u$ er vinkelen mellom de to sidelengdene. Siden $\sin u$ er en voksende størrelse for $u \in [0\degree, 90\degree]$, så vil en vinkel nærmest mulig $u = 90\degree$ gi størst mulig verdi for $\sin u$ og dermed størst areal. Siden $\sin u = \sin (180\degree - u)$, følger det at 

$$
\sin 150\degree = \sin (180\degree - 30\degree) = \sin 30\degree.
$$

Men $u = 32\degree$ er nærmere $90\degree$ enn $u = 30\degree$, som betyr at $\sin 32\degree > \sin 30\degree$. Dermed er arealet til trekanten med $u = 32\degree$ større enn arealet til trekanten med $u = 150\degree$. Derfor er trekanten til høyre med $u = 32\degree$ trekanten med størst areal.
:::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 4 (Vår 2024)
::::{sidebar}
:::{figure} ./figurer/oppgave_4/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::


Tom har arbeidet med trekanten til høyre og påstår at 

$$
\tan u \cdot \tan v = 1. 
$$

:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at Tom har rett.

:::::{solution}
Vi kan først bestemme $tan u$:

$$
\tan u = \dfrac{\mathrm{motstående \, katet \, til \,} u}{\mathrm{hosliggende \, katet \, til \,} u} = \dfrac{6}{8} = \dfrac{3}{4}.
$$

Deretter bestemmer vi $\tan v$:

$$
\tan v = \dfrac{\mathrm{motstående \, katet \, til \,} v}{\mathrm{hosliggende \, katet \, til \,} v} = \dfrac{8}{6} = \dfrac{4}{3}.
$$

Så ganger vi de to sammen:

$$
\tan u \cdot \tan v = \dfrac{3}{4} \cdot \dfrac{4}{3} = \dfrac{3\cdot 4}{4\cdot 3} = 1.
$$

Så Tom har derfor rett i sin påstand.
:::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør om påstanden stemmer for alle rettvinklede trekanter med to spisse trekanter $u$ og $v$.

:::::{solution}
::::{sidebar}
:::{figure} ./figurer/oppgave_4/hjelpefigur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::


Vi lager oss en generell trekant med spisse vinkler $u$ og $v$, og sidelengder $a$, $b$ og $c$. Se figuren til høyre.

Fra figuren kan vi skrive ned $\tan u$ som:

$$
\tan u = \dfrac{\mathrm{motstående \, katet \, til \,} u}{\mathrm{hosliggende \, katet \, til \,} u} = \dfrac{c}{b}.
$$

og tilsvarende for $\tan v$:

$$
\tan v = \dfrac{\mathrm{motstående \, katet \, til \,} v}{\mathrm{hosliggende \, katet \, til \,} v} = \dfrac{b}{c}.
$$

Deretter ganger vi de to sammen:

$$
\tan u \cdot \tan v = \dfrac{c}{b} \cdot \dfrac{b}{c} = \dfrac{c\cdot b}{b\cdot c} = 1.
$$

Dermed stemmer påstanden for alle rettvinklede trekanter med to spisse vinkler $u$ og $v$.



:::::

:::::::::::::

::::::::::::::



:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 5 (Høst 2024)
::::{sidebar}
:::{figure} ./figurer/oppgave_5/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

Snorre har funnet formelen nedenfor i en matematikkbok

$$
2\cdot \sin (u) \cdot \cos (u) = \sin (2\cdot u)
$$

Bruk trekanten til høyre og vis at formelen gjelder når $u = 30\degree$.

:::{clear}
:::

::::::::::{solution}
Vi skal bruke at $u = 30\degree$. For å vise at formelen gjelder for trekanten trenger vi da å bestemme 
1. $\sin (30\degree)$
2. $\cos (30\degree)$
3. $\sin (2\cdot 30\degree) = \sin (60\degree)$

Vi har 

$$
\sin (30\degree) = \dfrac{1}{2} \and \cos (30\degree) = \dfrac{\sqrt{3}}{2}.
$$

Tilsvarende kan vi bestemme $\sin (60\degree)$ ved 

$$
\sin (60\degree) = \dfrac{\sqrt{3}}{2}.
$$

Så sjekker vi om formelen stemmer:

::::::::{grid} 1 1 2 2
:::::::{grid-item-card}
---
columns: 8
---
Venstre side
^^^
$$
2 \cdot \sin (30\degree) \cdot \cos (30\degree) = 2 \cdot \dfrac{1}{2} \cdot \dfrac{\sqrt{3}}{2} = \dfrac{\sqrt{3}}{2}
$$
:::::::

:::::::{grid-item-card}
---
columns: 4
---
Høyre side
^^^
$$
\sin (60\degree) = \dfrac{\sqrt{3}}{2}
$$
:::::::
::::::::

Sammenligner vi venstre side og høyre side, så kan vi observere at de er like. Dermed gjelder formelen for trekanten når $u = 30\degree$.

::::::::::

:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 6 (Høst 2024)


I koordinatsystemet til nedenfor har vi tegnet en sirkel med radius $r = 1$. Punktet $P(0.64, 0.77)$ ligger på sirkelen.

:::{figure} ./figurer/oppgave_6/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Er $\tan 50\degree > 1$? <br>
Husk å begrunne svaret ditt.

:::::{solution}
Fra figuren kan vi se at 

$$
\tan 50\degree = \dfrac{0.77}{0.64} > 1
$$

Dermed er $\tan 50\degree > 1$.
:::::

:::::::::::::


:::::::::::::{tab-item} b
Er $\tan 130\degree > 0$? <br>
Husk å begrunne svaret ditt.

:::::{solution}
Hvis vi speiler punktet $P$ om $y$-aksen og tegner en stråle ut fra origo til punktet, får vi et punkt $Q$ som danner en vinkel $130\degree$ med $x$-aksen. Koordinatene til punktet $Q$ er da $Q(-0.64, 0.77)$. Regner vi ut $\tan 130\degree$ får vi:

$$
\tan 130\degree = \dfrac{0.77}{-0.64} < 0
$$

Dermed er **ikke** $\tan 130\degree > 0$.
:::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7 (Høst 2022)
::::{sidebar}
:::{figure} ./figurer/oppgave_7/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::
::::

Gitt trekanten til høyre.

Vis at 

$$
\dfrac{\sin u}{\cos u} = \tan u
$$


:::{clear}
:::

:::::{solution}
Først regner vi ut $\sin u$:

$$
\sin u = \dfrac{\mathrm{motstående \, katet \, til \,} u}{\mathrm{hypotenus}} = \dfrac{4}{5}.
$$

Deretter regner vi ut $\cos u$:

$$
\cos u = \dfrac{\mathrm{hosliggende \, katet \, til \,} u}{\mathrm{hypotenus}} = \dfrac{3}{5}.
$$

Så bestemmer vi $\tan u$ med definisjonen:

$$
\tan u = \dfrac{\mathrm{motstående \, katet \, til \,} u}{\mathrm{hosliggende \, katet \, til \,} u} = \dfrac{4}{3}.
$$

Alt vi må gjøre nå er å vise at kvotienten $\dfrac{\sin u}{\cos u}$ gir samme verdi som $\tan u$:

$$
\dfrac{\sin u}{\cos u} = \dfrac{4/5}{3/5} = \dfrac{4}{\cancel{5}} \cdot \dfrac{\cancel{5}}{3} = \dfrac{4}{3} = \tan u.
$$
:::::

:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 8 (Vår 2022)
Om en rettvinklet trekant $ABC$ får du vite at $\tan \angle B = \dfrac{3}{4}$. 
* Kan det være riktig at $\sin \angle B = \dfrac{3}{10}$?
* Kan det være riktig at den ene kateten er $6$ og den andre kateten er $8$?
* Kan det være riktig at hypotenusen er kortere enn $4$?



:::::{solution}
::::{tab-set}
---
class: tabs-parts
---
:::{tab-item} Påstand 1
Dersom $\tan \angle B = \dfrac{3}{4}$ så følger det at trekanten må være formlik med en trekant der katetene er $3$ og $4$. Det betyr at hvilken enn trekant dette måtte være, så er den formlik med en trekant der hypotenusen $h$ er 

$$
h = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5.
$$

Dermed må $\sin \angle B$ være

$$
\sin \angle B = \dfrac{\mathrm{motstående \, katet}}{\mathrm{hypotenus}} = \dfrac{3}{5}.
$$

Så med andre ord er $\sin \angle B \neq \dfrac{3}{10}$.
:::

:::{tab-item} Påstand 2
La oss anta at den ene kateten er $6$ og den andre kateten er $8$. Dette er en mulighet fordi

$$
\tan \angle B = \dfrac{3}{4} = \dfrac{2\cdot 3}{2\cdot 4} = \dfrac{6}{8}.
$$

Så denne påstanden kan være riktig.
:::

:::{tab-item} Påstand 3
Hypotenusen kan være kortere enn $4$ fordi $\tan \angle B$ bare beskriver forholdstallet mellom katetene. Dermed vil finnes to kateter som medfører at hypotenusen er kortere enn $4$ og samtidig at $\tan \angle B = \dfrac{3}{4}$.
:::
::::
:::::



:::::::::::::::









