# Polynomdivisjon


::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive og utføre polynomdivisjon. 
* Kunne forklare hva som er kvotient og rest i en polynomdivisjon, og forklare hva resten forteller oss om dividenden.
::::

Polynomdivisjon er en metode for å dele et polynom med et annet polynom og skrive det på en enklere form. 

:::::::::::::::{admonition} Eksempel 1
---
class: example
---
Vi skal regne ut 

$$
(3x^2 + 3x - 6) : (x + 2). 
$$

For å gjøre dette, følger vi disse stegene:


::::::::::::::{tab-set}
:::::::::::::{tab-item} Steg 1
Vi deler $3x^2$ fra $(3x^2 + 3x - 6)$ med $x$ fra $(x + 2)$ som gir $3x$. 

::::{figure} ./koder/eksempler/eksempel_1/stage_2.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::

:::::::::::::{tab-item} Steg 2
Vi ganger $3x$ med $(x + 2)$ som gir $3x^2 + 6x$. Deretter trekker vi fra dette fra $(3x^2 + 3x - 6)$: 

::::{figure} ./koder/eksempler/eksempel_1/stage_3.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::

:::::::::::::{tab-item} Steg 3
Vi trekker fra $(3x^2 + 3x - 6) - (3x^2 + 6x)$ som gir $-3x - 6$.

::::{figure} ./koder/eksempler/eksempel_1/stage_4.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::

:::::::::::::{tab-item} Steg 4
Vi deler $-3x$ fra $(-3x - 6)$ med $x$ fra $(x + 2)$ som gir $-3$.

::::{figure} ./koder/eksempler/eksempel_1/stage_5.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::

:::::::::::::{tab-item} Steg 5
Så ganger vi $-3$ med $(x + 2)$ som gir $-3x - 6$. Deretter trekker vi fra dette som gir $3x + 6$. Da sitter vi igjen med $0$.

::::{figure} ./koder/eksempler/eksempel_1/stage_7.svg
---
width: 60%
class: no-click
---
::::


:::::::::::::
::::::::::::::



Hele utregningen kan derfor skrives ned som: 


::::{figure} ./koder/eksempler/eksempel_1/eksempel_1.svg
---
width: 60%
class: no-click
---
::::

:::::::::::::::

