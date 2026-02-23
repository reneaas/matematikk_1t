# Dev



:::{plot}
width: 70%
function: x**2 - 3 * x, f, blue
function: -2 * x + 1, g, red
function: 3 * exp(-x), h, orange
function: log(x), p, teal
:::



:::{interactive-graph} 
interactive-var: N, 1, 64, 64
interactive-var-start: 6
xmin: -1
xmax: 8
ymin: -1
ymax: 8
width: 100%
function: 1/9 * (x + 1) * (x - 6)**2, f
let: a = 0
let: b = 6
let: h = (b - a) / N
repeat: n=0..N-1; polygon: (a + n * h, 0), (a + (n + 1) * h, 0), (a + (n + 1) * h, f(a + n * h)), (a + n * h, f(a + n * h)), blue, 0.2
text: 6, 5, "{N:0.f} rektangler", bbox
:::


:::{interactive-graph} 
interactive-var: N, 1, 64, 64
interactive-var-start: 6
xmin: -1
xmax: 8
ymin: -1
ymax: 8
width: 100%
function: 1/9 * (x + 1) * (x - 6)**2, f
let: a = 0
let: b = 6
let: h = (b - a) / N
repeat: n=0..N-1; polygon: (a + n * h, 0), (a + (n + 1) * h, 0), (a + (n + 1) * h, f(a + (n + 1) * h)), (a + n * h, f(a + n * h)), blue, 0.2
text: 6, 5, "{N:0.f} trapeser", bbox
:::


:::{interactive-graph} 
interactive-var: N, 1, 64, 64
interactive-var-start: 6
xmin: -1
xmax: 8
ymin: -1
ymax: 8
width: 100%
function: 1/9 * (x + 1) * (x - 6)**2, f
let: a = 0
let: b = 6
let: h = (b - a) / N
repeat: n=0..N-1; polygon: (a + n * h, 0), (a + (n + 1) * h, 0), (a + (n + 1) * h, f(a + 0.5 * h + n * h)), (a + n * h, f(a + 0.5 * h + n * h)), blue, 0.2
text: 6, 5, "{N:0.f} rektangeler", bbox
:::
