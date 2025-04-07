# Mengder som ulikheter

:::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive begrensede og ubegrensede mengder av reelle tall ved hjelp av ulikheter.
:::

Når vi har en mengde som består av reelle tall på en avgrenset del av tallinja, kan vi beskrive denne mengden ved hjelp av ulikheter. Dette kan både være begrensede og ubegrensede mengder. Betydningen av disse begrepene skiller seg litt fra hvordan de brukes for lister:

* **Begrensede mengder**: En del av tallinja som ligger mellom to tall $a$ og $b$.
* **Ubegrensede mengder**: En del av tallinja som kun kan være avgrenset av et tall $a$ nedenfra eller et tall $b$ ovenfra. Delen av tallinja strekker seg altså i det uendelige minst én retning.  

## Begrensede mengder

::::{admonition} Begrensede mengder som ulikheter
---
class: theory
---
Vi kan skrive en begrenset mengde av reelle tall på følgende måter:

| Ulikhet | Beskrivelse |
|:---:|---|
| $a \leq x \leq b$ | Alle reelle tall større enn eller lik $a$ og mindre enn eller lik $b$. |
| $a < x < b$ | Alle reelle tall større enn $a$ og mindre enn $b$. |
| $a \leq x < b$ | Alle reelle tall større enn eller lik $a$ og mindre enn $b$. |
| $a < x \leq b$ | Alle reellle tall større enn $a$ og mindre enn eller lik $b$. |

<br>

{numref}`fig-algebra-lister-ulikheter-intervaller-teori-begrenset-mengde` illustrerer grafisk delen av tallinja som er beskrevet av ulikhetene i tabellen.

:::{figure} ./figurer/teori/begrenset_mengde.svg
---
name: fig-algebra-lister-ulikheter-intervaller-teori-begrenset-mengde
width: 80%
---
illustrerer mengdene beskrevet av ulikhetene i tabellen over i rødt på tallinja. Avhengig av hvilket ulikhetstegn som er brukt er et endepunkt inkludert ($\leq$) eller ekskludert ($<$).
:::

::::

Vi går løs på et eksempel:

::::{admonition} Eksempel 1
---
class: example
---
I tabellen vises ulike eksempler på ulikheter og hvilke intervaller de tilsvarer:

| Ulikhet | Beskrivelse |
| :---: | --- |
| $-1 \leq x \leq 1$ | Alle reelle tall større enn eller lik $-1$ og mindre enn eller lik $1$.|
| $0 < x < 3$ | Alle reelle tall større enn $0$ og mindre enn $3$. |
| $2 \leq x < 5$ | Alle reelle tall større enn eller lik $2$ og mindre enn $5$. |
| $-4 < x \leq 1$ | Alle reelle tall større enn $-4$ og mindre enn eller lik $1$. |
::::

Så er det **din tur**!


::::{admonition} Underveisoppgave 1
---
class: check, full-width
---
Under vises ulikheter og beskrivelser som parvis hører sammen. Pusle sammen parene.

:::{raw} html
---
file: ./pair_puzzles/underveisoppgave_1.html
---
:::

::::


<!-- ::::{admonition} Underveisoppgave 1
---
class: check
---
Skriv av og fyll ut tabellen:

| Ulikhet | Beskrivelse |
|:---:|:---|
| $-1 < x \leq 3$ | |
| | Alle reelle tall $x$ mellom $2$ og $4$. Her er $2$ inkludert, men ikke $4$. |
| $0 \leq x < 2$ |  |
| | Alle reelle tall $x$ mellom $-3$ og $1$. Hverken $-3$ eller $1$ er inkludert |
| $-2 \leq x \leq 4$ |  | 

:::{admonition} Fasit
---
class: answer, dropdown
---

| Ulikhet | Beskrivelse |
|:---:|:---|
| $-1 < x \leq 3$ | Alle tall større enn $-1$ og mindre enn eller lik $3$. |
| $2 \leq x < -4$ | Alle reelle tall $x$ mellom $2$ og $4$. Her er $2$ inkludert, men ikke $4$. |
| $0 \leq x < 2$ | Alle reelle tall $x$ større enn eller lik $0$ og mindre enn $2$. |
| $-3 < x < 1$ | Alle reelle tall $x$ mellom $-3$ og $1$. Hverken $-3$ eller $1$ er inkludert. |
| $-2 \leq x \leq 4$ | Alle reelle tall $x$ som er større enn eller lik $-2$ og mindre enn eller lik $4$.  | 

:::

:::: -->


## Ubegrensede mengder 

Vi kan også bruke ulikheter til å beskrive ubegrensede mengder. Disse er enklere å skrive opp enn begrensede mengder.

:::{admonition} Begreper: nedad og oppad
---
class: sidenote, margin
---
Noen ganger i matematikk blir vi offer for ord som er litt gamle og ubrukte i dagligtalen. To slike ord er *nedad* og *oppad*. Men vi kan oversette dem slik:

Nedad
: Nedenfra

Oppad
: Ovenfra
:::

::::{admonition} Ubegrensede mengder som ulikheter
---
class: theory
---

Ubegrensende mengder som kan beskrives med ulikheter kommer i to varianter:

Oppad begrenset
: | Ulikhet | Beskrivelse |
    |:---:|:---|
    | $x < b$ | Alle reelle tall $x$ som er mindre enn $b$. |
    | $x \leq b$ | Alle reelle tall $x$ som er mindre enn eller lik $b$. |
    
    <br>

    Mengden er begrenset *ovenfra*, men ikke nedenfra. {numref}`fig-algebra-lister-ulikheter-intervaller-teori-oppad-begrenset-mengde` illustrerer grafisk hvilken del av tallinja det er snakk om.

    :::{figure} ./figurer/teori/oppad_begrenset_mengde.svg
    ---
    name: fig-algebra-lister-ulikheter-intervaller-teori-oppad-begrenset-mengde
    width: 90%
    ---
    viser en ubegrenset mengde som er oppad begrenset (i rødt). Avhengig av hvilket ulikhetstegn som er brukt er endepunktet inkludert ($\leq$) eller ekskludert ($<$).
    :::

<br>

Nedad begrenset
: | Ulikhet | Beskrivelse | 
    |:---:|:---|
    | $x > a$ |  Alle reelle tall $x$ som er større enn $a$. Skrives iblant som $a < x$. |
    | $x \geq a$ | Alle reelle tall $x$ som er større enn eller lik $a$. Skrives iblant som $a \leq x$. |

    <br>

    Mengden er begrenset nedenfra, men ikke ovenfra. {numref}`fig-algebra-lister-ulikheter-intervaller-teori-nedad-begrenset-mengde` illustrerer grafisk hvilken del av tallinja det er snakk om.

    :::{figure} ./figurer/teori/nedad_begrenset_mengde.svg
    ---
    name: fig-algebra-lister-ulikheter-intervaller-teori-nedad-begrenset-mengde
    width: 90%
    ---
    viser en ubegrenset mengde som er nedad begrenset (i rødt). Avhengig av hvilket ulikhetstegn som er brukt er endepunktet inkludert ($\leq$) eller ekskludert ($<$).
    :::



::::

Som vanlig, tar vi et eksempel for å illustrere teorien:


:::{admonition} Eksempel 2
---
class: example
---
I tabellen under vises noen eksempler på ubegrensede mengder beskrevet med ulikheter:

| Ulikhet | Beskrivelse |
| :---: | --- |
| $x \geq 2$ | Alle reelle tall større enn eller lik $2$. |
| $x \leq 4$ | Alle reelle tall mindre enn eller lik $4$. |
| $x > 0$ | Alle reelle tall større enn $0$. |
| $x < -3$ | Alle reelle tall mindre enn $-3$. |
| $-1 < x$ | Alle reelle tall større enn $-1$. |

:::


Så er det **din tur**!

::::{admonition} Underveisoppgave 2
---
class: check, full-width
---
Under vises ulikheter og beskrivelser som parvis hører sammen. Pusle sammen parene.

:::{raw} html
---
file: ./pair_puzzles/underveisoppgave_2.html
---
:::

:::: 

<!-- ::::{admonition} Underveisoppgave 2
---
class: check
---
Skriv av og fyll ut tabellen:

| Ulikhet | Beskrivelse |
|:---:|:---|
| $x \geq 0$ | |
| | Alle reelle tall $x$ mindre enn eller lik $-2$. |
| $x > 2$ |  |
| | Alle reelle tall $x$ mindre enn $-\dfrac{1}{2}$. |
| $x \leq 1$ |  |

:::{admonition} Fasit
---
class: answer, dropdown
---

| Ulikhet | Beskrivelse |
|:---:|:---|
| $x \geq 0$ | Alle reelle tall $x$ større enn eller lik $0$. |
| $x \leq -2$ | Alle reelle tall $x$ mindre enn eller lik $-2$. |
| $x > 2$ | Alle reelle tall $x$ større enn $2$. |
| $x < -\dfrac{1}{2}$  | Alle reelle tall $x$ mindre enn $-\dfrac{1}{2}$. |
| $x \leq 1$ | Alle reelle tall $x$ mindre enn eller lik $1$. |


:::

:::: -->
