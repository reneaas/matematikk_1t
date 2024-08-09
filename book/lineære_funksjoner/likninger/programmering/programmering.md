# Løsning med programmering

:::{admonition} Læringsmål: lineære likninger med programmering
---
class: tip
---
Etter å ha gått gjennom denne delen, er målet at du skal kunne:
* Lese og tolke programmer som løser lineære likninger
* Justere og tilpasse programmer for å løse dine egne likninger
:::


## Numerisk løsning av likninger


Å løse likninger **numerisk** betyr å finne en tilnærmet tallverdi for løsningen ved hjelp av et program. For å bestemme løsningen av en likning numerisk, bruker man gjerne en systematisk metode for å gradvis nærme seg løsningen. En slik metode kalles for en **numerisk metode**. En numerisk metode kan oftest formuleres ved hjelp av en **algoritme**. En algoritme er en oppskrift som forteller oss nøyaktig hvilke steg vi skal gjøre for å utføre en bestemt numerisk metode.

Når man løser numeriske likninger, jobber man oftest med likninger som har null på høyre side. En slik likning kan skrives som $f(x) = 0$. Numerisk løsning av likninger handler derfor om å finne nullpunktene til en funksjon $f$.

::::{admonition} `abs`{l=python}-funksjonen
---
class: sidenote, margin
---
I programmet i {ref}`utforsk 1 <lineære-funksjoner-likninger-programmering-utforsk-1>` brukes `abs`{l=python}-funksjonen. Denne funksjonen gir absoluttverdien $|x|$ av et tall $x$. For eksempel er `abs(-3)`{l=python} lik 3. I programmet brukes `abs(f(x))`{l=python} som er det samme som å skrive $|f(x)|$. Dette gir absoluttverdien av funksjonsverdien!

::::


:::::{admonition} Utforsk 1
---
class: explore
name: lineære-funksjoner-likninger-programmering-utforsk-1
---
Under vises en kode som finner en tilnærmet verdi til løsningen av en lineær likning. Vi kaller dette for en *numerisk løsning*.

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_1.html 
---
:::

<!-- :::{raw} html
<div id="code-lineære-funksjoner-lineære-likninger-programmering-utforsk-1"></div>
<script type="text/javascript">
    const code = `
def f(x):
    return x - 3

x = -10
dx = 0.001

while abs(f(x)) > 0.00001:
    x = x + dx

print(f"{x = :.2f}")
`
    const Id = "lineære-funksjoner-lineære-likninger-programmering-utforsk-1";
    generateInteractiveCode(
        "code-lineære-funksjoner-lineære-likninger-programmering-utforsk-1",
        code,
        Id
    );
</script>
::: -->


<br>

Deloppgave 1
: Hvilken likning er det programmet løser? Hva er løsningen? <br> Sjekk om programmet får samme svar som du får ved å løse likningen for hånd.

<br>

Deloppgave 2
: Kan du forklare hva programmet gjør? Hva er prinsippet bak den numeriske metoden som brukes?

<br>

Deloppgave 3
: Bruk programmet til å løse likningen $2x - 4 = 0$. <br> Sjekk at svaret stemmer. 

:::::


Men hvis numerisk løsning handler om å løse likninger på formen $f(x) = 0$, hvordan kan man løse likninger numerisk når høyre siden ikke er null? 

Tenk deg at vi har likningen $f(x) = g(x)$ for to lineære funksjoner $f$ og $g$. Da kan vi skrive likningen som

$$
f(x) = g(x) \quad \Leftrightarrow \quad \underbrace{f(x) - g(x)}_{=h(x)} = 0 \quad \Leftrightarrow \quad h(x) = 0.
$$

Dermed vil løsningen av likningen $f(x) = g(x)$ være det samme som nullpunktet til funksjonen $h(x) = f(x) - g(x)$.

:::::{admonition} Utforsk 2
---
class: explore
---
Under vises et program som regner ut løsningen av en likning $f(x) = g(x)$. 

:::{raw} html
---
file: interaktiv_kode/utforsk/utforsk_2.html
---
:::

<br>

Deloppgave 1
: Hvilken likning er det programmet løser? Hva er løsningen? <br> Sjekk om programmet får samme svar som du får ved å løse likningen for hånd.


<br>

Deloppgave 2
: Endre programmet slik at det løser likningen $2x + 3 = -x + 6$. <br> Sjekk at svaret stemmer.


<br>

Deloppgave 3
: Endre programmet slik at det skriver ut verdien til `x`{l=python}. Endre startverdien til 



:::::