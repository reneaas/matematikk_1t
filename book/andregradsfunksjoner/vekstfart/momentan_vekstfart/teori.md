# Momentan vekstfart 

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive sammenhengen mellom momentan vekstfart og tangenter til en graf.
* Kunne redegjøre for sammenhengen mellom momentan vekstfart og gjennomsnittlig vekstfart for andregradsfunksjoner, og bruke denne sammenhengen til å regne ut momentan vekstfart.
:::::


I forrige delkapittel innførte vi en ny størrelse – gjennomsnittlig vekstfart – som lar oss sette tall på hvor mye funksjonsverdien til en andregradsfunksjon $f$ ender seg i *gjennomsnitt* dersom vi øker $x$ med 1 i et intervall. Selv om dette gir oss noe informasjon om hvordan $f(x)$ ender seg, kunne vi tenkt oss en størrelse som forteller oss hvor mye $f(x)$ endrer seg *nøyaktig i ett punkt* når vi øker $x$ med 1 – et slags mål på "hvor bratt er grafen til $f$ i punktet. 

Vi skal kalle dette for **momentan vekstfart** fordi den skal gi oss informasjon om hvor mye $f(x)$ *momentant* ("akkurat i") ett punkt når vi endrer på $x$. Men hvordan skal vi definere momentan vekstfart så det fanger opp denne ideen?


## Fra gjennomsnittlig vekstfart til momentan vekstfart

Momentan vekstfart skal vi tenke på som stigningstallet til en linje som "sneier" grafen til $f$ i et bestemt punkt. Stigningstallet skal svaret til hvor "bratt" grafen er *akkurat* i dette punktet. 


:::::::::::::::{admonition} Momentan vekstfart
---
class: summary
---
Den **momentane vekstfarten** til en andregradsfunksjon $f$ er stigningstallet til en rett linje som går gjennom punktet $(x_1, f(x_1))$ på grafen til $f$ og som "sneier" grafen til $f$ i punktet. Linjen har samme stigningstall som hvor "bratt" grafen er momentant ("akkurat i") det punktet. 

Denne linjen kaller vi for en **tangent** og vi sier at linjen **tangerer** grafen til $f$ i $(x_1, f(x_1))$.  Se {numref}`fig-teori-andregradsfunksjoner-vekstfart-momentan-vekstfart-tangenter`.

:::{figure} ./figurer/teori/momentan_vekstfart.svg
---
name: fig-teori-andregradsfunksjoner-vekstfart-momentan-vekstfart-tangenter
class: no-click, adaptive-figure
width: 80%
---
viser grafen til en andregradsfunksjon $f$ og en tangent som "sneier" grafen til $f$ i punktet $(x_1, f(x_1))$. Stigningstallet til tangenten er den momentane vekstfarten til $f$ i punktet.
:::

:::::::::::::::

---

## Regne ut momentan vekstfart

Målet vårt nå er å finne en måte å regne ut momentan vekstfart for en andregradsfunksjon. Det er ikke opplagt hvordan vi skal finne stigningstallet til en linje som skal gå gjennom **ett** punkt på grafen til en andregradsfunksjon og så vidt "sneie" grafen.

Hvordan finner vi stigningstallet til tangenten (linjen) når vi kun har ett punkt å gå ut ifra?

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Vi skal skrive momentan vekstfart som:

$$
f'(x) = \text{"momentan vekstfart i  } x \text{"}
$$

Under vises en animasjon som illustrerer sammenhengen mellom stigningstallet til noen sekanter (gjennomsnittlig vekstfart) og stigningstallet til noen tangenter (momentan vekstfart) for en andregradsfunksjon.

1. Se på animasjonen. 
2. Prøv å finne en formel for den momentane vekstfarten $f'(x)$ uttrykt med den gjennomsnittlige vekstfarten til $f$ i et passende intervall.

::::{video}  ./koder/animasjoner/media/videos/momentan_vekstfart_og_gjennomsnittlig_vekstfart/1440p60/momentan_vekstfart_og_gjennomsnittlig_vekstfart.mp4
---
width: 95%
---
::::

:::::::::::::::

---

> Se på oppsummeringen etter Utforsk 1!

:::::::::::::::{admonition} Oppsummering: regne ut momentan vekstfart
---
class: summary, dropdown
---
Stigningstallet til en tangent i et punkt $(x, f(x))$ er det samme som stigningstallet til en sekant som går gjennom $(x - 1, f(x - 1))$ og $(x + 1, f(x + 1))$ på grafen til en andregradsfunksjon. 

Den momentane vekstfarten $f'(x)$ er derfor det samme som den gjennomsnittlige vekstfarten i intervallet $[x - 1, x + 1]$ der $x$ er **midtpunktet**:

$$
f'(x) = \dfrac{f(x + 1) - f(x - 1)}{2}
$$



:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---

I {numref}`fig-andregradsfunksjoner-vekstfart-momentan-vekstfart-underveisoppgave-1` vises grafen til $f(x) = (x - 1)(x + 4)$ og en sekant som går gjennom $(-1, f(-1))$ og $(1, f(1))$.

Bruk sekanten til å bestemme $f'(0)$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1.svg
---
name: fig-andregradsfunksjoner-vekstfart-momentan-vekstfart-underveisoppgave-1
width: 80%
class: no-click, adaptive-figure
---
viser grafen til $f(x) = (x - 1)(x + 4)$ og en sekant som går gjennom $(-1, f(-1))$ og $(1, f(1))$.
:::

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f'(0) = 3
$$
::::

::::{admonition} Løsning
---
class: dropdown, solution
---
$$
f'(0) = \dfrac{f(1) - f(-1)}{1 - (-1)} = \dfrac{0 - (-6)}{2} = \dfrac{6}{2} = 3
$$
::::

:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
En andregradsfunksjon er gitt ved 

$$
f(x) = x^2 - 2x - 3.
$$

Bestem $f'(2)$. 


::::{admonition} Fasit
---
class: dropdown, answer
---
$$
f'(2) = 2
$$
::::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vi regner ut gjennomsnittlig vekstfart i et intervall der $x = 1$ er midtpunktet:

$$
f'(2) = \dfrac{f(3) - f(1)}{3 - 1}
$$

Vi regner ut $f(3)$ og $f(1)$:

$$
f(3) = 3^2 - 2\cdot 3 - 3 = 0
$$

$$
f(1) = 1^2 - 2\cdot 1 - 3 = -4
$$

Vi setter dette inn i formelen for den gjennomsnittlige vekstfarten:

$$
f'(2) = \dfrac{0 - (-4)}{2} = \dfrac{4}{2} = 2
$$

som er den momentane vekstfarten til $f$ i $x = 2$.
::::

:::::::::::::::

---

## Likningen for en tangent

Nå som vi har en metode for å bestemme den momentane vekstfarten til en andregradsfunksjon, er vi også i stand til å bestemme likningen for en tangent til grafen til $f$. 

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
En andregradsfunksjon $f$ er gitt ved


$$
f(x) = (x + 1)^2 - 4
$$

Bestem likningen for tangenten som går gjennom $(1, f(1))$. 

::::{admonition} Løsning
---
class: solution
---
Vi bestemmer den momentane vekstfarten i $(1, f(1))$ siden dette gir oss stigningstallet til tangenten:

$$
f'(1) = \dfrac{f(2) - f(0)}{2 - 0} = \dfrac{f(2) - f(0)}{2}
$$

Vi regner ut funksjonsverdiene:

\begin{align*}
    f(2) &= (2 + 1)^2 - 4 = 9 - 4 = 5, \\
    \\
    f(0) &= (0 + 1)^2 - 4 = 1 - 4 = -3.
\end{align*}

Dermed er den momentane vekstfarten (stigningstallet til tangenten) gitt ved:

$$
a = f'(1) = \dfrac{f(2) - f(0)}{2} = \dfrac{5 - (-3)}{2} = \dfrac{8}{2} = 4.
$$

Vi bruker ettpunktsformelen for å bestemme likningen til tangenten i $(1, f(1))$, men da må vi først kjenne til $y$-koordinaten til punktet:

$$
f(1) = (1 + 1)^2 - 4 = 4 - 4 = 0.
$$

Dermed blir likningen til tangenten: 

\begin{align*}
    y - y_1 &= a(x - x_1) \\
    \\
    y - 0 &= 4(x - 1) \\
    \\
    y &= 4x - 4.
\end{align*}
::::
:::::::::::::::

---

:::::::::::::::{admonition} Underveisoppgave 3
---
class: check
---
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = (x + 1)(x - 3).
$$

Bestem likningen for tangenten i punktet $(0, f(0))$.

::::{admonition} Fasit
---
class: dropdown, answer
---
$$
y = -2x - 3
$$
::::
:::::::::::::::






