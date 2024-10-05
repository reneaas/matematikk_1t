# Løsning med programmering

:::{admonition} Læringsmål: lineære likninger med programmering
---
class: tip
---
Etter å ha gått gjennom denne delen, er målet at du skal kunne:
* Lese og tolke programmer som løser lineære likninger
* Justere og tilpasse programmer for å løse dine egne likninger
:::


## Numerisk løsning av lineære likninger
Mange likninger man møter på i det virkelige liv, har ingen **analytisk løsning** - det vil si, vi kan ikke få $x$ alene. Et eksempel slik likning er

$$
2^x = 6x + 5
$$

Men vi kan alltid prøve å finne en verdi for $x$ slik at likningen er oppfylt - dette kaller vi å bestemme løsningen **numerisk**. Her skal vi se på én strategi for å gjøre dette med lineære likninger.


---

## Repetisjon av nødvendige verktøy


Først må vi repetere noen verktøy vi trenger for å få løst en likning numerisk. 


::::{admonition} Repetisjon 1: nullpunkter og likninger
---
class: reminder
---
Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::

::::

---

::::{admonition} Oppsummering: nullpunkter og likninger
---
class: dropdown, summary
---
For en funksjon $f$, så er følgende ekvivalent:
* Nullpunktet til $f$
* Skjæringen mellom grafen til $f$ og $x$-aksen
* Løsningen til likningen $f(x) = 0$

:::{figure} ../grafisk_løsning/figurer/teori/ax+b=0.svg
---
width: 80%
---
viser grafisk nullpunktet for en lineær funksjon $f(x) = ax + b$. 
:::
::::

---

Så bør du nok repetere litt om `for`-løkker.



::::::{admonition} Repetisjon 2: `for`{l=python}-løkker
---
class: reminder
---

:::::{tab-set} 
---
class: tabs-parts
---

::::{tab-item} a
Ta quizen! 

:::{raw} html
---
file: ./quiz/quiz_2/quiz_2.html
---
:::
::::

::::{tab-item} b
For hvert av programmene under:
1. Les programmet og forutsi hva det vil skrive ut.
2. Skriv inn hypotesen din for å sjekke svaret ditt.

````{tab-set} 
---
class: tabs-parts
---
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_2/program_1.html
---
:::

```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_2/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_2/program_3.html
---
:::

```
````

::::

:::::

::::::

::::::::{admonition} Oppsummering: `for`{l=python}-løkker
---
class: summary, dropdown
---
Når vi bruker `range`{l=python}-funksjonen til å lage en liste med tall kan vi enten bruke den som:
::::{tab-set}
:::{tab-item} `range(start, stopp, steglengde)`{l=python}
```{code-block} python
for x in range(start, stopp, steglengde):
    # kode som skal gjentas
```

* `start`{l=python} er det første tallet i listen.
* `stopp`{l=python} er stoppekriteriet. Vi stopper alltid *før* dette tallet.
* `steglengde`{l=python} er hvor mye vi skal endre på løkkevariabelen `x`{l=python} på hver runde i løkken.
* `x`{l=python} kalles for **løkkevariabelen** fordi den lages av løkka og endres for hver runde i løkka automatisk.

| Eksempel | Liste med tall |
|-----------|----------|
| `range(1, 5, 1)`{l=python} | $1, 2, 3, 4$ |
| `range(1, 10, 2)`{l=python} | $1, 3, 5, 7, 9$ |
| `range(5, 1, -1)`{l=python} | $5, 4, 3, 2$ |
:::

:::{tab-item} `range(start, stopp)`{l=python}
```{code-block} python
for y in range(start, stopp):
    # kode som skal gjentas
```

* `start`{l=python} er det første tallet i listen.
* `stopp`{l=python} er stoppekriteriet. Vi stopper alltid *før* dette tallet.
* `steglengde`{l=python} er satt fast til `1`{l=python} som standardverdi her.
* `y`{l=python} kalles for **løkkevariabelen** fordi den lages av løkka og endres for hver runde i løkka automatisk.


| Eksempel | Liste med tall |
|-----------|----------|
| `range(1, 5)`{l=python} | $1, 2, 3, 4$ |
| `range(1, 10)`{l=python} | $1, 2, 3, 4, 5, 6, 7, 8, 9$ |
| `range(5, 1)`{l=python} | Ingen tall lages |
:::
::::
::::::::

---

::::::::{admonition} Repetisjon 3: funksjoner i Python
---
class: reminder
---

::::::{tab-set}
---
class: tabs-parts
---

:::::{tab-item} a
Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_3/quiz_3.html
---
:::

:::::

:::::{tab-item} b

For hvert av programmene under:

1. Les programmet og forutsi hva det vil skrive ut.
2. Skriv inn hypotesen din for å sjekke svaret ditt.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_3/b/program_1.html
---
:::

```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_3/b/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_3/b/program_3.html
---
:::

```
````

:::::

:::::{tab-item} c
Her generaliserer vi programmene litt slik at vi jobber med en variabel `x`{l=python} i stedet.

For hvert av programmene under:

1. Les programmet og forutsi hva det vil skrive ut.
2. Skriv inn hypotesen din for å sjekke svaret ditt.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_3/c/program_1.html
---
:::

```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_3/c/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/repetisjon/repetisjon_3/c/program_3.html
---
:::

```
````

:::::
::::::


::::::::


::::::{admonition} Oppsummering: funksjoner i Python
---
class: summary, dropdown
---

Generell skrivemåte: 

:::{code-block} python
def funksjonsnavn(x):
    return funksjonsuttrykk

x = tall
y = f(x)
:::

:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} Eksempel 1
* Funksjon: $f(x) = 2x + 1$.
* Funksjonsverdi: $f(2)$.

:::{code-block} python
---
linenos: true
---
def f(x):
    return 2 * x + 1

y = f(2)
print(y)
:::
::::

::::{tab-item} Eksempel 2
* Funksjon: $g(x) = -x + 5$.
* Funksjonsverdi: $g(3)$.

:::{code-block} python
---
linenos: true
---
def g(x):
    return -x + 5

print(g(3))
:::
::::

::::{tab-item} Eksempel 3
* Funksjon: $h(x) = \dfrac{1}{2}x + 2$.
* Funksjonsverdi: $h(-4)$.

:::{code-block} python
---
linenos: true
---

def h(x):
    return 0.5 * x + 2

x = -4
y = h(x)
print(y)
::::::


---


## Bestemme nullpunkter ved hjelp av programmering

Alle likninger kan alltid skrives om til formen $f(x) = 0$. Vi skal derfor fokusere på hvordan vi løser likninger av denne typen - altså likninger der vi skal finne nullpunktene til en funksjon $f(x)$.


### Hvordan sjekke om $f(x) = 0$ med et program

::::::{admonition} Utforsk 1: hvordan sjekker vi om $f(x) = 0$? 
---
class: explore
---

:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} a
Bestem nullpunktene til funksjonene

* $f(x) = x - 2$
* $g(x) = 2x + 4$
* $h(x) = -3x + 6$
::::

::::{tab-item} b

Når vi skal sjekke om en funksjonsverdi $f(x) = 0$, kan vi skrive `f(x) == 0`{l=python} i Python. 
* Hvis `f(x)`{l=python} er lik 0, vil dette gi `True`{l=python}.
* Hvis `f(x)`{l=python} ikke en lik 0, vil dette gi `False`{l=python}.

Under vises tre programkoder som tester ut om en funksjonsverdi er lik 0 og skriver ut svaret (som er enten `True`{l=python} eller `False`{l=python}).

For hvert av programmene under:
1. Les programmet og forutsi hva det vil skrive ut.
2. Skriv inn hypotesen din for å sjekke svaret ditt.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/b/program_1.html
---
:::
```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/b/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/b/program_3.html
---
:::

```
````

::::

::::{tab-item} c

For hvert av programmene under:

1. Les programmet og forutsi på *hvilken linje* i utskriften det vil skrives ut `True`{l=python}. 
2. Skriv inn hypotesen din for å sjekke svaret.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/c/program_1.html
---
:::
```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/c/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_1/c/program_3.html
---
:::

```

::::
:::::

::::::

---

:::::{admonition} Underveisoppgave 1
---
class: check
---
Ta quizen!

:::{raw} html
---
file: ./quiz/quiz_4/quiz_4.html
---
:::

:::::

---

### Hvordan automatisere søket etter nullpunkter

Siste steg er å få et program til å fortelle oss når $f(x) = 0$ automatisk uten at vi må lete gjennom en liste med `True`{l=python} og `False`{l=python}. For da kunne vi vel egentlig strengt tatt tatt bare gått gjennom en liste med tall i stedet. Denne automatiseringen skal vi se på nå!

:::::::{admonition} Utforsk 2: automatisere søket etter nullpunkter
---
class: explore
---
For å automatisere søket etter nullpunkter, kan vi bruke:
1. En `for`{l=python}-løkke som går gjennom en liste med mulige verdier for $x$. 
2. For hver verdi av $x$, sjekker vi om $f(x) = 0$.
3. *Hvis* $f(x) = 0$ er sant, skriver vi ut verdien til $x$.

Så langt har vi sett på punkt 1 og 2 - nå må vi utvide verktøykassa vår så vi kan få til punkt 3. Dette kan vi få til med å bruke en `if`{l=python}-setning. Dette er en setning som gjør noe *hvis* noe er sant! 

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} a
Under vises tre eksempelkoder som bruker en `if`{l=python}-setning for å bestemme nullpunktet til en funksjon.

For hvert av programmene under:
1. Les programmet og forutsi hva det vil skrive ut.
2. Skriv inn hypotesen din for å sjekke svaret ditt.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} Program 1

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/program_1.html
---
:::
```

```{tab-item} Program 2

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/program_2.html
---
:::

```

```{tab-item} Program 3

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/a/program_3.html
---
:::

```
````


:::::

:::::{tab-item} b


````{tab-set}
---
class: tabs-parts
---
```{tab-item} I
Under vises et program som søker etter nullpunktet til en funksjon $f$, men kodelinjene er plassert i tilfeldig rekkefølge. 

Plasser kodelinjene i riktig rekkefølge.

```

```{tab-item} II
Endre på programmet slik at det finner nullpunktet til 

$$
f(x) = 4x + 12
$$

Kjør programmet og sjekk at du finner nullpunktet til $f$. 
```

```{tab-item} III
Endre på programmet slik at det søker etter nullpunktet til

$$
f(x) = -x + 16
$$

:::{admonition} Hint
---
class: dropdown, hints
---
Hvis du ikke får noen utskrift, kan det hende du må endre på *mer* enn bare funksjonsuttrykket! <br> Hvilke $x$-verdier sjekker du? Og hva er nullpunktet til $f$?
:::
```

````

<br>

:::{raw} html
---
file: ./interaktiv_kode/utforsk/utforsk_2/b.html
---
:::



:::::
::::::


:::::::

---

:::::{admonition} Underveisoppgave 2
---
class: check 
---


:::::