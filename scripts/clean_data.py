import numpy as np

def identify_duplicate_values(data_array, dup_col, index_col):
    """
    Summary:

    Args:
        data_array: array to be cleaned
        dup_col: position of the column to check for duplicates
        index_col : position of index column required for recording duplicates to remove
    Returns:
        index_to_remove_list: list of indexes to identify rows to remove
    """
    data_rows = range(1, len(data_array)) #get number of rows to iterate through
    index_to_remove_list = []
    id_list = []
    for row in data_rows:
        if data_array[row, dup_col] in id_list:
            index_to_remove_list.append(data_array[row, index_col])
        else:
            id_list.append(data_array[row, dup_col])
            
    return index_to_remove_list