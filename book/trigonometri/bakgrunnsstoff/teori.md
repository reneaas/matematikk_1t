# Pytagoras' setning, formlikhet og vinkler

En trekant er en geometrisk figur som består av tre hjørner og tre sider. Vi skal se på noen grunnleggende egenskaper ved trekanter, og vi skal se på noen viktige sammenhenger som er nyttige når vi skal jobbe med trigonometri.


## Vinkler

En **vinkel** er mål på hvor mange grader det er i en vinkelbue mellom to rette linjer.

:::::::::::::::{admonition} Vinkler
---
class: summary
---
En vinkel $v$ kan deles inn i tre typer:

Spiss vinkel
: Vinkelen $v$ er en **spiss vinkel** dersom $v \in \langle 0, 90 \degree \rangle$.

Rett vinkel
: Vinkelen $v$ er en **rett vinkel** dersom $v = 90 \degree$.

Stump vinkel
: Vinkelen $v$ er en **stump vinkel** dersom $v \in \langle 90\degree, 180 \degree \rangle$.

:::::::::::::::



## Spesielle trekanter

Vi skal starte med å se på to spesielle trekanter
* **Likesidet trekant**: En trekant der alle sidene er like lange.
* **Likebeint trekant**: En trekant der to av sidene er like lange.

:::::::::::::::{admonition} Spesielle trekanter
---
class: summary
---
To spesielle trekanter er

Likesidet trekant
: Alle sidene og vinklene i trekanten er like store. Hver vinkel er $60 \degree$.

Likebeint trekant
: To av sidene i trekanten er like store. De to vinklene som hører til de like sidene er også like store.

:::{figure} ./figurer/teori/spesielle_trekanter/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

:::::::::::::::



## Vinkler

En **vinkel** er et mål på hvor mange grader en vinkelbue spenner ut mellom to linjer. 



Først skal vi se på noen spesielle sammenhenger mellom vinkler. 

:::::::::::::::{admonition} Toppvinkler og samsvarende vinkler
---
class: summary
---

Toppvinkler
: Like vinkler på hver sin side av en linje som skjærer en annen linje. 

Samsvarende vinkler
: Like vinkler som dannes ved at to parallelle linjer skjæres av en tredje linje.

Se figuren nedenfor.

:::{figure} ./figurer/teori/vinkler/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

:::::::::::::::



:::::::::::::::{admonition} Utforsk 1
---
class: explore
---
Nedenfor vises en figur der en trekant er tegnet inn sammen med noen vinkler. 

Kan du bruke figuren til å bestemme vinkelsummen i en trekant?

:::{figure} ./figurer/utforsk/utforsk_1/figur_løsning.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::{admonition} Løsning
---
class: solution, dropdown
---
Vinklene $x$, $y$ og $z$ spenner ut en halvsirkel som betyr at $x + y + z = 180 \degree$.

Fra figuren kan også observere at:
1. $x$ og $b$ er samsvarende vinkler, så $x = b$.
2. $y$ og $c$ er toppvinkler, så $y = c$.
3. $z$ og $a$ er samsvarende vinkler, så $z = a$.

Men siden $x + y + z = 180 \degree$, så betyr dette også at $a + b + c = 180 \degree$. Dermed er vinkelsummen i en trekant $180 \degree$.

::::


:::::::::::::::

 
## Pytagoras' setning
En **rettvinklet** trekant er en trekant der én av vinklene er $90 \degree$.
Pytagoras' setning er en setning som forteller oss hvordan sidene i en rettvinklet trekant henger sammen. 

:::::::::::::::{admonition} Pytagoras' setning
---
class: summary
---
For en rettvinklet trekant gjelder

$$
(\mathrm{hypotenus})^2 = (\mathrm{katet}_1)^2 + (\mathrm{katet}_2)^2
$$

Se figuren til venstre nedenfor.

:::{figure} ./figurer/teori/pytagoras_setning/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Typisk navnsettes sidene i en rettvinklet trekant slik at den motstående siden til hjørne $A$ kalles for $a$, den motstående siden til hjørne $B$ kalles for $b$ og den motstående siden til $C$ kalles for $c$. Se figuren til høyre ovenfor. 

Da kan vi skrive ned Pytagoras' setning ved

$$
a^2 = b^2 + c^2
$$

:::::::::::::::

---


:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---
Bestem $x$ i trekanten nedenfor.

:::{figure} ./figurer/underveisoppgaver/oppgave_1/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 6.
$$
::::

:::::::::::::::






## Formlikhet

To trekanter er formlike dersom vi kan forminske, forstørre, rotere eller speile den ene trekanten slik at den passer nøyaktig på den andre trekanten.
I praksis kan vi ikke gjøre dette når vi skal undersøke om to trekanter er formlike. Heldigvis kan vi undersøke om to trekanter er formlike ved å sjekke om de oppfyller ett av tre kriterier.


:::::::::::::::{admonition} Formlike trekanter
---
class: summary
---
En trekant $\triangle ABC$ og en trekant $\triangle DEF$ er **formlike** dersom én av følgende betingelser er oppfylt:

**SSS** (side-side-side): 
: Forholdet mellom sidene i $\triangle ABC$ og de tilsvarende sidene i $\triangle DEF$ er én konstant.

$$
\dfrac{AB}{DE} = \dfrac{BC}{EF} = \dfrac{AC}{DF}
$$

**SVS** (side-vinkel-side): 
: Forholdet mellom to av sidene i $\triangle ABC$ med de tilsvarende sidene i $\triangle DEF$ er like, og vinkelen mellom disse sidene er lik i begge trekanter.

**VVV** (vinkel-vinkel-vinkel): 
: Alle vinkler i $\triangle ABC$ er like store som de tilsvarende vinklene i $\triangle DEF$.


<br>

De tre betingelsene ovenfor er **ekvivalente**.

Hvis $\triangle ABC$ og $\triangle DEF$ er formlike, så skriver vi $\triangle ABC \sim \triangle DEF$.


:::{figure} ./figurer/teori/formlikhet/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
viser to formlike trekanter $\triangle ABC$ og $\triangle DEF$. Her er $\angle A = \angle D$, $\angle B = \angle E$ og $\angle C = \angle F$. De tilsvarende sidene i trekantene er $AB$ og $DE$, sidene $BC$ og $EF$, og sidene $AC$ og $DF$.
:::


:::::::::::::::


---


:::::::::::::::{admonition} Underveisoppgave 2
---
class: check
---
Nedenfor vises to trekanter.

:::{figure} ./figurer/underveisoppgaver/oppgave_2/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar at $\triangle ABC \sim \triangle DEF$.


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi kan starte med å undersøke om VVV-kriteriet er oppfylt. I trekant $\triangle ABC$ er vinklene 

$$
\angle A = 63.43 \degree \and \angle B = 90 \degree \and \angle C = 180\degree - \angle A - \angle B
$$

Fra den siste delen av påstanden kan vi regne ut at

$$
\angle C = 180\degree - \angle A - \angle B = 180 \degree - 63.43 \degree - 90 \degree = 26.57 \degree. 
$$

Vi kan se at $\angle E = 90 \degree$ og $\angle F = 26.57 \degree$. Siden to av vinklene er like, betyr det automatisk at alle tre vinklene er like, så da er VVV-kriteriet er oppfylt. Dermed er 

$$
\triangle ABC \sim \triangle DEF.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem de ukjente sidelengdene i trekanten $\triangle DEF$.


::::{admonition} Løsning
---
class: solution, dropdown
---
Vi vet nå at $\triangle ABC \sim \triangle DEF$. Dermed er forholdet mellom to tilsvarende sider en konstant. De tilsvarende sidene i trekanten er $AB$ og $DE$, sidene $BC$ og $EF$, og sidene $AC$ og $DF$. Vi kan dermed skrive

$$
\dfrac{AB}{DE} = \dfrac{BC}{EF} = \dfrac{AC}{DF}.
$$

Fra $\triangle ABC$ har vi at $AC = \sqrt{5}$ og fra $\triangle DEF$ har vi at $DF = 2\sqrt{5}$. Dermed er 

$$
\dfrac{DF}{AC} = \dfrac{2\sqrt{5}}{\sqrt{5}} = 2.
$$

Dette betyr at alle sidene i $\triangle DEF$ er $2$ ganger så store som sidelengdene i $\triangle ABC$. Dermed er

$$
DE = 2\cdot AB = 2 \cdot 1 = 2 \and EF = 2\cdot BC = 2 \cdot 2 = 4. 
$$
::::

:::::::::::::



::::::::::::::




:::::::::::::::







