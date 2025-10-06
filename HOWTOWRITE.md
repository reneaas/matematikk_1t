# Hvordan bruke koden

> Nedenfor finner du en oversikt over hvordan du kan skrive kode i boka for å lage ulike typer innhold. 

## Sette inn Geogebra-vinduer
Det eksisterer tre **directives** for å sette inn Geogebra-vinduer i boka:

1. `{cas}`: setter inn et CAS-vindu 
2. `{cas-popup}`: setter inn et klikkbart CAS-vindu som kan åpnes, lukkes og flyttes rundt.
3. `{ggb}`: setter inn et Geogebra-vindu med material_id fra Geogebra.org


### CAS-vinduer
For å sette inn et CAS-vindu i boka bruker vi `{cas}`-direktivet med følgende generelle syntaks:

```markdown
:::{cas} bredde høyde
:::
```

**Eksempel:**
Hvis vi ønsker et CAS-vindu med bredde på 400 piksler og høyde på 600 piksler, kan vi skrive

```markdown
:::{cas} 400 600
:::
```


### Popup-vinduer for CAS

For å sette inn et popup-vindu med CAS i boka, bruker vi `{cas-popup}`-direktivet med følgende generelle syntaks:

```markdown
:::{cas-popup} bredde høyde
:::
```

**Eksempel:**
Hvis vi ønsker et popup-vindu med CAS med bredde på 400 piksler og høyde på 600 piksler, kan vi skrive

```markdown
:::{cas-popup} 400 600
:::
```


### Geogebra-vinduer med material-id fra Geogebra.org

En fleksibel løsning er å lage et Geogebra-vindu med vilkårlig innhold på [Geogebra](geogebra.org) og så sette inn vinduet i boka ved hjelp av en `material_id`. Da bruker vi `{ggb}`-direktivet med følgende generelle syntaks:

```markdown
:::{ggb} bredde høyde
---
material_id: <material_id>
---
:::
```

**Eksempel:**
Hvis material_id er `rweg2th2` og vi ønsker høyde 400 og bredde 600, kan vi skrive

```markdown
:::{ggb} 600 400
---
material_id: rweg2th2
---
:::
```


## Sette inn kodevinduer
Det er 3 måter å sette inn kodevinduer i boka avhengig av oppgavetype:

1. `{interactive-code}`: for interaktive kodevinduer
2. `{parsons-puzzle}`: for Parsons-puzzles

### Interaktive kodevinduer
For å lage et generelt interaktive kodevindu som kan brukes umiddelbart, bruker vi `{interactive-code}`-direktivet med følgende generelle syntaks:

```markdown
:::{interactive-code} 
# Forhåndsskrevet kode her
:::
```

**Eksempel:**

```markdown
:::{interactive-code}
for x in range(10):
    print(x)
:::
```

### Prediktive kodevinduer
I mange tilfeller er det nyttig å lage et kodevindu der elevene må lese og forutsi utskriften til programmet før de kjører det. For å lage et slikt vindu, kan vi legge til et `option`-argument i `{interactive-code}`-direktivet. Da bruker vi følgende syntaks:

```markdown
:::{interactive-code}
---
predict:
---
# Kode de skal forutsi utskriften til her
:::
```

**Eksempel:**

```markdown
:::{interactive-code}
---
predict:
---
def f(x):
    return x**2 - 4

y = f(2)
print(y)
:::
```

### Parsons puzzles 
Parsons-puzzles er en type oppgave der kodelinjene i et program er *shuffled* i tilfeldig rekkefølge slik at elevene må dra og slippe dem i riktig rekkefølge for å få et fungerende program. For å lage et Parsons-puzzle bruker vi `{parsons-puzzle}`-direktivet med følgende generelle syntaks:

```markdown
:::{parsons-puzzle}
# Kode de skal dra og slippe i riktig rekkefølge her
:::
```

**Eksempel:**

```markdown
:::{parsons-puzzle}
def f(x):
    return x**2 - 4

y = f(2)
print(y)
:::
```

Noen ganger er det ikke en entydig rekkefølge i et program. Da kan vi koble sammen linjene ved å skrive dem i grupper ved å separere dem med `;`: 

```markdown
:::{parsons-puzzle}
a = 1 ;b = 2 ;c = 3
x = 2
y = a * x**2 + b * x + c
:::
```

I eksempelet over vil kodelinjene som definerer `a`, `b` og `c` være én boks. 

## Sette inn figurer

### Vanlige figurer

### Klikkbare figurer


## Sette inn videoer


## Sette inn quiz


## Sette inn par-puzzles

## Plot-direktivet (matematikkfigurer)

Plot-direktivet (`{plot}` / `.. plot::`) lar deg lage fleksible matematikkfigurer med et kompakt YAML‑lignende oppsett. Nedenfor følger en praktisk oppslagsguide med eksempler for alle primitivene. Eksemplene bruker MyST‑syntaks; reST fungerer tilsvarende.

### Grunnstruktur

```markdown
:::{plot}
function: sin(x)/x, f(x), (-6*pi, 6*pi) \ {0}
point: (pi, f(pi))
xmin: -10
xmax: 10
ymin: -5
ymax: 5
grid: on
:::
```

Alle linjer før første blanklinje (eller slutten av blokken) tolkes som oppsett. Eventuell tekst etterpå blir bildetekst.

### Uttrykk (SymPy)

Nesten alle tallfelt støtter nå uttrykk: `pi`, `sqrt(2)`, `2*pi/3`, `exp(1)`, `sin(pi/6)`, osv. Feil eller ugyldige uttrykk fører bare til at den aktuelle linjen hoppes over (bygget feiler ikke).

Støttede funksjoner (utvalg): `pi`, `E`, `sqrt`, `exp`, `log`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `Abs` + vanlige aritmetiske operatorer.

### Felles stil og farger

Der hvor `linestyle` kan angis: `solid`, `dotted`, `dashed`, `dashdot`.

Farger forsøkes først slått opp i `plotmath.COLORS` (paletten). Hvis ikke funnet brukes token direkte (Matplotlib-navn/hex). Hvis fortsatt ikke gyldig brukes en fornuftig standard (typisk svart eller blå). Enkeltbokstav-farger (`b`, `g`, …) er deaktivert for funksjonsnavn slik at `f`, `g` osv. kan brukes som etiketter.

### Funksjoner

Former:
```
function: uttrykk
function: uttrykk, etikett
function: uttrykk (a,b)
function: uttrykk (a,b) \ {x1, x2}
function: [uttrykk, "etikett", (a,b), {x1, x2}]
```

Eksempler:
```markdown
function: x**2 - 2*x + 3, f(x)
function: sin(x)/x, s(x), (-10,10) \ {0}
```

### Punkter

```
point: (x, y)
```
Der `x` eller `y` kan bruke funksjonskall på etiketter: `point: (pi, f(pi))`.

### Vertikale og horisontale linjer

```
vline: x[, ymin, ymax][, linestyle][, farge]
hline: y[, x0, x1][, linestyle][, farge]
```
Eksempel:
```markdown
vline: pi/2, -, 3, dashed, red
hline: 0
```

### Generell linje og linjesegment

```
line: a, b[, linestyle][, farge]        # y = a*x + b
line: a, (x0, y0)[, linestyle][, farge] # y = a*(x-x0) + y0
line-segment: (x1, y1), (x2, y2)[, linestyle][, farge]
```
Eksempler:
```markdown
line: 2, -1
line: -sqrt(3), (pi, 0), dotted, teal
line-segment: (0,0), (2*sqrt(2), 2), dashed, purple
```

### Polygoner og fyll

```
polygon: (x1, y1), (x2, y2), ...[, show_vertices]
fill-polygon: (x1, y1), (x2, y2), ...[, farge][, alpha]
```
Eksempler:
```markdown
polygon: (0,0), (2,0), (2,1), (0,1), show_vertices
fill-polygon: (0,0), (3,0), (3,2), (0,2), lightgray, 0.25
```

### Søyle (bar)

```
bar: (x, y), lengde, orientering
```
`orientering`: `h|hor|horiz|horizontal` eller `v|vert|vertical`.

Eksempel:
```markdown
bar: (0,0), 4, h
```

### Vektorer

```
vector: x, y, dx, dy[, farge]
```
Alle fire tall kan være uttrykk.
```markdown
vector: 0, 0, 2*cos(pi/6), 2*sin(pi/6), orange
```

### Vinkelbue (angle-arc)

```
angle-arc: (cx, cy), radius, start_grad, slutt_grad[, linestyle][, farge]
```
Vinkler i grader (0° på +x-aksen, mot klokka).
```markdown
angle-arc: (0,0), 3, 0, 60, dashed, red
```

### Sirkel og ellipse

```
circle: (cx, cy), r[, linestyle][, farge]
ellipse: (cx, cy), a, b[, linestyle][, farge]
```
`r`, `a`, `b` > 0. Eksempel:
```markdown
circle: (0,0), 2*pi/6, dotted, green
ellipse: (1, -1), 3, sqrt(5), red
```

### Parametrisk kurve

```
curve: x(t), y(t), (t0, t1)[, linestyle][, farge]
```
Symbol `t` er reservert. Eksempel:
```markdown
curve: cos(t), sin(2*t), (0, 2*pi), dashed, orange
```

### Annotering og tekst

Annotering:
```
annotate: (xy_text), (xy_point), "Tekst"[, bue]
```
`bue` (kurvatur) valgfri (standard 0.3).

Tekst:
```
text: [x, y, "tekst"[, pos][, bbox]]
```
`pos` kan være: `top-left`, `bottom-right`, `center-center`, osv. Prefiks `long` for større avstand: `longtop-left`.

Eksempler:
```markdown
annotate: (pi, f(pi)), (pi, 0), "Maks?", 0.25
text: [0, 0, "Origo", top-right, bbox]
```

### Aksevalg

```
axis: off
axis: equal
axis: off, equal
```
`off` skjuler ramme og rutenett. `equal` gir lik skala i x og y.

### Figur- og layoutvalg

```
width: 100%
figsize: (6, 4)
fontsize: 20
lw: 2.5
alpha: 0.6
```

### Farge- og stiloppløsning

1. Sjekk paletten `plotmath.COLORS`.
2. Hvis ikke funnet: bruk token direkte (navn eller hex `#rrggbb`).
3. Hvis fortsatt feil: bruk en standard (svart/blå).

### Feilsituasjoner

* Enkeltlinjer med feil uttrykk hoppes over – resten av figuren rendres.
* Ugyldige intervaller (byttede grenser) blir automatisk sortert for kurver.
* Null eller negativ radius / a / b ignoreres.

### Komplett eksempel

```markdown
:::{plot}
function: sin(x)/x, s(x), (-8*pi, 8*pi) \ {0}
curve: cos(t), sin(2*t), (0, 2*pi), dashed, orange
circle: (0,0), 2*pi/6, dotted, green
ellipse: (1, -1), 3, sqrt(5), red
point: (pi, s(pi))
line-segment: (0,0), (2*sqrt(2), 2), dashed, purple
vector: 0, 0, 2*cos(pi/6), 2*sin(pi/6), teal
angle-arc: (0,0), 2.5, 0, 60, dashed
annotate: (pi, s(pi)), (pi, 0), "Maks?", 0.25
text: [0,0, "Origo", top-right, bbox]
xmin: -10
xmax: 10
ymin: -6
ymax: 6
grid: on
fontsize: 22
width: 100%
:::
```

Dette skal gi en rik figur med flere elementtyper og uttrykk.

---

For ytterligere interne detaljer se docstring i `_ext/plot.py`.