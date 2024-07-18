# Algebraisk løsning

Å løse likninger algebraisk, handler om å jobbe med likningene symbolsk og bruke algebraiske lover til å isolere variabelen i likningen, hvis mulig. Vi kaller dette å bestemme løsningen. Grovt sett er det fire regneoperasjoner vi kan gjøre med likninger:
1. Legge til noe på begge sider av likningen.
2. Trekke fra noe på begge sider av likningen.
3. Gange med noe på begge sider av likningen.
4. Dele på noe på begge sider av likningen.

Det er viktig å understreke at vi må gjøre samme regneoperasjon på **begge sider** av likningen. 


## Likninger av typen $ax + b = 0$



```{admonition} Flytte og bytte
:class: note, margin
I eksempel 1 har vi konsekvent lagt til eller trukket fra det samme på begge sider. Kanskje er du vant med å *flytte og bytte* istedenfor? Disse to metodene gir samme resultat, men vår erfaring er at det er lettere å unngå feil dersom du bruker metoden over. 
```

````{admonition} Underveisoppgave 1
:class: check
Løs likningen

$$ 
2x + 3 = - x - 3
$$

```{admonition} Løsning
:class: dropdown, solution
For å løse denne ønsker vi å samle leddene som inneholder $x$ på *venstre side* og leddene som kun inneholder tall på *høyre side*. Det gjør vi ved å trekke fra eller legge til det samme på begge sider: 

Vi starter med å fjerne $x$ fra *høyre side*. Det gjør vi ved å legge til $x$ på begge sider: 

$$
2x + 3 + x = -x - 3 + x
$$

Det gir oss likningen: 

$$
3x + 3  = - 3
$$

Deretter trekker vi fra $3$ på begge sider: 

$$
3x + 3 - 3 = -3 - 3
$$

Vi har da ett ledd igjen på *høyre side* og ett ledd igjen på *venstre side*: 

$$
3x = -6
$$

For å finne $x$ kan vi nå dele på $3$:

$$
x = -\frac{6}{3} = - 2
$$

Likningen har altså løsningen $x=-2$. 
```
````

## Sette prøve på svaret
På ungdomsskolen har du kanskje lært å sette prøve på svaret? Det betyr at vi setter inn verdien vi har funnet i likningen og sjekker at de to sidene faktisk blir like. Det er lurt å gjøre, spesielt dersom du løser nye type likninger. 

````{admonition} Underveisoppgave 2
:class: check
Sett prøve på svaret $x=-2$ for likningen

$$ 
2x + 3 = - x - 3
$$

```{admonition} Løsning
:class: solution, dropdown

Vi sjekker *venstre side* (VS) og *høyre side* (HS) hver for seg: 


$$
\text{VS:}\quad 2\cdot -2 + 3  = -4 + 3 = - 1
$$

$$
\text{HS:}\quad - (-2) - 3 = 2 - 3 = -1
$$

Vi ser at *venstre side* og *høyre side* er like, og dermed er løsningen $x=-2 $ riktig. 

```
````

## Uttrykke løsningen av en likning
Fra tidligere er du antakeligvis kjent med å oppgi løsningen av en likning som $x = -2$, som i underveisoppgaven over. Tidligere i 1T har du også lært om mengder. Mengdene kan også brukes til å uttrykke løsningen av likninger. Vi kan da skrive $ L = \{-2\}$. Vi leser dette som at løsningsmengden består av tallet $-2$. Det er likevel ofte nyttig å være tydelig på hvilken variabel som svarer til løsningsmengden, og vi skriver derfor ofte $x \in \{-2\}$. 

## Oppgaver

:::::{admonition} Oppgave 1
---
class: problem-level-1
---
Hvilke av linjene under er likninger?

1. $4$
2. $x+4$
3. $4x$
4. $x = 4$
5. $x + 4 = 9$
6. $4x = 16$ 
7. $4\left(x+1\right) = 4x + 4$

:::{admonition} Fasit
---
class: answer, dropdown
---

Linje 1-3 er uttrykk, mens linje 4-6 er likninger. Linje 7 er en identitet, fordi løsningsmengden er $L = \mathbb{R}$, altså er likningen oppfylt for alle reelle tall. 
:::
:::::


:::::{admonition} Oppgave 2 
---
class: problem-level-1
---
Løs likningene under og sett prøve på svaret.

Oppgave 2a
: $$ 2x = 4$$

:::{admonition} Fasit: 2a
---
class: dropdown, answer
---
$$x = 2 \quad \Leftrightarrow \quad x \in \{2\}.$$
:::

Oppgave 2b
: $$2x + 2 = 4$$

:::{admonition} Fasit: 2b
---
class: dropdown, answer
---

$$x = 1 \quad \Leftrightarrow \quad x \in \{1\}.$$
:::

Oppgave 2c
: $$2x + 2 = x + 4$$

:::{admonition} Fasit: 2c
---
class: dropdown, answer
---
$$x = 2 \quad \Leftrightarrow \quad x \in \{2\}.$$
:::

Oppgave 2d
: $$2x - 2 = x + 4$$

:::{admonition} Fasit: 2d
---
class: dropdown, answer
---
$$x = 6 \quad \Leftrightarrow \quad x \in \{6\}.$$
:::

Oppgave 2e
: $$\dfrac{x}{2} = 4$$

:::{admonition} Fasit: 2e
---
class: dropdown, answer
---
$$x = 8 \quad \Leftrightarrow \quad x \in \{8\}.$$
:::

Oppgave 2f
: $$\dfrac{x}{2} + 3 = 4$$


:::{admonition} Fasit: 2f
---
class: dropdown, answer
---
$$x = 2 \quad \Leftrightarrow \quad x \in \{2\}.$$
:::
:::::


:::::{admonition} Oppgave 3
---
class: problem-level-2
---
Løs likningene.

Oppgave 3a
: $$ 3x + 9 = 3(x + 3)$$

:::{admonition} Fasit: 3a
---
class: dropdown, answer
---
Likningen er en identitet, så løsningen er $x \in \mathbb{R}$. Venstre og høyre side er like for alle reelle tall.
:::

Oppgave 3b
: $$ 3x - (x - 2) = (2x - 1) - (3x + 9)$$

:::{admonition} Fasit: 3b
---
class: dropdown, answer
---
$$
x = -4 \quad \Leftrightarrow \quad x \in \{-4\}.
$$
:::

Oppgave 3c
: $$ \dfrac{x}{2}−\left(\dfrac{x}{3}+\dfrac{1}{2}\right)=𝑥−2\left(\dfrac{x}{4}−1\right)$$

:::{admonition} Fasit: 3c
---
class: dropdown, answer
---
$$
x = -\dfrac{15}{2} \quad \Leftrightarrow \quad x \in \left\{-\dfrac{15}{2}\right\}.
$$
:::


Oppgave 3d
: $$ \dfrac{1}{2} \left(x-4\right)-\left(\dfrac{2x}{3}-1\right)=\dfrac{1}{3} \left(x-1\right)+\dfrac{x}{6}$$

:::{admonition} Fasit: 3d
---
class: dropdown, answer
---
$$
x = -1 \quad \Leftrightarrow \quad x \in \{-1\}.
$$
:::


:::::
