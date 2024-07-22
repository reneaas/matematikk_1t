```{mermaid} 
flowchart TD
    A["Sett x = startverdi"] --> B
    B{"Er f(x) nærme null?"} --> |Nei| C[Øk x med Δx]
    C --> B
    B --> |Ja| D["Skriv ut x"]
```