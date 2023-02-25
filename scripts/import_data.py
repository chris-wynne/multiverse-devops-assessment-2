import csv
import numpy as np

def get_input(fpath):
    """
    Summary:
        Imports csv file and returns array
    Args:
        fpath: full path of desired import file
        data_file: list of rows from import file
    Returns:
        data_array: imported file as a numpy array
    """
    with open(fpath, newline='') as csvfile:
        data_file = list(csv.reader(csvfile))
    
    #convert to numpy array
    data_array = np.array(data_file)
    
    #add index
    data_array = add_index(data_array)
     
    return data_array

def add_index(data_array):
    """
    Summary:
        Adds an index column to an existing array
    Args:
        data_array: existing array you want to add an index to
    Returns:
        array_with_indices: returns original array with a index column
    """
    index = np.arange(data_array.shape[0])
    index_col_position = len(data_array[0])
    
    array_with_indices = np.c_[data_array, index]
    array_with_indices[0,index_col_position] = "index"
    
    return array_with_indices