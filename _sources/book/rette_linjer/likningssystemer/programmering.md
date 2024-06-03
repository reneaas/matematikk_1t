# Løsning med programmering


Eleven har skrevet følgende kode der eleven har brukt en strategi som på _godt norsk_ kalles for **grid search**. 

```python
for y in range(-4, 5):
    for x in range(-4, 5):
        if x - y == -1 and x + y == 1:
            print(f"{x = } og {y = }")
```

Animasjonen i {numref}`grid_search` illustrerer hvordan koden går gjennom punkter $(x, y)$ i et gitt område. Koden sjekker så om likningene er oppfylt samtidig for hvert punkt.

```{figure} ./animasjoner/grid_search.gif
:name: grid_search
:width: 80%

Animasjonen viser strategien bak grid search for å løse et likningssystem. Metoden søker gjennom noen mulige punkter $(x, y)$ i et gitt område og sjekker om likningene i likningssystemet er oppfylt. 
```