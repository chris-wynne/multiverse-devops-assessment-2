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
     
    return data_array

def remove_duplicate_ids(data_file):
    pass