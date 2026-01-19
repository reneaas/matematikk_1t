# Test Endpoint Markers with Division by Zero

This tests that endpoint markers are drawn correctly even when the function divides by zero at the endpoint.

## Test Case 1: Endpoint at singularity

The function $(x^2 - 4) / (x^2 - x - 6)$ has singularities at $x = -2$ and $x = 3$.

When we split the domain at $x = -2$, the endpoint markers should still be drawn:

:::{plot}
width: 60%
function: (x**2 - 4) / (x**2 - x - 6), f, (-20, -2), blue
function: (x**2 - 4) / (x**2 - x - 6), (-2, 20), blue
function-endpoints: true
vline: 3
vline: -2
hline: 1
xmin: -10
xmax: 10
ymin: -5
ymax: 5
:::

## Test Case 2: Endpoint slightly away from singularity (for comparison)

:::{plot}
width: 60%
function: (x**2 - 4) / (x**2 - x - 6), f, (-20, -2.1), blue
function: (x**2 - 4) / (x**2 - x - 6), (-1.9, 20), blue
function-endpoints: true
vline: 3
vline: -2
hline: 1
xmin: -10
xmax: 10
ymin: -5
ymax: 5
:::
