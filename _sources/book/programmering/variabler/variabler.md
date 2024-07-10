# Variabler

```{admonition} Læringsmål: variabler
:class: tip
Etter å ha lest dette delkapittelet, er målet at du skal kunne:
* Forklare hva en **variabel** er.
* Vite hva som menes med **variabelnavn**, **verdi** og **datatype**.
* Kjenne til noen viktige datatyper i Python som er relevante for programmering i matematikken.
```


## Hva er en variabel? 

En variabel er den grunnleggende byggesteinen i Python. Det er noe vi selv lager (såkalt *brukerdefinert*). Vi bruker variabelen til å gjøre noe - i matematikk bruker vi det typisk til å regne ut noe og lagre tall. 


````{admonition} Variabel i Python
:class: theory

En **variabel** er en brukerdefinert ting som:
* Har et **variabelnavn** som vi selv velger.
* Har en **verdi** som vi selv gir.
* Har en **datatype** som avhenger av hva slags verdi vi gir variabelen.
````

La oss se på noen eksempler på variabler i Python

```{admonition} #-tegnet
:class: note, margin
I koden i eksempel 1 kan du se at vi skriver `#` bak en kodelinje, etterfulgt av en kommentar med forklaringer. Python ignorerer alt som kommer etter `#`-tegnet slik at vi kan skrive forklarende kommentarer i koden til oss selv. 
```

````{admonition} Eksempel 1: variabler
:class: example

Under vises en kort Python-kode: 

```python
a = 5                       # Definerer en variabel med navn `a` med verdi `5`
print(f"{a = }")            # Skriver ut verdien til variabelen `a`
print(f"{type(a) = }")      # Skriver ut datatypen til variabelen `a`
```

Kjører du koden over, får du utskriften:

```console
a = 5
type(a) = <class 'int'>
```
som forteller oss at verdien til `a` er `5` og datatypen til `a` er `int`. Denne datatypen står for *integer* som er engelsk for *heltall*. 
````