from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import Slider, CustomJS, Label, SingleIntervalTicker, HoverTool, ColumnDataSource
from bokeh.models.formatters import NumeralTickFormatter
import numpy as np

# Generate x-axis data
x = np.linspace(-10, 11, 1024)

x_min = -8.5
x_max = 8.3
y_min = -8.5
y_max = 8.3

# Set up the initial plot
p = figure(title=r"Gjennomsnittlig og momentan vekstfart",
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
a, b, c = 1, 0, -2
line = p.line(x, [a * xi**2 + b * xi + c for xi in x], line_width=3, line_color="teal")

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

# Create sliders for points
slider_x1 = Slider(start=-10, end=10, value=0, step=1, title=r"$$x_1$$")
slider_x2 = Slider(start=-10, end=10, value=1, step=0.01, title=r"$$x_2$$")

# Add secant line
x1 = slider_x1.value
x2 = slider_x2.value
y1 = a * x1**2 + b * x1 + c
y2 = a * x2**2 + b * x2 + c
stigningstall = (y2 - y1) / (x2 - x1)
konstantledd = y1 - stigningstall * x1
secant = p.line(x, [stigningstall * xi + konstantledd for xi in x], line_width=3, line_color="blue")

# Add points (x1, y1) and (x2, y2)
source_points = ColumnDataSource(data=dict(x=[x1, x2], y=[y1, y2]))
points = p.scatter('x', 'y', source=source_points, size=8, color="blue")

tangent_slope = 2 * a * x1 + b
tangent_intercept = y1 - tangent_slope * x1
tangent = p.line(x, [tangent_slope * x_i + tangent_intercept for x_i in x], line_width=3, line_color="purple")

# Add labels for points
label_x1 = Label(x=x1, y=y1, text=f"({x1}, {y1})", text_font_size="14pt", text_color="blue", x_offset=5, y_offset=5)
label_x2 = Label(x=x2, y=y2, text=f"({x2}, {y2})", text_font_size="14pt", text_color="blue", x_offset=5, y_offset=5)
p.add_layout(label_x1)
p.add_layout(label_x2)

# Add label for slope of the secant
slope_label = Label(x=2, y=-5, text=f"Gjennomsnittlig vekstfart = {stigningstall:.2f}", 
                    text_font_size="14pt", text_color="black")
p.add_layout(slope_label)

tangent_slope_label = Label(x=2, y=-7, text=f"Momentan vekstfart = {tangent_slope:.2f}",
                            text_font_size="14pt", text_color="black")
p.add_layout(tangent_slope_label)


# JavaScript callback for updating the plot
callback = CustomJS(args=dict(line=p.renderers[0], secant=secant, tangent=tangent, slider_x1=slider_x1, slider_x2=slider_x2,
                              source_points=source_points, label_x1=label_x1, label_x2=label_x2, slope_label=slope_label, tangent_slope_label=tangent_slope_label),
                    code="""
    const data = line.data_source.data;
    const A = 1;
    const B = 0;
    const C = -2;
    const x = data['x'];
    const y = data['y'];
    for (let i = 0; i < x.length; i++) {
        y[i] = A * x[i]**2 + B * x[i] + C;
    }
    line.data_source.change.emit();

    

    // Update secant line
    const x1 = slider_x1.value;
    const x2 = slider_x2.value;
    const y1 = A * x1**2 + B * x1 + C;
    const y2 = A * x2**2 + B * x2 + C;
    const y_secant = secant.data_source.data['y'];
    const stigningstall = (y2 - y1) / (x2 - x1);
    const konstantledd = y1 - stigningstall * x1;
    for (let i = 0; i < x.length; i++) {
        y_secant[i] = stigningstall * x[i] + konstantledd;
    }
    
    secant.data_source.change.emit();


    //Update tangent line
    const tangent_slope = 2 * A * x1 + B;
    const tangent_intercept = y1 - tangent_slope * x1;
    const y_tangent = tangent.data_source.data['y'];
    for (let i = 0; i < x.length; i++) {
        y_tangent[i] = tangent_slope * x[i] + tangent_intercept;
    }
    tangent.data_source.change.emit();

    // Update points
    const source = source_points.data;
    source['x'] = [x1, x2];
    source['y'] = [y1, y2];
    source_points.change.emit();


    // Update labels
    label_x1.x = x1;
    label_x1.y = y1;
    label_x1.text = `(${x1.toFixed(2)}, ${y1.toFixed(2)})`;

    label_x2.x = x2;
    label_x2.y = y2;
    label_x2.text = `(${x2.toFixed(2)}, ${y2.toFixed(2)})`;

    // Update secant slope label
    slope_label.text = `Gjennomsnittlig vekstfart = ${stigningstall.toFixed(2)}`;

    // Update tangent slope label
    tangent_slope_label.text = `Momentan vekstfart = ${tangent_slope.toFixed(2)}`;
""")

slider_x1.js_on_change('value', callback)
slider_x2.js_on_change('value', callback)


# Organize layout and output
layout = column(p, slider_x1, slider_x2)
output_file("../figurer/gjennomsnittlig_vs_momentan_vekstfart.html")
save(layout)