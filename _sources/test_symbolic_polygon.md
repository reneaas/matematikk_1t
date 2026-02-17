# Test Symbolic Evaluation in Polygons

Let's test if we can use function evaluation in polygon coordinates:

```{plot}
functions: f(x) = x**2
polygon: (0, 0), (2, 0), (2, f(2)), (0, f(2))
```

This should create a rectangle where the top side is at height f(2) = 4.