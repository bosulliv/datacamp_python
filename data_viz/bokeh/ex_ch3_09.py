# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Select, Button
import numpy as np

#--- Datacamp exercise code below 

# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.models import CheckboxGroup, RadioGroup, Toggle

# Add a Toggle: toggle
toggle = Toggle(label='Toggle button', button_type='success')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))

# bokeh serve --show ex_ch2_09.py