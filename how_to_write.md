# Guide for skriving

## Bygge en Jupyterbook

For å bygge en Jupyterbook, skriv følgende kommando i terminalen i **root** av directory:

```bash
jb build . --all
```

html-kode for hele boka genereres og en link til root i html-filene skrives ut i terminalen. 
html-koden vil ligge i `_build/html` mappen. Du må åpne `index.html` i nettleseren (på Windows, anyway) for å se på den lokale versjonen av boka. Denne pushes ikke opp til skyen - GitHub bygger boka når du pusher til skyen automatisk.

## git stuff

Viktig sjekkliste:
1. Jobb alltid på din *egen branch* lokalt. Merge til `main` når du er ferdig med noe fra Github.com ved å legge inn en pull request og merge i skyen. 
2. Pull endringer fra skyen hver gang du setter i gang å jobbe for å redusere antall merge konflikter.
3. Skriv en beskrivende commit message når du legger inn en ny commit. 


### Viktige kommandoer

|Kommando|Beskrivelse|
|:---:|:---|
|`git pull`| Henter endringer fra skyen|
|`git pull origin branch`| Puller nytt content fra en branch i skyen. Merger endringene i den branchen med dine lokale endringer. Kan gjøres i stedet for å merge i skyen (men kun anbefalt når du er blitt litt dreven på git). |
|`git add --all`| Legger til nye endringer som er gjort i alle filer. |
|`git commit -m "Din beskrivende melding"`| Committer endringer |
|`git push`| Pusher endringer til skyen |
|`git branch` | Viser alle branches, inkludert hvilken du jobber på. |
|`git checkout branchnavn`| Bytter til en annen branch |
|`git status`| Viser status på filer som er endret, lagt til, osv. |

### Merge konflikter
Hvis det oppstår en merge-konflikt, er dette **hensikten med git** og er ønsket atferd. For å løse merge-konflikter lokalt, må du åpne opp filene og identifisere hvor i filen konflikten er (git markerer dette og forteller deg hvilken versjon av innholdet som er din egen, og hvilken som er hentet fra skyen). Du må manuelt redigere filene for å fjerne konflikten, og så er det bare å committe endringene og pushe opp til skyen. 
Typisk når du merger, gjør du det fra skyen som medfører at du kanskje må fikse merge-konflikter der oppe. Er du usikker på hva du må gjøre, spør en kollega så du ikke sletter noe ved et uhell.



## Matematikk

### Vanlige kommandoer

|Type| Syntaks|
|:---:|:---:|
|Inline| `$a^2 + b^2 = c^2$`|
|Blokk| `$$a^2 + b^2 = c^2$$`|
|Likningssystem| `\begin{align} x + y &= 2 \\ x - y &= 0 \end{align}`|

### Spesielle matematikksymboler i LaTeX

| Tegn | Syntaks |
|:---:|:---:|
|$\land$| `\land`|
|$\lor$| `\lor`|
|$\Leftrightarrow$| `\Leftrightarrow`|
|$\Rightarrow$| `\Rightarrow`|
|$\Leftarrow$| `\Leftarrow`|
|$\Updownarrow$| `\Updownarrow`|
|$\forall$| `\forall`|
|$\langle a , b\rangle$| `\langle a, b \rangle`|
|$\in$| `\in`|
|$\notin$| `\notin`|
|$\subset$| `\subset`|
|$\subseteq$| `\subseteq`|
|$\cup$| `\cup`|
|$\cap$| `\cap`|
|$\emptyset$| `\emptyset`|
|$\mathbb{N}$| `\mathbb{N}`|
|$\mathbb{Z}$| `\mathbb{Z}`|
|$\mathbb{Q}$| `\mathbb{Q}`|
|$\mathbb{R}$| `\mathbb{R}`|
|$\to$|`\to`|
|$\gets$ |`\gets`|
| \{ a, b \} |`\{a, b\}`|
|$\dfrac{a}{b}$ |`\dfrac{a}{b}`|
|$a\cdot b$ |`a\cdot b`|
|$a_1, a_2, \ldots, a_n$ | `a_1, a_2, \ldots, a_n`|

### Likningnummerering
For å nummerere likninger, brukes følgende syntaks:
````markdown
$$
x^3 + y^2 - 3x + 4y = 0,
$$ (eq:likning1)
````

Så kan man referere til likningen ved å skrive 

````markdown
Som vi ser i likning {eq}`eq:likning1`, så er [...]
````

## Sette inn figur
For å sette inn en figur, brukes følgende syntaks:
````markdown
:::{figure} mappenavn/filnavn.svg
---
name: fig-path-til-figuren
width: 80%
---

Figurtekst her. 
```
````

Man kan refere til figuren ved å skrive 
````markdown
I {numref}`fig-path-til-figuren` ser vi [...]
````


## Lage tabell
For å lage en tabell, brukes følgende syntaks:
````markdown
| Kolonne 1 | Kolonne 2 | Kolonne 3 |
|:---:|---:|:---|
| Midtstilt | Høyrestilt | Venstrestilt |
| $2$ | $\pi$ | $\xi$ |
````

som gir 

| Kolonne 1 | Kolonne 2 | Kolonne 3 |
|:---:|---:|:---|
| Midtstilt | Høyrestilt | Venstrestilt |
| $2$ | $\pi$ | $\xi$ |

## Lage lister

### Punktliste
For å lage en punktliste, brukes følgende syntaks:
````markdown
* Første punkt
* Andre punkt
* Tredje punkt
````
som gir
* Første punkt
* Andre punkt
* Tredje punkt

### Nummerert liste
For å lage en nummerert liste, brukes følgende syntaks:
````markdown
1. Første punkt
2. Andre punkt
3. Tredje punkt
````
som gir
1. Første punkt
2. Andre punkt
3. Tredje punkt

## Bokser og farger
For å lage bokser og farger, brukes følgende syntaks:
````markdown
:::{admonition} Tittel på boksen
---
class: klasse1, klasse2, ..., klasseN
---
Tekstinnhold i boksen.

:::
````

| Klasse | Bruksområde |
|:---|:---|
|`tip`| Læringsmål |
|`theory`| Generell teori. |
|`example`| Eksempler |
|`solution`| Løsningsforslag uten dropdown meny. Brukes i eksempler. |
|`answer, dropdown`| Fasit med dropdown meny |
|`solution, dropdown`| Løsningsforslag med dropdown meny |
|`check`| Underveisoppgaver |
|`hints, dropdown`| Hint |
|`sidenote, margin`| Oppklaring i sidemargen |
|`problem-level-1`| Oppgaver: level 1 |
|`problem-level-2`| Oppgaver: level 2 |
|`problem-level-3`| Oppgaver: level 3 |


Dropdown bokser kan brukes sammen med de andre klassene, for eksempel:


## Kode
For å sette inn kode, brukes følgende syntaks:
````markdown
```{code-block} python
def f(x):
    return x**2
```
````

Mulige konfigurasjoner for kodeblokker er:
* `linenos: true` - Viser linjenummer
* `emphasize-lines: 1, 3, 5-7` - Fremhever linje 1, lunje 3 og linjene 5 til 7. 

For eksempel vil koden under ha linjenummer og fremheve linje 2:

````markdown
```{code-block} python
---
linenos: true
emphasize-lines: 2
---
def f(x):
    return x**2 - 2*x + 1

y = f(2)
print(y)
```
````