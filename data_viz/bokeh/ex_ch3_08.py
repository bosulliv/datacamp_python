# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Select, Button
import numpy as np

# data prep
N = 200
x = np.linspace(0,10,200)
y = np.sin(x) + np.random.random(200)
source = ColumnDataSource(data={'x': x, 'y': y})
plot = figure()
plot.circle('x','y', source=source)

#--- Datacamp exercise code below 

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():
    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)

# bokeh serve --show ex_ch2_08.py