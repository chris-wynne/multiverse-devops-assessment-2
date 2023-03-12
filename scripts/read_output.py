from scripts.import_data import get_input
from scripts.clean_data import drop_index

def read_output(fpath):
    """
    Summary:
        Imports csv file using get_input and drops an index column if it exists.
    Args:
        fpath: full path of desired import file
    """
    data_array = get_input(fpath) #uses existing module to import csv data
    
    if "index" in data_array[0]:
        data_array = drop_index(data_array) #drops the new index column used for processing
    
    return data_array
    
    
def print_output(data_array):        
    """
    Summary:
        Prints data array line by line with a fixed string format
    Args:
        data_array : data_array to print
    """
    col_num = len(data_array[0]) #get number of columns
    
    format_string = "{: >20} " #string format for each column
    format_string_full = " ".join((format_string,) * col_num) #concatenate string to itself
    
    for row in data_array:
        print(format_string_full.format(*row)) #format print output