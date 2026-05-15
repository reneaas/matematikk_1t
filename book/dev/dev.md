# Dev


:::{plot}
width: 70%
axis: off
axis: equal
let: l = 2
let: r = 0.2
line-segment: (0, 0), (0, -l), gray, solid
circle: (0, -(l + r)), r, fill, red
line-segment: (-2 * r, 0), (-2 * r, -l), gray, solid
circle: (-2 * r, -(l + r)), r, fill, blue
line-segment: (-2*r, 0), (-2*r - l + r, 0), gray, dashed
circle: (-r*2 - l, 0), r, fill, blue, dashed
angle-arc: (-2*r, -r), l, 180 + 2, 270 - 7, gray, dashdot
line-segment: (-2*r, 0), (4*r, 0), gray, solid
vector: (-2*r - l, -2*r), (-2 * r - l, -4 * r), gray
nocache:
:::


:::{plot}
width: 70%
axis: off
axis: equal
let: s = 1
let: S = 2
let: L = 8
let: d = 4
line-segment: (-2 * s, 0), (L, 0), gray, solid
polygon: (-s, 0), (s, 0), (s, s), (-s, s), blue, 0.2
polygon: (d - S, 0), (d + S, 0), (d + S, S), (d - S, S), red, 0.2
text: 0, 0.5 * s, "$m$", center-center
text: d, 0.5 * S, "$3m$", center-center
line-segment: (s, 0.5 * s), (d - S, 0.5 * s), black, solid
vector: (d + S, 0.5 * S), (d + S + 2, 0.5 * S), black
text: 0.5 * (d + S + d + S + 2), 0.5 * S, "$\vec{F}$", top-center
:::

