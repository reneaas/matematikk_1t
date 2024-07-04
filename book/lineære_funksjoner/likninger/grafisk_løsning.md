# Grafisk løsning

Å løse likninger grafisk betyr at vi bruker den grafiske representasjonen til en funksjon til å løse likningen. 

Igjen kan vi ta utgangspunktet i likningen

$$
2x + 3 = -x - 3
$$

Denne likningen kan vi løse grafisk ved å tegne de to funksjonene $y = 2x + 3$ og $y = x - 3$. Hver side av likningen vil da være representert ved en funksjon. 

```{figure} ./figurer/eksempler/eksempel1.svg
:name: likningergrafisk
:width: 80%

Grafisk løsning av likninger
```

Ettersom vi ønsker å finne ut hvor de to sidene er like, må vi finne en x-verdi som gjør at de to sidene får samme y-verdi. Det vil være tilfellet i skjæringspunktet mellom de to linjene. I dette tilfellet får vi at $x = - 2$. 

````{admonition} Underveisoppgave 1
Bruk figuren under til å løse likningen $ - 2x + 1 = x - 2$

```{figure} ./figurer/eksempler/eksempel2.svg
:name: eksempel2
:width: 80%

Grafisk representasjon av likningen $ - 2x + 1 = x - 2$

```
```{dropdown} Fasit

Fra figuren ser vi at de to linjene krysser hverandre når $x = 1$. Løsningen av likningen er derfor $x = -1$

```
````

## Grafisk løsning når kun venstreside inneholder variabler
I tilfellet over måtte vi tegne to skrå linjer, for deretter å finne skjæringspunktet. Mange likninger vil være på formen $2 x + 3 = k$. I såfall holder det å bestemme for hvilken verdi av $x$ funksjonen krysser linja $y = k$. Husk at hvis $k = 0$, så betyr det at $y = 0$ som er det samme som $x$-aksen.

````{admonition} Underveisoppgave 2
Under vises et interaktivt plott for likningen $2x + 3 = k$. Bruk plottet til å 
1. Bestemme løsningen av likningen $2x + 3 = -3$
2. Bestemme løsningen av likningen $2x + 3 = 1$.
3. Bestemme hvilken verdi av $k$ som gir løsningen $x = -2$.

```{raw} html
:file: ./figurer/interaktive_plot/lineær_likning_2x+3=k.html
```
````

## Ingen, én eller uendelig mange løsninger
Eksemplene vi har sett på så langt har hatt én løsning, men det finnes også lineære likninger som har ingen løsninger, eller uendelig mange løsninger. 

Et eksempel på en lineær likning uten løsninger er 

$$
x + 1 = x + 3.
$$ 

Dette kan vi se dersom vi forsøker å løse likningen grafisk. 

```{figure} ./figurer/eksempler/eksempel3.svg
:name: ingenløsning
:width: 100%

Likningen $x + 3 = x + 1$ har ingen løsninger
```

Vi ser at vi har to parallelle linjer som aldri skjærer hverandre, og dermed finnes det ingen verdier for $x$ der de to sidene av likningen har samme verdi. 

Likningen 

$$
2(x+1) = 2x + 2
$$ 

vil på den andre siden ha uendelig mange løsninger. Det skyldes at likningen er en identitet, og altså vil den være oppfylt for alle tenkelige verdier av $x$. Forsøker vi å løse likningen grafisk, ser vi at de to sidene gir to overlappende linjer, som dermed deler alle verdier. 

```{figure} ./figurer/eksempler/eksempel4.svg
:name: uendeligløsning
:width: 100%

Likningen $2(x + 1) = 2x + 2$ har uendelig mange løsninger
```

## Oppgaver
---
### Oppgave 1
Bruk figuren under til å løse likningene: 

1. $ x + 3 = 0$
2. $ x + 3 = 4$
3. $ x + 3 = -2$

```{figure} ./figurer/oppgaver/oppg_1.svg
:name: oppg_1
:width: 80%
```

```{admonition} Fasit
:class: dropdown, note
1. $x = -3$
2. $x = 1$
3. $x = -5$

```
---
### Oppgave 2
Bruk figuren under til:
1. Å Sette opp minst tre ulike likninger. 
2. Å Løse likningene ved hjelp av figuren. 

```{figure} ./figurer/oppgaver/oppg_2.svg
:name: oppg_2
:width: 80%
``` 

---
### Oppgave 3
Bruk den interaktive figuren under til å forklare hvorfor likningen $2x+1 = k$ har løsninger for alle verdier av $k$. 
Bestem hvilken verdi av $k$ som gir løsningen $x = -2$. 


```{raw} html
:file: ./figurer/interaktive_plot/lineær_likning_2x+1=k.html
```


