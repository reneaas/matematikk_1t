from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import Slider, CustomJS

# Generate x-axis data
x = [i for i in range(-100, 101)]

# Set up the initial plot
p = figure(title="Interactive Linear Function: f(x) = ax + b",
           x_axis_label='x', y_axis_label='f(x)',
           x_range=(-100, 100), y_range=(-100, 100),
           width=500, height=500)

# Move axes to the center
p.xaxis.fixed_location = 0
p.yaxis.fixed_location = 0

# Remove grid lines
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# Add line glyph
line = p.line(x, [1 * xi + 0 for xi in x], line_width=3, line_color="red")

# Create sliders for slope and intercept
slider_a = Slider(start=-10, end=10, value=1, step=0.1, title="Slope (a)")
slider_b = Slider(start=-100, end=100, value=0, step=1, new_title="Intercept (b)")

# JavaScript callback for updating the plot
callback = CustomJS(args=dict(line=line, slider_a=slider_a, slider_b=slider_b), code="""
    const data = line.data_source.data;
    const A = slider_a.value;
    const B = slider_b.value;
    const x = data['x'];
    const y = data['y'];
    for (let i = 0; i < x.length; i++) {
        y[i] = A * x[i] + B;
    }
    line.data_source.change.emit();
""")

slider_a.js_on_change('value', callback)
slider_b.js_on_change('value', callback)

# Organize layout and output
layout = column(p, slider_a, slider_b)
output_file("interactive_linear_function.html")
save(layout)