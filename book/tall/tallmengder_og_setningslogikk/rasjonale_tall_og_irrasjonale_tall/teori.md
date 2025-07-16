# De rasjonale tallene $\mathbb{Q}$ og de irrasjonale tallene $\mathbb{Q}^c$

:::::{admonition} Læringsmål
---
class: tip
---
* Kan beskrive mengden av de rasjonale tallene $\mathbb{Q}$.
* Kan forklare hva som kjennetegner de rasjonale tallene. 
* Kunne beskrive mengden av de irrasjonale tallene $\mathbb{Q}^c$ og hva som kjennetegner disse.
:::::

## De rasjonale tallene $\mathbb{Q}$

:::{margin}
Symbolet "$\mid$" leses som "slik at". Når vi skriver $\left\{ \dfrac{a}{b} \mid a, b \in \mathbb{Z}, \quad b \neq 0 \right\}$, så leser vi dette som "mengden av alle brøker $\dfrac{a}{b}$ slik at $a$ og $b$ er heltall og $b$ ikke er lik null". 
:::

:::::{theory} De rasjonale tallene

De rasjonale tallene er alle tall som kan skrives som en brøk $\dfrac{a}{b}$ der $a$ og $b$ er heltall og $b \neq 0$. De rasjonale tallene betegnes med symbolet $\mathbb{Q}$. Vi kan skrive mengden av de rasjonale tallene som

$$
\mathbb{Q} = \left\{ \dfrac{a}{b} \mid a, b \in \mathbb{Z}, \quad b \neq 0 \right\}
$$

:::::

De rasjonale tallene kan altså skrives som en brøk der telleren og nevneren er hele tall. Eksempler på rasjonale tall er $\dfrac{1}{2}$ og $\dfrac{-3}{4}$. Men også alle heltall er rasjonale tall, som for eksempel $5$ og $-2$. Dette er fordi vi kan skrive $5$ som $\dfrac{5}{1}$ og $-2$ som $\dfrac{-2}{1}$.

### Desimalrepresentasjon av rasjonale tall

Rasjonale tall kan også skrives som desimaltall. Det som kjennetegner desimalrepresentasjonen av rasjonale tall er de enten
1. har en endelig sifferutvikling
2. har en uendelig og repeterende sifferutvikling. Sifrene i desimalutviklingen repeterer seg i et fast mønster.



:::::{example} Eksempel 1
Det rasjonale tallet $\dfrac{1}{4}$ kan skrives som desimaltallet

$$
\dfrac{1}{4} = 0.25
$$

Dette er sant fordi $0.25 \cdot 4 = 1$. Sifferutviklingen er endelig og stopper etter to desimaler. 
:::::


Så tar vi et med repeterende sifferutvikling:

:::{margin}
Når sifrene i desimalrepresentasjonen repeterer seg for alltid, bruker vi enten "$\ldots$" eller en strek over tallene for å vise at de repeterer seg: 

$$
0.3333\ldots = 0.\overline{3}
$$

Hva som brukes er avhengig av hva som gjør det enklest å regne med. Vi skal her bruke streken over tallene for å gjøre det enklere å lese.
:::

:::::{example} Eksempel 2
Det rasjonale tallet $\dfrac{1}{3}$ kan skrives som 

$$
\dfrac{1}{3} = 0.3333\ldots = 0.\overline{3}
$$

:::::

Vi kan ha enda mer komplekse repeterende sifferutviklinger. 

:::::{example} Eksempel 3
La oss se på desimaltallet

$$
0.142142142\ldots = 0.\overline{142}
$$

Kan dette skrives som en brøk der telleren og nevneren er hele tall? Vi lar 

$$
x = 0.\overline{142}
$$

Siden sifrene $142$ gjentar seg med en periode på $3$, så kan vi gange begge sider med $1000$ for å flytte desimaltegnet tre plasser til høyre:


$$
1000x = 142.\overline{142}
$$

Hvis vi nå trekker fra $x$ på begge sider får vi:

$$
1000x - x = 142.\overline{142} - 0.\overline{142}
$$

Siden alle de repeterende sifrene etter desimaltegnet nå er like, så vil de nulle hverandre ut. Da får vi:

$$
999x = 142
$$

som betyr at 

$$
x = \dfrac{142}{999}
$$

så med andre ord var tallet et rasjonalt tall. 
:::::


:::::{exercise} Underveisoppgave 1 
Skriv følgende rasjonale tall som en brøk

$$
0.\overline{5216}
$$

::::{answer}
$$
0.\overline{5216} = \dfrac{5216}{9999}
$$
::::
:::::


## De irrasjonale tallene $\mathbb{Q}^c$

:::{margin}
Når vi skriver $\mathbb{Q}^c$ så betyr $c$ "komplement". Det vi mener med det er at $\mathbb{Q}^c$ er mengden av alle tall som ikke er rasjonale tall. Det kalles for den *komplementære mengden* til de rasjonale tallene og utfyller med å ta med alle tall som mangler i de rasjonale tallene.
:::

:::::{theory} De irrasjonale tallene
De irrasjonale tallene er alle tall som ikke kan skrives som en brøk $\dfrac{a}{b}$ der $a$ og $b$ er heltall og $b \neq 0$. De irrasjonale tallene betegnes med symbolet $\mathbb{Q}^c$. 
:::::

Et typisk kjennetegn på de irrasjonale tallene er at desimalrepresentasjonen av disse har en uendelig sifferutvikling som aldri får et repeterende mønster. Eksempler på irrasjonale tall er $\sqrt{2}$ og $\pi$. Men hvordan vet vi at $\sqrt{2}$ er et irrasjonalt tall?

:::::{example} Eksempel 4
For å vise at $\sqrt{2}$ er et irrasjonalt tall, skal vi anta det motsatte og vise at dette fører til en motsigelse. 

Vi antar at $\sqrt{2}$ er et rasjonalt tall. Da vet vi at det må finnes to heltall $a$ og $b$ slik at 

$$
\dfrac{a}{b} = \sqrt{2}
$$

og $a$ og $b$ har ingen felles faktorer. Hvis vi nå kvadrerer begge sider, så får vi

$$
\dfrac{a^2}{b^2} = 2
$$

Ganger vi med $b^2$ på begge sider, får vi

$$
a^2 = 2b^2
$$

Siden høyresiden inneholder en faktor $2$, betyr det at $a^2$ og $2b^2$ må begge være partall. Vi vet også at hvis $a^2$ er et partall, så må $a$ være et partall. Det betyr at vi kan skrive $a = 2n$ for et naturlig tall $n$. Vi setter inn dette i likningen som gir:

$$
(2n)^2 = 2b^2
$$

som vi kan videre forenkle til

$$
4n^2 = 2b^2
$$

deretter kan vi dele begge sider med $2$ som gir:

$$
2n^2 = b^2
$$

Men nå inneholder venstresiden en faktor $2$ som betyr at $b^2$ også må være et partall. Og da må også $b$ være et partall. Men det går jo ikke! Vi startet jo opprinnelig med at $a$ og $b$ var heltall som ikke hadde noen felles faktorer. Mens nå har vi kommet fram til at begge to må være partall som betyr at begge to må inneholde minst én faktor av $2$. Dette er en motsigelse, så antakelsen vår om at $\sqrt{2}$ er et rasjonalt tall må være feil. Da følger det at $\sqrt{2}$ er et irrasjonalt tall.


:::::


## Røtter
Røttene til tall dukker opp i mange sammenhenger. Spesielt vil vi møte på kvadratrøtter ofte. Det er derfor viktig at vi kan forenkle kvadratrøtter. 

:::{margin}
Husk at $y^2 = y \cdot y$
:::

:::::{theory} Kvadratrøtter
Kvadratroten til et tall $x$ skrives som $\sqrt{x}$ og er det tallet $y$ ganget med seg selv for å få $x$. Det vil si

$$
y^2 = x
$$
:::::


For eksempel er $\sqrt{4} = 2$ fordi $2^2 = 4$. Men ikke alle kvadratrøtter kan skrives som et naturlig tall. Som vi så over, så er noen kvadratrøtter irrasjonale tall. Når vi tar kvadratroten av et tall, så vil vi alltid enten få:
1. et naturlig tall
2. et irrasjonalt tall

Nedenfor skal vi se hvordan vi kan skrive en kvadratrot så enkelt som mulig ved å bruke primtallsfaktorisering og en egenskap ved kvadratrøtter.


:::{margin}
For eksempel er $\sqrt{4 \cdot 25} = \sqrt{4} \cdot \sqrt{25} = 2 \cdot 5 = 10$. Dette stemmer også med at $4\cdot 25 = 100$ og $\sqrt{100} = 10$.
:::

:::::{theory} Produktregelen for kvadratrøtter
Hvis vi tar kvadratroten av et produkt av to tall $A$ og $B$, så er dette det samme som å ta kvadratroten av hver faktor og gange det sammen:

$$
\sqrt{A \cdot B} = \sqrt{A} \cdot \sqrt{B}
$$
:::::

Nedenfor viser vi et eksempel der vi forenkler en kvadratrot ved hjelp av primtallsfaktorisering og produktregelen for kvadratrøtter.


:::{margin}
Vi kan alltid regne ut kvadratrøttene av kvadrattallene $1, 4, 9, 16, 25, \ldots$; Tall som ikke er kvadrattall vil derimot være irrasjonale tall som vi ikke kan regne ut kvadratroten av eksakt. Som i eksempelet til venstre, så er ikke $17$ et kvadrattall, så $\sqrt{17}$ er et irrasjonalt tall. Vi skriver da bare $\sqrt{17}$ som en "merkelapp" som vi i prinsippet kan regne ut en tilnærmet verdi for med kalkulator. 
:::

:::::{example} Eksempel 5
:::{figure} ./figurer/eksempler/eksempel_5.svg
---
width: 100%
class: no-click, adaptive-figure
align: right
---
:::

Fra faktortreet til høyre kan vi skrive

$$
68 = 2 \cdot 2 \cdot 17 = 4 \cdot 17
$$

Det betyr at $\sqrt{68}$ kan forenkles ved produktregelen som

$$
\sqrt{68} = \sqrt{4 \cdot 17} = \sqrt{4} \cdot \sqrt{17} = 2 \cdot \sqrt{17}
$$

Vi utelar gjerne gangetegnet i svaret, og bare skriver:

$$
\sqrt{68} = 2\sqrt{17}
$$
:::::

---

:::::{exercise} Underveisoppgave 2
Skriv $\sqrt{92}$ så enkelt som mulig.

::::{answer}
$$
\sqrt{92} = 2 \sqrt{23}
$$
::::

::::{solution}
:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2.svg
---
width: 100%
class: no-click, adaptive-figure
align: right
---
:::

Fra faktortreet til høyre kan vi skrive

$$
92 = 2 \cdot 2 \cdot 23 = 4 \cdot 23
$$

Så bruker vi produktregelen for kvadratrøtter:

$$
\sqrt{92} = \sqrt{4 \cdot 23} = \sqrt{4} \cdot \sqrt{23} = 2 \cdot \sqrt{23}
$$

Dermed er 

$$
\sqrt{92} = 2\sqrt{23}
$$
::::
:::::