import numpy as np
from scripts.import_data import get_input
from scripts.clean_data import identify_duplicate_values, remove_duplicates



fpath = r"data/results.csv"

dataset = get_input(fpath) #import dataset
data_array = dataset
index_col_position = len(dataset[0])-1 #set position of index column (last column)

duplicate_index_list = identify_duplicate_values(dataset, 0, index_col_position)
clean_array = remove_duplicates(dataset, index_col_position, duplicate_index_list)

print(clean_array)