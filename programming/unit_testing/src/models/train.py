import numpy as np

def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        msg = "Argument data_array must be two dimensional. "
        msg += "Got {0} dimensional array instead!"
        raise ValueError(msg.format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        msg = "Argument data_array must have at least 2 rows, "
        msg += "it actually has just {0}"
        raise ValueError(msg.format(num_rows))
    num_training = int(0.75 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]
