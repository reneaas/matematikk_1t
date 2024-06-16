# Sammensatte mengder

Noen ganger kan vi ikke beskrive en mengde med ett intervall eller med én ulikhet. Noen ganger kan vi ikke uttrykke de som ulikheter eller intervaller i det hele tatt.
Vi kan gi noen eksempler på tilfeller der vi teorien vi kjenner så langt ikke strekker til:
* Alle reelle tall bortsett fra $x = 0$. 
* Alle reelle tall over $x = 2$ og mindre enn $x = -1$.
* Alle reelle fra $x = -2$ til $x = 1$ og fra $x = 3$ til $x = 4$.
* Mengden av tallene $-1$, $1$ og $3$.
* Mengden av punktene $(1, 2)$ og $(3, 4)$ og $(-2, 3)$.

Etter denne seksjonen vil du kunne beskrive slike mengder på en kort og kompakt måte.


For å beskrive slike mengder, må vi finne ut hvordan vi setter sammen flere mengder, enten uttrykt som intervaller eller som ulikheter.

```{admonition} Læringsmål: sammensatte mengder
:class: tip
Målet for denne seksjon er at du skal:
* Kjenne til ulike regneregler for mengder.
* Kunne beskrive sammensatte mengder ved hjelp av intervaller, ulikheter og listenotasjon.
```



## Regneregler for mengder
Akkurat som reelle tall har regneregler, har også mengder sine egne regneregler. Vi trenger heldigvis bare noen få regneregler for å kunne beskrive sammensatte mengder.

```{admonition} Regneregler for mengder
:class: tip

La $A$ og $B$ være to mengder. Da har vi følgende regneregler:
1. **Union**: $A \cup B$ er mengden av alle elementer som er i $A$ eller i $B$, eller i begge.
2. **Snitt**: $A \cap B$ er mengden av alle elementer som er i både $A$ og $B$.
3. **Mengdeminus**: $A \setminus B$ er mengden av alle elementer som er $A$, *bortsett* fra alle som også er i $B$.
```

I tabellen under vises noen eksempler med listenotasjon og intervaller. Les den **nøye** og overbevis deg selv om at du forstår regnereglene:

````{margin}
```{admonition} Den tomme mengden
:class: tip
Noen ganger er det nyttig å kunne beskrive en mengde som ikke inneholder *noen elementer*. Vi kaller denne mengden for den **tomme mengden**. Vi bruker symbolet $\emptyset$ for denne mengden. På listeform kan vi skrive $\emptyset = \{\}$.
```
````

| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
| $\{1, 2, 3\}$ | $\{2, 3, 4\}$ | $\{1, 2, 3, 4\}$ | $\{2, 3\}$ | $\{1\}$ |
| $\{-2, -1\}$ | $\{1, 2\}$ | $\{-2, -1, 1, 2\}$ | $\emptyset$ | $\{-2, -1\}$ |
| $[1, 3]$ | $[2, 4]$ | $[1, 4]$ | $[2, 3]$ | $[1, 2 \rangle$ |
| $[1, 3]$ | $[4, 6]$ | $[1, 3] \cup [4, 6]$ | $\emptyset$ | $[1, 3]$ |
| $[-3, 3]$ | $[0, 2]$ | $[-3, 3]$ | $[0, 2]$ | $[-3, 0 \rangle$ |

```{admonition} Underveisoppgave 1
:class: note

Fyll ut tabellen under:
| Mengde $A$ | Mengde $B$ | $A \cup B$ | $A \cap B$ | $A \setminus B$ |
| :---: | :---: | :---: | :---: | :---: |
|$\{-1, 1\}$| $\{0, 2\}$ | | | |
| $\{-4, 2, 4\}$ | $\{1, 2, 4\}$ | | | |
| $\{1, 2, 3\}$ | $\{3, 4, 5\}$ | | | |
| $[1, 2]$ | $[2, 4]$ | | | |
| $[-1, 2]$ | $[4, 6]$ | | | |
| $[-3, 3]$ | $[0, 2]$ | | | |
```


## Sammensatte mengder som intervaller 


## Sammensatte mengder som ulikheter



````{comment}
```{admonition} Ekvivalens
:class: tip
Ekvivalens
: Når to utsagn som er uttrykt på forskjellig måte betyr det samme, sier vi at de er **ekvivalente**. Hvis $p$ og $q$ er to påstander som er ekvivalente, skriver vi $p \Leftrightarrow q$.

Implikasjon
: Når et utsagn fører til at et annet utsagn er sant, men ikke omvendt, sier vi at det første utsagnet **impliserer** det andre. Hvis $p$ impliserer $q$, skriver vi $p \Rightarrow q$. Vi kan også snu på det å skrive $q \Leftarrow p$. Begge skrivemåter uttrykker at $p$ implisere $q$.

Konjunksjon
: Når to utsagn er sanne, sier vi at de er **konjunktive**. Hvis $p$ og $q$ er sanne, skriver vi $p \land q$. Vi kan lese $\land$ som **og samtidig** fordi det uttrykker at $p$ og $q$ er sanne på én og samme tid.

Disjunksjon
: Når minst ett av to utsagn er sant, sier vi at de er **disjunktive**. Hvis $p$ eller $q$ er sanne, skriver vi $p \lor q$. Vi kan lese $\lor$ som **eller** fordi det uttrykker at enten $p$ er sann, eller $q$ er sann, eller så er begge sanne. 
```
````