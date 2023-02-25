import csv

def get_input(fpath):
    """
    Summary:
        Imports csv file and returns array
    Args:
        fpath: full path of desired import file
    Returns:
        data_file: imported file
    """
    with open(fpath, newline='') as csvfile:
        data_file = list(csv.reader(csvfile)) 
    
    return data_file