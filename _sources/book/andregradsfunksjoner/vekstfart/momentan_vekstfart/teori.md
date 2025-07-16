# Momentan vekstfart 

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive sammenhengen mellom momentan vekstfart og tangenter til en graf.
* Kunne bestemme likningen til tangenter til en andregradsfunksjon med digitale hjelpemidler.
* Kunne bestemme $f(x)$ ut ifra opplysninger om tangenter og punkter på grafen til en andregradsfunksjon.
:::::


I forrige delkapittel innførte vi en ny størrelse – gjennomsnittlig vekstfart – som lar oss sette tall på hvor mye funksjonsverdien til en andregradsfunksjon $f$ endrer seg i *gjennomsnitt* dersom vi øker $x$ med 1 i et intervall. Selv om dette gir oss noe informasjon om hvordan $f(x)$ endrer seg, kunne vi tenkt oss en størrelse som forteller oss hvor mye $f(x)$ endrer seg i *nøyaktig ett punkt* når vi øker $x$ med 1 – et slags mål på "hvor bratt er grafen til $f$ i punktet. 

Vi skal kalle dette for **momentan vekstfart** fordi den skal gi oss informasjon om hvor mye $f(x)$ endres *momentant* ("akkurat i") ett punkt når vi endrer på $x$. Men hvordan skal vi definere momentan vekstfart så det fanger opp denne ideen?


## Fra gjennomsnittlig vekstfart til momentan vekstfart

Momentan vekstfart skal vi tenke på som stigningstallet til en linje som "sneier" grafen til $f$ i et bestemt punkt. Stigningstallet skal svare til hvor "bratt" grafen er *akkurat* i dette punktet. 


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


## Bestemme momentan vekstfart

For å bestemme den momentane vekstfarten, trenger vi å finne opp ny matematikk som gir oss en sammenheng mellom stigningstallet til tangenter og en funksjon $f$. 



:::::::::::::::{explore} Utforsk
Nedenfor vises et program som gradvis regner ut gjennomsnittlig vekstfart over et mindre og mindre intervall. Ideen er at når størrelsen på intervallet blir veldig liten, så vil den gjennomsnittlige vekstfarten nærme seg den momentane vekstfarten. Animasjonen nedenfor viser ideen:

:::{figure} ./koder/animasjoner/media/videos/den_deriverte/1440p60/momentan_vekstfart.gif
---
width: 80%
class: no-click, manim-figure
---
:::


:::{interactive-code}
def f(x):
    return x**2 - 2*x + 1

x = 2
dx = 1
while dx > 0.00000001: # frem til vi har et veldig lite intervall
    gjennomsnittlig_vekstfart = (f(x + dx) - f(x)) / dx
    print(f"{gjennomsnittlig_vekstfart = }")
    
    dx = dx / 10
:::

:::::::::::::::
