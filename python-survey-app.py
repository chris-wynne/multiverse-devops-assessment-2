import numpy as np
from scripts.import_data import get_input
from scripts.clean_data import identify_duplicate_values, remove_duplicates, capitalise_column_values

fpath = r"data/results.csv"

dataset = get_input(fpath) #import dataset

duplicate_index_list = identify_duplicate_values(dataset, "user_id")
clean_array = remove_duplicates(dataset, duplicate_index_list)

#capitalise name columns
clean_array = capitalise_column_values(clean_array, "first_name")
clean_array = capitalise_column_values(clean_array, "last_name")

print(clean_array)