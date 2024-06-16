# Guide for skriving

## Bygge en Jupyterbook

For å bygge en Jupyterbook, skriv følgende kommando i terminalen i **root** av directory:

```bash
jb build . --all
```

Html-kode for hele boka genereres og en link til root i html-filene skrives ut i terminalen. 
Html-koden vil ligge i `_build/html` mappen. Du må åpne `index.html` i nettleseren for å se på den lokale versjonen av boka. Denne pushes ikke opp til skyen - Git bygger boka når du pusher slik at vi ikke kan *breake* noe.

## Git greier

Viktig sjekkliste:
1. Jobb alltid på din *egen branch* lokalt. Merge til `main` når du er ferdig med noe fra Github.com ved å legge inn en pull request og merge i skyen. 
2. Pull endringer fra skyen hver gang du setter i gang å jobbe for å redusere antall merge konflikter.
3. Skriv en beskrivende commit message når du legger inn en ny commit. 


### Viktige kommandoer

|Kommando|Beskrivelse|
|:---:|:---|
|`git pull`| Henter endringer fra skyen|
|`git add --all`| Legger til nye endringer som er gjort i alle filer. |
|`git commit -m "Din beskrivende melding"`| Committer endringer |
|`git push`| Pusher endringer til skyen |
|`git branch` | Viser alle branches, inkludert hvilken du jobber på. |
|`git checkout branchnavn`| Bytter til en annen branch |
| `git status` | Viser status på filer som er endret, lagt til, osv. |

### Merge konflikter
Hvis det oppstår en merge-konflikt, er dette **hensikten med git** og er ønsket atferd. For å løse merge-konflikter lokalt, må du åpne opp filene og identifisere hvor i filen konflikten er (git markerer dette og forteller deg hvilken versjon av innholdet som er din egen, og hvilken som er hentet fra skyen). Du må manuelt redigere filene for å fjerne konflikten, og så er det bare å committe endringene og pushe opp til skyen. 



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
|$\frac{a}{b}$ |`\frac{a}{b}`|
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
```{figure} mappenavn/filnavn.svg
:name: navn-på-figuren
:width: 80%

Figurtekst her. 
```
````

Man kan refere til figuren ved å skrive 
````markdown
I {numref}`navn-på-figuren` ser vi [...]
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
- Første punkt
- Andre punkt
- Tredje punkt
````
som gir
- Første punkt
- Andre punkt
- Tredje punkt

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
```{admonition} Tittel på boksen
:class: klasse1, klasse2, ..., klasseN

Innholdet i boksen
```
````

| Klasse | Farge |
|:---:|:---:|
|`note`| Blå |
|`tip`| Grønn |
|`warning`| Gul |
|`important`| Rød |
|`dropdown`| Dropdown versjon av boksen |

Dropdown bokser kan brukes sammen med de andre klassene, for eksempel:


````markdown
```{admonition} Tittel på boksen
:class: tip, dropdown
Skjult innhold som kan åpnes ved å klikke på tittelboksen. 
```
````

## Kode
For å sette inn kode, brukes følgende syntaks:
````markdown
```python
def f(x):
    return x**2
```
````

Bokser kan kombineres:

`````markdown
````{dropdown} Klikk for kode
```python
def f(x):
    return x**2
```
````
`````