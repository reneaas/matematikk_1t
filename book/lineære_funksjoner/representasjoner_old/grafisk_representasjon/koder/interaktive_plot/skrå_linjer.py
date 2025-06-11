from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import Slider, CustomJS, Label, SingleIntervalTicker, HoverTool
from bokeh.models.formatters import NumeralTickFormatter

# Generate x-axis data
x = [i for i in range(-10, 11)]

x_min = -5
x_max = 5
y_min = -5
y_max = 5


# Set up the initial plot
p = figure(title="y = ax + b",
           x_range=(x_min, x_max + 0.5), y_range=(y_min, y_max + 0.5),
           width=700, height=500,
           toolbar_location=None)

# Enhance aesthetics: font, title, and colors
p.title.align = 'center'
p.title.text_font_size = '16pt'
p.title.text_color = "navy"

# Set up tickers for a fixed interval of 1
x_ticker = SingleIntervalTicker(interval=1)
y_ticker = SingleIntervalTicker(interval=1)
p.xaxis.ticker = x_ticker
p.yaxis.ticker = y_ticker

# Configure major tick formatting
p.xaxis.formatter = NumeralTickFormatter(format="0")
p.yaxis.formatter = NumeralTickFormatter(format="0")

# Add labels to the axes
x_label = Label(x=x_max, y=-1, text='x', text_font_size="16pt", text_align="center")
y_label = Label(x=-0.5, y=y_max, text='y', text_font_size="16pt", text_align="center")
p.add_layout(x_label)
p.add_layout(y_label)

# Move axes to the center
p.xaxis.fixed_location = 0
p.yaxis.fixed_location = 0

# Styling lines and axes
line = p.line(x, [1 * xi + 0 for xi in x], line_width=3, line_color="#008080")

# Hover tool
hover = HoverTool(tooltips=[('x', '$x'), ('y', '$y')], mode='vline')
p.add_tools(hover)

# Configure grid lines
p.xgrid.grid_line_color = "#D3D3D3"
p.ygrid.grid_line_color = "#D3D3D3"
p.xgrid.grid_line_dash = "dashed"
p.ygrid.grid_line_dash = "dashed"

# Remove plot border
p.outline_line_color = None

# Styling axes ticks and labels
p.axis.major_label_text_font_size = "12pt"
p.axis.major_label_text_color = "black"
p.axis.axis_line_color = "black"
p.axis.major_tick_line_color = "black"
p.axis.minor_tick_line_color = "black"

# Create sliders for slope and intercept
slider_a = Slider(start=-10, end=10, value=1, step=0.5, title="Stigningstall")
slider_b = Slider(start=-10, end=10, value=0, step=1, title="Konstantledd")

# JavaScript callback for updating the plot
callback = CustomJS(args=dict(line=p.renderers[0], slider_a=slider_a, slider_b=slider_b), code="""
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
output_file("../../figurer/interaktive_plot/skrå_linjer_interaktiv.html")
save(layout)