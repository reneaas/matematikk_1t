```{mermaid} 
flowchart TD
    A["Sett x = startverdi"] --> B
    B["Har f(x) endret fortegn?"] --> |Nei| C[Øk x med Δx]
    C --> B
    B --> |Ja| D["Skriv ut x"]
```