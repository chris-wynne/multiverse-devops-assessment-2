import numpy as np

def identify_duplicate_values(data_array, dup_col_name):
    """
    Summary:
        Identifies duplicate column values by index 
    Args:
        data_array: array to be cleaned
        dup_col_name: name of the column to check for duplicates
    Returns:
        index_to_remove_list: list of indexes to identify rows to remove
    """
    dup_col = find_column_position(data_array, dup_col_name) #finds position of column
    index_col = find_column_position(data_array, "index") #finds position of index column
    data_rows = range(1, len(data_array)) #get number of rows to iterate through
    index_to_remove_list = []
    id_list = []
    for row in data_rows:
        if data_array[row, dup_col] in id_list:
            index_to_remove_list.append(data_array[row, index_col])
        else:
            id_list.append(data_array[row, dup_col]) #only append first indexes and no other duplicates
            
    return index_to_remove_list

def remove_rows(data_array, index_to_remove_list):
    """
    Summary:
        Removes rows by index number based on given index list
    Args:
        data_array: array to be cleaned
        index_to_remove_list: list of indexes to identify rows to remove
    Returns:
        clean_array: data array without specified rows
    """
    index_col = find_column_position(data_array, "index") #finds position of index column
    data_rows = range(1, len(data_array)) #get number of rows to iterate through
    column_names = data_array[0]
    clean_list = [column_names]
    
    for row in data_rows:
        clean_array = []
        if data_array[row, index_col] not in index_to_remove_list:
            clean_list.append(data_array[row])
    clean_array = np.array(clean_list)
    
    return clean_array

def find_column_position(data_array, column_name):
    """   
    Summary:
        Find the position of a specific column name
    Args:
        data_array : array containing column names
        column_name : column value to find position

    Returns:
        col_position: int value and position of column_name
    """#
    column_names = data_array[0].tolist()
    col_position = column_names.index(column_name)
    return col_position

def capitalise_column_values(data_array, col_to_capitalise):
    """   
    Summary:
        Capitalises the values of specified column, excluding the headers.
    Args:
        data_array : array containing columns to be capitalised
        col_to_capitalise : column where values should be capitalised

    Returns:
        capitalised_data_array : returns data_array but with capitalised values in specified column
    """
    index_col = find_column_position(data_array, "index") #finds position of index column
    col_to_capitalise_pos = find_column_position(data_array, col_to_capitalise) #finds position of column to capitalise
    column_names = data_array[0]

    data_array_without_headers = np.delete(data_array, (0), axis=0)
    data_array_transposed = np.transpose(data_array_without_headers)
    data_array_transposed[col_to_capitalise_pos] = np.char.capitalize(data_array_transposed[col_to_capitalise_pos]) #capitalise specific row
    
    capitalised_array_headers = [column_names]
    capitalised_array = np.transpose(data_array_transposed)
    capitalised_data_array = np.concatenate((capitalised_array_headers, capitalised_array), axis=0)
    
    return capitalised_data_array

def identify_invalid_score(data_array, column_name):
    """
    Summary:
        Identifies rows where score is not 1 - 10 based on index column.
    Args:
        data_array : array containing columns to be validated
        column_name : column where values should be validated

    Returns:
        index_to_remove_list: list of indexes to identify rows to remove
    """
    index_col = find_column_position(data_array, "index") #finds position of index column
    a3_col = find_column_position(data_array, column_name) #finds position of column_name
    data_rows = range(1, len(data_array)) #get number of rows to iterate through
    
    index_to_remove_list = []
    valid_range = range(1,10)
    for row in data_rows:
        if int(data_array[row, a3_col]) not in valid_range:
            index_to_remove_list.append(data_array[row, index_col])
    
    return index_to_remove_list

def drop_index(data_array):
    """
    Summary:
        Locates and removes index column within data array
    Args:
        data_array : array with index column for removal
    Returns:
        clean_array : data array without index column
    """
    index_col = int(find_column_position(data_array, "index")) #finds position of index column
    clean_array = np.delete(data_array, index_col, axis=1)
    return clean_array