import csv
import numpy as np

def get_input(fpath):
    """
    Summary:
        Imports csv file, ignored blank rows and returns array
    Args:
        fpath: full path of desired import file
    Returns:
        data_array: imported file as a numpy array
    """
    data_file = []
    #import csv data ignoring blank rows
    with open(fpath, newline='') as csvfile:
        csv_data = list(csv.reader(csvfile))
        #append valid rows to data_file and skip blank rows
        for row in csv_data:
            if any(x.strip() for x in row):
                data_file.append(row)
            
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
    array_with_indices[0,index_col_position] = "index" #change column name to index
    
    return array_with_indices

def save_output(clean_array, output_path):
    """
    Summary:
        Saves data array to a csv file
    Args:
        clean_array : Cleaned data array ready to be saved
        output_path : filepath for saving output
    """
    with open(output_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(clean_array)