import numpy as np
import plotly.graph_objects as go

# Generate x-values
x = np.linspace(-10, 10, 100)

# Initial values for slope (a) and intercept (b)
initial_a = 1
initial_b = 0
y = initial_a * x + initial_b

# Create the figure
fig = go.Figure()

# Add the linear function trace with initial values
fig.add_trace(
    go.Scatter(x=x, y=y, mode="lines", name=f"y = {initial_a}x + {initial_b}")
)

# Add x-axis and y-axis lines
fig.add_trace(
    go.Scatter(
        x=[-11, 11],
        y=[0, 0],
        mode="lines",
        line=dict(color="black", width=2),
        showlegend=False,
    )
)
fig.add_trace(
    go.Scatter(
        x=[0, 0],
        y=[-11, 11],
        mode="lines",
        line=dict(color="black", width=2),
        showlegend=False,
    )
)

# Arrow annotations for the axis
fig.add_annotation(
    x=10,
    y=0,
    axref="x",
    ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowwidth=2,
    ax=9.5,
    ay=0,
)
fig.add_annotation(
    x=0,
    y=10,
    axref="x",
    ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowwidth=2,
    ax=0,
    ay=9.5,
)

# Create the slider for slope (a) and intercept (b)
sliders = [
    {
        "active": 0,
        "currentvalue": {"prefix": "Slope (a): "},
        "pad": {"t": 50},
        "steps": [
            {
                "label": f"{a}",
                "method": "update",
                "args": [
                    {"y": [a * x + initial_b]},  # Update y values
                    {
                        "annotations": [
                            dict(
                                x=10,
                                y=0,
                                axref="x",
                                ayref="y",
                                showarrow=True,
                                arrowhead=2,
                                arrowwidth=2,
                                ax=9.5,
                                ay=0,
                            ),
                            dict(
                                x=0,
                                y=10,
                                axref="x",
                                ayref="y",
                                showarrow=True,
                                arrowhead=2,
                                arrowwidth=2,
                                ax=0,
                                ay=9.5,
                            ),
                        ],
                        "title": f"Linear Function: y = {a}x + {initial_b}",
                    },
                ],
            }
            for a in np.linspace(-10, 10, 21)
        ],
    },
    {
        "active": 0,
        "currentvalue": {"prefix": "Intercept (b): "},
        "pad": {"t": 100},
        "steps": [
            {
                "label": f"{b}",
                "method": "update",
                "args": [
                    {"y": [initial_a * x + b]},  # Update y values
                    {
                        "annotations": [
                            dict(
                                x=10,
                                y=0,
                                axref="x",
                                ayref="y",
                                showarrow=True,
                                arrowhead=2,
                                arrowwidth=2,
                                ax=9.5,
                                ay=0,
                            ),
                            dict(
                                x=0,
                                y=10,
                                axref="x",
                                ayref="y",
                                showarrow=True,
                                arrowhead=2,
                                arrowwidth=2,
                                ax=0,
                                ay=9.5,
                            ),
                        ],
                        "title": f"Linear Function: y = {initial_a}x + {b}",
                    },
                ],
            }
            for b in np.linspace(-10, 10, 21)
        ],
    },
]


# Add arrowhead annotations for x-axis and y-axis
fig.add_annotation(
    x=11.2,
    y=0,  # Arrow for x-axis
    axref="x",
    ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="black",
    ax=9.5,
    ay=0,
)

fig.add_annotation(
    x=0,
    y=11.2,  # Arrow for y-axis
    axref="x",
    ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="black",
    ax=0,
    ay=9.5,
)


# Update the layout
fig.update_layout(
    sliders=sliders,
    xaxis=dict(
        showline=False,
        zeroline=False,
        showgrid=False,
        range=[-11, 11],
        showticklabels=False,
    ),
    yaxis=dict(
        showline=False,
        zeroline=False,
        showgrid=False,
        range=[-11, 11],
        showticklabels=False,
    ),
    plot_bgcolor="white",
    showlegend=False,
)

# Display the figure
fig.show()


# Export the plot as a static HTML file
# fig.write_html("../../figurer/interaktive_plot/linear_function.html")
