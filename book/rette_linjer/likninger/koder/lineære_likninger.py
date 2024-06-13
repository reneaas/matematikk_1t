from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import Slider, CustomJS, Label, SingleIntervalTicker, HoverTool
from bokeh.models.formatters import NumeralTickFormatter
from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import Slider, CustomJS, Label, SingleIntervalTicker, HoverTool
from bokeh.models.formatters import NumeralTickFormatter
from bokeh.models.sources import ColumnDataSource


# Generate x-axis data
x = [i for i in range(-10, 11)]

x_min = -5
x_max = 5
y_min = -5
y_max = 5


a = 2
b = 3
k = 0

# Set up the initial plot
p = figure(title=f"2x + 3 = k",
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
line_source = ColumnDataSource(data={'x': x, 'y': [2 * xi + 3 for xi in x]})
line = p.line('x', 'y', source=line_source, line_width=3, line_color="#008080")

# Line for y = k
k_line_source = ColumnDataSource(data={'x': x, 'y': [0 for _ in x]})
y_const_line = p.line('x', 'y', source=k_line_source, line_width=3, line_color="#0000FF")



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

# Create slider for k
slider_k = Slider(start=-4, end=5, value=0, step=0.25, title="k")

# JavaScript callback for updating the plot
callback = CustomJS(args=dict(line_source=line_source, k_line_source=k_line_source, slider_k=slider_k), code="""
    const k = slider_k.value;
    const k_data = k_line_source.data;
    const y_const_line = k_data['y'];
    for (let i = 0; i < y_const_line.length; i++) {
        y_const_line[i] = k;
    }
    k_line_source.change.emit();
""")
slider_k.js_on_change('value', callback)

slider_k.js_on_change('value', callback)

# Organize layout and output
layout = column(p, slider_k)
output_file("../figurer/interaktive_plot/lineær_likning_med_variabel_høyre_side.html")
save(layout)