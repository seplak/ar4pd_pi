import pandas as pd
import numpy as np
from numpy.lib.stride_tricks import as_strided
def load_file(filepath):
    dataframe = pd.read_csv(filepath, delim_whitespace=True)
    part_of_experiment = dataframe['annotation'] != 0
    cleaned_dataframe = dataframe[part_of_experiment]
    cleaned_dataframe['time'] = pd.to_datetime(cleaned_dataframe['time'], unit='ms')
    return cleaned_dataframe


def windowed_view(arr, window, overlap):
    arr = np.asarray(arr)
    window_step = window - overlap
    new_shape = arr.shape[:-1] + ((arr.shape[-1] - overlap) // window_step,
                                  window)
    new_strides = (arr.strides[:-1] + (window_step * arr.strides[-1],) +
                   arr.strides[-1:])
    return as_strided(arr, shape=new_shape, strides=new_strides)




