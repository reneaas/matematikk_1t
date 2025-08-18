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