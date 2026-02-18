# Dev


:::{plot}
xmin: -1
xmax: 8
ymin: -1
ymax: 8
width: 100%
function: 1/9 * (x + 1) * (x - 6)**2, f
let: N = 12
let: a = 0
let: b = 6
let: h = (b - a) / N
repeat: n=0..N; polygon: (a + n * h, 0), (a + (n + 1) * h, 0), (a + (n + 1) * h, f(a + n * h)), (a + n * h, f(a + n * h)), blue, 0.3
text: 6, 5, "12 rektangler", bbox
:::

:::{interactive-graph} 
interactive-var: N, 1, 64, 64
interactive-var-start: 1
xmin: -1
xmax: 8
ymin: -1
ymax: 8
width: 100%
function: 1/9 * (x + 1) * (x - 6)**2, f
let: a = 0
let: b = 6
let: h = (b - a) / N
repeat: n=0..N; polygon: (a + n * h, 0), (a + (n + 1) * h, 0), (a + (n + 1) * h, f(a + n * h)), (a + n * h, f(a + n * h)), blue, 0.3
text: 6, 5, "{N:0.f} rektangler", bbox
:::


:::{interactive-graph} 
width: 70%
interactive-var: a, 0, 5, 64
interactive-var: b, 0.01, 5, 64
interactive-var-start: a=1, b=2
xmin: -6
xmax: 6
ymin: -1
ymax: 6
function: a * b**x
point: (0, a)
:::