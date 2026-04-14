# Sinussetningen


:::{admonition} Læringsmål
---
class: tip
---
* Kunne begrunne sinussetningen ut ifra arealsetningen.
* Kunne bruke sinussetningen ti lå finne ukjente sinusverdier eller ukjente sider i en trekant.
:::

Sinussetningen gir oss en direkte sammenheng mellom sinus til en vinkel og lengden av den motstående siden i en trekant. Dette lar oss bestemme både ukjente sider og ukjente sinusverdier i en hvilken som helst trekant. Og det som er så greit, er at det bare er en konsekvens av arealsetningen.


:::{plot}
width: 100%
ticks: off
axis: off
axis: equal 
align: right
triangle: svs=(3, 45, 4), angles=all, color=blue, angle-color=red, angle-radius=80, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24
fontsize: 32
:::

Når vi jobbet med arealsetningen, fant vi at vi kunne skrive opp arealet ut ifra alle tre hjørnene i trekanten. 

$$
\begin{align*}
T &= \dfrac{1}{2} bc \sin A \\
\\
T &= \dfrac{1}{2} ac \sin B \\
\\
T &= \dfrac{1}{2} ab \sin C
\end{align*}
$$

De tre uttrykkene er jo lik det **samme** arealet, så da må de alle tre være lik hverandre:

$$
\dfrac{1}{2} bc \sin A = \dfrac{1}{2} ac \sin B = \dfrac{1}{2} ab \sin C
$$

Hvis vi ganger med $2$ i hvert uttrykk, så får vi at

$$
bc \sin A = ac \sin B = ab \sin C
$$

Hvis vi nå deler med $abc$ i hvert uttrykk, så får vi at 

$$
\dfrac{bc \sin A}{abc} = \dfrac{ac \sin B}{abc} = \dfrac{ab \sin C}{abc}
$$

Deler vi bort alle faktorer som er felles, får vi et en ganske fin sammenheng:

$$
\dfrac{\sin A}{a} = \dfrac{\sin B}{b} = \dfrac{\sin C}{c}
$$

Vi ser at sinus til en vinkel delt på lengden av den motstående siden er den samme for alle tre hjørner. Dette kalles for **sinussetningen**.



:::::::::::::::{summary} Sinussetningen
:::{plot}
width: 100%
ticks: off
axis: off
axis: equal 
align: right
triangle: svs=(3, 45, 4), angles=all, color=blue, angle-color=red, angle-radius=80, corner-labels=(A="$A$", B="$B$", C="$C$"), lw=3, side-text=(AB="$c$", CA="$b$", BC="$a$"), label-offset=24
fontsize: 32
:::

For alle trekanter $ABC$, så gjelder 

$$
\boxed{\dfrac{\sin A}{a} = \dfrac{\sin B}{b} = \dfrac{\sin C}{c}}
$$

:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
:::{plot}
figsize: (6, 3)
width: 100%
align: right
fontsize: 32
axis: off
axis: equal 
triangle: sss=(4, 2*sqrt(6), 2*sqrt(3) - 2), angles=(A, C), color=blue, angle-color=red, angle-radius=40, corner-labels=(A="$A$", B="$B$", C="$C$"), side-labels=(AB=exact), label-offset=24, angle-labels=(A=numeric, C=numeric), angle-offset=24
nocache:
:::

Gitt trekanten $\triangle ABC$.

Bestem $BC$.


:::{clear}
:::

::::{solution}
---
dropdown: 0
---
Vi kjenner til vinkelene i hjørne $A$ og hjørne $C$. Den motstående siden til vinkel $A$ er $BC$, og den motstående siden til vinkel $C$ er $AB$. Med sinussetningen kan vi da sette opp likningen

$$
\dfrac{\sin A}{BC} = \dfrac{\sin C}{AB}
$$

Vi lar $x = BC$. Da får vi at 

$$
\dfrac{\sin 120\degree}{x} = \dfrac{\sin 45\degree}{4}
$$

Vi har at $\sin 120\degree = \dfrac{\sqrt{3}}{2}$ og $\sin 45\degree = \dfrac{\sqrt{2}}{2}$, så da får vi at

$$
\dfrac{\sqrt{3} / 2}{x} = \dfrac{\sqrt{2} / 2}{4}
$$

$$
\dfrac{\sqrt{3}}{x} = \dfrac{\sqrt{2}}{4}
$$

Har kan vi snu begge brøkene på hode slik at

$$
\dfrac{x}{\sqrt{3}} = \dfrac{4}{\sqrt{2}}
$$

Så ganger vi med $\sqrt{3}$ på begge sider, og da får vi at

$$
x = \dfrac{4\sqrt{3}}{\sqrt{2}} = \dfrac{4 \sqrt{3} \cdot \sqrt{2}}{\sqrt{2} \cdot \sqrt{2}} = \dfrac{4\sqrt{6}}{2} = 2\sqrt{6}
$$

Altså er $BC = 2\sqrt{6}$.

::::

:::::::::::::::
