import plotly.graph_objs as go
import numpy as np

# Generate data for the line
def generate_data(a, b):
    x = np.linspace(-10, 10, 400)
    y = a * x + b
    return x, y

# Initial values for a and b
a_initial, b_initial = 1, 0
x_initial, y_initial = generate_data(a_initial, b_initial)

# Create the figure
fig = go.Figure()

# Add trace for the linear function
fig.add_trace(go.Scatter(x=x_initial, y=y_initial, mode='lines', name='Linear Function'))

# Update layout for a centered axis cross with arrows
fig.update_layout(
    xaxis=dict(
        zeroline=True,
        showline=True,
        showticklabels=True,
        ticks="outside",
        tickvals=[-10, -5, 0, 5, 10],
        zerolinecolor='black',
        zerolinewidth=2,
        range=[-10, 10],
        linecolor='black'
    ),
    yaxis=dict(
        zeroline=True,
        showline=True,
        showticklabels=True,
        ticks="outside",
        tickvals=[-10, -5, 0, 5, 10],
        zerolinecolor='black',
        zerolinewidth=2,
        range=[-10, 10],
        linecolor='black'
    ),
    plot_bgcolor='white',
    sliders=[
        {
            'pad': {"t": 50},
            'len': 0.5,
            'x': 0.25,
            'y': 0,
            'currentvalue': {"visible": True, "prefix": "Slope (a): "},
            'steps': [{'method': 'relayout', 'label': str(a), 'args': [{'yaxis.range': [-10*a, 10*a]}]} for a in np.linspace(-10, 10, 21)]
        },
        {
            'pad': {"t": 50},
            'len': 0.5,
            'x': 0.75,
            'y': 0,
            'currentvalue': {"visible": True, "prefix": "Intercept (b): "},
            'steps': [{'method': 'relayout', 'label': str(b), 'args': [{'yaxis.range': [b-10, b+10]}]} for b in np.linspace(-20, 20, 21)]
        }
    ],
    autosize=False,
    width=500,
    height=500,
    margin=dict(l=20, r=20, t=50, b=20),
    annotations=[
        dict(x=0, y=1.1, xref="paper", yref="paper", showarrow=True, arrowhead=1, ax=0, ay=-40),
        dict(x=1.1, y=0, xref="paper", yref="paper", showarrow=True, arrowhead=1, ax=-40, ay=0)
    ]
)

# Decouple the parameters
fig.update_traces(mode='lines')

# Save to HTML
fig.write_html("../../figurer/interaktive_plot/skrå_linjer_interaktiv_plotly.html")