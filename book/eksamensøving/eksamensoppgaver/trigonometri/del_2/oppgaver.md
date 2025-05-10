# Trigonometri (Del 2)

> Oppgavene her kan løses **med** hjelpemidler.

:::::::::::::::{exercise} Oppgave 1 (Vår 2024)
Du får vite følgende om en trekant $ABC$

* $AB$ er $8$
* $\angle A = 120\degree$
* Arealet av trekanten er $4\sqrt{3}$


Bestem lengdene av sidene $AC$ og $BC$ {popup}`eksakt.<Med eksakt så mener man at svaret skal uttrykkes med eventuelle brøker, kvadratrøtter, hele tall osv. Ingen desimaltall.>`


:::{cas-popup} 350 500
:::


:::::{answer}
$$
AC = 2 \and BC = 2 \sqrt{21}
$$

:::::


:::::{solution}
Vi kan lage oss en hjelpetegning for å få oversikt over trekanten:

:::{figure} ./figurer/oppgave_1/hjelpefigur.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser en skisse av trekanten der vi har satt $x = AC$ og $y = BC$. 
:::

Siden arealet er $T = 4\sqrt{3}$, kan vi sette opp en likningen for $x$ med utgangspunkt i arealsetningen for trekanten:

$$
T = \dfrac{1}{2} \cdot x \cdot 8 \cdot \sin (120\degree)
$$

\begin{align*}
4\sqrt{3} &= \dfrac{1}{2} \cdot x \cdot 8 \cdot \sin (120\degree)\\
\\
4 \cancel{\sqrt{3}} &= \dfrac{1}{2} \cdot x \cdot 8 \cdot \dfrac{\cancel{\sqrt{3}}}{2}\\
\\
4 &= \dfrac{8x}{4} \\
\\
4 &= 2x \\
\\
x &= 2
\end{align*}

Dermed er $AC = 2$. Så bruker vi cosinussetningen for å bestemme $y = BC$:

\begin{align*}
    y^2 &= 8^2 + 2^2 - 2 \cdot 8 \cdot 2 \cdot \cos (120\degree) \\
    \\
    y^2 &= 64 + 4 - 2 \cdot 8 \cdot 2 \cdot \left(-\dfrac{1}{2}\right) \\
    \\
    y^2 &= 64 + 4 + 16 \\
    \\
    y^2 &= 84 \\
    \\
    y &= \sqrt{84} = \sqrt{4\cdot 21} = \sqrt{4} \cdot \sqrt{21} \\
    \\
    y &= 2\sqrt{21}
\end{align*}

Dermed er $BC = 2\sqrt{21}$.


:::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2 (Høst 2024)

:::{figure} ./figurer/oppgave_2/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser en stjerne satt sammen av 12 like store likesidede trekanter.
:::

Maria skal lage en stjerne ved å sette sammen $12$ like store likesidede trekanter. <br>
Lengdene av sidekantene i trekantene er $4$.

Ved å bruke Pytagoras' setning og arealberegninger har Maria kommet fram til at arealet av stjernen vil bli $48\sqrt{3}$. 

Vis at du kan komme fram til samme resultat ved å bruke trigonometri. 


:::{cas-popup} 350 500
:::


:::::{solution}
Hver trekant er likesidet som betyr at alle vinklene er $60\degree$. Sidelengdene i trekantene er $4$, som betyr at arealet av én trekant kan regnes ut med arealsetningen direkte:


$$
T_\triangle = \dfrac{1}{2}\cdot 4 \cdot 4 \cdot \sin (60\degree) = \dfrac{16}{2}\cdot \frac{\sqrt{3}}{2} = 4 \sqrt{3}. 
$$

Stjernen består av $12$ slike trekanter, som betyr at arealet av stjernen er:

$$
T_\mathrm{stjerne} = 12 \cdot T_\triangle = 12 \cdot 4\sqrt{3} = 48\sqrt{3}.
$$

:::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 3 (Høst 2024)
Klassen til Isabel og Anniken skal vise at de kan bruke trigonometri til å bestemme arealet av figuren nedenfor.

:::{figure} ./figurer/oppgave_3/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Læreren har delt klassen i grupper og gitt hver gruppe noen opplysninger i tillegg til informasjon kan leses ut fra figuren.

:::{cas-popup} 350 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Gruppen til Isabel har fått vite at $AD = 6.0$, $BC = 10.0$, og at diagonalen $AC = 16.4$. 

Vis hvordan gruppen til Isabel kan bestemme arealet ved å bruke opplysningene de har tilgang til. <br> Husk å gjøre rede for hvilke trigonometriske sammenhenger du bruker.


:::::{answer}
$$
T_{\square ABCD} \approx 58.5
$$
:::::


:::::{solution}
Med den oppgitte diagonalen, er det naturlig å tenke på $\square ABCD$ som bestående av to trekanter $\triangle ABC$ og $\triangle ACD$. Vi kan bestemme arealet av de to trekantene hver for seg og så summere dem. 

For $\triangle ABC$ kan vi bruke arealsetningen umiddelbart så lenge vi kjenner til sinus til én av vinklene i trekanten. Vi kan bruke cosinussetningen for å bestemme $\cos \angle B$, og deretter kan vi Pytagoras' identitet til å bestemme $\sin \angle B$ ved

$$
(\sin \angle B)^2 + (\cos \angle B)^2 = 1 \limplies \sin \angle B = \sqrt{1 - (\cos \angle B)^2}.
$$

deretter brukes vi arealsetningen ved

$$
T_{\triangle ABC} = \dfrac{1}{2} \cdot AB \cdot BC \cdot \sin \angle B.
$$

Vi utfører beregningene med CAS:

:::{figure} ./figurer/oppgave_3/a_del1.png
---
width: 100%
class: no-click, adaptive-figure
---
her har vi satt $x = \cos \angle B$ i første likning.
:::

Vi gjør tilsvarende utregning for $\triangle ACD$ der vi må bestemme $\cos \angle D$ med cosinussetningen etterfulgt av å bruke Pytagoras' identitet for å bestemme $\sin \angle D$ som vi så plugger inn i arealsetningen:

:::{figure} ./figurer/oppgave_3/a_del2.png
---
width: 100%
class: no-click, adaptive-figure
---
her har vi satt $x = \cos \angle D$ i første likning.
:::

Til slutt summerer vi de to arealene som gir:

:::{figure} ./figurer/oppgave_3/a_del3.png
---
width: 85%
class: no-click, adaptive-figure
---
:::

Dermed er arealet av figuren

$$
T_{\square ABCD} = \dfrac{24 \sqrt{989} + 8\sqrt{7826}}{25} \approx 58.5
$$



:::::

:::::::::::::


:::::::::::::{tab-item} b
Gruppen til Anniken har fått vite at $\angle A = 62.5\degree$, $\angle C = 38.3\degree$, $\angle ABD = 45.5\degree$ og $\angle CBD = 85.5\degree$.


Vis hvordan gruppen til Anniken kan bestemme arealet ved å bruke opplysningene de har tilgang til. <br> Husk å gjøre rede for hvilke trigonometriske sammenhenger du bruker.



:::::{answer}
$$
T_{\square ABCD} \approx 58.5
$$
:::::

:::::{solution}
Med opplysningene som er oppgitt, er det naturlig å trekke en diagonal $BD$ slik at firkanten deles inn i to trekanter $\triangle ABD$ og $\triangle BCD$. Da kan vi bruke sinussetningen til å bestemme $x = AB$ ved 

$$
\dfrac{x}{\sin \angle C} = \dfrac{CD}{\sin \angle CBD}
$$

som vi gjør med CAS:

:::{figure} ./figurer/oppgave_3/b_del1.png
---
width: 90%
class: no-click, adaptive-figure
---
:::

Deretter kan vi bruke at 

$$
\angle BCD = 180\degree - \angle C - \angle CBD
$$

og så bruke arealsetningen ut ifra denne vinkelen for å bestemme arealet av $\triangle BCD$:

:::{figure} ./figurer/oppgave_3/b_del2.png
---
width: 90%
class: no-click, adaptive-figure
---
:::

Deretter bruker vi arealsetningen utifra vinkelen $\angle ABD$ til å bestemme arealet av $\triangle ABD$:

:::{figure} ./figurer/oppgave_3/b_del3.png
---
width: 90%
class: no-click, adaptive-figure
---
:::

Deretter er det bare å summere arealene av de to trekantene:

:::{figure} ./figurer/oppgave_3/b_del4.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er arealet av figuren

$$
T_{\square ABCD} \approx 58.5
$$



:::::

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4 (Høst 2024)


:::{figure} ./figurer/oppgave_4/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

I denne oppgaven skal du vise at du kan bruke trigonometri til å bestemme arealet av figuren ovenfor.

Bestem arealet. <br>
Husk å gjøre rede for hvilke trigonometriske sammenhenger du bruker.

:::{cas-popup} 350 500
:::

:::::{answer}
$$
T_{\square ABCD} \approx 50.78.
$$
:::::


:::::{solution} 
Vi starter med å lage en diagonal $AC$ i firkanten slik at vi får to trekanter $\triangle ABC$ og $\triangle ACD$. Se figuren nedenfor.

:::{figure} ./figurer/oppgave_4/hjelpefigur.svg
---
width: 80%
class: no-click, adaptive-figure
---
viser firkanten der diagonalen $x = AC$ er tegnet inn.
:::

Så bruker vi cosinussetningen for å bestemme lengden av diagonalen:

:::{figure} ./figurer/oppgave_4/del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Dermed er $AC$ eksakt gitt ved 

$$
AC = 5 \sqrt{\sqrt{2} - \sqrt{6} + 5}
$$

Deretter kan vi bruke cosinussetningen til å bestemme $\angle D$ slik at vi kan regne ut $\sin \angle D$ når vi skal bruke arealsetningen for $\triangle ACD$:

:::{figure} ./figurer/oppgave_4/del_2.png
---
width: 85%
class: no-click, adaptive-figure
---
:::


Med andre ord er $\angle D \approx 80.47\degree$. Da kan vi bruke arealsetningen for å bestemme arealet av $\triangle ACD$:

:::{figure} ./figurer/oppgave_4/del_3.png
---
width: 70%
class: no-click, adaptive-figure
---
:::

Altså er arealet av $\triangle ACD$ gitt ved

$$
T_{\triangle ACD} \approx 26.63.
$$

Deretter bruker vi arealsetningen for å bestemme arealet av $\triangle ABC$:

:::{figure} ./figurer/oppgave_4/del_4.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Til slutt summerer vi de to arealene for å bestemme arealet av firkanten:

:::{figure} ./figurer/oppgave_4/del_5.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er arealet av firkanten 

$$
T_{\square ABCD} \approx 50.78.
$$




:::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5 (Høst 2022)


:::{figure} ./figurer/oppgave_5/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

En sirkel har sentrum i $S$. $AB$ er diameter og $C$ er ligger på {popup}`sirkelperiferien.<Begrepet "sirkelperiferi" er en annen måte å si "sirkelbuen" eller "på kanten av sirkelskiven". Generelt betyr ordet "[...]periferi" noe sånn som "på kanten av [...]">`

Arealet av $\triangle SBC$ er $3\cdot \sqrt{2}$.

:::{cas-popup} 350 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem sirkelen radius. Bruk eksakte verdier.

:::::{answer}
$$
r = 2\sqrt{3}
$$
:::::


:::::{solution}
Vi lar $r$ være radiusen til sirkelen. Arealet til $\triangle SBC$ kan da skrives som 

$$
T_{\triangle SBC} = \dfrac{1}{2} \cdot r \cdot r \cdot \sin (45\degree) = \dfrac{1}{2} \cdot r^2 \cdot \frac{\sqrt{2}}{2} = \dfrac{r^2 \cdot \sqrt{2}}{4}
$$

> I utregningen ovenfor brukte vi at $\sin (45\degree) = \dfrac{\sqrt{2}}{2}$

Videre er $T_{\triangle SBC} = 3\sqrt{2}$, så vi kan sette opp en likning og løse den for radiusen $r$ som gir:

\begin{align*}
    3\sqrt{2} &= \dfrac{r^2 \cdot \sqrt{2}}{4} \\
    \\
    3 \cancel{\sqrt{2}} &= \dfrac{r^2 \cdot \cancel{\sqrt{2}}}{4} \\
    \\
    3 &= \dfrac{r^2}{4} \\
    \\
    3 \cdot 4 &= r^2 \\
    \\
    12 &= r^2 \\
    \\
    r &= \sqrt{12} = \sqrt{4\cdot 3} = \sqrt{4} \cdot \sqrt{3} = 2\sqrt{3}.
\end{align*}


:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem arealet av $\triangle ABC$. Bruk eksakte verdier.



:::::{answer}
$$
T_{\triangle ABC} = 6\sqrt{2}
$$
:::::

:::::{solution}
Trekant $\triangle ABC$ har samme høyde som $\triangle SBC$, men grunnlinja er dobbelt så lang siden $AB = 2\cdot SB = 2r$. Det betyr at arealet av $\triangle ABC$ er dobbelt så stort som arealet av $\triangle SBC$:

$$
T_{\triangle ABC} = 2 \cdot T_{\triangle SBC} = 2 \cdot 3\sqrt{2} = 6\sqrt{2}.
$$
:::::

:::::::::::::

::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 6 (Vår 2022)

:::{figure} ./figurer/oppgave_6/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

Gitt firkanten $ABCD$ ovenfor. 


:::{cas-popup} 350 500
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem et eksakt uttrykk for omkretsen av firkanten $ABCD$.


:::::{answer}
$$
\mathcal{O} = \left( 3\sqrt{2} + \sqrt{3} + 7\right) a
$$

:::::

:::::{solution}
For å regne ut omkretsen av firkanten, trenger vi først å bestemme lengden av $BD$. Vi kan bruke cosinussetningen til dette. La $x = BD$. Da får vi:

:::{figure} ./figurer/oppgave_6/del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at $BD = 2\sqrt{3} a$. Deretter kan vi bruke sinussetningen til å bestemme $AB$. La $x = AB$, da har vi:

:::{figure} ./figurer/oppgave_6/del_2.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at $AB = 3 \sqrt{2} a$. Så kan vi bruke sinussetningen én gang til for å bestemme $AD$. Vi lar $x = AD$, som gir:

:::{figure} ./figurer/oppgave_6/del_3.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at $AD = \left(\sqrt{3} + 3\right) a$. Så legger vi sammen alle sidene i firkanten for å bestemme omkretsen $\mathcal{O}$:

\begin{align*}
    \mathcal{O} &= AB + BC + CD + AD \\
    \\
    &= 3\sqrt{2} a + 2a + 2a + \left(\sqrt{3} + 3\right) a \\
    \\
    &= \left(3\sqrt{2} + 2 + 2 + \sqrt{3} + 3\right) a \\
    \\
    &= \left( 3\sqrt{2} + \sqrt{3} + 7\right) a
\end{align*}

:::::

:::::::::::::


:::::::::::::{tab-item} b
Vis at forholdet mellom arealet av $\triangle ABC$ og arealet av $\triangle BCD$ er $\dfrac{3}{2}\left(\sqrt{3} + 1\right)$


:::::{solution}
Vi regner ut arealet av $\triangle ABC$ og $\triangle BCD$ hver for seg, og deretter summerer vi de to arealene:

:::{figure} ./figurer/oppgave_6/b_del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at 

$$
T_{ABC} = \dfrac{1}{2} a^2 (3\sqrt{3} + 9) \and T_{BCD} = \sqrt{3} a^2. 
$$

Deretter tar vi forholdet mellom $T_{ABC}$ og $T_{BCD}$:

:::{figure} ./figurer/oppgave_6/b_del_2.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er forholdet mellom arealene:

$$
\dfrac{T_{ABC}}{T_{BCD}} = \dfrac{1}{2}\left(\sqrt{3} + 3\right) = \dfrac{3}{2}\left(\sqrt{3} + 1\right)
$$


:::::

:::::::::::::

::::::::::::::


:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 7 (Høst 2023)

:::{figure} ./figurer/oppgave_7/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

I denne oppgaven skal du vise at du kan bruke trigonometri til å bestemme arealet av figuren ovenfor.

Bestem arealet. <br>
Husk å gjøre rede for hvilke trigonometriske sammenhenger du bruker.


:::{cas-popup} 350 500
:::

:::::{answer}
$$
T_{ABCD} \approx 38.57.
$$
:::::


:::::{solution}
Vi starter med å bestemme vinkel $\angle C$ i $\triangle BCD$ slik at vi kan bruke arealsetningen. Vi bruker cosinussetningen til å bestemme $\angle C$:

:::{figure} ./figurer/oppgave_7/del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at $\angle C \approx 117.28\degree$. Deretter bruker vi arealsetningen for å bestemme arealet av $\triangle BCD$:

:::{figure} ./figurer/oppgave_7/del_2.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at $T_{BCD} \approx 21.33$. Deretter bruker vi sinussetningen for å bestemme $AD$. La $x = AD$. Da får vi:

:::{figure} ./figurer/oppgave_7/del_3.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som gir $AD \approx 8.4$. Til slutt bruker vi arealsetningen med utgangspunkt i $\angle ADB$. Først kan vi merke oss at 

$$
\angle ABD = 180\degree - 35\degree - 125\degree = 20\degree.
$$

Med arealsetningen får vi da:

:::{figure} ./figurer/oppgave_7/del_4.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som gir $T_{ABD} \approx 17.24$. Til slutt legger vi arealene sammen for å bestemme arealet til figuren:


:::{figure} ./figurer/oppgave_7/del_5.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Altså er arealet av figuren 

$$
T_{ABCD} \approx 38.57.
$$

:::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8 (Høst 2021)

:::{figure} ./figurer/oppgave_8/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::


Gitt firkanten $ABCD$. 

:::{cas-popup} 350 500
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at $BD = \sqrt{3} \cdot a$.


:::::{solution}
Først kan vi observere at $\triangle ABD$ er en likebeint trekant siden

$$
\angle ABD = 180\degree - 30\degree - 120\degree = 30\degree.
$$

Da følger det at $AD = a$. Da kan vi bruke cosinussetningen til å bestemme $BD$. La $x = BD$. Da har vi:

:::{figure} ./figurer/oppgave_8/a_del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at $AD = \sqrt{3} a$.

:::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem et eksakt uttrykk for omkretsen av firkanten.



:::::{answer}
$$
\mathcal{O} = \dfrac{1}{2} \left(4 + 3\sqrt{2} + \sqrt{6}\right) a
$$
:::::

:::::{solution}
For å bestemme omkretsen av firkanten, mangler vi nå bare å bestemme $CD$. Siden vi kjenner til både $BC$ og $BD$, kan vi bruke cosinussetningen til å bestemme $CD$. La $x = CD$. Da får vi:

:::{figure} ./figurer/oppgave_8/b_del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som betyr at 

$$
CD = \dfrac{\sqrt{2} + \sqrt{6}}{2}\cdot a
$$

Da blir omkretsen $\mathcal{O}$ av firkanten:

\begin{align*}
    \mathcal{O} &= AB + BC + CD + AD \\
    \\
    &= a + \sqrt{2} a + \dfrac{\sqrt{2} + \sqrt{6}}{2}\cdot a + a\\
    \\
    &= 2a + \dfrac{3\sqrt{2}}{2}a + \dfrac{\sqrt{6}}{2}a \\
    \\
    &= \left(2 + \dfrac{3\sqrt{2}}{2} + \dfrac{\sqrt{6}}{2}\right) a \\
    \\ 
    &= \dfrac{1}{2} \left(4 + 3\sqrt{2} + \sqrt{6}\right) a
\end{align*}



:::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $a$ slik at arealet av firkanten blir lik $\sqrt{3}$.


:::::{answer}
$$
a = \sqrt{6} - \sqrt{2}
$$
:::::

:::::{solution}
Vi starter med å bestemme et eksakt uttrykk for arealet av firkanten. Vi tar først utgangspunkt i $\triangle ABD$ og bruker arealsetningen med utgangspunkt i $\angle A$:

:::{figure} ./figurer/oppgave_8/c_del_1.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som gir $T_{ABD} = \dfrac{1}{4}\sqrt{3} a^2$. Deretter bruker vi arealsetningen for $\triangle BCD$ med utgangspunkt i $\angle DBC$:

:::{figure} ./figurer/oppgave_8/c_del_2.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

som gir at $T_{BCD} = \dfrac{1}{4}\left(\sqrt{3} + 3\right) a^2$. Til slutt setter vi opp likningen

$$
T_{ABD} + T_{BCD} = \sqrt{3}
$$

og løser likningen med hensyn på $a$:

:::{figure} ./figurer/oppgave_8/c_del_3.png
---
width: 80%
class: no-click, adaptive-figure
---
:::

Siden $\sqrt{6} > \sqrt{2}$, følger det at den eneste gyldige løsningen som gir det ønskede arealet er 

$$
a = -\sqrt{2} + \sqrt{6} = \sqrt{6} - \sqrt{2}
$$


:::::

:::::::::::::

::::::::::::::

:::::::::::::::



