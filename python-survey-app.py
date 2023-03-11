import numpy as np
from scripts.import_data import get_input
from scripts.clean_data import identify_duplicate_values, remove_rows, capitalise_column_values, identify_invalid_score

fpath = r"data/results.csv"

dataset = get_input(fpath) #import dataset

duplicate_index_list = identify_duplicate_values(dataset, "user_id")
invalid_a3_index_list = identify_invalid_score(dataset, "answer_3")
clean_array = remove_rows(dataset, duplicate_index_list)
clean_array = remove_rows(clean_array, invalid_a3_index_list)

#capitalise name columns
clean_array = capitalise_column_values(clean_array, "first_name")
clean_array = capitalise_column_values(clean_array, "last_name")

print(clean_array)