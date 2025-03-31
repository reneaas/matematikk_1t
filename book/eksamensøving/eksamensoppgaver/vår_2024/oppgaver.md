# Vår 2024


## Del 1
> Oppgavene i del 1 skal løses **uten** hjelpemidler.


:::::::::::::::{admonition} Oppgave 1
---
class: check
---

:::{figure} ./figurer/del_1/oppgave_1/figur.svg
---
width: 80%
class: no-click
---
:::

Tom har arbeidet med trekanten ovenfor og påstår at $\tan u \cdot \tan v = 1$. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at Tom har rett.

:::::::::::::


:::::::::::::{tab-item} b
Avgjør om påstanden stemmer for alle rettvinklede trekanter med to spisse vinkler $u$ og $v$. 

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 2
---
class: check
---
Guri har utført to ulike polynomdivisjoner og påstår begge divisjonene viser at faktoriseringen nedenfor er riktig.

$$
2x^3 + 3x^2 - 11x - 6 = (2x^2 + 7x + 3)\cdot (x - 2)
$$


Hvilke to polynomdivisjoner kan hun ha utført?

Utfør de to polynomdivisjonene, og forklar at hver av dem viser at faktoriseringen er riktig.


:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 3
---
class: check
---
Sett opp en matematisk identitet med utgangspunkt i arealet av det grønne området.

:::{figure} ./figurer/del_1/oppgave_3/figur.svg
---
width: 80%
class: no-click
---
:::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 4
---
class: check 
---

Ada har laget programmet nedenfor. 

:::{code-block} python
---
linenos:
---
def f(x):
    return x ** 2 - 3 * x + 7

a = 0
b = 5

v = (f(b) - f(a)) / (b - a)

print(v)
:::

Hvilken verdi skrives ut når Ada kjører programmet, og hva forteller verdien?

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 5
---
class: check 
---
Figuren viser grafen til en funksjon $f$. 

:::{figure} ./figurer/del_1/oppgave_5/figur.svg
---
width: 80%
class: no-click
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f(x)$. 

:::::::::::::


:::::::::::::{tab-item} b
Løs ulikheten $f(x) > 12$. 

:::::::::::::

::::::::::::::


:::::::::::::::


---

## Del 2

> Oppgavene i del 2 kan løses med digitale hjelpemidler. Det er **viktig** at du øver på å føre oppgavene dine digitalt slik du ville gjort på en vaskeekte eksamen eller heldagsprøve! Du blir bare god på noe hvis du øver på det!


:::::::::::::::{admonition} Oppgave 1
---
class: check 
---
Tabellen nedenfor viser hvor mange bagetter en kantine har solgt hver av de siste sju ukene, og hvor stor overskudd salget har gitt.


| Solgte bagetter | 100 | 130 | 160 | 175 | 190 | 220 | 235 |
|------|---|---|---|---|---|---|---|
| Overskudd (kroner) | 1450 | 2300 | 3050 | 3365 | 3720 | 4140 | 4175 |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk opplysningene ovenfor til å vise at funksjonen $O$ gitt ved 

$$
O(x) = -0.09x^2 + 51.04x - 2776.98
$$

er en god modell for hvor stort overskuddet en uke blir når kantinen produserer og selger $x$ bagetter i løpet av uken.

:::::::::::::

:::::::::::::{tab-item} b
Hvor mange bagetter må kantinen produsere og selge i løpet av en uke, ifølge modellen O, for at overskuddet skal bli størst mulig? 

Hvor stort blir dette overskuddet?

:::::::::::::


:::::::::::::{tab-item} c
Bestem stigningstallet til den rette linjen som går gjennom punktene $(100, O(100))$ og $(200, O(200))$. Gi en praktisk tolkning av svaret du får.

:::::::::::::


:::::::::::::{tab-item} d
Bestem den momentane vekstfarten når $x = 235$. Gi en praktisk tolkning av svaret du får.

:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 2
---
class: check
---
Når en lysstråle går fra luft til vann, skifter den retning.

På figuren nedenfor står linjen $m$ vinkelrett på vannoverflaten og lysstrålen går fra å danne en vinkel $u$ med $m$ til å danne en vinkel $v$ med $m$.

Når lysstrålen går fra luft til vann, vil

$$
\sin u = 1.33 \cdot \sin v
$$

:::{figure} ./figurer/del_2/oppgave_2/figur.svg
---
width: 80%
class: no-click
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor står må vinkelen $u$ være for at vinkelen $v$ skal bli $39 \degree$? 

:::::::::::::


:::::::::::::{tab-item} b
Hva vil skje med vinkelen $v$ dersom vinkelen $u$ nærmer seg $90\degree$?

:::::::::::::


:::::::::::::{tab-item} c
Kan vinklene $u$ og $v$ bli like store?


:::::::::::::


::::::::::::::

Husk å begrunne svarene dine.


:::::::::::::::


---



:::::::::::::::{admonition} Oppgave 3
---
class: check
---
Du får vite følgende om trekant $ABC$

* $AB$ er $8$.
* $\angle A = 120\degree$. 
* Arealet av trekanten er $4\sqrt{3}$. 


Bestem lengdene av sidene $AC$ og $BC$ eksakt.


:::::::::::::::

---



:::::::::::::::{admonition} Oppgave 4
---
class: check
---
I denne oppgaven skal du arbeide med summer av oddetall. 

\begin{align*}
    S_1 &= 1 \\
    S_2 &= 1 + 3 \\
    S_3 &= 1 + 3 + 5 \\
    S_4 &= 1 + 3 + 5 + 7 \\
    S_5 &= 1 + 3 + 5 + 7 + 9 \\
    S_6 &= 1 + 3 + 5 + 7 + 9 + 11 \\
    \vdots & \quad \quad \vdots \quad \quad \vdots \quad \quad \vdots \quad \quad \vdots
\end{align*}


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som summerer og skriver ut summene $S_1, S_2, S_3, \ldots, S_{20}$.

:::::::::::::


:::::::::::::{tab-item} b
Beskriv sammenhengen du oppdager når du ser på summene som er skrevet ut.

Bruk figuren nedenfor til å argumentere for at sammenhengen må være riktig.


:::{figure} ./figurer/del_2/oppgave_4/figur.png
---
width: 80%
class: no-click
---
:::

:::::::::::::

::::::::::::::

:::::::::::::::

---


:::::::::::::::{admonition} Oppgave 5
---
class: check
---
Lufttrykk måles ofte i hektopascal (hPa). Jo høyere over vi befinner oss, jo lavere er lufttrykket. Lufttrykket ved havets overflate er ca. 1000 hPa.


Når lufttrykket er lavere enn 100 hPa, vil kokepunktet for vann være lavere enn $100 \degree \mathrm{C}$. Se tabellen nedenfor.

| Lufttrykk $\left(\mathrm{hPa}\right)$ | Kokepunkt for vann $\left(\degree \mathrm{C}\right)$ |
|------|---|
| $1000$ | $100$ |
| $500$ | $81.4$ |
| $200$ | $60.1$ |
| $80$ | $41.5$ |
| $40$ | $29$ |


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en modell $K$ på formen 

$$
K(x) = a \cdot x^b
$$

som tilnærmet viser sammenhengen mellom lufttrykket $x$ hPa og kokepunktet $K(x) \, \degree \mathrm{C}$. 

:::::::::::::

:::::::::::::{tab-item} b
Nedenfor vises en samtale mellom to elever:

Ari 
: Betyr dette at det ikke går an å få egg hardkokte oppe på et høyt fjell? 
: Et egg blir ikke hardkokt dersom temperaturen i vannet er lavere enn $85 \, \degree \mathrm{C}$.

Lisa
: Det kommer vel an på hvor høyt fjellet er?

Ari
: Jeg vil lage en modell som viser hvor høyt lufttrykket er $x$ kilometer over havets overflate. Jeg har lært at lufttrykket minker med ca. $12 \, \%$ per km. 

Lisa
: Jeg har lært at lufttrykket halveres for hver $5.5$ km. Jeg vil ta utgangspunkt i dette og lage en modell på samme form som den du lager, Ari.

---

**Lag modellene for Ari og Lisa.**

:::::::::::::


:::::::::::::{tab-item} c
Omtrent hvor høyt over havet er det mulig å få egg hardkokte?

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 6
---
class: check
---

:::{figure} ./figurer/del_2/oppgave_6/figur.svg
---
width: 80%
class: no-click
---
:::

Den rette linjen som er tegnet i koordinatsystemet ovenfor, er den deriverte av en funksjon $f$. Punktet $P(1, 2)$ ligger på grafen til $f$. 

Bestem likningen for tangenten til grafen til $f$ i punket $P$. 

Husk å argumentere for at svaret ditt er riktig.

:::::::::::::::


---


:::::::::::::::{admonition} Oppgave 7
---
class: check
---


:::::::::::::::



















