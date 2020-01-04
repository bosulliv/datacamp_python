import matplotlib.pyplot as plt
import numpy as np


def get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title):
    x_array_ndim = x_array.ndim
    if not x_array_ndim == 1:
        msg = "Argument x_array should be 1 dimensional. "
        msg += "It actually is {0} dimensional"
        raise ValueError(msg.format(x_array_ndim))
    y_array_ndim = y_array.ndim
    if not y_array_ndim == 1:
        msg = "Argument y_array should be 1 dimensional. "
        msg += "It actually is {0} dimensional"
        raise ValueError(msg.format(y_array_ndim))
    x_array_length = x_array.shape[0]
    y_array_length = y_array.shape[0]
    if x_array_length != y_array_length:
        msg = "Arguments x_array and y_array should have same length. "
        msg += "But x_array has length {0} and y_array has length {1}"
        raise RuntimeError(msg.format(x_array_length,y_array_length))
    fig, ax = plt.subplots()
    ax.plot(x_array, y_array, ".")
    ax.plot([0, np.max(x_array)], [intercept, slope * np.max(x_array) + intercept], "-")
    ax.set(xlabel="area (square feet)", ylabel="price (dollars)", title=title)
    return fig
