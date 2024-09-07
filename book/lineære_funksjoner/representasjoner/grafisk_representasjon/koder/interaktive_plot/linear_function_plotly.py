import plotly.graph_objects as go
import numpy as np

# Define your data
x = np.linspace(-10, 10, 100)
slope = 1
intercept = 0
y = slope * x + intercept

# Create your Plotly figure
fig = go.Figure(
    data=go.Scatter(x=x, y=y, mode="lines", name=f"y = {slope}x + {intercept}")
)
fig.update_layout(title="Linear Function", xaxis_title="x", yaxis_title="y")

# Export the plot as a static HTML file
fig.write_html("../../figurer/interaktive_plot/linear_function.html")
