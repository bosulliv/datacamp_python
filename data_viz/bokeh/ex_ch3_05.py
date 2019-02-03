# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
import numpy as np

# data prep
x = np.linspace(0.3, 10, 300)
y = np.sin(1/x)

slider = Slider(title='slider', start=1, end=10, step=1, value=1)
plot = figure()

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y': y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# <Datacamp exercise code below>

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)

# bokeh serve --show ex_ch2_05.py