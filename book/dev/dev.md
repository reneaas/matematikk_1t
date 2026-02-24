# Dev


:::{plot}
let: S = 4
let: gap = 1
let: h = sqrt(3)/2 * S
def: ox(i) = i*(S+gap)

repeat: i=0..5; polygon: (ox(i), 0), (ox(i)+S, 0), (ox(i)+S/2, h), black
axis: equal
axis: off
:::


:::{plot}
let: S = 6              # overall side length
let: n = 2             # depth (rows = 2**n). Try 4..7 first.
let: rows = 2**n
let: a = S / rows       # side length of each small triangle
let: ha = sqrt(3)/2 * a # height of each small triangle
def: r(t) = floor((sqrt(8*t + 1) - 1)/2)
def: k(t) = t - r(t) * (r(t) + 1) / 2
def: x0(t) = (S - (r(t) + 1) * a) / 2 + k(t) * a
def: y0(t) = r(t) * ha
def: odd(t) = ((k(t) & (r(t) - k(t))) == 0)
let: T = rows * (rows + 1) / 2
repeat: t=0..T-1; polygon: (x0(t), y0(t)), (x0(t) + a, y0(t)), (x0(t) + a/2, y0(t) + ha), black, 1 * odd(t)
axis: equal
axis: off
:::


:::{plot}
width: 50%
figsize: (3, 3)
let: x = 4
let: y = 2
polygon: (0, 0), (x, 0), (x, x), (0, x), blue, 0.2
polygon: (x, x), (x + x, x), (x + x, x + y), (x, x + y), red, 0.2
polygon: (0, 0), (-x, 0), (-x, -y), (0, -y), red, 0.2
polygon: (0, x), (-x, x), (-x, x + y), (0, x + y), red, 0.2
polygon: (x, 0), (x + x, 0), (x + x, -y), (x, -y), red, 0.2
text: 0.5 * x, 0, "$x$", bottom-center
text: 0, 0.5 * x, "$x$", center-left
text: x + 0.5 * x, x, "$x$", bottom-center
text: x + x, x + 0.5 * y, "$y$", center-right
axis: equal
axis: off
:::



:::{plot}
width: 70%
ticks: off
let: x = 2.4
point: (0, 4)
point: (8, 0)
point: (0, x)
point: (x, 0)
point: (4, 2)
line-segment: (0, 4), (8, 0), solid, black
polygon: (x, 0), (0, x), (4, 2), blue, 0.2
text: 0, x, "$P(0, a)$", center-left
text: x, 0, "$Q(a, 0)$", bottom-center
text: 0, 0, "$O$", bottom-left
text: 8, 0, "$B(8, 0)$", bottom-center
text: 0, 4, "$A(0, 4)$", center-left
text: 4, 2, "$M(4, 2)$", top-right
xmin: -1
xmax: 9
ymin: -1
ymax: 5 
:::


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
