# Eksponentialfunksjoner


:::::{admonition} Læringsmål
---
class: tip
---
* Kunne veksle mellom prosentvis endring og vekstfaktor. 
* Kunne sette opp og tolke eksponentialfunksjoner i praktiske situasjoner.
* Kunne lage matematiske modeller ved bruk av regresjon. 
* Kunne skrive enkle programmer som bruker prosentvis endring og eksponentiell vekst. 
:::::

**Eksponentialfunksjoner** brukes til å beskrive situasjoner der noe vokser eller synker med en **fast prosentvis** endring. Denne prosentvise endringen kan vi uttrykke med en **vekstfaktor** som lar oss sette opp en funksjon som beskriver utviklingen.


## Prosent
Når vi snakker om prosent av noe, så mener vi gjerne en del av det hele. Prosent betyr "per hundre" eller "delt på hundre", og vi kan tolke prosenttegnet $\% = \dfrac{1}{100} = 0.01$. Det betyr at vi kan representere prosent på tre ulike måter:

:::::::::::::::{summary} Prosent: Representasjoner

$$
\underbrace{\dfrac{30}{100}}_{\text{brøk}} = \underbrace{0.3}_{\text{desimaltall}} = \underbrace{30 \%}_{\text{prosent}}
$$

Vi tolker prosenttegnet $\%$ som at det betyr  $\% = \dfrac{1}{100} = 0.01$ og at $30\%$ betyr $30 \cdot \dfrac{1}{100} = 0.3$.

:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen! Flere alternativer kan være riktig.


::::::::{quiz-2}
:::::::{quiz-question}
Hva er det samme som $20\%$?

::::::{quiz-answer}
---
correct: true
---
$$
0.2
$$
::::::

::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{20}{100}
$$
::::::


::::::{quiz-answer}
$$
\dfrac{2}{100}
$$
::::::


::::::{quiz-answer}
$$
0.02
$$
::::::

:::::::



:::::::{quiz-question}
Hva er det samme som $0.75$?

::::::{quiz-answer}
---
correct: true
---
$$
75\%
$$
::::::


::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{3}{4}
$$
::::::


::::::{quiz-answer}
$$
7.5 \%
$$
::::::


::::::{quiz-answer}
$$
\dfrac{75}{10}
$$
::::::



:::::::



:::::::{quiz-question}
Hva er det samme som $\dfrac{1}{4}$?


::::::{quiz-answer}
---
correct: true
---
$$
25\%
$$
::::::


::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{25}{100}
$$
::::::


::::::{quiz-answer}
$$
2.5 \%
$$
::::::



::::::{quiz-answer}
$$
0.20
$$
::::::




:::::::


:::::::{quiz-question}
Hva er det samme som $150\%$? 


::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{150}{100}
$$
::::::


::::::{quiz-answer}
---
correct: true
---
$$
1.5
$$
::::::


::::::{quiz-answer}
$$
0.15
$$
::::::


::::::{quiz-answer}
$$
\dfrac{15}{100}
$$
::::::


:::::::


:::::::{quiz-question}
Hva er det samme som $0.08$?


::::::{quiz-answer}
---
correct: true
---
$$
8 \%
$$
::::::


::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{8}{100}
$$
::::::


::::::{quiz-answer}
$$
\dfrac{8}{10}
$$
::::::


::::::{quiz-answer}
$$
80 \%
$$
::::::






:::::::



::::::::

:::::::::::::::


---

## Vekstfaktor

En **vekstfaktor** er det tallet vi må gange en opprinnelig verdi med for å få den nye verdien etter en prosentvis endring. 

Tenk deg at du har $1000$ kr på sparekonto og så øker beløpet med $5\%$. Pengene du har etter økningen er da 

$$
\underbrace{1000}_{100 \%} + \underbrace{0.05 \cdot 1000}_{5 \%} = \underbrace{(1 + 0.05)}_{105\%} \cdot 1000 = \textcolor{red}{1.05} \cdot 1000
$$

Tallet $1.05$ kaller vi for **vekstfaktoren** til endringen. 

Vi kan også forestille oss en situasjon der beløpet i stedet synker med $5\%$. Da har vi at det nye beløpet er

$$
\underbrace{1000}_{100 \%} - \underbrace{0.05 \cdot 1000}_{5 \%} = \underbrace{(1 - 0.05)}_{95\%} \cdot 1000 = \textcolor{red}{0.95} \cdot 1000
$$

Da ble vekstfaktoren $0.95$. 

Vi kan merke oss at når det er en økning, så blir vekstfaktoren et tall større enn $1$, og når det er en nedgang, så blir vekstfaktoren et positivt tall mindre enn $1$.

Mer generelt har vi følgende beskrivelse av vekstfaktorer:

:::::::::::::::{summary} Vekstfaktor og prosentvis endring
Når en størrelse øker eller minker med en prosent $p$, så er vekstfaktoren $V$ gitt ved

$$
V = 1 + p
$$

| $V$ | $p$ | Beskrivelse |
| --- | --- | --- |
| $V > 1$ | $p > 0$ | Økning |
| $0 < V < 1$ | $p < 0$ | Nedgang |

:::::::::::::::



---


:::::::::::::::{example} Eksempel 1
En vare øker med $15 \%$. Bestem vekstfaktoren til endringen.


::::{solution}
---
dropdown: 0
---
Her er $p = 15 \% = 0.15$ siden det er en økning på $15 \%$. Vekstfaktoren $V$ er da

$$
V = 1 + p = 1 + 0.15 = 1.15.
$$
::::

:::::::::::::::



---



:::::::::::::::{example} Eksempel 2
Prisen på en vare synker med $8 \%$. Bestem vekstfaktoren til endringen.

::::{solution}
---
dropdown: 0
---
Her er $p = -8 \% = -0.08$ siden det er en nedgang på $8 \%$. Vekstfaktoren $V$ er da

$$
V = 1 + p = 1 - 0.08 = 0.92
$$
::::
:::::::::::::::




---




:::::::::::::::{exercise} Underveisoppgave 2
Ta quizen!

::::::::{quiz-2}

:::::::{quiz-question}
Hva blir vekstfaktoren ved $10\%$ økning?


::::::{quiz-answer}
---
correct: true
---
$$
1.1
$$
::::::


::::::{quiz-answer}
$$
1.01
$$
::::::


::::::{quiz-answer}
$$
0.9
$$
::::::


::::::{quiz-answer}
$$
0.99
$$
::::::



:::::::


:::::::{quiz-question}
Hva er vekstfaktoren ved $9\%$ nedgang?


::::::{quiz-answer}
---
correct: true
---
$$
0.91
$$
::::::


::::::{quiz-answer}
$$
1.09
$$
::::::


::::::{quiz-answer}
$$
-0.91
$$
::::::

::::::{quiz-answer}
$$
-0.09
$$
::::::


:::::::


:::::::{quiz-question}
Hva er den prosentvise endringen hvis vekstfaktoren er $1.02$?


::::::{quiz-answer}
---
correct: true
---
$$
2\%
$$
::::::


::::::{quiz-answer}
$$
20\%
$$
::::::

::::::{quiz-answer}
$$
102\%
$$
::::::


::::::{quiz-answer}
$$
-2\%
$$
::::::


:::::::


:::::::{quiz-question}
Hva er den prosentvise endringen hvis vekstfaktoren er $0.70$?


::::::{quiz-answer}
---
correct: true
---
$$
-30\%
$$
::::::


::::::{quiz-answer}
$$
30 \%
$$
::::::


::::::{quiz-answer}
$$
70 \%
$$
::::::


::::::{quiz-answer}
$$
-70\%
$$
::::::




:::::::


:::::::{quiz-question}
Hva er den prosentvise endringen hvis vekstfaktoren er $1.25$?

::::::{quiz-answer}
---
correct: true
---
$$
25\%
$$
::::::

::::::{quiz-answer}
$$
125\%
$$
::::::

::::::{quiz-answer}
$$
-25\%
$$
::::::

::::::{quiz-answer}
$$
0.25\%
$$
::::::

:::::::


:::::::{quiz-question}
Hva er den prosentvise endringen hvis vekstfaktoren er $0.85$?

::::::{quiz-answer}
---
correct: true
---
$$
-15\%
$$
::::::

::::::{quiz-answer}
$$
15\%
$$
::::::

::::::{quiz-answer}
$$
-85\%
$$
::::::

::::::{quiz-answer}
$$
85\%
$$
::::::




:::::::





::::::::


:::::::::::::::


---



## Eksponentiell vekst fremover og bakover

La oss forestille oss en vare som koster $100$ kr i dag, og som øker med $10\%$. Da er vekstfaktoren $1.10$. Da vil verdien etter endringen være gitt ved 

$$
\underbrace{100}_{\mathrm{Startverdi}} \cdot \underbrace{1.10}_{\mathrm{Vekstfaktor}} = \underbrace{110}_{\mathrm{Sluttverdi}}
$$

Når vi skal finne verdien *etter* en endring ganger vi altså vekstfaktoren med startverdien for å få sluttverdien.


:::::::::::::::{summary} Eksponentiell vekst fremover
La $G$ være startverdien og $V$ være vekstfaktoren for en prosentvis endring. Da er sluttverdien $N$ etter endringen gitt ved

$$
N = G \cdot V
$$
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
En vare koster $300$ kr. Prisen øker med $20\%$.

Bestem et uttrykk for prisen etter økningen.


::::{answer}
$$
300 \cdot 1.20
$$
::::


:::::::::::::::



---



La oss nå forestille oss at en vare opprinnelig kostet $G$ kr, og så sank prisen med $20 \%$. Da kostet den 400 kr. For å finne startverdien $G$ kan vi da sette opp likningen

$$
G \cdot 0.80 = 400 \liff G = \dfrac{400}{0.80} = 500.
$$


Altså deler vi med vekstfaktoren når vi ønsker å regne oss *bakover* for å finne startverdien.

:::::::::::::::{summary} Eksponentiell vekst bakover
La $N$ være sluttverdien og $V$ være vekstfaktoren for en prosentvis endring. Da er startverdien $G$ før endringen gitt ved

$$
G = \dfrac{N}{V}
$$

:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 4
En jakke er på tilbud med $30\%$ rabatt, og prisen er nå $700$ kr.

Bestem et uttrykk for den opprinnelige prisen. 


::::{answer}
$$
\dfrac{700}{0.70}
$$
::::

:::::::::::::::



## Eksponentiell vekst i flere steg

La oss forestille oss at en vare først koster $100$ kr, så øker den med $10\%$ og så synker den med $10\%$. Hva er prisen på varen etter disse to endringene? Vi kan beregne verdien etter hver endring hver for seg. 

Først har vi at 

$$
100 \cdot \underbrace{1.10}_{10\% \, \mathrm{økning}} = 110
$$

Deretter skal varen synke med $10\%$, så vi har at

$$
110 \cdot \underbrace{0.90}_{10\% \, \mathrm{nedgang}} = 99.
$$

Den samlede regningen vi har gjort fra den opprinnelige verdien er da

$$
\underbrace{100}_{\mathrm{Startverdi}} \cdot \underbrace{ \underbrace{1.10}_{10\% \, \mathrm{økning}} \cdot\underbrace{0.90}_{10\% \, \mathrm{nedgang}}}_{\mathrm{Samlet \, vekstfaktor}} = \underbrace{99}_{\mathrm{Sluttverdi}}
$$

Vi kan altså regne ut en **samlet** vekstfaktor for alle endringene ved å gange vekstfaktorene sammen. Deretter ganger vi den samlede vekstfaktoren med startverdien for å få sluttverdien.

:::::::::::::::{summary} Eksponentiell vekst i flere steg
Når en størrelse gjennomgår $n$ prosentvise endringer med vekstfaktorer $V_1, V_2, \ldots, V_n$, så er den samlede vekstfaktoren $V$ gitt ved

$$
V = V_1 \cdot V_2 \cdot \ldots \cdot V_n
$$

La $G$ være startverdien. Da er sluttverdien $N$ gitt ved 

$$
N = G \cdot V = G \cdot V_1 \cdot V_2 \cdot \ldots \cdot V_n
$$

Hvis de prosentvise endringene er like, altså at $V_1 = V_2 = \ldots = V_n = V$, så vil sluttverdien være gitt ved 

$$
N = G \cdot V^n
$$

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 5
En vare koster $500$ kr. Prisen øker først med $20\%$, og så synker den med $10\%$.

Bestem et uttrykk for prisen etter disse to endringene.

::::{answer}
$$
500 \cdot 1.2 \cdot 0.9
$$
::::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 6
Lønna til Anna har økt med $5\%$ per år i $3$ år. Lønnen til Anna var opprinnelig $400~000$ kr. 

Bestem et uttrykk for lønnen til Anna etter de $3$ årene.


::::{answer}
$$
400~000 \cdot 1.05^3
$$
::::
:::::::::::::::



---


## Eksponentialfunksjoner
Vi kan generalisere mønsteret vi har kommet fram til så langt til å lage oss en funksjon som beskriver en eksponentiell vekst. En slik funksjon kaller vi for en **eksponentialfunksjon**.

En eksponentialfunksjon $f(x)$ består av to byggesteiner: 
1. En **startverdi** $a$ som forteller oss hvor den eksponentielle veksten starter.
2. En **vekstfaktor** $b$ som forteller oss hvor stor den prosentvise veksten er når vi øker $x$ med $1$.

> Vi bruker ordet "prosentvis vekst" både når det er en økning og når det er en nedgang. 


La oss lage oss en oversikt over funksjonstypen:

:::::::::::::::{summary} Eksponentialfunksjoner
En eksponentialfunksjon $f$ kan skrives på formen

$$
f(x) = a \cdot b^x
$$

der 

* $a$ er **startverdien** til den eksponentielle veksten når $x = 0$ (skjæring med $y$-aksen).
* $b$ er **vekstfaktoren** som forteller oss hvor mye $f(x)$ vokser eller synker når $x$ øker med $1$.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{plot}
width: 100%
function: 1 * 2**x, blue
function: 1 * 0.5**x, red
ymin: -1
ymax: 6
xmax: 5
xmin: -5
text: 3.5, 4, "$b > 1$", center-center, bbox 
text: -3.5, 4, "$0 < b < 1$", center-center, bbox 
annotate: (2, 1), (0, 1), "$f(0) = a$", 0
point: (0, 1)
ticks: off
fontsize: 26
:::

:::{interactive-graph} 
width: 100%
interactive-var: a, 0, 5, 50
interactive-var: b, 0, 5, 50
interactive-var-start: a=1, b=2
xmin: -6
xmax: 6
ymin: -1
ymax: 6
function: a * b**x
point: (0, a)
text: 0, a, "(0, {a :.2f})", top-left
fontsize: 24
:::

::::


:::::::::::::::


---

:::::::::::::::{example} Eksempel 3
Nedenfor ser vi to eksempler på eksponentialfunksjoner. 


::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 26
---
:::{plot}
function: 1 * 2**x, f
ymin: -1
ymax: 6
xmax: 6
xmin: -6
text: -3.5, 4, "$f(x) = 1 \cdot 2^x$", center-center, bbox
:::

:::{plot}
function: 4 * 0.5**x, g
ymin: -1
ymax: 6
xmax: 6
xmin: -6
text: -3.5, 4, "$g(x) = 4 \cdot \left(\displaystyle \frac{1}{2}\right)^x$", center-center, bbox
:::

::::



:::::::::::::::


---


La oss se mer konkret på hvordan eksponentialfunksjoner kan brukes til å beskrive praktiske situasjoner.


:::::::::::::::{example} Eksempel 4
Du setter inn $1000$ kr på en sparekonto som gir $5\%$ rente per år. 

Bestem en funksjon $f(x)$ som gir beløpet du har på kontoen etter $x$ år.


::::{solution}
---
dropdown: 0
---
Siden vi setter inn $1000$ kr, så er startverdien 

$$
a = 1000.
$$ 

Siden renten er $5\%$ per år, så er vekstfaktoren 

$$
b = 1 + 0.05 = 1.05.
$$

Det betyr at funksjonen $f(x)$ som beskriver beløpet på kontoen etter $x$ år er

$$
f(x) = 1000 \cdot 1.05^x
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 7
En bil blir kjøpt for 200 000 kr, og verdien synker med 15\% per år.

Sett opp et funksjonsuttrykk $f(x)$ som gir verdien av bilen etter $x$ år.

::::{answer}
$$
f(x) = 200 \, 000 \cdot 0.85^x
$$
::::


::::{solution}
Startverdien er $200 \, 000$ kr siden dette er det bilen blir kjøpt for, så 

$$
a = 200 \, 000.
$$

Verdien til bilen synker med $15 \%$ hvert år som betyr at vekstfaktoren er

$$
b = 100\% - 15\% = 85\% = 0.85.
$$

Dermed er funksjonen $f(x)$ som beskriver verdien av bilen etter $x$ år gitt ved

$$
f(x) = a \cdot b^x = 200 \, 000 \cdot 0.85^x.
$$
::::


:::::::::::::::



---


## Negative eksponenter
Når vi definerte eksponentialfunksjonen $f(x)$, så sa vi at $a = f(0)$ representerte startverdien og at $b$ var vekstfaktoren som forteller oss hvor mye $f(x)$ vokser eller synker når $x$ øker med $1$. Men funksjonsuttrykket kan helt fint brukes til å regne ut $f(x)$ for negative $x$-verdier også. Å regne ut $f(x)$ for negative $x$-verdier kan tolkes som å regne seg bakover i tid. For eksempel, hvis vi har at


$$
f(x) = 100 \cdot 0.9^x
$$

betyr det at at verdien $2$ år *før* "startverdien" må være

$$
f(-2) = 100 \cdot 0.9^{-2}
$$

Dette bør være et helt rimelig uttrykk å regne med siden det er helt rimelig å tenke at noe kan ha hatt en verdi i fortiden, men det er litt uklart hva det vil si å opphøye et tall med en negativ eksponent. Det vi skal *mene* med å opphøye med en negativ eksponent er at

$$
0.9^{-2} = \dfrac{1}{0.9^2}
$$

Vi så tidligere at når vi ønsket å regne oss *bakover* fra en sluttverdi, så delte vi med vekstfaktoren. Siden det å sette inn en negativ $x$-verdi må svare til å regne oss bakover (gjerne bakover i *tid*), så er det rimelig å **definere** det som følger:


:::::::::::::::{summary} Negative eksponenter
La $b$ være et grunntall. Da vil en potens med negativ eksponent $-x$ være definert ved

$$
b^{-x} = \dfrac{1}{b^x}
$$

Når vi regner ut $b^{-x}$ betyr dette altså det samme som å dele med $b^x$. 

:::::::::::::::


---


:::::::::::::::{example} Eksempel 5
Du har satt inn et innskudd på en bankkonto som gir $5\%$ rente per år. Etter $3$ år har du $20~000$ kr på kontoen. 

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hvor mye du satte inn i utgangspunktet?


::::{grid} 1 1 2 3
---
gutter: 2
---
:::{grid-item-card}
1)
^^^
$$
20~000 \cdot 0.95^3
$$
:::

:::{grid-item-card}
2)
^^^
$$
\dfrac{20~000}{1.05^3}
$$
:::

:::{grid-item-card}
3)
^^^
$$
20~000 \cdot 1.05^3
$$
:::

:::{grid-item-card}
4)
^^^
$$
20~000 \cdot 0.95^{-3}
$$
:::


:::{grid-item-card}
5)
^^^
$$
\dfrac{20~000}{0.95^3}
$$
:::


:::{grid-item-card}
6)
^^^
$$
20~000 \cdot 1.05^{-3}
$$
:::
::::


::::{solution}
---
dropdown: 0
---
Siden innskuddet skal vokse med $5\%$ per år, så er vekstfaktoren $b = 1.05$. Da har vi at innskuddet vi satt inn må oppfylle

$$
20~000 \cdot 1.05^{-3} = 20~000 \cdot \dfrac{1}{1.05^3} = \dfrac{20~000}{1.05^3}
$$

Dermed vil uttrykk 2) og 6) kunne brukes til å finne ut hvor mye du satte inn i utgangspunktet.
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 8
Ta quizen nedenfor. Flere alternativer kan være riktige.


::::::::{quiz-2}
:::::::{quiz-question}
En vare har økt med $4 \%$ over 5 år. Varen koster nå $500$ kr.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hva varen kostet for noen år siden?


::::::{quiz-answer}
---
correct: true
---
$$
500 \cdot 1.04^{-5}
$$
::::::


::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{500}{1.04^5}
$$
::::::


::::::{quiz-answer}
$$
500 \cdot 0.96^5
$$
::::::

::::::{quiz-answer}
$$
\dfrac{500}{0.96^5}
$$
::::::

:::::::

:::::::{quiz-question}
En bakteriekultur dobles hver time. Etter 6 timer er det 12 800 bakterier.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hvor mange bakterier det var i utgangspunktet?

::::::{quiz-answer}
---
correct: true
---
$$
12~800 \cdot 2^{-6}
$$
::::::

::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{12~800}{2^6}
$$
::::::

::::::{quiz-answer}
$$
12~800 \cdot 0.5^6
$$
::::::

::::::{quiz-answer}
$$
\dfrac{12~800}{0.5^6}
$$
::::::

:::::::

:::::::{quiz-question}
Mengden radioaktivt stoff minker med 8% per dag. Etter 10 dager er det 500 gram igjen.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hvor mye stoff det var for 10 dager siden?

::::::{quiz-answer}
---
correct: true
---
$$
500 \cdot 0.92^{-10}
$$
::::::

::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{500}{0.92^{10}}
$$
::::::

::::::{quiz-answer}
$$
500 \cdot 1.08^{10}
$$
::::::

::::::{quiz-answer}
$$
500 \cdot 0.08^{-10}
$$
::::::

:::::::

:::::::{quiz-question}
En befolkning vokser med 3% per år. Etter 8 år er befolkningen 150 000 mennesker.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hvor mange mennesker det var for 8 år siden?

::::::{quiz-answer}
---
correct: true
---
$$
150~000 \cdot 1.03^{-8}
$$
::::::

::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{150~000}{1.03^8}
$$
::::::

::::::{quiz-answer}
$$
150~000 \cdot 0.97^8
$$
::::::

::::::{quiz-answer}
$$
\dfrac{150~000}{0.97^8}
$$
::::::

:::::::

:::::::{quiz-question}
En bil minker i verdi med 12% per år. Etter 4 år er bilen verdt 88 000 kr.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hva bilen kostet i utgangspunktet?

::::::{quiz-answer}
---
correct: true
---
$$
88~000 \cdot 0.88^{-4}
$$
::::::

::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{88~000}{0.88^4}
$$
::::::

::::::{quiz-answer}
$$
88~000 \cdot 1.12^4
$$
::::::

::::::{quiz-answer}
$$
\dfrac{88~000}{1.12^4}
$$
::::::

:::::::

:::::::{quiz-question}
En investering øker med 6% per kvartal. Etter 12 kvartaler er investeringen verdt 45 000 kr.

Hvilket eller hvilke av uttrykkene nedenfor kan brukes til å finne ut hva den opprinnelige investeringen var?

::::::{quiz-answer}
---
correct: true
---
$$
45~000 \cdot 1.06^{-12}
$$
::::::

::::::{quiz-answer}
---
correct: true
---
$$
\dfrac{45~000}{1.06^{12}}
$$
::::::

::::::{quiz-answer}
$$
45~000 \cdot 0.94^{12}
$$
::::::

::::::{quiz-answer}
$$
\dfrac{45~000}{0.94^{12}}
$$
::::::

:::::::

::::::::


:::::::::::::::



---



## Programmering av eksponentiell vekst

Vi kan bruke programmering til å regne med eksponentiell vekst. La oss se på et eksempel.


:::::::::::::::{example} Eksempel 6
Du setter inn $1000$ kr på en sparekonto som gir $5\%$ rente per år. 

Lag et program som regner ut på kontoen etter $5$ år.



::::{solution}
---
dropdown: 0
---
Vi har at startverdien er $a = 1000$ og at vekstfaktoren er $b = 1.05$. Da har vi at 

En algoritme for å regne ut beløpet på kontoen etter $5$ år kan da være:

* Start med $s = 1000$.
* for $n = 1, 2, \ldots, 5$:
    * Sett $s = s \cdot 1.05$

Programmet nedenfor regner ut beløpet på kontoen etter $5$ år:

:::{interactive-code}
s = 1000                # startverdi
for n in range(1, 6):   # for år 1, 2, 3, 4, 5
    s = s * 1.05        # Øk sparebeløpet med 5%

print(f"{s = :.2f} kr")
:::
::::


:::::::::::::::


I eksempelet ovenfor kunne vi i prinsippet bare regnet ut $1000 \cdot 1.05^5$ direkte, så det kan virke litt *unødvendig* å bruke programmering her.

Men la oss forestille oss at vi i stedet skal sette inn et innskudd på starten av hvert år. Det er her programmering kan skinne. 


:::::::::::::::{example} Eksempel 7
Du skal sette inn et innskudd på $1000$ kr på en sparekonto på starten av hvert år. Renten per år er på $5\%$. 

Hvor mye penger har du på kontoen etter $10$ år?

::::{solution}
---
dropdown: 0
---
Her har vi at startverdien er $a = 1000$ og at vekstfaktoren er $b = 1.004$. Siden vi setter inn et innskudd hver måned, kan vi ikke bare bruke én eksponentiell modell for å regne ut beløpet på kontoen over tid. I stedet må vi bruke algoritmen nedenfor:

* Start med $s = 0$.
* For $n = 1, 2, \ldots, 10$ år:
    * Sett $s = s + 1000$ for å legge til det nye innskuddet
    * Sett $s = s \cdot 1.05$ for å øke sparebeløpet med 5% rente
    

Programmet nedenfor bruker algoritmen ovenfor.

:::{interactive-code}
s = 0
for n in range(1, 11):  # for år 1, 2, ..., 10
    s = s + 1000        # Legg til det nye innskuddet
    s = s * 1.05        # Øk sparebeløpet med 5% rente

print(f"{s = :.2f} kr")
:::

::::


:::::::::::::::
